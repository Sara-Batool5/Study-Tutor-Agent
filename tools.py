from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.

    Use this tool when the student asks for a mathematical calculation.
    Example: 25 * 48
    """

    try:
        allowed_characters = "0123456789+-*/(). "

        if not all(char in allowed_characters for char in expression):
            return "Invalid mathematical expression."

        result = eval(expression, {"__builtins__": {}}, {})

        return f"Result: {result}"

    except Exception:
        return "I could not calculate that expression."


@tool("Study Planner")
def study_planner(topic: str, days: int, hours_per_day: float) -> str:
    """
    Create a simple study plan for a topic.

    Use this tool when the student asks for a study schedule.
    """

    if days <= 0:
        return "Number of days must be greater than zero."

    if hours_per_day <= 0:
        return "Hours per day must be greater than zero."

    total_hours = days * hours_per_day

    plan = f"""
Study Plan
Topic: {topic}
Duration: {days} days
Hours per day: {hours_per_day}
Total study time: {total_hours} hours

Suggested structure:

Day 1:
Understand the basic concepts.

Day 2:
Study important terms and mechanisms.

Day 3:
Review examples and applications.

Day 4:
Practice questions.

Day 5:
Review difficult areas.

Remaining days:
Revision, practice and self-testing.
"""

    return plan
