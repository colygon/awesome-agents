"""
FOMC Research CrewAI Tasks
Defines workflow for Federal Reserve policy analysis
"""

from crewai import Task
from agents import document_researcher, economic_analyzer, policy_synthesizer


def create_tasks(research_query: str, date_range: str = "last 12 months"):
    """
    Create tasks for FOMC research workflow

    Args:
        research_query: Research question about Fed policy
        date_range: Time period to analyze

    Returns:
        List of Task objects
    """

    # Task 1: Analyze FOMC documents
    analyze_fomc_docs_task = Task(
        description=f"""Analyze FOMC documents to address the research query.

        Research Query: "{research_query}"
        Time Period: {date_range}

        Requirements:
        1. Retrieve relevant FOMC meeting minutes, statements, and press releases
        2. Identify key policy decisions and changes in the specified period
        3. Extract language about:
           - Interest rate decisions (federal funds rate)
           - Forward guidance
           - Balance sheet policy (QT/QE)
           - Economic outlook and projections
           - Dot plot expectations
        4. Note shifts in tone (hawkish vs dovish)
        5. Identify dissenting votes and their rationale
        6. Extract key quotes from Chair Powell and other members

        Provide structured analysis with:
        - Timeline of key decisions
        - Policy stance evolution
        - Notable quotes and statements
        - Sources cited""",
        agent=document_researcher,
        expected_output="""Comprehensive FOMC document analysis including:
        - Chronological timeline of policy decisions
        - Summary of policy stance changes
        - Key quotes from FOMC members
        - Forward guidance signals
        - Document sources with dates"""
    )

    # Task 2: Analyze economic data
    analyze_economic_data_task = Task(
        description=f"""Analyze economic data relevant to the research query.

        Research Query: "{research_query}"
        Time Period: {date_range}

        Requirements:
        1. Gather key economic indicators:
           - Inflation (CPI, PCE, Core PCE)
           - Employment (Unemployment rate, NFP, wage growth)
           - GDP and economic growth
           - Consumer spending and confidence
           - Housing market indicators
        2. Compare actual data to FOMC projections
        3. Identify trends and turning points
        4. Assess progress toward Fed's 2% inflation target
        5. Evaluate labor market conditions (maximum employment mandate)
        6. Calculate key metrics (real rates, unemployment gap, etc.)

        Provide data-driven analysis with:
        - Key metrics and trends
        - Deviations from FOMC projections
        - Charts/tables of critical indicators
        - Data sources""",
        agent=economic_analyzer,
        expected_output="""Economic data analysis including:
        - Summary of key indicator trends
        - Comparison to FOMC forecasts
        - Progress toward Fed mandates (inflation, employment)
        - Critical turning points or anomalies
        - Data sources and time periods""",
        context=[analyze_fomc_docs_task]
    )

    # Task 3: Synthesize policy insights
    synthesize_policy_task = Task(
        description=f"""Synthesize FOMC research and economic data into comprehensive policy insights.

        Research Query: "{research_query}"

        Requirements:
        1. Combine FOMC document analysis with economic data assessment
        2. Explain the relationship between data trends and policy decisions
        3. Identify key factors driving Fed decisions
        4. Assess current policy stance:
           - Is policy restrictive, neutral, or accommodative?
           - What is the terminal rate expectation?
           - When might policy pivot occur?
        5. Provide forward-looking analysis:
           - Likely next policy moves
           - Conditions that could trigger changes
           - Risks to the outlook
        6. Address market implications
        7. Note uncertainty and alternative scenarios

        Format:
        - Executive Summary
        - Current Policy Assessment
        - Key Drivers of Policy
        - Forward-Looking Analysis
        - Risks and Scenarios
        - Market Implications
        - Sources and References""",
        agent=policy_synthesizer,
        expected_output="""Comprehensive policy synthesis report with:
        - Executive summary of findings
        - Current policy stance assessment
        - Analysis of policy drivers
        - Forward-looking insights
        - Risk scenarios
        - Market implications
        - Complete source references""",
        context=[analyze_fomc_docs_task, analyze_economic_data_task]
    )

    return [analyze_fomc_docs_task, analyze_economic_data_task, synthesize_policy_task]


def create_quick_analysis_task(policy_question: str):
    """
    Create a simplified task for quick policy questions

    Args:
        policy_question: Specific question about Fed policy

    Returns:
        Single Task object
    """

    quick_task = Task(
        description=f"""Provide a concise answer to the policy question using FOMC documents and economic data.

        Question: "{policy_question}"

        Workflow:
        1. Retrieve relevant FOMC statements and meeting minutes
        2. Gather pertinent economic data
        3. Synthesize a clear, concise answer
        4. Cite specific FOMC communications and data sources
        5. Note any uncertainty or caveats

        Answer Format:
        [Direct answer to question]

        Supporting Evidence:
        - FOMC communication excerpts
        - Relevant economic data
        - Key quotes

        Sources:
        1) [Source 1]
        2) [Source 2]""",
        agent=document_researcher,
        expected_output="""Concise answer with:
        - Direct response to question
        - Supporting evidence from FOMC docs
        - Relevant economic data
        - Source citations"""
    )

    return [quick_task]
