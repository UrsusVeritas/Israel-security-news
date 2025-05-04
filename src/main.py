from src.parsers.times_of_israel import get_times_of_israel_articles
from src.parsers.jerusalem_post import get_jerusalem_post_articles
from src.parsers.i24news import get_i24news_articles
import json
import os

def save_articles(articles, path="data/articles.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)

def main():
    print("[*] Fetching Times of Israel news...")
    toi_articles = get_times_of_israel_articles()
    print(f"[+] Times of Israel: {len(toi_articles)} articles found.")

    print("[*] Fetching Jerusalem Post news...")
    jpost_articles = get_jerusalem_post_articles()
    print(f"[+] Jerusalem Post: {len(jpost_articles)} articles found.")

    print("[*] Fetching i24News...")
    i24_articles = get_i24news_articles()
    print(f"[+] i24News: {len(i24_articles)} articles found.")

    all_articles = toi_articles + jpost_articles + i24_articles
    print(f"[✓] Total articles collected: {len(all_articles)}")
    save_articles(all_articles)

if __name__ == "__main__":
    main()
