"""
Emoji Shortcodes - CrewAI Tasks
Task definitions for emoji analysis and recommendations
"""

from crewai import Task
from agents import EmojiAnalysisAgents


class EmojiAnalysisTasks:
    """Factory class for creating emoji analysis tasks"""

    def __init__(self):
        """Initialize the tasks factory"""
        self.agents = EmojiAnalysisAgents()

    def analyze_emoji_task(self, emoji: str, emoji_data: dict = None) -> Task:
        """
        Creates a task to analyze a specific emoji

        Args:
            emoji: The emoji or shortcode to analyze
            emoji_data: Optional dictionary with emoji metadata

        Returns:
            Task: Analysis task for the emoji
        """
        context = f"Emoji: {emoji}"
        if emoji_data:
            context += f"\nShortcode: {emoji_data.get('shortcode', 'N/A')}"
            context += f"\nKeywords: {emoji_data.get('keywords', [])}"

        return Task(
            description=f"""
            Analyze the emoji '{emoji}' in detail:
            1. Describe the visual appearance and what it represents
            2. Explain its common meanings and interpretations
            3. Identify contexts where it's commonly used
            4. Discuss any cultural variations in meaning
            5. Rate its versatility (1-10) and explain why

            Context: {context}

            Provide a comprehensive analysis that helps users understand
            when and how to use this emoji effectively.
            """,
            agent=self.agents.emoji_analyst_agent(),
            expected_output="Detailed emoji analysis with meanings, contexts, and usage guidelines"
        )

    def recommend_emojis_task(self, text: str, tone: str = "neutral") -> Task:
        """
        Creates a task to recommend emojis for given text

        Args:
            text: The text content to suggest emojis for
            tone: The desired tone (happy, sad, professional, casual, etc.)

        Returns:
            Task: Recommendation task
        """
        return Task(
            description=f"""
            Recommend appropriate emojis for the following text:

            Text: "{text}"
            Desired Tone: {tone}

            Please provide:
            1. Top 5 most relevant emojis with shortcodes
            2. Explanation of why each emoji fits
            3. Suggested placement (beginning, end, or inline)
            4. Alternative emoji combinations
            5. Tone assessment and emoji compatibility

            Consider the context, tone, and modern communication trends
            when making recommendations.
            """,
            agent=self.agents.recommendation_agent(),
            expected_output="List of recommended emojis with placement suggestions and explanations"
        )

    def emoji_trend_analysis_task(self, emoji_list: list) -> Task:
        """
        Creates a task to analyze emoji usage trends

        Args:
            emoji_list: List of emojis to analyze

        Returns:
            Task: Trend analysis task
        """
        return Task(
            description=f"""
            Analyze usage trends for this set of emojis:
            {', '.join(emoji_list)}

            Provide insights on:
            1. Which emojis are most versatile and widely used
            2. Emerging trends or declining popularity
            3. Common emoji combinations and patterns
            4. Best practices for using these emojis effectively
            5. Recommendations for emoji discovery and exploration

            Base your analysis on modern communication patterns and
            digital communication research.
            """,
            agent=self.agents.usage_insights_agent(),
            expected_output="Comprehensive trend analysis with usage statistics and recommendations"
        )

    def emoji_sentiment_task(self, text_with_emojis: str) -> Task:
        """
        Creates a task to analyze sentiment expressed through emojis

        Args:
            text_with_emojis: Text containing emojis to analyze

        Returns:
            Task: Sentiment analysis task
        """
        return Task(
            description=f"""
            Analyze the sentiment and emotional tone of this message:

            "{text_with_emojis}"

            Provide:
            1. Overall sentiment (positive, negative, neutral, mixed)
            2. Specific emotions conveyed by each emoji
            3. How emojis enhance or modify the text meaning
            4. Effectiveness rating of emoji usage (1-10)
            5. Suggestions for improving emotional expression

            Consider both the text and emoji elements in your analysis.
            """,
            agent=self.agents.emoji_analyst_agent(),
            expected_output="Sentiment analysis with emotional breakdown and effectiveness rating"
        )

    def find_emoji_alternatives_task(self, emoji: str, context: str = "") -> Task:
        """
        Creates a task to find alternative emojis

        Args:
            emoji: The emoji to find alternatives for
            context: Optional context for the alternatives

        Returns:
            Task: Alternative finding task
        """
        context_str = f" in the context of: {context}" if context else ""

        return Task(
            description=f"""
            Find alternative emojis for: {emoji}{context_str}

            Provide:
            1. List of 8-10 alternative emojis with similar meanings
            2. Explanation of how each alternative differs
            3. Ranking by similarity (most to least similar)
            4. Use cases where each alternative works better
            5. Creative combinations using alternatives

            Help users discover new ways to express the same idea.
            """,
            agent=self.agents.recommendation_agent(),
            expected_output="List of alternative emojis with detailed comparisons and use cases"
        )

    def emoji_combination_task(self, theme: str, count: int = 3) -> Task:
        """
        Creates a task to generate emoji combinations for a theme

        Args:
            theme: The theme or concept to express
            count: Number of emoji combinations to generate

        Returns:
            Task: Combination generation task
        """
        return Task(
            description=f"""
            Create {count} creative emoji combinations for the theme: "{theme}"

            For each combination:
            1. Show the emoji sequence with shortcodes
            2. Explain what the combination expresses
            3. Suggest when to use it
            4. Rate creativity and effectiveness (1-10)
            5. Provide usage examples

            Be creative and consider modern emoji communication trends.
            Focus on combinations that are meaningful and visually appealing.
            """,
            agent=self.agents.recommendation_agent(),
            expected_output=f"{count} creative emoji combinations with explanations and usage examples"
        )
