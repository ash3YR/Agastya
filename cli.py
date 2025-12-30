import argparse
from rich import print
from agent.repo_loader import load_repo
from agent.planner import create_plan

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--task", required=True)
    args = parser.parse_args()

    print("[bold green]Autonomous Coding Agent[/bold green]")
    print(f"Repo: {args.repo}")
    print(f"Task: {args.task}")

    print("[INFO] Loading repository...")
    repo_files = load_repo(args.repo)
    print(f"[INFO] Found {len(repo_files)} Python files")

    print("[yellow]Planning...[/yellow]")
    plan = create_plan(args.task, repo_files)

    print("[bold]PLAN[/bold]")
    print(plan)

if __name__ == "__main__":
    main()
