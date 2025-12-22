# Batch 3 Action Plan - Step-by-Step Guide

**Purpose**: This document provides a concrete, actionable plan to complete the batch 3 CrewAI upgrades.

**Current Status**: Analysis complete, ready for validation and execution

**Estimated Total Time**: 17 hours (0.5h validation + 14.5h upgrades + 2h QA)

---

## Prerequisites Checklist

Before starting, ensure you have:
- [ ] GitHub CLI (`gh`) installed and authenticated
- [ ] Git configured with proper credentials
- [ ] Python 3.8+ with pip
- [ ] Access to colygon GitHub organization
- [ ] OpenAI API key for testing
- [ ] Reviewed reference implementations:
  - [ ] `/Users/colinlowenberg/crew/llm-leaderboard-agent10/` (optional insights)
  - [ ] `/Users/colinlowenberg/crew/knowledge-gpt-agent5/` (RAG replacement)

---

## Phase 0: Repository Validation (30 minutes)

### Step 1: Run Validation Script

```bash
cd /Users/colinlowenberg/crew
chmod +x validate_batch3_repos.sh
./validate_batch3_repos.sh > validation_results.txt
cat validation_results.txt
```

### Step 2: Review Results

Identify which of the 13 pending repositories are accessible:
- [ ] zusegd/umamusume_virgo_cup_dashboard
- [ ] arup-group/social-data
- [ ] mito-ds/mito-for-streamlit-demo
- [ ] data-science-at-swast/handover_poc
- [ ] aydinarda/tge_case-web-page
- [ ] dataprofessor/hugchat
- [ ] koenleemans/paa
- [ ] steamship-packages/langchain-production-starter
- [ ] frog-land/chat2vis
- [ ] thomashacker/weaviate-magic-chat-demo
- [ ] e-johnstonn/docsummarizer
- [ ] singhjaspreetb/summerization-llm
- [ ] intelligenzaartificiale/ia-italia-chatbotv2

### Step 3: Update Tracking

Update `BATCH_3_RESULTS.json` with validation results:
- Change status from "not_attempted" to "validated" or "invalid"
- Add validation_date timestamp
- Update pending_validation count

---

## Phase 1: Optional Insights Apps (2.5 hours)

Process the 5 optional insights apps that validated successfully.

### For Each App:

#### 1. Fork & Clone (5 minutes)

```bash
# Set variables
APP_ID=<id>
REPO_OWNER=<owner>
REPO_NAME=<name>
AGENT_DIR="/Users/colinlowenberg/crew/${REPO_NAME}-agent${APP_ID}"

# Fork repository
gh repo fork ${REPO_OWNER}/${REPO_NAME} --clone=false --fork-name ${REPO_NAME} --org colygon

# Clone to agent directory
git clone https://github.com/colygon/${REPO_NAME}.git ${AGENT_DIR}
cd ${AGENT_DIR}
```

#### 2. Create CrewAI Structure (15 minutes)

