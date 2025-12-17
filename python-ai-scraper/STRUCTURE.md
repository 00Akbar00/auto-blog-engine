# Clean Function-Based Scraper Structure

## 📁 File Organization

```
src/scraper/
├── scraper.py    # Main scraping functions (reddit, run, filters)
├── models.py     # Data models (ScrapedContent, ScrapeConfig)
├── utils.py      # Utilities (rate limiting, retries, text cleaning)
├── parser.py     # HTML parsing functions
├── browser.py    # Browser automation functions (Playwright)
└── __init__.py   # Package exports
```

**Total: 6 files** (down from 9+ files with classes)

## 🎯 Key Principles

1. **Function-based** - No classes, just clean functions
2. **Simple imports** - `from scraper import run, scrape_reddit`
3. **Easy to extend** - Just add new functions to `scraper.py`
4. **Less files** - Consolidated logic, no unnecessary abstractions

## 📝 Usage Examples

### Basic Usage
```python
from scraper import run, scrape_reddit
from scraper.models import ScrapeConfig

# Using config file
results = run("config.yml")

# Direct function call
config = ScrapeConfig(source="reddit", subreddit="python", limit=10)
results = scrape_reddit(config)
```

### Browser Scraping
```python
from scraper.browser import fetch_page, fetch_multiple_pages
from scraper.parser import parse_article

# Single page
html = fetch_page("https://example.com", wait_for=".content")
article = parse_article(html)

# Multiple pages
urls = ["https://site1.com", "https://site2.com"]
results = fetch_multiple_pages(urls)
```

## 🔧 Adding New Sources

Just add a new function to `scraper.py`:

```python
def scrape_hackernews(config: ScrapeConfig) -> List[ScrapedContent]:
    """Scrape HackerNews."""
    # Your implementation here
    pass

# Register in run() function
scrapers = {
    "reddit": scrape_reddit,
    "hackernews": scrape_hackernews,  # Add here
}
```

## ✨ Benefits

- ✅ **Simpler** - No class inheritance, just functions
- ✅ **Cleaner** - Less files, easier to navigate
- ✅ **Flexible** - Easy to add new sources
- ✅ **Pythonic** - Functions are first-class citizens

