"""
agent/analyzer.py

Analyzes test results and determines next steps.
"""

from agent.state import AgentState


def analyze(state: AgentState) -> bool:
    """
    Analyze current agent state.

    Returns:
        True if the agent should continue iterating
        False if the task is considered complete or cannot proceed
    """
    state.record_action("analyze")

    # If there are no errors, we consider the task successful
    if not state.errors:
        return False

    # If max iterations reached, stop
    if not state.should_continue():
        return False

    # Otherwise, continue for another iteration
    return True
