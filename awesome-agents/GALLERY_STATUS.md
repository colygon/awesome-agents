# Awesome Agents Gallery Status

**Last Updated:** 2025-12-22

## Overview

The Awesome Agents gallery is a curated collection of AI agents, CrewAI applications, and multi-agent systems.

### Statistics

- **Total Apps:** 425
- **Apps with CrewAI:** 97 (22.8%)
- **Apps without CrewAI:** 328 (77.2%)
- **Apps with Valid Images:** 425 (100%)
- **Apps with Valid GitHub URLs:** 414 (97.4%)

## Recent Additions

### Latest App
- **GOAT SDK CrewAI Solana Agent** (ID: 498)
  - Autonomous blockchain querying with CrewAI + GOAT SDK
  - Solana SPL token intelligence
  - 70+ blockchain plugin integrations

### Recent MCP Integrations
- CrewAI-MCP Research Assistant (ID: 494)
- Claude-CrewAI-MCP Server (ID: 495)
- MCP Crew AI Server (ID: 496)
- 21st.dev Magic AI Agent (ID: 497)

## Category Breakdown

| Category | Total Apps | With CrewAI | CrewAI % |
|----------|------------|-------------|----------|
| Streamlit | 133 | 0 | 0% |
| ADK | 107 | 18 | 16.8% |
| Tools | 75 | 0 | 0% |
| CrewAI | 61 | 61 | 100% |
| TypeScript | 12 | 12 | 100% |
| Swarm | 11 | 0 | 0% |
| LangGraph | 11 | 0 | 0% |
| MCP | 4 | 4 | 100% |
| AutoGen | 4 | 0 | 0% |
| LangChain | 3 | 0 | 0% |
| Vertex AI | 2 | 0 | 0% |
| Llama | 2 | 2 | 100% |

## CrewAI Migration Status

### ADK Apps (107 total)
- **Migrated:** 18 apps (16.8%)
- **In Progress:** 89 apps (83.2%)
- **Target:** Migrate all 107 ADK apps to CrewAI

### Implementation Files Created
- 90+ directories with full CrewAI implementations
- Each includes: agents.py, tasks.py, tools.py, main.py, requirements.txt, .env.example, README_CREWAI.md

## Features Implemented

### ✅ Gallery Review System
- **9 parallel review agents** processing all 425 apps
- Validates GitHub URLs (414/425 valid)
- Ensures all apps have images (425/425 complete)
- Identifies apps needing manual review

### ✅ Upgrade Button
- **On-demand CrewAI upgrades** for any app
- Click "⚡ Upgrade to CrewAI" on any non-CrewAI app
- Automatically clones repo and creates CrewAI implementation
- Updates database when complete

### ✅ Submit Form
- **Conversational UI** for submitting new apps
- Automatically detects framework (LangGraph, AutoGen, Swarm, etc.)
- Generates upgrade recommendations
- Adds CrewAI support automatically

## Apps Needing Attention

### Invalid GitHub URLs (11 apps)
These repositories return 404 errors and may need updating:

1. App 77: MathGPT
2. App 86: Gita GPT
3. App 106: Arup Social Data
4. App 109: McLachApp
5. App 111: BERT Semantic Interlinking App
6. App 114: rephraise
7. App 156: SEO A/B Test Analyzer
8. App 159: Digitálny ŠVP
9. App 202: Resource Finder
10. App 205: Sparky A Free AI Powered Chat Bot
11. App 207: The Distance Predictor

**Action Needed:** Verify if these repos moved, were renamed, or should be removed.

## Migration Opportunities

### Framework Distribution (Non-CrewAI Apps)

**High Priority for Migration:**
- **Streamlit Apps:** 133 apps ready for CrewAI upgrades
- **Agent Tools:** 75 tools that could integrate with CrewAI
- **Swarm Apps:** 11 apps (easy migration path)
- **LangGraph Apps:** 11 apps (graph-based workflows map well to CrewAI)
- **AutoGen Apps:** 4 apps (conversational patterns)

**Migration Benefits:**
- Multi-agent orchestration
- Task-based workflows
- Tool integration
- Better observability
- Structured agent roles

## Technical Infrastructure

### Database Schema
```sql
CREATE TABLE apps (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  description TEXT,
  github_url TEXT,
  tags TEXT,
  watchers INTEGER DEFAULT 0,
  views INTEGER DEFAULT 0,
  image_url TEXT,
  has_crewai INTEGER DEFAULT 0,
  category TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### API Endpoints
- `GET /api/apps` - List all apps with search/filter
- `POST /api/apps` - Submit new app
- `POST /api/upgrade` - Trigger CrewAI upgrade

### Scripts
- `sync.js` - Sync apps from external sources
- `review-agent.js` - Validate and review gallery apps
- `upgrade-agent.js` - Create CrewAI implementations

## Usage

### Running the Gallery

```bash
# Install dependencies
npm install

# Sync external app listings
npm run sync

# Start the development server
npm run dev
```

Then open http://localhost:3000

### Submitting an App

1. Visit http://localhost:3000/submit
2. Answer the conversational questions
3. Provide GitHub URL, title, description
4. Agent automatically reviews code and suggests CrewAI upgrade

### Upgrading an App

1. Browse the gallery
2. Find an app without the "🤖 CrewAI" badge
3. Click "⚡ Upgrade to CrewAI"
4. Upgrade agent creates full implementation in background

## Roadmap

### Completed ✅
- [x] Rename to Awesome Agents
- [x] Add CrewAI filter toggle
- [x] Implement upgrade button UI
- [x] Create automated review system
- [x] Generate missing images
- [x] Validate GitHub URLs
- [x] Add MCP integrations

### In Progress 🚧
- [ ] Complete ADK app migrations (18/107 done)
- [ ] Verify apps with invalid URLs
- [ ] Add more MCP servers

### Future Enhancements 💡
- [ ] Migrate all Streamlit apps (133 apps)
- [ ] Migrate LangGraph apps (11 apps)
- [ ] Migrate Swarm apps (11 apps)
- [ ] Add live demo links
- [ ] Implement app ratings/favorites
- [ ] Add search by framework capabilities
- [ ] Create comparison views
- [ ] Add deployment guides

## Contributing

To add a new app to the gallery:

1. **Via Submit Form:** http://localhost:3000/submit
2. **Via sync.js:** Add to `sync.config.json` feeds
3. **Manual:** Direct database insert

## Credits

**Gallery System:** Built with Next.js, React, SQLite
**Agents:** Powered by CrewAI
**Automation:** Claude Code Agent SDK
**Framework:** Model Context Protocol (MCP)

## Resources

- [CrewAI Documentation](https://docs.crewai.com)
- [MCP Protocol](https://modelcontextprotocol.io)
- [GOAT SDK](https://ohmygoat.dev)
- [Google ADK](https://cloud.google.com/products/agent-development-kit)

---

**Note:** This gallery is actively maintained and continuously expanding. Apps are regularly reviewed, validated, and upgraded to use the latest multi-agent frameworks.
