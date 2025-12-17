# Python AI Scraper

Professional, modular project structure for scraping and AI processing with FastAPI.

## Overview

- `src/api/`: FastAPI routes and application
- `src/services/`: Business logic and scraper services
- `src/models/`: Pydantic schemas for requests/responses
- `src/utils/`: Configuration, logging, and utilities
- `src/storage/`: Storage utilities
- `src/prompts/`: AI prompt templates (YAML/MD)

## Quick Start

1. Create a virtualenv: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Set up environment variables by creating a `.env` file:
   ```bash
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=auto-blog-scraper/1.0
   ```
   Get Reddit credentials from https://www.reddit.com/prefs/apps
5. Run the API server: `python main.py`
6. API will be available at `http://localhost:8000`
7. View API documentation at `http://localhost:8000/docs`

## API Usage

### Scrape Reddit Posts

**Endpoint:** `POST /api/v1/scrape/reddit`

**Request Body:**
```json
{
  "subreddit": "python",
  "limit": 10,
  "sort_by": "hot",
  "time_filter": "day"
}
```

**Parameters:**
- `subreddit` (required): Name of the subreddit to scrape
- `limit` (optional, default: 10): Number of posts (1-100)
- `sort_by` (optional, default: "hot"): Sort by "hot", "new", "top", or "rising"
- `time_filter` (optional): For "top" sort only - "hour", "day", "week", "month", "year", "all"

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/api/v1/scrape/reddit" \
  -H "Content-Type: application/json" \
  -d '{
    "subreddit": "python",
    "limit": 5,
    "sort_by": "hot"
  }'
```

## Project Structure

```
python-ai-scraper/
├── src/
│   ├── api/               # FastAPI application
│   │   ├── main.py        # FastAPI app initialization
│   │   └── routes.py      # API endpoints
│   ├── services/         # Business logic services
│   │   └── reddit_service.py  # Reddit scraper service
│   ├── models/            # Data models and schemas
│   │   └── schemas.py     # Pydantic request/response models
│   ├── utils/             # Utilities
│   │   ├── config.py      # Configuration helpers
│   │   └── logger.py      # Logging setup
│   ├── storage/           # Storage utilities
│   └── prompts/           # AI prompt templates
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Features

- **Clean Architecture**: Service-based design with separation of concerns
- **FastAPI**: Modern, fast API framework with automatic documentation
- **Reddit Scraper**: Professional Reddit scraping using praw
- **Type Safety**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive error handling and logging
- **Extensible**: Easy to add new scrapers and endpoints
