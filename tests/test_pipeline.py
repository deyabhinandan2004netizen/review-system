import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient
from backend.main import app
from backend.aggregator import price_aggregator

from backend.review_detector import review_detector
from backend.absa_engine import absa_engine
from backend.visual_matcher import visual_matcher
from backend.schemas import ReviewItem, PriceAlertRequest
from backend.history_tracker import history_tracker

client = TestClient(app)

# ==========================================
# 1. Price Aggregator Tests
# ==========================================

def test_price_aggregator_preset_and_generic():
    # Test catalog preset
    res = price_aggregator.search_and_compare("Sony WH-1000XM5")
    assert res.product_name == "Sony WH-1000XM5 Wireless Noise-Canceling Headphones"
    assert len(res.offers) == 5
    assert res.lowest_price <= res.highest_price
    assert any(o.is_best_deal for o in res.offers)
    assert res.potential_savings >= 0

    # Test generic search query
    res2 = price_aggregator.search_and_compare("Smart Watch OLED")
    assert len(res2.offers) == 5
    assert res2.lowest_price > 0

# ==========================================
# 2. 2-Tier Fake Review & Bot Detection Tests
# ==========================================

def test_levenshtein_similarity():
    s1 = "This is a great product loved it"
    s2 = "This is a great product loved it!"
    sim = review_detector.calculate_similarity(s1, s2)
    assert sim >= 0.90

def test_bot_detection_and_trust_score():
    reviews = [
        ReviewItem(
            id="1", author="Real Buyer", rating=5.0, date="2024-05-01",
            text="The active noise cancelling is top notch and sound quality is clear.",
            verified_purchase=True, platform="Amazon"
        ),
        ReviewItem(
            id="2", author="Bot 1", rating=5.0, date="2024-05-10",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! 5 stars all the way!!!!!!",
            verified_purchase=False, platform="Amazon"
        ),
        ReviewItem(
            id="3", author="Bot 2", rating=5.0, date="2024-05-10",
            text="THIS IS A GAME CHANGER AND A TESTAMENT TO INNOVATION! 5 stars all the way!!!!!!",
            verified_purchase=False, platform="Walmart"
        ),
        ReviewItem(
            id="4", author="Critical User", rating=5.0, date="2024-05-12",
            text="terrible horrible defective waste of money broke immediately",
            verified_purchase=False, platform="Flipkart"
        )
    ]

    analysis = review_detector.analyze_reviews("Test Audio Device", reviews)
    assert analysis.total_reviews == 4
    assert analysis.bot_reviews_count >= 2 # Bot 1 & Bot 2 duplicate templates + rating mismatch
    assert analysis.trust_score < 100.0
    assert analysis.adjusted_rating <= analysis.original_rating

# ==========================================
# 3. ABSA Engine Tests
# ==========================================

def test_absa_engine():
    reviews = [
        ReviewItem(
            id="1", author="Alex", rating=5.0, date="2024-05-01",
            text="Solid aluminum build quality and very comfortable design. Battery lasts over 30 hours of continuous music.",
            verified_purchase=True, platform="Amazon"
        ),
        ReviewItem(
            id="2", author="Sam", rating=4.0, date="2024-05-02",
            text="A bit overpriced for the specs, but sound performance is crystal clear and bass is deep.",
            verified_purchase=True, platform="Flipkart"
        )
    ]

    aspects = absa_engine.analyze_aspects(reviews)
    aspect_names = [a.aspect for a in aspects]
    assert "Build Quality & Design" in aspect_names
    assert "Performance & Speed" in aspect_names
    assert "Value for Money" in aspect_names
    
    # Check that sum of percentages is close to 100
    for a in aspects:
        assert 90 <= (a.positive_score + a.neutral_score + a.negative_score) <= 101

# ==========================================
# 4. Visual Search & Feature Matching Tests
# ==========================================

def test_visual_matcher():
    # URL keyword test
    res = visual_matcher.match_image(image_url="https://example.com/macbook-laptop.png")
    assert "MacBook" in res.detected_object or "Laptop" in res.detected_object
    assert len(res.matched_products) > 0

# ==========================================
# 5. Price History & Alerts Tests
# ==========================================

