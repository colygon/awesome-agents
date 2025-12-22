"""
McLachApp Sports Analytics Tasks
CrewAI task definitions for sports analysis workflows
"""

from crewai import Task
from typing import Dict, Any


class SportsAnalyticsTasks:
    """Factory class for creating sports analytics tasks"""

    @staticmethod
    def analyze_player_statistics(agent, player_data: Dict[str, Any]) -> Task:
        """
        Create a task for analyzing player statistics

        Args:
            agent: The agent to assign this task to
            player_data: Dictionary containing player statistics

        Returns:
            Task: CrewAI task for player statistics analysis
        """
        return Task(
            description=(
                f"Analyze the following player statistics and provide insights:\n"
                f"{player_data}\n\n"
                "Your analysis should include:\n"
                "1. Key performance metrics and their significance\n"
                "2. Statistical trends over time\n"
                "3. Areas of strength and weakness\n"
                "4. Comparison to league averages (if available)\n"
                "5. Data quality assessment\n\n"
                "Provide a comprehensive statistical report."
            ),
            agent=agent,
            expected_output=(
                "A detailed statistical analysis report including key metrics, "
                "trends, strengths, weaknesses, and data quality assessment."
            )
        )

    @staticmethod
    def evaluate_team_performance(agent, team_data: Dict[str, Any]) -> Task:
        """
        Create a task for evaluating team performance

        Args:
            agent: The agent to assign this task to
            team_data: Dictionary containing team statistics

        Returns:
            Task: CrewAI task for team performance evaluation
        """
        return Task(
            description=(
                f"Evaluate the following team performance data:\n"
                f"{team_data}\n\n"
                "Your evaluation should include:\n"
                "1. Overall team performance rating\n"
                "2. Key contributors and their impact\n"
                "3. Team strengths and weaknesses\n"
                "4. Performance trends across the season\n"
                "5. Comparison with competitor teams\n\n"
                "Provide a comprehensive performance evaluation."
            ),
            agent=agent,
            expected_output=(
                "A comprehensive team performance evaluation including ratings, "
                "key contributors, strengths, weaknesses, trends, and competitive analysis."
            )
        )

    @staticmethod
    def generate_strategy_recommendations(agent, analysis_data: Dict[str, Any]) -> Task:
        """
        Create a task for generating strategic recommendations

        Args:
            agent: The agent to assign this task to
            analysis_data: Dictionary containing analysis results

        Returns:
            Task: CrewAI task for strategy recommendations
        """
        return Task(
            description=(
                f"Based on the following analysis data, generate strategic recommendations:\n"
                f"{analysis_data}\n\n"
                "Your recommendations should include:\n"
                "1. Tactical adjustments for improved performance\n"
                "2. Lineup optimization suggestions\n"
                "3. Training focus areas for players\n"
                "4. Game plan modifications\n"
                "5. Risk assessment and mitigation strategies\n\n"
                "Provide actionable strategic recommendations."
            ),
            agent=agent,
            expected_output=(
                "Actionable strategic recommendations including tactical adjustments, "
                "lineup suggestions, training priorities, game plan modifications, and risk assessment."
            )
        )

    @staticmethod
    def compare_players(agent, player1_data: Dict[str, Any], player2_data: Dict[str, Any]) -> Task:
        """
        Create a task for comparing two players

        Args:
            agent: The agent to assign this task to
            player1_data: Dictionary containing first player's statistics
            player2_data: Dictionary containing second player's statistics

        Returns:
            Task: CrewAI task for player comparison
        """
        return Task(
            description=(
                f"Compare the following two players:\n\n"
                f"Player 1: {player1_data}\n\n"
                f"Player 2: {player2_data}\n\n"
                "Your comparison should include:\n"
                "1. Side-by-side metric comparison\n"
                "2. Relative strengths and weaknesses\n"
                "3. Playing style differences\n"
                "4. Situational advantages\n"
                "5. Overall recommendation based on team needs\n\n"
                "Provide a detailed player comparison."
            ),
            agent=agent,
            expected_output=(
                "A detailed player comparison including metric comparisons, "
                "strengths/weaknesses, style differences, situational advantages, and recommendations."
            )
        )

    @staticmethod
    def analyze_match_performance(agent, match_data: Dict[str, Any]) -> Task:
        """
        Create a task for analyzing a specific match performance

        Args:
            agent: The agent to assign this task to
            match_data: Dictionary containing match statistics

        Returns:
            Task: CrewAI task for match analysis
        """
        return Task(
            description=(
                f"Analyze the following match performance data:\n"
                f"{match_data}\n\n"
                "Your analysis should include:\n"
                "1. Key moments and turning points\n"
                "2. Individual player contributions\n"
                "3. Team tactical execution\n"
                "4. Statistical highlights and lowlights\n"
                "5. Lessons learned and improvement areas\n\n"
                "Provide a comprehensive match analysis."
            ),
            agent=agent,
            expected_output=(
                "A comprehensive match analysis including key moments, player contributions, "
                "tactical execution, statistical highlights, and improvement areas."
            )
        )

    @staticmethod
    def predict_performance(agent, historical_data: Dict[str, Any], context: Dict[str, Any]) -> Task:
        """
        Create a task for predicting future performance

        Args:
            agent: The agent to assign this task to
            historical_data: Dictionary containing historical statistics
            context: Dictionary containing contextual information

        Returns:
            Task: CrewAI task for performance prediction
        """
        return Task(
            description=(
                f"Based on the following historical data and context, predict future performance:\n\n"
                f"Historical Data: {historical_data}\n\n"
                f"Context: {context}\n\n"
                "Your prediction should include:\n"
                "1. Expected performance metrics\n"
                "2. Confidence levels and uncertainty ranges\n"
                "3. Key factors influencing the prediction\n"
                "4. Potential scenarios (best case, worst case, most likely)\n"
                "5. Recommendations for maximizing performance\n\n"
                "Provide a data-driven performance prediction."
            ),
            agent=agent,
            expected_output=(
                "A data-driven performance prediction including expected metrics, "
                "confidence levels, influencing factors, scenario analysis, and recommendations."
            )
        )
