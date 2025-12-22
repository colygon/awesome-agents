"""
Files Compressor Tool - CrewAI Task Definitions

This module defines tasks for the file compression workflow.
"""

from crewai import Task


def create_strategy_task(agent, compression_request):
    """
    Create a task for formulating compression strategy.

    Args:
        agent: Compression Strategist agent
        compression_request: User's compression requirements

    Returns:
        Task: Strategy formulation task
    """
    return Task(
        description=f"""Analyze the compression requirements and formulate an
        optimal compression strategy:

        Compression Request: {compression_request}

        Consider:
        1. File types and their compression characteristics
        2. Total size and file count
        3. Compression format recommendations (ZIP, TAR.GZ, 7Z, etc.)
        4. Compression level trade-offs (speed vs. ratio)
        5. Compatibility requirements
        6. Directory structure preservation
        7. Include/exclude patterns

        Provide a comprehensive compression plan with:
        - Recommended compression format and level
        - Expected compression ratio
        - Estimated processing time
        - Memory requirements
        - Compatibility considerations""",
        expected_output="""A detailed compression strategy with:
        - Optimal compression format and algorithm
        - Compression level recommendation (0-9)
        - Expected space savings percentage
        - Processing time estimate
        - Technical implementation details
        - Compatibility notes""",
        agent=agent
    )


def create_execution_task(agent, strategy_context):
    """
    Create a task for executing compression operations.

    Args:
        agent: Archive Manager agent
        strategy_context: Context from the strategy task

    Returns:
        Task: Execution task
    """
    return Task(
        description=f"""Execute the compression operation based on the strategy:

        {strategy_context}

        Implementation steps:
        1. Validate source files and directories
        2. Prepare file list with include/exclude patterns
        3. Configure compression parameters
        4. Execute compression with progress tracking
        5. Verify archive integrity
        6. Generate compression report

        Handle:
        - Large file processing
        - Symbolic links and special files
        - File permissions preservation
        - Error handling and recovery
        - Progress monitoring""",
        expected_output="""Compression execution report with:
        - Files processed count and total size
        - Archive file location and size
        - Actual compression ratio achieved
        - Processing time and speed
        - Any errors or warnings
        - Integrity verification results""",
        agent=agent
    )


def create_analysis_task(agent, execution_context):
    """
    Create a task for analyzing compression results.

    Args:
        agent: Optimization Analyst agent
        execution_context: Context from the execution task

    Returns:
        Task: Analysis task
    """
    return Task(
        description=f"""Analyze the compression results and provide insights:

        {execution_context}

        Perform analysis on:
        1. Compression efficiency (actual vs. expected ratio)
        2. Processing performance (time, speed, memory)
        3. Space savings (bytes, percentage)
        4. File type breakdown and compression rates
        5. Potential optimizations
        6. Comparison with alternative methods

        Provide recommendations for:
        - Future compression operations
        - Format or level adjustments
        - Workflow improvements
        - Storage cost savings""",
        expected_output="""Comprehensive analysis report with:
        - Compression efficiency metrics
        - Performance statistics
        - Space savings breakdown
        - File type analysis
        - Optimization recommendations (3-5 items)
        - Cost-benefit analysis
        - Alternative approach suggestions""",
        agent=agent
    )
