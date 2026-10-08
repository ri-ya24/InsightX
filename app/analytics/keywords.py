from collections import Counter
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

STOPWORDS = {
    "the", "and", "for", "that", "with", "this", "from", "are",
    "was", "were", "has", "have", "will", "into", "about", "their",
    "they", "them", "than", "then", "also", "been", "being", "your",
    "you", "its", "our", "out", "but", "not", "can", "all", "more",
    "one", "two", "three", "how", "what", "why", "who", "after",
    "before", "over", "under", "while", "where", "when", "which",
    "new", "said", "say", "says", "according", "just",
    "would", "could", "should", "may", "might",
    "year", "years", "today", "time", "first", "last",
    "million", "billion"
}


def extract_keywords(articles, top_n=10):
    """
    Extract frequent meaningful single words.
    """

    word_counts = Counter()

    for article in articles:
        text = article["combined_text"].lower()

        words = re.findall(r"\b[a-z]{3,}\b", text)

        meaningful_words = [
            word for word in words
            if word not in STOPWORDS
        ]

        word_counts.update(meaningful_words)

    return word_counts.most_common(top_n)


def extract_key_phrases(articles, top_n=10):
    """
    Extract frequent natural two-word phrases from article text.
    """

    phrase_counts = Counter()

    for article in articles:
        text = article["combined_text"].lower()

        words = re.findall(r"\b[a-z]{3,}\b", text)

        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]

            # Keep only natural adjacent phrases
            if (
                first_word not in ENGLISH_STOP_WORDS
                and second_word not in ENGLISH_STOP_WORDS
            ):
                phrase = f"{first_word} {second_word}"
                phrase_counts[phrase] += 1

    return phrase_counts.most_common(top_n)