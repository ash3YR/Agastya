from agent.state import AgentState
from agent.tester import run_tests

state = AgentState(goal="test", repo_path=".")
run_tests(state, ["echo hello"])

print("Errors:", state.errors)
print("Output:")
print(state.test_output)
