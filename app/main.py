from app.services.news_pipeline import run_news_pipeline


def main():

    topic = input(
        "\nEnter a topic to analyse: "
    ).strip()

    if not topic:
        print("Please enter a valid topic.")
        return

    try:

        result = run_news_pipeline(topic)

        # Article date range
        article_dates = [
            article["published_at"]
            for article in result["cleaned_articles"]
            if article.get("published_at") is not None
        ]

        if article_dates:
            print("\nArticle Date Range:")
            print("Oldest article:", min(article_dates).date())
            print("Newest article:", max(article_dates).date())
        else:
            print("\nPublished dates unavailable.")

        # InsightX results
        print("\n========== INSIGHTX ==========")

        print("Topic:", result["topic"])

        print(
            "Articles fetched:",
            result["fetched_count"]
        )

        print(
            "New articles saved:",
            result["saved_count"]
        )

        print(
            "Total articles in database:",
            result["total_articles"]
        )

        print("\nTop Keywords:")

        for word, count in result["keywords"]:
            print(f"{word} -> {count}")

        print("\nTop Key Phrases:")

        for phrase, count in result["key_phrases"]:
            print(f"{phrase} -> {count}")

        print("\n==============================")

    except Exception as error:

        print("\nInsightX pipeline failed:")
        print(error)

        raise


if __name__ == "__main__":
    main()