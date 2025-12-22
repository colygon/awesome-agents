# Realtime Conversational Agent - CrewAI Edition

## Migration from Google ADK to CrewAI

This application has been migrated from Google's Agent Development Kit (ADK) to CrewAI, replacing Google Gemini with OpenAI models and implementing a multi-agent conversational workflow using CrewAI's framework.

## Overview

The Realtime Conversational Agent provides intelligent, context-aware conversational capabilities through a multi-agent system. It offers:

1. **Intent Recognition** - Accurately identifies user intentions and extracts entities
2. **Knowledge Retrieval** - Accesses relevant information to answer questions
3. **Conversation Management** - Maintains context and manages dialogue flow
4. **Response Generation** - Produces natural, contextually appropriate responses

## Architecture

### ADK vs CrewAI Comparison

| Component | Google ADK (Original) | CrewAI (Migrated) |
|-----------|----------------------|-------------------|
| **Framework** | Google ADK | CrewAI |
| **LLM** | Gemini Flash | OpenAI GPT-4o-mini |
| **Conversation Flow** | Single agent with tools | Multi-agent crew |
| **Context Management** | Built-in session state | Custom ConversationManagerTool |
| **Realtime Capabilities** | WebSocket streaming | Sequential processing |
| **Deployment** | Vertex AI Agent Engine | Standalone Python application |

### CrewAI Agents

1. **Conversation Manager Agent** (`conversation_manager`)
   - Replaces: ADK's session state management
   - Role: Manages multi-turn conversations and context
   - Tools: ConversationManagerTool, ContextMemoryTool
   - Capabilities: Track history, analyze patterns, maintain flow

2. **Intent Recognizer Agent** (`intent_recognizer`)
   - Replaces: ADK's intent detection logic
   - Role: Identifies user intent and extracts entities
   - Capabilities: Intent classification, entity extraction, tone detection

3. **Response Generator Agent** (`response_generator`)
   - Replaces: ADK's response generation
   - Role: Crafts natural, contextually appropriate responses
   - Tools: ResponseGeneratorTool
   - Capabilities: Adaptive tone, style customization, clear communication

4. **Knowledge Retriever Agent** (`knowledge_retriever`)
   - Replaces: ADK's knowledge base access
   - Role: Retrieves relevant information to support responses
   - Capabilities: Search formulation, source evaluation, information synthesis

### Custom Tools

1. **ConversationManagerTool**
   - Manages conversation state and history
   - Operations: store, retrieve, analyze
   - Tracks: turns, intents, entities, timestamps

2. **ContextMemoryTool**
   - Stores and retrieves contextual information
   - Remembers: user preferences, mentioned facts, ongoing topics
   - Operations: get, set

3. **ResponseGeneratorTool**
   - Provides response generation guidelines
   - Adapts: style (conversational, formal, concise, detailed)
   - Intent-aware: templates for different user intentions

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key
- (Optional) Serper API key for web search

### Installation

1. **Clone or download this directory**

```bash
cd realtime-conversational-agent402
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

## Usage

### Interactive Chat Mode

```bash
python main.py
```

This launches an interactive chat session where you can have ongoing conversations with the agent.

**Available Commands:**
- Type your message to chat
- `history` - View conversation history
- `clear` - Clear conversation history
- `quit` or `exit` - End the session

### Single Message Mode

```bash
python main.py "What is the weather like today?"
```

Process a single message and exit.

### Example Interaction

```
Welcome! I'm your conversational AI assistant.
I can help you with questions, tasks, and general conversation.

Commands:
  - Type your message to chat
  - 'history' to see conversation history
  - 'clear' to clear conversation history
  - 'quit' or 'exit' to end the session

================================================================================

You: Hello! Can you help me understand machine learning?

================================================================================
User: Hello! Can you help me understand machine learning?
================================================================================

Processing your message...

[Agent execution logs...]

================================================================================
Assistant: Hello! I'd be happy to help you understand machine learning!

Machine learning is a branch of artificial intelligence where computers learn
from data without being explicitly programmed. Instead of following specific
instructions, ML systems identify patterns and make decisions based on examples.

There are three main types:
1. Supervised Learning - Learning from labeled examples
2. Unsupervised Learning - Finding patterns in unlabeled data
3. Reinforcement Learning - Learning through trial and error

What aspect of machine learning interests you most? Would you like to know
about specific algorithms, applications, or how to get started with learning it?
================================================================================

