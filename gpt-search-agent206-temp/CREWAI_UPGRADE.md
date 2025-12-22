# CrewAI Upgrade Guide - GPT Search

## Overview

This document describes the CrewAI upgrade for the GPT Search application. The upgrade introduces a multi-agent system that enhances the quality and reliability of query answering through specialized AI agents working together.

## Architecture

### Original Architecture

The original GPT Search application used a simple pipeline:

1. **Semantic Search**: Use sentence transformers to find similar passages
2. **Single-Agent Inference**: Pass top-k results to GPT-3.5-turbo with a single prompt
3. **Return Response**: Display the generated answer

### Enhanced CrewAI Architecture

The upgraded system uses a multi-agent collaborative approach:

```
User Query + Text Corpus
         ↓
   Semantic Search (unchanged)
         ↓
   Top-K Similar Passages
         ↓
┌─────────────────────────────┐
│   CrewAI Agent Pipeline     │
├─────────────────────────────┤
│ 1. Semantic Search Agent    │
│    - Analyzes query intent  │
│    - Identifies relevant    │
│      passages               │
│    - Extracts key info      │
│         ↓                   │
│ 2. Answer Synthesis Agent   │
│    - Generates answer from  │
│      extracted info         │
│    - Maintains context      │
│    - Ensures accuracy       │
│         ↓                   │
│ 3. Quality Validator Agent  │
│    - Verifies accuracy      │
│    - Checks for             │
│      hallucinations         │
│    - Validates completeness │
└─────────────────────────────┘
         ↓
   Final Answer
```

## Agent Specifications

### 1. Semantic Search Specialist

**Role**: Find the most relevant information from text corpus

**Responsibilities**:
- Understanding user intent from queries
- Identifying key passages that contain answers
- Extracting relevant facts and statements
- Noting important context and qualifications

**Tools**: FileReadTool (for potential extended capabilities)

**Configuration**:
- Model: GPT-4
- Temperature: 0.2 (for consistent analysis)
- Verbose: True

### 2. Answer Synthesis Expert

**Role**: Generate accurate, well-structured answers

**Responsibilities**:
- Analyzing retrieved text passages
- Extracting key information relevant to queries
- Synthesizing clear, concise answers
- Maintaining context and accuracy
- Never making up information

**Configuration**:
- Model: GPT-4
- Temperature: 0.2 (for reliable answers)
- Verbose: True

### 3. Quality Assurance Specialist

**Role**: Ensure answer quality and accuracy

**Responsibilities**:
- Verifying answers against source material
- Detecting hallucinations or unsupported claims
- Ensuring answers directly address queries
- Improving answer clarity and completeness

**Configuration**:
- Model: GPT-4
- Temperature: 0.2 (for consistent validation)
- Verbose: True

## Task Workflow

### Sequential Process

The agents work in a sequential process where each agent builds upon the previous one's work:

1. **Search Task** → Identifies relevant passages and extracts key information
2. **Answer Synthesis Task** → Uses search results to generate answer
3. **Quality Validation Task** → Verifies and improves the answer

### Task Dependencies

```python
search_task = SearchTask(query, top_results)
answer_task = AnswerSynthesisTask(query, search_task)  # Depends on search_task
validation_task = ValidationTask(query, answer_task, top_results)  # Depends on answer_task
```

## Usage Modes

### Standard Mode (Original)

Uses the original OpenAI GPT-3.5-turbo inference:
- Fast, single-agent response
- Good for simple queries
- Lower cost

### CrewAI Simple Mode

Uses 2 agents (Search + Synthesis):
- Better quality than standard
- Moderate speed
- Good balance of quality and performance

### CrewAI Full Mode

Uses all 3 agents (Search + Synthesis + Validation):
- Highest quality answers
- Most thorough analysis
- Best for complex or critical queries

## Integration

### Environment Variables

```bash
# Enable CrewAI mode
export USE_CREWAI=true

# Set OpenAI API key
export OPENAI_API_KEY=your_api_key_here
```

