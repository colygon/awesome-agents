"""
ADK Test Automation - CrewAI Task Definitions
Sequential Test Automation Workflow

This module defines the tasks for the multi-agent test automation workflow:
1. Test Strategy Planning
2. Test Case Generation
3. Test Suite Review and Optimization
"""

from crewai import Task
from textwrap import dedent


def create_test_strategy_task(agent, application_context: dict) -> Task:
    """
    Creates a task for developing a comprehensive test strategy.

    Args:
        agent: The Test Strategist agent
        application_context: Dictionary containing:
            - app_type: Type of application
            - tech_stack: Technologies used
            - features: Key features to test
            - description: Application description

    Returns:
        Task: Configured test strategy task
    """
    app_type = application_context.get('app_type', 'Unknown')
    tech_stack = ', '.join(application_context.get('tech_stack', ['Unknown']))
    features = ', '.join(application_context.get('features', ['Unknown']))
    description = application_context.get('description', '')

    return Task(
        description=dedent(f"""
            Develop a comprehensive test automation strategy for the following application:

            APPLICATION TYPE: {app_type}
            TECH STACK: {tech_stack}
            KEY FEATURES: {features}

            DESCRIPTION:
            {description}

            Create a detailed test strategy that includes:

            1. TEST COVERAGE ANALYSIS
               - Identify critical user workflows
               - Map high-risk areas requiring testing
               - Define test pyramid (unit, integration, E2E ratios)
               - Specify coverage targets by layer
               - Identify areas for manual vs. automated testing

            2. TEST TYPE SELECTION
               For each appropriate test type, specify:
               - Unit Tests: Component isolation, business logic
               - Integration Tests: API contracts, data flow
               - E2E Tests: Critical user journeys
               - API Tests: Endpoint validation, error handling
               - Performance Tests: Load, stress scenarios
               - Security Tests: Authentication, authorization, input validation
               - Accessibility Tests: WCAG compliance (if applicable)

            3. TESTING FRAMEWORK RECOMMENDATIONS
               - Recommended frameworks for each test type
               - Rationale for framework selection
               - Required dependencies and tools
               - CI/CD integration approach

            4. TEST PRIORITIZATION
               Prioritize tests by:
               - Business criticality
               - Risk level
               - Frequency of use
               - Complexity of feature
               - Cost of failure

            5. TEST DATA STRATEGY
               - Test data generation approach
               - Data isolation and cleanup
               - Edge cases and boundary conditions
               - Mock/stub requirements

            6. EXECUTION PLAN
               - Test execution order
               - Parallelization strategy
               - Environment requirements
               - CI/CD pipeline integration

            7. SUCCESS METRICS
               - Coverage targets
               - Execution time goals
               - Defect detection effectiveness
               - Maintenance overhead limits
        """),
        expected_output=dedent("""
            A comprehensive test strategy document containing:

            ## Test Strategy Overview
            - Application context summary
            - Testing objectives
            - Success criteria

            ## Test Coverage Plan

            ### Unit Tests (Target: X% coverage)
            - Components to test
            - Business logic validation
            - Edge cases

            ### Integration Tests
            - Component integration points
            - API contract testing
            - Data flow validation

            ### End-to-End Tests
            - Critical user workflows (prioritized)
            - Happy path scenarios
            - Error handling flows

            ### Additional Test Types
            - Performance testing requirements
            - Security testing focus areas
            - Accessibility requirements

            ## Framework Recommendations
            - Unit Testing: [Framework + rationale]
            - Integration Testing: [Framework + rationale]
            - E2E Testing: [Framework + rationale]
            - API Testing: [Framework + rationale]

            ## Test Prioritization Matrix
            | Feature | Priority | Risk | Test Type | Est. Effort |
            |---------|----------|------|-----------|-------------|
            | [Feature] | High/Med/Low | High/Med/Low | Unit/Integration/E2E | Hours |

            ## Test Data Strategy
            - Data generation approach
            - Fixture management
            - Mock/stub strategy

            ## Execution Plan
            - Test execution sequence
            - Parallelization approach
            - CI/CD integration points
            - Environment setup

            ## Success Metrics
            - Coverage targets
            - Performance benchmarks
            - Quality gates

            Format as a structured markdown document with clear sections and actionable guidance.
        """),
        agent=agent
    )


