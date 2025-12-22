# CAMEL Multi-Agent Framework - CrewAI Implementation

**C**ommunicative **A**gents for **M**ind **E**xploration of **L**arge Language Models

A role-playing multi-agent framework where AI agents collaborate through structured communication and reasoning to solve complex tasks.

## Overview

CAMEL implements a novel approach to multi-agent collaboration where agents take on distinct roles and communicate to achieve shared objectives. This CrewAI implementation brings the CAMEL framework's role-playing paradigm to practical task execution.

### Core Concept

CAMEL uses role-playing to enable autonomous cooperation between agents:
- **AI User Agent**: Provides requirements, guidance, and validation
- **AI Assistant Agent**: Proposes and implements solutions
- **AI Critic Agent**: Evaluates quality and provides constructive feedback

This creates a collaborative loop that mirrors human teamwork patterns.

### Agents

1. **AI User Agent** (Configurable Role)
   - Default: Product Manager, Project Lead, Researcher
   - Responsibilities:
     - Define requirements and specifications
     - Guide the collaboration process
     - Validate final solutions
     - Provide strategic direction
   - Tools: Web search for requirements research

2. **AI Assistant Agent** (Configurable Role)
   - Default: Software Engineer, Data Analyst, Designer
   - Responsibilities:
     - Understand and clarify requirements
     - Propose and implement solutions
     - Refine solutions based on feedback
     - Deliver high-quality outputs
   - Tools: Web search, file reading

3. **AI Critic Agent** (Quality Assurance)
   - Role: Solution evaluator and quality assurance
   - Responsibilities:
     - Evaluate solutions objectively
     - Identify weaknesses and edge cases
     - Provide constructive feedback
     - Ensure quality standards
   - Tools: None (focuses on evaluation)

## Features

- **Flexible Role Assignment**: Customize agent roles for any domain
- **Structured Collaboration**: 5-phase workflow ensures thorough solutions
- **Iterative Refinement**: Solutions improve through critique and refinement
- **Domain Agnostic**: Works for software, research, business, design, etc.
- **Quality Assurance**: Built-in critic ensures high-quality outputs
- **Autonomous Cooperation**: Agents collaborate without human intervention

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys
```

## Configuration

Required API keys:
- `OPENAI_API_KEY`: OpenAI API key for GPT-4

Optional:
- `SERPER_API_KEY`: Serper API key for web search

## Usage

### Command Line

```bash
python main.py
```

Follow the interactive prompts to:
1. Define your task description
2. Specify the task domain
3. Choose roles for user and assistant agents
4. Watch agents collaborate
5. Save the collaboration output

### Python API

```python
from main import run_camel_collaboration, save_collaboration_output

# Run collaboration with custom roles
result = run_camel_collaboration(
    task_description="Design a microservices architecture for an e-commerce platform",
    task_domain="software architecture",
    user_role="Solutions Architect",
    assistant_role="Senior Backend Engineer"
)

# Access different phases
print(result["requirements"])
print(result["initial_solution"])
print(result["critique"])
print(result["final_solution"])
print(result["validation"])

