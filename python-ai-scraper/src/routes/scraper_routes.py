"""Scraper routes."""
from fastapi import APIRouter

from src.controllers.scraper_controller import ScraperController
from src.scraper.reddit_scraper import (
    RedditMultiScrapeRequest,
    RedditMultiScrapeResponse
)

router = APIRouter(prefix="/api", tags=["scraper"])



@router.post("/scrape/reddit/multi", response_model=RedditMultiScrapeResponse)
async def scrape_multiple_subreddits(request: RedditMultiScrapeRequest) -> RedditMultiScrapeResponse:
    """Scrape posts from multiple Reddit subreddits."""
    return await ScraperController.scrape_multiple_subreddits(request)

