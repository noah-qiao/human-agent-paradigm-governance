"""Render check results as JSON, Markdown, and console summaries."""

import json
from collections import Counter


def summarize(findings):
    by_rule = Counter(finding.rule_id for finding in findings)
    return {
        "total_findings": len(findings),
        "findings_by_rule": dict(sorted(by_rule.items())),
    }


def result_payload(run_id, root, config_path, docs_dir, elapsed_seconds, findings):
    return {
        "run_id": run_id,
        "root": str(root),
        "docs_dir": str(docs_dir),
        "config_path": str(config_path),
        "elapsed_seconds": round(elapsed_seconds, 4),
        "summary": summarize(findings),
        "findings": [finding.to_dict() for finding in findings],
    }


def render_json(payload):
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def render_markdown(payload):
    summary = payload["summary"]
    lines = [
        "# repo_governance_check 结构检查报告",
        "",
        "> 本报告仅表示结构检查结果，不构成对文档内容实质符合性的证明。",
        "",
        f"- Run ID: `{payload['run_id']}`",
        f"- Root: `{payload['root']}`",
        f"- Docs dir: `{payload['docs_dir']}`",
        f"- Config: `{payload['config_path']}`",
        f"- Elapsed: {payload['elapsed_seconds']} s",
        f"- Total findings: {summary['total_findings']}",
        "",
        "## 规则汇总",
        "",
        "| 规则 | 发现数 |",
        "| :--- | :--- |",
    ]
    for rule_id, count in summary["findings_by_rule"].items():
        lines.append(f"| {rule_id} | {count} |")
    lines.extend(["", "## 发现清单", ""])
    if not payload["findings"]:
        lines.append("无发现。")
    else:
        lines.extend(
            [
                "| 规则 | 严重度 | 文件 | 行号 | 消息 | 证据 |",
                "| :--- | :--- | :--- | :--- | :--- | :--- |",
            ]
        )
        for finding in payload["findings"]:
            lines.append(
                "| {rule_id} | {severity} | `{file}` | {line} | {message} | {evidence} |".format(
                    **finding
                )
            )
    lines.append("")
    return "\n".join(lines)


def render_console(payload):
    summary = payload["summary"]
    status = "STRUCTURAL FAIL" if summary["total_findings"] else "STRUCTURAL PASS"
    return (
        f"{status}: {summary['total_findings']} structural finding(s) "
        f"in {payload['root']} (docs: {payload['docs_dir']}, "
        f"{payload['elapsed_seconds']} s)"
    )
