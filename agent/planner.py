def create_plan(task: str, repo_files: list[str]) -> dict:
    return {
        "goal": task,
        "steps": [
            "Inspect repository structure",
            "Identify relevant modules",
            "Implement required changes",
            "Run tests"
        ],
        "files_to_modify": repo_files[:1],  # temporary
        "tests_to_run": ["pytest"]
    }
