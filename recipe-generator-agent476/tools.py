from crewai_tools import tool
import json
from typing import Dict, List, Any

class RecipeCreationTools:
    @tool("Generate Recipe")
    def generate_recipe(ingredients: str) -> str:
        """
        Generates a recipe based on available ingredients.
        Useful for creating meals from what you have.
        """
        recipe = {
            "title": "Mediterranean Chicken Bowl",
            "servings": 4,
            "prep_time": "15 minutes",
            "cook_time": "25 minutes",
            "total_time": "40 minutes",
            "difficulty": "Easy",
            "cuisine": "Mediterranean",
            "ingredients": [
                {"item": "chicken breast", "amount": "1.5 lbs", "preparation": "diced"},
                {"item": "olive oil", "amount": "3 tbsp", "preparation": ""},
                {"item": "garlic", "amount": "4 cloves", "preparation": "minced"},
                {"item": "cherry tomatoes", "amount": "2 cups", "preparation": "halved"},
                {"item": "cucumber", "amount": "1 large", "preparation": "diced"},
                {"item": "red onion", "amount": "1 medium", "preparation": "sliced"},
                {"item": "feta cheese", "amount": "1 cup", "preparation": "crumbled"},
                {"item": "quinoa", "amount": "2 cups", "preparation": "cooked"},
                {"item": "lemon", "amount": "2", "preparation": "juiced"},
                {"item": "oregano", "amount": "1 tsp", "preparation": "dried"}
            ],
            "tags": ["healthy", "protein-rich", "meal-prep-friendly"]
        }

        return json.dumps(recipe, indent=2)

    @tool("Suggest Substitutions")
    def suggest_substitutions(ingredient: str) -> str:
        """
        Suggests substitutions for ingredients.
        Useful for dietary restrictions or missing ingredients.
        """
        substitutions_db = {
            "chicken": ["turkey", "tofu", "chickpeas", "tempeh"],
            "butter": ["olive oil", "coconut oil", "ghee", "applesauce (for baking)"],
            "milk": ["almond milk", "oat milk", "coconut milk", "soy milk"],
            "eggs": ["flax eggs", "chia eggs", "applesauce", "mashed banana"],
            "flour": ["almond flour", "coconut flour", "oat flour", "rice flour"],
            "sugar": ["honey", "maple syrup", "stevia", "monk fruit sweetener"]
        }

        subs = substitutions_db.get(ingredient.lower(), ["No common substitutions found"])

        return json.dumps({
            "ingredient": ingredient,
            "substitutions": [
                {"substitute": sub, "ratio": "1:1", "notes": "Adjust to taste"}
                for sub in subs
            ]
        }, indent=2)

    @tool("Scale Recipe")
    def scale_recipe(recipe_servings: str) -> str:
        """
        Scales recipe quantities for different serving sizes.
        Useful for adjusting recipe yield.
        """
        # Parse input like "4 servings to 8 servings"
        scaling_factor = 2.0  # Example: doubling

        scaling_info = {
            "original_servings": 4,
            "target_servings": 8,
            "scaling_factor": scaling_factor,
            "adjustments": {
                "ingredients": "Multiply all quantities by 2.0",
                "cooking_time": "May increase by 10-20% for larger quantities",
                "pan_size": "Use larger cookware if needed",
                "notes": [
                    "Seasonings: Scale conservatively, taste and adjust",
                    "Liquids: May not need full scaling in some recipes",
                    "Baking: Temperature stays same, time may increase slightly"
                ]
            },
            "example": {
                "1 cup flour": "2 cups flour",
                "2 eggs": "4 eggs",
                "1 tsp salt": "1.75 tsp salt (scale conservatively)"
            }
        }

        return json.dumps(scaling_info, indent=2)

    @tool("Create Meal Plan")
    def create_meal_plan(duration: str) -> str:
        """
        Creates a balanced meal plan for specified duration.
        Useful for weekly or monthly meal planning.
        """
        meal_plan = {
            "duration": duration,
            "meals": {
                "Monday": {
                    "breakfast": "Greek Yogurt Parfait with Berries",
                    "lunch": "Mediterranean Chicken Bowl",
                    "dinner": "Baked Salmon with Roasted Vegetables",
                    "snacks": ["Apple with almond butter", "Hummus with carrots"]
                },
                "Tuesday": {
                    "breakfast": "Overnight Oats with Banana",
                    "lunch": "Quinoa Salad with Chickpeas",
                    "dinner": "Turkey Meatballs with Zucchini Noodles",
                    "snacks": ["Trail mix", "Celery with peanut butter"]
                },
                "Wednesday": {
                    "breakfast": "Veggie Omelet with Whole Grain Toast",
                    "lunch": "Leftover Salmon with Side Salad",
                    "dinner": "Chicken Stir-fry with Brown Rice",
                    "snacks": ["Protein smoothie", "String cheese"]
                }
            },
            "prep_tips": [
                "Cook quinoa and brown rice in bulk on Sunday",
                "Prep vegetables for the week",
                "Marinate proteins night before",
                "Make overnight oats in batches"
            ]
        }

        return json.dumps(meal_plan, indent=2)

    @tool("Suggest Recipe Variations")
    def suggest_recipe_variations(base_recipe: str) -> str:
        """
        Suggests variations of a base recipe.
        Useful for adding variety to meals.
        """
        variations = {
            "base_recipe": base_recipe,
            "variations": [
                {
                    "name": "Vegetarian Version",
                    "changes": "Replace chicken with chickpeas or tofu",
                    "additional_ingredients": ["extra veggies", "tahini sauce"]
                },
                {
                    "name": "Low-Carb Version",
                    "changes": "Replace quinoa with cauliflower rice",
                    "additional_ingredients": ["avocado", "extra olive oil"]
                },
                {
                    "name": "Spicy Version",
                    "changes": "Add harissa paste and jalapeños",
                    "additional_ingredients": ["red pepper flakes", "sriracha"]
                },
                {
                    "name": "Asian Fusion",
                    "changes": "Use soy sauce, ginger, and sesame oil",
                    "additional_ingredients": ["edamame", "sesame seeds", "green onions"]
                }
            ]
        }

        return json.dumps(variations, indent=2)


