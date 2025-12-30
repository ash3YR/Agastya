"""
agent/tester.py

Runs tests for the repository and captures results.
"""

import subprocess
from pathlib import Path
from typing import List

from agent.state import AgentState


def run_tests(
    state: AgentState,
    commands: List[str],
    timeout: int = 60,
) -> None:
    """
    Run test commands and store output in agent state.

    Args:
        state: AgentState
        commands: list of shell commands to execute
        timeout: max seconds per command
    """
    repo_root = Path(state.repo_path).resolve()
    state.record_action("run_tests")

    all_output = []

    for cmd in commands:
        try:
            result = subprocess.run(
                cmd,
                cwd=repo_root,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            output = (
                f"$ {cmd}\n"
                f"Return code: {result.returncode}\n"
                f"STDOUT:\n{result.stdout}\n"
                f"STDERR:\n{result.stderr}\n"
            )

            all_output.append(output)

            if result.returncode != 0:
                state.record_error(f"Test failed: {cmd}")

        except subprocess.TimeoutExpired:
            msg = f"Test timed out after {timeout}s: {cmd}"
            all_output.append(msg)
            state.record_error(msg)

        except Exception as e:
            msg = f"Error running test '{cmd}': {e}"
            all_output.append(msg)
            state.record_error(msg)

    state.test_output = "\n".join(all_output)
