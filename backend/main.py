"""Vercel entrypoint for FastAPI backend service."""
import sys
from pathlib import Path

# Ensure backend root is on Python path
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from app.main import app

__all__ = ["app"]

