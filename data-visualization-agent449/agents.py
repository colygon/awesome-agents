from crewai import Agent
from tools import (
    data_analyzer,
    chart_generator,
    color_palette_selector,
    dashboard_builder,
    insight_extractor
)

class DataVisualizationAgents:
    def data_analyst_agent(self):
        return Agent(
            role='Data Analysis Specialist',
            goal='Analyze data and identify key patterns and insights',
            backstory="""You are a data analyst expert who understands statistical
            analysis, data patterns, and how to extract meaningful insights from
            datasets. You excel at identifying trends and anomalies.""",
            tools=[data_analyzer, insight_extractor],
            verbose=True,
            allow_delegation=True
        )

    def visualization_designer_agent(self):
        return Agent(
            role='Visualization Design Expert',
            goal='Design effective and beautiful data visualizations',
            backstory="""You are a visualization design expert who knows which
            chart types best represent different data. You understand visual
            hierarchy, color theory, and data-ink ratio principles.""",
            tools=[chart_generator, color_palette_selector],
            verbose=True,
            allow_delegation=False
        )

    def chart_specialist_agent(self):
        return Agent(
            role='Chart Generation Specialist',
            goal='Create various types of charts and graphs',
            backstory="""You are a charting expert who creates bar charts, line
            graphs, scatter plots, heatmaps, and more. You ensure charts are
            clear, accurate, and visually appealing.""",
            tools=[chart_generator, data_analyzer],
            verbose=True,
            allow_delegation=False
        )

    def dashboard_architect_agent(self):
        return Agent(
            role='Dashboard Architect',
            goal='Design and build comprehensive data dashboards',
            backstory="""You are a dashboard design expert who creates cohesive,
            informative dashboards. You arrange visualizations effectively and
            ensure dashboards tell a clear data story.""",
            tools=[dashboard_builder, chart_generator],
            verbose=True,
            allow_delegation=True
        )

    def insight_analyst_agent(self):
        return Agent(
            role='Insight Analyst',
            goal='Extract and communicate actionable insights from visualizations',
            backstory="""You are an insight specialist who translates visual data
            into actionable business intelligence. You identify key takeaways
            and communicate them clearly.""",
            tools=[insight_extractor, data_analyzer],
            verbose=True,
            allow_delegation=False
        )
