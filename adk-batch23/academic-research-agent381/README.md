# Academic Research Agent - CrewAI Implementation

Converted from Google ADK Academic Research Agent to CrewAI multi-agent system with OpenAI.

## Overview

An automated academic research system powered by CrewAI with four specialized agents working together to produce comprehensive research papers.

### Agents

1. **Academic Literature Researcher**
   - Role: Conduct comprehensive literature reviews
   - Capabilities: Identify key papers, track research trends, evaluate sources
   - Tools: Web search for finding academic papers and sources
   - Output: Structured literature review with citations

2. **Research Data Analyst**
   - Role: Analyze and synthesize research findings
   - Capabilities: Pattern identification, comparative analysis, methodological evaluation
   - Tools: File reading for analyzing data
   - Output: Detailed analysis and synthesis of findings

3. **Academic Paper Writer**
   - Role: Write scholarly research papers
   - Capabilities: IMRAD structure, academic tone, logical argumentation
   - Tools: Web search for additional context
   - Output: Complete research paper draft

4. **Academic Citation Specialist**
   - Role: Manage citations and bibliographies
   - Capabilities: Citation formatting (APA, MLA, Chicago), verification, consistency
   - Tools: None (focuses on citation management)
   - Output: Final paper with properly formatted bibliography

## Features

- **Multi-agent collaboration**: Four specialized agents work sequentially
- **Comprehensive literature review**: Automated source discovery and synthesis
- **IMRAD structure**: Introduction, Methods, Results, And Discussion
- **Citation management**: Support for APA, MLA, and Chicago styles
- **Web search integration**: Access to current academic sources
- **Markdown output**: Clean, formatted research papers

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Configuration

Required API keys:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Command Line

```bash
python main.py
```

Follow the prompts to:
1. Enter your research topic or question
2. Select citation style (APA/MLA/Chicago)
3. Review the generated research paper
4. Save to file

### Python API

```python
from main import conduct_research, save_research_output

# Conduct research
result = conduct_research(
    research_topic="The Impact of AI on Higher Education",
    citation_style="APA"
)

# Access different outputs
print(result["literature_review"])
print(result["analysis"])
print(result["final_paper"])

# Save to file
save_research_output(result["final_paper"], "research-paper.md")
```

## Workflow

1. **Literature Review Phase**: Researcher identifies and reviews key papers
2. **Analysis Phase**: Analyst synthesizes findings and identifies patterns
3. **Writing Phase**: Writer creates comprehensive research paper
4. **Citation Phase**: Citation specialist formats bibliography and verifies citations

## Research Paper Structure

The generated papers follow academic IMRAD format:

1. **Introduction**
   - Background and context
   - Research question
   - Significance of study

2. **Literature Review**
   - Synthesis of existing research
   - Identification of gaps
   - Theoretical framework

3. **Methodology** (if applicable)
   - Research approach
   - Data collection methods
   - Analysis techniques

4. **Results/Discussion**
   - Findings and analysis
   - Interpretation
   - Implications

5. **Conclusion**
   - Summary of findings
   - Contributions to field
   - Future research directions

6. **References**
   - Properly formatted bibliography

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| Literature review agent | Academic Literature Researcher |
| Data analysis agent | Research Data Analyst |
| Writing agent | Academic Paper Writer |
| Citation agent | Academic Citation Specialist |
| Gemini model | OpenAI GPT-4 |
| Google Search tool | SerperDevTool |

### Architecture Differences

- **ADK**: Uses multi-agent orchestration with validation
- **CrewAI**: Sequential process with task context passing
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Tools**: Migrated from ADK tools to CrewAI tools

## Citation Styles Supported

- **APA**: American Psychological Association (default)
- **MLA**: Modern Language Association
- **Chicago**: Chicago Manual of Style

## Example Topics

- "The Impact of Large Language Models on Academic Research"
- "Machine Learning Applications in Healthcare"
- "Blockchain Technology in Supply Chain Management"
- "Climate Change Mitigation Strategies"
- "The Future of Quantum Computing"

## Output Example

The system produces:
- Comprehensive literature review (10-15 key sources)
- Detailed analysis and synthesis
- 3000-5000 word research paper
- Properly formatted bibliography
- Academic tone and scholarly language

## Limitations

- Relies on web search for sources (may not access paywalled journals)
- Citations are generated based on available information
- Does not replace human peer review and validation
- Best used as a research assistant, not a replacement for original research

## Original ADK Agent

Based on: Google Agent Development Kit (ADK) Academic Research sample

## License

Apache License 2.0
