# Eliza → CrewAI Migration Plan

**Date:** December 21, 2025
**Apps to Upgrade:** 7 ElizaOS applications
**Goal:** Migrate from Eliza framework to CrewAI framework

---

## Apps Added to Gallery

| ID | Title | GitHub | Stars | Pattern |
|----|-------|--------|-------|---------|
| 374 | Eliza Knowledge System | elizaOS/knowledge | 56 | rag_replacement |
| 375 | SWE Agent | elizaOS/SWEagent | 17 | autonomous_agent |
| 376 | Live Video Chat | elizaOS/LiveVideoChat | 74 | real_time_communication |
| 377 | Eliza Framework | elizaOS/eliza | 17,205 | framework_migration |
| 378 | Eliza NextJS Starter | elizaOS/eliza-nextjs-starter | 28 | rag_replacement |
| 379 | The Org | elizaOS/the-org | 41 | multi_agent_coordination |
| 380 | Eliza 3D Hyperfy Starter | elizaOS/eliza-3d-hyperfy-starter | 33 | 3d_mmo_integration |

---

## Migration Strategy

### Phase 1: Analysis
For each app, analyze:
1. **Current Eliza architecture** - identify agents, actions, evaluators
2. **Data flow patterns** - understand how information moves
3. **External integrations** - Discord, Telegram, Twitter, etc.
4. **RAG/Knowledge systems** - document retrieval and embedding approaches

### Phase 2: CrewAI Architecture Design

#### Eliza → CrewAI Mapping:

**Eliza Concepts → CrewAI Equivalents:**
- **Eliza Character** → **CrewAI Agent** with role and backstory
- **Eliza Action** → **CrewAI Task** or **CrewAI Tool**
- **Eliza Evaluator** → **CrewAI Task** with validation logic
- **Eliza Memory** → **CrewAI Memory** (short-term, long-term, entity)
- **Eliza Provider** → **CrewAI LLM** integration
- **Eliza Plugin** → **CrewAI Tool** or custom integration

#### Common Agent Architectures:

**For Knowledge/RAG Apps (374, 378):**
- Document Ingestion Agent
- Query Processor Agent
- Answer Synthesis Agent

**For Autonomous Coding (375):**
- Code Analysis Agent
- Implementation Agent
- Testing & Validation Agent

**For Real-time Communication (376):**
- Conversation Manager Agent
- Media Processing Agent
- Response Generator Agent

**For Framework Migration (377):**
- Multi-agent coordinator
- Platform integration agents
- Workflow orchestration

---

## Upgrade Pattern Details

### Pattern 1: RAG Replacement (Apps 374, 378)

**Current Eliza Approach:**
```typescript
// Eliza uses embeddings + similarity search
const memory = await runtime.messageManager.getMemories({
  roomId,
  count: 10,
  unique: true
});
```

**CrewAI Approach:**
```python
from crewai import Agent, Task, Crew
from crewai_tools import FileReadTool, WebSearchTool

# Document Analyzer
doc_analyzer = Agent(
    role="Document Analyzer",
    goal="Extract and index knowledge from documents",
    tools=[FileReadTool(), WebSearchTool()]
)

# Query Processor
query_processor = Agent(
    role="Query Processor",
    goal="Understand user questions and retrieve relevant context"
)

# Answer Synthesizer
answer_agent = Agent(
    role="Answer Synthesizer",
    goal="Generate accurate responses from retrieved knowledge"
)
```

### Pattern 2: Autonomous Agent (App 375 - SWE Agent)

**Current Eliza Approach:**
```typescript
// Eliza uses actions for code operations
const codeAction = {
  name: "WRITE_CODE",
  handler: async (runtime, message) => {
    // Implementation
  }
};
```

**CrewAI Approach:**
```python
from crewai import Agent, Task, Crew, Process
from crewai.tools import CodeInterpreterTool

# Code Analyst
code_analyst = Agent(
    role="Senior Software Engineer",
    goal="Analyze code requirements and design solutions",
    tools=[CodeInterpreterTool()]
)

# Implementation Agent
implementer = Agent(
    role="Code Implementation Specialist",
    goal="Write clean, tested code based on specifications"
)

# Create sequential workflow
crew = Crew(
    agents=[code_analyst, implementer],
    process=Process.sequential
)
```

### Pattern 3: Real-time Communication (App 376)

**Migration Approach:**
- Keep video/communication infrastructure
- Add CrewAI agents for conversation management
- Implement agent-driven response generation
- Maintain real-time latency requirements

### Pattern 4: Framework Migration (App 377)

**Strategy:**
- Create CrewAI wrapper/compatibility layer
- Migrate core agent logic to CrewAI
- Maintain existing integrations (Discord, Telegram, Twitter)
- Provide migration guide for users

---

## Technical Implementation Plan

