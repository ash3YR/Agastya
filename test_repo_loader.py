from agent.state import AgentState
from agent.repo_loader import load_repository

state = AgentState(goal="test", repo_path=".")
load_repository(state)

print(f"Loaded {len(state.files)} files")
print(list(state.files.keys())[:5])
