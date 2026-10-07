import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.database.news_repository import Base


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise ValueError("DATABASE_URL was not found in .env")

engine = create_engine(database_url)

Base.metadata.create_all(engine)

print("Database tables created successfully!")