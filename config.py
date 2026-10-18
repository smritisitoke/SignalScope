import os
from pathlib import Path
from dotenv import load_dotenv

ENV_FILE = Path(__file__).resolve().parent / ".env"
load_dotenv(ENV_FILE, override=True)

GEMINI_API_KEY = (os.getenv("GEMINI_API_KEY") or "").strip()
TAVILY_API_KEY = (os.getenv("TAVILY_API_KEY") or "").strip()
GEMINI_MODEL = (
    os.getenv("GEMINI_MODEL") or "gemini-3.8-flash"
).strip()


def validate_config():
    missing = []

    if not GEMINI_API_KEY:
        missing.append("GEMINI_API_KEY")

    if not TAVILY_API_KEY:
        missing.append("TAVILY_API_KEY")

    if missing:
        raise ValueError(
            "Missing environment variables: " + ", ".join(missing)
        )

    print("Configuration loaded successfully.")
