
from tavily import TavilyClient
from config import TAVILY_API_KEY


def search_news(query: str, max_results: int = 5) -> list[dict]:
    """Search for news articles and return useful fields."""

    client = TavilyClient(api_key=TAVILY_API_KEY)

    response = client.search(
        query=query,
        topic="news",
        max_results=max_results,
    )

    articles = []

    for result in response.get("results", []):
        articles.append({
            "title": result.get("title", "Untitled"),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
            "score": result.get("score", 0),
        })

    return articles


if __name__ == "__main__":
    query = input("What news topic do you want to explore? ").strip()

    if not query:
        print("Please enter a topic.")
    else:
        articles = search_news(query)

        if not articles:
            print("No articles found.")
        else:
            for number, article in enumerate(articles, start=1):
                print(f"\n{number}. {article['title']}")
                print(f"URL: {article['url']}")
                print(f"Summary: {article['content'][:250]}")
