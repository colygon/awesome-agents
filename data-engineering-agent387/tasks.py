"""
Data Engineering Tasks
CrewAI task definitions for data pipeline operations
"""

from crewai import Task
from textwrap import dedent


class DataEngineeringTasks:
    """Task definitions for data engineering pipeline"""

    def ingest_data_task(self, agent, data_source, data_format):
        """
        Task for ingesting data from specified source

        Args:
            agent: Data ingestion specialist agent
            data_source: Source identifier (database, API, file path, etc.)
            data_format: Data format (CSV, JSON, Parquet, etc.)
        """
        return Task(
            description=dedent(f"""
                Ingest data from the following source:

                Source: {data_source}
                Format: {data_format}

                Your responsibilities:
                1. Establish connection to the data source
                2. Verify source availability and accessibility
                3. Extract data while handling:
                   - Connection timeouts and retries
                   - Rate limiting (for APIs)
                   - Incremental loading patterns
                   - Large file/dataset handling
                4. Perform initial data validation:
                   - Schema validation
                   - Record count verification
                   - Data type checking
                5. Store raw data in staging area
                6. Generate ingestion metadata:
                   - Timestamp
                   - Record count
                   - File size
                   - Source version/snapshot

                Provide a comprehensive ingestion report including:
                - Data source details
                - Records extracted
                - Any issues encountered
                - Data schema overview
            """),
            expected_output=dedent("""
                A detailed ingestion report containing:
                - Source connection status
                - Number of records ingested
                - Data schema (column names and types)
                - File size or data volume
                - Ingestion timestamp
                - Any warnings or errors
                - Staging location of raw data
            """),
            agent=agent
        )

    def transform_data_task(self, agent, transformation_requirements):
        """
        Task for transforming and cleaning data

        Args:
            agent: Data transformation engineer agent
            transformation_requirements: Specific transformation rules
        """
        return Task(
            description=dedent(f"""
                Transform the ingested data according to these requirements:

                {transformation_requirements}

                Your responsibilities:
                1. Data Cleansing:
                   - Remove duplicates
                   - Handle missing values (imputation or removal)
                   - Fix data type inconsistencies
                   - Standardize formats (dates, phone numbers, etc.)

                2. Data Transformation:
                   - Apply business logic rules
                   - Normalize/denormalize as needed
                   - Create derived columns and features
                   - Perform aggregations if required
                   - Join with reference/dimension tables

                3. Data Enrichment:
                   - Add calculated fields
                   - Create timestamps and metadata columns
                   - Apply categorization or classification

                4. Performance Optimization:
                   - Partition data appropriately
                   - Optimize data types for storage
                   - Create indexes where beneficial

                5. Documentation:
                   - Document all transformations applied
                   - Track data lineage
                   - Note any assumptions made

                Provide a comprehensive transformation report.
            """),
            expected_output=dedent("""
                A detailed transformation report containing:
                - List of all transformations applied
                - Before/after record counts
                - Data quality improvements made
                - New columns/features created
                - Performance metrics (processing time)
                - Data lineage documentation
                - Location of transformed data
                - Sample of transformed records
            """),
            agent=agent
        )

    def validate_quality_task(self, agent, quality_rules):
        """
        Task for validating data quality

        Args:
            agent: Data quality assurance specialist agent
            quality_rules: Quality validation rules and thresholds
        """
        return Task(
            description=dedent(f"""
                Validate data quality according to these rules:

                {quality_rules}

                Your responsibilities:
                1. Completeness Checks:
                   - Verify all required fields are present
                   - Check for null/missing value percentages
                   - Validate record counts against expectations

                2. Accuracy Checks:
                   - Validate data ranges and constraints
                   - Check referential integrity
                   - Verify calculations and aggregations
                   - Compare with source data samples

                3. Consistency Checks:
                   - Cross-field validation
                   - Format consistency
                   - Business rule compliance
                   - Historical trend analysis

                4. Timeliness Checks:
                   - Verify data freshness
                   - Check processing SLA compliance
                   - Validate temporal ordering

                5. Validity Checks:
                   - Schema conformance
                   - Data type validation
                   - Domain value validation
                   - Pattern matching (regex)

                6. Statistical Analysis:
                   - Outlier detection
                   - Distribution analysis
                   - Anomaly detection
                   - Data profiling statistics

                7. Quality Reporting:
                   - Calculate quality scores
                   - Flag critical issues
                   - Provide remediation recommendations

                Generate a comprehensive data quality report.
            """),
            expected_output=dedent("""
                A comprehensive data quality report containing:
                - Overall quality score (0-100)
                - Completeness metrics
                - Accuracy validation results
                - Consistency check results
                - Timeliness assessment
                - Validity check results
                - Statistical profiling summary
                - List of quality issues found (with severity)
                - Failed quality rules (if any)
                - Recommendations for data quality improvement
                - Pass/Fail status for deployment
                - Detailed quality metrics table
            """),
            agent=agent
        )
