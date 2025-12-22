from crewai import Agent
from tools import RecipeCreationTools, NutritionTools, CookingTools

class RecipeGeneratorAgents:
    def recipe_creator(self):
        return Agent(
            role='Recipe Creator',
            goal='Create delicious and innovative recipes based on available ingredients',
            backstory="""You are a creative chef with expertise in various cuisines
            and cooking techniques. You can combine ingredients in innovative ways,
            adapt recipes for dietary restrictions, and create balanced, flavorful
            dishes. You understand flavor profiles, cooking methods, and presentation.""",
            tools=[
                RecipeCreationTools.generate_recipe,
                RecipeCreationTools.suggest_substitutions,
                RecipeCreationTools.scale_recipe
            ],
            verbose=True,
            allow_delegation=False
        )

    def nutritionist(self):
        return Agent(
            role='Nutritionist',
            goal='Analyze nutritional content and optimize recipes for health goals',
            backstory="""You are a certified nutritionist who understands macros,
            micronutrients, and dietary requirements. You can calculate nutritional
            values, suggest healthy modifications, and ensure recipes meet specific
            dietary needs like keto, vegan, or low-sodium diets.""",
            tools=[
                NutritionTools.calculate_nutrition,
                NutritionTools.analyze_dietary_compliance,
                NutritionTools.suggest_healthy_modifications
            ],
            verbose=True,
            allow_delegation=False
        )

    def cooking_instructor(self):
        return Agent(
            role='Cooking Instructor',
            goal='Provide clear, detailed cooking instructions and tips',
            backstory="""You are an experienced cooking instructor who excels at
            breaking down complex techniques into simple steps. You provide timing
            guidance, explain why certain steps matter, and offer troubleshooting
            tips to ensure cooking success.""",
            tools=[
                CookingTools.generate_instructions,
                CookingTools.provide_cooking_tips,
                CookingTools.estimate_cooking_time
            ],
            verbose=True,
            allow_delegation=False
        )

    def meal_planner(self):
        return Agent(
            role='Meal Planner',
            goal='Create balanced meal plans and shopping lists',
            backstory="""You are a meal planning expert who creates practical,
            balanced meal plans. You consider variety, nutrition, budget, and
            convenience. You generate efficient shopping lists and help minimize
            food waste through smart ingredient usage.""",
            tools=[
                RecipeCreationTools.create_meal_plan,
                CookingTools.generate_shopping_list,
                RecipeCreationTools.suggest_recipe_variations
            ],
            verbose=True,
            allow_delegation=False
        )
