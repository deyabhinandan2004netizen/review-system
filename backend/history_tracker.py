import random
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any
from backend.schemas import PriceHistoryPoint, PriceHistoryResponse, PriceAlertRequest, PriceAlertResponse

class HistoryTracker:
    """
    Manages historical price trend analytics, buy/wait recommendations,
    and user price-drop alert subscriptions.
    """

    def __init__(self):
        self.alerts_db: Dict[str, Dict[str, Any]] = {}

    def get_price_history(self, product_name: str, current_price: float, days: int = 90) -> PriceHistoryResponse:
        """
        Generates realistic chronological price history points with realistic seasonal dips
        and market adjustments.
        """
        history: List[PriceHistoryPoint] = []
        now = datetime.now()
        
        # Seed based on product name for deterministic consistency
        seed_val = sum(ord(c) for c in product_name)
        rng = random.Random(seed_val)

        base = current_price
        history_prices = []
        
        # Generate daily/bi-weekly historical snapshots
        step_days = 3 if days <= 30 else (5 if days <= 90 else 10)
        num_points = days // step_days

        platforms = ["Amazon", "Flipkart", "Croma"]

        for i in range(num_points, -1, -1):
            point_date = now - timedelta(days=i * step_days)
            date_str = point_date.strftime("%b %d, %Y")
            
            # Add subtle seasonal cycles
            variation = rng.uniform(-0.12, 0.15)
            # Simulate a festive flash sale dip around 30-45 days ago
            if 30 <= (i * step_days) <= 45:
                variation -= 0.08
                
            pt_price = round(max(base * 0.70, base * (1 + variation)), -1)
            if i == 0:
                pt_price = current_price # Latest point matches current price exactly

            history_prices.append(pt_price)
            chosen_platform = rng.choice(platforms)
            history.append(PriceHistoryPoint(date=date_str, price=pt_price, platform=chosen_platform))

        lowest_h = min(history_prices)
        highest_h = max(history_prices)
        avg_h = round(sum(history_prices) / len(history_prices), 2)

        # Smart Recommendation engine
        diff_from_lowest = current_price - lowest_h
        diff_from_avg = current_price - avg_h

        if current_price <= lowest_h * 1.03:
            recommendation = f"🔥 Best Time to Buy! Current price is within 3% of the all-time historical low (₹{lowest_h:,.0f})."
        elif diff_from_avg < 0:
            recommendation = f"🟢 Good Deal: Price is ₹{abs(diff_from_avg):,.0f} below the {days}-day average (₹{avg_h:,.0f})."
        elif current_price >= highest_h * 0.95:
            recommendation = f"⏳ Wait for Drop: Price is near the {days}-day peak. Target buying around ₹{lowest_h:,.0f}."
        else:
            recommendation = f"🟡 Fair Price: Currently ₹{diff_from_lowest:,.0f} above the historical low."

        return PriceHistoryResponse(
            product_name=product_name,
            currency="INR",
            current_price=current_price,
            lowest_historical=lowest_h,
            highest_historical=highest_h,
            average_historical=avg_h,
            price_recommendation=recommendation,
            history=history
        )

    def create_price_alert(self, request: PriceAlertRequest) -> PriceAlertResponse:
        """
        Registers a new price drop notification alert.
        """
        alert_id = f"ALT-{uuid.uuid4().hex[:8].upper()}"
        self.alerts_db[alert_id] = {
            "product_name": request.product_name,
            "target_price": request.target_price,
            "current_price": request.current_price,
            "email": request.email,
            "created_at": datetime.now().isoformat(),
            "active": True
        }

        savings = max(0.0, request.current_price - request.target_price)
        return PriceAlertResponse(
            status="SUCCESS",
            message=f"Price drop tracker activated for {request.email}. We will notify you when price hits ₹{request.target_price:,.0f} (Target savings: ₹{savings:,.0f}).",
            alert_id=alert_id
        )

history_tracker = HistoryTracker()
