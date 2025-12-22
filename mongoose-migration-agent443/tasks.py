from crewai import Task
from textwrap import dedent

class MongooseMigrationTasks:
    def analyze_schema_task(self, agent, old_schema, new_schema):
        return Task(
            description=dedent(f"""
                Analyze the schema changes between old and new versions.

                Old Schema: {old_schema}
                New Schema: {new_schema}

                Steps:
                1. Parse both schema definitions
                2. Identify added, removed, and modified fields
                3. Detect data type changes
                4. Analyze index changes
                5. Assess migration complexity and risks
            """),
            agent=agent,
            expected_output="Detailed schema change analysis with migration requirements"
        )

    def generate_migration_task(self, agent, schema_analysis):
        return Task(
            description=dedent(f"""
                Generate migration scripts based on schema analysis.

                Schema Analysis: {schema_analysis}

                Steps:
                1. Design migration strategy
                2. Generate up migration script
                3. Generate down migration script (rollback)
                4. Add data validation checks
                5. Include error handling and logging
            """),
            agent=agent,
            expected_output="Complete migration scripts with up and down migrations"
        )

    def transform_data_task(self, agent, migration_plan, sample_data):
        return Task(
            description=dedent(f"""
                Transform data according to the migration plan.

                Migration Plan: {migration_plan}
                Sample Data: {sample_data}

                Steps:
                1. Analyze data transformation requirements
                2. Create transformation pipeline
                3. Handle data type conversions
                4. Manage default values for new fields
                5. Test transformation on sample data
            """),
            agent=agent,
            expected_output="Data transformation pipeline with tested results"
        )

    def validate_migration_task(self, agent, migration_scripts, test_data):
        return Task(
            description=dedent(f"""
                Validate the migration scripts and data integrity.

                Migration Scripts: {migration_scripts}
                Test Data: {test_data}

                Steps:
                1. Set up test database environment
                2. Execute migration on test data
                3. Validate data integrity
                4. Test rollback functionality
                5. Generate validation report
            """),
            agent=agent,
            expected_output="Migration validation report with test results"
        )
