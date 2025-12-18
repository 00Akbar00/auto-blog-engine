"""Scraper routes."""
from fastapi import APIRouter

from src.controllers.scraper_controller import ScraperController
from src.domains.reddit import (
    RedditMultiScrapeRequest,
    RedditMultiScrapeResponse
)

router = APIRouter(prefix="/api/v1", tags=["scraper"])





@router.post("/scrape/reddit/multi", response_model=RedditMultiScrapeResponse)
async def scrape_multiple_subreddits(request: RedditMultiScrapeRequest) -> RedditMultiScrapeResponse:
    """Scrape posts from multiple Reddit subreddits."""
    return await ScraperController.scrape_multiple_subreddits(request)

