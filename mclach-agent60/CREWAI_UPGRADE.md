# McLachApp CrewAI Upgrade Documentation

## Overview

This document describes the CrewAI upgrade for McLachApp, transforming it into an intelligent sports analytics platform powered by multi-agent AI systems.

## Upgrade Summary

**Version:** 2.0.0-crewai
**Date:** December 2025
**Agent:** Agent 60

### Key Changes

1. **Multi-Agent Architecture**: Implemented three specialized AI agents for comprehensive sports analytics
2. **Intelligent Workflows**: CrewAI-powered orchestration for complex analysis tasks
3. **Flexible Integration**: Easy-to-use API for various sports analytics use cases
4. **Enhanced Analytics**: Advanced player, team, and match analysis capabilities

## Architecture

### Three Core Agents

#### 1. Data Analyst Agent
**Role:** Sports Data Analyst
**Specialization:** Statistical analysis and data processing

**Capabilities:**
- Analyze raw sports data
- Identify statistical patterns and trends
- Process player and team performance metrics
- Data cleaning and validation
- Generate comprehensive statistical reports

**Configuration:**
- Temperature: 0.7
- Max Iterations: 5
- Delegation: Disabled (focused on data analysis)

#### 2. Performance Evaluator Agent
**Role:** Performance Evaluator
**Specialization:** Player and team assessment

**Capabilities:**
- Evaluate player performance across multiple metrics
- Compare players and teams
- Identify strengths and weaknesses
- Create detailed performance reports
- Provide fair and comprehensive evaluations

**Configuration:**
- Temperature: 0.7
- Max Iterations: 5
- Delegation: Enabled (can work with other agents)

#### 3. Strategy Advisor Agent
**Role:** Sports Strategy Advisor
**Specialization:** Tactical recommendations

**Capabilities:**
- Develop game strategies based on data
- Identify tactical advantages
- Recommend lineup changes
- Predict opponent strategies
- Provide context-aware strategic advice

**Configuration:**
- Temperature: 0.7
- Max Iterations: 5
- Delegation: Enabled (can coordinate with other agents)

## Project Structure

```
mclach-agent60/
├── agents.py              # Agent definitions and configurations
├── tasks.py               # Task definitions for various analyses
├── crew.py                # Crew orchestration and workflows
├── main.py                # Main application entry point
├── config.py              # Configuration management
├── utils.py               # Helper utilities
├── requirements.txt       # Python dependencies
├── .env.example           # Example environment variables
├── .gitignore            # Git ignore rules
└── CREWAI_UPGRADE.md     # This documentation
```

## Features

### 1. Player Analysis Workflow
Complete analysis of individual player performance using all three agents in sequence:

```python
from crew import run_player_analysis

player_data = {
    "name": "John Doe",
    "position": "Forward",
    "games_played": 38,
    "goals": 25,
    "assists": 12,
    # ... more metrics
}

result = run_player_analysis(player_data)
```

**Workflow:**
1. Data Analyst analyzes raw statistics
2. Performance Evaluator provides comprehensive evaluation
3. Strategy Advisor recommends development and deployment strategies

### 2. Team Analysis Workflow
Comprehensive team performance analysis:

```python
from crew import run_team_analysis

team_data = {
    "team_name": "Athletic FC",
    "season": "2024-25",
    "games_played": 38,
    "wins": 22,
    # ... more metrics
}

result = run_team_analysis(team_data)
```

**Workflow:**
1. Statistical analysis of team metrics
2. Performance evaluation and rating
3. Strategic recommendations for improvement

### 3. Player Comparison Workflow
Side-by-side player comparison:

```python
from crew import run_player_comparison

result = run_player_comparison(player1_data, player2_data)
```

### 4. Match Analysis Workflow
Detailed post-match analysis:

```python
from crew import SportsAnalyticsCrew

crew_manager = SportsAnalyticsCrew()
crew = crew_manager.match_analysis_crew(match_data)
result = crew.kickoff()
```

## Installation

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Setup Instructions

1. **Clone the repository:**
```bash
cd /Users/colinlowenberg/crew
git clone <repository-url> mclach-agent60
cd mclach-agent60
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

5. **Run the application:**
```bash
python main.py
```

## Dependencies

### Core Dependencies
- **crewai>=0.86.0**: Multi-agent orchestration framework
- **langchain-openai>=0.3.0**: OpenAI integration for LangChain
- **langchain>=0.1.0**: LLM application framework
- **openai>=1.0.0**: OpenAI API client

### Supporting Libraries
- **pandas>=2.0.0**: Data manipulation
- **numpy>=1.24.0**: Numerical computing
- **python-dotenv>=1.0.0**: Environment variable management
- **pydantic>=2.0.0**: Data validation

### Optional Dependencies
- **scipy>=1.11.0**: Scientific computing
- **scikit-learn>=1.3.0**: Machine learning utilities
- **matplotlib>=3.7.0**: Data visualization
- **seaborn>=0.12.0**: Statistical visualization

## Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| OPENAI_API_KEY | OpenAI API key | - | Yes |
| OPENAI_MODEL | Model to use | gpt-4 | No |
| OPENAI_TEMPERATURE | Model temperature | 0.7 | No |
| CREWAI_VERBOSE | Enable verbose logging | True | No |
| MAX_ITERATIONS | Max agent iterations | 5 | No |
| DEBUG | Enable debug mode | False | No |

### Configuration Management

The `config.py` module provides centralized configuration:

```python
from config import Config

