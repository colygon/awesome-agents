# SingleStore Search Tool - CrewAI Agent System

A sophisticated multi-agent system powered by CrewAI for querying and analyzing SingleStore distributed SQL databases. This application uses three specialized AI agents working collaboratively to transform user queries into actionable database insights.

## Overview

This project demonstrates the integration of CrewAI's agent framework with SingleStore database operations, providing intelligent query formulation, data analysis, and comprehensive reporting capabilities.

## Architecture

### Specialized Agents

1. **Database Analyst Agent**
   - Formulates optimized SingleStore SQL queries
   - Understands distributed database architecture
   - Leverages columnstore and rowstore capabilities
   - Optimizes for performance and efficiency

2. **Data Interpreter Agent**
   - Analyzes query results and extracts insights
   - Identifies patterns, trends, and anomalies
   - Provides business-relevant interpretations
   - Considers distributed data characteristics

3. **Results Synthesizer Agent**
   - Creates comprehensive, actionable reports
   - Generates visualization recommendations
   - Provides executive summaries and technical details
   - Translates technical findings for all stakeholders

## Features

- Multi-agent collaborative workflow using CrewAI
- Optimized for SingleStore distributed SQL database
- Sequential task processing with context sharing
- Interactive command-line interface
- Comprehensive error handling
- Environment-based configuration
- Detailed logging and verbose output

## Installation

```bash
# Clone or navigate to the project directory
cd singlestore-agent300

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - Add your OpenAI API key
# - Configure SingleStore connection details
```

## Configuration

Edit the `.env` file with your credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
SINGLESTORE_HOST=your_singlestore_host
SINGLESTORE_PORT=3306
SINGLESTORE_USER=your_username
SINGLESTORE_PASSWORD=your_password
SINGLESTORE_DATABASE=your_database
```

## Usage

Run the interactive application:

```bash
python main.py
```

### Example Queries

- "Show me sales trends by region for the last quarter"
- "Analyze customer churn patterns in the subscription database"
- "Find the top 10 products by revenue and their performance metrics"
- "Identify anomalies in transaction data for the past month"

## Project Structure

```
singlestore-agent300/
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
- `singlestoredb>=1.0.0` - SingleStore database connector

## How It Works

1. **Query Input**: User provides a data query or question
2. **Query Formulation**: Database Analyst creates optimized SQL query
3. **Data Analysis**: Data Interpreter analyzes expected results and insights
4. **Report Synthesis**: Results Synthesizer creates comprehensive report
5. **Output**: User receives detailed findings with actionable recommendations

## Advanced Features

- Context-aware task dependencies
- Sequential process orchestration
- Verbose output for transparency
- Customizable LLM temperature settings
- Specialized agent backstories for domain expertise

## License

MIT License - Feel free to use and modify for your projects

## Author

Agent 300 - SingleStore Search Tool
Part of the CrewAI Tools demonstration series

## Support

For issues, questions, or contributions, please refer to the project documentation or contact the development team.
