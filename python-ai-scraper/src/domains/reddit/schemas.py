"""Reddit API schemas for request and response validation."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class RedditScrapeRequest(BaseModel):
    """Request schema for Reddit scraping."""
    subreddit: str = Field(..., description="Name of the subreddit to scrape")
    limit: int = Field(default=10, ge=1, le=100, description="Number of posts to scrape (1-100)")
    sort_by: str = Field(default="hot", description="Sort posts by: hot, new, top, rising")
    time_filter: Optional[str] = Field(default=None, description="Time filter for top posts: hour, day, week, month, year, all")


class RedditPost(BaseModel):
    """Schema for a single Reddit post."""
    id: str = Field(..., description="Reddit post ID")
    title: str = Field(..., description="Post title")
    author: str = Field(..., description="Post author username")
    score: int = Field(..., description="Post upvote score")
    upvote_ratio: float = Field(..., description="Upvote ratio (0-1)")
    num_comments: int = Field(..., description="Number of comments")
    url: str = Field(..., description="Post URL")
    permalink: str = Field(..., description="Reddit permalink")
    selftext: str = Field(default="", description="Post text content (if self-post)")
    created_utc: datetime = Field(..., description="Post creation timestamp (UTC)")
    subreddit: str = Field(..., description="Subreddit name")
    is_self: bool = Field(..., description="Whether post is a self-post or link")
    over_18: bool = Field(..., description="Whether post is NSFW")


class RedditScrapeResponse(BaseModel):
    """Response schema for Reddit scraping."""
    success: bool = Field(..., description="Whether scraping was successful")
    subreddit: str = Field(..., description="Subreddit that was scraped")
    posts_count: int = Field(..., description="Number of posts scraped")
    posts: List[RedditPost] = Field(..., description="List of scraped posts")
    message: Optional[str] = Field(default=None, description="Optional message or error description")

