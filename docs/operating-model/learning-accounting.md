# Learning Accounting

Learning Accounting is Huginn's adaptation of Eric Ries's **Innovation Accounting** (see
[ADR 0015](../adr/0015-learning-accounting.md)). It is how the Product Owner accounts for
*progress as learning*, so that a sprint that shipped nothing but reduced a decisive uncertainty
is correctly recognised as progress — and a sprint that shipped a lot but learned nothing is not.

## The question it answers

> "Given what this sprint cost, how much consequential uncertainty did we reduce, and did the
> target Outcome move?"

## What it accounts for

- **Consequential uncertainty reduced** — which Propositions changed epistemic state or
  confidence, and how much that mattered to the Outcome.
- **Outcome movement** — did the target Outcome metric move, or did we learn why it will not?
- **Cost of learning** — what the sprint spent (effort, time, money) to buy that reduction.
- **Value of information gained** — was the learning worth its cost (Expected Value of
  Information, retrospectively sanity-checked)?
- **Belief-revision trail** — the before/after on the affected Propositions, drawn from their
  history.

The Learning Accounting skill (`skills/learning-accounting/`) produces this as a structured
record, referencing canonical Propositions, Learnings and the Sprint. It is an input to the
Pivot/Persevere Review, not a vanity metric.

## What it is *not*

- Not a velocity or output count. Shipping is not the unit of account.
- Not a single universal score. Like risk, it selects an appropriate lens and shows its working.
- Not a substitute for Evidence. Every claimed reduction must trace to admitted Learning.

## Relationship to risk

Risk assessment (before) and Learning Accounting (after) are two ends of the same discipline:
risk says *which uncertainty is most worth reducing*; Learning Accounting says *how much of it we
actually reduced, and at what cost*. Together they keep attention pointed at consequential
uncertainty sprint after sprint.
