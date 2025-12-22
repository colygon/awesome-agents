"""
CrewAI Tasks for GPT Search Application

This module defines tasks that agents perform to process queries and generate answers.
"""

from crewai import Task


class GPTSearchTasks:
    """Factory class for creating search and answer generation tasks."""

    def search_task(self, agent, query: str, top_results: list) -> Task:
        """
        Create a task for semantic search and information retrieval.

        Args:
            agent: The agent that will perform this task
            query: User's search query
            top_results: List of top-k similar sentences from similarity search

        Returns:
            Task: Configured search task
        """
        return Task(
            description=f"""Analyze the following query and identify the most relevant
            information from the provided text passages.

            User Query: {query}

            Top Similar Passages (ordered by relevance):
            {self._format_results(top_results)}

            Your task:
            1. Analyze the user's query to understand their information need
            2. Review all provided passages carefully
            3. Identify which passages contain information relevant to the query
            4. Extract key facts, statements, or information that addresses the query
            5. Note any important context or qualifications from the passages
            6. If no passage adequately addresses the query, identify this clearly

            Provide a structured analysis identifying:
            - Which passages are most relevant (reference by number)
            - Key information extracted from each relevant passage
            - How this information relates to the user's query
            """,
            expected_output="""A structured analysis containing:
            1. List of relevant passage numbers with extracted key information
            2. Connection between extracted information and the user query
            3. Any important context or qualifications
            4. Assessment of whether sufficient information exists to answer the query""",
            agent=agent
        )

    def answer_synthesis_task(self, agent, query: str, search_analysis: str) -> Task:
        """
        Create a task for synthesizing an answer from search results.

        Args:
            agent: The agent that will perform this task
            query: User's original query
            search_analysis: Output from the search task

        Returns:
            Task: Configured answer synthesis task
        """
        return Task(
            description=f"""Based on the search analysis, generate a clear and accurate
            answer to the user's query.

            User Query: {query}

            Search Analysis:
            {{search_analysis}}

            Your task:
            1. Review the search analysis and identified relevant information
            2. Synthesize the information into a coherent answer
            3. Ensure the answer directly addresses the user's query
            4. Include only information supported by the provided passages
            5. If information is insufficient, clearly state what cannot be answered
            6. Keep the answer concise but complete

            Guidelines:
            - Do NOT make up or infer information not present in the passages
            - Maintain the context and nuances from the source material
            - Use clear, natural language
            - If the query cannot be answered, respond with: 'Unable to answer the query.'
            """,
            expected_output="""A clear, accurate answer to the user's query that:
            1. Directly addresses the question asked
            2. Is grounded entirely in the provided passages
            3. Is well-structured and easy to understand
            4. Clearly indicates if the query cannot be fully answered""",
            agent=agent,
            context=[search_analysis] if isinstance(search_analysis, Task) else []
        )

    def quality_validation_task(self, agent, query: str, answer: str, top_results: list) -> Task:
        """
        Create a task for validating answer quality and accuracy.

        Args:
            agent: The agent that will perform this task
            query: User's original query
            answer: Generated answer to validate
            top_results: Original top-k similar passages

        Returns:
            Task: Configured quality validation task
        """
        return Task(
            description=f"""Validate the quality and accuracy of the generated answer.

            User Query: {query}

            Generated Answer:
            {{answer}}

            Source Passages:
            {self._format_results(top_results)}

            Your task:
            1. Verify every claim in the answer is supported by the source passages
            2. Check that the answer directly addresses the user's query
            3. Identify any hallucinations or unsupported statements
            4. Assess the clarity and completeness of the answer
            5. If issues are found, provide specific corrections or improvements
            6. If the answer is accurate and complete, approve it

            Validation Criteria:
            - Accuracy: All information must be from source passages
            - Relevance: Answer must directly address the query
            - Completeness: Important information shouldn't be omitted
            - Clarity: Answer should be easy to understand
            - Honesty: If sources don't answer the query, this must be stated
            """,
            expected_output="""A validation report containing:
            1. Pass/Fail assessment
            2. List of any issues found (hallucinations, inaccuracies, omissions)
            3. Specific corrections or improvements if needed
            4. Final approved answer (either original or corrected version)""",
            agent=agent,
            context=[answer] if isinstance(answer, Task) else []
        )

    @staticmethod
    def _format_results(results: list) -> str:
        """
        Format a list of results into a numbered string.

        Args:
            results: List of text passages

        Returns:
            str: Formatted string with numbered passages
        """
        return "\n".join([f"{i+1}. {result}" for i, result in enumerate(results)])
