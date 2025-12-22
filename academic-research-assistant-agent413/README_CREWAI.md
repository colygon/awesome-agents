# Academic Research Assistant - CrewAI Edition

## Overview

The Academic Research Assistant is a comprehensive AI-powered system that helps researchers with literature search, paper analysis, citation management, literature review synthesis, and research question development. It streamlines the research process from initial literature search to research proposal development.

## Features

1. **Literature Search** - Finds relevant papers across academic databases
2. **Paper Summarization** - Analyzes and summarizes research papers
3. **Citation Management** - Generates citations in multiple formats (APA, MLA, Chicago, IEEE)
4. **Literature Review** - Synthesizes multiple papers into cohesive review
5. **Research Questions** - Develops focused research questions from literature gaps

## Architecture

### CrewAI Agents

1. **Literature Searcher** (`literature_searcher`)
   - Searches academic databases
   - Finds relevant, high-quality papers
   - Tools: LiteratureSearchTool

2. **Paper Summarizer** (`paper_summarizer`)
   - Analyzes paper methodology and findings
   - Creates structured summaries
   - Tools: PaperSummarizerTool

3. **Citation Manager** (`citation_manager`)
   - Formats citations in multiple styles
   - Creates bibliographies
   - Tools: CitationManagerTool

4. **Literature Synthesizer** (`literature_synthesizer`)
   - Identifies themes across papers
   - Creates comprehensive reviews
   - No specific tools (uses LLM reasoning)

5. **Research Question Developer** (`research_question_developer`)
   - Identifies research gaps
   - Develops focused questions
   - No specific tools (uses LLM reasoning)

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for automated searches

### Installation

```bash
cd academic-research-assistant-agent413
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API keys
```

## Usage

```bash
python main.py
```

Enter your research topic when prompted.

## Output

The system provides:

1. **Literature List** (15+ papers)
   - Bibliographic information
   - Citation counts
   - Relevance notes

2. **Paper Summaries** (top 10)
   - Research question
   - Methodology
   - Key findings
   - Limitations

3. **Citations**
   - Multiple formats (APA, MLA, Chicago, IEEE)
   - BibTeX entries
   - In-text examples

4. **Literature Review** (2000-3000 words)
   - Thematic organization
   - Critical analysis
   - Research gaps

5. **Research Questions** (5-7)
   - Gap analysis
   - Methodology suggestions
   - Feasibility assessments

## Citation Styles Supported

- APA 7th edition
- MLA 9th edition
- Chicago 17th edition
- IEEE style
- BibTeX format

## Use Cases

- Graduate students starting thesis research
- Researchers exploring new topics
- Systematic literature reviews
- Grant proposal development
- Course assignments requiring literature reviews

## License

Provided for academic research purposes.

---

**Created:** December 2025
**Version:** 1.0.0
