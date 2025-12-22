# Awesome Agents

A curated gallery of AI agents, CrewAI applications, and multi-agent systems. Built with Next.js and backed by a local SQLite database (`apps.db`).

This gallery showcases:
- **CrewAI Applications** - Multi-agent systems built with CrewAI
- **AI Agents** - From Google ADK, Claude Code, and other frameworks
- **Agent Tools** - Utilities and integrations for agent development
- **MCP Implementations** - Model Context Protocol integrations
- **Framework Ports** - TypeScript, JavaScript, and other language implementations

## Local setup

```zsh
npm install
```

## Sync app listings into SQLite

1) Copy the example config and edit it:

```zsh
cp sync.config.example.json sync.config.json
```

2) (Optional) set a GitHub token to avoid rate limits:

```zsh
export GITHUB_TOKEN="..."
```

3) Sync:

```zsh
npm run sync
```

Notes:
- `streamlit_official_gallery` pulls from `https://streamlit.io/gallery`.
- `streamlit_community_explore` pulls from Streamlit Community Cloud’s public JSON API.
- Add more lists by appending new objects in `sync.config.json` under `feeds` (e.g. `github_repos`).

## Run the web app

```zsh
npm run dev
```

Then open `http://localhost:3000`.
