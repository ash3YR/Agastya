from dataclasses import dataclass, field

@dataclass
class AgentState:
    repo_path: str
    task: str

    plan: dict | None = None
    context: list = field(default_factory=list)
    test_result: str | None = None

    retries: int = 0
    done: bool = False
