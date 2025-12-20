"""All API routes in a single module."""

from fastapi import APIRouter

from src.controllers.health_controller import HealthController
from src.controllers.scraper_controller import ScraperController
from src.scraper.reddit_scraper import RedditMultiScrapeRequest, RedditMultiScrapeResponse

router = APIRouter()


@router.get("/health", tags=["health"])
async def health_check() -> dict:
    """Basic health check endpoint."""
    return await HealthController.health_check()


@router.post(
    "/api/scrape/reddit/multi",
    response_model=RedditMultiScrapeResponse,
    tags=["scraper"],
)
async def scrape_multiple_subreddits(request: RedditMultiScrapeRequest) -> RedditMultiScrapeResponse:
    """Scrape posts from multiple Reddit subreddits."""
    return await ScraperController.scrape_multiple_subreddits(request)


