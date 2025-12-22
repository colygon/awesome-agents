from crewai import Agent
from tools import WorkoutTools, NutritionTools, ProgressTools

class FitnessCoachAgents:
    def personal_trainer(self):
        return Agent(
            role='Personal Trainer',
            goal='Design effective workout programs tailored to individual goals',
            backstory="""You are a certified personal trainer with expertise in
            strength training, cardio, and functional fitness. You create personalized
            workout plans that match fitness levels, goals, and available equipment.""",
            tools=[
                WorkoutTools.create_workout_plan,
                WorkoutTools.demonstrate_exercise,
                WorkoutTools.adjust_intensity
            ],
            verbose=True,
            allow_delegation=False
        )

    def nutrition_coach(self):
        return Agent(
            role='Nutrition Coach',
            goal='Provide nutrition guidance to support fitness goals',
            backstory="""You are a certified nutrition coach who understands
            macronutrients, calorie needs, and how nutrition supports athletic
            performance and body composition goals.""",
            tools=[
                NutritionTools.calculate_calorie_needs,
                NutritionTools.create_meal_plan,
                NutritionTools.track_macros
            ],
            verbose=True,
            allow_delegation=False
        )

    def progress_tracker(self):
        return Agent(
            role='Progress Tracker',
            goal='Monitor progress and adjust programs for optimal results',
            backstory="""You are an expert at tracking fitness metrics,
            analyzing progress, and making data-driven adjustments to training
            and nutrition programs.""",
            tools=[
                ProgressTools.track_metrics,
                ProgressTools.analyze_progress,
                ProgressTools.generate_report
            ],
            verbose=True,
            allow_delegation=False
        )

    def motivation_coach(self):
        return Agent(
            role='Motivation Coach',
            goal='Keep clients motivated and accountable',
            backstory="""You are a motivational expert who helps clients stay
            committed to their fitness journey through goal setting, positive
            reinforcement, and accountability strategies.""",
            tools=[
                ProgressTools.set_goals,
                ProgressTools.create_accountability_plan,
                WorkoutTools.suggest_modifications
            ],
            verbose=True,
            allow_delegation=False
        )
