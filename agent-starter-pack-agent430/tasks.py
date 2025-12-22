from crewai import Task
from textwrap import dedent

class AgentStarterTasks:
    def research_topic(self, agent, topic):
        return Task(
            description=dedent(f"""
                Conduct comprehensive research on the topic.
                Topic: {topic}
                Include: key facts, statistics, trends, expert opinions.
            """),
            expected_output="""Research report with key findings, facts, statistics,
                trends, sources, and comprehensive topic overview.""",
            agent=agent
        )

    def create_content(self, agent, content_type):
        return Task(
            description=dedent(f"""
                Create high-quality content based on research.
                Content Type: {content_type}
                Include: well-structured, engaging, accurate content.
            """),
            expected_output="""Polished content that is well-written, properly
                structured, engaging, and meets quality standards.""",
            agent=agent
        )

    def analyze_findings(self, agent, data):
        return Task(
            description=dedent(f"""
                Analyze data and generate insights.
                Data: {data}
                Include: patterns, trends, insights, visualizations.
            """),
            expected_output="""Analysis report with patterns, trends, insights,
                visualizations, and actionable recommendations.""",
            agent=agent
        )

    def deliver_project(self, agent):
        return Task(
            description=dedent("""
                Integrate all outputs and deliver final project.
                Include: integrated report, quality assurance, final deliverables.
            """),
            expected_output="""Complete project deliverable with integrated research,
                content, analysis, and quality-checked final output.""",
            agent=agent
        )
