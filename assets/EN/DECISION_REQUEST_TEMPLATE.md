# Decision Request and Necessary Information Request Template (execution layer)

> English translation of the frozen document `DECISION_REQUEST_TEMPLATE.md`. The Simplified Chinese original is
> authoritative for governance; this English copy is provided for agent reading, understanding, and reference. Version
> markers mirror the original (v1.0). Upstream references point to `HUMAN_AGENT_PARADIGM.md` and
> `DERIVED_SPECIFICATION.md`.

Version: v1.0  
Hierarchy: constitution `HUMAN_AGENT_PARADIGM.md` v1.0 → derived specification `DERIVED_SPECIFICATION.md` v1.0 → this
template  
Status: execution-layer template · produced with the Owner's authorization  
Applicable scope: any interaction during P0–P7 that needs a human response; Part A is for necessary decisions
(preference/value, authorization/responsibility); Part B is for necessary information completion in P0/P1

## Usage Rules

1. Run the necessity test first: anything the Agent could ascertain, verify, or cover under existing authorization must
   not be sent to the human.
2. "How-to" capability questions are forbidden; executive work must not be shifted.
3. Part A decision requests must carry all six elements (background summary, substantive options, recommendation,
   reason, default choice, decision impact) and state a response window.
4. Preference/value types: when the human is late in responding, the default may proceed with a disclosure trace;
   authorization/responsibility types: no default — wait for the explicit decision.
5. Every request and the human's choice must be archived as proof of accountability and traceability.

---

## Part A Decision Request

### A0 Metadata

| Field         | Content                                                     |
|:--------------|:------------------------------------------------------------|
| Request ID    |                                                             |
| Contract ID   |                                                             |
| Current phase |                                                             |
| Request type  | `P preference/value` / `A authorization/responsibility`     |
| Risk level    | `High/Medium/Low` (drives the window and escalation method) |
| Created at    |                                                             |

### A1 Necessity Test (mandatory; do not send if it fails)

1. Can the matter be resolved by the Agent through information gathering, reasoning, verification, or existing
   authorization?
    - `Yes` → **stop sending; the Agent decides on its own.**
    - `No` → continue to step 2.
2. Is the matter essentially the human's preference/value, or authorization/responsibility? (choose exactly one and
   state the basis)
3. If borderline: wrong self-decision costly and irreversible → escalate; cheap and reversible → decide and disclose
   afterwards.
4. Why this request cannot be self-decided by the Agent:

### A2 Background Summary

**Enough for an independent third party to understand the facts needed for the decision, without irrelevant
information:**

**Contract clauses directly related to this decision:**

### A3 Substantive Options

**At least two for type P; for type A at least "approve/not approve". Each option states key differences, benefits,
cost, and risk.**

| Option   | Content | Key difference | Benefit | Cost/risk | Impact on standard strength |
|:---------|:--------|:---------------|:--------|:----------|:----------------------------|
| Option 1 |         |                |         |           |                             |
| Option 2 |         |                |         |           |                             |
| (if any) |         |                |         |           |                             |

**Substantive-difference check:** the options differ discernibly on key dimensions such as scope/path/quality
strategy/cost-risk/experience orientation — not rewording.

### A4 Recommendation and Reasons

| Field                                  | Content |
|:---------------------------------------|:--------|
| Recommended option                     |         |
| Recommendation reasons                 |         |
| Cost of the recommendation             |         |
| Impact of rejecting the recommendation |         |

### A5 Default Choice and Timeout Handling

| Field                             | Content                                                                                     |
|:----------------------------------|:--------------------------------------------------------------------------------------------|
| Default option                    | type P may fill one; type A must fill "no default — wait for the explicit decision"         |
| Default activation condition      | only for preference/value types when the human has not responded within the response window |
| Disclosure after default proceeds | leave a trace in the decision records and the delivery report                               |

### A6 Decision Impact

| Option   | Scope impact | Cost impact | Quality impact | Risk impact | Time impact |
|:---------|:-------------|:------------|:---------------|:------------|:------------|
| Option 1 |              |             |                |             |             |
| Option 2 |              |             |                |             |             |

### A7 Response Window

| Field                     | Content                                                                             |
|:--------------------------|:------------------------------------------------------------------------------------|
| Suggested response window |                                                                                     |
| Window basis              | risk, cost, time sensitivity                                                        |
| Timeout handling          | type P: proceed on the A5 default with a trace; type A: keep waiting, never default |

### A8 The Human's Decision and Trace

| Field                        | Content                                                      |
|:-----------------------------|:-------------------------------------------------------------|
| Human's choice               |                                                              |
| Basis of the choice          |                                                              |
| Decision-impact confirmation |                                                              |
| Decision time                |                                                              |
| Traceability references      | constitution 4.3/4.4; derived spec 4.1–4.4; contract clauses |

---

## Part B Necessary Information Request (P0/P1 only)

### B0 Pre-checks (do not send if they fail)

- [ ] This request happens in P0/P1.
- [ ] Self-service retrieval was attempted and at least one tried channel is recorded.
- [ ] The information is necessary to proceed and cannot be replaced by reasoning, verification, or existing
  authorization.
- [ ] Contains no "how-to" and requires no executive work from the human.

### B1 Request Content

| Field                                                          | Content |
|:---------------------------------------------------------------|:--------|
| Request ID                                                     |         |
| Contract/intent record                                         |         |
| Exact missing information                                      |         |
| Which factual judgment/contract clause this information serves |         |
| Self-service channels already tried                            |         |
| Why it cannot be obtained independently                        |         |
| How the Agent will degrade if it cannot be provided            |         |

### B2 The Human's Answer and Trace

| Field                             | Content                                         |
|:----------------------------------|:------------------------------------------------|
| Information provided by the human |                                                 |
| Record the information enters     | intent record / fact-and-constraint baseline    |
| Answer time                       |                                                 |
| Traceability references           | constitution 4.2, 5.2 P1; derived spec 4.1, 4.4 |

---

## Pre-Send Self-Check

- [ ] Not a "how-to" question.
- [ ] Not something the Agent could self-decide.
- [ ] Part A has all six elements; type P has ≥2 substantively different options; type A has no default.
- [ ] Response window and timeout handling stated.
- [ ] Disclosure complete and unbiased; no information advantage used to induce weaker standards.
