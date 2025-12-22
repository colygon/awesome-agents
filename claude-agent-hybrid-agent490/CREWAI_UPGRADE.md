# Hybrid Migration Guide: Claude SDK → CrewAI

This guide focuses on the **hybrid migration path** - running SDK and CrewAI together during transition.

For basic SDK→CrewAI mapping, see [Basic App (agent488)](../claude-agent-basic-agent488/CREWAI_UPGRADE.md).
For advanced CrewAI features, see [Enhanced App (agent489)](../claude-agent-enhanced-agent489/CREWAI_UPGRADE.md).

## Migration Philosophy

**Gradual over Big Bang**
- Incremental changes reduce risk
- Validate each step before proceeding
- Rollback is always possible
- Team learns progressively

## Three-Stage Migration Path

### Stage 1: Pure SDK (Current State)

Your existing SDK-based application:

```python
from claude_agent_sdk import query, ClaudeSDKClient

# Simple query pattern
result = query(
    "List all Python files and analyze their imports",
    allowed_tools=["Glob", "Grep", "Read"]
)

# Client pattern with sessions
client = ClaudeSDKClient()
client.execute("Read main.py")
client.execute("Now analyze the code you just read")
```

**Characteristics:**
- Single agent per execution
- SDK-provided tools
- Session-based memory
- Sequential execution

### Stage 2: Hybrid (Transition)

SDK tools wrapped for CrewAI orchestration:

```python
from crewai import Agent, Task, Crew, Process
from sdk_tools import glob_files_sdk, grep_search_sdk, read_file_sdk

# Create CrewAI agent using SDK tools
code_analyst = Agent(
    role="Code Analyst",
    goal="Analyze Python codebase structure",
    tools=[glob_files_sdk, grep_search_sdk, read_file_sdk],  # SDK tools!
    verbose=True
)

security_reviewer = Agent(
    role="Security Reviewer",
    goal="Find security issues",
    tools=[read_file_sdk, grep_search_sdk],  # SDK tools!
    verbose=True
)

# CrewAI orchestration with SDK execution
tasks = [
    Task(description="Find all Python files", agent=code_analyst),
    Task(description="Scan for security vulnerabilities", agent=security_reviewer)
]

crew = Crew(
    agents=[code_analyst, security_reviewer],
    tasks=tasks,
    process=Process.sequential
)

result = crew.kickoff()  # Multi-agent with SDK tools!
```

**Characteristics:**
- Multiple agents (CrewAI)
- SDK tools (wrapped)
- Crew memory (CrewAI)
- Sequential or parallel (CrewAI)

**Benefits:**
- Immediate multi-agent collaboration
- Keep proven SDK tools
- Low migration risk
- Incremental tool replacement possible

### Stage 3: Pure CrewAI (Target State)

Native CrewAI implementation:

```python
from crewai import Agent, Task, Crew, Process
from tools import glob_files, grep_search, read_file  # Native tools

code_analyst = Agent(
    role="Code Analyst",
    goal="Analyze Python codebase structure",
    tools=[glob_files, grep_search, read_file],  # Native CrewAI!
    verbose=True
)

security_reviewer = Agent(
    role="Security Reviewer",
    goal="Find security issues",
    tools=[read_file, grep_search],  # Native CrewAI!
    verbose=True
)

# Same workflow, native execution
crew = Crew(
    agents=[code_analyst, security_reviewer],
    tasks=tasks,
    process=Process.parallel  # Now we can do parallel!
)

result = crew.kickoff()
```

**Characteristics:**
- Multiple agents (CrewAI)
- Native tools (CrewAI)
- Full CrewAI features
- Best performance

## Implementation Guide

### Step 1: Create SDK Tool Wrappers

```python
# sdk_tools.py
from crewai.tools import tool
from claude_agent_sdk import query

@tool("read_file_sdk")
def read_file_sdk(file_path: str) -> str:
    """
    Read file using Claude SDK.
    Wrapper for SDK Read tool.
    """
    result = query(
        f"Read the contents of {file_path}",
        allowed_tools=["Read"]
    )
    return str(result)

@tool("glob_files_sdk")
def glob_files_sdk(pattern: str, path: str = ".") -> str:
    """
    Find files using Claude SDK.
    Wrapper for SDK Glob tool.
    """
    result = query(
        f"Find files matching {pattern} in {path}",
        allowed_tools=["Glob"]
    )
    return str(result)

@tool("bash_command_sdk")
def bash_command_sdk(command: str) -> str:
    """
    Execute bash command using Claude SDK.
    Wrapper for SDK Bash tool.
    """
    result = query(
        f"Execute this bash command: {command}",
        allowed_tools=["Bash"]
    )
    return str(result)

# Wrap all SDK tools you currently use
```

### Step 2: Create Compatibility Bridge

