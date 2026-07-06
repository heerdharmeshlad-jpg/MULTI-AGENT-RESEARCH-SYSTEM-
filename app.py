import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Multi-Agent Research System")
st.caption("Search Agent → Reader Agent → Writer → Critic")

# ---- Session state ----
if "state" not in st.session_state:
    st.session_state.state = None
if "running" not in st.session_state:
    st.session_state.running = False

# ---- Input form ----
with st.form("research_form"):
    topic = st.text_input(
        "Enter a research topic",
        placeholder="e.g. Impact of AI on renewable energy adoption",
    )
    submitted = st.form_submit_button("Run Research", use_container_width=True)

# ---- Run pipeline ----
if submitted:
    if not topic.strip():
        st.warning("Please enter a topic before running the pipeline.")
    else:
        st.session_state.state = None

        with st.status("Running multi-agent research pipeline...", expanded=True) as status:
            try:
                st.write("**Step 1:** Search agent is gathering information...")
                st.write("**Step 2:** Reader agent will scrape the top result...")
                st.write("**Step 3:** Writer agent will draft the report...")
                st.write("**Step 4:** Critic agent will review the report...")

                # This call runs all 4 steps inside pipeline.py (blocking call),
                # so the messages above appear up-front, then the result below.
                result = run_research_pipeline(topic)

                st.session_state.state = result
                status.update(label="Pipeline completed!", state="complete", expanded=False)
            except Exception as e:
                status.update(label="Pipeline failed", state="error", expanded=True)
                st.error(f"An error occurred while running the pipeline:\n\n{e}")

# ---- Display results ----
state = st.session_state.state
if state:
    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Final Report", "🧐 Critic Feedback", "🔍 Search Results", "📚 Scraped Content"]
    )

    with tab_report:
        st.subheader("Final Report")
        st.markdown(state.get("report", "_No report generated._"))
        st.download_button(
            "Download Report as .md",
            data=str(state.get("report", "")),
            file_name="research_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.subheader("Critic Feedback")
        st.markdown(state.get("feedback", "_No feedback generated._"))

    with tab_search:
        st.subheader("Raw Search Results")
        st.text(state.get("search_results", "No search results."))

    with tab_scraped:
        st.subheader("Scraped Content")
        st.text(state.get("scraped_content", "No scraped content."))
else:
    st.info("Enter a topic above and click **Run Research** to start the pipeline.")
