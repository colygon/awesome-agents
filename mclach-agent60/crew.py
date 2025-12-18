"""
McLachApp Sports Analytics Crew
CrewAI orchestration for sports analytics workflows
"""

from crewai import Crew, Process
from typing import Dict, Any, List
from agents import SportsAnalyticsAgents
from tasks import SportsAnalyticsTasks


class SportsAnalyticsCrew:
    """Main crew orchestration for sports analytics"""

    def __init__(self, llm=None):
        """
        Initialize the sports analytics crew

        Args:
            llm: Language model to use for agents. Defaults to GPT-4
        """
        self.agents_factory = SportsAnalyticsAgents(llm=llm)
        self.tasks_factory = SportsAnalyticsTasks()

    def analyze_player_crew(self, player_data: Dict[str, Any]) -> Crew:
        """
        Create a crew for comprehensive player analysis

        This crew uses all three agents in sequence:
        1. Data Analyst analyzes raw statistics
        2. Performance Evaluator evaluates performance
        3. Strategy Advisor provides recommendations

        Args:
            player_data: Dictionary containing player statistics

        Returns:
            Crew: Configured CrewAI crew for player analysis
        """
        # Get agents
        data_analyst = self.agents_factory.data_analyst_agent()
        performance_evaluator = self.agents_factory.performance_evaluator_agent()
        strategy_advisor = self.agents_factory.strategy_advisor_agent()

        # Create tasks
        analysis_task = self.tasks_factory.analyze_player_statistics(
            agent=data_analyst,
            player_data=player_data
        )

        evaluation_task = Task(
            description=(
                "Based on the statistical analysis, evaluate the player's overall performance. "
                "Consider their strengths, weaknesses, and potential for improvement. "
                "Provide a comprehensive performance rating."
            ),
            agent=performance_evaluator,
            expected_output="A detailed performance evaluation with ratings and assessment.",
            context=[analysis_task]
        )

        strategy_task = Task(
            description=(
                "Based on the analysis and evaluation, provide strategic recommendations "
                "for maximizing this player's effectiveness. Include training suggestions, "
                "tactical deployment, and development priorities."
            ),
            agent=strategy_advisor,
            expected_output="Strategic recommendations for player development and deployment.",
            context=[analysis_task, evaluation_task]
        )

        # Create and return crew
        return Crew(
            agents=[data_analyst, performance_evaluator, strategy_advisor],
            tasks=[analysis_task, evaluation_task, strategy_task],
            process=Process.sequential,
            verbose=True
        )

    def analyze_team_crew(self, team_data: Dict[str, Any]) -> Crew:
        """
        Create a crew for comprehensive team analysis

        Args:
            team_data: Dictionary containing team statistics

        Returns:
            Crew: Configured CrewAI crew for team analysis
        """
        # Get agents
        data_analyst = self.agents_factory.data_analyst_agent()
        performance_evaluator = self.agents_factory.performance_evaluator_agent()
        strategy_advisor = self.agents_factory.strategy_advisor_agent()

        # Create tasks
        analysis_task = Task(
            description=(
                f"Analyze the following team statistics:\n{team_data}\n\n"
                "Provide insights on team performance metrics, trends, and patterns."
            ),
            agent=data_analyst,
            expected_output="Detailed statistical analysis of team performance."
        )

        evaluation_task = self.tasks_factory.evaluate_team_performance(
            agent=performance_evaluator,
            team_data=team_data
        )
        evaluation_task.context = [analysis_task]

        strategy_task = self.tasks_factory.generate_strategy_recommendations(
            agent=strategy_advisor,
            analysis_data={"team_data": team_data}
        )
        strategy_task.context = [analysis_task, evaluation_task]

        # Create and return crew
        return Crew(
            agents=[data_analyst, performance_evaluator, strategy_advisor],
            tasks=[analysis_task, evaluation_task, strategy_task],
            process=Process.sequential,
            verbose=True
        )

    def compare_players_crew(
        self,
        player1_data: Dict[str, Any],
        player2_data: Dict[str, Any]
    ) -> Crew:
        """
        Create a crew for comparing two players

        Args:
            player1_data: Dictionary containing first player's statistics
            player2_data: Dictionary containing second player's statistics

        Returns:
            Crew: Configured CrewAI crew for player comparison
        """
        # Get agents
        data_analyst = self.agents_factory.data_analyst_agent()
        performance_evaluator = self.agents_factory.performance_evaluator_agent()

        # Create tasks
        analysis_task = Task(
            description=(
                f"Analyze and compare the statistics of two players:\n\n"
                f"Player 1: {player1_data}\n\nPlayer 2: {player2_data}\n\n"
                "Provide a detailed statistical comparison."
            ),
            agent=data_analyst,
            expected_output="Statistical comparison of the two players."
        )

        comparison_task = self.tasks_factory.compare_players(
            agent=performance_evaluator,
            player1_data=player1_data,
            player2_data=player2_data
        )
        comparison_task.context = [analysis_task]

        # Create and return crew
        return Crew(
            agents=[data_analyst, performance_evaluator],
            tasks=[analysis_task, comparison_task],
            process=Process.sequential,
            verbose=True
        )

    def match_analysis_crew(self, match_data: Dict[str, Any]) -> Crew:
        """
        Create a crew for analyzing a specific match

        Args:
            match_data: Dictionary containing match statistics

        Returns:
            Crew: Configured CrewAI crew for match analysis
        """
        # Get agents
        data_analyst = self.agents_factory.data_analyst_agent()
        performance_evaluator = self.agents_factory.performance_evaluator_agent()
        strategy_advisor = self.agents_factory.strategy_advisor_agent()

        # Create tasks
        match_analysis_task = self.tasks_factory.analyze_match_performance(
            agent=data_analyst,
            match_data=match_data
        )

        performance_evaluation_task = Task(
            description=(
                "Based on the match analysis, evaluate the overall team and individual "
                "player performances. Identify standout performances and areas needing improvement."
            ),
            agent=performance_evaluator,
            expected_output="Performance evaluation of the match.",
            context=[match_analysis_task]
        )

        tactical_review_task = Task(
            description=(
                "Based on the match analysis and performance evaluation, provide tactical "
                "insights and recommendations for future matches. Identify what worked, "
                "what didn't, and how to improve."
            ),
            agent=strategy_advisor,
            expected_output="Tactical review and recommendations for future matches.",
            context=[match_analysis_task, performance_evaluation_task]
        )

        # Create and return crew
        return Crew(
            agents=[data_analyst, performance_evaluator, strategy_advisor],
            tasks=[match_analysis_task, performance_evaluation_task, tactical_review_task],
            process=Process.sequential,
            verbose=True
        )


