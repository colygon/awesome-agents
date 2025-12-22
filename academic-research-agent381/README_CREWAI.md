# Academic Research Assistant - CrewAI Edition

## Migration from Google ADK to CrewAI

This application has been migrated from Google's Agent Development Kit (ADK) to CrewAI, replacing Google Gemini with OpenAI models and implementing a multi-agent workflow using CrewAI's framework.

## Overview

The Academic Research Assistant helps researchers explore the academic landscape surrounding seminal research works. It provides:

1. **Seminal Paper Analysis** - Extracts and analyzes key information from foundational papers
2. **Citation Discovery** - Finds recent academic publications that cite the seminal work
3. **Future Research Directions** - Proposes promising avenues for novel investigation

## Architecture

### ADK vs CrewAI Comparison

| Component | Google ADK (Original) | CrewAI (Migrated) |
|-----------|----------------------|-------------------|
| **Framework** | Google ADK | CrewAI |
| **LLM** | Gemini 2.5 Pro | OpenAI GPT-4o-mini |
| **Main Agent** | academic_coordinator | Crew with 3 agents |
| **Sub-Agents** | academic_websearch, academic_newresearch | citation_researcher, future_research_synthesizer |
| **Search Tool** | google_search (built-in) | Custom WebSearchTool, CitationFinderTool |
| **PDF Processing** | Vertex AI | PyPDFLoader + LangChain |
| **Deployment** | Vertex AI Agent Engine | Standalone Python application |

### CrewAI Agents

1. **Document Analyzer Agent** (`document_analyzer`)
   - Replaces: ADK's main paper analysis logic
   - Role: Extracts metadata, abstract, innovations, and references from PDFs
   - Tools: PDFAnalysisTool

2. **Citation Researcher Agent** (`citation_researcher`)
   - Replaces: ADK's `academic_websearch_agent`
   - Role: Discovers recent papers citing the seminal work
   - Tools: WebSearchTool, CitationFinderTool
   - Target: 10+ papers per year (2024, 2025)

3. **Future Research Synthesizer Agent** (`future_research_synthesizer`)
   - Replaces: ADK's `academic_newresearch_agent`
   - Role: Proposes 10+ novel research directions
   - Criteria: Novelty, utility, unexpectedness, emerging popularity

### Custom Tools

1. **PDFAnalysisTool**
   - Loads PDF files using PyPDFLoader
   - Extracts structured information via LLM analysis
   - Returns: title, authors, abstract, summary, innovations, references

2. **WebSearchTool**
   - Integrates with Serper API (or other search services)
   - Searches academic databases (Scholar, arXiv, IEEE, ACM)
   - Fallback: Provides manual search guidance

3. **CitationFinderTool**
   - Specialized tool for finding citing papers
   - Filters by publication year
   - Returns: title, authors, year, source, link

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for automated searches

### Installation

1. **Clone or download this directory**

```bash
cd academic-research-agent381
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

Optional (for automated searches):
```
SERPER_API_KEY=...
```

## Usage

### Command Line

```bash
python main.py path/to/seminal_paper.pdf
```

### Interactive Mode

```bash
python main.py
```

Then enter the path to your PDF when prompted.

### Example Interaction

```
Welcome! I am an AI Research Assistant.

My purpose is to help you explore the academic landscape related to a seminal paper.

I can:
  • Analyze a seminal paper you provide
  • Find recent academic papers that cite the seminal work
  • Suggest potential future research directions

Please provide the path to the seminal paper PDF: attention_is_all_you_need.pdf

Analyzing seminal paper: attention_is_all_you_need.pdf

Starting academic research workflow...

[Agent execution logs...]

RESEARCH COMPLETE
================================================================================

Seminal Paper: Attention Is All You Need
Authors: Vaswani et al., 2017
...
[Full analysis with citations and future directions]
```

## Key Migration Changes

### 1. Agent Architecture

**Before (ADK):**
```python
academic_coordinator = LlmAgent(
    model="gemini-2.5-pro",
    tools=[
        AgentTool(agent=academic_websearch_agent),
        AgentTool(agent=academic_newresearch_agent),
    ]
)
```

**After (CrewAI):**
```python
crew = Crew(
    agents=[document_analyzer, citation_researcher, future_research_synthesizer],
    tasks=[analyze_task, find_citations_task, propose_research_task],
    process=Process.sequential
)
```

### 2. Tool Implementation

**Before (ADK):**
```python
from google.adk.tools import google_search

