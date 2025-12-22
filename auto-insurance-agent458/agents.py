"""
Auto Insurance CrewAI Agents
Based on Cymbal Auto Insurance ADK sample
"""

from crewai import Agent
from tools import MembershipTool, ClaimsTool, RoadsideAssistanceTool, RewardsTool

membership_specialist = Agent(
    role="Membership Registration Specialist",
    goal="Register new members and manage member information",
    backstory="""You are a customer service specialist for Cymbal Auto Insurance
    focused on membership registration. You collect required information, create
    member accounts, and guide new members through the registration process.""",
    verbose=True,
    allow_delegation=False,
    tools=[MembershipTool()]
)

claims_handler = Agent(
    role="Insurance Claims Handler",
    goal="Process insurance claims with empathy and efficiency",
    backstory="""You are a claims specialist who helps members file claims for
    accidents, hail damage, and other incidents. You are empathetic, reassuring,
    and focused on making the claims process stress-free.""",
    verbose=True,
    allow_delegation=False,
    tools=[ClaimsTool()]
)

roadside_coordinator = Agent(
    role="Roadside Assistance Coordinator",
    goal="Dispatch roadside assistance services quickly",
    backstory="""You coordinate roadside assistance including towing, jump starts,
    fuel delivery, tire changes, and lockout services. You work quickly to get
    help to members in need.""",
    verbose=True,
    allow_delegation=False,
    tools=[RoadsideAssistanceTool()]
)

rewards_advisor = Agent(
    role="Rewards Program Advisor",
    goal="Help members find and use reward offers",
    backstory="""You help members discover nearby reward offers from partner
    companies including shops, restaurants, and theaters.""",
    verbose=True,
    allow_delegation=False,
    tools=[RewardsTool()]
)
