"""
Emoji Shortcodes - CrewAI Agents
Intelligent emoji analysis and recommendation system
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


class EmojiAnalysisAgents:
    """Factory class for creating emoji analysis agents"""

    def __init__(self, llm=None):
        """
        Initialize the agents factory

        Args:
            llm: Language model to use for agents. Defaults to GPT-4
        """
        self.llm = llm or ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )

    def emoji_analyst_agent(self) -> Agent:
        """
        Creates an Emoji Analyst Agent specialized in emoji understanding

        This agent excels at:
        - Analyzing emoji meanings and contexts
        - Understanding cultural and emotional significance
        - Categorizing emojis by usage and theme
        - Identifying emoji trends and patterns
        """
        return Agent(
            role="Emoji Analyst",
            goal="Analyze emojis to understand their meanings, contexts, and appropriate usage",
            backstory=(
                "You are an expert in digital communication and semiotics with a deep "
                "understanding of how emojis convey meaning across cultures and contexts. "
                "You have studied thousands of emoji usage patterns and can identify the "
                "most effective emojis for any given situation. Your specialty is helping "
                "people communicate more effectively using visual symbols."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=5
        )

    def recommendation_agent(self) -> Agent:
        """
        Creates a Recommendation Agent for emoji suggestions

        This agent excels at:
        - Suggesting relevant emojis for text content
        - Creating emoji combinations for specific emotions
        - Recommending alternatives for common emojis
        - Personalizing emoji recommendations
        """
        return Agent(
            role="Emoji Recommendation Specialist",
            goal="Provide intelligent emoji recommendations based on context and intent",
            backstory=(
                "You are a creative communication expert who understands the nuances "
                "of expressing emotions and ideas through emojis. You have helped "
                "thousands of users find the perfect emojis to enhance their messages. "
                "Your recommendations consider tone, audience, cultural context, and "
                "modern communication trends. You excel at suggesting emoji combinations "
                "that create visual impact and convey complex ideas."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
            max_iter=5
        )

    def usage_insights_agent(self) -> Agent:
        """
        Creates a Usage Insights Agent for emoji analytics

        This agent excels at:
        - Analyzing emoji usage patterns
        - Identifying popular emoji trends
        - Providing statistics on emoji effectiveness
        - Suggesting best practices for emoji communication
        """
        return Agent(
            role="Emoji Usage Insights Expert",
            goal="Provide insights and analytics on emoji usage patterns and trends",
            backstory=(
                "You are a data analyst specializing in digital communication trends "
                "and emoji analytics. You have analyzed millions of messages across "
                "various platforms to understand how emojis enhance communication. "
                "Your insights help people use emojis more effectively by revealing "
                "patterns, trends, and best practices. You understand which emojis "
                "work best in different contexts and can predict emerging emoji trends."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
            max_iter=5
        )

    def get_all_agents(self) -> dict:
        """
        Returns all available agents as a dictionary

        Returns:
            dict: Dictionary of agent name to agent instance
        """
        return {
            "emoji_analyst": self.emoji_analyst_agent(),
            "recommendation": self.recommendation_agent(),
            "usage_insights": self.usage_insights_agent()
        }
