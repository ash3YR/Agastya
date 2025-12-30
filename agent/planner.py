"""
agent/planner.py

Generates a plan for modifying the repository to achieve a given goal.
"""

from typing import Dict, Any, List


def gemini_plan(
    repo_path: str,
    task: str,
    model: str,
) -> Dict[str, Any]:
    """
    Generate a plan using the Gemini API.

    Raises:
        Exception if the API call fails (quota, billing, network, etc.)
    """
    # Import here to avoid hard dependency if Gemini is not used
    import google.generativeai as genai

    prompt = f"""
You are an autonomous coding agent.

Repository path:
{repo_path}

Task:
{task}

Return a JSON object with the following fields:
- goal: string
- steps: list of clear, ordered steps
- files_to_modify: list of file paths
- tests_to_run: list of test commands

Respond with JSON only. No explanation.
"""

    model_client = genai.GenerativeModel(model)
    response = model_client.generate_content(prompt)

    # Gemini may return text wrapped in formatting
    text = response.text.strip()

    # Very defensive parsing (v1)
    import json
    try:
        plan = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Failed to parse Gemini plan JSON: {e}")

    return plan


def fallback_plan(
    repo_path: str,
    task: str,
) -> Dict[str, Any]:
    """
    Deterministic fallback planner.
    Used when LLM planning is unavailable.
    """
    return {
        "goal": task,
        "steps": [
            "Inspect repository structure",
            "Identify relevant modules",
            "Apply minimal changes",
            "Run tests",
        ],
        "files_to_modify": [],
        "tests_to_run": ["pytest"],
    }
