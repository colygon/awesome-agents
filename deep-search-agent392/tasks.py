from crewai import Task
from textwrap import dedent

class DeepSearchTasks:
    def plan_search_strategy(self, agent, query):
        return Task(
            description=dedent(f"""\
                Develop a comprehensive search strategy for the following query:
                {query}

                Break down the query into multiple search angles:
                1. Identify key concepts and entities
                2. Generate alternative phrasings and related terms
                3. Determine the most effective search approaches
                4. Plan the sequence of searches
                5. Identify potential sources and databases

                Create a detailed search plan with specific queries to execute."""),
            agent=agent,
            expected_output="A detailed search strategy with specific queries and sources to investigate"
        )

    def execute_deep_search(self, agent, search_plan):
        return Task(
            description=dedent(f"""\
                Execute the search strategy and gather comprehensive information:

                Search Plan:
                {search_plan}

                For each search query:
                1. Execute the search across multiple sources
                2. Collect and organize relevant results
                3. Identify additional search angles based on findings
                4. Document source URLs and publication dates
                5. Note any information gaps that need further investigation

                Gather diverse perspectives and comprehensive coverage."""),
            agent=agent,
            expected_output="Comprehensive search results organized by topic with source citations"
        )

    def analyze_information(self, agent, search_results):
        return Task(
            description=dedent(f"""\
                Analyze the collected information and extract key insights:

                Search Results:
                {search_results}

                Your analysis should:
                1. Identify main themes and patterns
                2. Extract key facts and data points
                3. Note different perspectives and viewpoints
                4. Identify any contradictions or inconsistencies
                5. Highlight particularly credible or questionable sources
                6. Organize information into logical categories

                Provide a structured analysis of the findings."""),
            agent=agent,
            expected_output="Structured analysis with key insights, themes, and organized findings"
        )

    def verify_facts(self, agent, key_claims):
        return Task(
            description=dedent(f"""\
                Verify the accuracy of key claims through cross-referencing:

                Key Claims to Verify:
                {key_claims}

                For each claim:
                1. Search for corroborating evidence from multiple sources
                2. Check the credibility and expertise of sources
                3. Look for primary sources when possible
                4. Identify any contradicting information
                5. Assess the overall reliability of the claim
                6. Note the confidence level of verification

                Provide a fact-check report with verification status."""),
            agent=agent,
            expected_output="Fact-check report with verification status and supporting evidence for each claim"
        )

    def synthesize_report(self, agent, query, analysis, verification):
        return Task(
            description=dedent(f"""\
                Create a comprehensive research report synthesizing all findings:

                Original Query: {query}
                Analysis: {analysis}
                Fact Verification: {verification}

                Your report should include:
                1. Executive Summary
                2. Main Findings (organized by theme)
                3. Key Facts and Data Points
                4. Different Perspectives
                5. Verified vs. Unverified Information
                6. Information Gaps and Limitations
                7. Source List with credibility assessment
                8. Conclusion and Recommendations

                Ensure the report is well-structured, comprehensive, and properly cited."""),
            agent=agent,
            expected_output="Comprehensive research report with all sections properly formatted and cited"
        )
