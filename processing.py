
from urllib.parse import urlsplit, urlunsplit


def normalize_url(url: str) -> str:
    """Normalize a URL for duplicate detection."""
    url = url.strip()

    if not url:
        return ""

    parts = urlsplit(url)

    # Ignore tracking parameters and URL fragments.
    return urlunsplit((
        parts.scheme.lower(),
        parts.netloc.lower(),
        parts.path.rstrip("/"),
        "",
        "",
    ))


def remove_duplicates(articles: list[dict]) -> list[dict]:
    """Keep the first article for each unique URL."""
    unique_articles = []
    seen_urls = set()

    for article in articles:
        url = normalize_url(article.get("url", ""))

        if not url or url in seen_urls:
            continue

        seen_urls.add(url)

        cleaned_article = article.copy()
        cleaned_article["url"] = url
        cleaned_article["title"] = (
            cleaned_article.get("title") or "Untitled"
        ).strip()
        cleaned_article["content"] = (
            cleaned_article.get("content") or ""
        ).strip()

        unique_articles.append(cleaned_article)

    return unique_articles
