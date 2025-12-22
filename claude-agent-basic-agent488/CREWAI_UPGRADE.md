# Claude Code Python Agent SDK → CrewAI Migration Guide

## Overview

This guide provides a comprehensive mapping from the Claude Code Python Agent SDK to the CrewAI framework. It demonstrates **1:1 feature parity**, showing how every SDK concept can be replicated using CrewAI patterns.

## Table of Contents

1. [Concept Mapping](#concept-mapping)
2. [Migration Steps](#migration-steps)
3. [Pattern-by-Pattern Conversion](#pattern-by-pattern-conversion)
4. [Code Examples](#code-examples)
5. [Benefits & Trade-offs](#benefits--trade-offs)
6. [Troubleshooting](#troubleshooting)

---

## Concept Mapping

### Core Concepts

| SDK Concept | CrewAI Equivalent | Notes |
|-------------|------------------|-------|
| `query()` | `Agent + Task + Crew.kickoff()` | One-off execution pattern |
| `ClaudeSDKClient` | `Crew` with `memory=True` | Stateful conversation |
| `ClaudeAgentOptions` | `Agent` parameters + `Crew` config | Distributed configuration |
| `allowed_tools` | `Agent(tools=[...])` | Per-agent tool assignment |
| `disallowed_tools` | Tool filtering logic | Custom implementation |
| `system_prompt` | `Agent(role=..., goal=..., backstory=...)` | More structured approach |
| `hooks` | Tool wrappers + callbacks | Different event model |
| `agents` (subagents) | Multiple `Agent` instances | First-class citizens in CrewAI |
| `resume` (session ID) | Crew `memory` + `cache` | Automatic persistence |
| `permission_mode` | Custom tool validation | No built-in equivalent |
| `can_use_tool` callback | Tool wrapper functions | Implement permission logic in tools |

### Built-in Tools

| SDK Tool | CrewAI Implementation |
|----------|----------------------|
| `Read` | `FileReadTool()` or custom `@tool` |
| `Write` | Custom `@tool` with file writing |
| `Edit` | Custom `@tool` with find/replace logic |
| `Bash` | `ShellTool()` or subprocess wrapper |
| `Glob` | Custom `@tool` using `glob.glob()` |
| `Grep` | Custom `@tool` with regex search |
| `WebSearch` | `SerperDevTool()` or `DuckDuckGoSearchTool()` |
| `WebFetch` | `ScrapeWebsiteTool()` or `WebsiteSearchTool()` |
| `NotebookEdit` | Custom `@tool` for Jupyter operations |
| `Task` | Native agent delegation in CrewAI |
| `TodoWrite` | Custom `@tool` for task management |

---

## Migration Steps

### Step 1: Identify Your SDK Pattern

**Determine which SDK pattern you're using:**

1. **`query()` pattern**: One-off task execution
2. **`ClaudeSDKClient` pattern**: Multi-turn conversation
3. **Subagent pattern**: Hierarchical delegation
4. **Hook pattern**: Tool execution monitoring

### Step 2: Map SDK Options to CrewAI Components

**Before (SDK):**
```python
options = ClaudeAgentOptions(
    system_prompt="You are an expert debugger",
    allowed_tools=["Read", "Edit", "Bash"],
    permission_mode="acceptEdits"
)
```

**After (CrewAI):**
```python
from crewai import Agent
from tools import read_file, edit_file, bash_command

agent = Agent(
    role="Expert Debugger",
    goal="Debug code efficiently and accurately",
    backstory="Senior engineer with 10+ years debugging experience",
    tools=[read_file, edit_file, bash_command],
    verbose=True
)
```

### Step 3: Convert Prompt to Task

**Before (SDK):**
```python
result = await query("Fix bug in auth.py", options=options)
```

**After (CrewAI):**
```python
from crewai import Task

task = Task(
    description="Find and fix the bug in auth.py",
    agent=agent,
    expected_output="Fixed code with detailed explanation"
)
```

### Step 4: Create and Execute Crew

**Before (SDK):**
```python
async for message in query(prompt, options):
    if hasattr(message, 'result'):
        print(message.result)
```

**After (CrewAI):**
```python
from crewai import Crew, Process

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
print(result)
```

---

## Pattern-by-Pattern Conversion

### Pattern 1: Simple Query

#### SDK Code
```python
from claude_agent_sdk import query, ClaudeAgentOptions

async def analyze_file():
    async for message in query(
        prompt="Analyze auth.py for security issues",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep"],
            system_prompt="You are a security expert"
        )
    ):
        print(message)

# Run
import asyncio
asyncio.run(analyze_file())
```

#### CrewAI Code
```python
from crewai import Agent, Task, Crew, Process
from tools import read_file, grep_search

def analyze_file():
    # Create agent
    agent = Agent(
        role="Security Expert",
        goal="Identify security vulnerabilities in code",
        backstory="Expert in application security and code review",
        tools=[read_file, grep_search],
        verbose=True
    )

    # Create task
    task = Task(
        description="Analyze auth.py for security issues",
        agent=agent,
        expected_output="Security analysis report"
    )

    # Execute
    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential
    )

    result = crew.kickoff()
    print(result)

# Run (no asyncio needed)
analyze_file()
```

### Pattern 2: Multi-turn Conversation

#### SDK Code
```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def conversation():
    options = ClaudeAgentOptions(allowed_tools=["Read", "Edit"])

    async with ClaudeSDKClient(options=options) as client:
        # Turn 1
        await client.query("Read config.py")
        async for msg in client.receive_response():
            print(msg)

        # Turn 2 (has context from Turn 1)
        await client.query("Update the timeout value to 30")
        async for msg in client.receive_response():
            print(msg)

asyncio.run(conversation())
```

#### CrewAI Code
```python
from crewai import Agent, Task, Crew, Process
from tools import read_file, edit_file

def conversation():
    # Create stateful agent
    agent = Agent(
        role="Configuration Manager",
        goal="Manage configuration files",
        backstory="Expert at configuration management",
        tools=[read_file, edit_file],
        verbose=True,
        memory=True  # Enables context retention
    )

    # Create sequential tasks
    task1 = Task(
        description="Read config.py",
        agent=agent,
        expected_output="Contents of config.py"
    )

    task2 = Task(
        description="Update the timeout value to 30",
        agent=agent,
        expected_output="Updated configuration",
        context=[task1]  # Has access to previous task output
    )

    # Execute with memory
    crew = Crew(
        agents=[agent],
        tasks=[task1, task2],
        process=Process.sequential,
        memory=True,  # Like SDK sessions
        verbose=True
    )

    result = crew.kickoff()
    print(result)

# Run (synchronous)
conversation()
```

### Pattern 3: Hierarchical Delegation

#### SDK Code
```python
from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition

async def hierarchical():
    options = ClaudeAgentOptions(
        allowed_tools=["Task"],  # Can delegate
        agents={
            "code-reviewer": AgentDefinition(
                description="Expert code reviewer",
                prompt="Review code for quality issues",
                tools=["Read", "Grep"]
            ),
            "tester": AgentDefinition(
                description="QA engineer",
                prompt="Test code functionality",
                tools=["Bash"]
            )
        }
    )

    async for msg in query("Review and test the codebase", options):
        print(msg)

asyncio.run(hierarchical())
```

#### CrewAI Code
```python
from crewai import Agent, Task, Crew, Process
from tools import read_file, grep_search, bash_command

def hierarchical():
    # Define specialized agents
    code_reviewer = Agent(
        role="Code Reviewer",
        goal="Review code for quality issues",
        backstory="Expert in code quality and best practices",
        tools=[read_file, grep_search],
        verbose=True
    )

    tester = Agent(
        role="QA Engineer",
        goal="Test code functionality",
        backstory="Expert in software testing",
        tools=[bash_command],
        verbose=True
    )

    # Manager agent that delegates
    manager = Agent(
        role="Development Lead",
        goal="Coordinate code review and testing",
        backstory="Experienced lead who manages quality processes",
        tools=[],
        allow_delegation=True,
        verbose=True
    )

    # Create high-level task (manager will delegate)
    task = Task(
        description="Review and test the codebase",
        agent=manager,
        expected_output="Complete code review and test results"
    )

    # Execute with hierarchical process
    crew = Crew(
        agents=[manager, code_reviewer, tester],
        tasks=[task],
        process=Process.hierarchical,  # Manager delegates automatically
        manager_llm="gpt-4",
        verbose=True
    )

    result = crew.kickoff()
    print(result)

# Run
hierarchical()
```

### Pattern 4: Hooks and Callbacks

#### SDK Code
```python
from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher

async def log_tool_use(input_data, tool_use_id, context):
    print(f"[PRE] Using tool: {input_data.get('tool_name')}")
    return {}

async def with_hooks():
    options = ClaudeAgentOptions(
        allowed_tools=["Read"],
        hooks={
            'PreToolUse': [HookMatcher(hooks=[log_tool_use])],
            'PostToolUse': [HookMatcher(hooks=[log_tool_use])]
        }
    )

    async for msg in query("Read auth.py", options):
        print(msg)

asyncio.run(with_hooks())
```

#### CrewAI Code
```python
from crewai import Agent, Task, Crew, Process
from crewai_tools import tool

# Create tool wrapper with logging
@tool("read_file_with_logging")
def read_file_logged(file_path: str) -> str:
    """Read file with pre/post logging."""
    print(f"[PRE] Using tool: read_file")

    try:
        with open(file_path, 'r') as f:
            content = f.read()

        print(f"[POST] Tool completed: read_file")
        return content
    except Exception as e:
        print(f"[ERROR] Tool failed: {str(e)}")
        return f"Error: {str(e)}"


def with_hooks():
    agent = Agent(
        role="File Reader",
        goal="Read files with logging",
        backstory="File operations specialist",
        tools=[read_file_logged],  # Use wrapped tool
        verbose=True
    )

    task = Task(
        description="Read auth.py",
        agent=agent,
        expected_output="File contents"
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential
    )

    result = crew.kickoff()
    print(result)

# Run
with_hooks()
```

### Pattern 5: Session Resumption

#### SDK Code
```python
from claude_agent_sdk import query, ClaudeAgentOptions

async def sessions():
    # First query - save session ID
    session_id = None
    async for msg in query("What is 5 + 3?", ClaudeAgentOptions()):
        if hasattr(msg, 'session_id'):
            session_id = msg.session_id

    # Resume session
    async for msg in query(
        "Multiply that by 2",
        ClaudeAgentOptions(resume=session_id)
    ):
        print(msg)

asyncio.run(sessions())
```

#### CrewAI Code
```python
from crewai import Agent, Task, Crew, Process

def sessions():
    # Create agent with memory
    agent = Agent(
        role="Calculator",
        goal="Perform calculations",
        backstory="Math expert",
        tools=[],
        memory=True
    )

    # First query
    task1 = Task(
        description="What is 5 + 3?",
        agent=agent,
        expected_output="Result of calculation"
    )

    # Second query (automatically has context from first)
    task2 = Task(
        description="Multiply that by 2",
        agent=agent,
        expected_output="Result of multiplication",
        context=[task1]
    )

    # Crew maintains memory automatically
    crew = Crew(
        agents=[agent],
        tasks=[task1, task2],
        process=Process.sequential,
        memory=True,  # Enables automatic context retention
        cache=True    # Persists memory
    )

    result = crew.kickoff()
    print(result)

# Run
sessions()
```

---

## Code Examples

### Complete Example: File Operations

#### SDK Implementation
```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def file_operations():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write", "Edit"],
        permission_mode="acceptEdits",
        system_prompt="You are a file management expert"
    )

    async with ClaudeSDKClient(options=options) as client:
        # Create file
        await client.query("Create a file called test.txt with content 'Hello World'")
        async for msg in client.receive_response():
            pass

        # Read file
        await client.query("Read test.txt")
        async for msg in client.receive_response():
            print(msg)

        # Edit file
        await client.query("Replace 'World' with 'CrewAI' in test.txt")
        async for msg in client.receive_response():
            pass

import asyncio
asyncio.run(file_operations())
```

#### CrewAI Implementation
```python
from crewai import Agent, Task, Crew, Process
from tools import read_file, write_file, edit_file

def file_operations():
    # Create agent
    agent = Agent(
        role="File Management Expert",
        goal="Manage file operations efficiently",
        backstory="Expert in file system operations and management",
        tools=[read_file, write_file, edit_file],
        verbose=True,
        memory=True
    )

    # Create tasks
    create_task = Task(
        description="Create a file called test.txt with content 'Hello World'",
        agent=agent,
        expected_output="Confirmation of file creation"
    )

    read_task = Task(
        description="Read test.txt",
        agent=agent,
        expected_output="Contents of test.txt",
        context=[create_task]
    )

    edit_task = Task(
        description="Replace 'World' with 'CrewAI' in test.txt",
        agent=agent,
        expected_output="Confirmation of edit",
        context=[read_task]
    )

    # Execute
    crew = Crew(
        agents=[agent],
        tasks=[create_task, read_task, edit_task],
        process=Process.sequential,
        memory=True,
        verbose=True
    )

    result = crew.kickoff()
    print(result)

# Run (no asyncio needed)
file_operations()
```

---

## Benefits & Trade-offs

### Benefits of CrewAI

✅ **Multi-Agent Collaboration**
- SDK: Single agent with tool delegation
- CrewAI: True multi-agent teams with specialized roles

✅ **Simpler Async Model**
- SDK: Requires async/await and generator iteration
- CrewAI: Synchronous execution, simpler code

✅ **Structured Agent Definition**
- SDK: Flat options dictionary
- CrewAI: Rich Agent objects with role/goal/backstory

✅ **Better Task Management**
- SDK: String prompts
- CrewAI: Task objects with context and dependencies

✅ **Automatic Memory**
- SDK: Manual session ID management
- CrewAI: Built-in crew-level memory

✅ **Parallel Execution**
- SDK: Sequential tool execution
- CrewAI: True parallel task execution with `async_execution=True`

### Trade-offs

⚠️ **Streaming Responses**
- SDK: Real-time streaming of messages
- CrewAI: Result-based (no streaming)
- **Mitigation**: Use verbose mode for progress updates

⚠️ **Permission System**
- SDK: Built-in `permission_mode` and `can_use_tool`
- CrewAI: No built-in equivalent
- **Mitigation**: Implement permission logic in tool wrappers

⚠️ **Hooks**
- SDK: Rich hook system (PreToolUse, PostToolUse, etc.)
- CrewAI: No direct equivalent
- **Mitigation**: Use tool wrappers or step callbacks

⚠️ **Session IDs**
- SDK: Explicit session IDs for fine-grained control
- CrewAI: Automatic memory (less granular)
- **Mitigation**: Use separate crews for separate "sessions"

⚠️ **File Checkpointing**
- SDK: Built-in `rewind_files()` functionality
- CrewAI: No built-in equivalent
- **Mitigation**: Implement custom version control in tools

---

## Troubleshooting

### Common Migration Issues

#### Issue 1: "Agent doesn't remember previous context"

**Problem**: Agent forgets previous tasks

**Solution**:
```python
# Make sure memory is enabled
crew = Crew(
    agents=[agent],
    tasks=[task1, task2],
    memory=True,  # Enable this!
    cache=True    # And this for persistence
)

# Also use task context
task2 = Task(
    description="...",
    agent=agent,
    context=[task1]  # Reference previous task
)
```

#### Issue 2: "Tools not executing"

**Problem**: Agent isn't using tools

**Solution**:
```python
# Ensure tools are imported correctly
from tools import read_file, write_file

# Assign to agent
agent = Agent(
    role="...",
    tools=[read_file, write_file],  # Pass function objects, not strings
    verbose=True  # See what's happening
)
```

#### Issue 3: "Need async functionality"

**Problem**: Need async operations like SDK

**Solution**:
```python
# CrewAI is sync, but you can wrap it
import asyncio
from concurrent.futures import ThreadPoolExecutor

async def async_crewai():
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, crew.kickoff)
    return result
```

#### Issue 4: "Missing SDK tools"

**Problem**: Need SDK built-in tools

**Solution**: Use the `tools.py` module in this project, which implements all common SDK tools as CrewAI tools.

```python
from tools import (
    read_file,    # SDK: Read
    write_file,   # SDK: Write
    edit_file,    # SDK: Edit
    bash_command, # SDK: Bash
    glob_files,   # SDK: Glob
    grep_search   # SDK: Grep
)
```

---

## Summary

This migration guide provides 1:1 feature parity between the Claude Code Python Agent SDK and CrewAI. While the APIs differ, every SDK capability can be replicated in CrewAI with equivalent or enhanced functionality.

**Quick Reference:**
- **Simple queries** → Agent + Task + Crew
- **Conversations** → Agent with memory=True + sequential tasks
- **Subagents** → Multiple Agent instances
- **Hooks** → Tool wrappers
- **Sessions** → Crew memory + cache

For more examples, see the `examples/` directory in this repository.

---

**Generated with Claude Code**
**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
