import os

def load_repo(repo_path: str) -> list[str]:
    files = []
    for root, _, filenames in os.walk(repo_path):
        if ".git" in root or "venv" in root:
            continue
        for f in filenames:
            if f.endswith(".py"):
                files.append(os.path.relpath(os.path.join(root, f), repo_path))
    return files
