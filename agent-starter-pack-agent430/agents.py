from crewai import Agent
from tools import AgentStarterTools

class AgentStarterAgents:
    def __init__(self):
        self.tools = AgentStarterTools()

    def research_agent(self):
        return Agent(
            role='Research Agent',
            goal='Conduct comprehensive research on any topic and gather information',
            backstory="""You are a skilled researcher who excels at finding,
            analyzing, and synthesizing information from various sources.""",
            tools=[
                self.tools.search_web,
                self.tools.summarize_content,
                self.tools.extract_key_facts
            ],
            verbose=True,
            allow_delegation=False
        )

    def writing_agent(self):
        return Agent(
            role='Content Writing Agent',
            goal='Create high-quality written content from research and ideas',
            backstory="""You are an expert writer who creates clear, engaging,
            and well-structured content for various purposes and audiences.""",
            tools=[
                self.tools.generate_content,
                self.tools.edit_text,
                self.tools.check_grammar
            ],
            verbose=True,
            allow_delegation=False
        )

    def analysis_agent(self):
        return Agent(
            role='Data Analysis Agent',
            goal='Analyze data and extract meaningful insights',
            backstory="""You are a data analyst who processes information,
            identifies patterns, and generates actionable insights.""",
            tools=[
                self.tools.analyze_data,
                self.tools.create_visualizations,
                self.tools.generate_insights
            ],
            verbose=True,
            allow_delegation=False
        )

    def coordinator_agent(self):
        return Agent(
            role='Project Coordinator',
            goal='Coordinate agent tasks and deliver comprehensive solutions',
            backstory="""You are a project manager who orchestrates multiple
            agents, integrates their work, and ensures quality deliverables.""",
            tools=[
                self.tools.integrate_outputs,
                self.tools.quality_check,
                self.tools.generate_final_report
            ],
            verbose=True,
            allow_delegation=True
        )