academic_websearch_agent = Agent(
    tools=[google_search]
)
```

**After (CrewAI):**
```python
class WebSearchTool(BaseTool):
    def _run(self, query: str) -> str:
        # Custom implementation using Serper API
        # or other search services
```

### 3. LLM Integration

**Before (ADK):**
- Used Google's Gemini 2.5 Pro
- Vertex AI integration
- Required Google Cloud setup

**After (CrewAI):**
- Uses OpenAI GPT-4o-mini
- LangChain integration
- Standard OpenAI API key

### 4. PDF Processing

**Before (ADK):**
- Used Vertex AI's document processing
- Integrated with Google Cloud Storage

**After (CrewAI):**
- Uses PyPDFLoader from LangChain
- Local file processing
- LLM-based extraction

## Features Preserved

All core functionality from the ADK version has been preserved:

- ✓ PDF analysis with structured extraction
- ✓ Author and affiliation extraction
- ✓ Abstract and summary generation
- ✓ Key innovations identification
- ✓ Reference list extraction
- ✓ Recent citation discovery (10+ per year)
- ✓ Future research direction proposals (10+ areas)
- ✓ Diversity criteria (utility, unexpectedness, popularity)

## Benefits of CrewAI Migration

1. **Platform Independence** - No Google Cloud dependency
2. **Flexibility** - Easy to swap LLM providers
3. **Transparency** - Clear agent roles and task definitions
4. **Extensibility** - Simple to add new agents or tools
5. **Cost Control** - Pay-per-use OpenAI pricing vs Vertex AI
6. **Local Development** - No cloud deployment required for testing

## Limitations and Notes

1. **Search API Required** - For automated searches, you need Serper API or similar
2. **PDF Quality** - Extraction quality depends on PDF structure
3. **Rate Limits** - Subject to OpenAI API rate limits
4. **No Google Scholar API** - Google Scholar doesn't offer an official API

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
document_analyzer = Agent(
    tools=[PDFAnalysisTool(), MyCustomTool()]
)
```

### Changing LLM Models

Edit `tools.py`:
```python
llm = ChatOpenAI(model="gpt-4", temperature=0)  # Use GPT-4 instead
```

Or agents directly:
```python
from langchain_openai import ChatOpenAI

document_analyzer = Agent(
    llm=ChatOpenAI(model="gpt-4"),
    ...
)
```

### Adding New Agents

1. Define agent in `agents.py`
2. Create task in `tasks.py`
3. Add to crew in `main.py`

## Troubleshooting

### "No module named 'crewai'"
```bash
pip install crewai>=0.86.0
```

### "OPENAI_API_KEY not found"
```bash
# Create .env file with your API key
echo "OPENAI_API_KEY=sk-..." > .env
```

### "PDF parsing errors"
- Ensure PDF is text-based (not scanned image)
- Try OCR preprocessing if needed
- Check PDF file permissions

### "Search results empty"
- Add SERPER_API_KEY for automated searches
- Use manual search guidance provided
- Check internet connectivity

## Future Enhancements

Potential improvements for this CrewAI version:

1. **Enhanced Search** - Integrate with Semantic Scholar API, arXiv API
2. **RAG Integration** - Add vector database for paper storage
3. **Batch Processing** - Analyze multiple papers simultaneously
4. **Export Options** - Generate reports in PDF, LaTeX, or Markdown
5. **Citation Graphs** - Visualize citation networks
6. **Collaboration** - Share research findings with team

## License

This CrewAI migration is based on the original Google ADK sample, which is licensed under Apache 2.0.

## Acknowledgments

- Original ADK implementation: Google LLC
- CrewAI framework: CrewAI team
- Migration: Claude Code

---

**Migration Date:** December 2025
**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