```bash
# Create crewai_agents directory
mkdir -p crewai_agents

# Create agents.py
cat > crewai_agents/agents.py << 'EOF'
"""
CrewAI Agents for AI Insights Feature.
This module defines specialized agents for analytics and insights generation.
"""

from crewai import Agent


def create_data_analyst_agent(llm):
    """Create an agent that analyzes data and identifies patterns."""
    return Agent(
        role="Data Analyst",
        goal="Analyze data to identify patterns, trends, and insights",
        backstory="""You are an expert data analyst with years of experience in
        statistical analysis and pattern recognition. You excel at identifying
        meaningful trends in complex datasets and translating technical findings
        into actionable insights.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_insight_generator_agent(llm):
    """Create an agent that generates insights from analysis."""
    return Agent(
        role="Insight Generator",
        goal="Generate actionable insights and recommendations from data analysis",
        backstory="""You are a strategic analyst who excels at synthesizing
        analytical findings into clear, actionable recommendations. You understand
        business context and can provide insights that drive decision-making.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_recommendation_agent(llm):
    """Create an agent that provides specific recommendations."""
    return Agent(
        role="Recommendation Specialist",
        goal="Provide specific, practical recommendations based on insights",
        backstory="""You are a strategic advisor who specializes in translating
        insights into specific action items. You consider feasibility, impact,
        and implementation when making recommendations.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def get_all_agents(llm):
    """Get all agents for the insights system."""
    return {
        'data_analyst': create_data_analyst_agent(llm),
        'insight_generator': create_insight_generator_agent(llm),
        'recommendation_agent': create_recommendation_agent(llm)
    }
EOF

# Create tasks.py
cat > crewai_agents/tasks.py << 'EOF'
"""
CrewAI Tasks for AI Insights Feature.
This module defines the tasks that agents will perform.
"""

from crewai import Task


def create_analysis_task(agent, data_context):
    """Create a task for data analysis."""
    return Task(
        description=f"""Analyze the following data and identify key patterns and trends:

        {data_context}

        Focus on:
        - Notable patterns and trends
        - Outliers and anomalies
        - Correlations and relationships
        - Statistical significance

        Provide a structured analysis with specific examples.""",
        agent=agent,
        expected_output="Structured analysis with patterns, trends, and insights"
    )


def create_insight_task(agent, analysis_context):
    """Create a task for insight generation."""
    return Task(
        description=f"""Based on the following analysis, generate actionable insights:

        {analysis_context}

        Your insights should:
        - Be specific and actionable
        - Include supporting evidence
        - Consider practical implications
        - Prioritize by importance

        Provide 3-5 key insights.""",
        agent=agent,
        expected_output="3-5 actionable insights with supporting evidence"
    )


def create_recommendation_task(agent, insights_context):
    """Create a task for generating recommendations."""
    return Task(
        description=f"""Based on these insights, provide specific recommendations:

        {insights_context}

        Your recommendations should:
        - Be specific and actionable
        - Include implementation steps
        - Consider constraints and feasibility
        - Prioritize by impact

        Provide 3-5 recommendations.""",
        agent=agent,
        expected_output="3-5 specific recommendations with implementation guidance"
    )
EOF
```

#### 3. Update Requirements (2 minutes)

```bash
# Add CrewAI dependencies
if ! grep -q "crewai" requirements.txt 2>/dev/null; then
  echo "" >> requirements.txt
  echo "# CrewAI dependencies" >> requirements.txt
  echo "crewai>=0.86.0" >> requirements.txt
  echo "langchain-openai>=0.3.0" >> requirements.txt
fi
```

#### 4. Create Documentation (5 minutes)

```bash
# Create .env.example
cat > .env.example << 'EOF'
# OpenAI API Key for CrewAI agents
OPENAI_API_KEY=your_openai_api_key_here
EOF

# Create CREWAI_UPGRADE.md
cat > CREWAI_UPGRADE.md << 'EOF'
# CrewAI Upgrade Documentation

## Overview
This application has been upgraded to support CrewAI multi-agent workflows with an optional AI Insights feature.

## Pattern: Optional Insights

## Agents
This implementation includes 3 specialized CrewAI agents:
1. **Data Analyst Agent**: Analyzes data for patterns and trends
2. **Insight Generator Agent**: Generates actionable insights
3. **Recommendation Agent**: Provides specific recommendations

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage
The AI Insights feature is optional and appears in the Streamlit interface.
Enable it by providing your OpenAI API key in the interface.

## Features
- Trend analysis across data
- Pattern identification
- Actionable recommendations
- Optional feature (doesn't break existing functionality)

---
**Upgraded**: 2025-12-21
**CrewAI Version**: 0.86.0+
**Pattern**: Optional Insights
EOF
```

#### 5. Git Commit (3 minutes)

```bash
git add .
git commit -m "Add CrewAI optional insights feature

Upgraded application to support CrewAI with optional AI insights.
Implemented 3 specialized agents for enhanced analytics.

- Created CrewAI agents (Data Analyst, Insight Generator, Recommendation)
- Created task definitions for analysis workflow
- Updated requirements.txt with crewai>=0.86.0, langchain-openai>=0.3.0
- Added CREWAI_UPGRADE.md documentation
- Maintained backward compatibility

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

#### 6. Create Completion Report (5 minutes)

```bash
cat > COMPLETION_REPORT.md << EOF
# ${REPO_NAME} - CrewAI Upgrade Completion Report

## Project Information
- **App ID**: ${APP_ID}
- **Repository**: ${REPO_OWNER}/${REPO_NAME}
- **Fork**: colygon/${REPO_NAME}
- **Agent Directory**: ${AGENT_DIR}
- **Pattern**: Optional Insights
- **Status**: COMPLETE

