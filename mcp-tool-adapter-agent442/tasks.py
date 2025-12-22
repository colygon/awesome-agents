from crewai import Task
from textwrap import dedent

class MCPAdapterTasks:
    def analyze_protocol_task(self, agent, tool_description):
        return Task(
            description=dedent(f"""
                Analyze the MCP protocol requirements for the given tool.

                Tool Description: {tool_description}

                Steps:
                1. Review MCP protocol specifications
                2. Identify required protocol features
                3. Analyze tool capabilities and requirements
                4. Map tool functions to MCP messages
                5. Document protocol requirements
            """),
            agent=agent,
            expected_output="Detailed protocol analysis with MCP requirements and mappings"
        )

    def validate_schema_task(self, agent, tool_schema):
        return Task(
            description=dedent(f"""
                Validate the tool schema against MCP standards.

                Tool Schema: {tool_schema}

                Steps:
                1. Parse the tool schema definition
                2. Validate against MCP schema requirements
                3. Check data types and parameter formats
                4. Verify response structures
                5. Report validation results and issues
            """),
            agent=agent,
            expected_output="Schema validation report with compliance status and any issues"
        )

    def generate_adapter_task(self, agent, protocol_requirements, tool_spec):
        return Task(
            description=dedent(f"""
                Generate an MCP adapter for the specified tool.

                Protocol Requirements: {protocol_requirements}
                Tool Specification: {tool_spec}

                Steps:
                1. Design adapter architecture
                2. Generate protocol message handlers
                3. Implement tool function wrappers
                4. Add error handling and logging
                5. Create configuration templates
            """),
            agent=agent,
            expected_output="Complete MCP adapter code with configuration and documentation"
        )

    def test_integration_task(self, agent, adapter_code):
        return Task(
            description=dedent(f"""
                Test the MCP adapter integration and functionality.

                Adapter Code: {adapter_code}

                Steps:
                1. Set up test environment
                2. Create comprehensive test cases
                3. Test protocol message handling
                4. Verify tool function execution
                5. Validate error handling
                6. Generate test report
            """),
            agent=agent,
            expected_output="Integration test report with results and recommendations"
        )
