#!/usr/bin/env python
"""
MCP-Gemma CrewAI Main Application
"""

import sys
from crewai import Crew, Process
from agents import mcp_coordinator, gemma_specialist, integration_expert
from tasks import create_tasks


def main():
    print("\n" + "="*80)
    print("MCP-GEMMA INTEGRATION")
    print("="*80)

    query = input("\nEnter your query: ").strip()
    if not query:
        print("No query provided.")
        return

    servers_input = input("MCP servers (comma-separated, default: filesystem,database): ").strip()
    servers = [s.strip() for s in servers_input.split(",")] if servers_input else ["filesystem", "database"]

    tasks = create_tasks(query, servers)
    crew = Crew(
        agents=[mcp_coordinator, gemma_specialist, integration_expert],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print("\nProcessing with MCP-Gemma...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("EXECUTION COMPLETE")
    print("="*80)
    print("\n" + str(result))


if __name__ == "__main__":
    main()
