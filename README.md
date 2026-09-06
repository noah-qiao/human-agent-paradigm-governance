# hap-governance

The **governance content package** of the Human-Agent Paradigm (HAP):
the frozen governance documents and their structural self-check tool, published as an independent npm package so content
(owner-approval cadence) and tooling (engineering cadence) release independently.

**English** | [简体中文](README.zh-CN.md)

## Contents

| Path                                    | Purpose                                                                                                                                                                                                                                                                 |
|:----------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `assets/ZH_CN/`                         | The six governance documents — Simplified Chinese originals: `HUMAN_AGENT_PARADIGM.md` (Constitution v1.0), `DERIVED_SPECIFICATION.md` (v1.0), `CONFORMANCE_CHECKLIST.md` (v1.0), `CONTRACT_TEMPLATE.md`, `DECISION_REQUEST_TEMPLATE.md`, `DELIVERY_REPORT_TEMPLATE.md` |
| `assets/EN/`                            | Official English translations of the same six documents                                                                                                                                                                                                                 |
| `scripts/python/repo_governance_check/` | Structural self-check for the document set (Python stdlib only; auto-detects `assets/ZH_CN` etc.)                                                                                                                                                                       |

## Usage

Consumers copy the `assets/` language directories into their workspace governance root

```bash
python3 -m scripts.python.repo_governance_check --root . --out-dir reports
```

## Version strategy

| Content version                                        | Package version    | Trigger                    |
|:-------------------------------------------------------|:-------------------|:---------------------------|
| Constitution v1.0                                      | 1.0.0 (baseline)   | initial release            |
| Constitution revision (major)                          | major bump         | a new Constitution version |
| Derived Specification / Checklist / Templates revision | minor / patch bump | derived-family edits       |

The Constitution version is authoritative; package versions follow it. Every content amendment requires explicit owner
approval in a HAP flow (Constitution §0.4, Derived Specification §0.4). Tooling changes to the checker do not change the
governance content.

## Governance

This repository is governed by its own content (the HAP Constitution). Amendments are made through HAP runs with owner
sign-off; publishing is an owner-authorized action.
