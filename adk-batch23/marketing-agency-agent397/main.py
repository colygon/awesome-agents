#!/usr/bin/env python3
"""
Marketing Agency CrewAI Agent
Converts Google ADK Marketing Agency to CrewAI implementation

Streamlines website and product launches with domain suggestions,
website generation, marketing strategies, and brand assets.
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import datetime
import json

# Initialize OpenAI LLM (replacing Gemini)
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.8,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize search tool
search_tool = SerperDevTool()

# Define Agents

# 1. Marketing Strategist Agent
strategist = Agent(
    role="Marketing Strategy Director",
    goal="Develop comprehensive marketing strategies for product and website launches",
    backstory="""You are a senior marketing strategist with expertise in brand
    positioning, market analysis, and go-to-market strategies. You create
    data-driven marketing plans that maximize launch success.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Content Creator Agent
content_creator = Agent(
    role="Creative Content Director",
    goal="Generate compelling marketing content, copy, and brand messaging",
    backstory="""You are a creative content director who crafts persuasive
    marketing copy, website content, and brand messaging. You excel at
    storytelling and creating content that resonates with target audiences.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Technical Marketing Analyst
analyst = Agent(
    role="Marketing Analytics Specialist",
    goal="Analyze market data, recommend domains, and optimize marketing performance",
    backstory="""You are a marketing analytics specialist who analyzes market
    trends, evaluates domain options, and provides data-driven recommendations
    for marketing optimization.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

def create_launch_campaign(
    product_name: str,
    product_description: str,
    target_audience: str,
    budget: str = "medium"
) -> dict:
    """
    Create comprehensive marketing campaign for product/website launch

    Args:
        product_name: Name of product or website
        product_description: Description of product/service
        target_audience: Target audience description
        budget: Marketing budget (low/medium/high)

    Returns:
        dict with strategy, content, recommendations
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: Market Analysis & Domain Recommendations
    analysis_task = Task(
        description=f"""Conduct market analysis and provide recommendations:
        - Product/Website: {product_name}
        - Description: {product_description}
        - Target Audience: {target_audience}
        - Budget: {budget}

        Analyze:
        1. Market landscape and competitors
        2. Target audience insights and demographics
        3. Domain name suggestions (5-10 options with availability likelihood)
        4. Market positioning opportunities
        5. Key differentiators

        Use web search to research competitors and market trends.
        Current date: {current_date}

        Provide comprehensive market analysis report.""",
        agent=analyst,
        expected_output="Market analysis with domain recommendations and positioning insights"
    )

    # Task 2: Marketing Strategy Development
    strategy_task = Task(
        description=f"""Develop comprehensive marketing strategy:
        - Product/Website: {product_name}
        - Description: {product_description}
        - Target Audience: {target_audience}
        - Budget: {budget}

        Create:
        1. Go-to-Market Strategy
        2. Channel Selection (social, email, content, paid ads, etc.)
        3. Campaign Timeline and Milestones
        4. Key Performance Indicators (KPIs)
        5. Budget Allocation Recommendations
        6. Launch Phase Strategy (pre-launch, launch, post-launch)

        Base recommendations on market analysis and budget constraints.""",
        agent=strategist,
        expected_output="Complete marketing strategy with timeline and KPIs",
        context=[analysis_task]
    )

    # Task 3: Content & Creative Assets
    content_task = Task(
        description=f"""Generate marketing content and creative direction:
        - Product/Website: {product_name}
        - Description: {product_description}
        - Target Audience: {target_audience}

        Create:
        1. Brand Messaging Framework
           - Tagline options (5-7 variations)
           - Value proposition
           - Key messages

        2. Website Content Plan
           - Homepage copy outline
           - Key page structures (About, Features, Pricing, Contact)
           - Call-to-action recommendations

        3. Marketing Copy
           - Email campaign templates (welcome, announcement, nurture)
           - Social media post ideas (10+ posts)
           - Ad copy variations for different channels

        4. Brand Asset Recommendations
           - Color palette suggestions
           - Typography recommendations
           - Visual style direction
           - Logo concept ideas

        Ensure all content aligns with marketing strategy and brand positioning.""",
        agent=content_creator,
        expected_output="Comprehensive content package with messaging, copy, and brand guidelines",
        context=[strategy_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[analyst, strategist, content_creator],
        tasks=[analysis_task, strategy_task, content_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "market_analysis": analysis_task.output.raw if hasattr(analysis_task, 'output') else "",
        "marketing_strategy": strategy_task.output.raw if hasattr(strategy_task, 'output') else "",
        "content_package": str(result),
        "metadata": {
            "product_name": product_name,
            "product_description": product_description,
            "target_audience": target_audience,
            "budget": budget,
            "date": current_date
        }
    }

def save_campaign(content: str, filename: str):
    """Save marketing campaign to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Marketing Campaign Plan\n\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(content)

    print(f"\nCampaign plan saved to: {filename}")

if __name__ == "__main__":
    print("Marketing Agency CrewAI Agent")
    print("=" * 50)
    print("Product & Website Launch Campaign Generator")
    print("=" * 50)

    # Get product/website details
    product_name = input("\nProduct/Website name: ").strip()
    if not product_name:
        product_name = "InnovateApp"

    product_description = input("Brief description: ").strip()
    if not product_description:
        product_description = "A productivity app that helps teams collaborate better"

    target_audience = input("Target audience: ").strip()
    if not target_audience:
        target_audience = "Small to medium-sized businesses and remote teams"

    budget = input("Marketing budget (low/medium/high): ").strip().lower()
    if budget not in ['low', 'medium', 'high']:
        budget = "medium"

    print(f"\nGenerating launch campaign...")
    print(f"Product: {product_name}")
    print(f"Description: {product_description}")
    print(f"Audience: {target_audience}")
    print(f"Budget: {budget}")

    # Create campaign
    result = create_launch_campaign(
        product_name=product_name,
        product_description=product_description,
        target_audience=target_audience,
        budget=budget
    )

    # Display result
    print("\n" + "=" * 50)
    print("MARKETING CAMPAIGN PLAN")
    print("=" * 50)
    print(result["content_package"])

    # Save option
    save = input("\n\nSave campaign plan to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_campaign(result["content_package"], filename)
        else:
            save_campaign(result["content_package"], f"{product_name.lower().replace(' ', '-')}-campaign")
