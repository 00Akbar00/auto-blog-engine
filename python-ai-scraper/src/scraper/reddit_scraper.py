"""Reddit scraper using praw."""
import praw
from typing import List
from datetime import datetime

from src.domains.reddit import RedditPost, RedditScrapeRequest
from src.utils.config import getenv
from src.utils.logger import get_logger

logger = get_logger(__name__)


class RedditScraper:
    """Scraper for Reddit posts using praw."""
    
    def __init__(self):
        """Initialize Reddit API client."""
        self.client_id = getenv("REDDIT_CLIENT_ID")
        self.client_secret = getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = getenv("REDDIT_USER_AGENT", "auto-blog-scraper/1.0")
        
        if not self.client_id or not self.client_secret:
            raise ValueError(
                "Reddit credentials not found. Please set REDDIT_CLIENT_ID, "
                "REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT environment variables."
            )
        
        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent
        )
        logger.info("Reddit API client initialized")
    
    def scrape_subreddit(self, request: RedditScrapeRequest) -> List[RedditPost]:
        """
        Scrape posts from a subreddit.
        
        Args:
            request: RedditScrapeRequest with scraping parameters
            
        Returns:
            List of RedditPost objects
            
        Raises:
            Exception: If subreddit doesn't exist or scraping fails
        """
        try:
            subreddit = self.reddit.subreddit(request.subreddit)
            
            # Validate subreddit exists
            try:
                subreddit.display_name
            except Exception as e:
                logger.error(f"Subreddit '{request.subreddit}' not found: {e}")
                raise ValueError(f"Subreddit '{request.subreddit}' not found or inaccessible")
            
            # Get posts based on sort_by
            if request.sort_by == "hot":
                posts = subreddit.hot(limit=request.limit)
            elif request.sort_by == "new":
                posts = subreddit.new(limit=request.limit)
            elif request.sort_by == "top":
                time_filter = request.time_filter or "day"
                posts = subreddit.top(limit=request.limit, time_filter=time_filter)
            elif request.sort_by == "rising":
                posts = subreddit.rising(limit=request.limit)
            else:
                logger.warning(f"Invalid sort_by '{request.sort_by}', defaulting to 'hot'")
                posts = subreddit.hot(limit=request.limit)
            
            # Convert to RedditPost objects
            reddit_posts = []
            for post in posts:
                try:
                    reddit_post = RedditPost(
                        id=post.id,
                        title=post.title,
                        author=str(post.author) if post.author else "[deleted]",
                        score=post.score,
                        upvote_ratio=post.upvote_ratio,
                        num_comments=post.num_comments,
                        url=post.url,
                        permalink=f"https://reddit.com{post.permalink}",
                        selftext=post.selftext[:5000] if post.selftext else "",  # Limit text length
                        created_utc=datetime.fromtimestamp(post.created_utc),
                        subreddit=post.subreddit.display_name,
                        is_self=post.is_self,
                        over_18=post.over_18
                    )
                    reddit_posts.append(reddit_post)
                except Exception as e:
                    logger.warning(f"Error processing post {post.id}: {e}")
                    continue
            
            logger.info(f"Successfully scraped {len(reddit_posts)} posts from r/{request.subreddit}")
            return reddit_posts
            
        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error scraping subreddit '{request.subreddit}': {e}")
            raise Exception(f"Failed to scrape subreddit: {str(e)}")

