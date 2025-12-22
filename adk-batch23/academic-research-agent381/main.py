#!/usr/bin/env python3
"""
Academic Research Agent - CrewAI Implementation
Converts Google ADK Academic Research Agent to CrewAI multi-agent system
"""

import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, FileReadTool, DirectoryReadTool
from langchain_openai import ChatOpenAI
import datetime

# Initialize OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.7,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Initialize tools
search_tool = SerperDevTool()
file_read_tool = FileReadTool()
directory_tool = DirectoryReadTool()

# Define Agents

# 1. Literature Review Agent
literature_reviewer = Agent(
    role="Academic Literature Researcher",
    goal="Conduct comprehensive literature reviews and identify key research papers",
    backstory="""You are an expert academic researcher specializing in literature reviews.
    You excel at identifying seminal papers, tracking research trends, and synthesizing
    findings from multiple sources. You understand academic citation standards and can
    evaluate paper quality and relevance.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Data Analysis Agent
data_analyst = Agent(
    role="Research Data Analyst",
    goal="Analyze research data and extract meaningful insights",
    backstory="""You are a skilled research data analyst with expertise in quantitative
    and qualitative analysis methods. You can identify patterns, statistical significance,
    and derive actionable insights from complex datasets. You understand research
    methodologies and best practices in data interpretation.""",
    verbose=True,
    allow_delegation=False,
    tools=[file_read_tool, directory_tool],
    llm=llm
)

# 3. Paper Writing Agent
paper_writer = Agent(
    role="Academic Paper Writer",
    goal="Write well-structured, scholarly research papers",
    backstory="""You are an experienced academic writer who crafts high-quality research
    papers following academic standards. You excel at organizing complex information,
    presenting arguments logically, and writing in a clear, scholarly tone. You understand
    IMRAD structure (Introduction, Methods, Results, And Discussion) and citation formats.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 4. Citation and Bibliography Agent
citation_manager = Agent(
    role="Academic Citation Specialist",
    goal="Manage citations and create properly formatted bibliographies",
    backstory="""You are a meticulous citation specialist who ensures all references
    are properly formatted according to academic standards (APA, MLA, Chicago, etc.).
    You verify citation accuracy, check for completeness, and maintain consistency
    throughout the document.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def conduct_research(research_topic: str, citation_style: str = "APA") -> dict:
    """
    Conduct comprehensive academic research on a given topic

    Args:
        research_topic: The research question or topic
        citation_style: Citation format (APA, MLA, Chicago)

    Returns:
        dict with literature_review, analysis, paper, bibliography
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: Literature Review
    literature_task = Task(
        description=f"""Conduct a comprehensive literature review on:
        Topic: {research_topic}

        Your review should:
        1. Identify 10-15 key papers and sources
        2. Summarize major themes and findings
        3. Identify research gaps and opportunities
        4. Track evolution of ideas in the field
        5. Evaluate quality and relevance of sources

        Use web search to find recent and seminal papers.
        Current date: {current_date}

        Output a structured literature review with citations.""",
        agent=literature_reviewer,
        expected_output="A comprehensive literature review with key papers and findings"
    )

    # Task 2: Data Analysis and Synthesis
    analysis_task = Task(
        description=f"""Analyze and synthesize findings from the literature review.

        Your analysis should:
        1. Identify major themes and patterns
        2. Compare and contrast different approaches
        3. Highlight consensus and controversies
        4. Identify methodological trends
        5. Suggest research directions

        Focus on extracting actionable insights for the research paper.""",
        agent=data_analyst,
        expected_output="Detailed analysis and synthesis of research findings",
        context=[literature_task]
    )

    # Task 3: Write Research Paper
    writing_task = Task(
        description=f"""Write a comprehensive academic research paper on: {research_topic}

        Structure (IMRAD format):
        1. **Introduction**: Background, research question, significance
        2. **Literature Review**: Synthesize findings from literature review
        3. **Methodology**: Research approach (if applicable)
        4. **Results/Discussion**: Analysis and interpretation
        5. **Conclusion**: Summary, implications, future research

        Requirements:
        - Academic tone and scholarly language
        - Clear argumentation and logical flow
        - Integration of citations throughout
        - 3000-5000 words
        - Use {citation_style} citation style (in-text citations)

        Output complete paper in Markdown format.""",
        agent=paper_writer,
        expected_output="A complete academic research paper in Markdown",
        context=[literature_task, analysis_task]
    )

    # Task 4: Format Citations and Bibliography
    citation_task = Task(
        description=f"""Review the research paper and create a properly formatted bibliography.

        Tasks:
        1. Verify all in-text citations are correct
        2. Create complete bibliography/references section
        3. Ensure {citation_style} format is followed consistently
        4. Check for missing or incomplete citations
        5. Organize references alphabetically

        Output the complete paper with properly formatted bibliography.""",
        agent=citation_manager,
        expected_output=f"Final paper with complete {citation_style} bibliography",
        context=[writing_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[literature_reviewer, data_analyst, paper_writer, citation_manager],
        tasks=[literature_task, analysis_task, writing_task, citation_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "literature_review": literature_task.output.raw if hasattr(literature_task, 'output') else "",
        "analysis": analysis_task.output.raw if hasattr(analysis_task, 'output') else "",
        "draft_paper": writing_task.output.raw if hasattr(writing_task, 'output') else "",
        "final_paper": str(result),
        "metadata": {
            "topic": research_topic,
            "citation_style": citation_style,
            "date": current_date
        }
    }

def save_research_output(content: str, filename: str):
    """Save research output to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nResearch paper saved to: {filename}")

if __name__ == "__main__":
    print("Academic Research Agent - CrewAI")
    print("=" * 60)

    # Get research topic
    topic = input("\nEnter research topic or question: ").strip()
    if not topic:
        topic = "The Impact of Large Language Models on Academic Research"

    # Get citation style
    citation_style = input("Enter citation style (APA/MLA/Chicago) [APA]: ").strip().upper()
    if citation_style not in ["APA", "MLA", "CHICAGO"]:
        citation_style = "APA"

    print(f"\nConducting research on: {topic}")
    print(f"Citation style: {citation_style}")
    print("\nThis may take several minutes...\n")

    # Conduct research
    result = conduct_research(topic, citation_style)

    # Display result
    print("\n" + "=" * 60)
    print("FINAL RESEARCH PAPER")
    print("=" * 60)
    print(result["final_paper"])

    # Save option
    save = input("\n\nSave research paper to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_research_output(result["final_paper"], filename)