## Agents Implemented
1. **Data Analyst Agent**: Analyzes data for patterns and trends
2. **Insight Generator Agent**: Generates actionable insights from analysis
3. **Recommendation Agent**: Provides specific, practical recommendations

## Files Created/Modified
- crewai_agents/agents.py - Agent definitions
- crewai_agents/tasks.py - Task definitions
- requirements.txt - Updated with CrewAI dependencies
- CREWAI_UPGRADE.md - User documentation
- COMPLETION_REPORT.md - This file
- .env.example - Environment variable template

## Testing
- [ ] Application runs without errors
- [ ] AI Insights feature accessible
- [ ] Original functionality preserved
- [ ] CrewAI agents respond correctly

## Next Steps
1. Test the application: streamlit run <main_file>.py
2. Verify AI Insights feature works
3. Push to GitHub: git push origin main
4. Update BATCH_3_RESULTS.json with success status

---
**Completed**: 2025-12-21
**Time Spent**: ~30 minutes
EOF
```

#### 7. Update Tracking (2 minutes)

Update `BATCH_3_RESULTS.json`:
- Change status to "successful"
- Add completion_date
- Add agent_directory path
- Add commit_hash

---

## Phase 2: RAG Replacement Apps (12 hours)

Process the 8 RAG replacement apps that validated successfully.

### For Each App:

#### 1. Fork & Clone (5 minutes)

Same as Phase 1, step 1.

#### 2. Analyze Existing Implementation (10 minutes)

```bash
# Find main Streamlit file
find . -name "*.py" -type f | grep -E "(main|app|streamlit)" | head -5

# Look for LangChain usage
grep -r "langchain" --include="*.py" . | head -10

# Look for document processing
grep -r "pdf\|document\|embedding" --include="*.py" . | head -10
```

Document findings for reference.

#### 3. Create CrewAI Structure (25 minutes)

```bash
# Create agents.py
cat > agents.py << 'EOF'
"""
CrewAI Agents for Document Q&A System.
This module defines specialized agents for document analysis and question answering.
"""

from crewai import Agent


