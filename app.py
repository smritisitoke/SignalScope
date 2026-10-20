import streamlit as st

from search import search_news
from processing import remove_duplicates
from analyser import analyze_news
from report import save_report


st.set_page_config(
    page_title="SignalScope",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 SignalScope")
st.caption("News-to-Insight Intelligence Engine")
st.write(
    "Discover recent news, identify major themes, "
    "and generate an evidence-aware intelligence report."
)

with st.form("news_search_form"):
    query = st.text_input(
        "What topic do you want to investigate?",
        placeholder="e.g. AI in healthcare",
    )
    max_results = st.slider(
        "Number of articles to retrieve",
        min_value=3,
        max_value=10,
        value=5,
    )
    submitted = st.form_submit_button(
        "Generate intelligence report",
        type="primary",
    )

if submitted:
    if not query.strip():
        st.warning("Please enter a topic first.")
    else:
        try:
            with st.spinner("Searching news with Tavily..."):
                articles = search_news(
                    query.strip(),
                    max_results=max_results,
                )
                cleaned_articles = remove_duplicates(articles)

            if not cleaned_articles:
                st.warning(
                    "No usable articles found. Try another topic."
                )
            else:
                st.success(
                    f"Found {len(cleaned_articles)} unique articles."
                )

                with st.spinner("Analyzing articles with Gemini..."):
                    report = analyze_news(cleaned_articles)

                saved_path = save_report(report, query.strip())

                st.session_state["report"] = report
                st.session_state["articles"] = cleaned_articles
                st.session_state["query"] = query.strip()
                st.session_state["saved_path"] = str(saved_path)

        except Exception as error:
            st.error(
                "Something went wrong while generating the report."
            )
            st.caption(
                f"Error type: {type(error).__name__}. "
                "Check your API configuration and terminal for details."
            )

if st.session_state.get("report"):
    st.divider()
    st.subheader("📊 Intelligence Report")
    st.markdown(st.session_state["report"])

    st.download_button(
        label="Download report as Markdown",
        data=st.session_state["report"],
        file_name="signalscope_report.md",
        mime="text/markdown",
    )

    st.caption(
        f"Saved locally at: {st.session_state['saved_path']}"
    )

    with st.expander("View retrieved source articles"):
        for i, article in enumerate(
            st.session_state["articles"], start=1
        ):
            st.markdown(f"**{i}. {article.get('title', 'Untitled')}**")
            url = article.get("url", "")
            if url:
                st.markdown(f"[Read original article]({url})")
            st.write(article.get("content", ""))
            st.divider()
