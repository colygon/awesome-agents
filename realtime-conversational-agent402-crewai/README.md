# Realtime Conversational Multi-Agent System - CrewAI

## Overview
This is a CrewAI implementation of a real-time conversational system powered by multiple specialized agents working asynchronously. The system manages live conversations, tracks context across turns, and generates intelligent, context-aware responses in real-time.

## Original ADK Architecture
The original ADK implementation likely used:
- Real-time message processing with async/await
- Streaming response generation
- Context management across conversation turns
- State persistence for conversation history
- Event-driven architecture for live updates

## CrewAI Architecture

### Process Type
**Process.hierarchical** with async task execution - Manager coordinates real-time conversation flow

### Agents

1. **Conversation Manager Agent** (Manager)
   - Role: Orchestrates real-time conversation flow and agent coordination
   - Responsibilities: Route messages, manage turn-taking, coordinate specialized agents, ensure coherent responses
   - Async capabilities: Handles concurrent user inputs and agent responses

2. **Context Tracker Agent**
   - Role: Maintains conversation context and memory
   - Responsibilities: Track conversation history, extract entities and topics, maintain user preferences
   - Async capabilities: Updates context in real-time as conversation progresses

3. **Response Generator Agent**
   - Role: Generates intelligent, context-aware responses
   - Responsibilities: Craft appropriate responses, maintain conversation style, ensure relevance
   - Async capabilities: Streams responses as they're generated

4. **Intent Classifier Agent**
   - Role: Understands user intent and sentiment
   - Responsibilities: Classify message intent, detect sentiment, identify action items
   - Async capabilities: Processes intents in parallel with response generation

5. **Knowledge Retrieval Agent**
   - Role: Retrieves relevant information for responses
   - Responsibilities: Search knowledge bases, fetch external data, provide factual information
   - Async capabilities: Concurrent knowledge lookups for faster responses

## Key Features

- **Real-time Processing**: Async agent coordination for low-latency responses
- **Context Awareness**: Continuous context tracking across conversation turns
- **Streaming Responses**: Progressive response generation for better UX
- **Multi-turn Conversations**: Coherent dialogue over extended interactions
- **Concurrent Processing**: Parallel intent classification and knowledge retrieval
- **Memory Management**: Short-term and long-term conversation memory

## Architecture Highlights

### Conversation Flow
1. **Message Reception**: User message arrives
2. **Parallel Processing**:
   - Intent Classifier: Determines user intent
   - Context Tracker: Updates conversation context
   - Knowledge Retrieval: Fetches relevant information
3. **Response Generation**: Crafts response based on all inputs
4. **Stream Delivery**: Progressively sends response to user
5. **Context Update**: Stores turn in conversation history

### Async Coordination
- All agents process tasks concurrently
- Manager coordinates timing and dependencies
- Streaming responses improve perceived responsiveness
- Context updates happen asynchronously

## Upgrade Differences

| Aspect | ADK Implementation | CrewAI Implementation |
|--------|-------------------|----------------------|
| Processing | Event-driven async handlers | Hierarchical process with async tasks |
| Context Management | State machine with history | Context Tracker Agent with memory |
| Response Generation | Streaming LLM calls | Response Generator Agent with streaming |
| Intent Detection | Integrated in main agent | Dedicated Intent Classifier Agent |
| Knowledge Access | Tool-based retrieval | Knowledge Retrieval Agent |
| Coordination | Event loop coordination | Manager agent orchestration |

## Installation

```bash
pip install crewai crewai-tools python-dotenv aiohttp
```

## Environment Variables

Create a `.env` file:
```
GOOGLE_API_KEY=your_google_api_key
MODEL_NAME=gemini-2.0-flash-exp
ENABLE_STREAMING=true
```

## Usage

### Basic Usage
```bash
python main.py
```

### Async API Server
```bash
python server.py
```

## Example Conversations

1. **Information Retrieval**:
   ```
   User: What's the weather like today?
   System: [Intent: weather_query] [Retrieving weather data...]
   System: Currently it's 72°F and sunny in your area...
   ```

2. **Multi-turn Conversation**:
   ```
   User: Tell me about Python
   System: Python is a high-level programming language...
   User: What about its history?
   System: [Using context: Python] Python was created by Guido van Rossum...
   User: Who is he?
   System: [Using context: Guido van Rossum] He's a Dutch programmer...
   ```

3. **Task Execution**:
   ```
   User: Set a reminder for tomorrow at 3pm
   System: [Intent: create_reminder] I'll set a reminder for tomorrow at 3:00 PM...
   ```

## Architecture Benefits

1. **Low Latency**: Async processing reduces response time
2. **Scalability**: Handles multiple concurrent conversations
3. **Context Continuity**: Maintains coherent multi-turn dialogues
4. **Flexibility**: Easy to add new intents or knowledge sources
5. **User Experience**: Streaming responses feel more natural

## Real-time Features

- **Typing Indicators**: Shows when system is processing
- **Progressive Responses**: Streams text as generated
- **Concurrent Processing**: Multiple aspects processed in parallel
- **Live Context Updates**: Context evolves with conversation
- **Fast Intent Detection**: Parallel intent classification

## License

Apache 2.0 - See LICENSE file for details
