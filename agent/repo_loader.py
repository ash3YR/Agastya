"""
agent/repo_loader.py

Loads a repository from disk into the agent state.
"""

from pathlib import Path
from typing import Iterable

from agent.state import AgentState


# Directories we never want to load
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    "venv",
    ".venv",
    "node_modules",
}


# File extensions we consider as source files (v1 scope)
ALLOWED_EXTENSIONS = {
    ".py",
    ".txt",
    ".md",
    ".yaml",
    ".yml",
}


def _should_ignore(path: Path) -> bool:
    """Check whether a path should be ignored."""
    return any(part in IGNORE_DIRS for part in path.parts)


def _iter_files(repo_path: Path) -> Iterable[Path]:
    """Yield all relevant source files in the repository."""
    for path in repo_path.rglob("*"):
        if not path.is_file():
            continue
        if _should_ignore(path):
            continue
        if path.suffix not in ALLOWED_EXTENSIONS:
            continue
        yield path


def load_repository(state: AgentState) -> None:
    """
    Load repository files into the agent state.

    Mutates:
        state.files
    """
    repo_root = Path(state.repo_path).resolve()

    if not repo_root.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo_root}")

    state.files.clear()
    state.record_action("load_repository")

    for file_path in _iter_files(repo_root):
        try:
            relative_path = str(file_path.relative_to(repo_root))
            state.files[relative_path] = file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Skip non-text or badly encoded files
            continue

