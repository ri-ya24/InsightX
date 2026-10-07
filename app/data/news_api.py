import os
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_news(topic, page_size=20):
    """
    Fetch recent news articles for a given topic from NewsAPI.
    """

    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        raise ValueError("NEWS_API_KEY was not found in .env")

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": topic,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": api_key,
    }

    response = requests.get(url, params=params, timeout=15)

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "ok":
        raise ValueError(
            f"NewsAPI request failed: {data.get('message', 'Unknown error')}"
        )

    return data.get("articles", [])