# 🧠 VeriPrice AI — E-Commerce Intelligence Platform

> **Next-Generation AI Price Comparator, Visual Reverse Search & 2-Tier Fake/Bot Review Detection Platform.**

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg?style=flat&logo=fastapi)](https://fastapi.tiangolo.com)
[![PyTorch](https://img.shields.io/badge/ML-PyTorch%20%7C%20Transformers-EE4C2C.svg?style=flat&logo=pytorch)](https://pytorch.org)
[![TailwindCSS](https://img.shields.io/badge/Frontend-TailwindCSS%20%7C%20Chart.js-38B2AC.svg?style=flat&logo=tailwind-css)](https://tailwindcss.com)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=flat&logo=python)](https://python.org)

---

## 🌟 Overview & Architecture

**VeriPrice AI** aggregates real-time product prices across major e-commerce platforms (**Amazon, Flipkart, eBay, Walmart, Croma**), tracks historical price trends, and uses computer vision and NLP to protect consumers from misleading pricing and synthetic bot reviews.

```
                    ┌──────────────────────────────────────────────┐
                    │               User Interface                 │
                    │   (Keyword / URL / Visual Image Search)      │
                    └──────────────────────┬───────────────────────┘
                                           │
                                           ▼
                    ┌──────────────────────────────────────────────┐
                    │              FastAPI Gateway                 │
                    └──────┬───────────────┼───────────────┬───────┘
                           │               │               │
            ┌──────────────▼──────┐ ┌──────▼──────┐ ┌──────▼──────────────┐
            │   Price Aggregator  │ │Visual Match │ │2-Tier NLP Detector  │
            │  (Amazon, Flipkart, │ │(Google Lens/│ │(Heuristic + Neural) │
            │   eBay, Croma, etc) │ │CLIP/Hashing)│ │  + ABSA Engine      │
            └──────────────┬──────┘ └──────┬──────┘ └──────┬──────────────┘
                           │               │               │
                           └───────────────┼───────────────┘
                                           ▼
                    ┌──────────────────────────────────────────────┐
                    │       VeriPrice Intelligence Dashboard       │
                    │  - Ranked Deals & Best Value Badge           │
                    │  - Trust Score & Adjusted Star Rating        │
                    │  - Aspect-Based Pros/Cons & Price History    │
                    └──────────────────────────────────────────────┘
```

---

## 🚀 Key Features

### 1. Multi-Input Search & Visual Matching
- **Keyword & URL Search**: Instant normalization of product queries and direct store URLs.
- **Visual Reverse Search**: Image upload & URL reverse image search matching products across stores using perceptual feature extraction and SerpApi/Lens endpoints.

### 2. Cross-Platform Price Aggregation
- Real-time normalization of prices across 5 platforms: **Amazon, Flipkart, Croma, Walmart, eBay**.
- Computes total landed cost (`Price + Delivery Fees`), discounts, stock status, seller ratings, and auto-identifies the **Best Deal**.

### 3. 2-Tier AI Fake & Bot Review Detection
- **Tier 1 (Heuristic Engine)**:
  - **Duplicate Template Matching**: Pairwise Levenshtein edit distance & Jaccard token overlap to uncover copy-paste bot farms.
  - **Temporal Burst Detection**: Identifies artificial spikes of 5-star reviews on specific dates.
  - **Rating-Sentiment Polarity Inversion**: Catches 5-star ratings accompanied by negative complaints.
  - **Lexical Entropy & 1-Liner Spam Checks**: Detects low-entropy generic phrase repetition.
- **Tier 2 (NLP & Synthetic Artifact Classifier)**:
  - Detects AI-generated marketing clichés (`"game changer"`, `"testament to innovation"`, robotic formality).
  - Neural sentiment classification via HuggingFace `distilbert-base-uncased`.
- **Output Metrics**:
  - **Product Trust Score (0-100%)**
  - **Adjusted Star Rating**: Recomputes the true customer satisfaction score after eliminating bots and de-weighting suspicious reviews.

### 4. Aspect-Based Sentiment Analysis (ABSA)
- Automatically evaluates authentic customer reviews across 5 core dimensions:
  1. *Build Quality & Design*
  2. *Value for Money*
  3. *Performance & Speed*
  4. *Battery & Power*
  5. *Customer Support & Delivery*
- Extracts structured **Key Pros** and **Key Cons**.

### 5. Historical Price Tracking & Alerts
- Interactive Chart.js graphs for 30-day, 90-day, and 180-day price trends.
- Smart Buy / Wait advisory.
- Price drop alert subscription engine.

---

## 📂 Project Directory Structure

```
MAJOR PROJ/
├── backend/
│   ├── __init__.py
│   ├── main.py                  # FastAPI application & REST routing
│   ├── config.py                # App configuration & environment loading
│   ├── schemas.py               # Pydantic v2 data models
│   ├── aggregator.py            # Multi-store price comparator engine
│   ├── visual_matcher.py        # Reverse image matching module
│   ├── review_detector.py       # 2-Tier fake review & bot detector
│   ├── absa_engine.py           # Aspect-Based Sentiment Analysis
│   ├── history_tracker.py       # Historical price analytics & alert manager
│   └── review_data.py           # Authentic + bot review datasets & generators
├── static/
│   ├── css/
│   │   └── styles.css           # Glassmorphism & cyber-dark styling
│   └── js/
│       └── app.js               # Reactive state manager & Chart.js logic
├── templates/
│   └── index.html               # Responsive single-page intelligence dashboard
├── tests/
│   └── test_pipeline.py         # Automated pytest test suite
├── .env.example                 # Environment variables template
├── requirements.txt             # Pinned python dependencies
├── run.py                       # One-click startup runner
└── README.md                    # Project documentation
```

---

## 🛠️ Quickstart Installation & Local Setup

### 1. Clone & Navigate to Repository
```bash
cd "c:\Users\deyab\.gemini\antigravity-ide\MAJOR PROJ"
```

### 2. Create and Activate Virtual Environment
```bash
# Windows PowerShell / CMD:
python -m venv venv
venv\Scripts\activate

# Linux / macOS:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment (Optional)
```bash
cp .env.example .env
```
*(Optional: Add your `SERPAPI_KEY` in `.env` if you wish to query live Google Lens API)*

### 5. Run the Application
```bash
python run.py
```

Open your browser at **`http://127.0.0.1:8000`** to access the live dashboard!

Interactive Swagger API docs are available at **`http://127.0.0.1:8000/docs`**.

---

## 🧪 Running Automated Tests

Run the test suite with pytest:
```bash
pytest tests/test_pipeline.py -v
```

---

## 📡 REST API Reference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/search` | Multi-store product search & price comparison |
| `GET` | `/api/price-compare` | Query-based price comparison |
| `POST` | `/api/visual-match` | Reverse visual image search matching |
| `POST` | `/api/analyze-reviews` | 2-Tier bot detection + ABSA engine |
| `GET` | `/api/price-history` | Historical price tracking & recommendations |
| `POST` | `/api/alert` | Register a price drop email notification |
| `GET` | `/api/health` | Service health status check |
| `GET` | `/` | Web dashboard single-page application |

---

## 📜 License & Acknowledgments
Built with ❤️ using FastAPI, Hugging Face Transformers, and Tailwind CSS.
