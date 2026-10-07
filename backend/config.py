import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env if present
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    PROJECT_NAME: str = "Fake Review Detector"
    PROJECT_SUBTITLE: str = "Product Authenticity Checker"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # API Keys (Optional)
    SERPAPI_KEY: str = os.getenv("SERPAPI_KEY", "")
    HUGGINGFACE_TOKEN: str = os.getenv("HUGGINGFACE_TOKEN", "")
    
    # NLP & Model Configs
    USE_TRANSFORMER_MODELS: bool = os.getenv("USE_TRANSFORMER_MODELS", "True").lower() == "true"
    TRANSFORMER_MODEL_NAME: str = os.getenv("DEFAULT_MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
    
    # Supported Platforms
    SUPPORTED_PLATFORMS = ["Amazon", "Flipkart", "eBay", "Walmart", "Croma"]
    
    # Static & Template directories
    STATIC_DIR = BASE_DIR / "static"
    TEMPLATES_DIR = BASE_DIR / "templates"

settings = Settings()
