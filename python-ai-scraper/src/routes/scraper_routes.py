"""Scraper routes."""
from fastapi import APIRouter

from src.controllers.scraper_controller import ScraperController
from src.domains.reddit import RedditScrapeRequest, RedditScrapeResponse

router = APIRouter(prefix="/api/v1", tags=["scraper"])


@router.post("/scrape/reddit", response_model=RedditScrapeResponse)
async def scrape_reddit(request: RedditScrapeRequest) -> RedditScrapeResponse:
    """Scrape posts from a Reddit subreddit."""
    return await ScraperController.scrape_reddit(request)

