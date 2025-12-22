"""
Email Management CrewAI Tasks
"""

from crewai import Task
from agents import email_classifier, draft_writer, workflow_optimizer

def create_tasks(email_content: str, context: str = ""):
    classify_task = Task(
        description=f"""Classify this email:

{email_content}

{f"Context: {context}" if context else ""}

Determine:
- Type (inquiry, request, notification, marketing, etc.)
- Priority (urgent, high, normal, low)
- Action required
- Sentiment
- Suggested response time""",
        agent=email_classifier,
        expected_output="Email classification with priority and action recommendations"
    )

    draft_task = Task(
        description=f"""Draft appropriate response for:

{email_content}

Generate:
- Professional response
- Alternative casual version
- Key points to address
- Follow-up actions""",
        agent=draft_writer,
        expected_output="Professional email draft with variations",
        context=[classify_task]
    )

    optimize_task = Task(
        description="""Analyze email pattern and suggest:
        - Folder/label structure
        - Filter rules
        - Template opportunities
        - Automation suggestions
        - Time-saving strategies""",
        agent=workflow_optimizer,
        expected_output="Workflow optimization recommendations",
        context=[classify_task, draft_task]
    )

    return [classify_task, draft_task, optimize_task]
