"""Scraper controller for handling scraping requests."""

from fastapi import HTTPException, status
from pydantic import BaseModel, Field

from src.scraper import (
    scrape_latest_post,
    get_available_subreddits,
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

    @staticmethod
    async def get_available_subreddits() -> dict:
        """
        Get list of available subreddits and their categories.
        """
        try:
            subreddits = get_available_subreddits()
            return {
                "success": True,
                "subreddits": subreddits,
                "message": f"Found {len(subreddits)} available subreddits"
            }
        except Exception as e:
            logger.error(f"Error getting subreddits: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to get subreddits: {str(e)}",
            )