### Step 1: Fork Repositories
```bash
gh repo fork elizaOS/knowledge --clone=false --fork-name knowledge --org colygon
gh repo fork elizaOS/SWEagent --clone=false --fork-name SWEagent --org colygon
gh repo fork elizaOS/LiveVideoChat --clone=false --fork-name LiveVideoChat --org colygon
gh repo fork elizaOS/eliza --clone=false --fork-name eliza --org colygon
gh repo fork elizaOS/eliza-nextjs-starter --clone=false --fork-name eliza-nextjs-starter --org colygon
gh repo fork elizaOS/the-org --clone=false --fork-name the-org --org colygon
gh repo fork elizaOS/eliza-3d-hyperfy-starter --clone=false --fork-name eliza-3d-hyperfy-starter --org colygon
```

### Step 2: Clone and Analyze
For each app:
1. Clone to local directory: `{app-name}-agent{id}/`
2. Analyze existing codebase structure
3. Identify key Eliza components to migrate
4. Map to CrewAI equivalents

### Step 3: Implement CrewAI Version

**Files to Create:**
- `agents.py` - CrewAI agent definitions
- `tasks.py` - CrewAI task definitions
- `tools.py` - Custom CrewAI tools (if needed)
- `crews.py` - CrewAI crew orchestration
- `requirements_crewai.txt` - New dependencies
- `README_CREWAI.md` - Migration documentation
- `MIGRATION_GUIDE.md` - For users migrating from Eliza

**Dependencies to Add:**
```
crewai>=0.86.0
langchain-openai>=0.3.0
langchain-community>=0.3.0
python-dotenv>=1.0.0
```

### Step 4: Integration Approach

**Option A: Dual Mode (Recommended for 377)**
- Keep existing Eliza implementation
- Add parallel CrewAI implementation
- Allow users to choose via config flag
- Gradual migration path

**Option B: Full Replacement (For 374, 375, 378)**
- Replace Eliza with CrewAI
- Maintain backward compatibility for APIs
- Provide migration scripts

**Option C: Hybrid (For 376)**
- Keep real-time infrastructure
- Add CrewAI for agent logic
- Best of both worlds

---

## Key Differences: Eliza vs CrewAI

| Feature | Eliza | CrewAI |
|---------|-------|---------|
| **Language** | TypeScript/JavaScript | Python |
| **Agent Definition** | Character files (JSON) | Python classes |
| **Task Execution** | Action handlers | Task objects with descriptions |
| **Memory** | Custom memory manager | Built-in memory (short/long/entity) |
| **Tool System** | Plugins | Tools (Function-based or class-based) |
| **Orchestration** | Custom runtime | Crew with Process types |
| **Integrations** | Discord.js, etc. | LangChain ecosystem |
| **State Management** | Custom | Agent/Crew state |

---

## Migration Challenges & Solutions

### Challenge 1: Language Barrier (TypeScript → Python)
**Solution:**
- Rewrite core logic in Python
- Maintain API compatibility
- Use Python equivalents for TS libraries

### Challenge 2: Real-time Requirements (App 376)
**Solution:**
- Keep low-latency infrastructure
- Use async CrewAI agents
- Implement streaming responses

### Challenge 3: Platform Integrations (Discord, Twitter, etc.)
**Solution:**
- Use Python Discord.py instead of Discord.js
- Leverage existing Python social media libraries
- Maintain feature parity

### Challenge 4: Memory/Context Management
**Solution:**
- Map Eliza memory to CrewAI memory types
- Use vector stores for long-term memory
- Implement context windowing

---

## Success Metrics

For each migrated app:
- ✅ Maintains core functionality
- ✅ CrewAI agents properly defined
- ✅ Sequential/hierarchical workflows implemented
- ✅ External integrations working
- ✅ Comprehensive documentation
- ✅ Migration guide for users
- ✅ Tests passing
- ✅ Performance comparable or better

---

## Execution Timeline

### Batch Assignment

**Batch 16 - Quick Wins (Apps 374, 378):**
- Knowledge System (RAG replacement)
- NextJS Starter (RAG replacement)
- Estimated time: 2-3 hours

**Batch 17 - Autonomous Agent (App 375):**
- SWE Agent (complex autonomous workflow)
- Estimated time: 3-4 hours

**Batch 18 - Real-time (App 376):**
- Live Video Chat (hybrid approach)
- Estimated time: 4-5 hours

**Batch 19 - Framework (App 377):**
- Eliza Framework (most complex, dual-mode)
- Estimated time: 6-8 hours

**Batch 20 - Multi-Agent Coordination (App 379):**
- The Org (5-agent organizational system)
- Estimated time: 3-4 hours

**Batch 21 - 3D/Gaming (App 380):**
- Eliza 3D Hyperfy Starter (3D MMO integration)
- Estimated time: 4-5 hours

---

## Next Steps

1. **Review and approve** this migration plan
2. **Fork repositories** to colygon organization
3. **Launch upgrade agents** for each batch
4. **Monitor progress** and collect results
5. **Update gallery** with migrated apps
6. **Generate completion reports**

---

**Total Apps:** 7
**Estimated Total Time:** 22-30 hours sequential, 4-5 hours parallel
**Expected Success Rate:** 80-90% (based on previous batch results)
**Impact:** First major Eliza → CrewAI migration, establishes pattern for future conversions

---

**Generated:** December 21, 2025
**Status:** Ready for execution
**Approval:** Pending
