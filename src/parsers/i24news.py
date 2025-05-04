import requests
from bs4 import BeautifulSoup
from src.utils.filter import KEYWORDS

def get_i24news_articles():
    url = "https://www.i24news.tv/en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    for div in soup.find_all("div", class_="teaser-text"):
        a_tag = div.find("a")
        title = a_tag.get_text(strip=True) if a_tag else ""
        link = a_tag['href'] if a_tag and a_tag.has_attr('href') else ""
        if not title or not link:
            continue
        if any(keyword in title.lower() for keyword in KEYWORDS):
            if not link.startswith("http"):
                link = "https://www.i24news.tv" + link
            articles.append({
                "title": title,
                "url": link,
                "source": "i24News"
            })

    return articles
