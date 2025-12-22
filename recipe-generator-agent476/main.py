#!/usr/bin/env python
from crewai import Crew, Process
from agents import RecipeGeneratorAgents
from tasks import RecipeGeneratorTasks
from dotenv import load_dotenv

load_dotenv()

def run_recipe_generator():
    """
    Run the Recipe Generator crew to create recipes and meal plans
    """
    print("## Welcome to the Recipe Generator Crew")
    print("---------------------------------------")

    # Get user input
    print("\nWhat would you like to create?")
    print("1. Single recipe")
    print("2. Meal plan")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        ingredients = input("\nWhat ingredients do you have? (comma-separated): ")
        dietary = input("Any dietary restrictions? (e.g., vegetarian, gluten-free): ")
        cuisine = input("Preferred cuisine? (e.g., Italian, Asian, Mediterranean): ")

        recipe_request = f"""
        Available Ingredients: {ingredients}
        Dietary Restrictions: {dietary}
        Cuisine Preference: {cuisine}
        Servings: 4
        """

        # Initialize agents
        agents = RecipeGeneratorAgents()
        tasks_manager = RecipeGeneratorTasks()

        recipe_creator = agents.recipe_creator()
        nutritionist = agents.nutritionist()
        cooking_instructor = agents.cooking_instructor()

        # Create tasks
        recipe_task = tasks_manager.create_recipe(recipe_creator, recipe_request)
        nutrition_task = tasks_manager.analyze_nutrition(nutritionist, recipe_request)
        instructions_task = tasks_manager.write_instructions(cooking_instructor, recipe_request)
        variations_task = tasks_manager.generate_variations(recipe_creator, recipe_request)

        # Create and run crew
        crew = Crew(
            agents=[recipe_creator, nutritionist, cooking_instructor],
            tasks=[recipe_task, nutrition_task, instructions_task, variations_task],
            process=Process.sequential,
            verbose=True
        )

    else:
        duration = input("\nMeal plan duration? (e.g., 1 week, 3 days): ")
        dietary = input("Dietary preferences? (e.g., vegetarian, keto): ")
        goals = input("Health goals? (e.g., weight loss, muscle gain): ")

        meal_plan_requirements = f"""
        Duration: {duration}
        Dietary Preferences: {dietary}
        Health Goals: {goals}
        People: 2-4
        """

        # Initialize agents
        agents = RecipeGeneratorAgents()
        tasks_manager = RecipeGeneratorTasks()

        meal_planner = agents.meal_planner()
        nutritionist = agents.nutritionist()

        # Create tasks
        meal_plan_task = tasks_manager.create_meal_plan(meal_planner, meal_plan_requirements)
        nutrition_task = tasks_manager.analyze_nutrition(nutritionist, meal_plan_requirements)

        # Create and run crew
        crew = Crew(
            agents=[meal_planner, nutritionist],
            tasks=[meal_plan_task, nutrition_task],
            process=Process.sequential,
            verbose=True
        )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Recipe Generator Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_recipe_generator()
