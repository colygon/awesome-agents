"""
McLachApp Sports Analytics Agents
CrewAI-powered intelligent agents for sports data analysis
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


class SportsAnalyticsAgents:
    """Factory class for creating sports analytics agents"""

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

    def data_analyst_agent(self) -> Agent:
        """
        Creates a Data Analyst Agent specialized in sports statistics

        This agent excels at:
        - Analyzing raw sports data
        - Identifying statistical patterns and trends
        - Processing player and team performance metrics
        - Data cleaning and validation
        """
        return Agent(
            role="Sports Data Analyst",
            goal="Analyze sports data to extract meaningful statistics and insights",
            backstory=(
                "You are an expert sports data analyst with years of experience "
                "working with professional sports teams. You have a deep understanding "
                "of statistical analysis, data quality, and sports metrics. Your specialty "
                "is transforming raw data into actionable insights that coaches and "
                "analysts can use to improve team performance."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=5
        )

    def performance_evaluator_agent(self) -> Agent:
        """
        Creates a Performance Evaluator Agent for player/team assessment

        This agent excels at:
        - Evaluating player performance across multiple metrics
        - Comparing players and teams
        - Identifying strengths and weaknesses
        - Creating performance reports
        """
        return Agent(
            role="Performance Evaluator",
            goal="Evaluate and compare player and team performance to identify key insights",
            backstory=(
                "You are a seasoned sports performance evaluator who has worked "
                "with top-tier sports organizations. You understand the nuances of "
                "player evaluation, including both quantitative metrics and qualitative "
                "factors. Your evaluations are known for being comprehensive, fair, "
                "and providing actionable recommendations for improvement."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=True,
            max_iter=5
        )

    def strategy_advisor_agent(self) -> Agent:
        """
        Creates a Strategy Advisor Agent for tactical recommendations

        This agent excels at:
        - Developing game strategies based on data
        - Identifying tactical advantages
        - Recommending lineup changes
        - Predicting opponent strategies
        """
        return Agent(
            role="Sports Strategy Advisor",
            goal="Provide strategic recommendations based on performance data and analytics",
            backstory=(
                "You are a brilliant sports strategist with a proven track record "
                "of helping teams win championships. You combine deep tactical knowledge "
                "with data-driven insights to create winning strategies. Your recommendations "
                "consider not just statistics, but also game context, opponent analysis, "
                "and situational factors. Coaches trust your judgment because you understand "
                "both the numbers and the game."
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
            "data_analyst": self.data_analyst_agent(),
            "performance_evaluator": self.performance_evaluator_agent(),
            "strategy_advisor": self.strategy_advisor_agent()
        }
