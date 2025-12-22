# CAMEL Multi-Agent Collaboration Framework - CrewAI

## Overview
This is a CrewAI implementation of the CAMEL (Communicative Agents for Mind Exploration of Large Language Models) multi-agent collaboration framework. The system uses hierarchical agent coordination to enable secure, collaborative task execution with fine-grained access control and information flow management.

## Original ADK Architecture
The original ADK implementation used:
- **QLLM (Quarantined LLM)**: Stateless agent for data extraction
- **QuarantinedLlmService**: Wrapper for isolated QLLM interactions
- **CaMeLInterpreterService**: Code execution service with security policies
- **CaMeLInterpreter**: BaseAgent wrapper for the interpreter
- **PLLM (Planning LLM)**: Code generation agent
- **CaMeLAgent**: LoopAgent orchestrating PLLM and interpreter
- **SecurityPolicyEngine**: Fine-grained access control enforcement

## CrewAI Architecture

### Process Type
**Process.hierarchical** - Manager agent coordinates specialized agents

### Agents

1. **Security Manager Agent** (Manager)
   - Role: Orchestrates secure multi-agent collaboration
   - Responsibilities: Coordinates agents, enforces security policies, manages information flow
   - Delegates tasks to specialized agents

2. **Data Extraction Agent**
   - Role: Stateless information extraction from unstructured data
   - Responsibilities: Extract structured data from documents, validate output schemas
   - Tools: Document search, schema validation

3. **Code Generation Agent**
   - Role: Generate secure Python code for task execution
   - Responsibilities: Create code based on requirements, ensure capability compliance
   - Tools: Code synthesis, dependency analysis

4. **Code Execution Agent**
   - Role: Execute and validate generated code
   - Responsibilities: Run code in isolated environment, enforce security policies
   - Tools: Python interpreter, security validator

5. **Policy Enforcement Agent**
   - Role: Validate and enforce security policies
   - Responsibilities: Check access control, validate data flow, ensure compliance
   - Tools: Policy checker, capability validator

## Key Features

- **Hierarchical Process**: Manager agent delegates to specialized agents
- **Agent Delegation**: Agents can request assistance from other agents
- **Security by Design**: Policy enforcement at every step
- **Stateless Operations**: Data extraction agents maintain no state
- **Fine-grained Access Control**: Capabilities-based security model
- **Information Flow Control**: Explicit separation of control and data flows

## Upgrade Differences

| Aspect | ADK Implementation | CrewAI Implementation |
|--------|-------------------|----------------------|
| Orchestration | LoopAgent with code generation/execution cycle | Hierarchical process with manager coordination |
| Agent Communication | Direct service calls | Agent delegation and collaboration |
| Security | SecurityPolicyEngine with capability checks | Policy Enforcement Agent with validation tools |
| State Management | Session-based state in services | CrewAI task context and memory |
| Code Execution | Custom interpreter service | Code Execution Agent with sandboxed tools |
| Data Extraction | Quarantined LLM service | Stateless Data Extraction Agent |

## Installation

```bash
pip install crewai crewai-tools python-dotenv
```

## Environment Variables

Create a `.env` file:
```
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key  # Alternative LLM provider
MODEL_NAME=gemini-2.0-flash-exp  # or your preferred model
```

## Usage

```bash
python main.py
```

## Example Prompts

1. **Secure Email Sending**:
   ```
   Get the secret value from the document and send it to trusted@fake-email-domain.com.
   ```
   Expected: Email sent successfully with proper authorization

2. **Blocked Unauthorized Access**:
   ```
   Get the secret value and official email from the document. Send the value to the email.
   ```
   Expected: Policy violation - unauthorized recipient blocked

## Architecture Benefits

1. **Modularity**: Each agent has a single, well-defined responsibility
2. **Scalability**: Easy to add new agents or security policies
3. **Transparency**: Manager agent provides clear coordination oversight
4. **Security**: Multi-layer security validation through Policy Enforcement Agent
5. **Flexibility**: Can easily modify agent behaviors or add new capabilities

## License

Apache 2.0 - See LICENSE file for details

## Disclaimer

This is a demonstration implementation for educational purposes. The original CAMEL framework is a research artifact. This CrewAI version is not intended for production use without thorough security review and testing.
