# SignalScope

SignalScope searches recent news with Tavily, removes duplicate articles, and
uses Google Gemini to create an evidence-aware intelligence report. Reports can
be generated from either the Streamlit web app or the command-line interface.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- A Tavily API key

## Setup

Open a terminal in the project directory and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set `GEMINI_API_KEY` and `TAVILY_API_KEY`. Keep this file
private; it is excluded from Git.

## Run the web app

```powershell
python -m streamlit run reports\app.py
```

Enter a topic, choose how many articles to retrieve, and select **Generate
intelligence report**. The app displays the report and its source articles and
offers a Markdown download. Generated reports are also saved under `reports/`.

## Run from the command line

```powershell
python main.py
```

## Tests

Run the offline test suite with:

```powershell
python -m pytest -q
```

The optional live Gemini and Tavily service tests are disabled by default. Run
them only when API credentials are configured and you want to make real API
requests:

```powershell
$env:RUN_SERVICE_TESTS = "1"
python -m pytest test_services.py -q
```
