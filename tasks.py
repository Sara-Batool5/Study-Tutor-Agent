from crewai import Task


def create_tutor_task(agent, question, level, mode):
    """
    Create the task for the Study Tutor Agent.
    """

    task = Task(
        description=f"""
You are tutoring a student.

Student level:
{level}

Learning mode:
{mode}

Student request:
{question}

Instructions:

1. Understand exactly what the student is asking.
2. Adapt your explanation to the student's level.
3. Use simple language when appropriate.
4. Break complicated concepts into smaller parts.
5. Use examples when they improve understanding.
6. Use an available tool when it is genuinely useful.
7. Do not use tools unnecessarily.
8. Encourage active learning.
9. If the student asks for a quiz, provide questions appropriate
   for their level.
10. If the student asks for a study plan, create a practical plan.
11. If the question is ambiguous, explain your assumption.
12. Do not invent scientific facts.
13. End with a short "Key Takeaway" section.

Return a clear and well-structured educational response.
""",
        expected_output=(
            "A clear educational response adapted to the student's "
            "level, with useful explanations, examples when appropriate, "
            "and a short Key Takeaway."
        ),
        agent=agent,
    )

    return task
