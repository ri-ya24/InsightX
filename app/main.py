from app.data.news_api import fetch_news
from app.database.news_repository import save_articles


topic = "artificial intelligence"

articles = fetch_news(topic, page_size=5)

print("Articles fetched:", len(articles))

saved_count = save_articles(articles, topic)

print("Articles saved to database:", saved_count)