"""
Example test file for McLachApp
Demonstrates how to test agents and crews
"""

import pytest
from agents import SportsAnalyticsAgents
from tasks import SportsAnalyticsTasks
from utils import (
    calculate_efficiency_rating,
    calculate_shot_accuracy,
    validate_player_data,
    validate_team_data
)


class TestUtilities:
    """Test utility functions"""

    def test_efficiency_rating(self):
        """Test efficiency rating calculation"""
        rating = calculate_efficiency_rating(goals=10, assists=5, games=20)
        assert rating == 0.75

    def test_efficiency_rating_zero_games(self):
        """Test efficiency rating with zero games"""
        rating = calculate_efficiency_rating(goals=10, assists=5, games=0)
        assert rating == 0.0

    def test_shot_accuracy(self):
        """Test shot accuracy calculation"""
        accuracy = calculate_shot_accuracy(shots_on_target=50, total_shots=100)
        assert accuracy == 50.0

    def test_shot_accuracy_zero_shots(self):
        """Test shot accuracy with zero shots"""
        accuracy = calculate_shot_accuracy(shots_on_target=0, total_shots=0)
        assert accuracy == 0.0

    def test_validate_player_data_valid(self):
        """Test player data validation with valid data"""
        player_data = {
            "name": "John Doe",
            "position": "Forward",
            "goals": 10,
            "assists": 5,
            "games_played": 20
        }
        errors = validate_player_data(player_data)
        assert len(errors) == 0

    def test_validate_player_data_missing_field(self):
        """Test player data validation with missing field"""
        player_data = {
            "position": "Forward",
            "goals": 10
        }
        errors = validate_player_data(player_data)
        assert len(errors) > 0
        assert any("name" in error for error in errors)

    def test_validate_player_data_negative_value(self):
        """Test player data validation with negative value"""
        player_data = {
            "name": "John Doe",
            "position": "Forward",
            "goals": -5
        }
        errors = validate_player_data(player_data)
        assert len(errors) > 0
        assert any("negative" in error.lower() for error in errors)

    def test_validate_team_data_valid(self):
        """Test team data validation with valid data"""
        team_data = {
            "team_name": "Athletic FC",
            "season": "2024-25",
            "wins": 10,
            "draws": 5,
            "losses": 3
        }
        errors = validate_team_data(team_data)
        assert len(errors) == 0


class TestAgents:
    """Test agent creation and configuration"""

    def test_agent_factory_creation(self):
        """Test that agent factory can be created"""
        factory = SportsAnalyticsAgents()
        assert factory is not None

    def test_data_analyst_agent_creation(self):
        """Test data analyst agent creation"""
        factory = SportsAnalyticsAgents()
        agent = factory.data_analyst_agent()
        assert agent is not None
        assert agent.role == "Sports Data Analyst"
        assert agent.verbose is True

    def test_performance_evaluator_agent_creation(self):
        """Test performance evaluator agent creation"""
        factory = SportsAnalyticsAgents()
        agent = factory.performance_evaluator_agent()
        assert agent is not None
        assert agent.role == "Performance Evaluator"
        assert agent.allow_delegation is True

    def test_strategy_advisor_agent_creation(self):
        """Test strategy advisor agent creation"""
        factory = SportsAnalyticsAgents()
        agent = factory.strategy_advisor_agent()
        assert agent is not None
        assert agent.role == "Sports Strategy Advisor"
        assert agent.allow_delegation is True

    def test_get_all_agents(self):
        """Test getting all agents"""
        factory = SportsAnalyticsAgents()
        agents = factory.get_all_agents()
        assert len(agents) == 3
        assert "data_analyst" in agents
        assert "performance_evaluator" in agents
        assert "strategy_advisor" in agents


class TestTasks:
    """Test task creation"""

    def test_task_factory_creation(self):
        """Test that task factory can be created"""
        factory = SportsAnalyticsTasks()
        assert factory is not None

    def test_analyze_player_statistics_task(self):
        """Test player statistics analysis task creation"""
        agent_factory = SportsAnalyticsAgents()
        agent = agent_factory.data_analyst_agent()
        task_factory = SportsAnalyticsTasks()

        player_data = {"name": "Test Player", "goals": 10}
        task = task_factory.analyze_player_statistics(agent, player_data)

        assert task is not None
        assert task.agent == agent
        assert "Test Player" in task.description or "goals" in task.description

    def test_evaluate_team_performance_task(self):
        """Test team performance evaluation task creation"""
        agent_factory = SportsAnalyticsAgents()
        agent = agent_factory.performance_evaluator_agent()
        task_factory = SportsAnalyticsTasks()

        team_data = {"team_name": "Test Team", "wins": 10}
        task = task_factory.evaluate_team_performance(agent, team_data)

        assert task is not None
        assert task.agent == agent

    def test_compare_players_task(self):
        """Test player comparison task creation"""
        agent_factory = SportsAnalyticsAgents()
        agent = agent_factory.performance_evaluator_agent()
        task_factory = SportsAnalyticsTasks()

        player1 = {"name": "Player 1", "goals": 10}
        player2 = {"name": "Player 2", "goals": 8}
        task = task_factory.compare_players(agent, player1, player2)

        assert task is not None
        assert task.agent == agent


# Note: Full integration tests with actual LLM calls would require
# an API key and would be slower/more expensive. These can be added
# as needed for end-to-end testing.

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