def create_test_generation_task(agent, test_strategy_output, application_context: dict) -> Task:
    """
    Creates a task for generating automated test cases.

    Args:
        agent: The Test Generator agent
        test_strategy_output: Output from the test strategy task
        application_context: Application context dictionary

    Returns:
        Task: Configured test generation task
    """
    return Task(
        description=dedent(f"""
            Based on the test strategy below, generate comprehensive automated test cases.

            TEST STRATEGY:
            {test_strategy_output}

            Generate test cases following these requirements:

            1. TEST IMPLEMENTATION
               For each test type identified in the strategy:
               - Write complete, runnable test code
               - Follow framework-specific best practices
               - Include proper setup and teardown
               - Implement appropriate assertions
               - Add descriptive test names and comments

            2. TEST PATTERNS
               Apply appropriate patterns:
               - Page Object Model for UI tests
               - Arrange-Act-Assert for unit tests
               - Given-When-Then for BDD tests
               - Test fixtures for data setup
               - Proper mocking/stubbing

            3. TEST COVERAGE
               Ensure comprehensive coverage:
               - Happy path scenarios
               - Edge cases and boundaries
               - Error conditions and exceptions
               - Invalid input handling
               - State transitions

            4. CODE QUALITY
               - Clear, descriptive names
               - Single responsibility per test
               - Independent, isolated tests
               - No hard-coded values
               - Proper resource cleanup
               - Meaningful error messages

            5. DOCUMENTATION
               - Test purpose and intent
               - Setup requirements
               - Expected behavior
               - Known limitations

            Generate at least 3-5 examples for each major test type (unit, integration, E2E)
            covering the highest priority features from the test strategy.
        """),
        expected_output=dedent("""
            A comprehensive test implementation document containing:

            ## Unit Tests

            ### [Component Name] Tests

            ```[language]
            // Test file: [filename]
            // Framework: [framework]

            describe('[Component Name]', () => {{
              // Test setup
              beforeEach(() => {{
                // Setup code
              }});

              // Test teardown
              afterEach(() => {{
                // Cleanup code
              }});

              it('should [expected behavior] when [condition]', () => {{
                // Arrange
                const input = ...;

                // Act
                const result = ...;

                // Assert
                expect(result).toBe(...);
              }});

              it('should handle [edge case]', () => {{
                // Test implementation
              }});
            }});
            ```

            ## Integration Tests

            ### [Feature] Integration Tests

            ```[language]
            // Test implementation with setup, execution, and assertions
            ```

            ## End-to-End Tests

            ### [User Workflow] E2E Tests

            ```[language]
            // Complete user flow test implementation
            ```

            ## Test Fixtures and Helpers

            ### Test Data Fixtures
            ```[language]
            // Reusable test data and factories
            ```

            ### Test Helpers
            ```[language]
            // Common test utilities and helpers
            ```

            ## Configuration Files

            ### Test Configuration
            ```[language]
            // Framework configuration
            ```

            ## Documentation
            - Setup instructions
            - Running tests
            - CI/CD integration
            - Troubleshooting guide

            Provide complete, runnable code examples with proper syntax highlighting.
        """),
        agent=agent,
        context=[test_strategy_output] if isinstance(test_strategy_output, Task) else []
    )


