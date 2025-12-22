"""
Incident Management CrewAI Agents
ServiceNow integration for IT incident management
"""

from crewai import Agent
from tools import IncidentCreationTool, IncidentStatusTool, KnowledgeBaseTool

incident_coordinator = Agent(
    role="IT Incident Coordinator",
    goal="Create and manage IT incidents in ServiceNow",
    backstory="""You are an IT service desk coordinator who manages incidents
    in ServiceNow. You collect incident details, assign priorities, and ensure
    proper categorization and routing.""",
    verbose=True,
    allow_delegation=False,
    tools=[IncidentCreationTool(), KnowledgeBaseTool()]
)

status_tracker = Agent(
    role="Incident Status Tracker",
    goal="Monitor and update incident status",
    backstory="""You track incident progress, provide status updates, and
    ensure incidents are resolved within SLA timelines.""",
    verbose=True,
    allow_delegation=False,
    tools=[IncidentStatusTool()]
)

resolution_specialist = Agent(
    role="Incident Resolution Specialist",
    goal="Provide solutions and workarounds for incidents",
    backstory="""You are an IT specialist who provides solutions, workarounds,
    and guidance for resolving incidents based on knowledge base articles.""",
    verbose=True,
    allow_delegation=False,
    tools=[KnowledgeBaseTool()]
)
