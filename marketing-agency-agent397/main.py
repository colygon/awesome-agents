#!/usr/bin/env python
from crewai import Crew, Process
from agents import MarketingAgencyAgents
from tasks import MarketingAgencyTasks
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def run_marketing_campaign(product: str, industry: str, objective: str, budget: str = "$10,000", channels: str = "social,email,content"):
    """
    Run a comprehensive marketing campaign using a team of marketing specialists.

    Args:
        product: Product or service to market
        industry: Industry sector
        objective: Campaign objective (awareness, leads, sales)
        budget: Marketing budget
        channels: Marketing channels (comma-separated)
    """
    print(f"\n{'='*60}")
    print(f"Marketing Campaign Starting")
    print(f"Product: {product}")
    print(f"Industry: {industry}")
    print(f"Objective: {objective}")
    print(f"Budget: {budget}")
    print(f"Channels: {channels}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = MarketingAgencyAgents()
    tasks = MarketingAgencyTasks()

    # Create agents
    market_researcher = agents.market_researcher()
    brand_strategist = agents.brand_strategist()
    content_creator = agents.content_creator()
    seo_specialist = agents.seo_specialist()
    campaign_manager = agents.campaign_manager()

    # Create tasks
    research_task = tasks.conduct_market_research(
        agent=market_researcher,
        product=product,
        industry=industry
    )

    strategy_task = tasks.develop_brand_strategy(
        agent=brand_strategist,
        product=product,
        market_research="Use market research findings"
    )

    content_task = tasks.create_content_calendar(
        agent=content_creator,
        brand_strategy="Use brand strategy",
        channels=channels,
        duration="3 months"
    )

    seo_task = tasks.optimize_for_search(
        agent=seo_specialist,
        content="Optimize content calendar items",
        keywords=f"{product} keywords"
    )

    campaign_task = tasks.create_campaign(
        agent=campaign_manager,
        objective=objective,
        budget=budget,
        channels=channels,
        timeline="90 days"
    )

    # Create crew
    crew = Crew(
        agents=[
            market_researcher,
            brand_strategist,
            content_creator,
            seo_specialist,
            campaign_manager
        ],
        tasks=[
            research_task,
            strategy_task,
            content_task,
            seo_task,
            campaign_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Marketing Campaign Plan Complete!")
    print(f"{'='*60}\n")
    print(result)

    # Save campaign plan
    output_file = f"marketing_campaign_{product.replace(' ', '_').lower()}.txt"
    with open(output_file, 'w') as f:
        f.write(str(result))
    print(f"\nCampaign plan saved to: {output_file}")

    return result

def analyze_campaign_performance(campaign_name: str):
    """
    Analyze performance of an existing marketing campaign.
    """
    print(f"\n{'='*60}")
    print(f"Analyzing Campaign: {campaign_name}")
    print(f"{'='*60}\n")

    agents = MarketingAgencyAgents()
    tasks = MarketingAgencyTasks()

    campaign_manager = agents.campaign_manager()

    analysis_task = tasks.measure_and_report(
        agent=campaign_manager,
        campaign_data=f"Performance data for {campaign_name}",
        metrics="reach,engagement,conversions,roi"
    )

    crew = Crew(
        agents=[campaign_manager],
        tasks=[analysis_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Campaign Analysis Complete!")
    print(f"{'='*60}\n")
    print(result)

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  New campaign:  python main.py new <product> <industry> <objective> [budget] [channels]")
        print("  Analyze:       python main.py analyze <campaign_name>")
        print("\nExamples:")
        print("  python main.py new 'SaaS Platform' 'B2B Software' 'lead_generation' '$50000' 'social,email,content,ppc'")
        print("  python main.py analyze 'Q4_2024_Campaign'")
        print("\nObjective options: awareness, lead_generation, sales, retention")
        print("Channel options: social, email, content, ppc, seo, display, video")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new":
        if len(sys.argv) < 5:
            print("Error: Product, industry, and objective required")
            print("Usage: python main.py new <product> <industry> <objective> [budget] [channels]")
            sys.exit(1)

        product = sys.argv[2]
        industry = sys.argv[3]
        objective = sys.argv[4]
        budget = sys.argv[5] if len(sys.argv) > 5 else "$10000"
        channels = sys.argv[6] if len(sys.argv) > 6 else "social,email,content"

        run_marketing_campaign(product, industry, objective, budget, channels)

    elif command == "analyze":
        if len(sys.argv) < 3:
            print("Error: Campaign name required")
            print("Usage: python main.py analyze <campaign_name>")
            sys.exit(1)

        campaign_name = sys.argv[2]
        analyze_campaign_performance(campaign_name)

    else:
        print(f"Unknown command: {command}")
        print("Use 'new' to create a campaign or 'analyze' to analyze performance")
        sys.exit(1)