# Save complete collaboration
save_collaboration_output(result["validation"], "collaboration-output.md")
```

## Collaboration Workflow

### Phase 1: Requirements Definition
**Agent**: AI User Agent

The user agent analyzes the task and creates a detailed requirements specification including:
- Specific requirements and objectives
- Success criteria
- Constraints and considerations
- Scope and deliverables

### Phase 2: Solution Proposal
**Agent**: AI Assistant Agent

The assistant agent develops an initial solution:
- Addresses all requirements
- Explains approach and methodology
- Outlines implementation steps
- Identifies potential challenges
- Provides concrete examples

### Phase 3: Critical Evaluation
**Agent**: AI Critic Agent

The critic evaluates the solution:
- Identifies strengths
- Points out weaknesses and gaps
- Highlights edge cases
- Suggests improvements
- Provides quality rating

### Phase 4: Solution Refinement
**Agent**: AI Assistant Agent

The assistant refines the solution:
- Addresses critique feedback
- Implements suggested improvements
- Handles identified edge cases
- Mitigates risks
- Enhances clarity and completeness

### Phase 5: Final Validation
**Agent**: AI User Agent

The user agent validates the refined solution:
- Verifies requirement fulfillment
- Assesses quality and completeness
- Confirms alignment with objectives
- Provides final approval

## Example Use Cases

### Software Development
```python
result = run_camel_collaboration(
    task_description="Build a RESTful API for a todo application with authentication",
    task_domain="software development",
    user_role="Product Manager",
    assistant_role="Backend Developer"
)
```

### Research
```python
result = run_camel_collaboration(
    task_description="Design an experimental study on AI decision-making biases",
    task_domain="AI research",
    user_role="Research Lead",
    assistant_role="Research Scientist"
)
```

### Business Strategy
```python
result = run_camel_collaboration(
    task_description="Develop a go-to-market strategy for a B2B SaaS product",
    task_domain="business strategy",
    user_role="CEO",
    assistant_role="Marketing Director"
)
```

### Data Analysis
```python
result = run_camel_collaboration(
    task_description="Create a customer segmentation model using clustering",
    task_domain="data science",
    user_role="Data Science Manager",
    assistant_role="Data Scientist"
)
```

## Recommended Role Combinations

### Software Development
- Product Manager → Software Engineer
- Tech Lead → Developer
- Solutions Architect → Backend Engineer
- UX Designer → Frontend Developer

### Research
- Research Lead → Research Scientist
- Principal Investigator → Postdoc Researcher
- Lab Director → Research Assistant

### Business
- CEO → Marketing Director
- VP Sales → Sales Manager
- CFO → Financial Analyst
- COO → Operations Manager

### Design
- Creative Director → Graphic Designer
- UX Lead → UI Designer
- Brand Manager → Content Designer

## Key Advantages of CAMEL Framework

1. **Autonomous Cooperation**: Agents collaborate without human intervention
2. **Role Specialization**: Each agent has clear responsibilities
3. **Iterative Improvement**: Solutions improve through feedback loops
4. **Quality Assurance**: Built-in evaluation ensures high standards
5. **Scalability**: Easily adaptable to new domains and roles
6. **Transparency**: Full visibility into agent reasoning and decisions

## Migration from ADK

### Key Changes

| ADK Component | CrewAI Equivalent |
|---------------|-------------------|
| CAMEL user agent | Configurable AI User Agent |
| CAMEL assistant agent | Configurable AI Assistant Agent |
| Evaluation system | AI Critic Agent |
| Role-playing loop | Sequential task workflow |
| Gemini model | OpenAI GPT-4 |

### Architecture Differences

- **ADK**: Uses CAMEL's original role-playing framework
- **CrewAI**: Implements role-playing through agent backstories and tasks
- **LLM**: Migrated from Google Gemini to OpenAI GPT-4
- **Communication**: Task context passing instead of direct agent messaging

## Research Background

CAMEL is based on the research paper:

**"CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society"**

The framework demonstrates that:
- LLMs can engage in autonomous cooperation through role-playing
- Structured communication improves task completion quality
- Multiple agents can outperform single-agent approaches
- Role specialization enables more effective collaboration

## Best Practices

### Choosing Roles
- Select roles that naturally collaborate in the real world
- Ensure complementary skill sets
- Consider power dynamics and hierarchy
- Match roles to task complexity

### Task Description
- Be specific about objectives
- Include relevant constraints
- Specify desired output format
- Provide necessary context

### Domain Selection
- Choose domains where roles have clear responsibilities
- Ensure domain expertise exists in training data
- Consider task complexity relative to domain

## Limitations

- Quality depends on LLM capabilities
- May require multiple iterations for complex tasks
- Agent "personalities" can vary between runs
- Not suitable for tasks requiring real-time interaction
- Limited by training data for specialized domains

## Future Enhancements

- Support for more than 3 agents
- Parallel collaboration tracks
- Memory persistence across sessions
- Custom evaluation criteria
- Integration with external tools and APIs
- Real-time collaboration monitoring
- Multi-modal agent capabilities

## Original Research

CAMEL framework based on research from:
- Li, Guohao, et al. "CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Model Society." (2023)

## License

Apache License 2.0
