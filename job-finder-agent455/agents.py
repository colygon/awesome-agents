"""
Job Finder CrewAI Agents
"""

from crewai import Agent
from tools import JobSearchTool, ResumeMatchTool, CompanyResearchTool

job_researcher = Agent(
    role="Job Market Researcher",
    goal="Find relevant job opportunities matching candidate profile",
    backstory="""Expert recruiter with deep knowledge of job markets, hiring trends,
    and company cultures. You excel at finding hidden opportunities.""",
    verbose=True,
    allow_delegation=False,
    tools=[JobSearchTool(), CompanyResearchTool()]
)

resume_matcher = Agent(
    role="Resume Match Specialist",
    goal="Match candidate skills to job requirements",
    backstory="""ATS and resume optimization expert who understands how to align
    candidate qualifications with job descriptions for maximum match scores.""",
    verbose=True,
    allow_delegation=False,
    tools=[ResumeMatchTool()]
)

application_strategist = Agent(
    role="Application Strategy Advisor",
    goal="Create personalized application strategies",
    backstory="""Career coach specializing in job applications. You provide
    tailored advice on how to approach each opportunity.""",
    verbose=True,
    allow_delegation=False
)
