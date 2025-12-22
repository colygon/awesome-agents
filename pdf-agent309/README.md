# PDF Search Tool - CrewAI Agent System with RAG

A sophisticated multi-agent system powered by CrewAI for intelligent PDF search with RAG (Retrieval Augmented Generation) capabilities. This application uses three specialized AI agents working collaboratively to search and extract insights from PDF documents semantically.

## Overview

This project demonstrates the integration of CrewAI's agent framework with RAG-enhanced PDF search, providing intelligent content extraction, semantic search, and comprehensive document analysis.

## Architecture

### Specialized Agents

1. **PDF Analyzer Agent**
   - Analyzes PDF structure and search requirements
   - Formulates extraction strategies
   - Configures RAG parameters
   - Plans chunking and embedding approach

2. **RAG Content Extractor Agent**
   - Extracts text from PDFs (including OCR)
   - Creates semantic embeddings
   - Performs vector similarity search
   - Ranks results by relevance

3. **Insights Synthesizer Agent**
   - Organizes search results across documents
   - Creates comprehensive summaries
   - Identifies themes and patterns
   - Provides actionable insights

## Features

- Multi-agent collaborative workflow using CrewAI
- RAG-enhanced semantic PDF search
- Support for text-based and scanned PDFs (OCR)
- Sequential task processing with context sharing
- Interactive command-line interface
- Comprehensive error handling
- Environment-based configuration
- Detailed logging and verbose output

## Installation

```bash
# Navigate to the project directory
cd pdf-agent309

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your OpenAI API key
```

## Configuration

Edit the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the interactive application:

```bash
python main.py
```

### Example Queries

- "Find information about machine learning algorithms"
- "Search for references to climate change data"
- "Locate sections discussing financial regulations"
- "Extract key findings from research papers"

## Project Structure

```
pdf-agent309/
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
- `pypdf>=3.0.0` - PDF processing
- `chromadb>=0.4.0` - Vector database for RAG

## How It Works

1. **Query Input**: User provides search query
2. **Analysis**: PDF Analyzer creates extraction strategy
3. **Extraction**: Content Extractor performs RAG-based search
4. **Synthesis**: Insights Synthesizer creates comprehensive report
5. **Output**: User receives curated, actionable insights

## RAG Capabilities

- Semantic content search beyond keywords
- Vector embeddings for similarity matching
- Context-aware passage retrieval
- Relevance scoring and ranking
- Cross-document analysis

## Advanced Features

- Context-aware task dependencies
- Sequential process orchestration
- Verbose output for transparency
- Customizable LLM temperature settings
- ChromaDB integration for vector storage
- Support for both text-layer and OCR extraction

## License

MIT License - Feel free to use and modify for your projects

## Author

Agent 309 - PDF Search Tool
Part of the CrewAI Tools demonstration series

## Support

For issues, questions, or contributions, please refer to the project documentation.