```python
# hybrid_integration.py
from claude_agent_sdk import ClaudeAgentOptions
from crewai import Agent

class SDKCrewAIBridge:
    """Convert between SDK and CrewAI concepts."""

    @staticmethod
    def sdk_options_to_agent(sdk_options: ClaudeAgentOptions) -> Agent:
        """
        Convert SDK ClaudeAgentOptions to CrewAI Agent.

        Args:
            sdk_options: SDK agent configuration

        Returns:
            Equivalent CrewAI Agent
        """
        # Extract role from system prompt
        role = sdk_options.system_prompt[:100] if sdk_options.system_prompt else "Assistant"

        # Map SDK tools to wrapped tools
        from sdk_tools import (
            read_file_sdk, write_file_sdk, edit_file_sdk,
            bash_command_sdk, glob_files_sdk, grep_search_sdk
        )

        tool_map = {
            "Read": read_file_sdk,
            "Write": write_file_sdk,
            "Edit": edit_file_sdk,
            "Bash": bash_command_sdk,
            "Glob": glob_files_sdk,
            "Grep": grep_search_sdk
        }

        tools = [tool_map[t] for t in sdk_options.allowed_tools if t in tool_map]

        # Create CrewAI agent
        return Agent(
            role=role,
            goal="Execute tasks using SDK tools",
            backstory="Agent migrated from Claude SDK",
            tools=tools,
            verbose=sdk_options.verbose if hasattr(sdk_options, 'verbose') else True
        )

    @staticmethod
    def execute_with_sdk_session(agent: Agent, prompt: str):
        """
        Execute using SDK session management.
        Useful for maintaining SDK session semantics.
        """
        from claude_agent_sdk import ClaudeSDKClient

        client = ClaudeSDKClient()
        # Integrate with agent execution
        # Implementation depends on specific needs
        pass
```

### Step 3: Migrate Incrementally

**Week 1: Add CrewAI, Keep SDK Tools**

```python
# Install CrewAI
# pip install crewai>=0.86.0

# Create hybrid agents
from crewai import Agent
from sdk_tools import read_file_sdk, write_file_sdk

agent = Agent(
    role="Developer",
    tools=[read_file_sdk, write_file_sdk],  # Still using SDK!
)

# Test multi-agent workflows with SDK tools
```

**Week 2: Replace One Tool**

```python
# Implement native read_file
from tools import read_file  # New native implementation
from sdk_tools import write_file_sdk  # Still SDK

agent = Agent(
    role="Developer",
    tools=[read_file, write_file_sdk],  # Mixed!
)

# Compare results: SDK vs native
```

**Week 3-N: Continue Tool Migration**

Replace tools one at a time, testing thoroughly after each change.

**Final Week: Remove SDK Dependency**

```python
from tools import read_file, write_file  # All native

agent = Agent(
    role="Developer",
    tools=[read_file, write_file],  # Fully migrated!
)

# Remove claude-agent-sdk from requirements.txt
```

## Decision Matrix

### When to Keep SDK Tools

✅ **Keep SDK Tool If:**
- Complex custom logic hard to replicate
- Proven reliability in production
- Infrequent usage (not worth migration effort)
- Requires specific SDK features

❌ **Replace with Native If:**
- Simple tool (easy to reimplement)
- High-frequency usage (performance matters)
- Need advanced CrewAI features
- SDK tool has known issues

### Migration Priority

**High Priority (Migrate First):**
1. High-frequency tools (biggest performance gain)
2. Simple tools (easy wins)
3. Tools blocking advanced features

**Medium Priority:**
4. Moderately complex tools
5. Tools with acceptable SDK performance

**Low Priority (Consider Keeping):**
6. Complex custom tools
7. Rarely used tools
8. Tools requiring significant testing

## Common Migration Patterns

### Pattern 1: Tool-by-Tool Replacement

```python
# Start: All SDK
tools = [read_sdk, write_sdk, edit_sdk, bash_sdk, glob_sdk, grep_sdk]

# Step 1: Replace simple tools
tools = [read_file, write_file, edit_sdk, bash_sdk, glob_sdk, grep_sdk]

# Step 2: Replace more tools
tools = [read_file, write_file, edit_file, bash_command, glob_sdk, grep_sdk]

# Step 3: Complete migration
tools = [read_file, write_file, edit_file, bash_command, glob_files, grep_search]
```

### Pattern 2: Agent-by-Agent Replacement

```python
# Agent 1: Fully migrated
agent1 = Agent(role="Analyst", tools=[native_tools])

# Agent 2: Still hybrid
agent2 = Agent(role="Developer", tools=[mixed_tools])

# Agent 3: Still SDK
agent3 = Agent(role="Reviewer", tools=[sdk_tools])

# Gradually migrate agent2, then agent3
```

