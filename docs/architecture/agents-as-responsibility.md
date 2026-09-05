# Agents as Responsibility Boundaries

(See [ADR 0010](../adr/0010-agents-as-responsibility-boundaries.md).)

Huginn draws its agent boundaries along **persistent responsibility**, not capability or
methodology. This is the load-bearing architectural choice that keeps the system coherent as
agents are added, deepened or replaced.

## The three boundary types

| Boundary | Represents | Where it lives |
|---|---|---|
| **Agent** | a persistent responsibility | `agents/<name>/CHARTER.md` |
| **Skill** | a reusable capability | `skills/<name>/SKILL.md` |
| **Methodology** | how a capability is performed well | *inside* a skill's body |

## Why responsibility, not capability

- **Capability is shared.** "Design a Test" is a capability many contexts need; it is a *skill*
  (`test-design`) reused by the Research Orchestrator, Designer and Engineer — not an agent.
- **Responsibility is durable.** "Keep the belief model coherent" is a standing responsibility;
  it is the *Proposition Steward*, regardless of which methods it uses this week.
- **Knowledge survives the agent.** Because responsibility (not knowledge) is what an agent owns,
  Product Knowledge is canonical and shared (ADR 0012); replacing an agent does not lose truth.

## Consequences for design

1. Don't create an agent for a methodology (no "Bayesian agent"); put the method in a skill.
2. Don't duplicate a capability across agents; factor it into a skill and attach it.
3. Give each agent a charter stating its responsibility, owned entities, decision rights,
   interfaces and escalation path.
4. Decision rights are governed centrally (`governance/decision_rights.yaml`), so responsibility
   and authority are explicit and testable.
