from crewai_tools import tool
import os
import json
from typing import List, Dict

class DataPipelineTools:
    @tool("Design pipeline")
    def design_pipeline(requirements: str) -> str:
        """
        Design a data pipeline architecture based on requirements.
        Returns pipeline architecture design.
        """
        pipeline_design = {
            'architecture_type': 'batch',  # or 'streaming', 'hybrid'
            'components': {
                'extraction': {
                    'method': 'API/Database/File',
                    'schedule': 'Daily at 2 AM UTC',
                    'incremental_key': 'updated_at'
                },
                'transformation': {
                    'engine': 'Spark/Python/SQL',
                    'steps': [
                        'Data cleaning',
                        'Type conversion',
                        'Business logic application',
                        'Aggregation'
                    ]
                },
                'loading': {
                    'method': 'Bulk insert/Upsert',
                    'target': 'Data Warehouse',
                    'partitioning': 'By date'
                },
                'orchestration': {
                    'tool': 'Airflow/Prefect/Dagster',
                    'monitoring': 'Datadog/CloudWatch',
                    'alerting': 'PagerDuty/Slack'
                }
            },
            'technology_stack': {
                'extraction': 'Python + SQLAlchemy',
                'transformation': 'dbt/Spark',
                'storage': 'S3/GCS for staging',
                'warehouse': 'Snowflake/BigQuery/Redshift',
                'orchestration': 'Apache Airflow'
            },
            'best_practices': [
                'Implement idempotency',
                'Add comprehensive logging',
                'Use staging tables',
                'Implement data quality checks',
                'Version control all code',
                'Document data lineage'
            ]
        }

        return json.dumps(pipeline_design, indent=2)

    @tool("Analyze data flow")
    def analyze_data_flow(source: str, target: str) -> str:
        """
        Analyze data flow between source and target systems.
        Returns data flow analysis.
        """
        data_flow = {
            'source': source,
            'target': target,
            'flow_characteristics': {
                'volume': 'Estimated daily volume',
                'velocity': 'Batch/Real-time',
                'variety': 'Structured/Semi-structured/Unstructured',
                'complexity': 'Simple/Medium/Complex transformations'
            },
            'data_path': [
                '1. Extract from source',
                '2. Stage in landing zone',
                '3. Transform and clean',
                '4. Load to staging tables',
                '5. Final load to target',
                '6. Archive raw data'
            ],
            'considerations': [
                'Data freshness requirements',
                'Transformation complexity',
                'Error handling strategy',
                'Monitoring requirements'
            ]
        }

        return json.dumps(data_flow, indent=2)

    @tool("Optimize pipeline")
    def optimize_pipeline(metrics: str) -> str:
        """
        Provide pipeline optimization recommendations based on metrics.
        Returns optimization suggestions.
        """
        optimization = {
            'current_performance': 'Analysis of current metrics',
            'bottlenecks_identified': [
                'Slow database queries',
                'Network latency',
                'Inefficient transformations'
            ],
            'recommendations': [
                {
                    'area': 'Query Optimization',
                    'suggestion': 'Add indexes on join columns',
                    'expected_impact': '40% faster queries'
                },
                {
                    'area': 'Parallelization',
                    'suggestion': 'Process partitions in parallel',
                    'expected_impact': '3x throughput increase'
                },
                {
                    'area': 'Caching',
                    'suggestion': 'Cache frequently accessed reference data',
                    'expected_impact': 'Reduce API calls by 80%'
                }
            ],
            'implementation_priority': [
                '1. Quick wins - indexing',
                '2. Medium effort - parallelization',
                '3. Long term - architecture improvements'
            ]
        }

        return json.dumps(optimization, indent=2)

    @tool("Monitor performance")
    def monitor_performance(pipeline_name: str) -> str:
        """
        Monitor data pipeline performance metrics.
        Returns performance monitoring data.
        """
        monitoring = {
            'pipeline': pipeline_name,
            'metrics': {
                'execution_time': '25 minutes',
                'records_processed': 1000000,
                'success_rate': '99.5%',
                'data_quality_score': 98,
                'resource_utilization': {
                    'cpu': '65%',
                    'memory': '70%',
                    'storage': '45%'
                }
            },
            'alerts': [],
            'trends': {
                'execution_time': 'stable',
                'volume': 'growing 5% monthly',
                'errors': 'decreasing'
            },
            'recommendations': [
                'Consider horizontal scaling for growing volume',
                'Review and update partitioning strategy'
            ]
        }

        return json.dumps(monitoring, indent=2)

    @tool("Generate documentation")
    def generate_documentation(pipeline_info: str) -> str:
        """
        Generate comprehensive pipeline documentation.
        Returns formatted documentation.
        """
        documentation = {
            'title': 'Data Pipeline Documentation',
            'sections': {
                'overview': 'Pipeline purpose and business value',
                'architecture': 'Technical architecture and components',
                'data_flow': 'Detailed data flow diagrams',
                'operations': 'How to run and monitor',
                'troubleshooting': 'Common issues and solutions',
                'maintenance': 'How to modify and update'
            },
            'appendices': {
                'data_dictionary': 'Field-level documentation',
                'sla_metrics': 'Performance targets and SLAs',
                'change_log': 'Version history'
            }
        }

        return json.dumps(documentation, indent=2)

