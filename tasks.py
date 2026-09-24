from crewai import Task


def create_tutor_task(agent, question, level, mode):

    mode_instructions = {
        "Explain": """
Teach the requested topic clearly and progressively.

- Start with the basic concept.
- Break complex ideas into smaller sections.
- Adapt the explanation to the student's level.
- Use examples or analogies when helpful.
- Include practical applications when relevant.
- Focus on understanding rather than memorization.
""",

        "Ask a Question": """
Answer the student's question directly and accurately.

- Start with a clear answer.
- Explain the reasoning behind the answer.
- Add relevant details or examples when useful.
- Adapt the depth to the student's level.
- Do not turn the response into a quiz or study plan.
""",

        "Quiz": """
Create a quiz based on the student's requested topic.

- Generate 5 quiz questions.
- Adapt the difficulty to the student's level.
- Use multiple-choice questions.
- Give four options for each question: A, B, C, and D.
- Clearly identify the correct answer after each question.
- Give a short explanation for each correct answer.
- Cover different concepts from the requested topic.
- Do not provide a long lesson before the quiz.
- Present each question clearly and separately.
""",

        "Study Plan": """
Create a practical study plan for the requested topic.

- Break the topic into logical learning sessions.
- Organize the material in a sensible order.
- Include what the student should learn in each session.
- Suggest practice and revision activities.
- Adapt the plan to the student's level.
- If the student provides a duration, follow it.
- If the student provides available study time, consider it.
- Use the Study Planner tool when genuinely useful.
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
2. Adapt the response to the student's level.
3. Use simple language for beginners.
4. Use appropriate technical terminology for advanced students.
5. Use examples or analogies when useful.
6. Use available tools only when genuinely necessary.
7. Do not invent facts.
8. If the request is unclear, state your assumption.
9. Encourage understanding rather than memorization.
10. Keep the response well structured and readable.

For Explain and Ask a Question modes:
End the response with a short "Key Takeaway".

For Quiz mode:
Generate the quiz questions and provide the correct answer
and a short explanation after each question.
""",

        expected_output=(
            "A clear, accurate and educational response that follows "
            "the selected learning mode and is appropriate for the "
            "student's level."
        ),

        agent=agent,
    )
