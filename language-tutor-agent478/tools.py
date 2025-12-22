from crewai_tools import tool
import json

class LanguageLearningTools:
    @tool("Teach Grammar")
    def teach_grammar(topic: str) -> str:
        """Teaches grammar concepts with examples."""
        return json.dumps({"topic": topic, "rule": "Explanation", "examples": ["Example 1", "Example 2"]}, indent=2)

    @tool("Build Vocabulary")
    def build_vocabulary(theme: str) -> str:
        """Builds vocabulary around specific themes."""
        return json.dumps({"theme": theme, "words": [{"word": "hello", "meaning": "greeting", "example": "Hello, how are you?"}]}, indent=2)

    @tool("Explain Concepts")
    def explain_concepts(concept: str) -> str:
        """Explains language concepts clearly."""
        return json.dumps({"concept": concept, "explanation": "Clear explanation", "usage": "When to use"}, indent=2)

    @tool("Teach Idioms")
    def teach_idioms(language: str) -> str:
        """Teaches common idioms and expressions."""
        return json.dumps({"idioms": [{"phrase": "Break a leg", "meaning": "Good luck", "usage": "Before performances"}]}, indent=2)

    @tool("Explain Cultural Context")
    def explain_cultural_context(topic: str) -> str:
        """Explains cultural contexts for language use."""
        return json.dumps({"context": topic, "explanation": "Cultural background", "dos_donts": ["Do this", "Don't do that"]}, indent=2)


class PracticeTools:
    @tool("Conduct Conversation")
    def conduct_conversation(topic: str) -> str:
        """Conducts conversation practice."""
        return json.dumps({"topic": topic, "dialogue": ["Q: How are you?", "A: I'm fine, thanks!"]}, indent=2)

    @tool("Provide Feedback")
    def provide_feedback(student_response: str) -> str:
        """Provides constructive feedback."""
        return json.dumps({"feedback": "Good effort!", "corrections": ["Fix this"], "suggestions": ["Try this"]}, indent=2)

    @tool("Suggest Phrases")
    def suggest_phrases(situation: str) -> str:
        """Suggests useful phrases for situations."""
        return json.dumps({"situation": situation, "phrases": ["Phrase 1", "Phrase 2"], "notes": "Usage tips"}, indent=2)

    @tool("Role Play Scenarios")
    def role_play_scenarios(scenario: str) -> str:
        """Creates role-play scenarios for practice."""
        return json.dumps({"scenario": scenario, "roles": ["Customer", "Waiter"], "objectives": "Practice ordering food"}, indent=2)


class AssessmentTools:
    @tool("Assess Proficiency")
    def assess_proficiency(sample: str) -> str:
        """Assesses language proficiency level."""
        return json.dumps({"level": "B1 - Intermediate", "strengths": ["Good vocabulary"], "areas_to_improve": ["Grammar"]}, indent=2)

    @tool("Track Progress")
    def track_progress(history: str) -> str:
        """Tracks learning progress over time."""
        return json.dumps({"progress": "Improving steadily", "milestones": ["Completed A1 level"], "next_goals": ["Master B1"]}, indent=2)

    @tool("Create Study Plan")
    def create_study_plan(goals: str) -> str:
        """Creates personalized study plan."""
        return json.dumps({"plan": "Weekly study schedule", "focus_areas": ["Grammar", "Speaking"], "resources": ["Textbook Ch. 5"]}, indent=2)
