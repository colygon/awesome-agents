# Medical Search Pro - CrewAI Implementation

## Overview
A multi-agent system for comprehensive medical literature search, clinical trial discovery, and evidence-based medical information retrieval.

## Agents

### 1. Medical Literature Researcher
- Searches PubMed and medical databases
- Retrieves relevant research papers
- Filters for quality and relevance

### 2. Clinical Trial Specialist
- Searches clinical trial registries
- Finds relevant ongoing and completed trials
- Analyzes trial methodologies

### 3. Drug Information Specialist
- Provides comprehensive drug information
- Details mechanisms, dosing, interactions
- Compiles safety data

### 4. Medical Information Synthesizer
- Synthesizes evidence from multiple sources
- Creates clear medical summaries
- Identifies consensus and controversies

### 5. Medical Evidence Evaluator
- Evaluates study quality
- Assesses evidence reliability
- Rates evidence levels

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

3. Get NCBI API key (optional but recommended):
   - Visit: https://www.ncbi.nlm.nih.gov/account/

4. Run the system:
```bash
python main.py
```

## Features
- PubMed literature search
- Clinical trial discovery
- Drug information retrieval
- Evidence synthesis
- Quality assessment
- Medical summarization

## Data Sources
- PubMed/MEDLINE
- ClinicalTrials.gov
- Drug databases
- Medical journals
- Systematic reviews

## Search Capabilities
- Condition research
- Treatment options
- Drug information
- Clinical trials
- Latest research
- Evidence synthesis

## Use Cases
- Medical research
- Clinical decision support
- Patient education materials
- Literature reviews
- Drug information lookup
- Treatment research

## IMPORTANT DISCLAIMER
This system is for informational and educational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified healthcare providers with questions regarding medical conditions.

## Quality Standards
- Evidence-based information
- Peer-reviewed sources
- Quality assessment
- Bias evaluation
- Source transparency

## Limitations
- Not for emergency medical use
- Requires professional interpretation
- Information may become outdated
- Not a diagnostic tool
- Supplement to professional judgment
