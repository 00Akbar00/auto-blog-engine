"""Data source domains for scraping."""
from .reddit import (
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

