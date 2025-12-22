#!/usr/bin/env python3
"""
Personalized Shopping CrewAI Agent
Converts Google ADK Personalized Shopping to CrewAI implementation

E-commerce shopping assistant providing personalized product recommendations.
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
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize search tool
search_tool = SerperDevTool()

# Define Agents

# 1. Preference Analyzer Agent
preference_analyzer = Agent(
    role="Customer Preference Analyst",
    goal="Analyze customer preferences, needs, and shopping behavior",
    backstory="""You are an expert at understanding customer preferences and
    shopping patterns. You analyze customer information, past purchases, and
    stated needs to build comprehensive preference profiles.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Product Researcher Agent
product_researcher = Agent(
    role="Product Research Specialist",
    goal="Research and evaluate products based on customer preferences",
    backstory="""You are a product research specialist who finds and evaluates
    products across various e-commerce platforms. You compare features, prices,
    reviews, and specifications to identify the best options.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Recommendation Engine Agent
recommendation_engine = Agent(
    role="Personalized Recommendation Expert",
    goal="Generate personalized product recommendations with detailed rationale",
    backstory="""You are an expert at creating personalized product recommendations.
    You synthesize preference analysis and product research to suggest items that
    best match customer needs, preferences, and budget.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def get_shopping_recommendations(
    product_category: str,
    preferences: dict,
    budget_range: str = "medium",
    num_recommendations: int = 5
) -> dict:
    """
    Get personalized shopping recommendations

    Args:
        product_category: Category of products (e.g., "laptop", "running shoes")
        preferences: Dict with customer preferences
        budget_range: Budget level (low/medium/high) or specific range
        num_recommendations: Number of recommendations to generate

    Returns:
        dict with preference_analysis, product_research, recommendations
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Build preference description
    pref_description = "\n".join([f"- {k}: {v}" for k, v in preferences.items()])

    # Task 1: Analyze Preferences
    preference_task = Task(
        description=f"""Analyze customer preferences for {product_category}:

        Customer Preferences:
        {pref_description}

        Budget: {budget_range}

        Analyze:
        1. Key requirements and must-have features
        2. Nice-to-have features
        3. Deal-breakers or items to avoid
        4. Style and aesthetic preferences
        5. Use case scenarios
        6. Priority ranking of preferences

        Create a comprehensive preference profile to guide product search.
        Current date: {current_date}""",
        agent=preference_analyzer,
        expected_output="Detailed customer preference profile with prioritized requirements"
    )

    # Task 2: Product Research
    research_task = Task(
        description=f"""Research {product_category} products matching the preference profile:

        Product Category: {product_category}
        Budget: {budget_range}
        Number of Options Needed: {num_recommendations}

        Research and evaluate:
        1. Available products in the market
        2. Product specifications and features
        3. Customer reviews and ratings
        4. Price comparisons
        5. Brand reputation
        6. Availability and shipping options

        Use web search to find current products and reviews.
        Identify {num_recommendations}+ strong candidates that match preferences.

        Provide detailed product research with specifications and pricing.""",
        agent=product_researcher,
        expected_output=f"Research report on {num_recommendations}+ candidate products with detailed specs",
        context=[preference_task]
    )

    # Task 3: Generate Recommendations
    recommendation_task = Task(
        description=f"""Generate {num_recommendations} personalized product recommendations:

        Product Category: {product_category}
        Budget: {budget_range}

        For each recommendation, provide:
        1. Product name and brand
        2. Key specifications
        3. Price and availability
        4. Why it matches customer preferences (detailed rationale)
        5. Pros and cons
        6. Best for (specific use case)
        7. Rating/Review summary
        8. Where to buy (retailers/links)

        Rank recommendations from best to {num_recommendations}th best match.
        Ensure recommendations span different price points within budget range.

        Format as a clear, easy-to-read recommendation list.""",
        agent=recommendation_engine,
        expected_output=f"Personalized list of {num_recommendations} products with detailed rationale",
        context=[research_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[preference_analyzer, product_researcher, recommendation_engine],
        tasks=[preference_task, research_task, recommendation_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "preference_analysis": preference_task.output.raw if hasattr(preference_task, 'output') else "",
        "product_research": research_task.output.raw if hasattr(research_task, 'output') else "",
        "recommendations": str(result),
        "metadata": {
            "product_category": product_category,
            "preferences": preferences,
            "budget_range": budget_range,
            "num_recommendations": num_recommendations,
            "date": current_date
        }
    }

def save_recommendations(content: str, filename: str):
    """Save recommendations to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Personalized Shopping Recommendations\n\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(content)

    print(f"\nRecommendations saved to: {filename}")

def interactive_shopping_assistant():
    """Interactive shopping assistant"""
    print("Personalized Shopping CrewAI Agent")
    print("=" * 50)
    print("AI-Powered Shopping Recommendation System")
    print("=" * 50)

    # Get product category
    product_category = input("\nWhat are you shopping for? ").strip()
    if not product_category:
        product_category = "laptop"

    # Collect preferences
    print(f"\nLet's understand your preferences for {product_category}:")
    print("(Press Enter to skip any question)\n")

    preferences = {}

    # Common preference questions
    if input("Any specific brands you prefer? ").strip():
        preferences["preferred_brands"] = input("Preferred brands: ").strip()

    if input("Any brands to avoid? ").strip():
        preferences["brands_to_avoid"] = input("Brands to avoid: ").strip()

    primary_use = input("Primary use case/purpose: ").strip()
    if primary_use:
        preferences["primary_use"] = primary_use

    must_have = input("Must-have features: ").strip()
    if must_have:
        preferences["must_have_features"] = must_have

    nice_to_have = input("Nice-to-have features: ").strip()
    if nice_to_have:
        preferences["nice_to_have_features"] = nice_to_have

    style_pref = input("Style/aesthetic preferences: ").strip()
    if style_pref:
        preferences["style_preferences"] = style_pref

    other_pref = input("Any other preferences or requirements: ").strip()
    if other_pref:
        preferences["other_preferences"] = other_pref

    # Budget
    budget_range = input("\nBudget range (e.g., 'under $500', 'low', 'medium', 'high'): ").strip()
    if not budget_range:
        budget_range = "medium"

    # Number of recommendations
    try:
        num_recs = int(input("Number of recommendations (default 5): ").strip() or "5")
    except ValueError:
        num_recs = 5

    print(f"\nGenerating {num_recs} personalized recommendations for {product_category}...")

    # Get recommendations
    result = get_shopping_recommendations(
        product_category=product_category,
        preferences=preferences,
        budget_range=budget_range,
        num_recommendations=num_recs
    )

    # Display results
    print("\n" + "=" * 50)
    print("YOUR PERSONALIZED RECOMMENDATIONS")
    print("=" * 50)
    print(result["recommendations"])

    # Save option
    save = input("\n\nSave recommendations to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_recommendations(result["recommendations"], filename)
        else:
            save_recommendations(result["recommendations"], f"{product_category.replace(' ', '-')}-recommendations")

if __name__ == "__main__":
    interactive_shopping_assistant()
