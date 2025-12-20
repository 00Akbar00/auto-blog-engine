# Python AI Scraper

Professional, modular project structure for scraping and AI processing with FastAPI.

## Overview

- `src/app.py`: FastAPI application initialization
- `src/routes/`: FastAPI routes (single file)
- `src/scraper/`: Scraper implementations + related Pydantic schemas
- `src/controllers/`: Endpoint controllers (business logic)
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
│   ├── app.py             # FastAPI app initialization
│   ├── routes/            # API endpoints
│   │   └── routes.py       # all routes in one file
│   ├── controllers/        # endpoint controllers (logic)
│   │   ├── health_controller.py
│   │   └── scraper_controller.py
│   ├── scraper/           # Scraper logic + related schemas
│   │   └── reddit_scraper.py
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

- **Clean Architecture**: Simple routing layer with scraper logic kept inside `src/scraper/`
- **FastAPI**: Modern, fast API framework with automatic documentation
- **Reddit Scraper**: Professional Reddit scraping using praw
- **Type Safety**: Pydantic models for request/response validation
- **Error Handling**: Comprehensive error handling and logging
- **Extensible**: Easy to add new scrapers and endpoints
