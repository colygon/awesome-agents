# CrewAI-JS - JavaScript SDK for Multi-Agent AI

**Gallery ID:** 493
**Category:** CrewAI Framework Implementation
**Language:** JavaScript/TypeScript

## Overview

CrewAI-JS is an unofficial JavaScript/TypeScript SDK that brings the CrewAI multi-agent framework to the JavaScript ecosystem. It enables developers to build sophisticated multi-agent AI systems in Node.js and browser environments, filling a gap in the JavaScript ecosystem for LLM-powered agent orchestration.

## External Repository

This is a reference to an external project. For full source code, examples, and documentation:

**Repository:** https://github.com/codewithbro95/crewai-js
**License:** MIT
**Status:** Early-stage development (v0.0.1)

## Key Features

- **Agent-Based Architecture** - Autonomous AI entities powered by LLMs (GPT-3.5, GPT-4)
- **Task Management** - Define specific objectives and goals for agents
- **Crew Coordination** - Multi-agent collaboration and orchestration
- **Modular Design** - Clean separation of agents, crews, tasks, types, and utilities
- **Extensible** - Built for future LLM support beyond OpenAI
- **Type-Safe** - TypeScript implementations with proper typing

## Getting Started

Visit the official repository for installation instructions and examples:

```bash
npm install crewai-js
```

Full documentation: https://github.com/codewithbro95/crewai-js

## Example Usage

```javascript
import { Agent, Crew, Task } from 'crewai-js';

// Create agents
const agent = new Agent({
  role: 'Assistant',
  goal: 'Help users accomplish tasks',
  // ... configuration
});

// Create tasks
const task = new Task({
  description: 'Complete the objective',
  agent: agent
});

// Create crew
const crew = new Crew({
  agents: [agent],
  tasks: [task]
});

// Execute
await crew.kickoff();
```

## Architecture

The framework is organized into modular components:
- `/src/agents/` - Agent implementation modules
- `/src/crews/` - Crew orchestration systems
- `/src/tasks/` - Task definitions and handling
- `/src/types/` - TypeScript type definitions
- `/src/utils/` - Utility functions and helpers

## Why CrewAI-JS?

- Bridges the gap in JavaScript ecosystem for multi-agent AI orchestration
- Brings proven Python CrewAI patterns to Node.js
- Early-stage project with ambitious roadmap for LLM flexibility
- Active community welcoming contributions
- MIT licensed with full transparency

## Development Status

- **Version:** 0.0.1 (Alpha)
- **Production Ready:** Not yet (active development)
- **Community:** Small but active, seeking contributions
- **Stars:** 28 stars, 4 forks

## Examples

The repository includes example projects demonstrating framework usage:
- Basic agent and crew setup
- Task orchestration patterns
- Multi-agent collaboration

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - Python CrewAI migration example
- [Claude Agent Enhanced (agent489)](../claude-agent-enhanced-agent489/) - Advanced multi-agent workflows
- [Claude Agent Hybrid (agent490)](../claude-agent-hybrid-agent490/) - Hybrid SDK approach
- [JCrewAI (agent491)](../jcrewai-agent491/) - TypeScript multi-agent framework
- [CrewAI-TS (agent492)](../crewai-ts-agent492/) - TypeScript agent orchestration

## Credits

**Repository:** https://github.com/codewithbro95/crewai-js
**License:** MIT
**Framework:** CrewAI JavaScript Port
**Last Updated:** October 2025
**Status:** Early-stage, actively developing
