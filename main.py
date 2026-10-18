
from search import search_news
from processing import remove_duplicates
from analyser import analyze_news
from report import save_report


def main():
    print("\n===== SignalScope =====")
    query = input("Enter a news topic: ").strip()

    if not query:
        print("Please enter a topic.")
        return

    print("\nSearching for articles...")
    articles = search_news(query, max_results=5)
    print(f"Articles retrieved: {len(articles)}")

    print("\nCleaning articles...")
    cleaned_articles = remove_duplicates(articles)
    print(f"Unique articles: {len(cleaned_articles)}")

    if not cleaned_articles:
        print("No usable articles found. Try another topic.")
        return

    print("\nAnalyzing with Gemini...")
    report = analyze_news(cleaned_articles)

    print("\n===== SIGNALSCOPE REPORT =====\n")
    print(report)
    report_path = save_report(report, query)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
