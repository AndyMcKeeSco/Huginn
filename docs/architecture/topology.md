# Topology

Huginn v1 runs as **one OpenClaw instance** containing all eight agents, operating against shared
Product Knowledge (see [ADR 0009](../adr/0009-single-openclaw-instance-topology.md)). Deployment
topology is an **implementation concern kept separate from the methodology**.

```
┌──────────────────────────── OpenClaw instance ────────────────────────────┐
│                                                                            │
│  Product Trio            Specialists                 Governance/Attention  │
│  ┌───────────────┐       ┌────────────────────┐      ┌──────────────────┐  │
│  │ Product Owner │       │ Proposition Steward│      │ AI Chief of Staff│  │
│  │ Designer (lt) │       │ Research Orchestr. │      └──────────────────┘  │
│  │ Engineer  (lt)│       │ Learning Steward   │                            │
│  └───────────────┘       │ Product Scout      │                            │
│                          └────────────────────┘                            │
│                                                                            │
│                 ▼ all read/write ▼                                         │
│        ┌───────────────────────────────────────────┐                      │
│        │   Shared canonical Product Knowledge        │                     │
│        │   (schemas/ + records; provenance; ids)     │                     │
│        └───────────────────────────────────────────┘                      │
│                                                                            │
│  Reusable capability: skills/ (SKILL.md) attached to agents by config      │
└────────────────────────────────────────────────────────────────────────────┘
```

## Mapping methodology to deployment

| Methodology concept | Deployment realisation |
|---|---|
| Agent (persistent responsibility) | one `agents.entries.*` entry in `deploy/openclaw.config.example.json5` |
| Agent charter | the agent's system prompt / responsibility description |
| Skill (reusable capability) | an OpenClaw `SKILL.md` package under a skills root, attached to agents |
| Shared Product Knowledge | records validated by `schemas/`, accessible to all agents |
| Governance (decision rights) | `governance/decision_rights.yaml`, enforced by tests and referenced by the ACoS |

## What we explicitly do *not* do in v1

- No separate OpenClaw instances for Product, Design and Engineering.
- No deployment assumptions baked into charters or schemas.

Multi-instance topologies remain possible later **without** changing the reasoning kernel or the
Product Knowledge model.
