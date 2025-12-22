#!/usr/bin/env python
from crewai import Crew, Process
from agents import SocialMediaManagerAgents
from tasks import SocialMediaManagerTasks
from dotenv import load_dotenv

load_dotenv()

def run_social_media_manager():
    """
    Run the Social Media Manager crew to plan and execute social media campaigns
    """
    print("## Welcome to the Social Media Manager Crew")
    print("--------------------------------------------")

    # Get user input for social media campaign
    brand_name = input("What is your brand/company name? ")
    industry = input("What industry are you in? ")
    target_audience = input("Who is your target audience? ")
    campaign_goal = input("What is your campaign goal? (e.g., brand awareness, lead generation): ")

    brand_info = f"""
    Brand: {brand_name}
    Industry: {industry}
    Target Audience: {target_audience}
    Campaign Goal: {campaign_goal}
    """

    campaign_details = f"""
    Campaign for {brand_name}
    Goal: {campaign_goal}
    Target Audience: {target_audience}
    Platforms: Instagram, Twitter, LinkedIn, Facebook
    """

    content_calendar = f"""
    30-day content calendar for {brand_name}
    Mix of promotional, educational, and engaging content
    """

    # Initialize agents
    agents = SocialMediaManagerAgents()
    tasks_manager = SocialMediaManagerTasks()

    # Create agents
    content_strategist = agents.content_strategist()
    copywriter = agents.copywriter()
    scheduling_manager = agents.scheduling_manager()
    analytics_specialist = agents.analytics_specialist()

    # Create tasks
    strategy_task = tasks_manager.develop_content_strategy(
        content_strategist,
        brand_info
    )

    content_task = tasks_manager.create_social_posts(
        copywriter,
        campaign_details
    )

    scheduling_task = tasks_manager.schedule_content(
        scheduling_manager,
        content_calendar
    )

    tracking_task = tasks_manager.track_performance(
        analytics_specialist,
        "CAMPAIGN_001"
    )

    report_task = tasks_manager.generate_monthly_report(
        analytics_specialist,
        brand_info
    )

    # Create and run crew
    crew = Crew(
        agents=[
            content_strategist,
            copywriter,
            scheduling_manager,
            analytics_specialist
        ],
        tasks=[
            strategy_task,
            content_task,
            scheduling_task,
            tracking_task,
            report_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Social Media Manager Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_social_media_manager()
