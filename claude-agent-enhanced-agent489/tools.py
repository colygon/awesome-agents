"""
Enhanced Tools for Claude Code Agent - CrewAI Implementation
Provides all core SDK-compatible tools plus enhanced collaboration features.
"""

import os
import subprocess
import glob as glob_module
import re
from pathlib import Path
from typing import Optional
from crewai.tools import tool


@tool("read_file")
def read_file(file_path: str) -> str:
    """
    Read the contents of a file.
    Matches SDK Read tool behavior.

    Args:
        file_path: Path to the file to read

    Returns:
        File contents as string
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return f"Successfully read {file_path}:\n\n{content}"
    except FileNotFoundError:
        return f"Error: File not found: {file_path}"
    except PermissionError:
        return f"Error: Permission denied reading {file_path}"
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"


@tool("write_file")
def write_file(file_path: str, content: str) -> str:
    """
    Write content to a file, creating it if it doesn't exist.
    Matches SDK Write tool behavior.

    Args:
        file_path: Path to the file to write
        content: Content to write to the file

    Returns:
        Success or error message
    """
    try:
        # Create parent directories if they don't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return f"Successfully wrote {len(content)} characters to {file_path}"
    except PermissionError:
        return f"Error: Permission denied writing to {file_path}"
    except Exception as e:
        return f"Error writing to {file_path}: {str(e)}"


@tool("edit_file")
def edit_file(file_path: str, old_string: str, new_string: str) -> str:
    """
    Edit a file by replacing old_string with new_string.
    Matches SDK Edit tool behavior.

    Args:
        file_path: Path to the file to edit
        old_string: String to find and replace
        new_string: String to replace with

    Returns:
        Success message with number of replacements or error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_string not in content:
            return f"Error: String not found in {file_path}: {old_string[:50]}..."

        # Count occurrences
        count = content.count(old_string)

        # Replace
        new_content = content.replace(old_string, new_string)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return f"Successfully replaced {count} occurrence(s) in {file_path}"
    except FileNotFoundError:
        return f"Error: File not found: {file_path}"
    except Exception as e:
        return f"Error editing {file_path}: {str(e)}"


@tool("bash_command")
def bash_command(command: str, timeout: int = 60) -> str:
    """
    Execute a bash command and return the output.
    Matches SDK Bash tool behavior.

    Args:
        command: Command to execute
        timeout: Timeout in seconds (default 60)

    Returns:
        Command output or error message
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        output = result.stdout
        if result.stderr:
            output += f"\n[stderr]:\n{result.stderr}"

        if result.returncode != 0:
            return f"Command failed with exit code {result.returncode}:\n{output}"

        return output or "[Command executed successfully with no output]"
    except subprocess.TimeoutExpired:
        return f"Error: Command timed out after {timeout} seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"


@tool("glob_files")
def glob_files(pattern: str, path: str = ".") -> str:
    """
    Find files matching a glob pattern.
    Matches SDK Glob tool behavior.

    Args:
        pattern: Glob pattern (e.g., "*.py", "**/*.js")
        path: Root directory to search from (default current directory)

    Returns:
        List of matching files
    """
    try:
        # Change to the specified directory
        original_dir = os.getcwd()
        if path != ".":
            os.chdir(path)

        # Use recursive glob if ** is in pattern
        if "**" in pattern:
            matches = glob_module.glob(pattern, recursive=True)
        else:
            matches = glob_module.glob(pattern)

        # Change back to original directory
        os.chdir(original_dir)

        if not matches:
            return f"No files found matching pattern: {pattern}"

        # Sort for consistent output
        matches.sort()

        result = f"Found {len(matches)} file(s) matching '{pattern}':\n"
        result += "\n".join(f"  - {match}" for match in matches)

        return result
    except Exception as e:
        return f"Error searching for files: {str(e)}"


@tool("grep_search")
def grep_search(
    pattern: str,
    path: str = ".",
    file_pattern: str = "*",
    max_results: int = 100
) -> str:
    """
    Search for a pattern in files (like grep).
    Matches SDK Grep tool behavior.

    Args:
        pattern: Regex pattern to search for
        path: Directory to search in (default current directory)
        file_pattern: File glob pattern to filter files (default all files)
        max_results: Maximum number of results to return (default 100)

    Returns:
        Search results with file names and line numbers
    """
    try:
        # Compile regex pattern
        regex = re.compile(pattern)

        # Find matching files
        search_pattern = os.path.join(path, "**", file_pattern)
        files = glob_module.glob(search_pattern, recursive=True)

        results = []
        total_matches = 0

        for file_path in files:
            # Skip directories
            if os.path.isdir(file_path):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        if regex.search(line):
                            results.append(f"{file_path}:{line_num}: {line.rstrip()}")
                            total_matches += 1

                            if total_matches >= max_results:
                                break
            except Exception:
                # Skip files that can't be read
                continue

            if total_matches >= max_results:
                break

        if not results:
            return f"No matches found for pattern: {pattern}"

        result = f"Found {len(results)} match(es) for '{pattern}':\n"
        result += "\n".join(results)

        if total_matches >= max_results:
            result += f"\n\n[Limited to {max_results} results]"

        return result
    except re.error as e:
        return f"Error: Invalid regex pattern: {e}"
    except Exception as e:
        return f"Error searching files: {str(e)}"


# Enhanced collaboration tool
@tool("share_knowledge")
def share_knowledge(knowledge_type: str, content: str) -> str:
    """
    Share knowledge between agents in the crew.
    Enhanced feature beyond basic SDK.

    Args:
        knowledge_type: Type of knowledge (e.g., 'finding', 'decision', 'recommendation')
        content: The knowledge content to share

    Returns:
        Confirmation message
    """
    # In a real implementation, this would store to crew memory/knowledge base
    # For demo purposes, we just return confirmation
    return f"[Knowledge Shared] {knowledge_type}: {content}"


# Code quality analysis tool
@tool("analyze_code_quality")
def analyze_code_quality(file_path: str) -> str:
    """
    Analyze code quality metrics for a file.
    Enhanced feature for code review workflows.

    Args:
        file_path: Path to the code file to analyze

    Returns:
        Code quality analysis report
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Basic metrics
        total_lines = len(lines)
        code_lines = len([l for l in lines if l.strip() and not l.strip().startswith('#')])
        comment_lines = len([l for l in lines if l.strip().startswith('#')])
        blank_lines = total_lines - code_lines - comment_lines

        # Simple complexity indicators
        long_lines = len([l for l in lines if len(l) > 100])
        nested_depth = max([len(l) - len(l.lstrip()) for l in lines]) // 4

        report = f"""Code Quality Analysis: {file_path}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Lines of Code:     {code_lines}
Comment Lines:     {comment_lines}
Blank Lines:       {blank_lines}
Total Lines:       {total_lines}

Metrics:
- Lines > 100 chars: {long_lines}
- Max nesting depth: {nested_depth}
- Comment ratio:     {comment_lines/max(code_lines, 1):.1%}

Recommendations:
{"- Consider breaking up long lines" if long_lines > 5 else "✓ Line lengths look good"}
{"- High nesting detected, consider refactoring" if nested_depth > 4 else "✓ Nesting depth is reasonable"}
{"- Consider adding more comments" if comment_lines/max(code_lines, 1) < 0.1 else "✓ Comment coverage is adequate"}
"""
        return report
    except Exception as e:
        return f"Error analyzing {file_path}: {str(e)}"
