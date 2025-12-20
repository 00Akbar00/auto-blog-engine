# Python AI Scraper Structure (Clean + Practical)

## 📁 File Organization

```
src/
├── app.py                # FastAPI app setup
├── routes/
│   └── routes.py         # GET /health + POST /api/scrape/reddit/multi
├── controllers/
│   ├── health_controller.py
│   └── scraper_controller.py
├── scraper/
│   └── reddit_scraper.py # Reddit scraper + all scraper-related schemas
├── utils/
│   ├── config.py         # getenv() helper
│   └── logger.py         # logging setup
└── storage/
    └── filesystem.py     # optional file storage helpers
```

**Principle:** keep “scraper-related data” (schemas + scraping logic) inside the scraper module(s), and keep the API layer thin.

## 🎯 Key Principles

1. **Scraper module owns scraper data** - request/response schemas + scraping logic live together
2. **Thin API layer** - routes call scraper module directly
3. **Easy to extend** - add new modules under `src/scraper/` and expose new routes
4. **Neat structure** - minimal folders, no redundant “domain/controller” layers

## 📝 Usage Examples

### Basic Usage
```python
from src.scraper.reddit_scraper import RedditScraper, RedditMultiScrapeRequest

scraper = RedditScraper()
posts = scraper.scrape_subreddits(
    RedditMultiScrapeRequest(subreddits=["python", "learnpython"], limit=3, sort_by="hot")
)
print(len(posts))
```

## 🔧 Adding New Sources

Just add a new module under `src/scraper/` (example: `hackernews_scraper.py`) and call it from a route in `src/routes/`.

## ✨ Benefits

- ✅ **Simpler** - no redundant layering
- ✅ **Cleaner** - scraper logic is centralized in the scraper module(s)
- ✅ **Flexible** - easy to add new sources/routes

  