"""
Emoji Shortcodes - CrewAI Crew Orchestration
Manages multi-agent emoji analysis workflows
"""

from crewai import Crew, Process
from agents import EmojiAnalysisAgents
from tasks import EmojiAnalysisTasks
from typing import Optional


class EmojiAnalysisCrew:
    """Manages CrewAI crews for emoji analysis workflows"""

    def __init__(self, llm=None):
        """
        Initialize the crew manager

        Args:
            llm: Language model to use for agents
        """
        self.agents = EmojiAnalysisAgents(llm=llm)
        self.tasks = EmojiAnalysisTasks()

    def analyze_emoji_crew(self, emoji: str, emoji_data: dict = None) -> Crew:
        """
        Creates a crew to analyze a specific emoji

        Args:
            emoji: The emoji to analyze
            emoji_data: Optional metadata about the emoji

        Returns:
            Crew: Configured crew for emoji analysis
        """
        analyze_task = self.tasks.analyze_emoji_task(emoji, emoji_data)
        insights_task = self.tasks.emoji_trend_analysis_task([emoji])

        return Crew(
            agents=[
                self.agents.emoji_analyst_agent(),
                self.agents.usage_insights_agent()
            ],
            tasks=[analyze_task, insights_task],
            process=Process.sequential,
            verbose=True
        )

    def recommend_emojis_crew(self, text: str, tone: str = "neutral") -> Crew:
        """
        Creates a crew to recommend emojis for text

        Args:
            text: The text to suggest emojis for
            tone: Desired communication tone

        Returns:
            Crew: Configured crew for emoji recommendations
        """
        recommend_task = self.tasks.recommend_emojis_task(text, tone)

        return Crew(
            agents=[self.agents.recommendation_agent()],
            tasks=[recommend_task],
            process=Process.sequential,
            verbose=True
        )

    def sentiment_analysis_crew(self, text_with_emojis: str) -> Crew:
        """
        Creates a crew to analyze sentiment in emoji-enhanced text

        Args:
            text_with_emojis: Text containing emojis

        Returns:
            Crew: Configured crew for sentiment analysis
        """
        sentiment_task = self.tasks.emoji_sentiment_task(text_with_emojis)

        return Crew(
            agents=[self.agents.emoji_analyst_agent()],
            tasks=[sentiment_task],
            process=Process.sequential,
            verbose=True
        )

    def find_alternatives_crew(self, emoji: str, context: str = "") -> Crew:
        """
        Creates a crew to find emoji alternatives

        Args:
            emoji: The emoji to find alternatives for
            context: Optional usage context

        Returns:
            Crew: Configured crew for finding alternatives
        """
        alternatives_task = self.tasks.find_emoji_alternatives_task(emoji, context)
        insights_task = self.tasks.emoji_trend_analysis_task([emoji])

        return Crew(
            agents=[
                self.agents.recommendation_agent(),
                self.agents.usage_insights_agent()
            ],
            tasks=[alternatives_task, insights_task],
            process=Process.sequential,
            verbose=True
        )

    def emoji_combination_crew(self, theme: str, count: int = 3) -> Crew:
        """
        Creates a crew to generate emoji combinations

        Args:
            theme: The theme to express with emojis
            count: Number of combinations to generate

        Returns:
            Crew: Configured crew for combination generation
        """
        combination_task = self.tasks.emoji_combination_task(theme, count)

        return Crew(
            agents=[self.agents.recommendation_agent()],
            tasks=[combination_task],
            process=Process.sequential,
            verbose=True
        )


# Convenience functions for quick access
def analyze_emoji(emoji: str, emoji_data: dict = None, llm=None) -> str:
    """
    Quickly analyze an emoji

    Args:
        emoji: The emoji to analyze
        emoji_data: Optional metadata
        llm: Optional language model

    Returns:
        str: Analysis results
    """
    crew_manager = EmojiAnalysisCrew(llm=llm)
    crew = crew_manager.analyze_emoji_crew(emoji, emoji_data)
    result = crew.kickoff()
    return result


def recommend_emojis(text: str, tone: str = "neutral", llm=None) -> str:
    """
    Get emoji recommendations for text

    Args:
        text: The text to get recommendations for
        tone: Desired tone
        llm: Optional language model

    Returns:
        str: Emoji recommendations
    """
    crew_manager = EmojiAnalysisCrew(llm=llm)
    crew = crew_manager.recommend_emojis_crew(text, tone)
    result = crew.kickoff()
    return result


def analyze_sentiment(text_with_emojis: str, llm=None) -> str:
    """
    Analyze sentiment in emoji-enhanced text

    Args:
        text_with_emojis: Text containing emojis
        llm: Optional language model

    Returns:
        str: Sentiment analysis
    """
    crew_manager = EmojiAnalysisCrew(llm=llm)
    crew = crew_manager.sentiment_analysis_crew(text_with_emojis)
    result = crew.kickoff()
    return result


def find_alternatives(emoji: str, context: str = "", llm=None) -> str:
    """
    Find alternative emojis

    Args:
        emoji: The emoji to find alternatives for
        context: Optional context
        llm: Optional language model

    Returns:
        str: Alternative emojis
    """
    crew_manager = EmojiAnalysisCrew(llm=llm)
    crew = crew_manager.find_alternatives_crew(emoji, context)
    result = crew.kickoff()
    return result


def generate_combinations(theme: str, count: int = 3, llm=None) -> str:
    """
    Generate emoji combinations for a theme

    Args:
        theme: The theme to express
        count: Number of combinations
        llm: Optional language model

    Returns:
        str: Emoji combinations
    """
    crew_manager = EmojiAnalysisCrew(llm=llm)
    crew = crew_manager.emoji_combination_crew(theme, count)
    result = crew.kickoff()
    return result
