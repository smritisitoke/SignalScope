from pathlib import Path
from datetime import datetime


def save_report(report: str, query: str) -> Path:
    """Save a SignalScope report as a Markdown file."""

    output_dir = Path(__file__).resolve().parent / "reports"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"report_{timestamp}.md"

    file_path = output_dir / filename

    content = f"""# SignalScope Intelligence Report

**Topic:** {query}
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

{report}
"""

    file_path.write_text(content, encoding="utf-8")

    return file_path