You: I'm interested in getting started. What should I learn first?

[Conversation continues...]
```

## Key Migration Changes

### 1. Conversation Architecture

**Before (ADK):**
```python
# Single agent with built-in conversation handling
conversational_agent = ConversationalAgent(
    model="gemini-flash",
    enable_streaming=True
)
```

**After (CrewAI):**
```python
# Multi-agent crew with specialized roles
crew = Crew(
    agents=[conversation_manager, intent_recognizer,
            response_generator, knowledge_retriever],
    tasks=create_tasks(message, history),
    process=Process.sequential
)
```

### 2. Context Management

**Before (ADK):**
- Automatic session state in Vertex AI
- Built-in conversation history
- Native streaming support

**After (CrewAI):**
- Custom ConversationManagerTool
- Manual history tracking
- Sequential processing (batch-style)

### 3. Intent Handling

**Before (ADK):**
- Integrated intent recognition
- Automatic entity extraction

**After (CrewAI):**
- Dedicated IntentRecognizer agent
- Explicit intent and entity analysis
- More transparent intent processing

### 4. Response Generation

**Before (ADK):**
- Single-step response generation
- Streaming responses

**After (CrewAI):**
- Multi-step workflow (intent → knowledge → management → response)
- Richer context consideration
- More structured response process

## Features Preserved

All core conversational capabilities have been preserved:

- ✓ Multi-turn conversation support
- ✓ Context awareness across turns
- ✓ Intent recognition
- ✓ Entity extraction
- ✓ Natural language generation
- ✓ Adaptive tone and style
- ✓ Conversation history tracking
- ✓ Knowledge retrieval capabilities

## Benefits of CrewAI Migration

1. **Transparency** - Clear separation of conversational responsibilities
2. **Customization** - Easy to modify individual agent behaviors
3. **Extensibility** - Simple to add new agents or capabilities
4. **Platform Independence** - No Google Cloud dependency
5. **Debugging** - Easier to trace conversation processing steps
6. **Control** - More fine-grained control over conversation flow

## Limitations and Notes

1. **No Streaming** - Unlike ADK's realtime streaming, responses are generated in batch
2. **Latency** - Multi-agent processing takes longer than single-agent responses
3. **Memory** - In-memory storage only (conversation history not persisted)
4. **Scalability** - Not designed for concurrent multi-user scenarios out-of-the-box

## Customization

### Changing Response Style

Edit `agents.py` to modify agent backstories:

```python
response_generator = Agent(
    role="Response Generation Specialist",
    backstory="""Your custom backstory defining the agent's personality..."""
)
```

### Adding New Intents

Update the intent templates in `tools.py`:

```python
intent_templates = {
    "asking_question": "...",
    "your_new_intent": "Your custom template..."
}
```

### Enhancing Knowledge Retrieval

Add external search capabilities to `knowledge_retriever` agent:

```python
from crewai_tools import SerperDevTool

knowledge_retriever = Agent(
    tools=[SerperDevTool()]
)
```

### Persisting Conversation History

Replace in-memory storage with database:

```python
# In ConversationManagerTool
import sqlite3

def _run(self, action: str, data: Dict = None):
    # Store conversations in SQLite/PostgreSQL
    conn = sqlite3.connect('conversations.db')
    # Implementation...
```

## Troubleshooting

### "Responses are slow"
- Multi-agent processing takes time
- Consider reducing number of agents for simpler queries
- Use more concise agent backstories

### "Context not being maintained"
- Check that conversation history is being passed correctly
- Verify ConversationManagerTool is storing turns
- Ensure history is included in task descriptions

### "Repetitive responses"
- Adjust agent backstories to encourage variety
- Modify temperature in agent LLM configuration
- Review response generation templates

### "Memory errors with long conversations"
- Limit conversation history to recent N turns
- Implement conversation summarization
- Clear history periodically

## Future Enhancements

Potential improvements for this CrewAI version:

1. **Streaming Support** - Implement response streaming with callback handlers
2. **Persistent Storage** - Add database for conversation history
3. **Multi-User Support** - Session management for concurrent users
4. **Voice Integration** - Add speech-to-text and text-to-speech
5. **Advanced RAG** - Integrate vector databases for knowledge retrieval
6. **Emotion Detection** - Enhanced emotional intelligence
7. **Proactive Engagement** - Agent initiates relevant follow-ups
8. **Multi-Modal** - Support for image and document inputs

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
