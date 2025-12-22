from crewai import Agent
from textwrap import dedent
from tools import SearchTools, AnalysisTools

class DeepSearchAgents:
    def search_strategist(self):
        return Agent(
            role='Search Strategy Expert',
            goal='Design comprehensive search strategies to find relevant information',
            backstory=dedent("""\
                You are an expert in information retrieval and search strategy.
                You understand how to break down complex queries into effective
                search patterns and know how to find information across multiple
                sources and domains. You excel at query expansion and reformulation."""),
            tools=[SearchTools.search_web],
            verbose=True,
            allow_delegation=False
        )

    def information_analyst(self):
        return Agent(
            role='Information Analyst',
            goal='Analyze and synthesize information from multiple sources',
            backstory=dedent("""\
                You are a skilled analyst who can process large amounts of
                information and identify key insights. You excel at finding
                patterns, connections, and extracting relevant details from
                diverse sources. You can evaluate source credibility and
                information quality."""),
            tools=[
                SearchTools.search_web,
                AnalysisTools.analyze_content,
                AnalysisTools.extract_entities
            ],
            verbose=True,
            allow_delegation=False
        )

    def fact_checker(self):
        return Agent(
            role='Fact Verification Specialist',
            goal='Verify facts and cross-reference information across sources',
            backstory=dedent("""\
                You are a meticulous fact-checker who verifies claims by
                cross-referencing multiple reliable sources. You understand
                how to evaluate source credibility, identify potential biases,
                and distinguish between facts and opinions. You never accept
                information at face value."""),
            tools=[
                SearchTools.search_web,
                AnalysisTools.verify_facts
            ],
            verbose=True,
            allow_delegation=False
        )

    def research_synthesizer(self):
        return Agent(
            role='Research Synthesis Expert',
            goal='Synthesize findings into comprehensive, well-structured reports',
            backstory=dedent("""\
                You are an expert at synthesizing complex information into
                clear, comprehensive reports. You excel at organizing findings,
                identifying key themes, and presenting information in a logical
                and accessible manner. You ensure all sources are properly
                cited and findings are well-supported."""),
            tools=[AnalysisTools.summarize_findings],
            verbose=True,
            allow_delegation=False
        )
