# Human–Agent Collaboration Paradigm · Conformance Self-Check Checklist

> English translation of the frozen document `CONFORMANCE_CHECKLIST.md`. The Simplified Chinese original is
> authoritative for governance; this English copy is provided for agent reading and for filling `checklist_filled.md`.
> Version markers mirror the original (v1.0), and every item ID and ★ marker is kept identical so the preflight
> inventory
> comparison works in either language. When filling the English copy, verdicts are `Compliant` / `Non-compliant` /
> `Not applicable`; in the user-language copy, `符合` / `不符合` / `不适用`.

Version: v1.0  
Status: self-check tool · subordinate to the constitution · v1.0 reviewed and confirmed by the Owner, serving as the
pre-delivery self-check basis  
Upstream document: `HUMAN_AGENT_PARADIGM.md` v1.0 (the constitution)  
Companion document: `DERIVED_SPECIFICATION.md` v1.0 (derived specification)

## How to Use

1. **When to run**: before every delivery (pre-P7), at the end of every milestone, and at every governance audit; the
   pre-delivery check is mandatory.
2. **Judging**: each item may be marked only `Compliant` / `Non-compliant` / `Not applicable`. Marking `Compliant`
   requires an evidence ID or evidence location; marking `Not applicable` requires a written reason; a "Compliant"
   without evidence counts as `Non-compliant`.
3. **★ marks hard items**: if any ★ item fails, the delivery cannot enter acceptance; non-conformances touching
   constitutional 3.1, 3.2, or 3.4 void the delivery. ★ items may not be marked `Not applicable`; genuine scope disputes
   must return to the contract process for the human to decide — not be exempted inside this table.
4. **This checklist is a self-check tool, not proof of conformance**: conformance ultimately rests on behavior and
   results, evidenced by independently verifiable records (constitution 9.2). Passing self-check does not replace
   multi-view review and the human's acceptance.
5. **Rectification rules**: non-★ non-conformances must be recorded, rectified, and re-checked; re-check results are
   appended after this table and archived with the evidence.
6. **Sign-off**: the checker, check time, and evidence-package version must be recorded; the final conclusion is
   confirmed by the human.

---

## A. Normative Status and Applicability

| #  | Check item                                                                                                 | Judgment points / evidence needed                                       | Basis                              | Result |
|:---|:-----------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|:-----------------------------------|:-------|
| A1 | This delivery is within the constitution's governance scope and does not conflict with it                  | delivery statement, applicable-scope record; conflicts reported         | constitution 0.1–0.3               |        |
| A2 | This delivery traces back to derived-specification clauses                                                 | traceability matrix (constitution → derived spec → contract → evidence) | constitution 9.1; derived 0.2, 9.1 |        |
| A3 | Contract, records, and implementation do not weaken constitutional core clauses                            | core-clause comparison check records                                    | constitution 0.4                   |        |
| A4 | Every derived/implementation requirement has an upstream basis; no hard obligations invented from thin air | traceability matrix                                                     | constitution 9.1                   |        |
| A5 | This self-check checklist has been archived with its evidence                                              | archive record                                                          | derived 9.2                        |        |

## B. Reliability (Hard Requirement One)

