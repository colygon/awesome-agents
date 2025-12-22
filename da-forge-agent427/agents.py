from crewai import Agent
from tools import DAForgeTools

class DAForgeAgents:
    def __init__(self):
        self.tools = DAForgeTools()

    def data_analyst(self):
        return Agent(
            role='Data Analyst',
            goal='Analyze datasets, identify patterns, and extract insights',
            backstory="""Expert data analyst specializing in exploratory data analysis,
            statistical modeling, and insight generation from complex datasets.""",
            tools=[
                self.tools.explore_dataset,
                self.tools.identify_patterns,
                self.tools.generate_statistics
            ],
            verbose=True,
            allow_delegation=False
        )

    def ml_engineer(self):
        return Agent(
            role='Machine Learning Engineer',
            goal='Build and optimize machine learning models for data predictions',
            backstory="""ML engineering specialist who builds, trains, and optimizes
            machine learning models for various data science tasks.""",
            tools=[
                self.tools.build_ml_model,
                self.tools.train_model,
                self.tools.evaluate_model
            ],
            verbose=True,
            allow_delegation=False
        )

    def visualization_specialist(self):
        return Agent(
            role='Data Visualization Specialist',
            goal='Create compelling visualizations and dashboards from data insights',
            backstory="""Visualization expert who transforms complex data into clear,
            actionable visual insights and interactive dashboards.""",
            tools=[
                self.tools.create_visualizations,
                self.tools.build_dashboard,
                self.tools.generate_reports
            ],
            verbose=True,
            allow_delegation=False
        )

    def data_science_lead(self):
        return Agent(
            role='Data Science Lead',
            goal='Coordinate data science projects and deliver comprehensive solutions',
            backstory="""Senior data scientist who leads projects, integrates analyses,
            and ensures delivery of high-quality data science solutions.""",
            tools=[
                self.tools.integrate_findings,
                self.tools.recommend_actions,
                self.tools.create_project_summary
            ],
            verbose=True,
            allow_delegation=True
        )
