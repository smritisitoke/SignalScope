
from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY, GEMINI_MODEL


def analyze_news(articles: list[dict]) -> str:
    """Generate an evidence-grounded news intelligence report."""

    if not articles:
        return "No articles available to analyze."

    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0.2,
        max_retries=2,
    )

    article_text = ""

    for i, article in enumerate(articles, start=1):
        article_text += (
            f"\nArticle {i}\n"
            f"Title: {article.get('title', 'Untitled')}\n"
            f"Content: {article.get('content', '')[:1500]}\n"
            f"Source URL: {article.get('url', '')}\n"
        )

    prompt = f"""
You are SignalScope, a news intelligence analyst.

Analyze the articles below and produce a clear report with these sections:

1. Executive Summary
2. Major Themes and Trends
3. Key Claims and Supporting Sources
4. Conflicting or Uncertain Information
5. Important Caveats
6. Source List

Rules:
- Use only information supported by the supplied articles.
- Do not invent facts, quotes, dates, or sources.
- Distinguish reported claims from verified facts.
- If the articles do not provide enough evidence, say so.
- Include source URLs for relevant claims.
- Identify when multiple articles may discuss the same underlying event.

Articles:
{article_text}
"""

    response = model.invoke(prompt)
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_blocks = [
            block["text"]
            for block in content
            if isinstance(block, dict) and isinstance(block.get("text"), str)
        ]
        if text_blocks:
            return "\n".join(text_blocks)

    raise TypeError(
        f"Gemini returned unsupported content type: {type(content).__name__}"
    )


if __name__ == "__main__":
    print("Analyzer module loaded successfully.")