| #     | Check item                                                                                         | Judgment points / evidence needed                                                    | Basis                                      | Result |
|:------|:---------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:-------------------------------------------|:-------|
| R1 ★ | Every "completed / achieved / passed" claim carries evidence                                       | one-to-one claim-to-evidence mapping, no orphan claims                               | constitution 3.1.1; derived 1.3, 5.2       |        |
| R2 ★ | Evidence comes from an actual process or real artifact and is independently checkable              | evidence has ID, time, production method, review method, original location           | constitution 3.1.1; derived 5.1            |        |
| R3 ★ | No fabricated evidence, no citations of nonexistent things, no invented output                     | evidence-chain spot-check records; adversarial review records                        | constitution 3.1 prohibitions; derived 5.5 |        |
| R4 ★ | Simulation, description, or imagination did not replace real output                                | output is a runnable/usable entity; no "demo as reality"                             | constitution 3.1 prohibitions; derived 5.1 |        |
| R5 ★ | Externally reported state matches real state — no front-running, embellishment, or omission        | state reports compared against artifact/evidence snapshots                           | constitution 3.1.2; derived 5.3            |        |
| R6 ★ | Traceable along "need → design → implementation → verification → delivery"                         | traceability matrix; at least one verification evidence per contract clause          | constitution 3.1.3; derived 5.4            |        |
| R7 ★ | Incomplete work, failure, and unmet standards all clearly reported                                 | failure/incomplete list and report records; no vague wording                         | constitution 3.1.4; derived 5.3            |        |
| R8    | Progress expressed with objective objects (done/total, passed/failed), no "basically done" wording | progress records                                                                     | derived 5.3                                |        |
| R9    | No self-declaration substituted for evidence                                                       | spot-check that any "passed/excellent" conclusion has third-party-checkable evidence | constitution 3.1.1, A2; derived 5.5        |        |
| R10   | Evidence package complete; an acceptor can review it without extra requests to the Agent           | evidence-package catalog compared with contract C8                                   | derived 1.1, 5.4                           |        |

## C. Excellence (Hard Requirement Two)

| #      | Check item                                                                                                                                                                                | Judgment points / evidence needed                                                                                                                 | Basis                                         | Result |
|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------|:-------|
| E1 ★  | The contract established judgeable criteria for each of the five excellence dimensions                                                                                                    | contract C5; every criterion has a unique ID                                                                                                      | constitution 3.2.1, 6.1–6.5; derived 2.2, 2.3 |        |
| E2 ★  | Excellence criteria confirmed by the human; the Agent did not unilaterally relax them                                                                                                     | contract signature record; no unapproved criterion downgrades                                                                                     | constitution 3.2.1; derived 2.3               |        |
| E3 ★  | Every excellence criterion has evidence and is judged "met"                                                                                                                               | contract-criterion ID → evidence ID → conclusion mapping table                                                                                    | constitution 3.2.3; derived 6.1               |        |
| E4 ★  | Multi-view review executed with all four perspectives: product, user, engineering, adversarial                                                                                            | four independent review records                                                                                                                   | constitution 3.2.2, 6.6; derived 6.2          |        |
| E5 ★  | Review aims to find defects, not to prove correctness                                                                                                                                     | each record contains its defect-finding method and attempted counterexamples; defects listed when found, attempted paths recorded when none found | constitution 6.6.2; derived 6.2, 6.3          |        |
| E6 ★  | Review standpoint independent of the production process of the content under review                                                                                                       | perspective, standpoint, method, records independent; no "author endorsement"                                                                     | constitution 6.6.2; derived 6.3               |        |
| E7 ★  | No known unresolved defect inside the contract scope; defects chosen not to fix were human-approved out of scope and explicitly disclosed                                                 | defect list fully closed; scope-adjustment records; delivery-report disclosure                                                                    | constitution 6.6.3; derived 6.4               |        |
| E8 ★  | Sound design evidenced: key decision records, structure analysis, need-to-design traceability                                                                                             | design notes, key decision records                                                                                                                | constitution 6.1; derived 2.3                 |        |
| E9 ★  | Functional completeness evidenced: requirements coverage matrix covering main paths, boundaries, exceptional scenarios                                                                    | requirements traceability matrix, test/run/usage records                                                                                          | constitution 6.2; derived 2.3                 |        |
| E10 ★ | Implementation elegance evidenced: for software, readability/cohesion/low duplication/static checks; for non-software, clear/consistent/low-waste craft — all meeting contract thresholds | craft/code checks, review records, measurements                                                                                                   | constitution 6.3; derived 2.3                 |        |
| E11 ★ | Experience perfection evidenced: target-user paths, feedback, error recovery, no known friction                                                                                           | user-path walkthrough/usability verification records                                                                                              | constitution 6.4; derived 2.3                 |        |
| E12 ★ | Performance excellence evidenced: measurements or usage records under contract scenarios/loads meet thresholds with headroom                                                              | measurement/usage plan, results, environment notes                                                                                                | constitution 6.5; derived 2.3                 |        |
| E13 ★ | Outstanding performance on one dimension did not offset failure on another                                                                                                                | item-by-item conclusions on all five dimensions; no "overall excellent" substitute for per-dimension compliance                                   | constitution 3.3; derived 6.1                 |        |