### Pattern 3: Feature Flag Migration

```python
USE_SDK_TOOLS = os.getenv("USE_SDK_TOOLS", "false") == "true"

if USE_SDK_TOOLS:
    tools = [read_file_sdk, write_file_sdk]
else:
    tools = [read_file, write_file]

agent = Agent(role="Assistant", tools=tools)

# Gradually roll out native tools via feature flag
```

## Testing Strategy

### Parallel Execution Test

```python
# Run both implementations, compare results
def test_migration():
    # SDK approach
    sdk_result = query("Analyze main.py", allowed_tools=["Read"])

    # CrewAI approach with SDK tools
    agent = Agent(role="Analyst", tools=[read_file_sdk])
    task = Task(description="Analyze main.py", agent=agent)
    crew = Crew(agents=[agent], tasks=[task])
    crewai_result = crew.kickoff()

    # Compare
    assert similar_results(sdk_result, crewai_result)
```

### Gradual Rollout

```python
# Route X% of traffic to CrewAI
import random

def analyze_code(file_path):
    if random.random() < 0.1:  # 10% CrewAI
        return crewai_analyze(file_path)
    else:  # 90% SDK
        return sdk_analyze(file_path)

# Gradually increase percentage
```

## Performance Considerations

### SDK Tool Overhead

SDK-wrapped tools have extra latency:
```
Native CrewAI tool:  X ms
SDK-wrapped tool:    X + API_CALL_OVERHEAD ms
```

**Mitigation:**
- Migrate high-frequency tools first
- Use caching where possible
- Batch SDK calls if feasible

### Memory Usage

Hybrid approach uses more memory:
- SDK session state
- CrewAI crew memory
- Both frameworks loaded

**Mitigation:**
- Remove SDK dependency when fully migrated
- Use process isolation if memory is critical

## Rollback Strategy

### Quick Rollback

```python
# Keep both implementations ready
class HybridExecutor:
    def execute(self, use_crewai=False):
        if use_crewai:
            return self.execute_crewai()
        else:
            return self.execute_sdk()

    def execute_sdk(self):
        # Original SDK implementation
        pass

    def execute_crewai(self):
        # New CrewAI implementation
        pass

# Easy to switch back
```

### Version Control

```bash
# Tag each migration milestone
git tag v1.0-sdk-only
git tag v1.1-hybrid-start
git tag v1.2-hybrid-50percent
git tag v1.3-hybrid-complete
git tag v2.0-crewai-only

# Easy rollback
git checkout v1.1-hybrid-start
```

## Success Metrics

Track these during migration:

1. **Functionality Parity**: Do results match SDK implementation?
2. **Performance**: Is latency acceptable?
3. **Error Rates**: Any increase in failures?
4. **Team Velocity**: Can team work effectively?
5. **Cost**: API usage and compute costs

## Timeline Estimation

**Small Project** (1-2 agents, 3-5 tools):
- Hybrid setup: 1-2 days
- Tool migration: 1 week
- Testing & validation: 1 week
- **Total: 2-3 weeks**

**Medium Project** (3-5 agents, 6-10 tools):
- Hybrid setup: 3-5 days
- Tool migration: 2-3 weeks
- Testing & validation: 1-2 weeks
- **Total: 4-7 weeks**

**Large Project** (6+ agents, 10+ tools):
- Hybrid setup: 1 week
- Tool migration: 4-8 weeks
- Testing & validation: 2-4 weeks
- **Total: 7-13 weeks**

## Troubleshooting

### SDK tools not working in CrewAI
- Check SDK installation
- Verify API keys
- Ensure wrapper signatures correct
- Test SDK tools independently first

### Session state not transferring
- SDK sessions ≠ CrewAI crews
- Implement custom state management
- Consider using CrewAI memory instead

### Performance degradation
- SDK wrappers add latency
- Migrate high-frequency tools first
- Profile to find bottlenecks

## Best Practices

1. **Test Incrementally** - Validate each tool migration
2. **Monitor Closely** - Track metrics during migration
3. **Document Decisions** - Why you kept/replaced each tool
4. **Feature Flag** - Enable easy rollback
5. **Parallel Run** - Compare SDK vs CrewAI results
6. **Team Training** - Ensure everyone understands CrewAI

---

## Migration Checklist

- [ ] Audit current SDK usage
- [ ] Create SDK tool wrappers
- [ ] Implement compatibility bridge
- [ ] Set up parallel testing
- [ ] Create rollback plan
- [ ] Train team on CrewAI
- [ ] Migrate tools incrementally
- [ ] Validate each migration step
- [ ] Monitor performance metrics
- [ ] Remove SDK dependency (when complete)
- [ ] Document final architecture

---

*Hybrid Migration Guide for Claude SDK → CrewAI*
*Part of Claude Code Agent migration suite*
