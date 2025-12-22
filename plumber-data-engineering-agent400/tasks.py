from crewai import Task
from textwrap import dedent

class DataEngineeringTasks:
    def design_data_pipeline(self, agent, source_systems, target_system, requirements):
        return Task(
            description=dedent(f"""\
                Design a comprehensive data pipeline architecture:

                Source Systems: {source_systems}
                Target System: {target_system}
                Requirements: {requirements}

                Design should include:
                1. Pipeline Architecture
                   - Overall architecture diagram
                   - Data flow design
                   - Technology stack recommendations
                   - Component breakdown

                2. Data Sources
                   - Source system connections
                   - Data extraction methods
                   - Incremental vs. full load strategy
                   - Authentication and security

                3. Transformation Logic
                   - Required transformations
                   - Business rules
                   - Data cleansing steps
                   - Aggregation logic

                4. Target Schema
                   - Destination data model
                   - Table structures
                   - Indexing strategy
                   - Partitioning approach

                5. Orchestration
                   - Scheduling strategy
                   - Dependency management
                   - Error handling approach
                   - Monitoring and alerting

                Provide a detailed pipeline design document."""),
            agent=agent,
            expected_output="Comprehensive pipeline design with architecture, data flow, and technical specifications"
        )

    def implement_etl_process(self, agent, pipeline_design, technology):
        return Task(
            description=dedent(f"""\
                Implement the ETL/ELT process based on the pipeline design:

                Pipeline Design: {pipeline_design}
                Technology: {technology}

                Implement:
                1. Data Extraction
                   - Connect to source systems
                   - Extract data efficiently
                   - Handle pagination and limits
                   - Implement retry logic
                   - Log extraction metrics

                2. Data Transformation
                   - Clean and standardize data
                   - Apply business rules
                   - Handle data type conversions
                   - Perform joins and aggregations
                   - Handle null values and defaults

                3. Data Loading
                   - Load to target system
                   - Implement upsert logic
                   - Handle duplicates
                   - Maintain audit trails
                   - Implement rollback capability

                4. Error Handling
                   - Catch and log errors
                   - Implement data quality checks
                   - Dead letter queue for failed records
                   - Alert on critical failures

                Generate complete, production-ready ETL code."""),
            agent=agent,
            expected_output="Production-ready ETL code with extraction, transformation, loading, and error handling"
        )

    def validate_data_quality(self, agent, dataset, quality_rules):
        return Task(
            description=dedent(f"""\
                Implement comprehensive data quality validation:

                Dataset: {dataset}
                Quality Rules: {quality_rules}

                Implement checks for:
                1. Completeness
                   - Required fields present
                   - No unexpected nulls
                   - Record count validation
                   - Coverage metrics

                2. Accuracy
                   - Data type validation
                   - Format validation
                   - Range checks
                   - Business rule validation

                3. Consistency
                   - Cross-field validation
                   - Referential integrity
                   - Duplicate detection
                   - Temporal consistency

                4. Timeliness
                   - Data freshness checks
                   - SLA compliance
                   - Lag metrics

                5. Validity
                   - Domain value checks
                   - Pattern matching
                   - Checksum validation

                Generate a data quality report with pass/fail status and metrics."""),
            agent=agent,
            expected_output="Data quality report with validation results, metrics, and identified issues"
        )

    def optimize_pipeline_performance(self, agent, pipeline_metrics, bottlenecks):
        return Task(
            description=dedent(f"""\
                Optimize data pipeline for better performance:

                Current Metrics: {pipeline_metrics}
                Identified Bottlenecks: {bottlenecks}

                Optimization areas:
                1. Query Optimization
                   - Analyze slow queries
                   - Add appropriate indexes
                   - Rewrite inefficient queries
                   - Use query hints if needed

                2. Parallelization
                   - Identify parallel opportunities
                   - Implement parallel processing
                   - Balance load across workers
                   - Optimize thread/process count

                3. Resource Optimization
                   - Memory usage optimization
                   - CPU utilization improvements
                   - Network transfer reduction
                   - Storage optimization

                4. Caching Strategy
                   - Identify cacheable data
                   - Implement caching layers
                   - Set appropriate TTLs
                   - Cache invalidation strategy

                5. Partitioning
                   - Partition large tables
                   - Optimize partition keys
                   - Implement partition pruning

                Provide specific optimization recommendations and implementation code."""),
            agent=agent,
            expected_output="Pipeline optimization plan with specific improvements and implementation code"
        )

    def create_pipeline_documentation(self, agent, pipeline_design, etl_code, quality_checks):
        return Task(
            description=dedent(f"""\
                Create comprehensive data pipeline documentation:

                Pipeline Design: {pipeline_design}
                ETL Implementation: {etl_code}
                Quality Checks: {quality_checks}

                Documentation should include:
                1. Overview
                   - Purpose and business value
                   - High-level architecture
                   - Key components
                   - Technology stack

                2. Data Flow Documentation
                   - Source systems and connections
                   - Transformation logic
                   - Target systems
                   - Data lineage

                3. Technical Documentation
                   - Setup and configuration
                   - Dependencies
                   - Environment variables
                   - Deployment process

                4. Operations Guide
                   - How to run the pipeline
                   - Scheduling details
                   - Monitoring and alerts
                   - Troubleshooting guide
                   - Common issues and solutions

                5. Data Dictionary
                   - Source field descriptions
                   - Target field descriptions
                   - Transformation mapping
                   - Business definitions

                6. Maintenance Guide
                   - How to modify pipeline
                   - Testing procedures
                   - Rollback procedures
                   - Version control practices

                7. Performance Metrics
                   - SLAs and targets
                   - Current performance
                   - Optimization opportunities

                Create professional, comprehensive documentation."""),
            agent=agent,
            expected_output="Complete pipeline documentation with all sections properly formatted and detailed"
        )
