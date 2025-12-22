from crewai import Task
from textwrap import dedent

class RecipeGeneratorTasks:
    def create_recipe(self, agent, recipe_request):
        return Task(
            description=dedent(f"""
                Create a delicious recipe based on the following requirements:

                Recipe Request:
                {recipe_request}

                Your tasks:
                1. Design recipe with available ingredients
                2. Determine appropriate portions and servings
                3. List all ingredients with measurements
                4. Consider flavor balance and texture
                5. Account for dietary restrictions if specified
                6. Suggest ingredient substitutions if needed
                7. Add preparation and cooking time estimates

                Provide complete recipe with ingredients and basic structure.
            """),
            agent=agent,
            expected_output="Complete recipe with ingredients list, measurements, servings, and time estimates"
        )

    def analyze_nutrition(self, agent, recipe_data):
        return Task(
            description=dedent(f"""
                Analyze the nutritional content of the recipe:

                Recipe Data:
                {recipe_data}

                Your tasks:
                1. Calculate calories per serving
                2. Determine macronutrient breakdown (protein, carbs, fat)
                3. Identify key vitamins and minerals
                4. Assess dietary compliance (keto, vegan, gluten-free, etc.)
                5. Suggest healthier modifications if possible
                6. Calculate nutritional score
                7. Provide health benefits and considerations

                Provide comprehensive nutritional analysis.
            """),
            agent=agent,
            expected_output="Detailed nutritional analysis with macros, calories, dietary compliance, and health recommendations"
        )

    def write_instructions(self, agent, recipe_details):
        return Task(
            description=dedent(f"""
                Write clear, detailed cooking instructions:

                Recipe Details:
                {recipe_details}

                Your tasks:
                1. Break down cooking process into clear steps
                2. Include timing for each step
                3. Explain important techniques
                4. Provide temperature guidelines
                5. Add cooking tips and tricks
                6. Include troubleshooting advice
                7. Describe expected results at each stage
                8. Add plating and serving suggestions

                Provide step-by-step cooking instructions.
            """),
            agent=agent,
            expected_output="Detailed step-by-step cooking instructions with timing, tips, and serving suggestions"
        )

    def create_meal_plan(self, agent, meal_plan_requirements):
        return Task(
            description=dedent(f"""
                Create a balanced meal plan:

                Meal Plan Requirements:
                {meal_plan_requirements}

                Your tasks:
                1. Design meals for specified duration (week/month)
                2. Ensure nutritional balance across meals
                3. Include breakfast, lunch, dinner, and snacks
                4. Consider variety and avoid repetition
                5. Account for dietary preferences and restrictions
                6. Plan for efficient ingredient usage
                7. Include prep-ahead suggestions
                8. Create consolidated shopping list

                Provide complete meal plan with shopping list.
            """),
            agent=agent,
            expected_output="Comprehensive meal plan with daily menus and organized shopping list"
        )

    def generate_variations(self, agent, base_recipe):
        return Task(
            description=dedent(f"""
                Generate recipe variations for different preferences:

                Base Recipe:
                {base_recipe}

                Your tasks:
                1. Create vegetarian/vegan variations
                2. Develop low-carb or keto versions
                3. Design kid-friendly adaptations
                4. Suggest international flavor variations
                5. Create budget-friendly alternatives
                6. Develop quick/easy versions
                7. Provide scaling options (2 servings to 12 servings)

                Provide multiple recipe variations.
            """),
            agent=agent,
            expected_output="Multiple recipe variations with modifications for different dietary needs and preferences"
        )
