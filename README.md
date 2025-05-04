# CyberSentinel

CyberSentinel is a real-time news parser and alerting system focused on cybersecurity threats. 
It gathers and filters the latest critical news from trusted sources using Python, helping analysts and engineers stay ahead of threats.

## 🚀 Features
- Pulls news from cybersecurity sources (RSS/HTML)
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
git clone https://github.com/yourusername/cybersentinel.git
cd cybersentinel
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
