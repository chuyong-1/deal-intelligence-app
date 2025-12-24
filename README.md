# Deal Intelligence API 🚀

## Architecture Overview

- API Layer: FastAPI
- Scraping Layer: Modular web scrapers (multi-source)
- Intelligence Layer: Explainable deal scoring engine
- Output: Best-deal decision with reasoning


An AI-powered backend system that searches products across websites, compares prices, and intelligently identifies the best available deal with explainable reasoning.

## Problem
Users often waste time manually comparing prices across multiple websites. Lowest price alone does not always mean best value.

## Solution
This system:
- Scrapes product data from multiple sources
- Cleans and normalizes inconsistent data
- Ranks deals using a scoring engine
- Returns the best deal with transparent explanations

## Features
- Real-time web scraping
- Modular FastAPI backend
- Explainable deal scoring
- Scalable architecture

## Tech Stack
- Python
- FastAPI
- BeautifulSoup
- Requests
- REST APIs

## Example API Response
```json
{
  "query": "light",
  "best_deal": {
    "title": "A Light in the Attic",
    "price": 51.77,
    "source": "books.toscrape.com"
  }
}