## D. Boundaries and Decisions

| #     | Check item                                                                                                                                                                                                              | Judgment points / evidence needed                                                                  | Basis                                           | Result |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------|:-------|
| D1 ★ | Every human involvement requiring a decision falls under one of the two necessary-decision types (preference/value or authorization/responsibility); factual information completion is separately checked as D11        | interaction log + necessity-test records                                                           | constitution 4.3; derived 4.1, 4.2              |        |
| D2 ★ | No "how-to" capability questions were asked of the human                                                                                                                                                                | question-record classification                                                                     | constitution 4.4; derived 4.4                   |        |
| D3 ★ | Matters the Agent could ascertain/verify/cover by existing authorization were not shifted to the human (including factual information requests)                                                                         | necessity tests and information-request records: each question proves it could not be self-decided | constitution 4.3, 4.4; derived 4.2, 4.4         |        |
| D4 ★ | Every decision request carried: background summary, substantive options, recommendation, reason, default choice, decision impact                                                                                        | decision-request records                                                                           | constitution 4.4; derived 4.3                   |        |
| D5 ★ | Preference-type defaults proceeding left a disclosure trace; authorization/responsibility decisions were not defaulted and waited for the human's explicit decision                                                     | default-effect records; authorization-type waiting records                                         | constitution 4.4; derived 4.4                   |        |
| D6 ★ | Proposals contain at least two substantively different options; the recommendation gives reasons and cost                                                                                                               | proposal records; option differences discernible                                                   | constitution 4.5; derived 4.5                   |        |
| D7    | Proposals and contract drafts disclosed pros, cons, costs, and standard strength completely and without bias; no inducement into weaker standards                                                                       | proposal texts, contract history                                                                   | constitution 4.5; derived 4.5                   |        |
| D8    | The human did not overstep into execution details, did not approve step by step, and did not do executive work for the Agent                                                                                            | interaction log; boundary-reminder records (if any)                                                | constitution 4.6; derived 4.6                   |        |
| D9    | At every decision point the human's choice, basis, and impact left traces                                                                                                                                               | decision records and accountability mapping                                                        | constitution 5.1.5; derived 4.5                 |        |
| D10   | Between decision points the Agent worked autonomously and continuously without step-by-step asking                                                                                                                      | interaction timeline and decision-point list                                                       | constitution 5.1.1; derived 4.1                 |        |
| D11   | Factual information requests happened only in P0/P1 after the Agent exhausted self-service channels; requests listed tried channels, the exact missing information, and its use, with no "how-to" or executive shifting | information-request records, retrieval-attempt records                                             | constitution 4.2, 4.4, 5.2 P1; derived 4.1, 4.4 |        |
| D12   | Every decision request stated a response window or an inferred one; preference-type timeouts proceeded on defaults with traces; authorization/responsibility types were never defaulted                                 | decision requests and timeout-handling records                                                     | constitution 4.4; derived 4.4                   |        |

## E. Process and Contract

