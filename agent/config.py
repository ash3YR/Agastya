import yaml
from pathlib import Path


class Config:
    def __init__(self, path: str = "config.yaml"):
        config_path = Path(path)
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(config_path, "r") as f:
            raw = yaml.safe_load(f)

        planner_cfg = raw.get("planner", {})

        self.planner_provider = planner_cfg.get("provider", "fallback")
        self.planner_model = planner_cfg.get("model", None)
