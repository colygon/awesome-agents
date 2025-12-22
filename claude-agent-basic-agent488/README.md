# Claude Code Agent - Basic SDK Migration

**Agent ID:** 488
**Category:** Agent SDK Migration
**Framework:** CrewAI
**Purpose:** Feature Parity - 1:1 SDK→CrewAI Mapping

## Overview

This application demonstrates **1:1 feature parity** between the Claude Code Python Agent SDK and the CrewAI framework. It shows exactly how to migrate from SDK patterns to equivalent CrewAI implementations.

### What This App Demonstrates

✅ SDK `query()` → CrewAI Agent + Task pattern
✅ SDK `ClaudeSDKClient` → CrewAI with memory
✅ SDK tools → Custom CrewAI tools
✅ SDK hooks → Tool wrappers and callbacks
✅ SDK subagents → Multi-agent CrewAI
✅ SDK sessions → CrewAI memory + cache

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Run interactive demo
python main.py
```

## Architecture

### SDK Concepts → CrewAI Mapping

| SDK Concept | CrewAI Implementation |
|-------------|----------------------|
| `query(prompt, options)` | `Agent + Task + Crew.kickoff()` |
| `ClaudeSDKClient()` | `Crew` with `memory=True` |
| `allowed_tools` | `Agent(tools=[...])` |
| `system_prompt` | `Agent(role=..., goal=..., backstory=...)` |
| Subagents | Multiple `Agent` instances |
| Hooks | Tool wrappers with logging |
| Sessions | Crew `memory` + `cache` |

### Project Structure

```
claude-agent-basic-agent488/
├── agents.py              # Agent definitions mapping SDK patterns
├── tasks.py               # Task builders for different patterns
├── tools.py               # Custom tools (Read, Write, Edit, Bash, Glob, Grep)
├── main.py                # Interactive demo with 5 scenarios
├── requirements.txt       # CrewAI and dependencies
├── .env.example           # API key template
├── examples/              # Side-by-side SDK vs CrewAI comparisons
│   ├── query_pattern.py   # query() pattern
│   ├── client_pattern.py  # ClaudeSDKClient pattern
│   ├── hooks_pattern.py   # Hooks and callbacks
│   ├── subagent_pattern.py # Hierarchical delegation
│   └── tools_pattern.py   # Tool mapping examples
├── README.md              # This file
├── CREWAI_UPGRADE.md      # Complete migration guide
└── COMPLETION_REPORT.md   # Implementation details
```

## Agents

This app defines several agents that map to common SDK patterns:

### 1. Query Agent
**Maps to**: `query()` pattern
**Tools**: File reading, bash commands, glob search
**Use case**: One-off task execution

### 2. Stateful Agent
**Maps to**: `ClaudeSDKClient` pattern
**Tools**: File operations
**Use case**: Multi-turn conversations with memory

### 3. File Operations Agent
**Maps to**: SDK with file tools
**Tools**: Read, Write, Edit, Glob
**Use case**: File manipulation tasks

### 4. Code Analyst Agent
**Maps to**: SDK with analysis tools
**Tools**: Read, Glob, Grep
**Use case**: Code analysis and searching

### 5. Delegating Agent
**Maps to**: SDK hierarchical pattern
**Tools**: Limited set, relies on delegation
**Use case**: Managing specialized sub-agents

## Tools

All SDK built-in tools have been reimplemented as CrewAI tools:

- ✅ **read_file**: Matches SDK Read tool
- ✅ **write_file**: Matches SDK Write tool
- ✅ **edit_file**: Matches SDK Edit tool
- ✅ **bash_command**: Matches SDK Bash tool
- ✅ **glob_files**: Matches SDK Glob tool
- ✅ **grep_search**: Matches SDK Grep tool

See `tools.py` for implementation details.

## Usage Examples

### Example 1: Simple Query Pattern

**SDK:**
```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for message in query(
    prompt="List Python files",
    options=ClaudeAgentOptions(allowed_tools=["Glob"])
):
    print(message)
```

**CrewAI:**
```python
from crewai import Agent, Task, Crew, Process
from tools import glob_files

agent = Agent(
    role="File Lister",
    tools=[glob_files],
    verbose=True
)

task = Task(
    description="List Python files",
    agent=agent,
    expected_output="List of .py files"
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
```

### Example 2: Multi-turn Conversation

**SDK:**
```python
from claude_agent_sdk import ClaudeSDKClient

async with ClaudeSDKClient(options) as client:
    await client.query("Read config.py")
    await client.query("Update timeout to 30")
```

**CrewAI:**
```python
agent = Agent(role="Config Manager", tools=[read_file, edit_file], memory=True)

task1 = Task(description="Read config.py", agent=agent)
task2 = Task(description="Update timeout to 30", agent=agent, context=[task1])

crew = Crew(agents=[agent], tasks=[task1, task2], memory=True)
result = crew.kickoff()
```

## Interactive Demo

Run `python main.py` to see:

1. **query() Pattern** - Simple one-off task
2. **ClaudeSDKClient Pattern** - Stateful conversation
3. **File Operations** - Create, read, edit files
4. **Code Analysis** - Search and analyze code
5. **Concept Mapping** - Side-by-side comparison

## Migration Guide

See [CREWAI_UPGRADE.md](./CREWAI_UPGRADE.md) for:

- Complete concept mapping table
- Step-by-step migration instructions
- Before/after code examples for every SDK pattern
- Troubleshooting common issues
- Benefits and trade-offs

## Key Differences

| Aspect | SDK | CrewAI |
|--------|-----|--------|
| **Execution** | Async (streaming) | Sync (result-based) |
| **Memory** | Session IDs | Automatic crew memory |
| **Tools** | String names | Function objects |
| **Agents** | Single with delegation | Multi-agent collaboration |
| **Permissions** | Built-in system | Custom tool wrappers |

## Benefits of CrewAI

- ✅ Simpler execution model (no async/await)
- ✅ True multi-agent collaboration
- ✅ Automatic memory management
- ✅ Structured agent definitions
- ✅ Parallel task execution
- ✅ Better task dependency management

## Requirements

- Python 3.8+
- OpenAI API key
- CrewAI >= 0.86.0

See `requirements.txt` for complete dependencies.

## Related Apps

- **[Claude Agent Enhanced (489)](../claude-agent-enhanced-agent489/)** - Advanced multi-agent workflows
- **[Claude Agent Hybrid (490)](../claude-agent-hybrid-agent490/)** - SDK + CrewAI integration

## Credits

**Migrated from**: Claude Code Python Agent SDK
**Framework**: CrewAI
**Generated with**: [Claude Code](https://claude.com/claude-code)
**Co-Authored-By**: Claude Sonnet 4.5 <noreply@anthropic.com>

## License

Apache 2.0 (same as original SDK)
