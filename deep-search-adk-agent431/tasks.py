"""
Deep Search ADK - CrewAI Task Definitions
Sequential Deep Research Workflow

This module defines the tasks for the multi-agent deep search workflow:
1. Query Analysis and Optimization
2. Comprehensive Research Execution
3. Findings Synthesis and Reporting
"""

from crewai import Task
from textwrap import dedent


def create_query_analysis_task(agent, query: str) -> Task:
    """
    Creates a task for analyzing and optimizing a search query.

    Args:
        agent: The Query Analyst agent
        query: The user's search query or research question

    Returns:
        Task: Configured query analysis task
    """
    return Task(
        description=dedent(f"""
            Analyze the following research query and develop a comprehensive search strategy:

            QUERY: {query}

            Your analysis must include:

            1. QUERY UNDERSTANDING
               - Identify the core question and user intent
               - Extract key concepts, entities, and topics
               - Determine the type of information needed (factual, analytical, comparative, etc.)
               - Assess the scope and complexity of the query
               - Identify any implicit assumptions or requirements

            2. SEARCH STRATEGY DEVELOPMENT
               - Break down the query into searchable sub-questions
               - Identify primary and secondary search terms
               - Suggest related concepts and synonyms to explore
               - Recommend specific sources and databases to consult
               - Prioritize search directions based on relevance and feasibility

            3. INFORMATION NEEDS ASSESSMENT
               - Current state and recent developments
               - Historical context and background
               - Expert opinions and perspectives
               - Empirical data and statistics
               - Practical applications and examples
               - Future trends and projections

            4. RESEARCH PLAN
               - Outline a logical sequence for research
               - Identify critical questions that must be answered
               - Note potential challenges or limitations
               - Suggest approaches for validating information
               - Define success criteria for comprehensive coverage

            Provide a clear, structured search strategy that will enable
            comprehensive and efficient research.
        """),
        expected_output=dedent("""
            A comprehensive query analysis document containing:

            ## Query Understanding
            - Core question and intent
            - Key concepts and entities
            - Information type needed
            - Scope assessment

            ## Search Strategy
            - Primary search questions (3-5)
            - Secondary research areas
            - Key search terms and synonyms
            - Recommended sources by category:
              * Academic/Research sources
              * Industry/Professional sources
              * News/Current events sources
              * Government/Official sources
              * Technical/Documentation sources

            ## Information Requirements
            - Essential facts to establish
            - Context needed
            - Perspectives to consider
            - Data/statistics required
            - Examples/case studies desired

            ## Research Plan
            - Research sequence (prioritized steps)
            - Critical questions checklist
            - Validation approach
            - Success criteria

            Format as a structured markdown document with clear sections and actionable guidance.
        """),
        agent=agent
    )


def create_deep_research_task(agent, query_analysis_output) -> Task:
    """
    Creates a task for conducting comprehensive multi-source research.

    Args:
        agent: The Deep Researcher agent
        query_analysis_output: Output from the query analysis task

    Returns:
        Task: Configured deep research task
    """
    return Task(
        description=dedent(f"""
            Based on the query analysis and search strategy below, conduct comprehensive
            research to gather authoritative information from multiple sources.

            SEARCH STRATEGY:
            {query_analysis_output}

            Execute the following research process:

            1. MULTI-SOURCE RESEARCH
               Consult diverse, authoritative sources across categories:
               - Academic: Research papers, studies, scholarly articles
               - Industry: Reports, whitepapers, expert analyses
               - News: Recent developments, current events, trends
               - Technical: Documentation, specifications, guides
               - Official: Government data, statistics, regulations
               - Expert: Interviews, opinions, commentaries

            2. INFORMATION GATHERING
               For each major aspect of the query, collect:
               - Factual information and definitions
               - Current state and recent developments
               - Historical context and evolution
               - Multiple perspectives and viewpoints
               - Empirical data and statistics
               - Expert opinions and analyses
               - Practical examples and case studies
               - Future projections and trends

            3. SOURCE EVALUATION
               For each source, document:
               - Source name, type, and publication date
               - Author credentials and expertise
               - Key findings or information obtained
               - Reliability and credibility assessment
               - Any potential biases or limitations

            4. EVIDENCE COMPILATION
               - Identify areas of consensus across sources
               - Note contradictions or disagreements
               - Highlight particularly authoritative sources
               - Flag information gaps or uncertainties
               - Collect supporting data and statistics

            5. QUALITY ASSURANCE
               - Cross-reference facts across multiple sources
               - Verify statistical claims
               - Identify primary vs. secondary sources
               - Note the recency of information
               - Assess completeness of coverage

            Conduct thorough research following the search strategy. Prioritize
            authoritative, recent, and well-documented sources. Aim for comprehensive
            coverage of all major aspects of the query.
        """),
        expected_output=dedent("""
            A comprehensive research findings document containing:

            ## Executive Summary
            - Brief overview of research scope
            - Key findings at a glance
            - Main sources consulted

            ## Detailed Findings
            Organized by major topic areas, each containing:
            - **Current State**: What is happening now
            - **Background**: Historical context and evolution
            - **Key Facts**: Essential information established
            - **Data & Statistics**: Relevant quantitative information
            - **Expert Perspectives**: Opinions and analyses from authorities
            - **Examples**: Real-world cases and applications
            - **Trends**: Emerging patterns and future directions

            ## Source Documentation
            For each major source:
            - [Source Name] (Type, Date)
              * Author/Organization and credentials
              * Key information obtained
              * Reliability assessment
              * URL/Citation

            ## Synthesis Notes
            - Areas of consensus across sources
            - Contradictions or debates
            - Information gaps
            - Particularly authoritative sources
            - Recency assessment

            Format as a structured markdown document with clear sections, bullet points,
            and proper source attribution throughout.
        """),
        agent=agent,
        context=[query_analysis_output] if isinstance(query_analysis_output, Task) else []
    )


