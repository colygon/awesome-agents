"""
Job Finder CrewAI Tasks
"""

from crewai import Task
from agents import job_researcher, resume_matcher, application_strategist

def create_tasks(job_title: str, location: str, skills: list):
    search_task = Task(
        description=f"""Find {job_title} positions in {location}.
        Required skills: {skills}

        Search for:
        - Direct matches
        - Adjacent roles
        - Remote opportunities
        - Company culture fit""",
        agent=job_researcher,
        expected_output="List of 10-20 relevant job opportunities with company info"
    )

    match_task = Task(
        description=f"""Analyze job matches for candidate with skills: {skills}

        For each job:
        - Calculate match percentage
        - Identify skill gaps
        - Highlight transferable skills
        - Suggest improvements""",
        agent=resume_matcher,
        expected_output="Ranked job list with match scores and gap analysis",
        context=[search_task]
    )

    strategy_task = Task(
        description="""Create application strategy:
        - Prioritize top 5 opportunities
        - Customize approach for each
        - Draft cover letter points
        - Networking recommendations
        - Timeline for applications""",
        agent=application_strategist,
        expected_output="Personalized application plan with priorities and tactics",
        context=[search_task, match_task]
    )

    return [search_task, match_task, strategy_task]
