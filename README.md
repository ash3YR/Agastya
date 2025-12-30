## Agastya

A **CLI-based autonomous coding agent** that analyzes a code repository and produces **structured, auditable plans** for code changes using an **LLM-driven planner with deterministic fallback**.

This project focuses on **engineering correctness and control**, not hype.

---

## Key Engineering Signals

- Explicit **state-machine–style agent design**
- Clear **separation of planning vs execution**
- **Strict JSON planning** (machine-validated)
- **Pluggable LLM backend** with graceful fallback
- No unsafe or hidden code modification

---

## What It Can Do (Iteration 1)

- Accept natural-language coding tasks  
- Inspect a local Git repository  
- Generate a step-by-step modification plan  
- Identify target files and tests to run  
- Remain functional even when LLM APIs fail  

---

## Example Usage

```bash
python cli.py --repo . --task "Add unit tests for the login function"
