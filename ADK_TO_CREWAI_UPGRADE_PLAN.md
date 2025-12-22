# Google ADK → CrewAI Migration Plan

**Date:** December 21, 2025
**Apps to Upgrade:** 30 Google ADK sample agents
**Source:** https://github.com/google/adk-samples (7.7K stars)
**Goal:** Migrate from Google Agent Development Kit to CrewAI framework

---

## Apps Added to Gallery

**Total:** 30 sample agents (IDs 381-410)
**Categories:** Python (26), Java (2), TypeScript (1), Go (1)

| ID Range | Language | Count | Examples |
|----------|----------|-------|----------|
| 381-406 | Python | 26 | Academic Research, Blog Writer, Financial Advisor |
| 407-408 | Java | 2 | Bug Assistant, Time Series Forecasting |
| 409 | TypeScript | 1 | Customer Service |
| 410 | Go | 1 | LLM Auditor |

---

## Gallery Statistics

- **Total apps:** 337
- **ADK apps:** 30 (new)
- **Eliza apps:** 7 (migration in progress)
- **CrewAI apps:** 37 (from previous upgrades)

---

## Migration Strategy

### Phase 1: Categorize by Pattern

#### Category A: RAG/Search Agents (6 apps)
- **IDs:** 381, 390, 392, 401
- Academic Research, FOMC Research, Deep Search, RAG Agent
- **Pattern:** Document retrieval → CrewAI RAG agents
- **Agents needed:** 3 (Indexer, Query Processor, Synthesizer)

#### Category B: Domain-Specific Assistants (12 apps)
- **IDs:** 383, 386, 387, 388, 389, 393, 396, 397, 398, 399, 405, 406
- Blog Writer, Customer Service, Data Engineering, Financial Advisor, etc.
- **Pattern:** Task-specific workflows → CrewAI specialist agents
- **Agents needed:** 2-3 per app

#### Category C: Multi-Agent Systems (3 apps)
- **IDs:** 385, 391, 404
- CAMEL, Gemini Fullstack, Short Movie Agents
- **Pattern:** Complex coordination → CrewAI crews with hierarchical process
- **Agents needed:** 4-5 per app

#### Category D: Real-time/Interactive (2 apps)
- **IDs:** 402, 376 (from Eliza)
- Realtime Conversational Agent
- **Pattern:** Low-latency responses → Async CrewAI agents
- **Agents needed:** 2-3 per app

#### Category E: Specialized Tools (7 apps)
- **IDs:** 382, 384, 394, 395, 400, 403, 407, 408, 409, 410
- Payment, SEO, Image Scoring, LLM Audit, Safety, etc.
- **Pattern:** Tool-based workflows → CrewAI with custom tools
- **Agents needed:** 2 per app

---

## ADK → CrewAI Concept Mapping

| ADK Concept | CrewAI Equivalent |
|-------------|-------------------|
| **ADK Agent** | CrewAI Agent (with role, goal, backstory) |
| **ADK Task** | CrewAI Task (with description, expected_output) |
| **ADK Tool** | CrewAI Tool (function-based or class-based) |
| **ADK Workflow** | CrewAI Crew (with Process.sequential or hierarchical) |
| **ADK Memory** | CrewAI Memory (short-term, long-term, entity) |
| **Google Gemini** | OpenAI GPT-4 or other LLM via LangChain |
| **ADK Plugins** | CrewAI Tools or custom integrations |
| **ADK Context** | CrewAI Agent context and crew shared state |

---

## Migration Approach by Language

### Python ADK → CrewAI (26 apps)
**Difficulty:** Medium
**Reason:** Both Python-based, straightforward translation

**Steps:**
1. Map ADK agents to CrewAI agents
2. Convert ADK tasks to CrewAI tasks
3. Translate Google Gemini calls to OpenAI/LangChain
4. Implement CrewAI crew orchestration
5. Maintain original functionality

### Java ADK → CrewAI Python (2 apps)
**Difficulty:** Hard
**Reason:** Cross-language migration

**Steps:**
1. Rewrite core logic in Python
2. Map Java ADK concepts to CrewAI Python
3. Use Python equivalents for Java libraries
4. Ensure feature parity

### TypeScript/Go → CrewAI Python (2 apps)
**Difficulty:** Hard
**Reason:** Cross-language migration

**Similar approach to Java migration**

---

## Sample Migrations by Category

### Example 1: Blog Writer Agent (383)

**Current ADK Approach:**
```python
# ADK version
from adk import Agent, Task

blog_agent = Agent(
    name="BlogWriter",
    model="gemini-2.0-flash"
)

research_task = Task(
    description="Research topic",
    agent=blog_agent
)
```

**CrewAI Approach:**
```python
from crewai import Agent, Task, Crew

# Research Agent
researcher = Agent(
    role="Content Researcher",
    goal="Research topics and gather information",
    backstory="Expert at finding relevant sources"
)

# Writer Agent
writer = Agent(
    role="Blog Writer",
    goal="Write engaging blog posts",
    backstory="Professional content creator"
)

# Editor Agent
editor = Agent(
    role="Content Editor",
    goal="Polish and refine content",
    backstory="Experienced editor"
)

# Create crew
blog_crew = Crew(
    agents=[researcher, writer, editor],
    process=Process.sequential
)
```

