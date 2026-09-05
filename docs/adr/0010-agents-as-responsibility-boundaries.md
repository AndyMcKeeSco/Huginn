# ADR 0010 — Agents as responsibility boundaries

**Status:** Accepted

## Context
There are several candidate axes for drawing agent boundaries: by capability, by methodology, or
by persistent responsibility. Boundaries by capability duplicate reusable work across agents;
boundaries by methodology turn methods into actors.

## Decision
**Agent boundaries represent persistent responsibility.** **Skill boundaries represent reusable
capability.** **Methodologies live inside skills.** Each agent has a durable charter
(`agents/<name>/CHARTER.md`) describing what it is responsible for and its decision rights.

## Consequences
- Reusable capability is factored into `skills/` and shared across agents.
- A methodology (e.g. Bayesian updating) is never an agent; it is used inside a skill.
- Knowledge survives the agent: Product Knowledge is canonical and shared (ADR 0012).
- See `docs/architecture/agents-as-responsibility.md` and
  `docs/architecture/skills-vs-methodology.md`.