def test_history_tracker_and_alert():
    hist = history_tracker.get_price_history("Sony WH-1000XM5", 28490.0, days=90)
    assert len(hist.history) > 0
    assert hist.lowest_historical <= hist.highest_historical

    alert_req = PriceAlertRequest(
        product_name="Sony WH-1000XM5",
        target_price=25000.0,
        email="test@example.com",
        current_price=28490.0
    )
    alert_res = history_tracker.create_price_alert(alert_req)
    assert alert_res.status == "SUCCESS"
    assert "ALT-" in alert_res.alert_id

# ==========================================
# 6. FastAPI Endpoints Integration Tests
# ==========================================

def test_api_routes():
    # Health
    r_health = client.get("/api/health")
    assert r_health.status_code == 200
    assert r_health.json()["status"] == "ok"

    # Search
    r_search = client.post("/api/search", json={"query": "MacBook Air M3", "search_type": "keyword"})
    assert r_search.status_code == 200
    data = r_search.json()
    assert "Apple MacBook Air" in data["product_name"]

    # Price Compare GET
    r_compare = client.get("/api/price-compare?q=iPhone 15 Pro")
    assert r_compare.status_code == 200
    assert len(r_compare.json()["offers"]) == 5

    # Analyze Reviews
    r_rev = client.post("/api/analyze-reviews?product_name=Sony WH-1000XM5")
    assert r_rev.status_code == 200
    rev_data = r_rev.json()
    assert "trust_score" in rev_data
    assert "adjusted_rating" in rev_data
    assert len(rev_data["aspect_analysis"]) > 0

    # Price History
    r_hist = client.get("/api/price-history?product_name=Sony WH-1000XM5&current_price=28490&days=90")
    assert r_hist.status_code == 200
    assert "price_recommendation" in r_hist.json()

    # Web Dashboard HTML
    r_home = client.get("/")
    assert r_home.status_code == 200
    assert "VeriPrice" in r_home.text

def test_amazon_url_extraction_and_reviews():
    # Test Amazon URL via /api/search
    amazon_url = "https://www.amazon.in/boAt-Airdopes-141/dp/B09N3ZNHTY"
    r_search = client.post("/api/search", json={"query": amazon_url, "search_type": "keyword"})
    assert r_search.status_code == 200
    search_data = r_search.json()
    assert len(search_data["product_name"]) > 3
    assert search_data["lowest_price"] > 0
    assert len(search_data["offers"]) == 5
    
    # Test Amazon URL directly passed to /api/analyze-reviews
    r_rev = client.post(f"/api/analyze-reviews?product_name={amazon_url}")
    assert r_rev.status_code == 200
    rev_data = r_rev.json()
    assert rev_data["total_reviews"] >= 10
    assert rev_data["authentic_reviews_count"] > 0
    assert rev_data["bot_reviews_count"] > 0
    assert "trust_score" in rev_data

    # Test complex sponsored tracking Amazon URL (user's exact URL)
    sponsored_url = "https://www.amazon.in/dp/B0CGZWGGJ9/ref=sspa_dk_rhf_search_pt_sub_1/?_encoding=UTF8&ie=UTF8&psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9yaGZfc2VhcmNoX3BlcnNvbmFsaXplZA%3D%3D&sp_cr=ZAZ&aref=49gM9MYudt&pd_rd_w=0x9oz&content-id=amzn1.sym.5a4e0702-6571-42c4-8929-1a5e014d9dae&pf_rd_p=5a4e0702-6571-42c4-8929-1a5e014d9dae&pf_rd_r=E1W2TV810S774SG8KB4K&pd_rd_wg=Cl2DB&pd_rd_r=50175619-c0bf-45d5-bef1-9ce23850f0f5&ref_=sspa_dk_rhf_search_pt_sub"
    r_spon = client.post("/api/search", json={"query": sponsored_url, "search_type": "keyword"})
    assert r_spon.status_code == 200
    spon_data = r_spon.json()
    assert "Kreo Tundra" in spon_data["product_name"] or "Cooler" in spon_data["product_name"]
    assert spon_data["lowest_price"] > 0
    assert len(spon_data["offers"]) == 5

    # Test analyze-reviews with the exact URL
    r_rev2 = client.post(f"/api/analyze-reviews?product_name={sponsored_url}")
    assert r_rev2.status_code == 200
    rev_data2 = r_rev2.json()
    assert rev_data2["total_reviews"] >= 10
    assert rev_data2["authentic_reviews_count"] >= 6
    assert rev_data2["bot_reviews_count"] >= 2
    assert rev_data2["trust_score"] > 50.0


