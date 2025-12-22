from crewai_tools import tool
import json

class WorkoutTools:
    @tool("Create Workout Plan")
    def create_workout_plan(goals: str) -> str:
        """Creates personalized workout plan."""
        plan = {
            "program": "4-Day Upper/Lower Split",
            "duration": "8 weeks",
            "workouts": {
                "Day 1 - Upper Body": [
                    {"exercise": "Bench Press", "sets": 4, "reps": "8-10"},
                    {"exercise": "Rows", "sets": 4, "reps": "8-10"},
                    {"exercise": "Shoulder Press", "sets": 3, "reps": "10-12"}
                ],
                "Day 2 - Lower Body": [
                    {"exercise": "Squats", "sets": 4, "reps": "8-10"},
                    {"exercise": "Romanian Deadlifts", "sets": 3, "reps": "10-12"},
                    {"exercise": "Leg Press", "sets": 3, "reps": "12-15"}
                ]
            }
        }
        return json.dumps(plan, indent=2)

    @tool("Demonstrate Exercise")
    def demonstrate_exercise(exercise: str) -> str:
        """Provides exercise demonstration and form cues."""
        demo = {
            "exercise": exercise,
            "form_cues": ["Keep back straight", "Control the movement", "Full range of motion"],
            "common_mistakes": ["Arching back", "Using momentum", "Incomplete reps"],
            "modifications": ["Easier: Use lighter weight", "Harder: Add pause at bottom"]
        }
        return json.dumps(demo, indent=2)

    @tool("Adjust Intensity")
    def adjust_intensity(current_level: str) -> str:
        """Adjusts workout intensity based on progress."""
        return json.dumps({"adjustment": "Increase weight by 5%", "reasoning": "Progressive overload"}, indent=2)

    @tool("Suggest Modifications")
    def suggest_modifications(limitation: str) -> str:
        """Suggests workout modifications for limitations."""
        return json.dumps({"modification": "Substitute with low-impact alternative", "examples": ["Swimming", "Cycling"]}, indent=2)


class NutritionTools:
    @tool("Calculate Calorie Needs")
    def calculate_calorie_needs(profile: str) -> str:
        """Calculates daily calorie requirements."""
        return json.dumps({"maintenance": 2200, "deficit": 1800, "surplus": 2600}, indent=2)

    @tool("Create Meal Plan")
    def create_meal_plan(calories: str) -> str:
        """Creates balanced meal plan."""
        plan = {
            "daily_calories": 2000,
            "meals": {
                "breakfast": {"food": "Oatmeal with berries", "calories": 400, "protein": "20g"},
                "lunch": {"food": "Chicken salad", "calories": 500, "protein": "40g"},
                "dinner": {"food": "Salmon with vegetables", "calories": 600, "protein": "45g"}
            }
        }
        return json.dumps(plan, indent=2)

    @tool("Track Macros")
    def track_macros(food_log: str) -> str:
        """Tracks macronutrient intake."""
        return json.dumps({"protein": "150g", "carbs": "200g", "fat": "60g", "calories": 1980}, indent=2)


class ProgressTools:
    @tool("Track Metrics")
    def track_metrics(data: str) -> str:
        """Tracks fitness metrics over time."""
        return json.dumps({"weight": [180, 178, 176], "body_fat": [18, 17, 16], "strength_gains": "+10%"}, indent=2)

    @tool("Analyze Progress")
    def analyze_progress(metrics: str) -> str:
        """Analyzes progress towards goals."""
        return json.dumps({"trend": "positive", "pace": "on track", "recommendations": ["Continue current plan"]}, indent=2)

    @tool("Generate Report")
    def generate_report(period: str) -> str:
        """Generates progress report."""
        return json.dumps({"summary": "Great progress!", "achievements": ["Lost 4 lbs", "Increased strength 10%"]}, indent=2)

    @tool("Set Goals")
    def set_goals(objective: str) -> str:
        """Sets SMART fitness goals."""
        return json.dumps({"goal": "Lose 10 lbs in 12 weeks", "milestones": ["2 lbs per month"]}, indent=2)

    @tool("Create Accountability Plan")
    def create_accountability_plan(preferences: str) -> str:
        """Creates accountability system."""
        return json.dumps({"check_ins": "Weekly", "tracking": "Daily", "rewards": "Monthly milestone prizes"}, indent=2)
