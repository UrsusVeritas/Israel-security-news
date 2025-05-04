import requests
from bs4 import BeautifulSoup
from src.utils.filter import KEYWORDS

def get_times_of_israel_articles():
    url = "https://www.timesofisrael.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    for article in soup.select("article.item-list"):
        title_tag = article.find("h2")
        if not title_tag:
            continue
        title = title_tag.get_text(strip=True)
        link = title_tag.find("a")['href'] if title_tag.find("a") else None

        if any(keyword in title.lower() for keyword in KEYWORDS):
            articles.append({
                "title": title,
                "url": link,
                "source": "Times of Israel"
            })

    return articles
