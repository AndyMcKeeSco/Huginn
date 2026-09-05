# ADR 0009 — Single OpenClaw instance topology

**Status:** Accepted

## Context
Huginn's agents could be deployed many ways (one instance, several instances, per-discipline
instances). Deployment choices are an **implementation concern** and must not leak into the
methodology.

## Decision
For v1, run Huginn as **one OpenClaw instance** containing all agents, operating against shared
Product Knowledge. **Do not** create separate OpenClaw instance configurations for Product, Design
and Engineering. Optimise for simplicity.

## Consequences
- One deployment config: `deploy/openclaw.config.example.json5`, mapping each agent charter to an
  `agents.entries.*` entry with attached skills.
- Topology stays separate from methodology (a core principle): the charters and schemas contain no
  deployment assumptions.
- Multi-instance topologies remain possible later without changing the reasoning model.
- OpenClaw skill format per <https://docs.openclaw.ai/tools/skills>.