class NutritionTools:
    @tool("Calculate Nutrition")
    def calculate_nutrition(recipe: str) -> str:
        """
        Calculates nutritional information for a recipe.
        Useful for understanding health impact.
        """
        nutrition = {
            "per_serving": {
                "calories": 425,
                "protein": "32g",
                "carbohydrates": "38g",
                "fat": "16g",
                "fiber": "6g",
                "sugar": "4g",
                "sodium": "480mg"
            },
            "macronutrient_ratio": {
                "protein": "30%",
                "carbs": "36%",
                "fat": "34%"
            },
            "vitamins_minerals": {
                "vitamin_a": "25% DV",
                "vitamin_c": "45% DV",
                "calcium": "15% DV",
                "iron": "20% DV"
            },
            "health_score": 8.5,
            "dietary_labels": ["high-protein", "good-source-of-fiber", "heart-healthy"]
        }

        return json.dumps(nutrition, indent=2)

    @tool("Analyze Dietary Compliance")
    def analyze_dietary_compliance(recipe: str) -> str:
        """
        Checks recipe compliance with various diets.
        Useful for dietary restrictions.
        """
        compliance = {
            "dietary_compatibility": {
                "vegetarian": False,
                "vegan": False,
                "gluten_free": True,
                "dairy_free": False,
                "keto": False,
                "paleo": False,
                "low_carb": False,
                "mediterranean": True,
                "whole30": False
            },
            "allergens": [
                "dairy (feta cheese)",
                "potential cross-contamination with gluten"
            ],
            "modifications_for_compliance": {
                "vegetarian": "Replace chicken with chickpeas",
                "vegan": "Remove feta, replace chicken with tofu",
                "dairy_free": "Omit feta cheese",
                "keto": "Remove quinoa, increase fats",
                "paleo": "Remove feta and quinoa, add sweet potato"
            }
        }

        return json.dumps(compliance, indent=2)

    @tool("Suggest Healthy Modifications")
    def suggest_healthy_modifications(recipe: str) -> str:
        """
        Suggests ways to make recipe healthier.
        Useful for health-conscious cooking.
        """
        modifications = {
            "current_health_score": 8.5,
            "potential_score": 9.2,
            "suggested_modifications": [
                {
                    "change": "Reduce feta cheese to 1/2 cup",
                    "impact": "Reduces sodium by 200mg, calories by 50",
                    "trade_off": "Slightly less creamy"
                },
                {
                    "change": "Add more vegetables (bell peppers, spinach)",
                    "impact": "Increases fiber and vitamins",
                    "trade_off": "None - only benefits"
                },
                {
                    "change": "Use brown rice instead of white",
                    "impact": "Increases fiber by 2g, adds B vitamins",
                    "trade_off": "Longer cooking time"
                },
                {
                    "change": "Grill instead of pan-fry chicken",
                    "impact": "Reduces fat by 3g per serving",
                    "trade_off": "Requires outdoor grill or grill pan"
                }
            ],
            "health_benefits": [
                "Lower sodium content",
                "Higher fiber",
                "More micronutrients",
                "Better fat profile"
            ]
        }

        return json.dumps(modifications, indent=2)


