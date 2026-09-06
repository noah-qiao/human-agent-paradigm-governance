"""Load and validate governance check configuration."""

import json
from pathlib import Path


REQUIRED_KEYS = (
    "required_files",
    "upstream_references",
    "required_headings",
    "checklist",
    "contract_template",
    "decision_request_template",
    "delivery_report_template",
)


def load_config(path):
    """Read a JSON config file and return the decoded object.

    The function only performs structural validation. Rule-specific values
    are consumed by the checks module.
    """
    config_path = Path(path)
    config = json.loads(config_path.read_text(encoding="utf-8"))
    missing = [key for key in REQUIRED_KEYS if key not in config]
    if missing:
        raise ValueError(f"config missing keys: {', '.join(missing)}")
    if not isinstance(config["required_files"], list):
        raise ValueError("config 'required_files' must be a list")
    if not isinstance(config["required_headings"], dict):
        raise ValueError("config 'required_headings' must be a dict")
    return config
