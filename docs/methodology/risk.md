# Risk

**Risk is an assessment, not an entity** (see [ADR 0006](../adr/0006-risk-as-assessment.md)). It
does not sit in the reasoning kernel alongside Intent, Opportunity, Proposition, Test and
Learning. Instead it is **continuously assessed across the whole product model** by the Product
Owner, and its job is to **direct attention**.

## The Product Owner's standing question

> "What is the most consequential uncertainty currently standing between us and the intended
> Outcome?"

Everything the Product Owner does — Target Opportunity selection, prioritisation, Sprint Goal
proposal, Learning Accounting — is downstream of answering this question honestly and
repeatedly.

## Dimensions a risk assessment may consider

Risk is multi-dimensional. An assessment *may* weigh any of:

- **uncertainty** — how unsure are we?
- **consequence** — how much does being wrong cost?
- **value** — how much is at stake if we are right?
- **desirability** — do users want it?
- **usability** — can they use it?
- **feasibility** — can we build it?
- **viability** — does it work for the business?
- **delivery** / **operational** risk
- **cost of being wrong**
- **cost of learning**
- **time to learning**

## No single universal formula

Huginn **does not hard-code one scoring formula**. Different situations warrant different lenses
(riskiest-assumption thinking, Expected Value of Information, RICE, WSJF, decision analysis). The
Risk Assessment skill (`skills/risk-assessment/`) selects an appropriate method for the
situation and records *which* method and *why*, so the reasoning is auditable — but the framework
does not force one number.

The consistent output is a **ranked view of consequential uncertainty**, with the reasoning
attached, not a single hidden score.

## How risk drives the loop

Risk is the first step of the operating loop (`../operating-model/operating-loop.md`):

```
Assess Risk → Set Sprint Goal → Select Tests/work → …
```

The most consequential uncertainty becomes the Sprint's focus. Tests are then chosen as the
**least costly sufficiently reliable** way to reduce *that* uncertainty. Progress is measured as
**Outcome movement and validated reduction of consequential uncertainty** — not activity.

## Where risk is recorded

Risk assessments are not a separate kernel entity, but they are captured as **Decisions** and
referenced from **Sprints** (see `schemas/decision.schema.json`, `schemas/sprint.schema.json`),
so the "why this focus, why now" is always traceable. A material, unresolved, high-consequence
uncertainty is one of the exception conditions the AI Chief of Staff watches for.
