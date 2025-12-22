"""
Data Engineering Agent System
CrewAI implementation for data pipeline operations
Migrated from Google ADK to CrewAI framework
"""

from crewai import Agent
from textwrap import dedent


class DataEngineeringAgents:
    """Data Engineering specialist agents for pipeline operations"""

    def data_ingestion_agent(self):
        """
        Agent responsible for data ingestion from various sources
        Handles connection, extraction, and initial validation
        """
        return Agent(
            role="Data Ingestion Specialist",
            goal="Extract and ingest data from various sources efficiently and reliably",
            backstory=dedent("""
                You are an expert in data ingestion with extensive experience in
                connecting to diverse data sources including databases, APIs, files,
                and streaming platforms. You understand data formats (CSV, JSON, Parquet,
                Avro), protocols (REST, JDBC, ODBC), and can handle both batch and
                real-time data ingestion. You ensure data is extracted completely and
                accurately while maintaining source system performance.
            """),
            verbose=True,
            allow_delegation=False
        )

    def data_transformation_agent(self):
        """
        Agent responsible for data transformation and enrichment
        Handles cleaning, normalization, aggregation, and feature engineering
        """
        return Agent(
            role="Data Transformation Engineer",
            goal="Transform raw data into clean, structured, analysis-ready datasets",
            backstory=dedent("""
                You are a skilled data transformation engineer with deep knowledge of
                data quality, cleansing techniques, and ETL/ELT patterns. You excel at
                data normalization, type conversion, handling missing values, deduplication,
                and feature engineering. You understand SQL, Python pandas, Spark, and
                modern data transformation frameworks. You ensure data integrity and
                consistency throughout the transformation pipeline.
            """),
            verbose=True,
            allow_delegation=False
        )

    def data_quality_agent(self):
        """
        Agent responsible for data quality validation and monitoring
        Ensures data meets quality standards and business rules
        """
        return Agent(
            role="Data Quality Assurance Specialist",
            goal="Validate data quality and ensure compliance with business rules and standards",
            backstory=dedent("""
                You are a meticulous data quality specialist with expertise in data
                profiling, validation, and monitoring. You define and enforce data quality
                rules including completeness, accuracy, consistency, timeliness, and
                validity checks. You understand statistical analysis, anomaly detection,
                and data governance principles. You create comprehensive quality reports
                and alert stakeholders to data issues before they impact downstream systems.
            """),
            verbose=True,
            allow_delegation=False
        )
