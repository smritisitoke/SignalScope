# 🔎 SignalScope — News-to-Insight Intelligence Engine

**Turn news into structured intelligence with Python, Google Gemini, Tavily, and Streamlit.**

SignalScope is an AI-powered news analysis application that retrieves recent articles on a user-selected topic, removes duplicate sources, and uses Google Gemini to generate a structured intelligence report with supporting source URLs.

Instead of manually reading multiple articles, users can explore major themes, key claims, uncertainties, and important caveats through a single interactive interface.


## ✨ Features

- **Topic-based news search:** Retrieve relevant news articles using Tavily.
- **Duplicate removal:** Normalize article URLs and remove duplicate results.
- **AI-powered analysis:** Use Google Gemini to generate structured, evidence-aware reports.
- **Key insights:** Organize findings into executive summaries, major themes, supporting claims, conflicting information, and caveats.
- **Source traceability:** Include original article URLs to help readers verify claims.
- **Interactive web interface:** Search for topics and generate reports through Streamlit.
- **Report downloads:** Download generated reports in Markdown format.
- **Local report storage:** Save generated reports for future reference.
- **Modular architecture:** Separate search, processing, analysis, configuration, and reporting logic.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| Google Gemini API | News analysis and insight generation |
| LangChain | Language-model integration |
| Tavily API | News and web search |
| python-dotenv | Local environment configuration |
| Pytest | Automated testing |

## 🏗️ Project Architecture

```text
SignalScope/
├── app.py              # Streamlit web application
├── main.py             # Command-line workflow
├── config.py           # Environment configuration
├── search.py           # Tavily news retrieval
├── processing.py       # URL normalization and deduplication
├── analyzer.py         # Gemini-powered report generation
├── report.py           # Markdown report generation and saving
├── test_services.py    # Service connection tests
├── test_gemini.py      # Gemini connection test
├── tests/              # Automated tests, if configured
├── assets/             # Screenshots and project images
├── reports/            # Locally generated reports
├── requirements.txt    # Python dependencies
├── .env                # Local API credentials (not committed)
├── .gitignore
└── README.md
```

*The tree illustrates the intended project organization; keep only files and folders that actually exist in your repository.*

## ⚙️ How It Works

1. **User input:** The user enters a topic, such as *Artificial Intelligence in Healthcare*.
2. **News retrieval:** Tavily searches for relevant news articles.
3. **Data processing:** SignalScope normalizes URLs and removes duplicate articles.
4. **AI analysis:** Google Gemini analyzes the retrieved article content and identifies major themes, claims, uncertainties, and caveats.
5. **Report generation:** The application displays the report and preserves source URLs for verification.
6. **Export:** The report can be downloaded as Markdown and saved locally.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible Python version supported by your installed dependencies
- A Google Gemini API key
- A Tavily API key
- Git

### 1. Clone the repository

```bash
git clone https://github.com/smritisitoke/SignalScope.git
cd SignalScope
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the Python executable inside `.venv` directly instead.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
GEMINI_MODEL=your_configured_gemini_model
```

Replace the placeholders with your own credentials and the Gemini model configured for your project.

**Security:** Never commit `.env` or publish API keys. Keep `.env` in `.gitignore`. If a key was exposed in a commit, revoke it and generate a replacement.

### 5. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL printed in the terminal, typically:

```text
http://localhost:8501
```

Enter a topic, choose the number of articles, and generate your intelligence report.

### 6. Run the command-line version

```bash
python main.py
```

Enter a topic when prompted to run the news analysis workflow from the terminal.

## 🧪 Testing

Run the project's test suite with:

```bash
python -m pytest -q
```

Some service tests may require valid API credentials and internet access. A skipped live API test does not confirm that the corresponding service is working.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Authenticates requests to Google Gemini |
| `TAVILY_API_KEY` | Authenticates Tavily search requests |
| `GEMINI_MODEL` | Configures the Gemini model used for analysis |

Keep real credentials in your local environment or an appropriate deployment secrets manager.

## ⚠️ Limitations

- Report quality depends on the relevance, completeness, and reliability of retrieved articles.
- Search results may contain duplicate coverage, incomplete excerpts, or conflicting claims.
- AI-generated summaries may contain errors and should be checked against original sources.
- Source links support verification but do not independently prove that a claim is true.
- API availability, usage limits, and model access depend on the provider and account.

SignalScope is an information-analysis tool, not a substitute for independent fact-checking or professional judgment.

## 🔮 Future Enhancements

- Add date and source filters.
- Improve source credibility assessment.
- Compare claims across multiple publications.
- Add structured JSON report export.
- Introduce report history and search history.
- Add automated tests for search processing and report generation.
- Deploy the Streamlit application publicly.

## 👩‍💻 Author

**Smriti Sitoke**

B.Tech — Computer Science and Business Systems

GitHub: [@smritisitoke](https://github.com/smritisitoke)

---

*Built to explore how AI can transform news discovery into structured, source-aware insights.*
