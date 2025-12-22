# Directory Search Tool - CrewAI Agent System with RAG

A sophisticated multi-agent system powered by CrewAI for intelligent directory search with RAG (Retrieval Augmented Generation) capabilities. This application uses three specialized AI agents working collaboratively to search and analyze file system contents semantically.

## Overview

This project demonstrates the integration of CrewAI's agent framework with RAG-enhanced directory search, providing intelligent search strategy formulation, semantic content search, and curated result presentation.

## Architecture

### Specialized Agents

1. **Directory Analyzer Agent**
   - Analyzes directory structures and search requirements
   - Formulates effective search strategies
   - Optimizes traversal and filtering approaches
   - Configures RAG parameters

2. **RAG Content Searcher Agent**
   - Performs semantic search using RAG
   - Creates embeddings of file contents
   - Executes vector similarity search
   - Ranks results by relevance

3. **Results Curator Agent**
   - Organizes search results by category
   - Creates hierarchical presentations
   - Provides summary statistics
   - Delivers actionable recommendations

## Features

- Multi-agent collaborative workflow using CrewAI
- RAG-enhanced semantic search capabilities
- Sequential task processing with context sharing
- Interactive command-line interface
- Comprehensive error handling
- Environment-based configuration
- Detailed logging and verbose output

## Installation

```bash
# Navigate to the project directory
cd directory-agent308

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

- "Find Python files related to authentication"
- "Search for configuration files containing database settings"
- "Locate documentation about API endpoints"
- "Find test files for the user management module"

## Project Structure

```
directory-agent308/
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
- `chromadb>=0.4.0` - Vector database for RAG

## How It Works

1. **Query Input**: User provides search query
2. **Analysis**: Directory Analyzer creates search strategy
3. **Search**: RAG Content Searcher performs semantic search
4. **Curation**: Results Curator organizes and presents findings
5. **Output**: User receives curated, actionable results

## RAG Capabilities

- Semantic file content search
- Vector embeddings for similarity matching
- Context-aware result ranking
- Relevance scoring
- Content excerpt extraction

## Advanced Features

- Context-aware task dependencies
- Sequential process orchestration
- Verbose output for transparency
- Customizable LLM temperature settings
- ChromaDB integration for vector storage

## License

MIT License - Feel free to use and modify for your projects

## Author

Agent 308 - Directory Search Tool
Part of the CrewAI Tools demonstration series

## Support

For issues, questions, or contributions, please refer to the project documentation.
