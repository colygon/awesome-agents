"""
Custom tools matching Claude Code Python Agent SDK built-in tools.

This module provides CrewAI-compatible tools that replicate the functionality
of the SDK's built-in tools (Read, Write, Edit, Bash, Glob, Grep).
"""

from crewai_tools import tool
import subprocess
import glob as py_glob
import re
from pathlib import Path
from typing import Optional


@tool("read_file")
def read_file(file_path: str) -> str:
    """
    Read file contents - matches SDK Read tool.

    Args:
        file_path: Path to the file to read

    Returns:
        File contents as string

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Read"])
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found: {file_path}"
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"


@tool("write_file")
def write_file(file_path: str, content: str) -> str:
    """
    Write content to file - matches SDK Write tool.

    Args:
        file_path: Path to the file to write
        content: Content to write to the file

    Returns:
        Success message or error

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Write"])
    """
    try:
        # Create parent directories if they don't exist
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote {len(content)} characters to {file_path}"
    except Exception as e:
        return f"Error writing {file_path}: {str(e)}"


@tool("edit_file")
def edit_file(file_path: str, old_string: str, new_string: str) -> str:
    """
    Edit file by replacing text - matches SDK Edit tool.

    Args:
        file_path: Path to the file to edit
        old_string: Text to find and replace
        new_string: Replacement text

    Returns:
        Success message or error

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Edit"])
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_string not in content:
            return f"Error: String '{old_string[:50]}...' not found in {file_path}"

        # Count occurrences
        count = content.count(old_string)
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
    Execute bash command - matches SDK Bash tool.

    Args:
        command: Shell command to execute
        timeout: Maximum execution time in seconds

    Returns:
        Command output (stdout + stderr) and exit code

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Bash"])
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        output = []
        output.append(f"Exit code: {result.returncode}")

        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output)

    except subprocess.TimeoutExpired:
        return f"Error: Command timed out after {timeout} seconds"
    except Exception as e:
        return f"Error executing command: {str(e)}"


@tool("glob_files")
def glob_files(pattern: str, path: str = ".") -> str:
    """
    Find files matching glob pattern - matches SDK Glob tool.

    Args:
        pattern: Glob pattern (e.g., "**/*.py", "*.txt")
        path: Base directory to search from

    Returns:
        Newline-separated list of matching files

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Glob"])
    """
    try:
        # Combine path and pattern
        search_pattern = str(Path(path) / pattern)

        # Use recursive glob
        matches = list(py_glob.glob(search_pattern, recursive=True))

        if not matches:
            return f"No files found matching pattern: {pattern}"

        # Sort for consistency
        matches.sort()

        return f"Found {len(matches)} file(s):\n" + "\n".join(matches)

    except Exception as e:
        return f"Error in glob search: {str(e)}"


@tool("grep_search")
def grep_search(
    pattern: str,
    path: str = ".",
    file_pattern: str = "*",
    max_results: int = 100
) -> str:
    """
    Search file contents with regex - matches SDK Grep tool.

    Args:
        pattern: Regular expression pattern to search for
        path: Base directory to search
        file_pattern: File glob pattern to filter files
        max_results: Maximum number of results to return

    Returns:
        Grep-style output: filename:line_number: line_content

    SDK Equivalent:
        ClaudeAgentOptions(allowed_tools=["Grep"])
    """
    try:
        results = []

        # Find files matching the file pattern
        search_pattern = str(Path(path) / "**" / file_pattern)
        files = py_glob.glob(search_pattern, recursive=True)

        # Compile regex pattern
        regex = re.compile(pattern)

        for file in files:
            if not Path(file).is_file():
                continue

            try:
                with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        if regex.search(line):
                            results.append(f"{file}:{i}: {line.rstrip()}")

                            # Stop if we hit max results
                            if len(results) >= max_results:
                                return "\n".join(results) + f"\n\n(Stopped at {max_results} results)"
            except:
                # Skip files that can't be read
                pass

        if not results:
            return f"No matches found for pattern: {pattern}"

        return f"Found {len(results)} match(es):\n" + "\n".join(results)

    except re.error as e:
        return f"Error: Invalid regular expression: {str(e)}"
    except Exception as e:
        return f"Error in grep search: {str(e)}"


# Export all tools for easy import
__all__ = [
    'read_file',
    'write_file',
    'edit_file',
    'bash_command',
    'glob_files',
    'grep_search'
]
