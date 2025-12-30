"""
cli.py

Entry point for the autonomous coding agent.
"""

import argparse

from agent.state import AgentState
from agent.repo_loader import load_repository
from agent.planner import gemini_plan, fallback_plan
from agent.editor import apply_changes
from agent.tester import run_tests
from agent.analyzer import analyze
from agent.config import Config


def main():
    parser = argparse.ArgumentParser(description="Autonomous Coding Agent")
    parser.add_argument("--repo", required=True, help="Path to repository")
    parser.add_argument("--task", required=True, help="Task description")
    args = parser.parse_args()

    # Load config
    config = Config("config.yaml")

    # Initialize state
    state = AgentState(
        goal=args.task,
        repo_path=args.repo,
    )

    print("Autonomous Coding Agent")
    print(f"Repo: {args.repo}")
    print(f"Task: {args.task}")
    print(f"Planner provider: {config.planner_provider}")
    print("-" * 50)

    # Load repository
    print("[INFO] Loading repository...")
    load_repository(state)
    print(f"[INFO] Found {len(state.files)} source files")

    # Main loop
    while True:
        state.next_iteration()
        print(f"\n[INFO] Iteration {state.iteration}")

        # ---- Planning ----
        try:
            if config.planner_provider == "gemini":
                plan = gemini_plan(
                    repo_path=state.repo_path,
                    task=state.goal,
                    model=config.planner_model,
                )
                print("[INFO] Planner: gemini (active)")
            else:
                raise RuntimeError("Planner forced to fallback")
        except Exception as e:
            print(f"[WARN] Gemini failed ({e}) — using fallback planner")
            plan = fallback_plan(state.repo_path, state.goal)
            print("[INFO] Planner: fallback")

        state.plan = plan

        print("\nPLAN")
        print(plan)

        # ---- Editing ----
        # v1: editor only applies explicit changes (none by default)
        apply_changes(state, changes={}, write_to_disk=False)

        # ---- Testing ----
        tests = plan.get("tests_to_run", [])
        if tests:
            print("[INFO] Running tests...")
            run_tests(state, tests)
        else:
            print("[INFO] No tests specified")

        # ---- Analysis ----
        should_continue = analyze(state)

        if not should_continue:
            print("\n[INFO] Agent finished")
            break

    # Final report
    print("\n===== FINAL REPORT =====")
    print("Actions:")
    for action in state.actions:
        print("-", action)

    if state.errors:
        print("\nErrors:")
        for error in state.errors:
            print("-", error)
    else:
        print("\nNo errors detected")

    if state.test_output:
        print("\nTest Output:")
        print(state.test_output)


if __name__ == "__main__":
    main()
