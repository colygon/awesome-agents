from crewai import Task
from textwrap import dedent

class FitnessCoachTasks:
    def create_workout_program(self, agent, user_profile):
        return Task(
            description=dedent(f"""
                Create personalized workout program: {user_profile}

                Tasks: Design workout split, select exercises, set rep/set schemes,
                determine progression strategy, include warm-up and cool-down.
            """),
            agent=agent,
            expected_output="Complete workout program with exercises, sets, reps, and progression plan"
        )

    def design_nutrition_plan(self, agent, goals):
        return Task(
            description=dedent(f"""
                Design nutrition plan: {goals}

                Tasks: Calculate calorie needs, set macro targets, suggest meal timing,
                provide food examples, include hydration guidelines.
            """),
            agent=agent,
            expected_output="Nutrition plan with calories, macros, meal timing, and food suggestions"
        )

    def track_progress(self, agent, metrics):
        return Task(
            description=dedent(f"""
                Track and analyze progress: {metrics}

                Tasks: Monitor key metrics, identify trends, assess goal progress,
                recommend adjustments, celebrate milestones.
            """),
            agent=agent,
            expected_output="Progress report with metrics, trends, and recommendations"
        )

    def create_motivation_plan(self, agent, challenges):
        return Task(
            description=dedent(f"""
                Create motivation and accountability plan: {challenges}

                Tasks: Set SMART goals, create accountability system, provide
                encouragement strategies, suggest habit-building techniques.
            """),
            agent=agent,
            expected_output="Motivation plan with goals, accountability measures, and encouragement strategies"
        )
