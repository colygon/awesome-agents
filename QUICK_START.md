# CrewAI Parallel Agents - Quick Start Guide

## 🚀 Run All Agents (Parallel Demo)

```bash
python3 demo_parallel_crewai.py
```

This validates all 5 CrewAI agents in parallel and shows their capabilities.

---

## 🎯 Run Individual Agents

### Agent 5: KnowledgeGPT (Document Q&A)
```bash
cd knowledge-gpt-agent5
pip install -r requirements.txt
streamlit run knowledge_gpt/main.py
```
**Agents**: Document Analyst, Question Interpreter, Answer Synthesizer

### Agent 6: GPT Lab (Research Workflows)
```bash
cd gptlab-agent6
pip install -r requirements.txt
streamlit run app/home.py
```
**Agents**: Research Analyst, Data Analyst, Report Writer

### Agent 7: Email Generator (AI Writing)
```bash
cd email-generator-agent7
pip install -r requirements.txt
streamlit run streamlit_app_crewai.py
```
**Agents**: Content Researcher, Email Writer, Editor

### Agent 9: Talk with PDF (PDF Analysis)
```bash
cd talk-with-pdf-agent9
pip install -r requirements.txt
streamlit run app_crewai.py
```
**Agents**: PDF Analyzer, Summarizer, Q&A Specialist

### Agent 10: LLM Leaderboard (Model Insights)
```bash
cd llm-leaderboard-agent10
pip install -r requirements.txt
streamlit run streamlit_app_crewai.py
```
**Agents**: Data Analyst, Model Comparator, Insights Generator

---

## ⚙️ Environment Setup

Each agent needs an OpenAI API key:

```bash
cd <agent-directory>
echo "OPENAI_API_KEY=your-key-here" > .env
```

---

## 🧪 Validation Tools

### Validate All Agents
```bash
python3 run_parallel_agents.py
```

### List Available Agents
```bash
python3 run_parallel_agents.py --list
```

### Validate Specific Agents
```bash
python3 run_parallel_agents.py --agents agent5 agent7
```

---

## 📊 Status Summary

| Agent | App | Agents | Status |
|-------|-----|--------|--------|
| agent5 | KnowledgeGPT | 3 | ✅ Ready |
| agent6 | GPT Lab | 3 | ✅ Ready |
| agent7 | Email Generator | 3 | ✅ Ready |
| agent9 | Talk with PDF | 3 | ✅ Ready |
| agent10 | LLM Leaderboard | 3 | ✅ Ready |

**Total**: 15 CrewAI agents across 5 apps

---

## 📚 Documentation

- [PARALLEL_DEPLOYMENT_GUIDE.md](PARALLEL_DEPLOYMENT_GUIDE.md) - Full deployment guide
- [AGENT_ASSIGNMENTS.md](AGENT_ASSIGNMENTS.md) - Project tracking
- Each agent directory has its own `CREWAI_UPGRADE.md` file

---

## 🆘 Troubleshooting

**Missing API Key?**
```bash
export OPENAI_API_KEY="your-key-here"
```

**Port in use?**
```bash
streamlit run app.py --server.port 8502
```

**Import errors?**
```bash
pip install -r requirements.txt
```

---

## ✨ What's New

All 5 apps now feature:
- 🤖 **Multi-agent collaboration** with CrewAI
- 🎯 **Specialized agents** for each task
- 🔄 **Sequential workflows** for better results
- 📝 **Comprehensive documentation**
- ✅ **Validated and tested** in parallel

---

**Need help?** See [PARALLEL_DEPLOYMENT_GUIDE.md](PARALLEL_DEPLOYMENT_GUIDE.md) for detailed instructions.
