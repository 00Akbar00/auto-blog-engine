"""Reddit domain module."""
from .schemas import (
    RedditPost, 
    RedditScrapeRequest, 
    RedditMultiScrapeRequest,
    RedditMultiScrapeResponse
)

__all__ = [
    "RedditPost",
    "RedditScrapeRequest",
    "RedditMultiScrapeRequest",
    "RedditMultiScrapeResponse",
]

