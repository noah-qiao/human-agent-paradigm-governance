"""Allow ``python -m repo_governance_check``."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
