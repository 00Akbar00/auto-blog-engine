"""Scraper controller for handling scraping requests."""
from fastapi import HTTPException, status

from src.domains.reddit import (
    RedditMultiScrapeRequest,
    RedditMultiScrapeResponse
)
from src.scraper import RedditScraper
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ScraperController:
    """Controller for scraper endpoints."""
    


    @staticmethod
    async def scrape_multiple_subreddits(request: RedditMultiScrapeRequest) -> RedditMultiScrapeResponse:
        """
        Handle multi-subreddit scraping request.
        
        Args:
            request: RedditMultiScrapeRequest
            
        Returns:
            RedditMultiScrapeResponse
            
        Raises:
            HTTPException: If scraping fails
        """
        try:
            scraper = RedditScraper()
            posts = scraper.scrape_subreddits(request)
            
            return RedditMultiScrapeResponse(
                success=True,
                total_posts=len(posts),
                posts=posts,
                message=f"Successfully scraped {len(posts)} posts from {len(request.subreddits)} subreddits"
            )
            
        except ValueError as e:
            logger.error(f"Validation error: {e}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
        except Exception as e:
            logger.error(f"Scraping error: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to scrape subreddits: {str(e)}"
            )

