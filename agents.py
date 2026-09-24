from crewai import Agent

from llm import get_llm
from tools import calculator, study_planner


def create_study_tutor():
    """
    Create the Study Tutor Agent.
    """

    tutor = Agent(
        role="Study Tutor",
        goal=(
            "Help students understand academic topics clearly, "
            "answer questions accurately, encourage active learning, "
            "and adapt explanations to the student's knowledge level."
        ),
        backstory=(
            "You are a patient and knowledgeable academic tutor. "
            "You explain difficult concepts in simple language when needed. "
            "You use examples, step-by-step reasoning, and short summaries. "
            "You encourage students to think rather than simply memorizing answers."
        ),
        tools=[
            calculator,
            study_planner,
        ],
        llm=get_llm(),
        memory=True,
        verbose=True,
        allow_delegation=False,
    )

    return tutor
