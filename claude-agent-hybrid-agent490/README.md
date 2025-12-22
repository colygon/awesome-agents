# Claude Code Agent - Hybrid SDK+CrewAI Integration

**Agent ID:** 490
**Purpose:** Migration Path - SDK + CrewAI Coexistence
**Category:** CrewAI Hybrid Implementation

## Overview

This application demonstrates a **hybrid approach** to migrating from the Claude Code Python Agent SDK to CrewAI. It shows how SDK tools and CrewAI orchestration can coexist during a gradual migration, providing a practical migration path for existing SDK-based applications.

## Three-Stage Migration Path

### Stage 1: Pure SDK (Starting Point)
```python
from claude_agent_sdk import query

# Traditional SDK approach
result = query("List Python files", allowed_tools=["Glob", "Read"])
```

### Stage 2: Hybrid (Transition)
```python
from crewai import Agent, Task, Crew
from sdk_tools import glob_files_sdk, read_file_sdk  # SDK tool wrappers

# CrewAI orchestration with SDK tools
agent = Agent(
    role="File Analyst",
    tools=[glob_files_sdk, read_file_sdk],  # Use SDK under the hood
)
```

### Stage 3: Pure CrewAI (End State)
```python
from crewai import Agent, Task, Crew
from tools import glob_files, read_file  # Native CrewAI tools

# Full CrewAI implementation
agent = Agent(
    role="File Analyst",
    tools=[glob_files, read_file],  # Pure CrewAI
)
```

## Project Structure

```
claude-agent-hybrid-agent490/
├── migration/
│   ├── step1_sdk_only.py       # Pure SDK implementation
│   ├── step2_hybrid.py         # SDK tools + CrewAI orchestration
│   └── step3_crewai_only.py    # Pure CrewAI implementation
├── sdk_tools.py                # SDK tool wrappers for CrewAI
├── crewai_agents.py            # Agents using SDK tools
├── hybrid_integration.py        # SDK↔CrewAI compatibility bridge
├── main.py                      # Interactive demo
├── requirements.txt             # Both SDK and CrewAI dependencies
├── .env.example                 # API keys
├── README.md                    # This file
├── CREWAI_UPGRADE.md            # Migration guide
└── COMPLETION_REPORT.md         # Implementation details
```

## Why Hybrid?

### Benefits of Gradual Migration

1. **Lower Risk** - Test CrewAI incrementally without rewriting everything
2. **Preserve Investment** - Keep using SDK tools that work well
3. **Learn Progressively** - Understand CrewAI patterns step-by-step
4. **Rollback Safety** - Easy to revert if issues arise
5. **Team Adoption** - Gradual learning curve for the team

### Migration Scenarios

**Scenario A: Keep SDK Tools, Add CrewAI Orchestration**
- You have complex SDK tools with custom logic
- Want multi-agent collaboration
- Don't want to reimplement tools
- Solution: Wrap SDK tools for CrewAI agents

**Scenario B: Gradual Tool Replacement**
- Replace SDK tools one at a time
- Test each replacement thoroughly
- Mix SDK and native CrewAI tools during transition
- Solution: Hybrid crew with mixed tool sources

**Scenario C: Feature Flag Migration**
- Run SDK and CrewAI implementations in parallel
- Compare results before full cutover
- Progressive rollout to users
- Solution: Feature flags to switch between implementations

## Quick Start

### Installation

```bash
# Navigate to project
cd claude-agent-hybrid-agent490

# Install dependencies (includes both SDK and CrewAI)
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add:
# - OPENAI_API_KEY (for CrewAI)
# - ANTHROPIC_API_KEY (for Claude SDK, optional)
```

### Run Migration Demos

```bash
# Stage 1: Pure SDK
python migration/step1_sdk_only.py

# Stage 2: Hybrid approach
python migration/step2_hybrid.py

# Stage 3: Pure CrewAI
python migration/step3_crewai_only.py

# Interactive comparison
python main.py
```

## Architecture

### SDK Tool Wrapper Pattern

```python
# sdk_tools.py
from crewai.tools import tool
from claude_agent_sdk import query

@tool("read_file_sdk")
def read_file_sdk(file_path: str) -> str:
    """Read file using Claude SDK under the hood."""
    result = query(
        f"Read the file at {file_path}",
        allowed_tools=["Read"]
    )
    return result

# Now CrewAI agents can use SDK tools!
agent = Agent(role="Analyst", tools=[read_file_sdk])
```

### Compatibility Bridge

```python
# hybrid_integration.py
class SDKCrewAIBridge:
    """Convert between SDK and CrewAI concepts."""

    @staticmethod
    def sdk_options_to_agent_config(sdk_options):
        """Convert ClaudeAgentOptions → Agent kwargs"""
        return {
            'role': sdk_options.system_prompt[:50],
            'tools': [wrap_sdk_tool(t) for t in sdk_options.allowed_tools],
            'verbose': True
        }

    @staticmethod
    def wrap_sdk_tool(tool_name):
        """Wrap an SDK tool for CrewAI usage"""
        # Implementation details...
```

## Migration Guide

### Step 1: Assess Current SDK Usage

Identify:
- Which SDK tools you use
- Custom tools you've built
- Workflow patterns
- Session management needs

