#!/usr/bin/env python
"""
Auto Insurance CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import membership_specialist, claims_handler, roadside_coordinator, rewards_advisor
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("CYMBAL AUTO INSURANCE - AI Assistant")
    print("="*80)
    print("\nWelcome! How can I help you today?")
    print("\n1. Register new membership")
    print("2. File a claim")
    print("3. Request roadside assistance")
    print("4. Find rewards")

    choice = input("\nSelect option (1-4): ").strip()

    if choice == "1":
        print("\nLet's get you registered!")
        name = input("Full name: ").strip()
        address = input("Address: ").strip()

        tasks = create_tasks("membership", details={"name": name, "address": address})
        agents = [membership_specialist]

    elif choice == "2":
        member_id = input("Member ID: ").strip()
        print("\nI'm sorry to hear you need to file a claim.")

        tasks = create_tasks("claim", member_id=member_id)
        agents = [claims_handler]

    elif choice == "3":
        member_id = input("Member ID: ").strip()
        location = input("Your location: ").strip()

        tasks = create_tasks("roadside", member_id=member_id, details={"location": location})
        agents = [roadside_coordinator]

    elif choice == "4":
        member_id = input("Member ID: ").strip()
        location = input("Your location: ").strip()

        tasks = create_tasks("rewards", member_id=member_id, details={"location": location})
        agents = [rewards_advisor]

    else:
        print("Invalid option.")
        return

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nProcessing your request...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("REQUEST COMPLETE")
    print("="*80)
    print("\n" + str(result))
    print("\nIs there anything else I can help you with?")


if __name__ == "__main__":
    main()
