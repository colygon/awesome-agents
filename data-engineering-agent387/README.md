# Data Engineering Pipeline - CrewAI Implementation

**Agent ID:** 387
**Category:** Data Engineering
**Framework:** CrewAI
**Migration:** Google ADK → CrewAI

## Overview

A comprehensive data engineering pipeline system built with CrewAI framework, featuring three specialized agents that handle data ingestion, transformation, and quality validation. Migrated from Google ADK to demonstrate modern multi-agent orchestration for data pipeline operations.

## Architecture

### Agents

1. **Data Ingestion Specialist**
   - Extracts data from various sources (databases, APIs, files, streams)
   - Handles connection management and retry logic
   - Performs initial schema validation
   - Manages incremental loading patterns

2. **Data Transformation Engineer**
   - Cleans and normalizes raw data
   - Applies business logic and transformations
   - Creates derived features and aggregations
   - Optimizes data for storage and querying

3. **Data Quality Assurance Specialist**
   - Validates data completeness, accuracy, and consistency
   - Performs statistical profiling and anomaly detection
   - Enforces business rules and constraints
   - Generates comprehensive quality reports

### Workflow

```
Data Source → Ingestion → Transformation → Quality Validation → Production-Ready Data
```

The agents work sequentially, with each agent building upon the previous agent's output.

## Features

- **Multi-Source Ingestion**: Support for databases, APIs, files (CSV, JSON, Parquet), and streaming data
- **Comprehensive Transformation**: Cleaning, normalization, enrichment, and feature engineering
- **Quality Assurance**: 6-dimensional quality validation (completeness, accuracy, consistency, timeliness, validity, statistical)
- **Data Lineage**: Full tracking of transformations and data flow
- **Error Handling**: Robust retry logic and error reporting
- **Scalable Design**: Optimized for large datasets with partitioning and indexing

## Installation

```bash
# Clone or download this directory
cd data-engineering-agent387

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Configuration

Edit the `.env` file:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
```

## Usage

### Basic Usage

```bash
python main.py
```

This runs the example pipeline with sample configuration.

### Custom Pipeline

```python
from main import run_data_engineering_pipeline

result = run_data_engineering_pipeline(
    data_source="s3://your-bucket/data/",
    data_format="Parquet",
    transformation_requirements="""
        1. Remove duplicates
        2. Handle missing values
        3. Normalize timestamps
        4. Calculate metrics
    """,
    quality_rules="""
        1. Completeness: All required fields > 95%
        2. Accuracy: Values within expected ranges
        3. Uniqueness: No duplicate keys
    """
)
```

### Example Output

```
================================================================================
DATA ENGINEERING PIPELINE - CREWAI
================================================================================

Data Source: s3://data-lake/customer-transactions/2025-12-21/
Data Format: Parquet

Starting pipeline execution...

[Data Ingestion Specialist] Connecting to data source...
[Data Ingestion Specialist] Extracted 1,234,567 records
[Data Ingestion Specialist] Schema validated: 15 columns

[Data Transformation Engineer] Applying transformations...
[Data Transformation Engineer] Removed 1,234 duplicates
[Data Transformation Engineer] Created 5 derived features
[Data Transformation Engineer] Output: 1,233,333 records

[Data Quality Assurance Specialist] Running quality checks...
[Data Quality Assurance Specialist] Quality score: 98.5%
[Data Quality Assurance Specialist] Status: PASSED

================================================================================
PIPELINE EXECUTION COMPLETE
================================================================================
```

## Use Cases

1. **ETL/ELT Pipelines**: Build robust data pipelines for analytics
2. **Data Lake Ingestion**: Load data from multiple sources into data lakes
3. **Data Quality Monitoring**: Continuous validation of data quality
4. **Data Migration**: Migrate data between systems with validation
5. **Feature Engineering**: Prepare data for machine learning workflows
6. **Data Warehouse Loading**: Load and transform data for warehouses

## ADK to CrewAI Migration

This application was migrated from Google Agent Development Kit (ADK) to CrewAI framework:

### Key Changes

1. **Agent Definition**: ADK agents → CrewAI Agent class with role/goal/backstory
2. **Task Structure**: ADK tasks → CrewAI Task with description/expected_output
3. **Orchestration**: ADK workflow → CrewAI Crew with Process.sequential
4. **LLM Backend**: Google Gemini → OpenAI GPT-4 via LangChain

### Migration Benefits

- More structured agent definitions with explicit roles and goals
- Better task output specifications
- Improved orchestration with sequential/hierarchical processes
- Ecosystem compatibility with LangChain tools
- Active community and regular updates

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    Data Engineering Pipeline                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  Data Sources    │
                    │  - Databases     │
                    │  - APIs          │
                    │  - Files         │
                    │  - Streams       │
                    └──────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │   Data Ingestion Specialist Agent   │
           │   - Connection Management           │
           │   - Extraction & Loading            │
           │   - Schema Validation               │
           └─────────────────────────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │  Data Transformation Engineer Agent │
           │  - Cleaning & Normalization         │
           │  - Business Logic Application       │
           │  - Feature Engineering              │
           └─────────────────────────────────────┘
                              │
                              ▼
           ┌─────────────────────────────────────┐
           │ Data Quality Assurance Specialist   │
           │  - Completeness Checks              │
           │  - Accuracy Validation              │
           │  - Statistical Analysis             │
           └─────────────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Production Data  │
                    │  - Validated     │
                    │  - Transformed   │
                    │  - Quality Score │
                    └──────────────────┘
```

## Requirements

- Python 3.10+
- OpenAI API key
- CrewAI >= 0.86.0
- LangChain OpenAI >= 0.3.0

## License

MIT License - See source repository for details

## Credits

Migrated from Google ADK samples to CrewAI framework
Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
