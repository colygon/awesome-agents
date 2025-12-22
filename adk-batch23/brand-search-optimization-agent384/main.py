#!/usr/bin/env python3
"""
Brand Search Optimization Agent - CrewAI Implementation
SEO and brand visibility optimization using multi-agent system
"""

import os
import json
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
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
scrape_tool = ScrapeWebsiteTool()

# Define Agents

# 1. SEO Analyst
seo_analyst = Agent(
    role="SEO Research Analyst",
    goal="Analyze search rankings, keywords, and SEO performance",
    backstory="""You are an expert SEO analyst specializing in search engine
    optimization and brand visibility. You analyze search rankings, identify
    keyword opportunities, and understand search engine algorithms. You excel
    at competitive analysis and identifying gaps in search presence.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm
)

# 2. Content Strategist
content_strategist = Agent(
    role="Content Strategy Specialist",
    goal="Develop content strategies to improve search rankings",
    backstory="""You are a skilled content strategist who creates comprehensive
    content plans to boost search visibility. You understand user intent, content
    gaps, and how to create engaging content that ranks well in search engines.
    You specialize in keyword integration and semantic SEO.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Technical SEO Specialist
technical_seo = Agent(
    role="Technical SEO Expert",
    goal="Identify and fix technical SEO issues",
    backstory="""You are a technical SEO expert who analyzes website structure,
    performance, and technical optimization opportunities. You understand
    crawlability, indexability, site speed, mobile optimization, and schema
    markup. You identify technical barriers to search visibility.""",
    verbose=True,
    allow_delegation=False,
    tools=[scrape_tool],
    llm=llm
)

# 4. Competitive Intelligence Analyst
competitive_analyst = Agent(
    role="Competitive Intelligence Specialist",
    goal="Analyze competitor strategies and identify opportunities",
    backstory="""You are a competitive intelligence specialist who tracks
    competitor SEO strategies, content approaches, and market positioning.
    You identify what competitors are doing well and find opportunities
    for competitive advantage in search results.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm
)

# 5. Reporting Specialist
reporting_specialist = Agent(
    role="SEO Reporting Analyst",
    goal="Create comprehensive SEO reports and action plans",
    backstory="""You are an SEO reporting specialist who synthesizes analysis
    into actionable reports. You create clear, prioritized recommendations
    with metrics, timelines, and expected impact. You communicate technical
    concepts to both technical and non-technical stakeholders.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

def optimize_brand_search(brand_name: str, website_url: str, target_keywords: list = None) -> dict:
    """
    Conduct comprehensive brand search optimization analysis

    Args:
        brand_name: The brand name to optimize
        website_url: Brand's website URL
        target_keywords: List of target keywords (optional)

    Returns:
        dict with analysis and recommendations
    """

    if target_keywords is None:
        target_keywords = [brand_name]

    keywords_str = ", ".join(target_keywords)
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Task 1: SEO Performance Analysis
    seo_analysis_task = Task(
        description=f"""Conduct comprehensive SEO analysis for:
        Brand: {brand_name}
        Website: {website_url}
        Target Keywords: {keywords_str}

        Analyze:
        1. Current search rankings for target keywords
        2. Search visibility and presence
        3. SERP features (snippets, knowledge panels, etc.)
        4. Brand mention frequency in search results
        5. Keyword difficulty and search volume

        Use web search to check current rankings and visibility.
        Date: {current_date}

        Provide detailed SEO performance assessment.""",
        agent=seo_analyst,
        expected_output="Comprehensive SEO performance analysis with current rankings"
    )

    # Task 2: Competitive Analysis
    competitive_task = Task(
        description=f"""Analyze competitors for: {brand_name}

        Research:
        1. Identify top 5 competitors ranking for target keywords
        2. Analyze their content strategies
        3. Evaluate their backlink profiles
        4. Assess their search visibility
        5. Identify competitive advantages and gaps

        Use web search to find and analyze competitors.
        Focus on {keywords_str}

        Provide competitive intelligence report.""",
        agent=competitive_analyst,
        expected_output="Competitive analysis with competitor strategies and gaps",
        context=[seo_analysis_task]
    )

    # Task 3: Technical SEO Audit
    technical_task = Task(
        description=f"""Conduct technical SEO audit for: {website_url}

        Evaluate:
        1. Site structure and navigation
        2. Page speed and performance
        3. Mobile optimization
        4. Schema markup implementation
        5. Indexability and crawlability issues
        6. Meta tags and on-page SEO

        Use scraping tool to analyze the website.
        Identify technical optimization opportunities.""",
        agent=technical_seo,
        expected_output="Technical SEO audit with issues and recommendations",
        context=[seo_analysis_task]
    )

    # Task 4: Content Strategy Development
    content_task = Task(
        description=f"""Develop content strategy to improve search visibility for: {brand_name}

        Based on SEO and competitive analysis, create:
        1. Content gap analysis
        2. Keyword integration strategy
        3. Content types and formats recommendations
        4. Topic clusters and pillar pages
        5. Content calendar priorities

        Target keywords: {keywords_str}

        Provide comprehensive content strategy plan.""",
        agent=content_strategist,
        expected_output="Detailed content strategy with actionable recommendations",
        context=[seo_analysis_task, competitive_task]
    )

    # Task 5: Generate Optimization Report
    report_task = Task(
        description=f"""Create comprehensive brand search optimization report for: {brand_name}

        Synthesize all findings into actionable report:

        1. **Executive Summary**
           - Current search visibility status
           - Key findings and opportunities
           - Expected impact of recommendations

        2. **SEO Performance Analysis**
           - Current rankings and visibility
           - Strengths and weaknesses

        3. **Competitive Landscape**
           - Competitor strategies
           - Competitive opportunities

        4. **Technical SEO**
           - Technical issues identified
           - Optimization priorities

        5. **Content Strategy**
           - Content recommendations
           - Keyword integration plan

        6. **Action Plan**
           - Prioritized recommendations
           - Timeline and milestones
           - Success metrics

        Format as comprehensive Markdown report.""",
        agent=reporting_specialist,
        expected_output="Complete brand search optimization report in Markdown",
        context=[seo_analysis_task, competitive_task, technical_task, content_task]
    )

    # Create and run crew
    crew = Crew(
        agents=[seo_analyst, competitive_analyst, technical_seo, content_strategist, reporting_specialist],
        tasks=[seo_analysis_task, competitive_task, technical_task, content_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "seo_analysis": seo_analysis_task.output.raw if hasattr(seo_analysis_task, 'output') else "",
        "competitive_analysis": competitive_task.output.raw if hasattr(competitive_task, 'output') else "",
        "technical_audit": technical_task.output.raw if hasattr(technical_task, 'output') else "",
        "content_strategy": content_task.output.raw if hasattr(content_task, 'output') else "",
        "full_report": str(result),
        "metadata": {
            "brand": brand_name,
            "website": website_url,
            "keywords": target_keywords,
            "analysis_date": current_date
        }
    }

def save_report(content: str, filename: str):
    """Save optimization report to file"""
    if not filename.endswith('.md'):
        filename += '.md'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nReport saved to: {filename}")

if __name__ == "__main__":
    print("Brand Search Optimization Agent - CrewAI")
    print("=" * 60)

    # Get brand information
    brand = input("\nEnter brand name: ").strip()
    if not brand:
        brand = "TechStartup Inc"

    website = input("Enter website URL: ").strip()
    if not website:
        website = "https://example.com"

    keywords_input = input("Enter target keywords (comma-separated, optional): ").strip()
    keywords = [k.strip() for k in keywords_input.split(",")] if keywords_input else None

    print(f"\nAnalyzing brand: {brand}")
    print(f"Website: {website}")
    if keywords:
        print(f"Target keywords: {', '.join(keywords)}")
    print("\nThis may take several minutes...\n")

    # Run optimization analysis
    result = optimize_brand_search(brand, website, keywords)

    # Display report
    print("\n" + "=" * 60)
    print("BRAND SEARCH OPTIMIZATION REPORT")
    print("=" * 60)
    print(result["full_report"])

    # Save option
    save = input("\n\nSave report to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = input("Enter filename (without .md extension): ").strip()
        if filename:
            save_report(result["full_report"], filename)
