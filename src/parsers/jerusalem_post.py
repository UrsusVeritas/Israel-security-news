import requests
from bs4 import BeautifulSoup
from src.utils.filter import KEYWORDS

def get_jerusalem_post_articles():
    url = "https://www.jpost.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    for article in soup.find_all("a", href=True):
        title = article.get_text(strip=True)
        link = article['href']
        if not title or len(title) < 20:
            continue
        if any(keyword in title.lower() for keyword in KEYWORDS):
            if not link.startswith("http"):
                link = "https://www.jpost.com" + link
            articles.append({
                "title": title,
                "url": link,
                "source": "Jerusalem Post"
            })

    return articles
