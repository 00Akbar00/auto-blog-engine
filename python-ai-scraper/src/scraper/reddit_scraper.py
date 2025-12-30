import praw
from typing import Dict
from pydantic import BaseModel, Field
from src.utils.config import getenv
from src.utils.logger import get_logger

logger = get_logger(__name__)


# ============================================================================
# HARD-CODED SUBREDDIT/CATEGORY MAPPINGS
# ============================================================================

SUBREDDIT_CATEGORIES = {
    "python": "Tech",
    "programming": "Tech", 
    "webdev": "Tech",
    "technology": "Tech",
    "linux": "Tech",
    "javascript": "Tech",
    "machinelearning": "Tech",
    "datascience": "Tech",
    "gaming": "Entertainment",
    "movies": "Entertainment", 
    "music": "Entertainment",
    "anime": "Entertainment",
    "books": "Entertainment",
    "news": "News",
    "worldnews": "News",
    "politics": "News",
    "economics": "News",
}


# ============================================================================
# SIMPLE SCHEMAS  
# ============================================================================

class SimpleRedditPost(BaseModel):
    """Simple schema for Reddit post - only title, description, category."""
    title: str = Field(..., description="Post title")
    description: str = Field(..., description="Post description/selftext") 
    category: str = Field(..., description="Post category")


class SimpleRedditResponse(BaseModel):
    """Simple response for Reddit scraping."""
    success: bool = Field(..., description="Whether scraping was successful")
    post: SimpleRedditPost = Field(..., description="The scraped post")
    message: str = Field(..., description="Response message")


# ============================================================================
# SIMPLE SCRAPING FUNCTION
# ============================================================================

def scrape_latest_post(subreddit_name: str) -> Dict[str, str]:      
    try:
        category = SUBREDDIT_CATEGORIES.get(subreddit_name.lower(), "General")
        client_id = getenv("REDDIT_CLIENT_ID")
        client_secret = getenv("REDDIT_CLIENT_SECRET") 
        user_agent = getenv("REDDIT_USER_AGENT", "auto-blog-scraper/1.0")

        if not client_id:
            raise ValueError(
                "Reddit credentials not found. Please set REDDIT_CLIENT_ID."
            )
        if not client_secret:
            raise ValueError(
                "REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT environment variables."
            )

        # Reddit client conneciton                
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

        logger.info("Reddit API client initialized")
        
        # Get subreddit
        subreddit = reddit.subreddit(subreddit_name)
        
        # Get the latest post title and description
        latest_post = next(subreddit.new(limit=1))
        title = latest_post.title
        description = latest_post.selftext if latest_post.selftext else "No description available"
        
        logger.info(f"Successfully scraped latest post from r/{subreddit_name}: '{title[:50]}...'")
        
        return {
            "title": title,
            "description": description,
            "category": category
        }
    except Exception as e:
        logger.error(f"Error scraping subreddit '{subreddit_name}': {e}")
        raise Exception(f"Failed to scrape subreddit: {str(e)}")

