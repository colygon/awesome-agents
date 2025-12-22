# Plumber Data Engineering Agent - CrewAI Implementation

A comprehensive data engineering system powered by CrewAI that designs, implements, and optimizes data pipelines from extraction to loading with quality checks and documentation.

## Overview

This CrewAI implementation provides end-to-end data pipeline development using specialized agents for architecture design, ETL implementation, data quality assurance, performance optimization, and documentation.

## Agents

1. **Data Architecture Specialist**: Designs scalable data pipeline architectures
2. **ETL/ELT Engineer**: Implements data extraction, transformation, and loading processes
3. **Data Quality Specialist**: Ensures data quality, validation, and integrity
4. **Pipeline Optimization Expert**: Optimizes performance and resource utilization
5. **Data Engineering Lead**: Coordinates projects and creates comprehensive documentation

## Features

- End-to-end pipeline design and architecture
- ETL/ELT process implementation
- Data quality validation and monitoring
- Performance optimization recommendations
- Comprehensive documentation generation
- Support for batch and streaming pipelines
- Multi-source data integration
- Incremental and full load strategies
- Error handling and retry logic
- Data lineage tracking

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials and API keys
```

3. Required configurations:
- OpenAI API key (or Google Gemini)
- Source database credentials
- Target warehouse credentials
- Optional: Cloud storage, monitoring tools

## Usage

### Build a New Data Pipeline

```bash
python main.py new 'MySQL Database' 'Snowflake' 'Daily customer data sync' 'Python/dbt'
```

### Optimize Existing Pipeline

```bash
python main.py optimize 'customer_data_pipeline'
```

### Programmatic Usage

```python
from main import build_data_pipeline

result = build_data_pipeline(
    source_systems="PostgreSQL + Salesforce API",
    target_system="BigQuery",
    requirements="Hourly sales data sync with transformations",
    technology="Python/dbt"
)
```

## Pipeline Components

### 1. Data Architecture Design
- Overall pipeline architecture
- Data flow diagrams
- Technology stack selection
- Component breakdown
- Orchestration strategy

### 2. ETL/ELT Implementation
- **Extraction**: Connect to sources, pull data efficiently
- **Transformation**: Clean, standardize, apply business logic
- **Loading**: Load to target with upsert/append strategies
- **Error Handling**: Comprehensive error catching and logging

### 3. Data Quality Assurance
- **Completeness**: Required fields validation
- **Accuracy**: Type and format validation
- **Consistency**: Cross-field validation, referential integrity
- **Timeliness**: Freshness checks, SLA compliance
- **Validity**: Domain value checks, pattern matching

### 4. Performance Optimization
- Query optimization
- Parallel processing
- Caching strategies
- Partitioning recommendations
- Resource utilization optimization

### 5. Documentation
- Architecture overview
- Data flow documentation
- Technical setup guide
- Operations manual
- Troubleshooting guide
- Data dictionary

## Technology Stack Support

### Extraction
- Databases: PostgreSQL, MySQL, SQL Server, Oracle
- APIs: REST, GraphQL, SOAP
- Files: CSV, JSON, Parquet, Avro
- Streaming: Kafka, Kinesis, Pub/Sub

### Transformation
- Python (pandas, PySpark)
- SQL
- dbt (data build tool)
- Apache Spark
- Apache Beam

### Loading
- Data Warehouses: Snowflake, BigQuery, Redshift
- Databases: PostgreSQL, MySQL
- Data Lakes: S3, GCS, Azure Data Lake

### Orchestration
- Apache Airflow
- Prefect
- Dagster
- AWS Step Functions

## Pipeline Patterns

### Batch Processing
```
Source → Extract (Daily) → Transform → Validate → Load → Archive
```

### Incremental Loading
```
Source → Extract (Changed Records) → Merge → Validate → Upsert
```

### Streaming
```
Source → Stream → Transform → Validate → Real-time Load
```

### ELT Pattern
```
Source → Extract → Load (Raw) → Transform (in DW) → Validate
```

## Example Use Cases

### Customer Data Pipeline
```bash
python main.py new \
  'MySQL CRM' \
  'Snowflake' \
  'Daily customer data with order history, handle deletions' \
  'Python/dbt'
