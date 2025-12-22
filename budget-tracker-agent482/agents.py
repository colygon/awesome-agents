"""
CrewAI Agents for Budget Tracker - Agent 482
Multi-agent system for personal finance management and budget tracking
"""

from crewai import Agent
from langchain_openai import ChatOpenAI


def create_expense_analyzer_agent(llm):
    """
    Agent 1: Expense Analyzer - Categorizes and analyzes spending patterns
    """
    return Agent(
        role='Expense Analysis Specialist',
        goal='Analyze spending patterns, categorize expenses, and identify financial trends',
        backstory="""You are a financial analyst specializing in personal finance and expense
        tracking. You excel at categorizing transactions, identifying spending patterns, and
        detecting unusual or excessive expenditures. You understand common expense categories
        (housing, transportation, food, entertainment, utilities, healthcare, etc.) and can
        spot trends over time. You provide clear insights into where money is being spent and
        how spending patterns change month-to-month or season-to-season.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_budget_planner_agent(llm):
    """
    Agent 2: Budget Planner - Creates budgets and spending recommendations
    """
    return Agent(
        role='Budget Planning Expert',
        goal='Create realistic budgets based on income, expenses, and financial goals',
        backstory="""You are a certified financial planner who helps individuals create
        sustainable budgets aligned with their income and goals. You understand budgeting
        methodologies (50/30/20 rule, zero-based budgeting, envelope method) and can tailor
        recommendations to different lifestyles and income levels. You excel at setting
        realistic spending limits for each category while ensuring essential needs are met
        and financial goals are achievable. You provide actionable advice for staying within
        budget and adjusting when circumstances change.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_savings_advisor_agent(llm):
    """
    Agent 3: Savings Advisor - Identifies savings opportunities and financial goals
    """
    return Agent(
        role='Savings Strategy Advisor',
        goal='Identify cost-saving opportunities and help achieve financial goals',
        backstory="""You are a savings strategist who helps people optimize their spending
        and build wealth. You excel at finding areas where costs can be reduced without
        sacrificing quality of life, identifying subscription waste, negotiating bills,
        and suggesting smarter purchasing decisions. You understand the psychology of
        spending and provide practical, sustainable strategies for saving money. You help
        set realistic savings goals (emergency funds, retirement, major purchases) and
        create actionable plans to achieve them. You track progress and celebrate milestones.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_all_agents(model="gpt-4", temperature=0.7):
    """
    Create all budget tracking agents with the specified LLM configuration
    """
    llm = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    return {
        'expense_analyzer': create_expense_analyzer_agent(llm),
        'budget_planner': create_budget_planner_agent(llm),
        'savings_advisor': create_savings_advisor_agent(llm)
    }
