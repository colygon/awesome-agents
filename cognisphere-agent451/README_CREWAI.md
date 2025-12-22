# Cognisphere - CrewAI Edition

## Overview

Cognisphere is a knowledge exploration and cognitive analysis system that helps users discover, map, and understand complex knowledge domains. It provides comprehensive analysis of topics, constructs knowledge graphs, analyzes concepts, and generates actionable insights.

## Features

1. **Knowledge Domain Mapping** - Discovers and maps the structure of knowledge domains
2. **Concept Analysis** - Performs deep analysis of key concepts and their relationships
3. **Insight Generation** - Generates actionable insights and strategic recommendations
4. **Semantic Search** - Retrieves relevant information based on meaning and context
5. **Knowledge Graphs** - Constructs visual representations of concept relationships

## Architecture

### CrewAI Agents

1. **Knowledge Explorer Agent** (`knowledge_explorer`)
   - Role: Discovers and maps knowledge domains
   - Tools: KnowledgeGraphTool, SemanticSearchTool
   - Identifies concepts, relationships, and structures

2. **Concept Analyzer Agent** (`concept_analyzer`)
   - Role: Analyzes concepts deeply and synthesizes insights
   - Tools: ConceptAnalysisTool, SemanticSearchTool
   - Breaks down complex ideas and identifies relationships

3. **Insight Generator Agent** (`insight_generator`)
   - Role: Generates actionable insights and recommendations
   - Synthesizes knowledge into practical applications
   - Identifies opportunities and future directions

### Custom Tools

1. **KnowledgeGraphTool**
   - Constructs knowledge graphs for topics
   - Identifies concepts and relationships
   - Organizes knowledge into structured networks

2. **SemanticSearchTool**
   - Performs semantic search for knowledge
   - Retrieves contextually relevant information
   - Integrates with Serper API when available

3. **ConceptAnalysisTool**
   - Performs deep analysis of individual concepts
   - Examines definition, relationships, and evolution
   - Identifies debates and open questions

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for enhanced searches

### Installation

1. **Navigate to directory**

```bash
cd cognisphere-agent451
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
cp .env.example .env
# Edit .env and add your API keys
```

Required:
```
OPENAI_API_KEY=sk-...
```

Optional:
```
SERPER_API_KEY=...
```

## Usage

### Command Line

```bash
python main.py "quantum computing"
```

### Interactive Mode

```bash
python main.py
```

Then enter your topic and select analysis depth when prompted.

### Example Interactions

```
Welcome to Cognisphere!

I help you explore knowledge domains through comprehensive analysis.

I can:
  • Map knowledge domains and their structures
  • Analyze concepts and their relationships
  • Generate actionable insights and recommendations

What topic or knowledge domain would you like to explore? artificial intelligence ethics

Analysis depth options:
  1. overview - High-level exploration
  2. detailed - In-depth analysis
  3. comprehensive - Exhaustive investigation (default)

Select depth (1-3, default=3): 3

Exploring topic: artificial intelligence ethics
Analysis depth: comprehensive

Starting knowledge exploration workflow...

[Agent execution logs...]

ANALYSIS COMPLETE
================================================================================

KNOWLEDGE DOMAIN MAP:
- Core concepts: Bias, Fairness, Transparency, Accountability, Privacy...
[Full analysis with knowledge graph, concept analysis, and insights]
```

## Use Cases

1. **Academic Research** - Explore research domains and identify gaps
2. **Strategic Planning** - Understand emerging trends and opportunities
3. **Learning & Education** - Map learning pathways in new subjects
4. **Innovation** - Discover novel connections and applications
5. **Knowledge Management** - Organize and structure organizational knowledge

## Analysis Depth Levels

- **Overview** - High-level exploration with 5-10 key concepts
- **Detailed** - In-depth analysis with comprehensive concept coverage
- **Comprehensive** - Exhaustive investigation with deep synthesis

## Output Structure

The system produces three main outputs:

1. **Knowledge Domain Map**
   - Core concepts and definitions
   - Relationship network
   - Historical development
   - Key contributors and works
   - Related domains

2. **Conceptual Analysis**
   - Deep dive into major concepts
   - Relationships and tensions
   - Meta-insights and patterns
   - Gaps and opportunities

3. **Actionable Insights**
   - Immediate applications
   - Innovation opportunities
   - Future trends
   - Learning pathways
   - Strategic recommendations

## Customization

### Adding New Tools

```python
from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "My Tool"
    description: str = "Tool description"

    def _run(self, **kwargs) -> str:
        # Implementation
        pass

# Add to agent
knowledge_explorer = Agent(
    tools=[KnowledgeGraphTool(), MyCustomTool()]
)
```

### Changing Analysis Parameters

Edit `tasks.py` to modify:
- Number of concepts to analyze
- Depth of analysis
- Output format
- Insight categories

### Using Different LLM Models

Edit `tools.py`:
```python
llm = ChatOpenAI(model="gpt-4", temperature=0.3)  # Use GPT-4
```

## Troubleshooting

### "No module named 'crewai'"
```bash
pip install crewai>=0.86.0
```

### "OPENAI_API_KEY not found"
```bash
echo "OPENAI_API_KEY=sk-..." > .env
```

### "Rate limit exceeded"
- Reduce analysis depth
- Add delays between API calls
- Upgrade OpenAI plan

## Future Enhancements

Potential improvements:

1. **Vector Database Integration** - Store and retrieve knowledge persistently
2. **Visual Knowledge Graphs** - Generate interactive graph visualizations
3. **Multi-Language Support** - Analyze knowledge in different languages
4. **Export Formats** - Export to mind maps, PDFs, or structured databases
5. **Collaborative Features** - Share and build knowledge collectively
6. **Domain-Specific Models** - Fine-tuned models for specific fields

## License

This CrewAI implementation is provided as-is under Apache 2.0 license.

## Acknowledgments

- CrewAI framework: CrewAI team
- Implementation: Claude Code

---

**Version:** 1.0.0
**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
