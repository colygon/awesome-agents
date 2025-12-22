"""
CrewAI Agents for Study Assistant - Agent 483
Multi-agent system for academic support and learning optimization
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_content_explainer_agent(llm):
    """
    Agent 1: Content Explainer - Breaks down complex topics into understandable concepts
    """
    return Agent(
        role='Academic Content Specialist',
        goal='Explain complex academic topics in clear, understandable ways using effective teaching techniques',
        backstory="""You are an expert educator with deep knowledge across multiple academic
        subjects including mathematics, science, history, literature, and more. You excel at
        breaking down complex concepts into digestible explanations using analogies, examples,
        and step-by-step reasoning. You understand different learning styles (visual, auditory,
        kinesthetic) and adapt your explanations accordingly. You use the Feynman Technique,
        socratic questioning, and active learning principles to ensure deep understanding.
        You make learning engaging and accessible to students of all levels.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_study_planner_agent(llm):
    """
    Agent 2: Study Planner - Creates effective study schedules and strategies
    """
    return Agent(
        role='Study Strategy Expert',
        goal='Design effective study plans and learning strategies optimized for retention and understanding',
        backstory="""You are a learning scientist who specializes in study optimization and
        academic planning. You understand evidence-based learning techniques including spaced
        repetition, active recall, interleaving, and the Pomodoro technique. You excel at
        creating realistic study schedules that balance multiple subjects, account for deadlines,
        and prevent burnout. You know how to prioritize topics based on difficulty and importance,
        build in review sessions, and incorporate breaks for optimal cognitive performance.
        You help students develop sustainable study habits and time management skills.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_test_prep_coach_agent(llm):
    """
    Agent 3: Test Prep Coach - Helps with exam preparation and practice
    """
    return Agent(
        role='Test Preparation Coach',
        goal='Create effective test preparation strategies and practice materials to maximize exam performance',
        backstory="""You are a test preparation expert who helps students excel on exams.
        You understand test-taking strategies, anxiety management, and how to identify and
        address knowledge gaps. You excel at creating practice questions, mock exams, and
        targeted review materials. You know how to analyze past exams to predict question
        types and topics. You teach effective strategies for multiple choice, essay questions,
        problem-solving, and time management during exams. You help students build confidence
        and reduce test anxiety through preparation and practice.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_all_agents(model="gpt-4", temperature=0.7):
    """
    Create all study assistant agents with the specified LLM configuration
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    return {
        'content_explainer': create_content_explainer_agent(llm),
        'study_planner': create_study_planner_agent(llm),
        'test_prep_coach': create_test_prep_coach_agent(llm)
    }
