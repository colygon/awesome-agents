from crewai import Task
from textwrap import dedent

class LanguageTutorTasks:
    def teach_lesson(self, agent, lesson_topic):
        return Task(
            description=dedent(f"""
                Teach language lesson: {lesson_topic}

                Tasks: Explain concepts, provide examples, teach vocabulary,
                demonstrate usage, give practice exercises.
            """),
            agent=agent,
            expected_output="Complete lesson with explanations, examples, and exercises"
        )

    def practice_conversation(self, agent, scenario):
        return Task(
            description=dedent(f"""
                Practice conversation: {scenario}

                Tasks: Conduct dialogue, provide corrections, suggest improvements,
                practice pronunciation, build fluency.
            """),
            agent=agent,
            expected_output="Conversation practice session with feedback and corrections"
        )

    def teach_culture(self, agent, cultural_topic):
        return Task(
            description=dedent(f"""
                Teach cultural context: {cultural_topic}

                Tasks: Explain cultural norms, teach idioms, discuss customs,
                provide context for language use.
            """),
            agent=agent,
            expected_output="Cultural lesson with idioms, customs, and contextual examples"
        )

    def assess_level(self, agent, student_work):
        return Task(
            description=dedent(f"""
                Assess language proficiency: {student_work}

                Tasks: Evaluate skills, identify strengths/weaknesses, determine
                level, create improvement plan.
            """),
            agent=agent,
            expected_output="Proficiency assessment with level determination and study recommendations"
        )
