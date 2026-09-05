# Principles

These are Huginn's canonical principles. They are the tie-breakers: when a design or operating
choice is ambiguous, resolve it in favour of these.

1. **Knowledge survives the agent.** Product Knowledge is canonical and shared; agents are
   replaceable stewards of it.
2. **Keep the reasoning kernel small.** Five entities — Intent, Opportunity, Proposition, Test,
   Learning. Resist adding more.
3. **Agents own persistent responsibilities.** Agent boundaries represent responsibility, not
   capability.
4. **Skills perform reusable capabilities.** Capability boundaries are skill boundaries.
5. **Methodologies live inside Skills.** Do not turn a methodology into an agent.
6. **Deployment topology is separate from methodology.** OpenClaw instance boundaries are an
   implementation concern.
7. **Outputs are not Outcomes.** An Outcome is a measurable behavioural or real-world change.
8. **Opportunities are not Solutions.** An Opportunity is a need/pain/desire/problem.
9. **Every Test has a Learning Objective.** If it teaches nothing specified, it is not a Test.
10. **Every Test has an Intended Decision Consequence.** "If we learn X we will do Y."
11. **Use the least costly sufficiently reliable way to learn.** Reliability must be *sufficient
    for the decision*, not maximised for its own sake.
12. **A prototype is not Evidence.** Observed interaction with a prototype may *produce* Evidence.
13. **Evidence requires provenance.** No provenance, no canonical standing.
14. **Learning must not exceed Evidence.** Conclusions stay within what the Evidence supports.
15. **Risk determines attention.** The most consequential uncertainty gets the focus.
16. **Progress means Outcome movement and validated reduction of consequential uncertainty** —
    not activity or output volume.
17. **Humans retain authority over strategic Challenge changes.** No agent may change the
    Challenge.
18. **The AI Chief of Staff manages human attention and governance, not product truth.**
19. **Designer and Engineer are intentionally simple in v1.** Their interfaces are stable so they
    can be expanded later without disturbing the kernel.

These principles are enforced in three ways: by the schemas (`schemas/`), by the decision-rights
model (`../../governance/decision_rights.yaml`), and by the automated checks (`tests/`).
