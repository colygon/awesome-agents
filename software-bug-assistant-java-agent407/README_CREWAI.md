# Software Bug Assistant (Java) - CrewAI Edition

## Overview
Java-specialized bug detection and resolution system. Original ADK version was in Java, this CrewAI version is Python-based but specialized for Java bug analysis.

## Agents
- Java Bug Detective
- Java Code Analyzer
- Java Solution Architect
- Java Test Engineer (JUnit/Mockito)
- Java Documentation Specialist

## Installation
```bash
cd software-bug-assistant-java-agent407
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Usage
```bash
python main.py "NullPointerException in Spring controller"
```

---
**Original:** Java ADK
**Migration Date:** December 2025
