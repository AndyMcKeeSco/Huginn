# ADR 0013 — AI Chief of Staff governance boundary

**Status:** Accepted

## Context
An autonomous multi-agent system needs someone to manage scarce human attention and enforce
governance — but that role could easily overreach into becoming a super-agent that owns product
truth or micromanages the others.

## Decision
The **AI Chief of Staff** manages the boundary between autonomous operation and human attention by
**Management by Exception**. It authors **Decision Briefs**, enforces decision rights, and detects
cross-agent incoherence. It **must not** change Intent/Challenge, make Product Owner decisions,
originate a Pivot/Reframe Recommendation, micromanage agents, or become an alternative source of
Product Knowledge.

## Consequences
- Schema-enforced: `decision-brief.schema.json` fixes `authored_by: ai-chief-of-staff`.
- Rule-enforced: `governance/decision_rights.yaml` grants it only `author_decision_brief` and
  `escalate_to_human`.
- Test-enforced: `tests/test_governance.py::test_ai_chief_of_staff_is_boundaried`.
- It coordinates attention and governance; it does not own product truth.
