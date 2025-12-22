from crewai import Agent
from textwrap import dedent
from tools import DataPipelineTools, DataQualityTools, ETLTools

class DataEngineeringAgents:
    def data_architect(self):
        return Agent(
            role='Data Architecture Specialist',
            goal='Design scalable and efficient data pipelines and architectures',
            backstory=dedent("""\
                You are an expert data architect with deep knowledge of data
                pipeline design, ETL/ELT processes, and data warehouse architecture.
                You understand how to design systems that are scalable, maintainable,
                and performant. You excel at choosing the right technologies and
                patterns for different data engineering challenges."""),
            tools=[
                DataPipelineTools.design_pipeline,
                DataPipelineTools.analyze_data_flow
            ],
            verbose=True,
            allow_delegation=False
        )

    def etl_engineer(self):
        return Agent(
            role='ETL/ELT Engineer',
            goal='Implement data extraction, transformation, and loading processes',
            backstory=dedent("""\
                You are a skilled ETL engineer who can build robust data
                pipelines. You understand various data sources, transformation
                logic, and loading strategies. You can write efficient SQL,
                Python, and other data processing code. You know how to handle
                incremental loads, error handling, and data validation."""),
            tools=[
                ETLTools.extract_data,
                ETLTools.transform_data,
                ETLTools.load_data,
                ETLTools.create_etl_script
            ],
            verbose=True,
            allow_delegation=False
        )

    def data_quality_engineer(self):
        return Agent(
            role='Data Quality Specialist',
            goal='Ensure data quality, validation, and integrity',
            backstory=dedent("""\
                You are a data quality expert who understands how to validate
                data, detect anomalies, and ensure data integrity. You can
                design data quality checks, monitoring systems, and alerting
                mechanisms. You understand data profiling, quality metrics,
                and best practices for maintaining high-quality data."""),
            tools=[
                DataQualityTools.validate_data,
                DataQualityTools.check_data_quality,
                DataQualityTools.profile_data
            ],
            verbose=True,
            allow_delegation=False
        )

    def pipeline_optimizer(self):
        return Agent(
            role='Pipeline Optimization Expert',
            goal='Optimize data pipeline performance and resource utilization',
            backstory=dedent("""\
                You are an expert in optimizing data pipelines for performance,
                cost, and reliability. You understand query optimization,
                partitioning strategies, caching, and parallel processing. You
                can identify bottlenecks and implement solutions to improve
                pipeline efficiency."""),
            tools=[
                DataPipelineTools.optimize_pipeline,
                DataPipelineTools.monitor_performance
            ],
            verbose=True,
            allow_delegation=False
        )

    def data_engineering_lead(self):
        return Agent(
            role='Data Engineering Lead',
            goal='Coordinate data engineering projects and ensure best practices',
            backstory=dedent("""\
                You are a seasoned data engineering lead who can coordinate
                complex data projects. You understand the full data lifecycle,
                from ingestion to consumption. You ensure pipelines are
                well-documented, maintainable, and follow best practices. You
                can create comprehensive documentation and deployment plans."""),
            tools=[DataPipelineTools.generate_documentation],
            verbose=True,
            allow_delegation=False
        )
