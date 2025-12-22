from crewai import Task
from textwrap import dedent

class MedicalSearchTasks:
    def search_literature_task(self, agent, query, focus):
        return Task(
            description=dedent(f"""
                Search medical literature for relevant research and information.

                Query: {query}
                Focus: {focus}

                Steps:
                1. Formulate effective search queries
                2. Search PubMed and medical databases
                3. Filter for relevance and quality
                4. Retrieve full abstracts
                5. Organize results by relevance
            """),
            agent=agent,
            expected_output="List of relevant medical research papers with abstracts"
        )

    def find_clinical_trials_task(self, agent, condition, intervention):
        return Task(
            description=dedent(f"""
                Find relevant clinical trials for the specified condition and intervention.

                Condition: {condition}
                Intervention: {intervention}

                Steps:
                1. Search clinical trial registries
                2. Filter by phase and status
                3. Identify relevant trials
                4. Extract trial details
                5. Summarize key trial information
            """),
            agent=agent,
            expected_output="List of relevant clinical trials with details and status"
        )

    def research_drug_task(self, agent, drug_name):
        return Task(
            description=dedent(f"""
                Research comprehensive information about a medication.

                Drug Name: {drug_name}

                Steps:
                1. Search drug databases
                2. Gather mechanism of action
                3. Identify indications and dosing
                4. List side effects and interactions
                5. Compile safety information
            """),
            agent=agent,
            expected_output="Comprehensive drug information including uses, dosing, and safety"
        )

    def synthesize_evidence_task(self, agent, research_data):
        return Task(
            description=dedent(f"""
                Synthesize medical evidence from multiple sources.

                Research Data: {research_data}

                Steps:
                1. Review all research findings
                2. Identify common themes and conclusions
                3. Note contradictions or controversies
                4. Assess overall evidence quality
                5. Create comprehensive summary
            """),
            agent=agent,
            expected_output="Evidence synthesis with key findings and quality assessment"
        )

    def evaluate_evidence_task(self, agent, studies):
        return Task(
            description=dedent(f"""
                Evaluate the quality and reliability of medical evidence.

                Studies: {studies}

                Steps:
                1. Assess study designs and methodologies
                2. Identify potential biases
                3. Evaluate sample sizes and power
                4. Rate evidence quality (high/moderate/low)
                5. Provide recommendations based on evidence
            """),
            agent=agent,
            expected_output="Evidence evaluation with quality ratings and recommendations"
        )
