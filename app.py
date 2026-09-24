import streamlit as st

from crew import run_tutor


st.set_page_config(
    page_title="Study Tutor Agent",
    page_icon="📚",
    layout="centered",
)


st.title("📚 Study Tutor Agent")

st.write(
    "Learn with an AI tutor that adapts to your level, "
    "uses tools when needed, and remembers study context."
)


# Sidebar
st.sidebar.header("Study Settings")

level = st.sidebar.selectbox(
    "Student Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced",
    ],
)


mode = st.sidebar.selectbox(
    "Learning Mode",
    [
        "Explain",
        "Ask a Question",
        "Quiz",
        "Study Plan",
    ],
)


st.sidebar.markdown("---")

st.sidebar.info(
    "Powered by CrewAI + Groq"
)


# Main input
question = st.text_area(
    "What would you like to study?",
    placeholder=(
        "Example: Explain PCR in simple terms.\n"
        "Or: Create a 7-day study plan for immunology."
    ),
    height=150,
)


if st.button("Ask Tutor", type="primary"):

    if not question.strip():

        st.warning("Please enter a topic or question.")

    else:

        with st.spinner("Study Tutor is thinking..."):

            try:

                response = run_tutor(
                    question=question,
                    level=level,
                    mode=mode,
                )

                st.markdown("### 👨‍🏫 Tutor")

                st.markdown(response)

            except Exception as e:

                st.error(
                    "Something went wrong while running the tutor."
                )

                st.exception(e)