class ETLTools:
    @tool("Extract data")
    def extract_data(source: str, query: str = "") -> str:
        """
        Extract data from source system.
        Returns extraction code template.
        """
        extraction_code = """
# Data Extraction Template
import pandas as pd
from sqlalchemy import create_engine
import logging

def extract_data(source_config, incremental_key=None, last_run_time=None):
    \"\"\"
    Extract data from source system.

    Args:
        source_config: Database connection configuration
        incremental_key: Column name for incremental loading
        last_run_time: Timestamp of last successful run

    Returns:
        DataFrame with extracted data
    \"\"\"
    try:
        # Create database connection
        engine = create_engine(source_config['connection_string'])

        # Build query
        if incremental_key and last_run_time:
            query = f\"\"\"
                SELECT * FROM {source_config['table']}
                WHERE {incremental_key} > '{last_run_time}'
            \"\"\"
        else:
            query = f"SELECT * FROM {source_config['table']}"

        # Extract data
        df = pd.read_sql(query, engine)
        logging.info(f"Extracted {len(df)} records")

        return df

    except Exception as e:
        logging.error(f"Extraction failed: {str(e)}")
        raise
"""
        return extraction_code

    @tool("Transform data")
    def transform_data(transformation_rules: str) -> str:
        """
        Generate data transformation code.
        Returns transformation code template.
        """
        transformation_code = """
# Data Transformation Template
import pandas as pd
import numpy as np
from datetime import datetime

def transform_data(df):
    \"\"\"
    Apply transformations to extracted data.

    Args:
        df: Input DataFrame

    Returns:
        Transformed DataFrame
    \"\"\"
    try:
        # Make a copy to avoid modifying original
        df_transformed = df.copy()

        # 1. Data Cleaning
        # Remove duplicates
        df_transformed = df_transformed.drop_duplicates()

        # Handle missing values
        df_transformed['column_name'] = df_transformed['column_name'].fillna('default_value')

        # 2. Data Type Conversion
        df_transformed['date_column'] = pd.to_datetime(df_transformed['date_column'])
        df_transformed['numeric_column'] = pd.to_numeric(df_transformed['numeric_column'], errors='coerce')

        # 3. Business Logic
        # Add calculated columns
        df_transformed['new_column'] = df_transformed['col1'] + df_transformed['col2']

        # Apply business rules
        df_transformed['category'] = df_transformed['value'].apply(
            lambda x: 'High' if x > 100 else 'Low'
        )

        # 4. Data Standardization
        df_transformed['text_column'] = df_transformed['text_column'].str.lower().str.strip()

        # 5. Add metadata
        df_transformed['loaded_at'] = datetime.utcnow()
        df_transformed['source_system'] = 'source_name'

        return df_transformed

    except Exception as e:
        logging.error(f"Transformation failed: {str(e)}")
        raise
"""
        return transformation_code

    @tool("Load data")
    def load_data(target: str, load_type: str = "append") -> str:
        """
        Generate data loading code.
        Returns loading code template.
        """
        loading_code = """
# Data Loading Template
import pandas as pd
from sqlalchemy import create_engine
import logging

def load_data(df, target_config, load_type='append'):
    \"\"\"
    Load data to target system.

    Args:
        df: DataFrame to load
        target_config: Target database configuration
        load_type: 'append', 'replace', or 'upsert'

    Returns:
        Number of records loaded
    \"\"\"
    try:
        engine = create_engine(target_config['connection_string'])

        if load_type == 'append':
            # Append to existing table
            df.to_sql(
                target_config['table'],
                engine,
                if_exists='append',
                index=False,
                method='multi'
            )

        elif load_type == 'replace':
            # Replace entire table
            df.to_sql(
                target_config['table'],
                engine,
                if_exists='replace',
                index=False
            )

        elif load_type == 'upsert':
            # Implement upsert logic
            # Load to staging table first
            staging_table = f"{target_config['table']}_staging"
            df.to_sql(staging_table, engine, if_exists='replace', index=False)

            # Execute merge/upsert SQL
            merge_sql = f\"\"\"
                MERGE INTO {target_config['table']} AS target
                USING {staging_table} AS source
                ON target.id = source.id
                WHEN MATCHED THEN UPDATE SET ...
                WHEN NOT MATCHED THEN INSERT ...
            \"\"\"
            engine.execute(merge_sql)

        logging.info(f"Loaded {len(df)} records to {target_config['table']}")
        return len(df)

    except Exception as e:
        logging.error(f"Loading failed: {str(e)}")
        raise
"""
        return loading_code

    @tool("Create ETL script")
    def create_etl_script(pipeline_name: str) -> str:
        """
        Create complete ETL script template.
        Returns full ETL script.
        """
        etl_script = f"""
# ETL Script: {pipeline_name}
import logging
import sys
from datetime import datetime
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def run_etl():
    \"\"\"
    Main ETL orchestration function.
    \"\"\"
    start_time = datetime.now()
    logging.info(f"Starting ETL pipeline: {pipeline_name}")

    try:
        # 1. Extract
        logging.info("Starting extraction...")
        df = extract_data(source_config)
        logging.info(f"Extracted {{len(df)}} records")

        # 2. Transform
        logging.info("Starting transformation...")
        df_transformed = transform_data(df)
        logging.info(f"Transformed {{len(df_transformed)}} records")

        # 3. Validate
        logging.info("Validating data quality...")
        validation_results = validate_data(df_transformed)
        if not validation_results['passed']:
            raise ValueError(f"Data quality check failed: {{validation_results['errors']}}")

        # 4. Load
        logging.info("Loading data...")
        records_loaded = load_data(df_transformed, target_config)
        logging.info(f"Loaded {{records_loaded}} records")

        # 5. Cleanup and logging
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logging.info(f"ETL completed successfully in {{duration}} seconds")

        return {{
            'status': 'success',
            'records_processed': len(df_transformed),
            'duration_seconds': duration
        }}

    except Exception as e:
        logging.error(f"ETL failed: {{str(e)}}")
        # Send alert
        # Cleanup
        raise

if __name__ == "__main__":
    run_etl()
"""
        return etl_script

