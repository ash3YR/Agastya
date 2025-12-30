from agent.state import AgentState
from agent.editor import apply_changes

print("Starting editor test...")

state = AgentState(goal="test", repo_path=".")
state.files["example.py"] = "print('old')"

apply_changes(
    state,
    {"example.py": "print('new')"},
    write_to_disk=False,
)

print("Updated content:")
print(state.files["example.py"])
