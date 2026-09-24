import streamlit as st

from crew import run_tutor


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       GLOBAL
    ================================= */

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


    /* ================================
       MAIN CONTAINER
    ================================= */

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ================================
       SIDEBAR
    ================================= */

    section[data-testid="stSidebar"] {

        background:
            linear-gradient(
                180deg,
                #080d18 0%,
                #0b1120 100%
            );

        border-right: 1px solid
            rgba(0, 204, 255, 0.15);
    }


    section[data-testid="stSidebar"] * {
        color: #e8f7ff;
    }


    /* ================================
       HERO
    ================================= */

    .hero {

        padding: 35px 35px 30px 35px;

        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                rgba(0, 183, 255, 0.13),
                rgba(126, 87, 255, 0.13)
            );

        border: 1px solid
            rgba(0, 204, 255, 0.18);

        box-shadow:
            0 0 40px
            rgba(0, 174, 255, 0.07);

        margin-bottom: 25px;
    }


    .hero-title {

        font-size: 48px;
        font-weight: 800;

        line-height: 1.1;

        margin-bottom: 12px;

        background:
            linear-gradient(
                90deg,
                #38d9ff,
                #7b61ff,
                #c66cff
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .hero-subtitle {

        font-size: 18px;

        color: #a9b9d6;

        max-width: 700px;

        line-height: 1.6;
    }


    /* ================================
       FEATURE CARDS
    ================================= */

    .feature-card {

        background:
            rgba(13, 21, 38, 0.75);

        border: 1px solid
            rgba(90, 174, 255, 0.14);

        border-radius: 18px;

        padding: 20px;

        height: 100%;

        box-shadow:
            0 8px 30px
            rgba(0, 0, 0, 0.20);
    }


    .feature-icon {

        font-size: 26px;

        margin-bottom: 10px;
    }


    .feature-title {

        font-weight: 700;

        font-size: 16px;

        color: #ffffff;

        margin-bottom: 6px;
    }


    .feature-description {

        color: #899bb9;

        font-size: 13px;

        line-height: 1.5;
    }


    /* ================================
       INPUT AREA
    ================================= */

    .input-label {

        color: #b7c7df;

        font-size: 14px;

        font-weight: 600;

        margin-bottom: 8px;
    }


    textarea {

        background-color: #0c1424 !important;

        color: #f4f8ff !important;

        border: 1px solid
            rgba(0, 200, 255, 0.18) !important;

        border-radius: 15px !important;
    }


    textarea:focus {

        border-color:
            #00c8ff !important;

        box-shadow:
            0 0 20px
            rgba(0, 200, 255, 0.12) !important;
    }


    /* ================================
       BUTTON
    ================================= */

    .stButton > button {

        width: 100%;

        border-radius: 14px;

        border: 1px solid
            rgba(0, 210, 255, 0.45);

        background:
            linear-gradient(
                90deg,
                #008cff,
                #6d4cff
            );

        color: white;

        font-weight: 700;

        padding: 13px 20px;

        transition: all 0.2s ease;

        box-shadow:
            0 0 20px
            rgba(0, 157, 255, 0.20);
    }


    .stButton > button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 0 30px
            rgba(0, 174, 255, 0.40);
    }


    /* ================================
       RESPONSE
    ================================= */

    .response-box {

        background:
            linear-gradient(
                145deg,
                rgba(12, 23, 42, 0.95),
                rgba(15, 19, 42, 0.95)
            );

        border:

            1px solid
            rgba(0, 200, 255, 0.18);

        border-radius: 20px;

        padding: 28px;

        margin-top: 25px;

        box-shadow:
            0 10px 40px
            rgba(0, 0, 0, 0.25);
    }


    /* ================================
       STATUS BADGES
    ================================= */

    .badge {

        display: inline-block;

        padding: 6px 12px;

        border-radius: 999px;

        font-size: 12px;

        font-weight: 600;

        margin-right: 6px;

        background:
            rgba(0, 174, 255, 0.10);

        border: 1px solid
            rgba(0, 174, 255, 0.20);

        color: #57dfff;
    }


    /* ================================
       FOOTER
    ================================= */

    .footer {

        text-align: center;

        color: #566681;

        font-size: 12px;

        margin-top: 50px;

        padding-top: 20px;

        border-top: 1px solid
            rgba(255, 255, 255, 0.05);
    }


    /* ================================
       MOBILE
    ================================= */

    @media (max-width: 768px) {

        .hero-title {
            font-size: 34px;
        }

        .hero {
            padding: 25px;
        }

        .hero-subtitle {
            font-size: 15px;
        }

        .block-container {
            padding: 1rem;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            font-size:28px;
            font-weight:800;
            margin-bottom:5px;
        ">
        🧠 Study Tutor
        </div>

        <div style="
            color:#6bdfff;
            font-size:13px;
            margin-bottom:30px;
        ">
        AI-powered learning companion
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown("### 🎯 Learning Settings")


    level = st.selectbox(
        "Your Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced",
        ],
    )


    mode = st.selectbox(
        "Learning Mode",
        [
            "Explain",
            "Ask a Question",
            "Quiz",
            "Study Plan",
        ],
    )


    st.markdown("---")


    st.markdown(
        """
        <div style="
            padding:15px;
            border-radius:14px;
            background:rgba(0,174,255,0.06);
            border:1px solid rgba(0,174,255,0.12);
        ">

        <div style="
            font-weight:700;
            margin-bottom:8px;
        ">
        ✨ Agent Capabilities
        </div>

        <div style="
            color:#899bb9;
            font-size:13px;
            line-height:1.8;
        ">
        🧠 Adaptive explanations<br>
        🛠️ Tool usage<br>
        💾 Persistent memory<br>
        📝 Quiz generation<br>
        📅 Study planning
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            Learn Smarter.<br>
            Think Deeper.
        </div>

        <div class="hero-subtitle">
            Meet your AI Study Tutor — an intelligent learning
            companion that explains concepts, answers questions,
            creates study plans and helps you practice.
        </div>

        <br>

        <span class="badge">⚡ Groq</span>
        <span class="badge">🧠 CrewAI</span>
        <span class="badge">💾 Memory</span>
        <span class="badge">🛠️ Tools</span>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">🧠</div>

            <div class="feature-title">
                Adaptive Learning
            </div>

            <div class="feature-description">
                Explanations adapt to your selected
                knowledge level.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">🛠️</div>

            <div class="feature-title">
                Smart Tools
            </div>

            <div class="feature-description">
                The agent can use tools when calculations
                or study planning are required.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">💾</div>

            <div class="feature-title">
                Memory
            </div>

            <div class="feature-description">
                Relevant learning context can be
                remembered between interactions.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col4:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">⚡</div>

            <div class="feature-title">
                Fast AI
            </div>

            <div class="feature-description">
                Powered by Groq and GPT-OSS 120B
                for responsive interactions.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# MAIN INPUT
# =========================================================

st.markdown(
    '<div class="input-label">What do you want to learn?</div>',
    unsafe_allow_html=True,
)


question = st.text_area(
    label="Study question",
    label_visibility="collapsed",
    placeholder=(
        "Ask anything...\n\n"
        "Example: Explain PCR to me as a beginner.\n"
        "Example: Create a 7-day study plan for immunology.\n"
        "Example: Quiz me about bacterial genetics."
    ),
    height=170,
)


# =========================================================
# ACTION
# =========================================================

if st.button(
    "✨ Ask Study Tutor",
    type="primary",
):

    if not question.strip():

        st.warning(
            "Please enter a topic or question first."
        )

    else:

        with st.spinner(
            "🧠 Study Tutor is thinking..."
        ):

            try:

                response = run_tutor(
                    question=question,
                    level=level,
                    mode=mode,
                )

                st.markdown(
                    """
                    <div class="response-box">
                    """,
                    unsafe_allow_html=True,
                )

                st.markdown(
                    "### ✨ Tutor Response"
                )

                st.markdown(response)

                st.markdown(
                    "</div>",
                    unsafe_allow_html=True,
                )

            except Exception as e:

                st.error(
                    "Something went wrong while running "
                    "the Study Tutor Agent."
                )

                with st.expander(
                    "Technical details"
                ):

                    st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        Study Tutor AI · Built with
        Streamlit + CrewAI + Groq

    </div>
    """,
    unsafe_allow_html=True,
)
