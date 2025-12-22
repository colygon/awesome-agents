#!/usr/bin/env python
from crewai import Crew, Process
from agents import NewsAggregatorAgents
from tasks import NewsAggregatorTasks
from dotenv import load_dotenv

load_dotenv()

def run_news_aggregator():
    print("## Welcome to the News Aggregator Crew")
    print("--------------------------------------")

    topics = input("Topics of interest? (comma-separated): ")
    sources = input("Preferred news sources? (or 'all'): ")
    frequency = input("Update frequency? (hourly/daily): ")

    news_config = f"Topics: {topics}, Sources: {sources}, Frequency: {frequency}"

    agents = NewsAggregatorAgents()
    tasks_manager = NewsAggregatorTasks()

    collector = agents.news_collector()
    curator = agents.content_curator()
    fact_checker = agents.fact_checker()
    summarizer = agents.news_summarizer()

    collect_task = tasks_manager.collect_news(collector, topics)
    curate_task = tasks_manager.curate_content(curator, "Collected articles")
    verify_task = tasks_manager.verify_accuracy(fact_checker, "Top articles")
    briefing_task = tasks_manager.create_briefing(summarizer, "Curated and verified news")

    crew = Crew(
        agents=[collector, curator, fact_checker, summarizer],
        tasks=[collect_task, curate_task, verify_task, briefing_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()
    print("\n## News Aggregator Results\n")
    print(result)
    return result

if __name__ == "__main__":
    run_news_aggregator()
