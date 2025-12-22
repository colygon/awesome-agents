"""
Email Management CrewAI Agents
"""

from crewai import Agent
from tools import EmailClassifierTool, DraftGeneratorTool, PriorityAnalyzerTool

email_classifier = Agent(
    role="Email Classification Specialist",
    goal="Classify and organize emails by type and priority",
    backstory="""Expert in email management and inbox zero methodologies.
    You categorize emails accurately and identify what needs attention.""",
    verbose=True,
    allow_delegation=False,
    tools=[EmailClassifierTool(), PriorityAnalyzerTool()]
)

draft_writer = Agent(
    role="Email Draft Writer",
    goal="Generate professional email responses",
    backstory="""Professional communicator skilled in crafting clear, appropriate
    email responses for various contexts and audiences.""",
    verbose=True,
    allow_delegation=False,
    tools=[DraftGeneratorTool()]
)

workflow_optimizer = Agent(
    role="Email Workflow Optimizer",
    goal="Optimize email workflow and suggest automation",
    backstory="""Productivity expert who streamlines email workflows, suggests
    filters, templates, and automation opportunities.""",
    verbose=True,
    allow_delegation=False
)
