"""
agent/editor.py

Applies planned code changes to the repository.
"""

from pathlib import Path
from typing import Dict

from agent.state import AgentState


def apply_changes(
    state: AgentState,
    changes: Dict[str, str],
    write_to_disk: bool = True,
) -> None:
    """
    Apply code changes to the agent state (and optionally disk).

    Args:
        state: AgentState object
        changes: mapping of file_path -> new file content
        write_to_disk: whether to persist changes to disk
    """
    repo_root = Path(state.repo_path).resolve()

    state.record_action("apply_changes")

    for file_path, new_content in changes.items():
        # Update in-memory state
        state.files[file_path] = new_content

        if write_to_disk:
            abs_path = repo_root / file_path
            abs_path.parent.mkdir(parents=True, exist_ok=True)
            abs_path.write_text(new_content, encoding="utf-8")
