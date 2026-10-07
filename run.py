import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import uvicorn
import os
from backend.config import settings

def main():
    print("=" * 70)
    print(f"[*] Starting {settings.PROJECT_NAME} v{settings.VERSION}")
    print(f"[*] API & Dashboard URL: http://{settings.HOST}:{settings.PORT}")
    print(f"[*] Interactive Swagger Docs: http://{settings.HOST}:{settings.PORT}/docs")
    print(f"[*] Supported Platforms: {', '.join(settings.SUPPORTED_PLATFORMS)}")
    print("=" * 70)

    uvicorn.run(
        "backend.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

if __name__ == "__main__":
    main()
