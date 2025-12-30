Autonomous Coding Agent (Iteration 1)
What This Is

A CLI-based autonomous coding agent that analyzes a code repository and produces structured, auditable plans for code changes using an LLM-driven planner with deterministic fallback.

This project focuses on engineering correctness and control, not hype.

Key Engineering Signals

Explicit state-machine–style agent design

Separation of planning vs execution

Strict JSON planning (machine-validated)

Pluggable LLM backend with graceful fallback

No unsafe or hidden code modification

What It Can Do (Iteration 1)

Accept natural-language coding tasks

Inspect a local Git repository

Generate a step-by-step modification plan

Identify target files and tests to run

Remain functional even when LLM APIs fail

Example Usage
python cli.py --repo . --task "Add unit tests for the login function"

Example Plan Output
{
  "goal": "Add unit tests for the login function",
  "steps": [
    "Inspect repository structure",
    "Identify relevant modules",
    "Apply minimal changes",
    "Run tests"
  ],
  "files_to_modify": ["tests/test_login.py"],
  "tests_to_run": ["pytest"]
}

Architecture (High-Level)
CLI → Repo Loader → Planner (LLM / Fallback) → Agent State


Planning is read-only

Execution stages are intentionally isolated

Designed for safe extension

Why This Matters

This project demonstrates:

Controlled use of LLMs in developer tooling

Failure-aware system design

Clear reasoning and observability

Industry-aligned engineering practices

Roadmap

Plan validation & guardrails

Diff-based file editing

Test execution & analysis

Recovery and retry logic