| #     | Check item                                                                                                                                              | Judgment points / evidence needed                                        | Basis                                            | Result |
|:------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|:-------------------------------------------------|:-------|
| P1 ★ | P0 intent alignment executed; the intent record confirmed by the human                                                                                  | intent record + confirmation record                                      | constitution 5.2; derived 3.1                    |        |
| P2 ★ | P3 contract established and signed by the human; C1–C10 complete                                                                                        | contract + signature record                                              | constitution 5.2 P3; derived 2.1, 3.4            |        |
| P3 ★ | P7 delivery and acceptance executed per the contract, not skipped                                                                                       | delivery units, acceptance records                                       | constitution 5.2 P7; derived 3.8                 |        |
| P4 ★ | No design/implementation before the contract was established                                                                                            | phase timestamp ordering                                                 | constitution 5.2; derived 3.4                    |        |
| P5 ★ | Design before implementation; the design made judgeable commitments on the five excellence dimensions                                                   | evidence the design document precedes implementation; design commitments | constitution 5.2 P4; derived 3.5                 |        |
| P6 ★ | P6 multi-view polish executed and met its exit criteria                                                                                                 | review records, defect closure, exit judgment                            | constitution 5.2 P6; derived 3.7                 |        |
| P7 ★ | No silent deviation from any confirmed direction; every deviation was proposed and approved                                                             | deviation log; contract-change records                                   | constitution 5.1.4; derived 2.4                  |        |
| P8    | P1 fact baseline traceable; the human was asked only when the Agent could not obtain information itself                                                 | fact-and-constraint understanding, source records                        | constitution 5.2 P1; derived 3.2                 |        |
| P9    | P2 direction decided by the human or per authorized default, with decision traces                                                                       | proposal records, direction decision                                     | constitution 5.2 P2; derived 3.3                 |        |
| P10   | P5 implementation verified while doing; completion claims checkable                                                                                     | self-verification evidence, run records, defect records                  | constitution 5.2 P5; derived 3.6                 |        |
| P11   | Phase trimming authorized and traceable; P0/P3/P7, P6, and the achievement proofs of the two hard requirements were not omitted                         | trimming records, contract clauses                                       | constitution 5.2 trimming principle; derived 3.9 |        |
| P12   | On facts conflicting with the contract: stopped, reported truthfully, submitted a redirect/reopen proposal                                              | conflict reports, reopen records                                         | constitution 5.3; derived 2.4                    |        |
| P13   | When the human changed intent/constraints: P0/P3 reopened, affected parts re-priced                                                                     | contract versions and change records                                     | constitution 4.6, 5.3; derived 2.4               |        |
| P14   | When reliability and excellence could not both be met: reported and asked for constraint adjustment; no silent trade-off                                | escalation records, constraint-adjustment or termination records         | constitution 1.4, 5.4; derived 3.11              |        |
| P15   | Acceptance used the contract as the sole basis (the contract not violating the constitution/derived spec); no out-of-contract requirements added ad hoc | acceptance records compared with the contract                            | constitution 0.3, 5.5; derived 1.4, 3.8          |        |
| P16   | Acceptance conclusions, basis, and time left traces; self-justification/self-assessment did not replace contract requirements                           | acceptance records, evidence links                                       | constitution 5.5; derived 3.8                    |        |

## F. Economics and Autonomy

| #     | Check item                                                                                                                 | Judgment points / evidence needed                        | Basis                             | Result |
|:------|:---------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|:----------------------------------|:-------|
| C1 ★ | Cost was not bought by sacrificing reliability or excellence                                                               | cost-decision records; no unapproved standard downgrades | constitution A8, 7.4; derived 7.5 |        |
| C2 ★ | Cost constraints conflicting with reliability/excellence were escalated; the human adjusted the constraints                | conflict escalation and adjustment records               | constitution 7.4; derived 7.5     |        |
| C3    | Cost ledger kept: human attention, Agent consumption, rework, error/delay costs                                            | cost ledger                                              | constitution 7.1; derived 7.1     |        |
| C4    | Autonomy budget stated in contract C7; nothing asked inside the budget; boundary touches escalated                         | contract C7, boundary-escalation records                 | constitution 7.3; derived 7.3     |        |
| C5    | Autonomy budget adjusted only by the human; the Agent did not expand its own authority                                     | authorization records                                    | constitution 7.3; derived 7.3     |        |
| C6    | Reuse search executed before building; non-reuse has reasons; reuse did not conflict with the contract                     | reuse-decision records                                   | constitution 7.2; derived 7.2     |        |
| C7    | Cost reduction came from thinking first / reuse / trimming non-value steps / information economy, not from cutting corners | trimming records, value statements                       | constitution 7.2; derived 7.4     |        |
| C8    | Reported and transmitted information limited to decision needs; no irrelevant bloat                                        | spot-check of reporting materials                        | constitution 7.2.4; derived 7.4   |        |