def create_document_analyst_agent(llm):
    """Create an agent that analyzes documents and identifies key themes."""
    return Agent(
        role="Document Analyst",
        goal="Analyze documents thoroughly to identify key themes, concepts, and important information",
        backstory="""You are an expert document analyst with years of experience in
        information extraction and summarization. You excel at quickly understanding
        the structure and content of documents, identifying main topics, and recognizing
        important details that might be relevant to user queries.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_question_interpreter_agent(llm):
    """Create an agent that interprets user questions to understand intent."""
    return Agent(
        role="Question Interpreter",
        goal="Understand the user's question intent, context, and what type of information they're seeking",
        backstory="""You are a skilled question analyst who specializes in understanding
        the nuances of user queries. You can identify whether users are looking for
        specific facts, summaries, comparisons, or explanations. You break down complex
        questions into their core components to ensure accurate and relevant answers.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_answer_synthesizer_agent(llm):
    """Create an agent that synthesizes answers from document analysis."""
    return Agent(
        role="Answer Synthesizer",
        goal="Combine document insights and question understanding to create accurate, well-cited answers",
        backstory="""You are a master synthesizer who brings together information from
        multiple sources to create comprehensive, accurate answers. You always cite your
        sources properly and ensure that every claim is backed by evidence from the
        documents. You present information clearly and concisely while maintaining accuracy.""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def get_all_agents(llm):
    """Get all agents for the document Q&A system."""
    return {
        'document_analyst': create_document_analyst_agent(llm),
        'question_interpreter': create_question_interpreter_agent(llm),
        'answer_synthesizer': create_answer_synthesizer_agent(llm)
    }
EOF

# Create tasks.py
cat > tasks.py << 'EOF'
"""
CrewAI Tasks for Document Q&A System.
This module defines the tasks that agents will perform.
"""

from crewai import Task


def create_document_analysis_task(agent, document_context):
    """Create a task for document analysis."""
    return Task(
        description=f"""Analyze the following document excerpts and identify key information:

        {document_context}

        Extract:
        - Main themes and topics
        - Key facts and details
        - Important concepts
        - Relevant context

        Provide a structured summary of the document content.""",
        agent=agent,
        expected_output="Structured analysis of document with main themes and key facts"
    )


def create_question_interpretation_task(agent, question):
    """Create a task for question interpretation."""
    return Task(
        description=f"""Analyze this user question to understand what they're asking:

        Question: {question}

        Determine:
        - What type of information is being requested?
        - What are the key concepts in the question?
        - What would constitute a complete answer?
        - Are there any implicit assumptions?

        Provide a clear interpretation of the question intent.""",
        agent=agent,
        expected_output="Clear interpretation of question intent and information needs"
    )


def create_answer_synthesis_task(agent, document_analysis, question_interpretation):
    """Create a task for answer synthesis."""
    return Task(
        description=f"""Create a comprehensive answer based on:

        Document Analysis:
        {document_analysis}

        Question Intent:
        {question_interpretation}

        Your answer should:
        - Directly address the question
        - Be supported by document evidence
        - Include proper citations
        - Be clear and concise

        Provide a well-structured answer with sources.""",
        agent=agent,
        expected_output="Comprehensive answer with citations and supporting evidence"
    )
EOF
```

#### 4. Create CrewAI Integration (30 minutes)

Create new file or modify existing to integrate CrewAI.
Follow knowledge-gpt-agent5 pattern.

Key elements:
- Toggle between original and CrewAI mode
- Use agents and tasks
- Maintain original functionality
- Add UI indicators

#### 5. Update Requirements (2 minutes)

Same as Phase 1, step 3.

#### 6. Create Comprehensive Documentation (15 minutes)

```bash
# .env.example
cat > .env.example << 'EOF'
# OpenAI API Key for CrewAI agents
OPENAI_API_KEY=your_openai_api_key_here
EOF

# CREWAI_UPGRADE.md
cat > CREWAI_UPGRADE.md << 'EOF'
# CrewAI Upgrade Documentation

## Overview
This application has been upgraded to support CrewAI multi-agent workflows for enhanced document Q&A capabilities.

## Pattern: RAG Replacement

## Agents
This implementation includes 3 specialized CrewAI agents:
1. **Document Analyst Agent**: Analyzes documents for key information
2. **Question Interpreter Agent**: Understands user question intent
3. **Answer Synthesizer Agent**: Creates comprehensive answers with citations

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Usage
The application now supports two modes:
1. **Original Mode**: Traditional LangChain processing (faster)
2. **CrewAI Mode**: Multi-agent processing (more accurate)

Toggle between modes in the application interface.

## Features
- Enhanced document understanding
- Better question interpretation
- More accurate answers with citations
- Backward compatible with original mode

## Architecture
```
Document Upload → Vector Embeddings → Question Input
                                            ↓
                                    [Mode Selection]
                                     ↙         ↘
                            CrewAI Mode    Original Mode
                                 ↓              ↓
                         3 Agent Pipeline    Single Chain
                                 ↓              ↓
                            Answer with     Quick Answer
                            Citations
```

---
**Upgraded**: 2025-12-21
**CrewAI Version**: 0.86.0+
**Pattern**: RAG Replacement
EOF

# QUICKSTART.md
cat > QUICKSTART.md << 'EOF'
# Quick Start Guide

## Installation
```bash
pip install -r requirements.txt
```

## Setup
1. Set OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-key"
   ```

2. Run the app:
   ```bash
   streamlit run <main_file>.py
   ```

## Using CrewAI Mode
1. Upload your document
2. Toggle "Use CrewAI Multi-Agent System" in Advanced Options
3. Ask your question
4. Get enhanced answer with citations

## Performance
- **Original Mode**: Fast, good for simple queries
- **CrewAI Mode**: Slower, better for complex questions

---
**Tip**: Start with CrewAI mode for best accuracy!
EOF
```

#### 7. Git Commit (3 minutes)

```bash
git add .
git commit -m "Add CrewAI multi-agent document Q&A support

Replaced single-chain LangChain with CrewAI multi-agent system.
Implemented 3 specialized agents for enhanced Q&A capabilities.

- Created CrewAI agents (Document Analyst, Question Interpreter, Answer Synthesizer)
- Created task definitions for sequential workflow
- Added dual-mode support (original + CrewAI)
- Updated requirements.txt with crewai>=0.86.0, langchain-openai>=0.3.0
- Added comprehensive documentation (CREWAI_UPGRADE.md, QUICKSTART.md)
- Maintained full backward compatibility

🤖 Generated with Claude Code (https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

#### 8. Create Completion Report (10 minutes)

Include detailed information about:
- Agents implemented
- Integration approach
- Files created/modified
- Testing performed
- Known limitations
- Future enhancements

#### 9. Test Application (15 minutes)

- [ ] App runs without errors
- [ ] Original mode works
- [ ] CrewAI mode works
- [ ] Toggle switches correctly
- [ ] Documents upload successfully
- [ ] Questions get answered
- [ ] Citations appear correctly

#### 10. Update Tracking (2 minutes)

Update `BATCH_3_RESULTS.json` with success status.

---

## Phase 3: Quality Assurance (2 hours)

### For Each Upgraded App:

1. **Functional Testing** (10 minutes per app)
   - [ ] Application starts without errors
   - [ ] UI is user-friendly
   - [ ] CrewAI features work
   - [ ] Original features still work
   - [ ] Error handling is graceful

2. **Code Review** (5 minutes per app)
   - [ ] Agents have clear roles and backstories
   - [ ] Tasks have proper descriptions
   - [ ] Code is well-documented
   - [ ] No hardcoded secrets
   - [ ] Follows Python best practices

3. **Documentation Review** (3 minutes per app)
   - [ ] CREWAI_UPGRADE.md exists and is clear
   - [ ] COMPLETION_REPORT.md is comprehensive
   - [ ] .env.example includes all variables
   - [ ] README preserved from original

4. **Git Review** (2 minutes per app)
   - [ ] Commit message follows template
   - [ ] Attribution included
   - [ ] No sensitive data committed
   - [ ] .gitignore properly configured

---

## Final Steps

### 1. Finalize Tracking

Update `BATCH_3_RESULTS.json` with final counts:
```json
{
  "completion_summary": {
    "attempted": <number>,
    "successful": <number>,
    "failed": <number>,
    "skipped": <number>
  }
}
```

### 2. Create Summary Report

Document:
- Total apps processed
- Success rate
- Common issues encountered
- Lessons learned
- Time actual vs estimated

### 3. Push All Changes

```bash
# For each successfully upgraded app
cd /Users/colinlowenberg/crew/<app-name>-agent<id>
git push origin main

# Update tracking in main crew directory
cd /Users/colinlowenberg/crew
git add BATCH_3_RESULTS.json
git commit -m "Update batch 3 results with final status"
git push
```

---

## Troubleshooting

### Repository Fork Failed
**Problem**: Cannot fork repository
**Solution**: Check if fork already exists in colygon org, or if repo is private/archived

### CrewAI Import Error
**Problem**: `ModuleNotFoundError: No module named 'crewai'`
**Solution**: `pip install crewai>=0.86.0`

### OpenAI API Error
**Problem**: Authentication failed
**Solution**: Verify OPENAI_API_KEY is set correctly

### Streamlit Won't Start
**Problem**: Application crashes on startup
**Solution**: Check requirements.txt, ensure all dependencies installed

---

## Success Criteria

Batch 3 is complete when:
- [ ] All valid repositories validated
- [ ] All accessible apps upgraded
- [ ] All upgrades committed to GitHub
- [ ] BATCH_3_RESULTS.json updated
- [ ] All apps tested and working
- [ ] Documentation complete
- [ ] No breaking changes introduced

---

## Time Tracking Template

Use this to track actual time spent:

| Phase | Estimated | Actual | Notes |
|-------|-----------|--------|-------|
| Validation | 0.5h | | |
| Optional Insights (total) | 2.5h | | |
| - App 1 | 0.5h | | |
| - App 2 | 0.5h | | |
| - App 3 | 0.5h | | |
| - App 4 | 0.5h | | |
| - App 5 | 0.5h | | |
| RAG Replacement (total) | 12h | | |
| - App 1 | 1.5h | | |
| - App 2 | 1.5h | | |
| - App 3 | 1.5h | | |
| - App 4 | 1.5h | | |
| - App 5 | 1.5h | | |
| - App 6 | 1.5h | | |
| - App 7 | 1.5h | | |
| - App 8 | 1.5h | | |
| QA & Testing | 2h | | |
| **TOTAL** | **17h** | | |

---

**This action plan provides everything needed to complete batch 3 upgrades successfully.**
