"""
CrewAI Tasks for Budget Tracker - Agent 482
"""

from crewai import Task


def create_expense_analysis_task(agent, financial_data):
    """
    Task for expense analyzer to categorize and analyze spending
    """
    return Task(
        description=f"""Analyze the financial data and provide spending insights:

        Financial Data: {financial_data}

        Your task:
        1. Categorize all expenses into standard categories:
           - Housing (rent/mortgage, utilities, insurance)
           - Transportation (car payment, gas, insurance, maintenance)
           - Food (groceries, dining out)
           - Entertainment (streaming, hobbies, activities)
           - Healthcare (insurance, medical, prescriptions)
           - Personal care (clothing, grooming)
           - Debt payments (credit cards, loans)
           - Savings and investments
           - Miscellaneous
        2. Calculate spending totals for each category
        3. Identify spending trends and patterns
        4. Detect unusual or excessive expenses
        5. Compare spending across time periods (if data available)
        6. Highlight areas of concern or opportunity

        Provide a comprehensive spending analysis with actionable insights.""",
        agent=agent,
        expected_output="""A detailed expense analysis including:
        - Complete expense categorization
        - Spending totals by category
        - Percentage breakdown of total spending
        - Month-over-month trends (if applicable)
        - Unusual expense alerts
        - Key spending insights
        - Areas requiring attention"""
    )


def create_budget_planning_task(agent, financial_data):
    """
    Task for budget planner to create personalized budget
    """
    return Task(
        description=f"""Create a realistic budget plan based on financial situation:

        Financial Data: {financial_data}

        Your task:
        1. Assess total income (after taxes)
        2. Review current expense analysis
        3. Apply appropriate budgeting methodology:
           - 50/30/20 rule (50% needs, 30% wants, 20% savings)
           - Zero-based budgeting (every dollar assigned)
           - Custom approach based on individual needs
        4. Set spending limits for each category:
           - Essential expenses (housing, food, utilities)
           - Discretionary spending (entertainment, dining)
           - Savings and debt repayment
        5. Ensure budget aligns with financial goals
        6. Provide variance analysis (budget vs actual)
        7. Suggest adjustments to align spending with budget

        Create a practical, sustainable budget plan.""",
        agent=agent,
        expected_output="""A comprehensive budget plan including:
        - Recommended budget for each category
        - Budget methodology used and rationale
        - Total income and expense allocation
        - Spending limits and guidelines
        - Variance analysis (actual vs budget)
        - Adjustment recommendations
        - Tips for staying within budget"""
    )


def create_savings_strategy_task(agent, financial_data):
    """
    Task for savings advisor to identify opportunities and goals
    """
    return Task(
        description=f"""Develop savings strategies and financial goals:

        Financial Data: {financial_data}

        Your task:
        1. Identify immediate cost-saving opportunities:
           - Subscription audits (unused services)
           - Bill negotiations (insurance, internet, phone)
           - Grocery optimization strategies
           - Energy cost reduction
           - Discretionary spending cuts
        2. Set realistic savings goals:
           - Emergency fund (3-6 months expenses)
           - Short-term goals (vacation, purchase)
           - Medium-term goals (down payment, education)
           - Long-term goals (retirement, investments)
        3. Create monthly savings targets
        4. Suggest automated savings strategies
        5. Recommend debt payoff priorities (if applicable)
        6. Track progress toward goals
        7. Provide motivational milestones

        Deliver actionable savings strategies and goal roadmap.""",
        agent=agent,
        expected_output="""A complete savings strategy including:
        - 5-10 immediate cost-saving opportunities
        - Estimated monthly savings from each opportunity
        - Defined savings goals with timelines
        - Monthly savings targets
        - Automated savings recommendations
        - Debt payoff strategy (if applicable)
        - Progress tracking framework
        - Milestone celebrations"""
    )


def create_all_tasks(agents, financial_data):
    """
    Create all tasks for the budget tracking crew
    """
    return [
        create_expense_analysis_task(agents['expense_analyzer'], financial_data),
        create_budget_planning_task(agents['budget_planner'], financial_data),
        create_savings_strategy_task(agents['savings_advisor'], financial_data)
    ]