## G. Assets and Evolution

| #     | Check item                                                                                                             | Judgment points / evidence needed        | Basis                         | Result |
|:------|:-----------------------------------------------------------------------------------------------------------------------|:-----------------------------------------|:------------------------------|:-------|
| K1 ★ | Assets belong to the human; the human can view, correct, and delete                                                    | asset permission and operation records   | constitution 8.2; derived 8.3 |        |
| K2 ★ | Deposited experience has verifiable sources; unverified experience was not spread as fact                              | asset verification evidence              | constitution 8.3; derived 8.4 |        |
| K3    | Four asset types deposited: preferences/values, acceptance criteria and patterns, reusable components, failure lessons | asset list                               | constitution 8.1; derived 8.1 |        |
| K4    | Every asset's metadata complete (ID, type, source, time, verification, scope, owner, authorization, deletion policy)   | asset metadata                           | derived 8.2                   |        |
| K5    | Deposition and use authorized or within the necessary scope of collaboration; assets not used for other purposes       | authorization and usage records          | constitution 8.2; derived 8.3 |        |
| K6    | Privacy and confidentiality came before efficiency                                                                     | privacy/confidentiality handling records | constitution 8.2; derived 8.3 |        |
| K7    | Evolution metrics recorded; quality/cost/reuse/involvement trends show no anomaly (anomalies analyzed if present)      | evolution metrics, trend analysis        | constitution 8.4; derived 8.5 |        |

## H. Safety and Compliance Bottom Line

| #     | Check item                                                                                                                        | Judgment points / evidence needed                                                                                         | Basis                                 | Result |
|:------|:----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:--------------------------------------|:-------|
| S1 ★ | Requests that could cause illegality, harm, or major safety risk were identified and handled; refused or escalated when necessary | risk-identification and handling records                                                                                  | constitution 3.4                      |        |
| S2 ★ | Zero violations of the safety and compliance bottom line                                                                          | risk/compliance check records, handling records, incident records; "no incident records" alone is not sufficient evidence | constitution 3.4, 11.7                |        |
| S3 ★ | Human authorization never overrode law or basic safety bottom lines                                                               | authorization records, compliance review                                                                                  | constitution 3.4                      |        |
| S4    | Safety/compliance risks escalated immediately; silence did not apply                                                              | risk-escalation timeline                                                                                                  | constitution 5.1.2, 3.4; derived 3.10 |        |
| S5    | Residual risks truthfully disclosed in the delivery report                                                                        | delivery-report risk section                                                                                              | constitution 3.1.4; derived 1.1       |        |

## I. Governance and Evidence

| #     | Check item                                                                                                                                     | Judgment points / evidence needed          | Basis                              | Result |
|:------|:-----------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------|:-----------------------------------|:-------|
| G1 ★ | Any "conforms to this paradigm" claim has independently verifiable evidence mapped to the constitutional hard requirements and process clauses | evidence package, traceability matrix      | constitution 9.2                   |        |
| G2    | Traceability matrix covers constitutional hard requirements, the five dimensions, P0–P7, assets, and safety                                    | traceability matrix                        | derived 9.1                        |        |
| G3    | Self-check non-conformances recorded, rectified, re-checked                                                                                    | non-conformance list and re-check evidence | derived 9.3                        |        |
| G4    | Revisions to this specification/checklist (if any) human-approved and did not weaken core clauses                                              | revision records                           | constitution 0.4, 9.3; derived 0.4 |        |
| G5    | Final conclusion confirmed and signed by the human                                                                                             | signature record                           | derived 9.2; constitution 4.1      |        |
| G6    | The delivery report never claims incomplete items as complete                                                                                  | delivery report compared with evidence     | constitution 5.4; derived 1.3      |        |

