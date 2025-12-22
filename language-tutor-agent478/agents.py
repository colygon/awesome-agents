from crewai import Agent
from tools import LanguageLearningTools, PracticeTools, AssessmentTools

class LanguageTutorAgents:
    def language_instructor(self):
        return Agent(
            role='Language Instructor',
            goal='Teach language fundamentals including grammar, vocabulary, and syntax',
            backstory="""You are an experienced language teacher who makes complex
            grammar rules understandable. You teach vocabulary in context and help
            students build strong language foundations.""",
            tools=[
                LanguageLearningTools.teach_grammar,
                LanguageLearningTools.build_vocabulary,
                LanguageLearningTools.explain_concepts
            ],
            verbose=True,
            allow_delegation=False
        )

    def conversation_partner(self):
        return Agent(
            role='Conversation Partner',
            goal='Practice conversational skills through dialogue and role-play',
            backstory="""You are a native-level conversation partner who helps
            students practice speaking naturally. You correct errors gently and
            help build confidence in real-world communication.""",
            tools=[
                PracticeTools.conduct_conversation,
                PracticeTools.provide_feedback,
                PracticeTools.suggest_phrases
            ],
            verbose=True,
            allow_delegation=False
        )

    def cultural_guide(self):
        return Agent(
            role='Cultural Guide',
            goal='Teach cultural context and nuances of language use',
            backstory="""You are a cultural expert who teaches idioms, customs,
            and cultural contexts that make language learning meaningful and
            practical for real-world situations.""",
            tools=[
                LanguageLearningTools.teach_idioms,
                LanguageLearningTools.explain_cultural_context,
                PracticeTools.role_play_scenarios
            ],
            verbose=True,
            allow_delegation=False
        )

    def progress_assessor(self):
        return Agent(
            role='Progress Assessor',
            goal='Evaluate language proficiency and track learning progress',
            backstory="""You are an assessment specialist who measures language
            proficiency, identifies strengths and weaknesses, and creates
            personalized learning paths based on progress.""",
            tools=[
                AssessmentTools.assess_proficiency,
                AssessmentTools.track_progress,
                AssessmentTools.create_study_plan
            ],
            verbose=True,
            allow_delegation=False
        )
