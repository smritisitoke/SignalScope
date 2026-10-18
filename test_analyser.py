import analyser


def test_analyze_news_extracts_text_from_gemini_content_blocks(monkeypatch):
    class FakeModel:
        def __init__(self, **kwargs):
            pass

        def invoke(self, prompt):
            return type(
                "Response",
                (),
                {"content": [{"type": "text", "text": "Report text"}]},
            )()

    monkeypatch.setattr(analyser, "ChatGoogleGenerativeAI", FakeModel)

    result = analyser.analyze_news([{"title": "Headline", "content": "Details"}])

    assert result == "Report text"
