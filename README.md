# Israel-security-news

Python application that scrapes and aggregates real-time English-language news related to national security and cybersecurity events in Israel. The system collects articles from multiple sources (Times of Israel, Jerusalem Post, i24News), filters content using a custom keyword list (e.g., cyberattacks, terror, fire, IDF, etc.), and stores the results in structured JSON format. Designed with modular architecture and clean separation of logic. Ready for future extensions like alerts, dashboards, or ML classification.

## 🚀 Features
- Pulls news from news sources (RSS/HTML)
- Filters for critical keywords (e.g. CVE, exploit, ransomware)
- Saves results in JSON
- Modular, extendable structure for future bots/alerts
- Can be containerized via Docker

## 📂 Project Structure
```
cybersentinel/
├── data/                  # Cached or stored results
├── src/
│   ├── parsers/           # Modules for each news source (RSS/HTML)
│   ├── utils/             # Filtering, text processing, etc.
│   └── main.py            # Entrypoint script
├── tests/                 # Unit tests
├── requirements.txt
├── Dockerfile
└── README.md
```

## ⚙️ Installation
```bash
git clone https://github.com/yourusername/Israel-security-news.git
cd Israel-security-news
pip install -r requirements.txt
python src/main.py
```

## 🛠 Tech Stack
- Python 3.10+
- Requests / Feedparser / BeautifulSoup
- JSON / Optional: MongoDB
- Docker (optional)

## 🔮 Future Ideas
- Telegram/email alerts
- Dashboard (Flask or Streamlit)
- NLP-based threat classification

---

*Built with ❤️ for threat awareness.*
