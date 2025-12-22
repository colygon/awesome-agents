# CrewAI-TS - TypeScript Agent Orchestration

**Gallery ID:** 492
**Category:** CrewAI Framework Implementation
**Language:** TypeScript

## Overview

CrewAI-TS is a community-driven TypeScript port of the Python CrewAI framework. It brings multi-agent orchestration capabilities to JavaScript environments, allowing developers to create role-based autonomous agents that work collaboratively on complex tasks.

## External Repository

This is a reference to an external project. For full source code, examples, and documentation:

**Repository:** https://github.com/shmck/crewai-ts
**License:** MIT
**Status:** Actively maintained (v0.0.1)

## Key Features

- **Agent Framework** - Role-based autonomous agents with customizable personalities and goals
- **Task Management** - Contextual task execution with Zod schema validation and file output support
- **Crew Orchestration** - Supports both sequential and hierarchical execution patterns
- **LLM Integration** - Compatible with OpenAI and Anthropic, extensible ChatLLM interface
- **Agent Memory** - Chat history tracking for context retention
- **Tool Support** - LLM-based tool invocation through JSON output parsing
- **Type Safety** - Full TypeScript support with Zod schema validation
- **Modular Design** - Separate modules for agents, tasks, crew, LLMs, and tools

## Getting Started

Visit the official repository for installation instructions and examples:

```bash
npm install crewai-ts
# or
pnpm add crewai-ts
```

**Requirements:** Node.js ≥22.14.0

Full documentation: https://github.com/shmck/crewai-ts

## Example Usage

```typescript
import { Agent, Task, Crew, Process } from 'crewai-ts';

// Research & Writing Workflow
const researcher = new Agent({
  role: 'Researcher',
  goal: 'Conduct thorough research',
  // ... configuration
});

const writer = new Agent({
  role: 'Writer',
  goal: 'Create compelling content',
  // ... configuration
});

const crew = new Crew({
  agents: [researcher, writer],
  tasks: [researchTask, writingTask],
  process: Process.Sequential
});

await crew.kickoff();
```

## Roadmap

- Expanded LLM provider support (Ollama, Google Gemini, Cohere)
- Enriched tool libraries
- Human-in-the-loop capabilities
- Enhanced telemetry with privacy standards
- Broader feature parity with Python CrewAI

## Development Tools

- **Testing:** Vitest with coverage
- **Linting & Formatting:** BiomeJS
- **Type Checking:** TypeScript strict mode
- **Git Hooks:** Husky for pre-commit checks

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - Python CrewAI migration example
- [Claude Agent Enhanced (agent489)](../claude-agent-enhanced-agent489/) - Advanced multi-agent workflows
- [Claude Agent Hybrid (agent490)](../claude-agent-hybrid-agent490/) - Hybrid SDK approach
- [JCrewAI (agent491)](../jcrewai-agent491/) - Alternative TypeScript implementation
- [CrewAI-JS (agent493)](../crewai-js-agent493/) - JavaScript/TypeScript SDK

## Credits

**Repository:** https://github.com/shmck/crewai-ts
**License:** MIT
**Framework:** CrewAI TypeScript Port
**Created:** May 18, 2025
**Status:** Early-stage development