### Programmatic Usage

```python
from main import crewai_inference, simple_crewai_inference

# Full quality mode
data = {
    'query': 'How has technology transformed work?',
    'top_results': [...list of relevant passages...]
}
answer = crewai_inference(data, k=5, temperature=0.2)

# Simple mode (faster)
answer = simple_crewai_inference(data, k=5, temperature=0.2)
```

### Streamlit UI Integration

The upgraded search_app.py provides three options:
1. **Standard GPT**: Original OpenAI inference
2. **CrewAI (Simple)**: 2-agent pipeline
3. **CrewAI (Full Quality Validation)**: 3-agent pipeline

## Benefits

### 1. Improved Accuracy
- Multiple agents verify information
- Reduced hallucinations
- Better grounding in source material

### 2. Enhanced Quality
- Thorough analysis of retrieved passages
- Better synthesis of information
- Quality validation before delivery

### 3. Transparency
- Verbose mode shows agent reasoning
- Clear task breakdown
- Easier to debug and understand

### 4. Flexibility
- Multiple modes for different use cases
- Backward compatible with original
- Optional CrewAI activation

## Performance Considerations

### Speed
- **Standard**: ~2-5 seconds
- **CrewAI Simple**: ~10-20 seconds
- **CrewAI Full**: ~20-40 seconds

### Cost
- **Standard**: ~$0.001-0.002 per query (GPT-3.5)
- **CrewAI Simple**: ~$0.01-0.02 per query (GPT-4, 2 agents)
- **CrewAI Full**: ~$0.02-0.04 per query (GPT-4, 3 agents)

### Quality
- **Standard**: Good for simple queries
- **CrewAI Simple**: Better for complex queries
- **CrewAI Full**: Best for critical queries requiring high accuracy

## Migration Path

### Step 1: Optional Installation
```bash
pip install crewai>=0.86.0 langchain-openai>=0.3.0 crewai-tools>=0.17.0
```

### Step 2: Enable CrewAI
```bash
export USE_CREWAI=true
```

### Step 3: Run Application
```bash
streamlit run search_app.py
```

### Step 4: Select Mode
Choose inference mode in the UI:
- Start with "CrewAI (Simple)" for testing
- Use "CrewAI (Full Quality Validation)" for production

## Backward Compatibility

The upgrade maintains full backward compatibility:

1. **Default Behavior**: Without CrewAI installation or USE_CREWAI flag, app works exactly as before
2. **Optional Dependencies**: CrewAI packages are optional
3. **API Compatibility**: Original functions remain unchanged
4. **No Breaking Changes**: All existing functionality preserved

## Testing

### Manual Testing
1. Run with standard mode and note answer
2. Run same query with CrewAI mode
3. Compare quality and accuracy
4. Verify no regressions

### Example Queries
```python
# Technology query
"How has technology transformed the way we work?"

# Healthcare query
"How can AI be used in healthcare?"

# Custom queries based on your corpus
```

## Troubleshooting

### CrewAI Not Loading
- Check `USE_CREWAI` environment variable
- Verify CrewAI installation: `pip list | grep crewai`
- Check import errors in console

### Slow Performance
- Use "CrewAI (Simple)" instead of full mode
- Reduce k value (number of top results)
- Consider using standard mode for simple queries

### Quality Issues
- Try increasing k value for more context
- Use full validation mode for critical queries
- Check source passages for relevance

## Future Enhancements

Potential improvements:
1. **Caching**: Cache agent responses for common queries
2. **Streaming**: Stream agent outputs in real-time
3. **Custom Tools**: Add domain-specific tools to agents
4. **Memory**: Add conversation memory for follow-up queries
5. **Metrics**: Track quality metrics and agent performance

## Conclusion

The CrewAI upgrade provides a flexible, high-quality enhancement to GPT Search while maintaining full backward compatibility. Users can choose the appropriate mode based on their quality, speed, and cost requirements.
