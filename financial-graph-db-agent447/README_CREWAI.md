# Financial Graph DB - CrewAI Implementation

## Overview
A multi-agent system for building and analyzing financial knowledge graphs using graph databases.

## Agents

### 1. Financial Entity Extractor
- Extracts financial entities
- Identifies companies, accounts, persons
- Standardizes entity identifiers

### 2. Relationship Analyst
- Maps entity relationships
- Analyzes ownership structures
- Identifies transaction patterns

### 3. Graph Database Engineer
- Builds knowledge graphs
- Creates nodes and edges
- Designs graph schemas

### 4. Graph Query Specialist
- Writes optimized queries
- Extracts insights
- Performs graph analysis

### 5. Graph Visualization Specialist
- Creates visual representations
- Highlights relationships
- Generates interactive visualizations

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install and start Neo4j:
```bash
# Using Docker
docker run -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/password neo4j
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your Neo4j credentials
```

4. Run the system:
```bash
python main.py
```

## Features
- Entity extraction
- Relationship mapping
- Graph database construction
- Complex query support
- Interactive visualization
- Pattern detection

## Graph Schema
- Nodes: Company, Account, Person, Transaction
- Relationships: OWNS, CONTROLS, TRANSACTS, AFFILIATED_WITH
- Properties: Timestamps, amounts, percentages, roles

## Use Cases
- Ownership structure analysis
- Transaction network mapping
- Fraud detection
- Compliance monitoring
- Risk assessment
- Due diligence

## Query Examples
- Find all companies owned by a person
- Trace transaction chains
- Identify circular ownership
- Detect suspicious patterns
- Map affiliate networks

## Visualization Features
- Force-directed layouts
- Interactive exploration
- Relationship highlighting
- Temporal analysis
- Network metrics