### Example 2: RAG Agent (401)

**Migration Pattern:**
- ADK retrieval → CrewAI RAG with vector stores
- ADK context → CrewAI agent memory
- Gemini → OpenAI with LangChain embeddings

### Example 3: CAMEL Multi-Agent (385)

**Migration Pattern:**
- Multiple ADK agents → Multiple CrewAI agents
- ADK collaboration → CrewAI hierarchical process
- Task distribution → CrewAI task delegation

---

## Batch Assignment for Parallel Execution

### Batch 22-27: Python ADK Apps (6 batches × 4-5 apps each)

**Batch 22 - RAG/Research (IDs 381, 390, 392, 401):**
- Academic Research, FOMC Research, Deep Search, RAG Agent
- Estimated time: 3 hours

**Batch 23 - Business Agents (IDs 383, 389, 397, 399):**
- Blog Writer, Financial Advisor, Marketing Agency, Shopping Agent
- Estimated time: 3 hours

**Batch 24 - Data/Engineering (IDs 387, 388, 396, 400):**
- Data Engineering, Data Science, ML Engineering, Plumber DE
- Estimated time: 3 hours

**Batch 25 - Support/Service (IDs 386, 393, 398, 405):**
- Customer Service, Trends Agent, Medical Pre-Auth, Bug Assistant
- Estimated time: 3 hours

**Batch 26 - Multi-Agent/Complex (IDs 385, 391, 402, 404):**
- CAMEL, Gemini Fullstack, Realtime Chat, Movie Agents
- Estimated time: 4 hours

**Batch 27 - Specialized Tools (IDs 382, 384, 394, 395, 403, 406):**
- Payment, SEO, Image Scoring, LLM Auditor, Safety, Travel
- Estimated time: 3 hours

### Batch 28: Cross-Language (IDs 407-410)
- Java: Bug Assistant, Time Series
- TypeScript: Customer Service
- Go: LLM Auditor
- Estimated time: 5 hours (complex cross-language)

---

## Technical Challenges & Solutions

### Challenge 1: Google Gemini → OpenAI Migration
**Solution:**
- Use LangChain abstraction layer
- Replace Gemini calls with OpenAI GPT-4
- Maintain similar prompt structures
- Test for quality parity

### Challenge 2: ADK-Specific Features
**Solution:**
- Map ADK features to CrewAI equivalents
- Create custom tools where needed
- Document differences

### Challenge 3: Cross-Language Migrations (Java, TS, Go)
**Solution:**
- Rewrite core logic in Python
- Use Python libraries for equivalent functionality
- Ensure feature parity through testing
- Create comprehensive migration docs

### Challenge 4: Multi-Agent Coordination (CAMEL, etc.)
**Solution:**
- Use CrewAI hierarchical process
- Implement manager agent for coordination
- Map ADK agent interactions to CrewAI delegation

---

## Success Metrics

For each migrated app:
- ✅ Core functionality preserved
- ✅ CrewAI agents properly defined (2-5 agents)
- ✅ Sequential or hierarchical workflow implemented
- ✅ Performance comparable to ADK version
- ✅ Comprehensive documentation
- ✅ Migration guide created
- ✅ Tests passing

---

## Expected Outputs Per App

1. **Working Directory:** `/Users/colinlowenberg/crew/{app-name}-agent{id}/`
2. **CrewAI Implementation:**
   - `agents.py` - Agent definitions
   - `tasks.py` - Task workflows
   - `tools.py` - Custom tools (if needed)
   - `crews.py` - Crew orchestration
   - `requirements.txt` - Dependencies (crewai>=0.86.0, langchain-openai>=0.3.0)
3. **Documentation:**
   - `README_CREWAI.md` - CrewAI version guide
   - `MIGRATION_GUIDE.md` - ADK → CrewAI migration notes
   - `COMPLETION_REPORT.md` - Upgrade summary
4. **Git Commit:** With proper Claude Code attribution

---

## Execution Timeline

### Parallel Execution (Recommended)

- **Total batches:** 7 (Batch 22-28)
- **Apps per batch:** 4-6
- **Estimated time:** 4-5 hours parallel
- **Sequential time:** 90-110 hours
- **Speedup:** ~20-25x

### Phased Approach (Alternative)

**Phase 1:** Python RAG/Research apps (Batch 22) - 3 hours
**Phase 2:** Python Business apps (Batch 23) - 3 hours
**Phase 3:** Python Data/Engineering (Batch 24) - 3 hours
**Phase 4:** Remaining Python apps (Batches 25-27) - 10 hours
**Phase 5:** Cross-language apps (Batch 28) - 5 hours

---

## Next Steps

1. **Review and approve** this migration plan
2. **Launch batch agents** for ADK → CrewAI migration (7 batches)
3. **Monitor progress** (~4-5 hours)
4. **Collect results** and update gallery
5. **Generate completion report**
6. **Announce** first Google ADK → CrewAI migration!

---

**Total Apps:** 30
**Estimated Total Time:** 90-110 hours sequential, 4-5 hours parallel
**Expected Success Rate:** 75-85% (cross-language migrations are harder)
**Impact:** First comprehensive ADK → CrewAI migration, establishes migration patterns

---

**Status:** Ready for execution
**Priority:** After Eliza migrations complete
**Generated:** December 21, 2025
