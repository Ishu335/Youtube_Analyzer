import streamlit as st
from app  import build_Agent

@st.cache_resource
def run_agent():
    return build_Agent()

agent=run_agent()

st.set_page_config(
    page_title="YouTube AI Analyzer",
    page_icon="🎥",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

/* Main container */
.hero {
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    margin-top:60px;
    background: white;
}

/* Logo */
.logo {
    font-size:32px;
    margin-bottom:8px;
}

/* Title */
.title {
    font-size:42px;
    font-weight:700;
    color:#2d3748;
    margin-bottom:20px;
}

/* Chat input width */
.stChatInput {
    max-width:700px !important;
    margin:auto !important;
}

/* Pills */
.pill-container {
    display:flex;
    justify-content:center;
    gap:8px;
    flex-wrap:wrap;
    margin-top:12px;
}

.pill {
    padding:6px 12px;
    border:1px solid #e5e7eb;
    border-radius:999px;
    background:white;
    font-size:13px;
    color:#4b5563;
}

/* Disclaimer */
.disclaimer {
    font-size:12px;
    color:#6b7280;
    margin-top:15px;
}

.block-container {
    padding-top: 1rem;
    max-width: 900px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero Section ---------------- #

st.markdown("""
<div class="hero">
    <div class="logo">🎥</div>
    <div class="title">YouTube AI Analyzer</div>
</div>
""", unsafe_allow_html=True)

# Suggestion Pills
st.markdown("""
<div class="pill-container">
    <div class="pill">📊 Analyze Video</div>
    <div class="pill">📝 Generate Summary</div>
    <div class="pill">🎯 Extract Key Points</div>
    <div class="pill">📈 Channel Analysis</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align:center;">
    <p class="disclaimer">
        ⚖ AI-generated insights may contain inaccuracies.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- Chat Section ---------------- #


# Search box
url=None
url = st.chat_input(
    "Paste a YouTube URL or ask a question..."
)
if url:
    with st.chat_message("user"):
        st.write(url)
    with st.spinner("Youtube Video is Analysizing .....", show_time=True):
        responce=agent.run(
            f"Analysize this Youtube Video :{url}"
        )

        with st.chat_message("assistant"):
            st.write("YouTube analysis result will appear here...")
            st.markdown(responce.content, unsafe_allow_html=True, help=None)