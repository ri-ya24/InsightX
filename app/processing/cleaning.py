import re


def clean_text(text):
    """
    Clean article text for further analysis.
    """
    if not text:
        return ""

    text = str(text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text


def prepare_article(article):
    """
    Create a cleaned representation of a NewsArticle database record.
    """
    title = clean_text(article.title)
    description = clean_text(article.description)

    combined_text = f"{title}. {description}".strip()

    return {
        "id": article.id,
        "topic": article.topic,
        "title": title,
        "description": description,
        "source_name": article.source_name,
        "published_at": article.published_at,
        "url": article.url,
        "combined_text": combined_text,
    }