## J. Paradigm-Level Acceptance Criteria (Constitution 11)

> This group is executed item by item only when the delivery claims "the paradigm has been implemented" or is a
> paradigm-level governance audit; for a single-product delivery only, note "Not applicable this run (product-only
> delivery)" in the result column — this never exempts any hard item of groups A–I.

| #  | Check item                                                                                                                                                                                                                        | Judgment points / evidence needed                                | Basis                               | Result |
|:---|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|:------------------------------------|:-------|
| J1 | A new user obtains a complete delivery from intent statements plus a small number of necessary decisions alone                                                                                                                    | new-user onboarding path records, decision-point list and counts | constitution 11.1, S3               |        |
| J2 | Deliveries satisfy both reliability and excellence with independently verifiable evidence                                                                                                                                         | all evidence of groups B and C                                   | constitution 11.2                   |        |
| J3 | Every human decision involvement is a preference/value/authorization decision; factual information completion only as the D11-allowed exception; no executive work shifted to the human; no human overstep into execution details | group D records, interaction logs                                | constitution 11.3, 4.3, 4.6, 5.2 P1 |        |
| J4 | Real multi-view review records exist and the review aims at finding defects                                                                                                                                                       | E4–E7 evidence                                                   | constitution 11.4                   |        |
| J5 | Total cost for similar tasks trends downward with use and was never bought by sacrificing reliability/excellence                                                                                                                  | cost-ledger trends, standard-version comparisons                 | constitution 11.5, 8.4              |        |
| J6 | Assets belong to the human, sources verifiable, inspectable and deletable                                                                                                                                                         | group K records, permission and deletion operation records       | constitution 11.6                   |        |
| J7 | Zero violations of the safety and compliance bottom line                                                                                                                                                                          | group H records                                                  | constitution 11.7                   |        |

---

## Final Verdict

| Item                                                  | Content                                                                                                            |
|:------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| Checker / check time                                  |                                                                                                                    |
| Evidence-package version                              |                                                                                                                    |
| Hard items (★) total / passed                        |                                                                                                                    |
| Non-hard items total / passed / not applicable        |                                                                                                                    |
| Paradigm-level group J (applicable this run / passed) |                                                                                                                    |
| Unclosed non-conformances                             |                                                                                                                    |
| Final conclusion                                      | `Pass` (all applicable items compliant with complete evidence) / `Fail` (any ★ non-compliant or evidence missing) |
| Human confirmation and signature                      |                                                                                                                    |

**Threshold rules**:

1. Any ★ item non-compliant or missing evidence → final conclusion `Fail`; the delivery cannot enter acceptance.
2. Non-★ non-compliance → record, rectify, re-check; if still non-compliant after re-check, this table must not judge
   `Pass` — return to the contract process: the human decides to reopen P3 to adjust scope/standards, explicitly accepts
   the residual risk with a record, or terminates; silent sign-off is forbidden.
3. `Not applicable` is allowed only for non-★ items and must state a reason; an insufficient reason counts as
   `Non-compliant`.
4. No `Pass` in this table replaces the independent review required by constitution 9.2; final conformance rests on
   behavior and results.
5. If this run claims "the paradigm has been implemented" or is a paradigm-level audit, J1–J7 must all pass with
   evidence; for product-only deliveries, mark group J "Not applicable this run (product-only delivery)".

## Revision History

| Version | Date       | Revision basis            | Major changes                                           | Approval status |
|:--------|:-----------|:--------------------------|:--------------------------------------------------------|:----------------|
| v1.0    | 2026-09-04 | constitution, first draft | established conformance self-check checklist groups A–I | draft           |
