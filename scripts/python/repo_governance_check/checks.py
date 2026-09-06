"""G01-G08 governance checks.

Every rule receives a CheckContext and returns a list of Finding objects.
Rules never modify files and only read files declared in the config.
"""

from dataclasses import dataclass
import re
from pathlib import Path


ITEM_RE = re.compile(r"^\|\s*([A-Z]\d+)\s*(★)?\s*\|")
SEPARATOR_CELL_RE = re.compile(r"^:?-{1,}:?$")


@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    file: str
    line: int
    message: str
    evidence: str

    def to_dict(self):
        return {
            "rule_id": self.rule_id,
            "severity": self.severity,
            "file": self.file,
            "line": self.line,
            "message": self.message,
            "evidence": self.evidence,
        }


def _upper_name(filename):
    """Language directories store documents under uppercase underscore names;
    consumer copies keep the canonical lowercase names."""
    stem, dot, ext = filename.rpartition(".")
    return stem.replace("-", "_").upper() + dot + ext


class CheckContext:
    def __init__(self, root, config, docs_dir=None):
        self.root = Path(root)
        self.config = config
        self.docs_dir = Path(docs_dir) if docs_dir else self.root

    def doc_file(self, filename):
        """First existing document path under docs_dir (canonical or
        uppercase-underscore form); falls back to the canonical path."""
        direct = self.docs_dir / filename
        if direct.is_file():
            return direct
        upper = self.docs_dir / _upper_name(filename)
        return upper if upper.is_file() else direct


def _read_lines(ctx, filename):
    try:
        return ctx.doc_file(filename).read_text(encoding="utf-8").splitlines()
    except OSError:
        return None


def _headings(lines):
    for number, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if stripped.startswith("#"):
            yield number, stripped.lstrip("#").strip()


def _finding(ctx, rule_id, filename, line, message, evidence):
    return Finding(rule_id, "error", filename, line, message, evidence)


def _table_blocks(lines):
    blocks = []
    current = []
    for number, raw in enumerate(lines, 1):
        if raw.strip().startswith("|"):
            current.append((number, raw.strip()))
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def _cell_count(row):
    return max(row.count("|") - 1, 0)


def _is_separator(row):
    cells = [cell.strip() for cell in row.strip("|").split("|")]
    if not cells:
        return False
    return all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)


def check_required_files(ctx):
    findings = []
    for filename in ctx.config["required_files"]:
        checked = ctx.doc_file(filename)
        if not checked.is_file():
            findings.append(
                _finding(
                    ctx,
                    "G01",
                    filename,
                    0,
                    f"required file is missing: {filename}",
                    f"checked path: {checked}",
                )
            )
    return findings


def check_upstream_references(ctx):
    findings = []
    for filename, expected in ctx.config["upstream_references"].items():
        lines = _read_lines(ctx, filename)
        if lines is None:
            continue
        content = "\n".join(lines)
        for ref in expected:
            if ref not in content:
                findings.append(
                    _finding(
                        ctx,
                        "G02",
                        filename,
                        0,
                        f"missing upstream reference: {ref!r}",
                        "full-file substring check",
                    )
                )
    return findings


def check_required_headings(ctx):
    findings = []
    for filename, expected in ctx.config["required_headings"].items():
        lines = _read_lines(ctx, filename)
        if lines is None:
            continue
        present = {heading for _, heading in _headings(lines)}
        for heading in expected:
            if heading not in present:
                findings.append(
                    _finding(
                        ctx,
                        "G03",
                        filename,
                        0,
                        f"missing required heading: {heading}",
                        "heading text parsed from markdown heading lines",
                    )
                )
    return findings


def check_markdown_tables(ctx):
    findings = []
    for filename in ctx.config["required_files"]:
        lines = _read_lines(ctx, filename)
        if lines is None:
            continue
        for block in _table_blocks(lines):
            first_line, _ = block[0]
            if len(block) < 2 or not _is_separator(block[1][1]):
                findings.append(
                    _finding(
                        ctx,
                        "G04",
                        filename,
                        first_line,
                        "table has no valid separator row as its second row",
                        f"table starts at line {first_line}",
                    )
                )
                continue
            expected_columns = _cell_count(block[1][1])
            for line_number, row in block:
                if _cell_count(row) != expected_columns:
                    findings.append(
                        _finding(
                            ctx,
                            "G04",
                            filename,
                            line_number,
                            "table row column count differs from separator row",
                            f"expected {expected_columns} columns, row has {_cell_count(row)}",
                        )
                    )
    return findings


