import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-2.html"

def scrape_books_page2():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]

        raw_price = book.select_one(".price_color").text
        price_match = re.search(r"\d+\.\d+", raw_price)
        price = float(price_match.group()) if price_match else None

        books.append({
            "title": title,
            "price": price,
            "source": "books.toscrape.com (page 2)"
        })

    return books
