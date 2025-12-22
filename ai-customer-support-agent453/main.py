#!/usr/bin/env python
"""
AI Customer Support CrewAI Main Application
Intelligent customer service automation system
"""

import sys
from crewai import Crew, Process
from agents import support_specialist, issue_resolver, escalation_manager
from tasks import create_tasks


def run_customer_support(inquiry: str, customer_id: str = None, priority: str = "normal"):
    """
    Run the AI Customer Support crew to handle customer inquiries

    Args:
        inquiry: The customer's question or issue
        customer_id: Optional customer identifier
        priority: Priority level - "low", "normal", "high", or "urgent"

    Returns:
        Support response and resolution plan
    """

    print("\n" + "="*80)
    print("AI CUSTOMER SUPPORT SYSTEM")
    print("="*80)
    print(f"\nCustomer Inquiry: {inquiry}")
    if customer_id:
        print(f"Customer ID: {customer_id}")
    print(f"Priority: {priority}\n")

    # Create tasks
    tasks = create_tasks(inquiry, customer_id, priority)

    # Create crew
    crew = Crew(
        agents=[support_specialist, issue_resolver, escalation_manager],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Execute the support workflow
    print("\nProcessing customer inquiry...\n")
    result = crew.kickoff()

    print("\n" + "="*80)
    print("SUPPORT ANALYSIS COMPLETE")
    print("="*80)
    print("\n" + str(result))

    return result


def main():
    """Main entry point for the application"""

    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║          AI CUSTOMER SUPPORT - CrewAI Edition                 ║
    ║                                                               ║
    ║  Intelligent Customer Service Automation                      ║
    ║  Analyze, troubleshoot, and resolve customer issues           ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

    # Check for command line arguments
    if len(sys.argv) > 1:
        inquiry = " ".join(sys.argv[1:])
        customer_id = None
        priority = "normal"
    else:
        # Interactive mode
        print("Welcome to AI Customer Support!\n")
        print("I help you handle customer inquiries with intelligence and empathy.\n")
        print("I can:")
        print("  • Analyze customer sentiment and urgency")
        print("  • Search knowledge base for solutions")
        print("  • Provide troubleshooting guidance")
        print("  • Draft empathetic responses")
        print("  • Manage escalations\n")

        inquiry = input("Enter customer inquiry or issue: ").strip()

        if not inquiry:
            print("\nError: No inquiry provided. Exiting.")
            sys.exit(1)

        customer_id = input("Customer ID (optional, press Enter to skip): ").strip() or None

        print("\nPriority levels:")
        print("  1. low - General questions")
        print("  2. normal - Standard support (default)")
        print("  3. high - Important issue")
        print("  4. urgent - Critical issue")

        priority_choice = input("\nSelect priority (1-4, default=2): ").strip()
        priority_map = {"1": "low", "2": "normal", "3": "high", "4": "urgent", "": "normal"}
        priority = priority_map.get(priority_choice, "normal")

    # Run the customer support workflow
    try:
        result = run_customer_support(inquiry, customer_id, priority)
        print("\n✓ Support analysis complete!")
        print("\nNext steps:")
        print("  1. Review the sentiment analysis and issue classification")
        print("  2. Send the drafted response or follow troubleshooting steps")
        print("  3. Escalate if recommended")
        print("  4. Track resolution and customer satisfaction")

    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Exiting.")
        sys.exit(0)

    except Exception as e:
        print(f"\n✗ Error during support processing: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
