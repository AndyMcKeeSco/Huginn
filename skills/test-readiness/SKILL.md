---
name: test-readiness
description: Check a designed Test is ready to run — dependencies met, method feasible, ethics/data access in place — before it enters the running state.
---

# Test Readiness

## Purpose
Confirm a Test is genuinely **ready to run** so learning flows instead of stalling.

## When to use
- Between `proposed` and `running`, before committing capacity.

## When NOT to use
- To design the Test (use `test-design`).

## Inputs
- A designed Test; its dependencies; available participants/data/tools; ethics/access needs.

## Definition of Ready
- A Test record exists with method and evidence sought defined.

## Methodology selection
- **ResearchOps** readiness checklist; **Theory of Constraints** to spot the binding blocker.

## Process
1. Verify dependencies are met (data access, participants, tooling, Designer/Engineer capacity).
2. Confirm the method is executable as specified.
3. Confirm ethics/consent/data-handling where relevant.
4. Set `status: ready` or `blocked` (with the blocker recorded).

## Structured output
Updated Test `status` (ready/blocked) with blockers noted; sequencing input for the Orchestrator.

## Quality criteria
- No Test enters `running` with unmet dependencies.

## Definition of Done
- Ready Tests are runnable end-to-end; blocked ones have a named blocker and owner.

## Failure modes
- Starting Tests that stall midway.
- Ignoring ethics/data-access constraints.

## Escalation / governance
- Persistent blockers on high-consequence Tests escalate to the AI Chief of Staff.
