"""Configuration helpers (env, YAML)."""
import os
from pathlib import Path
import yaml


def load_yaml(path: str):
    p = Path(path)
    if not p.exists():
        return {}
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def getenv(name: str, default=None):
    return os.getenv(name, default)
