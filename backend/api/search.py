from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any
from backend.scraper.books_scraper import scrape_books
from backend.scraper.books_scraper_page2 import scrape_books_page2
from backend.ranking.deal_ranker import rank_deals

router = APIRouter()


class Explanation(BaseModel):
    price: float
    price_weight: float
    final_score: float


class BestDeal(BaseModel):
    title: str
    price: float
    source: str
    score: float
    explanation: Explanation


class SearchResponse(BaseModel):
    query: str
    best_deal: BestDeal
    why_this_deal: Dict[str, Any]


@router.get("/search", response_model=SearchResponse)
def search_product(query: str):
    books_page1 = scrape_books()
    books_page2 = scrape_books_page2()

    all_books = books_page1 + books_page2

    filtered = [
        book for book in all_books
        if query.lower() in book["title"].lower()
    ]

    if not filtered:
        return {
            "query": query,
            "best_deal": None,
            "why_this_deal": {}
        }

    ranked = rank_deals(filtered)
    best_deal = ranked[0]

    return {
        "query": query,
        "best_deal": best_deal,
        "why_this_deal": best_deal["explanation"]
    }
