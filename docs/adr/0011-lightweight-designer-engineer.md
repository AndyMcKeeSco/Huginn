# ADR 0011 — Designer and Engineer deliberately lightweight in v1

**Status:** Accepted

## Context
Huginn's v1 purpose is to validate **product reasoning, research, learning, orchestration and
governance**. Building sophisticated autonomous design and engineering now would be expensive and
would distract from testing the core.

## Decision
Implement the **Product Owner** and the specialist/governance agents **in detail**, and implement
the **Designer and Engineer as deliberately lightweight** persistent agents with clear contracts
(`agents/designer/`, `agents/engineer/`, each with `CHARTER.md` + `INTERFACES.md`). The
engineering/design-adjacent skills (`technical-investigation`, `data-analytics`) are likewise
lightweight but structurally complete. This is documented explicitly as a v1 limitation.

## Consequences
- Faster path to testing the reasoning/learning system.
- Stable interfaces mean the Designer/Engineer (and their skills) can be **substantially
  expanded later** without disturbing the reasoning kernel.
- The Trio structure (ADR 0008) is preserved even while two of its members are thin.
