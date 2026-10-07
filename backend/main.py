import os
import asyncio
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, Request, UploadFile, File, Form, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse

from backend.config import settings
from backend.schemas import (
    SearchRequest, PriceComparisonResult, VisualMatchRequest,
    VisualMatchResponse, ReviewAnalysisResult, ReviewItem,
    PriceHistoryResponse, PriceAlertRequest, PriceAlertResponse
)
from backend.aggregator import price_aggregator
from backend.visual_matcher import visual_matcher
from backend.review_detector import review_detector
from backend.absa_engine import absa_engine
from backend.history_tracker import history_tracker
from backend.review_data import get_product_reviews

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Next-generation e-commerce intelligence engine with multi-store price aggregation, visual search, 2-tier fake review detection, and aspect sentiment analysis."
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static & Template directories
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

STATIC_DIR.mkdir(parents=True, exist_ok=True)
TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


# ==========================================
# Frontend Route
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def serve_dashboard(request: Request):
    """
    Renders the VeriPrice AI single-page intelligence dashboard.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"app_name": settings.PROJECT_NAME}
    )


# ==========================================
# Core API Routes
# ==========================================

@app.post("/api/search", response_model=PriceComparisonResult)
async def search_products(req: SearchRequest):
    """
    Multi-Input Product Search & Multi-Store Price Aggregator.
    Searches across Amazon, Flipkart, eBay, Walmart, and Croma.
    """
    if not req.query or len(req.query.strip()) < 2:
        raise HTTPException(status_code=400, detail="Search query or URL must be at least 2 characters.")
    
    result = await asyncio.to_thread(price_aggregator.search_and_compare, req.query)
    return result


@app.get("/api/price-compare", response_model=PriceComparisonResult)
async def price_compare(q: str = Query(..., min_length=2, description="Product name or keyword")):
    """
    GET endpoint for retrieving real-time multi-store price comparisons.
    """
    return await asyncio.to_thread(price_aggregator.search_and_compare, q)


@app.post("/api/visual-match", response_model=VisualMatchResponse)
async def visual_match(
    image_url: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    """
    Visual Reverse Search:
    Upload an image or pass an image URL to find the exact product across stores.
    """
    import base64
    if file:
        content = await file.read()
        b64_str = base64.b64encode(content).decode("utf-8")
        return await asyncio.to_thread(visual_matcher.match_image, image_base64=b64_str)
    elif image_url:
        return await asyncio.to_thread(visual_matcher.match_image, image_url=image_url)
    else:
        raise HTTPException(status_code=400, detail="Must provide either an image file or an image_url.")


@app.post("/api/analyze-reviews", response_model=ReviewAnalysisResult)
async def analyze_product_reviews(product_name: str = Query(...), custom_reviews: Optional[List[ReviewItem]] = None):
    """
    2-Tier Fake/Bot Review Detection + Aspect-Based Sentiment Analysis (ABSA).
    Calculates Product Trust Score (% authentic) and Adjusted Star Rating.
    """
    # If a URL was passed directly as product_name, resolve it first
    if not custom_reviews and ("http://" in product_name or "https://" in product_name):
        resolved = await asyncio.to_thread(price_aggregator.search_and_compare, product_name)
        product_name = resolved.product_name

    reviews = custom_reviews if custom_reviews else get_product_reviews(product_name)
    
    # 1. Run 2-Tier Fake/Bot Detection
    analysis_res = await asyncio.to_thread(review_detector.analyze_reviews, product_name, reviews)
    
    # 2. Run Aspect-Based Sentiment Analysis (ABSA) on authentic reviews
    authentic_only = [r for r in reviews if not any(c.review_id == r.id and c.is_bot for c in analysis_res.classifications)]
    aspect_scores = await asyncio.to_thread(absa_engine.analyze_aspects, authentic_only if authentic_only else reviews)
    analysis_res.aspect_analysis = aspect_scores
    
    return analysis_res


@app.get("/api/price-history", response_model=PriceHistoryResponse)
async def get_price_history(
    product_name: str = Query(..., description="Product name"),
    current_price: float = Query(..., description="Current price in INR"),
    days: int = Query(90, description="History window (30, 90, 180)")
):
    """
    Retrieves historical price tracking trends, 30/90/180-day charts, and buy/wait recommendations.
    """
    return history_tracker.get_price_history(product_name, current_price, days)


@app.post("/api/alert", response_model=PriceAlertResponse)
async def create_price_alert(req: PriceAlertRequest):
    """
    Subscribes user to a price drop threshold alert.
    """
    if req.target_price >= req.current_price:
        raise HTTPException(status_code=400, detail="Target price must be lower than current listing price.")
    return history_tracker.create_price_alert(req)


@app.get("/api/health")
async def health_check():
    """System health check endpoint."""
    return {"status": "ok", "app": settings.PROJECT_NAME, "version": settings.VERSION}
