# Contract Template (execution layer)

> English translation of the frozen document `CONTRACT_TEMPLATE.md`. The Simplified Chinese original is authoritative
> for governance and is the signing copy; this English copy is provided for agent reading, understanding, and reference.
> Version markers mirror the original (v1.0). Upstream references point to `HUMAN_AGENT_PARADIGM.md` and
> `DERIVED_SPECIFICATION.md`.

Version: v1.0  
Hierarchy: constitution `HUMAN_AGENT_PARADIGM.md` v1.0 → derived specification `DERIVED_SPECIFICATION.md` v1.0 → this
template  
Status: execution-layer template · produced with the Owner's authorization  
Applicable scope: the P3 contract-establishment phase; the first basis of judgment for all subsequent work (provided it
does not conflict with the constitution or the derived specification)

## Usage Rules

1. This template is filled in by the Agent at P3 and confirmed and signed by the human (the Owner); design and
   implementation must not start before the contract is established.
2. None of C1–C10 may be omitted; small tasks may shorten sections, but every section must answer "is it defined, what
   is the criterion, what is the evidence".
3. All thresholds, criteria, and budgets are proposed by the Agent and confirmed by the human; the Agent may not
   unilaterally relax them, and later changes must go through C10.
4. The contract ID is unique and versions are traceable; every change must record the reason, affected clauses, and the
   human's approval.
5. This contract must not conflict with the constitution or the derived specification; on conflict, the higher-level
   norms prevail and the matter returns to the contract process.

---

## Contract Metadata

| Field                       | Content                                             |
|:----------------------------|:----------------------------------------------------|
| Contract ID                 |                                                     |
| Version                     |                                                     |
| Product/task name           |                                                     |
| Upstream intent record      |                                                     |
| Direction-decision record   |                                                     |
| Constitutional traceability | constitution 5.2 P3, 3.2, 7.3; derived spec 2.1–2.4 |
| Status                      | `Draft` / `Signed` / `Amended` / `Terminated`       |

---

## C1 Background and Intent

**Original intent (stated by the human):**

**Agent restatement (requires human confirmation):**

**"What matters more" ordering:** 1. ______ 2. ______ 3. ______

**Key preferences and values:**

**Differences awaiting confirmation (if any):**

- [ ] The human has confirmed the restatement and ordering above.

---

## C2 Scope and Non-Goals

| No. | In-scope deliverable | Judgeable completion criterion (cite C4/C5 criterion IDs) |
|:----|:---------------------|:----------------------------------------------------------|
| S1  |                      |                                                           |
| S2  |                      |                                                           |

**Explicit non-goals (not delivered this run):**

**Product form:** (what the deliverable, runnable, usable outcome is; not limited to software)

---

## C3 Constraints and Bottom Lines

| Category                | Constraint | Non-crossable criterion | Handling on conflict |
|:------------------------|:-----------|:------------------------|:---------------------|
| Time                    |            |                         |                      |
| Cost                    |            |                         |                      |
| Risk                    |            |                         |                      |
| Safety                  |            |                         |                      |
| Compliance              |            |                         |                      |
| Privacy/confidentiality |            |                         |                      |
| Technology/resources    |            |                         |                      |

**Bottom-line statement:** safety and compliance outrank all efficiency and need metrics; human authorization never
overrides law or basic safety bottom lines.

---

## C4 Reliability Criteria

**Definition of done (DoD):** a "completed" claim is allowed only when all of the following hold:

1. the corresponding C2 deliverable runs/is usable;
2. every completion claim carries real evidence (evidence IDs pointing into the evidence package);
3. the C6 multi-view review passed with no unresolved in-contract defects;
4. failures and incomplete items are listed truthfully.

**Claim–evidence mapping (concretized for this project):**

| Claim type                   | Required evidence form                                                   | Evidence destination |
|:-----------------------------|:-------------------------------------------------------------------------|:---------------------|
| Feature/deliverable complete | runnable/usable artifact + run/use/test records                          | evidence package     |
| Quality met                  | review/test results + defect records + fix/re-verification records       | evidence package     |
| State report                 | snapshot of current real state + differences from previous state         | evidence package     |
| Performance met              | measurement plan under contract conditions + results + environment notes | evidence package     |
| Asset reused                 | source + verification records + post-reuse results                       | evidence package     |

**State-sync method:** (when to sync, what to sync, in which objective metrics)

**Failure-reporting method:** (how failures/unmet standards are reported once found, content and time limits; vague
wording forbidden)

**Prohibited behaviors:** reporting things that did not happen or were not completed; substituting simulation,
description, or imagination for real output; fabricating evidence or citing nonexistent things; replacing checkable
evidence with self-assessment.

---

## C5 Excellence Criteria (five dimensions, each judgeable)

**Filling rule:** every criterion must be writable as "object + condition + observable result + threshold/criterion +
evidence source"; adjectives alone are not allowed.

| Criterion ID | Dimension              | Object and condition | Observable result | Threshold/criterion | Evidence source and method |
|:-------------|:-----------------------|:---------------------|:------------------|:--------------------|:---------------------------|
| E6.1.x       | Sound design           |                      |                   |                     |                            |
| E6.2.x       | Complete functionality |                      |                   |                     |                            |
| E6.3.x       | Elegant implementation |                      |                   |                     |                            |
| E6.4.x       | Perfect experience     |                      |                   |                     |                            |
| E6.5.x       | Excellent performance  |                      |                   |                     |                            |

