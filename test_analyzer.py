from agent.state import AgentState
from agent.analyzer import analyze

# Case 1: No errors → stop
state1 = AgentState(goal="test", repo_path=".")
print("Should continue:", analyze(state1))

# Case 2: Errors but iterations left → continue
state2 = AgentState(goal="test", repo_path=".")
state2.record_error("failure")
print("Should continue:", analyze(state2))

# Case 3: Errors + max iterations reached → stop
state3 = AgentState(goal="test", repo_path=".")
state3.record_error("failure")
state3.iteration = state3.max_iterations
print("Should continue:", analyze(state3))
