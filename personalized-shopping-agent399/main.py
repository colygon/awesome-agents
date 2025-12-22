#!/usr/bin/env python
from crewai import Crew, Process
from agents import PersonalizedShoppingAgents
from tasks import PersonalizedShoppingTasks
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def personal_shopping_assistant(
    customer_preferences: str,
    category: str,
    budget: str,
    shopping_goal: str = "general"
):
    """
    Run personalized shopping assistant to find and recommend products.

    Args:
        customer_preferences: Customer's style preferences, sizes, etc.
        category: Product category (clothing, shoes, accessories, home, electronics)
        budget: Budget range
        shopping_goal: Shopping goal (wardrobe_refresh, specific_item, gift, etc.)
    """
    print(f"\n{'='*60}")
    print(f"Personal Shopping Assistant")
    print(f"Category: {category}")
    print(f"Budget: {budget}")
    print(f"Goal: {shopping_goal}")
    print(f"{'='*60}\n")

    # Initialize agents and tasks
    agents = PersonalizedShoppingAgents()
    tasks = PersonalizedShoppingTasks()

    # Create agents
    preference_analyst = agents.preference_analyst()
    product_researcher = agents.product_researcher()
    deal_finder = agents.deal_finder()
    style_consultant = agents.style_consultant()
    shopping_coordinator = agents.shopping_coordinator()

    # Create tasks
    preference_task = tasks.analyze_customer_preferences(
        agent=preference_analyst,
        customer_data=customer_preferences,
        shopping_goal=shopping_goal
    )

    research_task = tasks.research_products(
        agent=product_researcher,
        preferences="Use customer preferences",
        category=category,
        budget=budget
    )

    deals_task = tasks.find_best_deals(
        agent=deal_finder,
        products="Find deals on researched products"
    )

    style_task = tasks.create_style_recommendations(
        agent=style_consultant,
        products="Use researched products",
        preferences="Use customer preferences"
    )

    shopping_list_task = tasks.compile_shopping_list(
        agent=shopping_coordinator,
        recommendations="Use style recommendations",
        deals="Use deal information",
        budget=budget
    )

    # Create crew
    crew = Crew(
        agents=[
            preference_analyst,
            product_researcher,
            deal_finder,
            style_consultant,
            shopping_coordinator
        ],
        tasks=[
            preference_task,
            research_task,
            deals_task,
            style_task,
            shopping_list_task
        ],
        process=Process.sequential,
        verbose=True
    )

    # Execute
    result = crew.kickoff()

    print(f"\n{'='*60}")
    print("Personalized Shopping Recommendations Ready!")
    print(f"{'='*60}\n")
    print(result)

    # Save shopping list
    output_file = f"shopping_list_{category.replace(' ', '_').lower()}.txt"
    with open(output_file, 'w') as f:
        f.write(str(result))
    print(f"\nShopping list saved to: {output_file}")

    return result

def quick_recommendation(item_description: str, budget: str):
    """
    Get quick product recommendations for a specific item.
    """
    print(f"\n{'='*60}")
    print(f"Quick Recommendation")
    print(f"Looking for: {item_description}")
    print(f"Budget: {budget}")
    print(f"{'='*60}\n")

    agents = PersonalizedShoppingAgents()
    tasks = PersonalizedShoppingTasks()

    product_researcher = agents.product_researcher()
    deal_finder = agents.deal_finder()

    research_task = tasks.research_products(
        agent=product_researcher,
        preferences=item_description,
        category="general",
        budget=budget
    )

    deals_task = tasks.find_best_deals(
        agent=deal_finder,
        products="Find best deals"
    )

    crew = Crew(
        agents=[product_researcher, deal_finder],
        tasks=[research_task, deals_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print(f"\n{'='*60}")
    print("Recommendations Ready!")
    print(f"{'='*60}\n")
    print(result)

    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Full shopping: python main.py full '<preferences>' <category> <budget> [goal]")
        print("  Quick search:  python main.py quick '<item_description>' <budget>")
        print("\nExamples:")
        print('  python main.py full "casual style, size M, loves blue and black" "shirts" "$50-100" "wardrobe_refresh"')
        print('  python main.py quick "comfortable running shoes for daily training" "$80-120"')
        print("\nCategories: clothing, shoes, accessories, home, electronics")
        print("Goals: wardrobe_refresh, specific_item, gift, occasion, seasonal")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "full":
        if len(sys.argv) < 5:
            print("Error: Preferences, category, and budget required")
            print('Usage: python main.py full "<preferences>" <category> <budget> [goal]')
            sys.exit(1)

        preferences = sys.argv[2]
        category = sys.argv[3]
        budget = sys.argv[4]
        goal = sys.argv[5] if len(sys.argv) > 5 else "general"

        personal_shopping_assistant(preferences, category, budget, goal)

    elif mode == "quick":
        if len(sys.argv) < 4:
            print("Error: Item description and budget required")
            print('Usage: python main.py quick "<item_description>" <budget>')
            sys.exit(1)

        item_description = sys.argv[2]
        budget = sys.argv[3]

        quick_recommendation(item_description, budget)

    else:
        print(f"Unknown mode: {mode}")
        print("Use 'full' for complete shopping assistance or 'quick' for fast recommendations")
        sys.exit(1)
