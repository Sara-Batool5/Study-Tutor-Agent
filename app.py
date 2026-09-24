import streamlit as st

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🧠",
    layout="wide",
)

# ================================
# CUSTOM CSS
# ================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 174, 255, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(123, 92, 255, 0.12),
            transparent 30%
        ),
        #070b14;
    color: #f5f7ff;
}

.block-container {
    max-width: 1100px;
    padding-top: 3rem;
}

/* TITLE */

.title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(
        90deg,
        #38d9ff,
        #7b61ff,
        #c66cff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #a9b9d6;
    font-size: 18px;
    margin-top: 12px;
    margin-bottom: 35px;
}

/* TEXT AREA */

div[data-baseweb="textarea"] {
    background-color: #0c1424 !important;
    border: 1px solid rgba(0, 200, 255, 0.25) !important;
    border-radius: 15px !important;
}

div[data-baseweb="textarea"] textarea {
    background-color: #0c1424 !important;
    color: #f4f8ff !important;
    caret-color: #38d9ff !important;
}

div[data-baseweb="textarea"] textarea::placeholder {
    color: #7184a3 !important;
    opacity: 1 !important;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: 1px solid rgba(0, 210, 255, 0.45);
    background: linear-gradient(
        90deg,
        #008cff,
        #6d4cff
    );
    color: white;
    font-weight: 700;
    padding: 13px 20px;
    box-shadow: 0 0 20px rgba(0, 157, 255, 0.20);
}

/* SELECTBOX */

div[data-baseweb="select"] > div {
    background-color: #0c1424 !important;
    color: white !important;
    border-color: rgba(0, 200, 255, 0.25) !important;
}

</style>
""", unsafe_allow_html=True)


# ================================
# HERO
# ================================

st.markdown(
    '<div class="title">Learn Smarter.<br>Think Deeper.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Your AI Study Tutor</div>',
    unsafe_allow_html=True,
)


# ================================
# INPUT
# ================================

st.markdown("### Ask your Study Tutor")

question = st.text_area(
    "What do you want to learn?",
    placeholder="Example: Explain PCR to me as a beginner.",
    height=150,
)

level = st.selectbox(
    "Your Level",
    ["Beginner", "Intermediate", "Advanced"],
)

mode = st.selectbox(
    "Learning Mode",
    ["Explain", "Ask a Question", "Quiz", "Study Plan"],
)


# ================================
# TEST BUTTON
# ================================

if st.button(
    "✨ Ask Study Tutor",
    type="primary",
):

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        st.success(
            f"Question received: {question}"
        )
