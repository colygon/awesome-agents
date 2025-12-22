"""
Incident Management CrewAI Tasks
"""

from crewai import Task
from agents import incident_coordinator, status_tracker, resolution_specialist

def create_tasks(action: str, incident_number: str = None, description: str = ""):
    if action == "create":
        return [Task(
            description=f"""Create new ServiceNow incident:

Description: {description}

Steps:
- Collect incident details
- Determine priority and category
- Create incident in ServiceNow
- Assign to appropriate team
- Provide incident number""",
            agent=incident_coordinator,
            expected_output="Incident number and initial status"
        )]

    elif action == "status":
        return [Task(
            description=f"""Check status of incident: {incident_number}

Provide:
- Current status
- Assigned team
- Progress updates
- Estimated resolution time""",
            agent=status_tracker,
            expected_output="Incident status and timeline"
        )]

    elif action == "resolve":
        return [
            Task(
                description=f"""Research solution for: {description}

Find:
- Known solutions
- Workarounds
- Knowledge base articles
- Similar past incidents""",
                agent=resolution_specialist,
                expected_output="Solution recommendations"
            ),
            Task(
                description=f"""Update and close incident: {incident_number}

Provide:
- Resolution summary
- Root cause
- Prevention steps""",
                agent=incident_coordinator,
                expected_output="Incident closure confirmation",
                context=[]
            )
        ]

    return []
