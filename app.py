import streamlit as st

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="🧠",
    layout="wide",
)

st.markdown("""
<style>
.stApp {
    background: #070b14;
    color: white;
}

.title {
    font-size: 48px;
    font-weight: 800;
    color: #38d9ff;
}

.subtitle {
    color: #a9b9d6;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="title">Learn Smarter.<br>Think Deeper.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="subtitle">Your AI Study Tutor</div>',
    unsafe_allow_html=True,
)

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

if st.button("✨ Ask Study Tutor", type="primary"):
    st.write("Your question was:", question)
    st.write("Level:", level)
    st.write("Mode:", mode)
