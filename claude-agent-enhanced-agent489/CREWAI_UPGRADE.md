# CrewAI Advanced Features Guide

This document covers **advanced CrewAI patterns** that go beyond basic SDK feature parity. If you're looking for SDK→CrewAI migration basics, see the Basic app (agent488) documentation.

## Table of Contents

1. [Hierarchical Workflows](#hierarchical-workflows)
2. [Parallel Task Execution](#parallel-task-execution)
3. [Multi-Agent Collaboration](#multi-agent-collaboration)
4. [Specialized Agent Teams](#specialized-agent-teams)
5. [Advanced Task Patterns](#advanced-task-patterns)
6. [Memory and Context Sharing](#memory-and-context-sharing)
7. [Performance Optimization](#performance-optimization)

---

## Hierarchical Workflows

### Overview

Hierarchical workflows allow a manager agent to delegate tasks to specialist agents, similar to a software development team structure.

### Key Concept

SDK Pattern: Single agent, flat execution
CrewAI Enhancement: Manager delegates to team of specialists

### Implementation

```python
from crewai import Crew, Process
from agents import create_code_architect, create_senior_developer, create_code_reviewer

# Create team
manager = create_code_architect()  # Must have allow_delegation=True
developer = create_senior_developer()
reviewer = create_code_reviewer()

# Create tasks
tasks = [task1, task2, task3]  # Your task list

# Create hierarchical crew
crew = Crew(
    agents=[manager, developer, reviewer],
    tasks=tasks,
    process=Process.hierarchical,  # KEY: Use hierarchical process
    manager_agent=manager,          # KEY: Designate the manager
    verbose=True
)

result = crew.kickoff()
```

### Manager Agent Requirements

```python
manager_agent = Agent(
    role="Team Lead",
    goal="Coordinate team and ensure quality",
    backstory="Experienced leader...",
    tools=[read_file, glob_files],  # Tools for coordination
    allow_delegation=True,  # REQUIRED for managers
    verbose=True
)
```

### When to Use

- Complex projects requiring task breakdown
- Situations where different specialists are needed
- Projects where one agent should orchestrate others
- Quality-critical work requiring oversight

### Benefits

- Automatic task delegation
- Specialized expertise for each subtask
- Built-in quality control (manager reviews work)
- Realistic team simulation

---

## Parallel Task Execution

### Overview

Execute multiple tasks simultaneously using different agents, then synthesize results.

### Key Concept

SDK Pattern: Sequential execution only
CrewAI Enhancement: True parallel execution with async tasks

### Implementation

```python
# Create parallel tasks (set async_execution=True)
security_task = Task(
    description="Security audit of codebase",
    agent=security_agent,
    expected_output="Security findings",
    async_execution=True  # KEY: Enables parallel execution
)

performance_task = Task(
    description="Performance analysis",
    agent=performance_agent,
    expected_output="Performance metrics",
    async_execution=True  # KEY: Runs in parallel with security_task
)

quality_task = Task(
    description="Code quality review",
    agent=quality_agent,
    expected_output="Quality report",
    async_execution=True  # KEY: Runs in parallel
)

# Create synthesis task (waits for all parallel tasks)
synthesis_task = Task(
    description="Combine all findings into action plan",
    agent=architect_agent,
    expected_output="Prioritized action plan",
    context=[security_task, performance_task, quality_task],  # Waits for these
    async_execution=False  # Runs after parallel tasks complete
)

# Create crew
crew = Crew(
    agents=[security_agent, performance_agent, quality_agent, architect_agent],
    tasks=[security_task, performance_task, quality_task, synthesis_task],
    process=Process.sequential,  # Sequential process, but async tasks run in parallel
    verbose=True
)
```

### Execution Flow

```
Time 0:  security_task starts    ┐
         performance_task starts  ├─ All run in parallel
         quality_task starts      ┘

Time 1:  All parallel tasks complete

Time 2:  synthesis_task starts (has access to all results)

Time 3:  synthesis_task completes
```

### When to Use

- Independent analysis tasks (security, performance, quality)
- Research from multiple sources
- Code reviews from different perspectives
- Data collection from multiple APIs

### Benefits

- Significantly faster execution (3x speedup for 3 parallel tasks)
- Multiple perspectives on same problem
- No waiting for sequential bottlenecks
- Automatic result aggregation

### Performance Comparison

| Workflow | Execution Time | Best For |
|----------|---------------|----------|
| Sequential | N × task_time | Dependent tasks |
| Parallel (3 agents) | max(task_time) + synthesis | Independent analyses |
| Hierarchical | Varies | Complex delegation |

---

## Multi-Agent Collaboration

### Overview

Multiple agents working together with shared context and knowledge.

### Key Patterns

#### 1. Review Chain

```python
# Agent A implements → Agent B reviews → Agent C tests → Agent D documents

implementation = Task(description="Implement feature", agent=developer)
review = Task(description="Review code", agent=reviewer, context=[implementation])
testing = Task(description="Write tests", agent=qa, context=[implementation, review])
docs = Task(description="Document feature", agent=writer, context=[implementation, testing])

crew = Crew(
    agents=[developer, reviewer, qa, writer],
    tasks=[implementation, review, testing, docs],
    process=Process.sequential
)
```

#### 2. Collaborative Research

```python
# Multiple analysts research different aspects, architect synthesizes

aspect1 = Task(description="Research architecture", agent=analyst1, async_execution=True)
aspect2 = Task(description="Research dependencies", agent=analyst2, async_execution=True)
aspect3 = Task(description="Research patterns", agent=analyst3, async_execution=True)

synthesis = Task(
    description="Synthesize findings",
    agent=architect,
    context=[aspect1, aspect2, aspect3]
)

crew = Crew(
    agents=[analyst1, analyst2, analyst3, architect],
    tasks=[aspect1, aspect2, aspect3, synthesis],
    process=Process.sequential
)
```

#### 3. Quality Control Layers

```python
# Multiple reviewers check different aspects

code_review = Task(description="Code quality", agent=code_reviewer, async_execution=True)
security_review = Task(description="Security audit", agent=security_expert, async_execution=True)
perf_review = Task(description="Performance check", agent=perf_expert, async_execution=True)

approval = Task(
    description="Final approval or rejection",
    agent=architect,
    context=[code_review, security_review, perf_review]
)
```

### Context Sharing Best Practices

1. **Use context parameter** for task dependencies:
   ```python
   Task(description="...", agent=agent, context=[previous_task1, previous_task2])
   ```

2. **Enable crew memory** for long-term context:
   ```python
   Crew(agents=[...], tasks=[...], memory=True)
   ```

3. **Use share_knowledge tool** for explicit knowledge transfer:
   ```python
   @tool("share_knowledge")
   def share_knowledge(knowledge_type: str, content: str):
       # Store to crew knowledge base
       return f"Shared: {knowledge_type}"
   ```

---

## Specialized Agent Teams

### Overview

Create teams of agents with complementary skills for complex workflows.

### Team Configurations

#### Development Team (6 agents)

```python
from agents import EnhancedAgentFactory

team = EnhancedAgentFactory.create_development_team()
# Returns: [architect, developer, reviewer, qa, writer, devops]

crew = Crew(
    agents=team,
    tasks=development_tasks,
    process=Process.hierarchical,
    manager_agent=team[0]  # Architect manages
)
```

#### Code Review Team (3 agents)

```python
review_team = EnhancedAgentFactory.create_code_review_team()
# Returns: [reviewer, qa, developer]

crew = Crew(
    agents=review_team,
    tasks=review_tasks,
    process=Process.sequential
)
```

#### Research Team (3 agents)

```python
research_team = EnhancedAgentFactory.create_research_team()
# Returns: [analyst, architect, writer]
```

### Custom Team Creation

```python
class CustomTeamFactory:
    @staticmethod
    def create_security_team():
        return [
            Agent(role="Security Auditor", ...),
            Agent(role="Penetration Tester", ...),
            Agent(role="Security Architect", ...)
        ]

    @staticmethod
    def create_data_team():
        return [
            Agent(role="Data Engineer", ...),
            Agent(role="Data Analyst", ...),
            Agent(role="ML Engineer", ...)
        ]
```

---

## Advanced Task Patterns

### 1. DAG-Based Workflows

Create complex task dependencies:

```python
# Task dependency graph:
#     A
#    / \
#   B   C
#    \ /
#     D

task_a = Task(description="Root task", agent=agent1)
task_b = Task(description="Branch 1", agent=agent2, context=[task_a])
task_c = Task(description="Branch 2", agent=agent3, context=[task_a])
task_d = Task(description="Merge", agent=agent4, context=[task_b, task_c])

crew = Crew(agents=[agent1, agent2, agent3, agent4], tasks=[task_a, task_b, task_c, task_d])
```

### 2. Conditional Tasks

```python
def create_conditional_workflow(needs_security_review: bool):
    tasks = [design_task, implementation_task]

    if needs_security_review:
        security_task = Task(
            description="Security audit",
            agent=security_agent,
            context=[implementation_task]
        )
        tasks.append(security_task)

    tasks.append(deployment_task)
    return tasks
```

### 3. Iterative Refinement

```python
# Implement → Review → Refine loop

for iteration in range(3):
    impl_task = Task(description=f"Implementation iteration {iteration}", ...)
    review_task = Task(description=f"Review iteration {iteration}", context=[impl_task], ...)

    crew = Crew(agents=[developer, reviewer], tasks=[impl_task, review_task])
    result = crew.kickoff()

    if "APPROVED" in result:
        break
```

---

## Memory and Context Sharing

### Crew-Level Memory

```python
# Enable persistent memory across tasks
crew = Crew(
    agents=[agent1, agent2, agent3],
    tasks=[task1, task2, task3],
    memory=True,  # KEY: Enables shared memory
    verbose=True
)

# Agents can now access previous task results automatically
```

### Task-Level Context

```python
# Explicit context passing
task2 = Task(
    description="Build on previous work",
    agent=agent2,
    context=[task1],  # Has access to task1's output
    expected_output="Enhanced result"
)

task3 = Task(
    description="Synthesize multiple inputs",
    agent=agent3,
    context=[task1, task2],  # Has access to both
    expected_output="Final synthesis"
)
```

### Knowledge Sharing Tool

```python
# Custom tool for explicit knowledge sharing
@tool("share_knowledge")
def share_knowledge(knowledge_type: str, content: str) -> str:
    """
    Share knowledge with other agents in the crew.

    Args:
        knowledge_type: Category (finding, decision, recommendation)
        content: The knowledge to share

    Returns:
        Confirmation message
    """
    # In production, store to database or crew memory
    return f"[Knowledge Shared] {knowledge_type}: {content}"

# Agents can use this tool to explicitly share insights
agent = Agent(
    role="Analyst",
    tools=[read_file, share_knowledge],  # Include knowledge sharing
    ...
)
```

---

## Performance Optimization

### 1. Use Parallel Execution for Independent Tasks

```python
# BAD: Sequential (slow)
tasks = [
    Task(description="Security scan", agent=agent1),
    Task(description="Performance test", agent=agent2),
    Task(description="Quality check", agent=agent3)
]

# GOOD: Parallel (3x faster)
tasks = [
    Task(description="Security scan", agent=agent1, async_execution=True),
    Task(description="Performance test", agent=agent2, async_execution=True),
    Task(description="Quality check", agent=agent3, async_execution=True)
]
```

### 2. Minimize Context Size

```python
# BAD: Large context
task = Task(
    description="Final summary",
    context=[task1, task2, task3, task4, task5, task6],  # Too much context
    ...
)

# GOOD: Filtered context
relevant_tasks = [task for task in all_tasks if task.is_relevant()]
task = Task(
    description="Final summary",
    context=relevant_tasks,  # Only relevant context
    ...
)
```

### 3. Choose Right Process Type

| Process Type | When to Use | Performance |
|--------------|-------------|-------------|
| Sequential | Linear workflows, context dependencies | Good |
| Hierarchical | Complex delegation, quality control | Variable |
| Sequential + async tasks | Mix of parallel and sequential | Best |

### 4. Optimize Agent Tools

```python
# BAD: Give all agents all tools
agent = Agent(role="Reviewer", tools=[all_tools])  # Slow

# GOOD: Give only necessary tools
agent = Agent(
    role="Reviewer",
    tools=[read_file, analyze_code_quality]  # Fast, focused
)
```

---

## Comparison: SDK vs Enhanced CrewAI

| Aspect | SDK | Basic CrewAI | Enhanced CrewAI |
|--------|-----|--------------|-----------------|
| Agents per workflow | 1 | 1-3 | 3-7 |
| Execution model | Sequential | Sequential | Hierarchical + Parallel |
| Task delegation | Manual | Manual | Automatic |
| Context sharing | Session-based | Task-based | Multi-level (task + crew) |
| Specialization | General | Moderate | High (role-specific) |
| Workflow complexity | Simple | Medium | Complex (DAG-based) |
| Team simulation | No | Basic | Realistic |
| Performance | Good | Good | Excellent (parallel) |

---

## Best Practices

1. **Use hierarchical process for complex projects** - Let a manager agent coordinate
2. **Parallelize independent analyses** - Significant speed improvement
3. **Create specialized agents** - Better results than general-purpose agents
4. **Share context explicitly** - Use context parameter and knowledge tools
5. **Start simple, add complexity** - Begin with sequential, add parallel/hierarchical as needed
6. **Monitor agent interactions** - Use verbose=True during development
7. **Optimize tool assignments** - Give agents only the tools they need

---

## Troubleshooting

### Hierarchical delegation not working
- Ensure manager has `allow_delegation=True`
- Use `Process.hierarchical` not `Process.sequential`
- Set `manager_agent` parameter in Crew

### Parallel tasks running sequentially
- Set `async_execution=True` on tasks
- Check for unintended dependencies in `context`
- Verify agents are independent

### Context not propagating
- Use `context=[previous_task]` parameter
- Enable crew memory: `memory=True`
- Check task order matches dependency graph

### Poor performance
- Use parallel execution for independent tasks
- Minimize context size
- Assign minimal tool sets to agents
- Consider caching for repeated operations

---

## Further Reading

- [Basic SDK Migration](../claude-agent-basic-agent488/CREWAI_UPGRADE.md)
- [Hybrid Approach](../claude-agent-hybrid-agent490/CREWAI_UPGRADE.md)
- [CrewAI Official Docs](https://docs.crewai.com)

---

*Advanced features guide for Enhanced Multi-Agent System*
*Part of Claude Code Agent → CrewAI migration suite*
