import report as report_module


def test_save_report_creates_markdown_file(tmp_path, monkeypatch):
    monkeypatch.setattr(report_module, "__file__", str(tmp_path / "report.py"))

    path = report_module.save_report("Summary text", "AI policy")

    assert path.exists()
    assert path.parent == tmp_path / "reports"
    contents = path.read_text(encoding="utf-8")
    assert "**Topic:** AI policy" in contents
    assert "Summary text" in contents
