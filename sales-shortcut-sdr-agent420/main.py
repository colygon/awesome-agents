#!/usr/bin/env python
"""SalesShortcut SDR - CrewAI Implementation"""

import sys
from crewai import Crew, Process
from agents import lead_researcher, personalization_specialist, email_copywriter, sequence_designer, objection_handler, performance_optimizer
from tasks import create_tasks


def main():
    print("SalesShortcut SDR - Sales Development System")
    print("="*60)

    product = input("Product/Service: ").strip() or "SaaS Product"
    industry = input("Target industry: ").strip() or "Technology"
    persona = input("Target persona (e.g., VP Sales): ").strip() or "VP Sales"

    campaign_info = {
        'product': product,
        'industry': industry,
        'persona': persona
    }

    tasks = create_tasks(campaign_info)
    crew = Crew(
        agents=[lead_researcher, personalization_specialist, email_copywriter, sequence_designer, objection_handler, performance_optimizer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    print(f"\nCreating SDR campaign for {product}...")
    result = crew.kickoff()
    print("\n" + "="*60)
    print("SDR CAMPAIGN READY")
    print("="*60)
    print(result)


if __name__ == "__main__":
    main()
