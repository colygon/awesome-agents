# JCrewAI - TypeScript Multi-Agent Framework

**Gallery ID:** 491
**Category:** CrewAI Framework Implementation
**Language:** TypeScript/JavaScript

## Overview

JCrewAI is a TypeScript/JavaScript implementation of the multi-agent automation framework inspired by the Python-based CrewAI project. It enables developers to build systems where multiple AI agents collaborate to accomplish complex tasks through coordinated automation in the Node.js ecosystem.

## External Repository

This is a reference to an external project. For full source code, examples, and documentation:

**Repository:** https://github.com/rmtuckerphx/jcrewai
**Author:** Mark Tucker
**License:** MIT

## Key Features

- **Multi-Agent Support** - Create "Crews" (groups of agents) that work together on complex tasks
- **Agent Configuration** - Define agent roles, goals, and capabilities through YAML configuration
- **Task Management** - Specify and orchestrate tasks for agent collaboration
- **OpenAI Integration** - Direct integration with OpenAI as the LLM provider
- **Modular Architecture** - Clean separation with BaseAgent, BaseLlm, and BaseTask abstractions
- **YAML Configuration** - Configuration-driven agent and task setup
- **TypeScript Support** - Full TypeScript support with decorators and type safety

## Getting Started

Visit the official repository for installation instructions and examples:

```bash
npm install jcrewai
```

Full documentation: https://github.com/rmtuckerphx/jcrewai

## Example Usage

```typescript
import { Crew, Agent, Task } from 'jcrewai';

// Create agents via YAML configuration
// See repository for complete examples
```

## Development Status

- **Version:** 0.1.0 (Early-stage development)
- **Current Support:** OpenAI LLM provider
- **In Progress:** Tool integration infrastructure
- **Planned:** Additional LLM providers, Flows feature

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - Python CrewAI migration example
- [Claude Agent Enhanced (agent489)](../claude-agent-enhanced-agent489/) - Advanced multi-agent workflows
- [Claude Agent Hybrid (agent490)](../claude-agent-hybrid-agent490/) - Hybrid SDK approach
- [CrewAI-TS (agent492)](../crewai-ts-agent492/) - Alternative TypeScript implementation
- [CrewAI-JS (agent493)](../crewai-js-agent493/) - JavaScript/TypeScript SDK

## Credits

**Author:** Mark Tucker
**License:** MIT
**Framework:** CrewAI TypeScript Port
**Repository:** https://github.com/rmtuckerphx/jcrewai