# Check if configuration is valid
if Config.validate():
    # Get LLM configuration
    llm_config = Config.get_llm_config()

    # Print current configuration
    Config.print_config()
```

## Usage Examples

### Example 1: Quick Player Analysis
```python
from crew import run_player_analysis

player_data = {
    "name": "Jane Smith",
    "position": "Midfielder",
    "games_played": 30,
    "goals": 8,
    "assists": 15,
    "pass_completion": 87.5
}

result = run_player_analysis(player_data)
print(result)
```

### Example 2: Custom Crew Configuration
```python
from crew import SportsAnalyticsCrew
from langchain_openai import ChatOpenAI

# Custom LLM configuration
llm = ChatOpenAI(model="gpt-4", temperature=0.5)

# Create crew manager
crew_manager = SportsAnalyticsCrew(llm=llm)

# Get specific agents
agents = crew_manager.agents_factory.get_all_agents()
data_analyst = agents["data_analyst"]

# Create custom workflow
# ... (your custom tasks and crew setup)
```

### Example 3: Interactive Application
```python
# Run the interactive application
python main.py
```

The application provides a menu-driven interface for:
- Player analysis
- Team analysis
- Player comparison
- Custom workflows

## Advanced Features

### Custom Task Creation

Create custom tasks for specific analysis needs:

```python
from crewai import Task
from tasks import SportsAnalyticsTasks

task = Task(
    description="Analyze the impact of weather on player performance",
    agent=data_analyst,
    expected_output="Weather impact analysis report"
)
```

### Agent Collaboration

Agents can delegate tasks and collaborate:

```python
# Performance Evaluator can delegate to Data Analyst
# Strategy Advisor can coordinate with both agents
# Create complex workflows with agent collaboration
```

### Process Types

CrewAI supports different process types:
- **Sequential**: Tasks execute in order (default)
- **Hierarchical**: Manager agent delegates tasks
- **Custom**: Define your own execution flow

## Best Practices

### 1. Data Preparation
- Validate input data before analysis
- Use consistent data formats
- Include relevant context in data dictionaries

### 2. Agent Configuration
- Adjust temperature based on task type
- Set appropriate max iterations
- Enable delegation for complex workflows

### 3. Error Handling
- Always wrap crew execution in try-except blocks
- Validate API key before running
- Check configuration validity

### 4. Performance Optimization
- Cache frequently used analysis results
- Use appropriate model size for task complexity
- Batch similar analyses when possible

## Troubleshooting

### Common Issues

**Issue 1: API Key Error**
```
Error: OPENAI_API_KEY environment variable not set
```
**Solution:** Set your OpenAI API key in the .env file

**Issue 2: Import Errors**
```
ModuleNotFoundError: No module named 'crewai'
```
**Solution:** Install dependencies: `pip install -r requirements.txt`

**Issue 3: Timeout Errors**
**Solution:** Increase MAX_ITERATIONS in .env or reduce task complexity

### Debug Mode

Enable debug mode for detailed logging:
```bash
export DEBUG=True
export CREWAI_VERBOSE=True
```

## Performance Considerations

### Model Selection
- **GPT-4**: Best for complex analysis, slower, more expensive
- **GPT-3.5-turbo**: Faster, cheaper, good for simpler tasks

### Cost Optimization
- Use appropriate temperature settings
- Limit max iterations for cost control
- Cache results when possible
- Batch similar requests

### Scaling
- Implement async processing for multiple analyses
- Use Redis/database for result caching
- Consider API rate limits

## Future Enhancements

### Planned Features
1. **Data Integration**: Direct integration with sports data APIs
2. **Real-time Analysis**: Live game analysis capabilities
3. **Advanced Visualizations**: Interactive charts and dashboards
4. **Machine Learning Models**: Predictive analytics integration
5. **Multi-sport Support**: Expand beyond current sport focus
6. **API Service**: REST API for remote access
7. **Web Interface**: Browser-based UI for analysis

### Extension Points
- Custom agent types for specialized analysis
- Additional task templates for common workflows
- Plugin system for third-party integrations
- Export formats for different platforms

## Contributing

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Install pre-commit hooks (if available)
pre-commit install

# Run tests
pytest

# Format code
black .

# Type checking
mypy .
```

### Code Standards
- Follow PEP 8 style guidelines
- Add type hints to all functions
- Write comprehensive docstrings
- Include unit tests for new features

## License

[Add your license information here]

## Support

For issues, questions, or contributions:
- Create an issue in the repository
- Contact: [Your contact information]
- Documentation: [Link to additional docs]

## Changelog

### Version 2.0.0-crewai (December 2025)
- Initial CrewAI upgrade by Agent 60
- Implemented three core agents: Data Analyst, Performance Evaluator, Strategy Advisor
- Added multi-agent workflows for player, team, and match analysis
- Created comprehensive configuration system
- Added utility functions for data processing
- Included example application with interactive menu
- Full documentation and setup instructions

### Version 1.0.0 (Previous)
- Original McLachApp implementation
- [Previous features listed here]

## Acknowledgments

- **CrewAI**: Multi-agent orchestration framework
- **LangChain**: LLM application framework
- **OpenAI**: Language model provider
- **Agent 60**: CrewAI upgrade implementation

---

**McLachApp v2.0.0-crewai** - Sports Analytics Powered by AI Agents
