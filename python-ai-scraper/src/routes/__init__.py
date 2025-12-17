"""API routes."""
from .scraper_routes import router as scraper_router
from .health_routes import router as health_router

__all__ = ["scraper_router", "health_router"]

