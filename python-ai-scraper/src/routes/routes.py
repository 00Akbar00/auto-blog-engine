"""All API routes in a single module."""

from fastapi import APIRouter

from src.controllers.health_controller import HealthController
from src.controllers.scraper_controller import ScraperController, ScrapeRequest
from src.scraper.reddit_scraper import SimpleRedditResponse

router = APIRouter()


@router.post(
    "/api/scrape/reddit",
    response_model=SimpleRedditResponse,
    tags=["scraper"],
)
async def scrape_subreddit(request: ScrapeRequest) -> SimpleRedditResponse:
    """Scrape the latest post from a Reddit subreddit."""
    return await ScraperController.scrape_subreddit(request)

