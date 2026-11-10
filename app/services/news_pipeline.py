from app.data.news_api import fetch_news

from app.database.news_repository import (
    save_articles,
    get_articles
)

from app.processing.cleaning import prepare_article

from app.analytics.keywords import (
    extract_keywords,
    extract_key_phrases
)


def run_news_pipeline(topic, page_size=20, top_n=10):
    """
    Run the complete news analysis pipeline for a topic.

    Steps:
    1. Fetch news articles
    2. Save new articles to PostgreSQL
    3. Retrieve stored articles
    4. Clean article text
    5. Extract keywords
    6. Extract key phrases
    """

    if not topic or not topic.strip():
        raise ValueError("Please provide a valid topic.")

    topic = topic.strip()

    fetched_articles = fetch_news(
        topic,
        page_size=page_size
    )

    # Step 2: Save articles
    saved_count = save_articles(
        fetched_articles,
        topic
    )

    stored_articles = get_articles(topic)

    cleaned_articles = [
        prepare_article(article)
        for article in stored_articles
    ]

    keywords = extract_keywords(
        cleaned_articles,
        top_n=top_n
    )

    key_phrases = extract_key_phrases(
        cleaned_articles,
        top_n=top_n
    )

    return {
        "topic": topic,
        "fetched_count": len(fetched_articles),
        "saved_count": saved_count,
        "total_articles": len(stored_articles),
        "cleaned_articles": cleaned_articles,
        "keywords": keywords,
        "key_phrases": key_phrases
    }