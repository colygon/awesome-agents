# Deep Search ADK - CrewAI Implementation

A multi-agent deep research system built with CrewAI that conducts comprehensive research on any topic using specialized AI agents.

## Overview

This CrewAI implementation transforms the Deep Search ADK into a collaborative multi-agent system with three specialized agents:

1. **Query Analyst** - Optimizes search queries and develops research strategies
2. **Deep Researcher** - Conducts comprehensive multi-source research
3. **Synthesis Specialist** - Synthesizes findings into actionable insights

## Features

- **Intelligent Query Analysis** - Breaks down complex questions into searchable components
- **Multi-Source Research** - Gathers information from diverse authoritative sources
- **Evidence-Based Synthesis** - Transforms raw findings into comprehensive reports
- **Source Evaluation** - Assesses credibility and authority of information sources
- **Sequential Workflow** - Agents work in coordinated sequence for optimal results

## Installation

1. Clone or navigate to this directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Command Line

Run the interactive CLI:
```bash
python main.py
```

You'll be prompted to either:
- Use a sample query (quantum computing & cybersecurity)
- Enter your own research query

### Programmatic Usage

```python
from main import run_deep_search

# Run deep search on any topic
result = run_deep_search(
    query="What are the latest trends in artificial intelligence?",
    verbose=True
)

# Access the research report
print(result['result'])

# Save to file
from main import save_results
save_results(result, "my_research_report.md")
```

## Agent Roles

### Query Analyst
- Analyzes user intent and information needs
- Breaks down complex queries into searchable components
- Develops comprehensive search strategies
- Identifies key concepts and related terms

### Deep Researcher
- Conducts multi-source research following the strategy
- Evaluates source credibility and authority
- Gathers diverse perspectives and evidence
- Documents findings with proper attribution

### Synthesis Specialist
- Synthesizes research into coherent insights
- Identifies patterns and connections
- Generates actionable recommendations
- Produces professional research reports

## Workflow

```
User Query
    ↓
Query Analyst → Optimized Search Strategy
    ↓
Deep Researcher → Comprehensive Research Findings
    ↓
Synthesis Specialist → Final Research Report
    ↓
Output (Markdown Report)
```

## Example Queries

- "What are the security implications of quantum computing?"
- "How is AI being used in healthcare diagnosis?"
- "What are the latest developments in renewable energy storage?"
- "Analyze the impact of remote work on productivity and culture"
- "What are the ethical considerations in autonomous vehicles?"

## Output Format

The system generates comprehensive markdown reports including:

- **Executive Summary** - Direct answer and key findings
- **Overview** - Current landscape and context
- **Detailed Analysis** - In-depth examination by theme
- **Key Insights** - Patterns and implications
- **Practical Implications** - Real-world applications
- **Recommendations** - Actionable next steps
- **Sources** - Bibliography and methodology notes

## Configuration

### Agent Settings

Agents are configured in `agents.py` with:
- Role-specific expertise and backstory
- Memory enabled for context retention
- Verbose mode for detailed output

### Task Settings

Tasks are defined in `tasks.py` with:
- Detailed instructions for each phase
- Expected output formats
- Context dependencies

### Tools

Custom tools in `tools.py` provide:
- Query optimization capabilities
- Source credibility checking
- Research gap identification
- Information synthesis

## Best Practices

1. **Clear Queries** - Provide specific, well-defined research questions
2. **Scope Definition** - Indicate desired depth and breadth of research
3. **Time Constraints** - Complex queries may take several minutes
4. **API Limits** - Monitor OpenAI API usage for cost management
5. **Source Verification** - Always verify critical information from original sources

## Limitations

- Dependent on OpenAI API availability and rate limits
- Research quality depends on query clarity and specificity
- Cannot access paywalled or restricted content
- Information is based on AI training data and may need verification
- Real-time search integration requires additional API keys

## Advanced Configuration

### Adding Search APIs

Enhance research capabilities by adding search API keys to `.env`:

```bash
SERPER_API_KEY=your_key_here      # Google search
TAVILY_API_KEY=your_key_here      # AI-powered search
SERPAPI_API_KEY=your_key_here     # Search engine results
```

### Customizing Agents

Modify agent configurations in `agents.py`:
- Adjust expertise and backstory
- Enable/disable delegation
- Configure memory settings

### Customizing Tasks

Modify task prompts in `tasks.py`:
- Adjust research depth
- Change output formats
- Add specific requirements

## Troubleshooting

**Error: OPENAI_API_KEY not found**
- Ensure `.env` file exists and contains your API key
- Check that you've copied `.env.example` to `.env`

**Slow Performance**
- Complex queries naturally take longer
- Check OpenAI API status
- Consider breaking very broad queries into smaller parts

**Incomplete Research**
- Provide more specific queries
- Ensure query includes clear scope and objectives
- Check API rate limits aren't being exceeded

## Support

For issues, questions, or contributions:
- Review agent and task configurations
- Check CrewAI documentation: https://docs.crewai.com
- Verify API key validity and quota

## License

This implementation follows the original Deep Search ADK licensing terms.