class CookingTools:
    @tool("Generate Instructions")
    def generate_instructions(recipe: str) -> str:
        """
        Generates detailed cooking instructions.
        Useful for step-by-step guidance.
        """
        instructions = {
            "preparation_steps": [
                {
                    "step": 1,
                    "instruction": "Cook quinoa according to package directions and let cool",
                    "time": "20 minutes",
                    "tip": "Add a pinch of salt to cooking water for flavor"
                },
                {
                    "step": 2,
                    "instruction": "Dice chicken into 1-inch cubes and season with salt, pepper, and oregano",
                    "time": "5 minutes",
                    "tip": "Pat chicken dry for better browning"
                },
                {
                    "step": 3,
                    "instruction": "Chop all vegetables and set aside",
                    "time": "10 minutes",
                    "tip": "Uniform sizes ensure even cooking"
                }
            ],
            "cooking_steps": [
                {
                    "step": 4,
                    "instruction": "Heat 2 tbsp olive oil in large skillet over medium-high heat",
                    "time": "2 minutes",
                    "tip": "Oil should shimmer but not smoke"
                },
                {
                    "step": 5,
                    "instruction": "Add chicken and cook until golden brown, about 6-8 minutes",
                    "time": "8 minutes",
                    "tip": "Don't overcrowd the pan - cook in batches if needed"
                },
                {
                    "step": 6,
                    "instruction": "Add garlic and cook until fragrant, about 30 seconds",
                    "time": "1 minute",
                    "tip": "Watch carefully - garlic burns easily"
                }
            ],
            "assembly_steps": [
                {
                    "step": 7,
                    "instruction": "Divide quinoa among bowls, top with chicken and vegetables",
                    "time": "3 minutes",
                    "tip": "Arrange ingredients for visual appeal"
                },
                {
                    "step": 8,
                    "instruction": "Drizzle with remaining olive oil and lemon juice, top with feta",
                    "time": "2 minutes",
                    "tip": "Add fresh herbs if available"
                }
            ],
            "total_active_time": "40 minutes"
        }

        return json.dumps(instructions, indent=2)

    @tool("Provide Cooking Tips")
    def provide_cooking_tips(technique: str) -> str:
        """
        Provides expert cooking tips and techniques.
        Useful for improving cooking skills.
        """
        tips = {
            "technique": technique,
            "expert_tips": [
                {
                    "tip": "Temperature control is key",
                    "detail": "Use medium-high heat for proper browning without burning"
                },
                {
                    "tip": "Don't overcrowd the pan",
                    "detail": "Leave space between pieces for proper browning"
                },
                {
                    "tip": "Season in layers",
                    "detail": "Season at multiple stages for depth of flavor"
                },
                {
                    "tip": "Let meat rest",
                    "detail": "Rest cooked chicken 5 minutes before cutting"
                }
            ],
            "common_mistakes": [
                "Moving food too much in the pan",
                "Adding garlic too early",
                "Not preheating pan properly",
                "Forgetting to taste and adjust seasoning"
            ],
            "troubleshooting": {
                "if_dry": "Add splash of chicken broth or water",
                "if_bland": "Add more lemon juice and salt",
                "if_burning": "Reduce heat immediately"
            }
        }

        return json.dumps(tips, indent=2)

    @tool("Estimate Cooking Time")
    def estimate_cooking_time(recipe: str) -> str:
        """
        Estimates total cooking time including prep.
        Useful for meal planning.
        """
        time_breakdown = {
            "prep_time": "15 minutes",
            "active_cooking": "25 minutes",
            "passive_cooking": "0 minutes",
            "total_time": "40 minutes",
            "breakdown": {
                "washing_and_chopping": "10 minutes",
                "cooking_quinoa": "20 minutes (can do simultaneously)",
                "cooking_chicken": "10 minutes",
                "assembly": "5 minutes"
            },
            "time_saving_tips": [
                "Use pre-cooked quinoa (saves 15 minutes)",
                "Buy pre-diced vegetables (saves 8 minutes)",
                "Use rotisserie chicken (saves 10 minutes)",
                "Meal prep components in advance"
            ],
            "skill_level_adjustments": {
                "beginner": "+10 minutes",
                "intermediate": "as stated",
                "expert": "-5 minutes"
            }
        }

        return json.dumps(time_breakdown, indent=2)

    @tool("Generate Shopping List")
    def generate_shopping_list(recipes: str) -> str:
        """
        Generates organized shopping list from recipes.
        Useful for efficient grocery shopping.
        """
        shopping_list = {
            "organized_by_section": {
                "Produce": [
                    "Cherry tomatoes - 2 cups",
                    "Cucumber - 1 large",
                    "Red onion - 1 medium",
                    "Garlic - 1 head",
                    "Lemons - 2"
                ],
                "Meat & Seafood": [
                    "Chicken breast - 1.5 lbs"
                ],
                "Dairy": [
                    "Feta cheese - 1 cup"
                ],
                "Pantry": [
                    "Quinoa - 2 cups (dry)",
                    "Olive oil - if running low",
                    "Dried oregano - if needed"
                ]
            },
            "estimated_cost": "$28.50",
            "shopping_tips": [
                "Check pantry before shopping",
                "Buy seasonal produce for better prices",
                "Consider buying in bulk for staples",
                "Look for sales on proteins"
            ],
            "storage_tips": {
                "produce": "Store tomatoes at room temp, refrigerate others",
                "chicken": "Use within 2 days or freeze",
                "feta": "Keep in brine in refrigerator"
            }
        }

        return json.dumps(shopping_list, indent=2)