### Step 2: Choose Migration Strategy

**Option A: Big Bang** (Pure SDK → Pure CrewAI)
- Best for: Small projects, simple workflows
- Risk: High
- Duration: Short

**Option B: Gradual** (SDK → Hybrid → CrewAI)
- Best for: Production systems, complex workflows
- Risk: Low
- Duration: Longer, but safer

**Option C: Parallel** (Run both, compare results)
- Best for: Critical systems, need validation
- Risk: Lowest
- Duration: Longest

### Step 3: Implement Hybrid Layer

1. Create SDK tool wrappers:
   ```python
   # Wrap each SDK tool you use
   @tool("bash_sdk")
   def bash_sdk(command: str) -> str:
       return query(f"Run: {command}", allowed_tools=["Bash"])
   ```

2. Create CrewAI agents using SDK tools:
   ```python
   agent = Agent(
       role="Developer",
       tools=[bash_sdk, read_file_sdk],  # SDK tools
   )
   ```

3. Build CrewAI workflows:
   ```python
   crew = Crew(agents=[agent], tasks=[task])
   result = crew.kickoff()  # CrewAI orchestration with SDK execution
   ```

### Step 4: Migrate Tools Incrementally

Replace SDK tools one at a time:

```python
# Week 1: Replace Read tool
from tools import read_file  # New CrewAI tool
agent.tools = [read_file, bash_sdk]  # Mix native + SDK

# Week 2: Replace Bash tool
from tools import bash_command
agent.tools = [read_file, bash_command]  # All native

# Continue until fully migrated...
```

### Step 5: Remove SDK Dependency

Once all tools migrated:
```bash
# Remove from requirements.txt
- claude-agent-sdk>=1.0.0

pip install -r requirements.txt  # Reinstall without SDK
```

## Comparison: SDK vs Hybrid vs Pure CrewAI

| Aspect | Pure SDK | Hybrid | Pure CrewAI |
|--------|----------|--------|-------------|
| Tool execution | SDK | SDK | Native |
| Orchestration | SDK | CrewAI | CrewAI |
| Multi-agent | Limited | Full | Full |
| Migration risk | N/A | Low | Medium-High |
| Complexity | Low | Medium | Low |
| Performance | Good | Good | Better |
| Best for | Existing apps | Migration | New projects |

## Use Cases

1. **Gradual Migration**: Large SDK codebase moving to CrewAI
2. **Tool Preservation**: Keep complex SDK tools while adding multi-agent
3. **Validation**: Run both implementations, compare results
4. **Team Training**: Learn CrewAI without abandoning SDK
5. **Risk Mitigation**: Rollback capability during transition

## Example: Hybrid Code Review

```python
# Hybrid approach: SDK tools + CrewAI multi-agent collaboration

from crewai import Agent, Task, Crew
from sdk_tools import read_file_sdk, grep_search_sdk  # SDK wrappers
from tools import analyze_code_quality  # New CrewAI tool

# Reviewer uses SDK tools (proven, reliable)
reviewer = Agent(
    role="Code Reviewer",
    tools=[read_file_sdk, grep_search_sdk],  # SDK
)

# Analyst uses new CrewAI tool
analyst = Agent(
    role="Quality Analyst",
    tools=[read_file_sdk, analyze_code_quality],  # Mixed!
)

# CrewAI orchestration
crew = Crew(
    agents=[reviewer, analyst],
    tasks=[review_task, analysis_task],
    process=Process.sequential
)

result = crew.kickoff()  # Best of both worlds!
```

## Troubleshooting

### SDK tools not working in CrewAI
- Ensure SDK is installed: `pip list | grep claude-agent-sdk`
- Check API keys in .env
- Verify tool wrapper signatures match CrewAI @tool decorator

### Performance issues
- SDK tools may be slower than native (extra API calls)
- Consider migrating high-frequency tools first
- Use caching where possible

### Context/session management
- SDK sessions don't automatically map to CrewAI crews
- Implement custom session management if needed
- Consider using CrewAI's built-in memory instead

## Advantages of Hybrid Approach

1. **Incremental Migration** - No big-bang rewrite required
2. **Tool Reuse** - Leverage existing SDK tools investment
3. **Multi-Agent Benefits** - Get CrewAI collaboration immediately
4. **Lower Risk** - Test new patterns without full commitment
5. **Flexibility** - Mix and match as needed during transition

## When to Use Hybrid

✅ **Use Hybrid When:**
- Migrating existing SDK application
- Have complex custom SDK tools
- Need validation period
- Team learning CrewAI gradually
- Production system (low-risk migration)

❌ **Skip Hybrid When:**
- Starting new project (go pure CrewAI)
- Simple SDK usage (easy full migration)
- No SDK tool dependencies
- Want maximum performance

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - SDK→CrewAI feature parity
- [Claude Agent Enhanced (agent489)](../claude-agent-enhanced-agent489/) - Advanced multi-agent workflows

## Credits

**Framework**: CrewAI >= 0.86.0 + Claude Agent SDK (optional)
**Generated with**: [Claude Code](https://claude.com/claude-code)
**Co-Authored-By**: Claude Sonnet 4.5 <noreply@anthropic.com>

## License

MIT License - See parent repository for details
