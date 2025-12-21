"""FastAPI application entry point."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.routes import router
from src.utils.logger import get_logger

logger = get_logger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Auto Blog Scraper API",
    description="API for scraping content from various sources (Reddit, etc.)",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    """Log startup event."""
    logger.info("Auto Blog Scraper API started")


@app.on_event("shutdown")
async def shutdown_event():
    """Log shutdown event."""
    logger.info("Auto Blog Scraper API shutting down")

