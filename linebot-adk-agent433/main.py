"""LineBot ADK - CrewAI Multi-Agent LINE Bot Development System"""

import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_conversation_designer, create_bot_developer, create_ux_optimizer
from tasks import create_conversation_design_task, create_bot_development_task, create_ux_optimization_task


def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)


def run_linebot_development(bot_purpose: str, verbose: bool = True):
    if verbose:
        print("\nInitializing LINE Bot Development System\n")

    conversation_designer = create_conversation_designer()
    bot_developer = create_bot_developer()
    ux_optimizer = create_ux_optimizer()

    conversation_task = create_conversation_design_task(conversation_designer, bot_purpose)
    development_task = create_bot_development_task(bot_developer, conversation_task, bot_purpose)
    optimization_task = create_ux_optimization_task(ux_optimizer, conversation_task, development_task)

    crew = Crew(
        agents=[conversation_designer, bot_developer, ux_optimizer],
        tasks=[conversation_task, development_task, optimization_task],
        process=Process.sequential,
        verbose=True
    )

    start_time = datetime.now()
    result = crew.kickoff()
    duration = (datetime.now() - start_time).total_seconds()

    return {'result': result, 'duration': duration, 'timestamp': datetime.now().isoformat()}


def main():
    load_environment()
    bot_purpose = "Customer support bot for e-commerce platform"
    result = run_linebot_development(bot_purpose, verbose=True)
    print(f"\n\nLINE BOT DEVELOPMENT RESULTS\n{result['result']}")


if __name__ == "__main__":
    main()
