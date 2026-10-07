from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

# ==========================================
# 1. Search & Input Models
# ==========================================

class SearchRequest(BaseModel):
    query: str = Field(..., description="Product keyword, product URL, or image URL")
    search_type: str = Field("keyword", description="Type of search: 'keyword', 'url', or 'image_url'")

class VisualMatchRequest(BaseModel):
    image_url: Optional[str] = Field(None, description="Public URL of the product image")
    image_base64: Optional[str] = Field(None, description="Base64 encoded image content if uploaded")

# ==========================================
# 2. Product & Pricing Aggregation Models
# ==========================================

class StorePriceOffer(BaseModel):
    platform: str = Field(..., description="Store name: Amazon, Flipkart, eBay, Walmart, Croma")
    title: str = Field(..., description="Product title on the store")
    price: float = Field(..., description="Current listing price in INR/USD")
    original_price: float = Field(..., description="Original MSRP before discounts")
    currency: str = Field("INR", description="Currency code (e.g. INR, USD)")
    discount_percent: float = Field(0.0, description="Discount percentage")
    in_stock: bool = Field(True, description="Availability status")
    delivery_fee: float = Field(0.0, description="Estimated shipping / delivery cost")
    delivery_time: str = Field("2-4 Days", description="Estimated delivery timeline")
    rating: float = Field(0.0, description="Store customer rating (1-5)")
    rating_count: int = Field(0, description="Total review count on the store")
    product_url: str = Field(..., description="Direct link to store item")
    image_url: str = Field("", description="Product thumbnail image URL")
    seller_name: str = Field("Official Store", description="Seller or fulfillment name")
    is_best_deal: bool = Field(False, description="Flag if this is the lowest landed price")

class PriceComparisonResult(BaseModel):
    query: str
    product_name: str
    category: str
    thumbnail: str
    lowest_price: float
    highest_price: float
    average_price: float
    best_deal_platform: str
    potential_savings: float
    offers: List[StorePriceOffer]

# ==========================================
# 3. Review & NLP Bot Detection Models
# ==========================================

class ReviewItem(BaseModel):
    id: str
    author: str
    rating: float
    date: str
    text: str
    title: Optional[str] = ""
    verified_purchase: bool = True
    platform: str = "Amazon"

class ReviewClassification(BaseModel):
    review_id: str
    author: str
    text: str
    rating: float
    date: str
    platform: str
    is_bot: bool
    confidence: float
    classification_label: str = Field("AUTHENTIC", description="'AUTHENTIC', 'SUSPICIOUS', or 'BOT_DETECTED'")
    tier1_heuristic_flags: List[str] = Field(default_factory=list)
    tier2_nlp_score: float = Field(0.0, description="AI synthetic/deceptive text score")
    reasons: List[str] = Field(default_factory=list)

class AspectScore(BaseModel):
    aspect: str = Field(..., description="Aspect name: 'Build Quality', 'Value for Money', 'Performance', etc.")
    positive_score: float = Field(..., description="Percentage positive sentiment (0-100)")
    neutral_score: float = Field(..., description="Percentage neutral sentiment (0-100)")
    negative_score: float = Field(..., description="Percentage negative sentiment (0-100)")
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    sample_quote: str = ""

class ReviewAnalysisResult(BaseModel):
    product_name: str
    total_reviews: int
    authentic_reviews_count: int
    bot_reviews_count: int
    suspicious_reviews_count: int
    trust_score: float = Field(..., description="Overall authentic review score (0-100%)")
    original_rating: float = Field(..., description="Unfiltered customer star rating")
    adjusted_rating: float = Field(..., description="Corrected rating after stripping bot reviews")
    rating_delta: float = Field(..., description="Difference between original and adjusted rating")
    classifications: List[ReviewClassification]
    aspect_analysis: List[AspectScore]
    overall_sentiment_summary: str

# ==========================================
# 4. Visual Matching & Price History Models
# ==========================================

class VisualMatchResponse(BaseModel):
    detected_object: str
    visual_confidence: float
    matched_products: List[StorePriceOffer]
    best_deal: Optional[StorePriceOffer] = None

class PriceHistoryPoint(BaseModel):
    date: str
    price: float
    platform: str

class PriceHistoryResponse(BaseModel):
    product_name: str
    currency: str = "INR"
    current_price: float
    lowest_historical: float
    highest_historical: float
    average_historical: float
    price_recommendation: str
    history: List[PriceHistoryPoint]

class PriceAlertRequest(BaseModel):
    product_name: str
    target_price: float
    email: str
    current_price: float

class PriceAlertResponse(BaseModel):
    status: str
    message: str
    alert_id: str
