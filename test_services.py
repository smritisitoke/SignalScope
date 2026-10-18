
import os

import pytest
from config import GEMINI_API_KEY, GEMINI_MODEL, TAVILY_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient


RUN_SERVICE_TESTS = os.getenv("RUN_SERVICE_TESTS", "").strip().lower() in {
    "1",
    "true",
    "yes",
}


@pytest.mark.skipif(
    not RUN_SERVICE_TESTS,
    reason="Set RUN_SERVICE_TESTS=1 to run live service tests.",
)
@pytest.mark.skipif(not GEMINI_API_KEY, reason="GEMINI_API_KEY is not configured.")
def test_gemini():
    print("\nTesting Gemini...")

    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0,
        timeout=30,
        max_retries=1,
    )

    response = model.invoke(
        "Reply with exactly this text: SignalScope is ready."
    )

    print("Gemini response:", response.content)
    print("Gemini connection successful!")


@pytest.mark.skipif(
    not RUN_SERVICE_TESTS,
    reason="Set RUN_SERVICE_TESTS=1 to run live service tests.",
)
@pytest.mark.skipif(not TAVILY_API_KEY, reason="TAVILY_API_KEY is not configured.")
def test_tavily():
    print("\nTesting Tavily...")

    client = TavilyClient(api_key=TAVILY_API_KEY)

    response = client.search(
        query="latest artificial intelligence news",
        topic="news",
        time_range="week",
        max_results=3,
    )

    results = response.get("results", [])

    if not results:
        print("Search completed, but no results were returned.")
        return

    for i, article in enumerate(results, start=1):
        print(f"\nArticle {i}")
        print("Title:", article.get("title", "No title"))
        print("URL:", article.get("url", "No URL"))
        print("Content:", article.get("content", "")[:200])

    print("\nTavily connection successful!")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
