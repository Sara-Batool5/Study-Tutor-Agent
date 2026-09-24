import crewai.llms.cache as _crewai_cache

_crewai_cache.mark_cache_breakpoint = lambda msg: msg

from crewai import Crew, Process

from agents import create_study_tutor
from tasks import create_tutor_task
from memory import get_memory


def run_tutor(question, level, mode):
    """
    Run the Study Tutor Agent.
    """

    tutor = create_study_tutor()

    task = create_tutor_task(
        agent=tutor,
        question=question,
        level=level,
        mode=mode,
    )

    memory = get_memory()

    crew = Crew(
        agents=[tutor],
        tasks=[task],
        process=Process.sequential,
        memory=memory,
        verbose=True,
    )

    result = crew.kickoff()

    return str(result)