def create_test_review_task(agent, test_strategy_output, test_generation_output) -> Task:
    """
    Creates a task for reviewing and optimizing generated tests.

    Args:
        agent: The Test Reviewer agent
        test_strategy_output: Output from the test strategy task
        test_generation_output: Output from the test generation task

    Returns:
        Task: Configured test review task
    """
    return Task(
        description=dedent(f"""
            Review the generated test suite below and provide comprehensive feedback
            and optimization recommendations.

            TEST STRATEGY:
            {test_strategy_output}

            GENERATED TESTS:
            {test_generation_output}

            Conduct a thorough review covering:

            1. TEST QUALITY ASSESSMENT
               - Test effectiveness (will they catch real bugs?)
               - Test clarity (is intent obvious?)
               - Test reliability (are they deterministic?)
               - Assertion strength (specific and meaningful?)
               - Error messages (helpful for debugging?)

            2. COVERAGE ANALYSIS
               - Does the suite cover critical paths?
               - Are edge cases addressed?
               - Are there obvious gaps?
               - Is the test pyramid balanced?
               - Are redundant tests present?

            3. ANTI-PATTERN DETECTION
               - Test interdependencies
               - Hard-coded values or magic numbers
               - Brittle selectors or locators
               - Excessive or insufficient mocking
               - Weak assertions (asserting true)
               - Duplicate test logic
               - Slow or inefficient tests

            4. MAINTAINABILITY REVIEW
               - Code duplication analysis
               - Abstraction opportunities
               - Setup/teardown efficiency
               - Test data management
               - Documentation adequacy

            5. BEST PRACTICE COMPLIANCE
               - Naming conventions
               - Test structure and organization
               - Framework usage patterns
               - Resource management
               - Error handling

            6. OPTIMIZATION OPPORTUNITIES
               - Parallelization potential
               - Test data optimization
               - Execution speed improvements
               - Flakiness reduction
               - CI/CD integration enhancements

            Provide specific, actionable recommendations with code examples where appropriate.
            Prioritize feedback by impact (critical, high, medium, low).
        """),
        expected_output=dedent("""
            A comprehensive test review report containing:

            ## Executive Summary
            - Overall test suite quality assessment
            - Key strengths
            - Critical issues to address
            - Recommended priorities

            ## Detailed Review

            ### Test Quality Assessment
            - **Effectiveness**: [Assessment with examples]
            - **Clarity**: [Assessment with examples]
            - **Reliability**: [Assessment with examples]
            - **Assertions**: [Strength analysis]

            ### Coverage Analysis
            - **Critical Path Coverage**: [X%] - [Details]
            - **Edge Case Coverage**: [Assessment]
            - **Coverage Gaps**: [List of missing scenarios]
            - **Redundant Tests**: [List if any]

            ### Issues Identified

            #### Critical Issues
            1. [Issue description]
               - Impact: [Business/technical impact]
               - Example: [Code snippet]
               - Recommendation: [Specific fix]

            #### High Priority Issues
            [Similar structure]

            #### Medium Priority Issues
            [Similar structure]

            ### Anti-Patterns Detected
            - **[Pattern Name]**: [Description and location]
              ```[language]
              // Current implementation

              // Recommended fix
              ```

            ### Optimization Recommendations

            #### Execution Speed
            - [Specific optimization with example]

            #### Maintainability
            - [Refactoring suggestions with code]

            #### Coverage Enhancement
            - [Additional scenarios to test]

            ### Best Practice Improvements
            - **Naming**: [Suggestions]
            - **Structure**: [Reorganization ideas]
            - **Documentation**: [Areas needing docs]

            ## Revised Test Examples
            [Show improved versions of problematic tests]

            ## Action Plan
            1. [Priority 1 items with effort estimate]
            2. [Priority 2 items with effort estimate]
            3. [Priority 3 items with effort estimate]

            ## Metrics and Targets
            - Current coverage: X%
            - Target coverage: Y%
            - Current execution time: X seconds
            - Target execution time: Y seconds
            - Estimated improvement: [Metrics]

            Format as a structured markdown document with code examples and clear priorities.
        """),
        agent=agent,
        context=[test_strategy_output, test_generation_output] if isinstance(test_strategy_output, Task) else []
    )