def _checklist_missing_sections(ctx, headings):
    findings = []
    checklist_config = ctx.config["checklist"]
    for section in checklist_config["sections"]:
        if section not in headings:
            findings.append(
                _finding(
                    ctx,
                    "G05",
                    "conformance_checklist.md",
                    0,
                    f"missing checklist section heading: {section}",
                    "heading inventory",
                )
            )
    final_section = checklist_config["final_section"]
    if final_section not in headings:
        findings.append(
            _finding(
                ctx,
                "G05",
                "conformance_checklist.md",
                0,
                f"missing final section heading: {final_section}",
                "heading inventory",
            )
        )
    return findings


def _checklist_row_metrics(lines):
    item_count = 0
    star_count = 0
    bad_star_rows = []
    item_ids = []
    for line_number, raw in enumerate(lines, 1):
        match = ITEM_RE.match(raw.strip())
        if not match:
            continue
        item_count += 1
        item_ids.append(match.group(1))
        if match.group(2):
            star_count += 1
            cells = [cell.strip() for cell in raw.strip().strip("|").split("|")]
            if cells and cells[-1] == "不适用":
                bad_star_rows.append(line_number)
    return item_count, star_count, bad_star_rows, item_ids


def check_checklist_invariants(ctx):
    lines = _read_lines(ctx, "conformance_checklist.md")
    if lines is None:
        return []
    headings = {heading for _, heading in _headings(lines)}
    findings = _checklist_missing_sections(ctx, headings)
    item_count, star_count, bad_star_rows, item_ids = _checklist_row_metrics(lines)
    checklist_config = ctx.config["checklist"]
    prefix_map = checklist_config.get("item_prefixes", {})
    for section in checklist_config["sections"]:
        prefix = prefix_map.get(section, section.split(".")[0])
        if not any(item_id.startswith(prefix) for item_id in item_ids):
            findings.append(
                _finding(
                    ctx,
                    "G05",
                    "conformance_checklist.md",
                    0,
                    f"checklist section has no item rows: {section}",
                    f"no item ID starts with prefix {prefix!r}",
                )
            )
    expected_items = checklist_config["expected_items"]
    if item_count != expected_items:
        findings.append(
            _finding(
                ctx,
                "G05",
                "conformance_checklist.md",
                0,
                f"checklist item count is {item_count}, expected {expected_items}",
                "item rows matching the A-Z numbering pattern",
            )
        )
    expected_stars = checklist_config["expected_star_items"]
    if star_count != expected_stars:
        findings.append(
            _finding(
                ctx,
                "G05",
                "conformance_checklist.md",
                0,
                f"star item count is {star_count}, expected {expected_stars}",
                "item rows containing the star marker",
            )
        )
    for line_number in bad_star_rows:
        findings.append(
            _finding(
                ctx,
                "G05",
                "conformance_checklist.md",
                line_number,
                "star item result column must not contain 不适用",
                "star item rows may not be exempted in the checklist source",
            )
        )
    return findings


def _check_sections(ctx, rule_id, filename, config_key):
    lines = _read_lines(ctx, filename)
    if lines is None:
        return []
    present = {heading for _, heading in _headings(lines)}
    findings = []
    for section in ctx.config[config_key]["required_sections"]:
        if section not in present:
            findings.append(
                _finding(
                    ctx,
                    rule_id,
                    filename,
                    0,
                    f"missing required section: {section}",
                    "heading inventory",
                )
            )
    return findings


def check_contract_template_sections(ctx):
    return _check_sections(ctx, "G06", "contract_template.md", "contract_template")


def check_decision_template_sections(ctx):
    return _check_sections(ctx, "G07", "decision_request_template.md", "decision_request_template")


def check_delivery_template_sections(ctx):
    return _check_sections(ctx, "G08", "delivery_report_template.md", "delivery_report_template")


ALL_RULES = (
    check_required_files,
    check_upstream_references,
    check_required_headings,
    check_markdown_tables,
    check_checklist_invariants,
    check_contract_template_sections,
    check_decision_template_sections,
    check_delivery_template_sections,
)


def run_all_checks(ctx):
    findings = []
    for rule in ALL_RULES:
        findings.extend(rule(ctx))
    findings.sort(key=lambda item: (item.file, item.line, item.rule_id))
    return findings
