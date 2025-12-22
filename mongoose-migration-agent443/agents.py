from crewai import Agent
from tools import (
    schema_analyzer,
    migration_generator,
    data_transformer,
    migration_validator,
    rollback_planner
)

class MongooseMigrationAgents:
    def schema_analyst_agent(self):
        return Agent(
            role='Mongoose Schema Analyst',
            goal='Analyze MongoDB schemas and identify migration requirements',
            backstory="""You are an expert in MongoDB and Mongoose schemas.
            You understand schema design, data modeling, and the intricacies
            of schema migrations. You excel at analyzing schema changes and
            their impact on existing data.""",
            tools=[schema_analyzer, migration_validator],
            verbose=True,
            allow_delegation=False
        )

    def migration_engineer_agent(self):
        return Agent(
            role='Migration Engineer',
            goal='Generate safe and efficient migration scripts',
            backstory="""You are a database migration specialist who creates
            robust migration scripts. You ensure data integrity, handle edge
            cases, and create migrations that are both forward and backward
            compatible when possible.""",
            tools=[migration_generator, rollback_planner],
            verbose=True,
            allow_delegation=True
        )

    def data_transformer_agent(self):
        return Agent(
            role='Data Transformation Specialist',
            goal='Transform and migrate data safely between schema versions',
            backstory="""You are an expert in data transformation and migration.
            You handle complex data restructuring, ensure data integrity, and
            create efficient transformation pipelines for large datasets.""",
            tools=[data_transformer, migration_validator],
            verbose=True,
            allow_delegation=False
        )

    def validation_agent(self):
        return Agent(
            role='Migration Validation Specialist',
            goal='Validate migrations and ensure data integrity',
            backstory="""You are a quality assurance expert specializing in
            database migrations. You create validation strategies, verify data
            integrity, and ensure migrations complete successfully.""",
            tools=[migration_validator, schema_analyzer],
            verbose=True,
            allow_delegation=False
        )