def create_synthesis_task(agent, query: str, research_output) -> Task:
    """
    Creates a task for synthesizing research findings into actionable insights.

    Args:
        agent: The Synthesis Specialist agent
        query: The original user query
        research_output: Output from the deep research task

    Returns:
        Task: Configured synthesis task
    """
    return Task(
        description=dedent(f"""
            Synthesize the research findings below into a comprehensive, actionable report
            that directly answers the original query.

            ORIGINAL QUERY: {query}

            RESEARCH FINDINGS:
            {research_output}

            Create a synthesis that includes:

            1. DIRECT ANSWER
               - Provide a clear, concise answer to the original query
               - Support with evidence from research
               - Address all aspects of the question
               - Note any important caveats or limitations

            2. COMPREHENSIVE OVERVIEW
               - Current landscape and state of affairs
               - Key developments and trends
               - Important context and background
               - Major players or stakeholders

            3. IN-DEPTH ANALYSIS
               Organized by major themes:
               - Detailed examination of each aspect
               - Supporting evidence and examples
               - Multiple perspectives presented
               - Data and statistics integrated
               - Expert opinions included

            4. KEY INSIGHTS
               - Most important findings
               - Patterns and connections identified
               - Surprising or counterintuitive discoveries
               - Implications and significance
               - Areas of uncertainty or debate

            5. PRACTICAL IMPLICATIONS
               - Real-world applications
               - Strategic considerations
               - Opportunities and risks
               - Best practices or recommendations
               - Common pitfalls to avoid

            6. ACTIONABLE RECOMMENDATIONS
               - Specific next steps or actions
               - Resources for further exploration
               - Experts or organizations to consult
               - Tools or frameworks to use

            7. SOURCE SUMMARY
               - Most authoritative sources cited
               - Recency of information
               - Quality of evidence base
               - Limitations of available information

            Ensure the report is:
            - Well-organized with clear hierarchy
            - Evidence-based with proper citations
            - Balanced in presenting multiple perspectives
            - Accessible yet comprehensive
            - Actionable with concrete takeaways
        """),
        expected_output=dedent("""
            A comprehensive research report in the following format:

            # [Topic Title]

            ## Executive Summary
            - Direct answer to the query (2-3 paragraphs)
            - Key findings (3-5 bullet points)
            - Main recommendations (if applicable)

            ## Overview
            - Current state and landscape
            - Key context and background
            - Scope of this report

            ## Detailed Analysis

            ### [Major Theme 1]
            - Key findings
            - Supporting evidence
            - Expert perspectives
            - Relevant data/statistics
            - Examples and case studies

            ### [Major Theme 2]
            [Similar structure]

            [Additional themes as needed]

            ## Key Insights
            - Most important findings
            - Patterns identified
            - Implications
            - Areas of debate or uncertainty

            ## Practical Implications
            - Real-world applications
            - Strategic considerations
            - Opportunities and risks
            - Best practices

            ## Recommendations
            - Specific action items
            - Further resources
            - Experts to consult
            - Tools/frameworks

            ## Sources & Methodology
            - Summary of sources consulted
            - Quality of evidence
            - Information recency
            - Limitations

            ## Conclusion
            - Summary of main points
            - Final thoughts
            - Suggested next steps

            Format as a professional markdown document with proper headings, citations,
            and clear structure. Include inline citations [Source, Year] throughout.
        """),
        agent=agent,
        context=[research_output] if isinstance(research_output, Task) else []
    )