- [ ] All five dimension criteria are defined; no "adjective as acceptance" blank items.
- [ ] The human confirmed all thresholds; the Agent did not unilaterally relax them.

---

## C6 Multi-View Review Requirements

| Perspective | Problems that must be sought                                                                     | Review-record requirements                                          |
|:------------|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|
| Product     | intent drift, scope omissions, non-goal bloat, value proposition not holding                     | independent standpoint, defect-finding method, findings, conclusion |
| User        | whether target users complete independently, paths, feedback, error recovery, friction           | same                                                                |
| Engineering | design soundness, implementation craft, maintainability, quality debt, boundaries                | same                                                                |
| Adversarial | assume completion claims false; find counterexamples, exceptional paths, safety/compliance holes | same                                                                |

**Independence:** review standpoint, method, and records are independent of the production process of the content under
review; the same entity executing a review must explicitly switch standpoints and use independent methods.

**Defect closure:** Blockers/Majors must be fixed and re-verified; Minors should be fixed; any defect chosen not to fix
must reopen the contract, be human-approved out of scope, and be explicitly disclosed.

**Exit criteria:** all C5 criteria met and no known unresolved in-contract defect.

---

## C7 Autonomy Budget

| Item                   | Content             |
|:-----------------------|:--------------------|
| Authorized scope       |                     |
| Risk threshold         | escalate above this |
| Cost cap               | escalate above this |
| Self-decidable matters |                     |
| Must-escalate matters  |                     |
| Boundary-touch action  |                     |

**Rules:** no asking inside the boundaries; escalate immediately on touching a boundary; the autonomy budget may only be
adjusted by the human in a contract or explicit authorization; in-budget self-decisions must not conflict with the
contract or effectively lower the reliability or excellence standard.

---

## C8 Deliverables and Evidence List

| Category         | Concrete deliverable | Corresponding evidence/location |
|:-----------------|:---------------------|:--------------------------------|
| Product itself   |                      |                                 |
| Evidence package |                      |                                 |
| Reusable assets  |                      |                                 |
| Delivery report  |                      |                                 |

---

## C9 Acceptance Method

**Sole acceptance basis:** this contract (C2–C5, C6, C8).

**Acceptance actions:** the human verifies evidence item by item against the contract and signs the acceptance
conclusion and time; the Agent may not substitute self-justification, self-assessment, or "looks compliant" for contract
requirements.

**Forbidden:** adding out-of-contract requirements ad hoc at acceptance; new requirements must return to P0/P3 to be
re-aligned and re-priced.

---

## C10 Change, Termination, and Failure Handling

| Trigger                                                          | Handling                                                                                                                   |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| Human changes intent/constraints                                 | return to P0/P3; re-price affected parts                                                                                   |
| Facts conflict with the contract                                 | stop, report truthfully, submit a redirect/reopen proposal                                                                 |
| Contract does not cover a direction-affecting matter             | return to P3 to amend the contract                                                                                         |
| Deviation from a confirmed direction                             | must be proposed and approved first; acting first and telling later — or acting and staying silent — is forbidden          |
| Reliability and excellence cannot both be met within constraints | stop, escalate the trade-off, ask for constraint adjustment; silent trade-offs forbidden                                   |
| Human stops the project                                          | deliver what was actually completed, evidence, and an incomplete-state statement; never claim incomplete items as complete |
| Acceptance fails                                                 | fix per the contract defect list, or reopen the contract to adjust criteria                                                |

---

## Traceability and Effectiveness

| Contract section | Constitutional clauses served | Derived-spec clauses served |
|:-----------------|:------------------------------|:----------------------------|
| C1               | 1.2 S3, 4.1, 5.2 P0           | 3.1                         |
| C2               | 1.4, 5.2 P3                   | 2.1                         |
| C3               | 3.4, 7.3, 7.4                 | 2.1, 7.3                    |
| C4               | 3.1, 5.5                      | 2.1, 5                      |
| C5               | 3.2, 6.1–6.6                  | 2.2, 2.3, 6                 |
| C6               | 3.2, 6.6                      | 6.2–6.5                     |
| C7               | 7.3, A4                       | 7.3                         |
| C8               | 1.3, 5.5                      | 1.1                         |
| C9               | 5.5                           | 3.8                         |
| C10              | 5.3, 5.4, 1.4                 | 2.4, 3.11                   |

**Pre-delivery gate:** execute《Conformance Self-Check Checklist》v1.0 groups A–I with all ★ items passing; when claiming
"the paradigm has been implemented", J1–J7 must also all pass.

---

## Signature and Revision

| Role                       | Content                                                                       | Signature | Time |
|:---------------------------|:------------------------------------------------------------------------------|:----------|:-----|
| Agent drafter              | disclose pros, cons, costs, and standard strength completely and without bias |           |      |
| Human (Owner) confirmation | confirm intent, constraints, criteria, and budget                             |           |      |

| Version | Date | Change | Affected clauses | Human approval |
|:--------|:-----|:-------|:-----------------|:---------------|
|         |      |        |                  |                |
