"""
Career Counselor - Agent 487 CrewAI Integration
Main orchestration file for career guidance and job search multi-agent system
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_all_agents
from tasks import create_all_tasks

# Load environment variables
load_dotenv()


def create_career_counseling_crew(career_request):
    """
    Create and configure the career counseling crew
    """
    # Create the three specialized agents
    agents = create_all_agents(model="gpt-4", temperature=0.7)

    # Create tasks for each agent
    tasks = create_all_tasks(agents, career_request)

    # Create the crew with sequential process
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    return crew


def get_career_guidance(career_request):
    """
    Get comprehensive career counseling using the CrewAI multi-agent system

    Args:
        career_request: Dictionary or string with career situation and goals

    Returns:
        Complete career package with guidance, application materials, and job search strategy
    """
    print("\n" + "="*80)
    print("CAREER COUNSELOR - AGENT 487 CREWAI SYSTEM")
    print("="*80)
    print(f"\nCareer Request: {career_request}\n")
    print("="*80 + "\n")

    # Create and run the crew
    crew = create_career_counseling_crew(career_request)
    result = crew.kickoff()

    print("\n" + "="*80)
    print("CAREER COUNSELING COMPLETE")
    print("="*80 + "\n")

    return result


if __name__ == "__main__":
    # Example usage
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
    else:
        # Test with sample career counseling request
        sample_request = {
            "career_situation": """Currently working as a Marketing Coordinator (3 years experience)
                                  at a mid-size B2B software company. Background in communications
                                  and digital marketing. Strong skills in content creation, social
                                  media, email marketing, and some analytics. Interested in moving
                                  into Product Marketing or Growth Marketing roles. Want to work at
                                  a tech startup or fast-growing company. Willing to learn new skills
                                  but not sure what gaps to fill. Salary currently $65k, hoping to
                                  get to $80-90k range.""",

            "application_needs": """Need to update my resume - it's been 3 years since I job searched.
                                   Current resume is too focused on tasks rather than achievements.
                                   Want to apply for Product Marketing Manager roles at tech companies.
                                   Nervous about interviews, especially behavioral questions and
                                   explaining why I want to make this shift. Also need to negotiate
                                   better this time - accepted lowball offer last time.""",

            "search_parameters": """Looking to start active job search in SF Bay Area (open to remote).
                                   Target companies: Tech startups (Series A-C), product-led growth
                                   companies, B2B SaaS. Want to leverage my network but not sure how
                                   to do informational interviews. LinkedIn profile is outdated.
                                   Timeline: Hope to land new role in 2-3 months. Need strategy for
                                   finding unadvertised opportunities and getting referrals."""
        }

        result = get_career_guidance(sample_request)
        print("\nCareer Guidance Package:")
        print(result)
