"""
Product Ad Generator - CrewAI Implementation
Main execution file for generating product advertisements
"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import ProductAdAgents
from tasks import ProductAdTasks

# Load environment variables
load_dotenv()


def generate_product_ad(
    product_info: dict,
    platform: str = "general",
    brand_guidelines: dict = None
) -> str:
    """
    Generate a complete product advertisement campaign

    Args:
        product_info: Dictionary containing product details
            Required keys: name, category, description, features
            Optional keys: target_market, price, competitors
        platform: Ad platform (social, search, display, email, general)
        brand_guidelines: Optional brand guidelines dict with colors, fonts, voice

    Returns:
        Complete ad campaign package as string
    """

    print(f"\n{'='*70}")
    print(f"Product Ad Generator - CrewAI Edition")
    print(f"{'='*70}")
    print(f"\nGenerating ad campaign for: {product_info.get('name', 'Unknown Product')}")
    print(f"Platform: {platform}")
    print(f"{'='*70}\n")

    # Initialize agents and tasks
    agents = ProductAdAgents()
    tasks_factory = ProductAdTasks()

    # Create agents
    market_researcher = agents.market_researcher()
    copywriter = agents.copywriter()
    visual_designer = agents.visual_designer()
    performance_analyst = agents.performance_analyst()
    brand_strategist = agents.brand_strategist()

    # Create tasks
    research_task = tasks_factory.research_target_audience(
        agent=market_researcher,
        product_info=product_info
    )

    copywriting_task = tasks_factory.create_ad_copy(
        agent=copywriter,
        product_info=product_info,
        platform=platform
    )
    copywriting_task.context = [research_task]

    design_task = tasks_factory.design_visual_strategy(
        agent=visual_designer,
        product_info=product_info,
        brand_guidelines=brand_guidelines
    )
    design_task.context = [research_task, copywriting_task]

    performance_task = tasks_factory.evaluate_ad_performance(
        agent=performance_analyst,
        product_info=product_info
    )
    performance_task.context = [research_task, copywriting_task, design_task]

    brand_task = tasks_factory.ensure_brand_alignment(
        agent=brand_strategist,
        product_info=product_info,
        brand_guidelines=brand_guidelines
    )
    brand_task.context = [research_task, copywriting_task, design_task]

    synthesis_task = tasks_factory.synthesize_ad_campaign(
        agent=brand_strategist,
        product_info=product_info
    )
    synthesis_task.context = [research_task, copywriting_task, design_task,
                              performance_task, brand_task]

    # Create crew
    crew = Crew(
        agents=[
            market_researcher,
            copywriter,
            visual_designer,
            performance_analyst,
            brand_strategist
        ],
        tasks=[
            research_task,
            copywriting_task,
            design_task,
            performance_task,
            brand_task,
            synthesis_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()

    return result


def main():
    """
    Main execution function with example usage
    """

    # Example product information
    product_info = {
        'name': 'SmartFit Pro Tracker',
        'category': 'Fitness Technology',
        'description': 'Advanced fitness tracker with AI-powered coaching and health monitoring',
        'features': [
            'Real-time heart rate monitoring',
            'AI-powered workout recommendations',
            'Sleep quality analysis',
            '7-day battery life',
            'Water-resistant up to 50m',
            'Integrated GPS tracking'
        ],
        'target_market': 'Health-conscious adults aged 25-45',
        'price': '$199',
        'competitors': ['Fitbit', 'Apple Watch', 'Garmin']
    }

    # Optional brand guidelines
    brand_guidelines = {
        'colors': ['Electric Blue (#0066FF)', 'Fresh Green (#00CC66)', 'Clean White (#FFFFFF)'],
        'fonts': ['Montserrat (Headlines)', 'Open Sans (Body)'],
        'voice': 'Energetic, motivating, and empowering'
    }

    # Generate ad campaign
    result = generate_product_ad(
        product_info=product_info,
        platform="social",
        brand_guidelines=brand_guidelines
    )

    # Display results
    print("\n" + "="*70)
    print("AD CAMPAIGN PACKAGE")
    print("="*70 + "\n")
    print(result)
    print("\n" + "="*70)


if __name__ == "__main__":
    main()