```

### Real-time Analytics
```bash
python main.py new \
  'Kafka Streams' \
  'BigQuery' \
  'Real-time event processing with aggregations' \
  'Apache Beam'
```

### Data Lake Ingestion
```bash
python main.py new \
  'Multiple APIs' \
  'S3 Data Lake' \
  'Hourly API data collection in Parquet format' \
  'Python/Spark'
```

## Output Deliverables

### 1. Pipeline Design Document
- Architecture diagrams
- Component specifications
- Technology choices
- Data flow design

### 2. ETL Code
- Extraction scripts
- Transformation logic
- Loading procedures
- Error handling

### 3. Data Quality Framework
- Validation rules
- Quality checks
- Monitoring setup
- Alert configuration

### 4. Optimization Plan
- Performance improvements
- Resource optimization
- Cost reduction strategies
- Scaling recommendations

### 5. Complete Documentation
- Setup instructions
- Operations guide
- Data dictionary
- Troubleshooting guide

## Best Practices

### Design Principles
1. **Idempotency**: Pipelines should be rerunnable
2. **Incremental Processing**: Load only changed data when possible
3. **Data Quality First**: Validate before loading
4. **Comprehensive Logging**: Log all steps and errors
5. **Graceful Degradation**: Handle failures without data loss

### Implementation
1. Use staging tables for intermediate data
2. Implement comprehensive error handling
3. Add data quality checks at every stage
4. Version control all pipeline code
5. Document data transformations
6. Implement monitoring and alerting

### Operations
1. Schedule during low-traffic periods
2. Monitor performance metrics
3. Set up alerting for failures
4. Maintain audit logs
5. Regular optimization reviews
6. Document all changes

## Monitoring and Alerting

### Key Metrics
- Execution time
- Records processed
- Success/failure rate
- Data quality score
- Resource utilization

### Alerts
- Pipeline failures
- Data quality issues
- SLA violations
- Resource constraints
- Anomalies in data volume

## Advanced Features

### Data Lineage
Track data from source to destination:
```python
lineage = {
    'source': 'MySQL customers table',
    'transformations': ['cleaning', 'enrichment'],
    'target': 'Snowflake dim_customers'
}
```

### Schema Evolution
Handle schema changes gracefully:
```python
# Detect schema changes
# Apply transformations
# Update target schema
```

### Data Versioning
Version control for data:
```python
# Snapshot data at each stage
# Enable rollback capability
```

## Customization

Modify these files:
- `agents.py`: Adjust agent capabilities and expertise
- `tasks.py`: Modify pipeline development workflow
- `tools.py`: Add custom tools or database connectors
- `main.py`: Change orchestration logic

## Troubleshooting

### Common Issues

**Connection Failures**
- Check database credentials
- Verify network connectivity
- Check firewall rules

**Performance Issues**
- Add indexes on join columns
- Implement partitioning
- Use parallel processing

**Data Quality Failures**
- Review validation rules
- Check source data quality
- Implement data cleaning

## Integration Examples

### Airflow DAG
```python
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG('customer_pipeline', schedule_interval='@daily')

extract = PythonOperator(task_id='extract', python_callable=extract_data)
transform = PythonOperator(task_id='transform', python_callable=transform_data)
load = PythonOperator(task_id='load', python_callable=load_data)

extract >> transform >> load
```

### dbt Integration
```sql
-- models/staging/stg_customers.sql
SELECT
    customer_id,
    LOWER(TRIM(email)) as email,
    created_at
FROM {{ source('mysql', 'customers') }}
WHERE created_at > (SELECT MAX(created_at) FROM {{ this }})
```

## Notes

- Pipeline code saved to files for deployment
- Supports multiple database types and sources
- Scalable architecture patterns
- Production-ready code with error handling
- Comprehensive logging and monitoring
- Best used with actual database connections
- Documentation includes runbooks
- Optimization recommendations are actionable
