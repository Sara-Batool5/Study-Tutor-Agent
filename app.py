import streamlit as st


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🧠",
    layout="wide",
)


# ---------------------------------------------------------
# CUSTOM CSS
# Theme-safe: works with Light and Dark Streamlit themes
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main page spacing */
    .block-container {
        max-width: 1000px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }


    /* Hero */
    .hero-title {
        font-size: 46px;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 19px;
        opacity: 0.75;
        margin-bottom: 35px;
    }


    /* Text area */
    div[data-testid="stTextArea"] textarea {
        color: inherit !important;
        -webkit-text-fill-color: currentColor !important;
        background-color: transparent !important;
        caret-color: currentColor !important;
    }

    div[data-testid="stTextArea"] textarea::placeholder {
        opacity: 0.6 !important;
        -webkit-text-fill-color: currentColor !important;
    }


    /* Select boxes */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        color: inherit !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] * {
        color: inherit !important;
    }


    /* Buttons */
    div[data-testid="stButton"] button {
        width: 100%;
        min-height: 48px;
        border-radius: 10px;
        font-weight: 600;
    }


    /* Remove unnecessary decoration */
    header[data-testid="stHeader"] {
        background: transparent;
    }


    /* Mobile */
    @media (max-width: 768px) {

        .block-container {
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            font-size: 36px;
        }

        .hero-subtitle {
            font-size: 16px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero-title">
        Learn Smarter.<br>
        Think Deeper.
    </div>

    <div class="hero-subtitle">
        Your AI Study Tutor
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# STUDY INPUT
# ---------------------------------------------------------

st.markdown("### Ask your Study Tutor")

question = st.text_area(
    "What do you want to learn?",
    placeholder="Example: Explain PCR to me as a beginner.",
    height=150,
)


# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    level = st.selectbox(
        "Your Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )


with col2:

    mode = st.selectbox(
        "Learning Mode",
        [
            "Explain",
            "Ask a Question",
            "Quiz",
            "Study Plan",
        ],
    )


# ---------------------------------------------------------
# BUTTON
# ---------------------------------------------------------

st.markdown("")

if st.button(
    "✨ Ask Study Tutor",
    type="primary",
):

    if not question.strip():

        st.warning(
            "Please enter a question first."
        )

    else:

        st.info(
            "Your question has been received."
        )

        st.write("**Question:**", question)
        st.write("**Level:**", level)
        st.write("**Learning Mode:**", mode)
