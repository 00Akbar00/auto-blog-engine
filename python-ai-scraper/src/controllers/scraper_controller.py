"""Scraper controller for handling scraping requests."""
from fastapi import HTTPException, status

from src.domains.reddit import RedditScrapeRequest, RedditScrapeResponse
from src.scraper import RedditScraper
from src.utils.logger import get_logger

logger = get_logger(__name__)


class ScraperController:
    """Controller for scraper endpoints."""
    
    @staticmethod
    async def scrape_reddit(request: RedditScrapeRequest) -> RedditScrapeResponse:
        """
        Handle Reddit scraping request.
        
        Args:
            request: RedditScrapeRequest with scraping parameters
            
        Returns:
            RedditScrapeResponse with scraped posts
            
        Raises:
            HTTPException: If scraping fails
        """
        try:
            scraper = RedditScraper()
            posts = scraper.scrape_subreddit(request)
            
            return RedditScrapeResponse(
                success=True,
                subreddit=request.subreddit,
                posts_count=len(posts),
                posts=posts,
                message=f"Successfully scraped {len(posts)} posts from r/{request.subreddit}"
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
                detail=f"Failed to scrape subreddit: {str(e)}"
            )

