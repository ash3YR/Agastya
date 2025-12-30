"""
agent/state.py

Defines the shared state object for the autonomous coding agent.
This state is passed across planning, editing, testing, and analysis.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class AgentState:
    # --- High-level task info ---
    goal: str
    repo_path: str

    # --- Repository snapshot ---
    # Maps file path -> file contents
    files: Dict[str, str] = field(default_factory=dict)

    # --- Planning ---
    plan: Optional[dict] = None

    # --- Execution history ---
    actions: List[str] = field(default_factory=list)

    # --- Errors & feedback ---
    errors: List[str] = field(default_factory=list)
    test_output: Optional[str] = None

    # --- Control flags ---
    iteration: int = 0
    max_iterations: int = 3

    def record_action(self, action: str) -> None:
        """Record a high-level agent action."""
        self.actions.append(action)

    def record_error(self, error: str) -> None:
        """Record an error encountered during execution."""
        self.errors.append(error)

    def should_continue(self) -> bool:
        """Check whether the agent should continue iterating."""
        return self.iteration < self.max_iterations

    def next_iteration(self) -> None:
        """Advance the agent iteration counter."""
        self.iteration += 1
