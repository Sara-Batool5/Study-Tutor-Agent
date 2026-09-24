from crewai import Task


def create_tutor_task(
    agent,
    question,
    level,
    mode
):
    mode_instructions = {
        "Explain": """
Teach the requested topic clearly and progressively.

- Start with the basic concept.
- Break complex ideas into smaller sections.
- Adapt the explanation to the student's level.
- Use examples or analogies when helpful.
- Include important practical applications when relevant.
- Focus on understanding rather than memorization.
""",

        "Ask a Question": """
Answer the student's question directly and accurately.

- Start with a clear answer.
- Explain the reasoning behind the answer.
- Add relevant details or examples when useful.
- Adapt the depth to the student's level.
- Do not unnecessarily turn the response into a quiz or study plan.
""",

        "Quiz": """
Act as an interactive quiz tutor.

- Create a quiz based on the student's requested topic.
- Adapt the difficulty to the student's level.
- Ask one question at a time.
- Do NOT reveal the answer immediately.
- Ask the student to provide their answer.
- When the student provides an answer, evaluate it.
- Explain why the answer is correct or incorrect.
- Then provide the next question.
- Keep track of the student's progress when possible.
""",

        "Study Plan": """
Create a practical study plan for the requested topic.

- Break the topic into logical learning sessions.
- Organize the material in a sensible order.
- Include what the student should learn in each session.
- Suggest practice or revision activities.
- Adapt the plan to the student's level.
- If the student provides a duration, follow it.
- If the student provides available study time, consider it.
- Use the Study Planner tool when it is genuinely useful.
"""
    }

    selected_instructions = mode_instructions.get(
        mode,
        mode_instructions["Explain"]
    )

    return Task(
        description=f"""
You are helping a student learn.

Student level:
{level}

Learning mode:
{mode}

Student request:
{question}

Follow these learning-mode instructions:

{selected_instructions}

General tutor instructions:

1. Be clear, accurate, patient, and encouraging.
2. Adapt the explanation to the student's level.
3. Use simple language when the student is a beginner.
4. Use more technical terminology when appropriate for advanced students.
5. Use examples, analogies, or practical applications when useful.
6. Use available tools only when genuinely necessary.
7. Do not invent facts.
8. If the student's request is unclear, state your assumption.
9. Encourage active learning and understanding.
10. Keep the response well structured and easy to read.

For Explain and Ask a Question modes:
End the response with a short "Key Takeaway".

For Quiz mode:
Do not provide the answer to a new question before the student attempts it.
""",

        expected_output=(
            "A clear, accurate and educational response that follows "
            "the selected learning mode and is appropriate for the "
            "student's level."
        ),

        agent=agent,
    )
