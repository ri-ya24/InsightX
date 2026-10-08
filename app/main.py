from app.data.news_api import fetch_news
from app.database.news_repository import save_articles, get_articles
from app.processing.cleaning import prepare_article
from app.analytics.keywords import extract_keywords, extract_key_phrases


topic = "artificial intelligence"

articles = fetch_news(topic, page_size=5)

print("Articles fetched:", len(articles))

saved_count = save_articles(articles, topic)

print("Articles saved to database:", saved_count)
saved_articles = get_articles(topic)

print("Articles in database:", len(saved_articles))
if saved_articles:
    cleaned_article = prepare_article(saved_articles[0])

    print()
    print("Cleaned article:")
    print("Title:", cleaned_article["title"])
    print("Combined text:", cleaned_article["combined_text"])
    cleaned_articles = [
    prepare_article(article)
    for article in saved_articles
]

keywords = extract_keywords(cleaned_articles, top_n=10)

print()
print("Top keywords:")

for keyword, count in keywords:
    print(keyword, "->", count)
key_phrases = extract_key_phrases(cleaned_articles, top_n=10)

print()
print("Top key phrases:")

for phrase, count in key_phrases:
    print(phrase, "->", count)