# Import Task here to avoid circular import
from crewai import Task


def run_player_analysis(player_data: Dict[str, Any], llm=None) -> Dict[str, Any]:
    """
    Convenience function to run a complete player analysis

    Args:
        player_data: Dictionary containing player statistics
        llm: Optional language model to use

    Returns:
        Dict containing analysis results
    """
    crew_manager = SportsAnalyticsCrew(llm=llm)
    crew = crew_manager.analyze_player_crew(player_data)
    result = crew.kickoff()
    return result


def run_team_analysis(team_data: Dict[str, Any], llm=None) -> Dict[str, Any]:
    """
    Convenience function to run a complete team analysis

    Args:
        team_data: Dictionary containing team statistics
        llm: Optional language model to use

    Returns:
        Dict containing analysis results
    """
    crew_manager = SportsAnalyticsCrew(llm=llm)
    crew = crew_manager.analyze_team_crew(team_data)
    result = crew.kickoff()
    return result


def run_player_comparison(
    player1_data: Dict[str, Any],
    player2_data: Dict[str, Any],
    llm=None
) -> Dict[str, Any]:
    """
    Convenience function to run a player comparison

    Args:
        player1_data: Dictionary containing first player's statistics
        player2_data: Dictionary containing second player's statistics
        llm: Optional language model to use

    Returns:
        Dict containing comparison results
    """
    crew_manager = SportsAnalyticsCrew(llm=llm)
    crew = crew_manager.compare_players_crew(player1_data, player2_data)
    result = crew.kickoff()
    return result


def run_match_analysis(match_data: Dict[str, Any], llm=None) -> Dict[str, Any]:
    """
    Convenience function to run a match analysis

    Args:
        match_data: Dictionary containing match statistics
        llm: Optional language model to use

    Returns:
        Dict containing analysis results
    """
    crew_manager = SportsAnalyticsCrew(llm=llm)
    crew = crew_manager.match_analysis_crew(match_data)
    result = crew.kickoff()
    return result
