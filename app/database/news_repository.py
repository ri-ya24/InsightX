import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL was not found in .env")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(255), nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text)
    source_name = Column(String(255))
    author = Column(String(255))
    published_at = Column(DateTime)
    url = Column(Text, unique=True, nullable=False)
    image_url = Column(Text)


def save_articles(articles, topic):
    session = SessionLocal()

    try:
        saved_count = 0

        for article in articles:
            url = article.get("url")

            if not url:
                continue

            existing_article = (
                session.query(NewsArticle)
                .filter_by(url=url)
                .first()
            )

            if existing_article:
                continue

            news_article = NewsArticle(
                topic=topic,
                title=article.get("title") or "No title",
                description=article.get("description"),
                source_name=article.get("source", {}).get("name"),
                author=article.get("author"),
                published_at=article.get("publishedAt"),
                url=url,
                image_url=article.get("urlToImage"),
            )

            session.add(news_article)
            saved_count += 1

        session.commit()

        return saved_count

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()
def get_articles(topic=None):
    session = SessionLocal()

    try:
        query = session.query(NewsArticle)

        if topic:
            query = query.filter(NewsArticle.topic == topic)

        return query.order_by(NewsArticle.published_at.desc()).all()

    finally:
        session.close()