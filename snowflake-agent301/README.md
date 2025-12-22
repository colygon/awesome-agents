# Snowflake Search Tool - CrewAI Agent System

A sophisticated multi-agent system powered by CrewAI for querying and analyzing Snowflake data warehouse. This application uses three specialized AI agents working collaboratively to transform user queries into actionable business intelligence.

## Overview

This project demonstrates the integration of CrewAI's agent framework with Snowflake data warehouse operations, providing intelligent query design, advanced analytics, and comprehensive business intelligence reporting capabilities.

## Architecture

### Specialized Agents

1. **Warehouse Analyst Agent**
   - Designs optimal Snowflake SQL queries
   - Leverages virtual warehouses and clustering
   - Utilizes time travel and zero-copy cloning
   - Optimizes for performance and cost

2. **Analytics Specialist Agent**
   - Performs advanced data analytics
   - Identifies patterns, trends, and anomalies
   - Leverages Snowflake's analytical functions
   - Provides statistical insights

3. **Insights Communicator Agent**
   - Creates business intelligence reports
   - Generates visualization recommendations
   - Provides executive summaries
   - Delivers actionable recommendations

## Features

- Multi-agent collaborative workflow using CrewAI
- Optimized for Snowflake data warehouse
- Sequential task processing with context sharing
- Interactive command-line interface
- Comprehensive error handling
- Environment-based configuration
- Detailed logging and verbose output

## Installation

```bash
# Navigate to the project directory
cd snowflake-agent301

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
```

## Configuration

Edit the `.env` file with your credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=your_warehouse_name
SNOWFLAKE_DATABASE=your_database_name
SNOWFLAKE_SCHEMA=your_schema_name
```

## Usage

Run the interactive application:

```bash
python main.py
```

### Example Queries

- "Analyze customer retention trends over the past year"
- "Show revenue by product category with year-over-year comparison"
- "Identify top performing sales regions and growth patterns"
- "Find seasonal patterns in website traffic data"

## Project Structure

```
snowflake-agent301/
├── agents.py              # Agent definitions
├── tasks.py               # Task specifications
├── main.py                # Main application
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── COMPLETION_REPORT.md   # Detailed completion report
└── CREWAI_UPGRADE.md      # CrewAI integration documentation
```

## Dependencies

- `crewai>=0.86.0` - Multi-agent framework
- `langchain-openai>=0.3.0` - LLM integration
- `python-dotenv>=1.0.0` - Environment management
- `openai>=1.0.0` - OpenAI API client
- `snowflake-connector-python>=3.0.0` - Snowflake connector

## How It Works

1. **Query Input**: User provides a data query or question
2. **Query Design**: Warehouse Analyst creates optimized Snowflake query
3. **Analytics**: Analytics Specialist extracts insights and patterns
4. **Communication**: Insights Communicator creates BI report
5. **Output**: User receives comprehensive business intelligence

## Advanced Features

- Context-aware task dependencies
- Sequential process orchestration
- Verbose output for transparency
- Customizable LLM temperature settings
- Snowflake-specific optimizations
- Virtual warehouse recommendations
- Time travel and cloning strategies

## License

MIT License - Feel free to use and modify for your projects

## Author

Agent 301 - Snowflake Search Tool
Part of the CrewAI Tools demonstration series

## Support

For issues, questions, or contributions, please refer to the project documentation or contact the development team.
