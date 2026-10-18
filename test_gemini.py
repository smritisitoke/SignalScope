from config import GEMINI_API_KEY, GEMINI_MODEL
from langchain_google_genai import ChatGoogleGenerativeAI


def main():
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing from the project .env file."
        )

    print("Testing Gemini...")

    model = ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=GEMINI_API_KEY,
        temperature=0,
        max_retries=1,
    )

    response = model.invoke(
        "Reply with exactly this text: SignalScope is ready."
    )

    print("Gemini response:", response.content)
    print("Gemini connection successful!")


if __name__ == "__main__":
    main()