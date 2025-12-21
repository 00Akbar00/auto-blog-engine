from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from src.scraper.reddit_scraper import (
    scrape_latest_post,
    SimpleRedditPost,
    SimpleRedditResponse,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)


# Request schema for scraping a single subreddit
class ScrapeRequest(BaseModel):
    """Request schema for scraping a single subreddit."""
    subreddit: str = Field(..., description="Name of the subreddit to scrape")


class ScraperController:
    """Controller for scraper endpoints."""

    @staticmethod
    async def scrape_subreddit(request: ScrapeRequest) -> SimpleRedditResponse:
        """
        Scrape the latest post from a single subreddit.
        """
        try:
            post_data = scrape_latest_post(request.subreddit)
            
            post = SimpleRedditPost(
                title=post_data["title"],
                description=post_data["description"],
                category=post_data["category"]
            )
            
            return SimpleRedditResponse(
                success=True,
                post=post,
                message=f"Successfully scraped latest post from r/{request.subreddit}"
            )
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            logger.error(f"Scraping error: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to scrape subreddit: {str(e)}",
            )

