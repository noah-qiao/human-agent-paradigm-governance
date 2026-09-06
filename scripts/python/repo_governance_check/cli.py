"""Command line entry point for repo_governance_check."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import time

from .checks import CheckContext, _upper_name, run_all_checks
from .config import load_config
from .report import render_console, render_json, render_markdown, result_payload


def find_config(root):
    """Locate the check config: explicit root copy first, then the bundled
    default that ships next to this package."""
    candidates = [
        root / "governance_check_config.json",
        Path(__file__).resolve().parent / "governance_check_config.json",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def detect_docs_dir(root, config):
    """Pick the directory holding the governance document set.

    Candidates mirror the repository layouts: the root itself, the package's
    per-language assets directories (ZH_CN holds the frozen Chinese
    originals, EN the English translations), the project docs directory, and
    a consumer workspace's .hap/docs/ directory. Falls back to the root so an
    explicit --config against arbitrary directories keeps the historical
    semantics (missing files surface as G01 findings).
    """
    candidates = [
        root,
        root / "assets" / "ZH_CN",
        root / "assets" / "EN",
        root / "assets",
        root / "vendor" / "governance-snapshot" / "ZH_CN",
        root / "vendor" / "governance-snapshot" / "EN",
        root / "vendor" / "governance-snapshot",
        root / "docs",
        root / ".hap" / "docs",
    ]

    def _doc_exists(candidate, name):
        return (candidate / name).is_file() or (candidate / _upper_name(name)).is_file()

    for candidate in candidates:
        if all(_doc_exists(candidate, name) for name in config["required_files"]):
            return candidate
    return root


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="repo_governance_check",
        description="Check governance documents for structural consistency.",
    )
    parser.add_argument("--root", default=".", help="repository root to check")
    parser.add_argument(
        "--config",
        default=None,
        help="path to governance_check_config.json (default: ROOT or the bundled package copy)",
    )
    parser.add_argument(
        "--out-dir",
        default="reports",
        help="directory for generated reports (default: ROOT/reports)",
    )
    parser.add_argument(
        "--format",
        choices=("json", "markdown", "both"),
        default="both",
        help="report format to write",
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    root = Path(args.root).resolve()
    if args.config:
        config_path = Path(args.config).resolve()
    else:
        config_path = find_config(root)
        if config_path is None:
            raise SystemExit(
                "no governance_check_config.json found under --root "
                "or next to the package; pass --config explicitly"
            )
    out_dir = Path(args.out_dir)
    if not out_dir.is_absolute():
        out_dir = root / out_dir
    config = load_config(config_path)
    docs_dir = detect_docs_dir(root, config)
    context = CheckContext(root, config, docs_dir)
    started = time.perf_counter()
    findings = run_all_checks(context)
    elapsed = time.perf_counter() - started
    run_id = datetime.now(timezone.utc).strftime("RGC-%Y%m%d-%H%M%S")
    payload = result_payload(run_id, root, config_path, docs_dir, elapsed, findings)
    out_dir.mkdir(parents=True, exist_ok=True)
    if args.format in ("json", "both"):
        (out_dir / "repo_governance_check_report.json").write_text(
            render_json(payload), encoding="utf-8"
        )
    if args.format in ("markdown", "both"):
        (out_dir / "repo_governance_check_report.md").write_text(
            render_markdown(payload), encoding="utf-8"
        )
    print(render_console(payload))
    return 1 if payload["summary"]["total_findings"] else 0
