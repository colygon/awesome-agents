"""
CrewAI Integration for GPT Search

This module provides the main integration point for running GPT Search with CrewAI agents.
It can be used as a drop-in replacement for the OpenAI inference function.
"""

import os
from crewai import Crew, Process
from agents import GPTSearchAgents
from tasks import GPTSearchTasks


def crewai_inference(data: dict, k: int = 5, temperature: float = 0.1, api_key: str = None) -> str:
    """
    Run semantic search and answer generation using CrewAI agents.

    This function replaces the original openai_inference function with a multi-agent
    approach that provides more thorough analysis and higher quality answers.

    Args:
        data: Dictionary containing 'query' and 'top_results' keys
        k: Number of top results to consider (default: 5)
        temperature: Temperature for LLM responses (default: 0.1)
        api_key: OpenAI API key (optional, will use environment variable if not provided)

    Returns:
        str: Generated answer to the query

    Example:
        >>> data = {
        ...     'query': 'What is machine learning?',
        ...     'top_results': ['ML is...', 'Machine learning refers to...']
        ... }
        >>> answer = crewai_inference(data, k=5)
    """
    # Extract query and results
    query = data['query']
    top_results = data['top_results']

    # Initialize agents and tasks
    agents = GPTSearchAgents(api_key=api_key)
    tasks_factory = GPTSearchTasks()

    # Create agents
    search_agent = agents.semantic_search_agent()
    synthesis_agent = agents.answer_synthesizer_agent()
    validator_agent = agents.quality_validator_agent()

    # Create tasks
    search_task = tasks_factory.search_task(search_agent, query, top_results)
    answer_task = tasks_factory.answer_synthesis_task(synthesis_agent, query, search_task)
    validation_task = tasks_factory.quality_validation_task(validator_agent, query, answer_task, top_results)

    # Create crew
    crew = Crew(
        agents=[search_agent, synthesis_agent, validator_agent],
        tasks=[search_task, answer_task, validation_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    try:
        result = crew.kickoff()
        return str(result)
    except Exception as e:
        return f"Error processing query: {str(e)}\nFalling back to: Unable to answer the query."


def simple_crewai_inference(data: dict, k: int = 5, temperature: float = 0.1, api_key: str = None) -> str:
    """
    Simplified CrewAI inference using only search and synthesis agents.

    This is a faster alternative that skips the quality validation step.
    Suitable for simpler queries or when speed is more important than thoroughness.

    Args:
        data: Dictionary containing 'query' and 'top_results' keys
        k: Number of top results to consider (default: 5)
        temperature: Temperature for LLM responses (default: 0.1)
        api_key: OpenAI API key (optional, will use environment variable if not provided)

    Returns:
        str: Generated answer to the query
    """
    # Extract query and results
    query = data['query']
    top_results = data['top_results']

    # Initialize agents and tasks
    agents = GPTSearchAgents(api_key=api_key)
    tasks_factory = GPTSearchTasks()

    # Create agents (only search and synthesis)
    search_agent = agents.semantic_search_agent()
    synthesis_agent = agents.answer_synthesizer_agent()

    # Create tasks
    search_task = tasks_factory.search_task(search_agent, query, top_results)
    answer_task = tasks_factory.answer_synthesis_task(synthesis_agent, query, search_task)

    # Create crew
    crew = Crew(
        agents=[search_agent, synthesis_agent],
        tasks=[search_task, answer_task],
        process=Process.sequential,
        verbose=True
    )

    # Execute the crew
    try:
        result = crew.kickoff()
        return str(result)
    except Exception as e:
        return f"Error processing query: {str(e)}\nFalling back to: Unable to answer the query."


if __name__ == "__main__":
    # Example usage
    sample_data = {
        'query': 'How has technology transformed the way we work?',
        'top_results': [
            'Technology has revolutionized workplace communication through email and instant messaging.',
            'Remote work became possible due to advances in video conferencing and cloud computing.',
            'Automation has changed many traditional job roles and created new opportunities.',
            'Digital tools have increased productivity and collaboration across teams.',
            'The gig economy emerged as a result of technological platforms connecting workers with opportunities.'
        ]
    }

    print("Running CrewAI Inference Example...")
    print("=" * 80)
    answer = crewai_inference(sample_data, k=5)
    print("\nFinal Answer:")
    print("=" * 80)
    print(answer)
