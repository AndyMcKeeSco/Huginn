# Worked Example — Multi-organisation complaints

> **Challenge:** *Reduce customer confusion in a multi-organisation complaints process.*

This end-to-end example exercises the whole Huginn model with **validated canonical records**
(each file validates against `schemas/`, checked by `tests/test_examples_validate.py`). It shows
the reasoning kernel, the operating loop over two sprints, belief revision, a risk change, and
**both** AI Chief of Staff outcomes — a considered non-escalation and a required human Decision
Brief.

## The chain

```
Challenge  INT-challenge-complaints
  └─ Impact  INT-impact-trust
       └─ Outcome  INT-outcome-first-time-routing   (measure: first-time-correct routing ≥ 80%)
             └─ Target Opportunity  OPP-identify-owner
                   └─ Proposition (assumption)  PROP-cannot-identify
                         └─ Test  TEST-card-sort  ──produces──▶  Evidence  EV-cardsort-accuracy
                                                                       └─▶ Learning  LRN-misid (canonical)
                                                                              └─▶ belief update: PROP-cannot-identify  open/0.4 → supported/0.8
```

### Sprint 1 — persevere

- **Risk (`DEC-risk-01`):** the decisive uncertainty is whether complainants can identify the
  owner unaided.
- **Sprint (`SPR-01`):** goal = reduce that uncertainty; runs `TEST-card-sort` (the least costly
  sufficiently reliable method).
- **Evidence (`EV-cardsort-accuracy`):** 25% correct identification — moderate strength, honest
  limitations. Note the **prototype/materials** (`ART-cardsort-materials`) are *not* Evidence;
  the observed interaction is.
- **Learning (`LRN-misid`, canonical):** most complainants cannot identify the owner unaided —
  bounded by its limitations.
- **Belief revision:** `PROP-cannot-identify` rises to supported/0.8 (see its `history`).
- **Learning Accounting (`DEC-la-01`)** → **Sprint Outcome (`SPO-01`)** → **Pivot/Persevere
  (`PPR-01`): persevere.**
- **AI Chief of Staff (`briefs/DB-01-no-escalation.yaml`): NO escalation.** Everything was within
  delegated authority; escalating would be noise.

### Between sprints — a risk change

- **Product Scout** files `SIG-regulation`: a regulator now requires ownership to be set at
  **intake**, which `may_invalidate` the assumption `PROP-routing-is-lever` and seeds candidate
  `OPP-upstream-ownership`.
- **Risk shifts (`DEC-risk-02`):** the most consequential uncertainty is now *cause vs symptom* —
  is complainant-side routing even the right lever?

### Sprint 2 — pivot recommended

- **Sprint (`SPR-02`):** test whether confusion originates upstream via `TEST-intake-review`.
- **Evidence (`EV-intake-process`)** → **Learning (`LRN-upstream`, canonical)**, which
  **contradicts** `PROP-routing-is-lever` (downgraded to mixed/0.35).
- **Pivot/Persevere (`PPR-02`): pivot_reframe_recommended**, raising Pivot/Reframe Recommendation
  `PRR-reframe-outcome` (originated by the **Product Owner only**, `scope: outcome`).
- **AI Chief of Staff (`briefs/DB-02-escalate.yaml`): ESCALATE.** A reserved human decision
  (`decide_pivot_reframe`) and a possibly-invalidated strategic assumption are in play. The brief
  is decision-first, lists options and consequences, names the authority (**human**), and stays
  traceable to canonical ids.

## Governance demonstrated

- The **Challenge is never changed autonomously**; the reframe is only *recommended* to a human.
- Only the **Product Owner** originates the Pivot/Reframe Recommendation.
- Only the **AI Chief of Staff** authors the Decision Briefs, and it does not itself decide,
  reprioritise, or change Intent.
- Only the **Learning Steward** marks Learning `canonical: true`.

## Canvases (projections)

- `canvases/CNV-intent-outcomes.yaml` — the Intent hierarchy and target Opportunity.
- `canvases/CNV-risk-confidence.yaml` — the risk & confidence picture at the end of Sprint 2.

Every canvas element references canonical record ids; `tests/test_canvas_refs.py` checks the
references resolve.

## Validate it yourself

```bash
python scripts/validate.py examples/complaints
pytest -q
```
