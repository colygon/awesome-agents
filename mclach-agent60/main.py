"""
McLachApp - Sports Analytics Application with CrewAI
Main application entry point
"""

import os
from typing import Dict, Any
from crew import SportsAnalyticsCrew, run_player_analysis, run_team_analysis
from langchain_openai import ChatOpenAI


def setup_llm():
    """
    Setup and configure the language model

    Returns:
        Configured ChatOpenAI instance
    """
    # Check for API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY environment variable not set. "
            "Please set it to use the application."
        )

    return ChatOpenAI(
        model="gpt-4",
        temperature=0.7,
        api_key=api_key
    )


def example_player_analysis():
    """Example of analyzing a single player"""
    print("\n" + "="*80)
    print("EXAMPLE: Player Analysis")
    print("="*80 + "\n")

    # Example player data
    player_data = {
        "name": "John Doe",
        "position": "Forward",
        "games_played": 38,
        "goals": 25,
        "assists": 12,
        "shots": 150,
        "shots_on_target": 85,
        "pass_completion": 82.5,
        "tackles": 45,
        "interceptions": 30,
        "minutes_played": 3200,
        "yellow_cards": 4,
        "red_cards": 0
    }

    try:
        llm = setup_llm()
        result = run_player_analysis(player_data, llm=llm)
        print("\nAnalysis Result:")
        print(result)
    except Exception as e:
        print(f"Error running analysis: {e}")


def example_team_analysis():
    """Example of analyzing a team"""
    print("\n" + "="*80)
    print("EXAMPLE: Team Analysis")
    print("="*80 + "\n")

    # Example team data
    team_data = {
        "team_name": "Athletic FC",
        "season": "2024-25",
        "games_played": 38,
        "wins": 22,
        "draws": 10,
        "losses": 6,
        "goals_scored": 75,
        "goals_conceded": 40,
        "goal_difference": 35,
        "points": 76,
        "league_position": 3,
        "possession_avg": 58.5,
        "pass_accuracy": 84.2,
        "shots_per_game": 15.3,
        "shots_on_target_per_game": 6.2,
        "clean_sheets": 15
    }

    try:
        llm = setup_llm()
        result = run_team_analysis(team_data, llm=llm)
        print("\nAnalysis Result:")
        print(result)
    except Exception as e:
        print(f"Error running analysis: {e}")


def example_custom_crew():
    """Example of creating and running a custom crew"""
    print("\n" + "="*80)
    print("EXAMPLE: Custom Crew Configuration")
    print("="*80 + "\n")

    try:
        llm = setup_llm()
        crew_manager = SportsAnalyticsCrew(llm=llm)

        # Example: Compare two players
        player1 = {
            "name": "Player A",
            "goals": 25,
            "assists": 10,
            "games": 35
        }

        player2 = {
            "name": "Player B",
            "goals": 20,
            "assists": 18,
            "games": 38
        }

        crew = crew_manager.compare_players_crew(player1, player2)
        result = crew.kickoff()

        print("\nComparison Result:")
        print(result)
    except Exception as e:
        print(f"Error running custom crew: {e}")


def main():
    """Main application entry point"""
    print("\n" + "="*80)
    print("McLachApp - Sports Analytics with CrewAI")
    print("="*80)

    # Check for API key
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  WARNING: OPENAI_API_KEY environment variable not set!")
        print("Please set your OpenAI API key to use this application:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        print("\nRunning in demo mode (no actual LLM calls)...\n")
        return

    # Menu
    while True:
        print("\n" + "-"*80)
        print("Choose an analysis type:")
        print("1. Player Analysis")
        print("2. Team Analysis")
        print("3. Player Comparison (Custom Crew)")
        print("4. Exit")
        print("-"*80)

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            example_player_analysis()
        elif choice == "2":
            example_team_analysis()
        elif choice == "3":
            example_custom_crew()
        elif choice == "4":
            print("\nThank you for using McLachApp!")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
