# scrape books to scrape using https://books.toscrape.com

import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"
start_page = "catalogue/page-1.html"
output_page = "books_data.json"
target_count = 70


def scrap_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:

        print("Some erorr occured : \n", e)
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        title = title_tag.get("title")
        price = article.select_one("p.price_color").text.strip()
        print(f"{title} - {price}")
        books.append({"title": title, "price": price})

    next_link = soup.select_one("li.next > a")
    next_url = urljoin(url, next_link.get("href")) if next_link else None

    return books, next_url


def main():
    collected = []
    current_url = urljoin(base_url, start_page)

    while len(collected) < target_count and current_url:
        print(f"Scraping {current_url}")
        books, next_url = scrap_page(current_url)
        collected.extend(books)
        current_url = next_url
    collected = collected[:target_count]
    print(f"Scraped {len(collected) } books")

    with open(output_page, "w", encoding="utf-8") as f:
        json.dump(collected, f, indent=2)

    print(f"Data saved to {output_page}")


if __name__ == "__main__":
    main()