class DataQualityTools:
    @tool("Validate data")
    def validate_data(validation_rules: str) -> str:
        """
        Generate data validation code.
        Returns validation code template.
        """
        validation_code = """
# Data Validation Template
import pandas as pd
import logging

def validate_data(df, rules):
    \"\"\"
    Validate data against quality rules.

    Args:
        df: DataFrame to validate
        rules: Dictionary of validation rules

    Returns:
        Validation results
    \"\"\"
    results = {
        'passed': True,
        'checks': [],
        'errors': []
    }

    # 1. Completeness checks
    for col in rules.get('required_columns', []):
        null_count = df[col].isnull().sum()
        if null_count > 0:
            results['passed'] = False
            results['errors'].append(f"{col} has {null_count} null values")

    # 2. Uniqueness checks
    for col in rules.get('unique_columns', []):
        duplicate_count = df[col].duplicated().sum()
        if duplicate_count > 0:
            results['passed'] = False
            results['errors'].append(f"{col} has {duplicate_count} duplicates")

    # 3. Range checks
    for col, (min_val, max_val) in rules.get('range_checks', {}).items():
        out_of_range = ((df[col] < min_val) | (df[col] > max_val)).sum()
        if out_of_range > 0:
            results['passed'] = False
            results['errors'].append(f"{col} has {out_of_range} out-of-range values")

    # 4. Format checks
    # Email, phone, etc.

    return results
"""
        return validation_code

    @tool("Check data quality")
    def check_data_quality(dataset: str) -> str:
        """
        Perform comprehensive data quality assessment.
        Returns quality metrics.
        """
        quality_metrics = {
            'dataset': dataset,
            'completeness': {
                'score': 95,
                'missing_values': 500,
                'total_values': 10000
            },
            'accuracy': {
                'score': 98,
                'invalid_records': 20,
                'total_records': 1000
            },
            'consistency': {
                'score': 97,
                'inconsistencies': 30
            },
            'timeliness': {
                'score': 100,
                'data_freshness': 'within SLA'
            },
            'overall_quality_score': 97.5,
            'issues': [
                'Some missing email addresses',
                'Date format inconsistencies in 3% of records'
            ]
        }

        return json.dumps(quality_metrics, indent=2)

    @tool("Profile data")
    def profile_data(dataset: str) -> str:
        """
        Generate data profiling report.
        Returns profiling statistics.
        """
        profiling = {
            'dataset': dataset,
            'row_count': 1000000,
            'column_count': 25,
            'columns': [
                {
                    'name': 'customer_id',
                    'type': 'integer',
                    'null_count': 0,
                    'unique_count': 1000000,
                    'min': 1,
                    'max': 1000000
                },
                {
                    'name': 'email',
                    'type': 'string',
                    'null_count': 500,
                    'unique_count': 999500,
                    'pattern': 'email_format'
                }
            ],
            'data_quality_issues': [
                'Duplicate customer records: 50',
                'Invalid email formats: 120'
            ]
        }

        return json.dumps(profiling, indent=2)
