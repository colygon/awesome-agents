"""
McLachApp Utilities
Helper functions for sports analytics
"""

from typing import Dict, Any, List
import json


def load_player_data(file_path: str) -> Dict[str, Any]:
    """
    Load player data from a JSON file

    Args:
        file_path: Path to the JSON file

    Returns:
        Dict containing player data
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def load_team_data(file_path: str) -> Dict[str, Any]:
    """
    Load team data from a JSON file

    Args:
        file_path: Path to the JSON file

    Returns:
        Dict containing team data
    """
    with open(file_path, 'r') as f:
        return json.load(f)


def save_analysis_results(results: Any, output_path: str):
    """
    Save analysis results to a file

    Args:
        results: Analysis results to save
        output_path: Path to save the results
    """
    with open(output_path, 'w') as f:
        if isinstance(results, (dict, list)):
            json.dump(results, f, indent=2)
        else:
            f.write(str(results))


def calculate_efficiency_rating(goals: int, assists: int, games: int) -> float:
    """
    Calculate a simple efficiency rating for a player

    Args:
        goals: Number of goals scored
        assists: Number of assists
        games: Number of games played

    Returns:
        float: Efficiency rating (goals + assists per game)
    """
    if games == 0:
        return 0.0
    return (goals + assists) / games


def calculate_shot_accuracy(shots_on_target: int, total_shots: int) -> float:
    """
    Calculate shot accuracy percentage

    Args:
        shots_on_target: Number of shots on target
        total_shots: Total number of shots

    Returns:
        float: Shot accuracy as a percentage
    """
    if total_shots == 0:
        return 0.0
    return (shots_on_target / total_shots) * 100


def format_player_summary(player_data: Dict[str, Any]) -> str:
    """
    Format player data into a readable summary

    Args:
        player_data: Dictionary containing player statistics

    Returns:
        str: Formatted player summary
    """
    summary = f"\n{player_data.get('name', 'Unknown Player')}\n"
    summary += "=" * 50 + "\n"
    summary += f"Position: {player_data.get('position', 'N/A')}\n"
    summary += f"Games Played: {player_data.get('games_played', 0)}\n"
    summary += f"Goals: {player_data.get('goals', 0)}\n"
    summary += f"Assists: {player_data.get('assists', 0)}\n"

    # Calculate efficiency if data available
    if all(k in player_data for k in ['goals', 'assists', 'games_played']):
        efficiency = calculate_efficiency_rating(
            player_data['goals'],
            player_data['assists'],
            player_data['games_played']
        )
        summary += f"Efficiency Rating: {efficiency:.2f}\n"

    return summary


def format_team_summary(team_data: Dict[str, Any]) -> str:
    """
    Format team data into a readable summary

    Args:
        team_data: Dictionary containing team statistics

    Returns:
        str: Formatted team summary
    """
    summary = f"\n{team_data.get('team_name', 'Unknown Team')}\n"
    summary += "=" * 50 + "\n"
    summary += f"Season: {team_data.get('season', 'N/A')}\n"
    summary += f"Games Played: {team_data.get('games_played', 0)}\n"
    summary += f"Record: {team_data.get('wins', 0)}W-{team_data.get('draws', 0)}D-{team_data.get('losses', 0)}L\n"
    summary += f"Points: {team_data.get('points', 0)}\n"
    summary += f"League Position: {team_data.get('league_position', 'N/A')}\n"
    summary += f"Goal Difference: {team_data.get('goal_difference', 0)}\n"

    return summary


def compare_metrics(value1: float, value2: float) -> str:
    """
    Compare two metric values and return a descriptive comparison

    Args:
        value1: First value
        value2: Second value

    Returns:
        str: Comparison description
    """
    diff = value1 - value2
    percentage = (diff / value2 * 100) if value2 != 0 else 0

    if abs(percentage) < 5:
        return "approximately equal"
    elif diff > 0:
        return f"{abs(percentage):.1f}% higher"
    else:
        return f"{abs(percentage):.1f}% lower"


def validate_player_data(player_data: Dict[str, Any]) -> List[str]:
    """
    Validate player data and return any errors

    Args:
        player_data: Dictionary containing player data

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    required_fields = ['name', 'position']
    for field in required_fields:
        if field not in player_data:
            errors.append(f"Missing required field: {field}")

    # Validate numeric fields
    numeric_fields = ['goals', 'assists', 'games_played']
    for field in numeric_fields:
        if field in player_data:
            if not isinstance(player_data[field], (int, float)):
                errors.append(f"Field {field} must be numeric")
            elif player_data[field] < 0:
                errors.append(f"Field {field} cannot be negative")

    return errors


def validate_team_data(team_data: Dict[str, Any]) -> List[str]:
    """
    Validate team data and return any errors

    Args:
        team_data: Dictionary containing team data

    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []

    required_fields = ['team_name', 'season']
    for field in required_fields:
        if field not in team_data:
            errors.append(f"Missing required field: {field}")

    # Validate numeric fields
    numeric_fields = ['wins', 'draws', 'losses', 'goals_scored', 'goals_conceded']
    for field in numeric_fields:
        if field in team_data:
            if not isinstance(team_data[field], (int, float)):
                errors.append(f"Field {field} must be numeric")
            elif team_data[field] < 0:
                errors.append(f"Field {field} cannot be negative")

    return errors
