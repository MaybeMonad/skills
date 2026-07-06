---
name: implementation-notes
description: During-implementation notes workflow for logging decisions, deviations, edge cases, conservative choices, evidence, and open questions while an agent implements a plan. Use when the user asks to keep implementation-notes.md or notes, when unknowns may appear during implementation, when the plan may need to change, or when a future attempt should learn from this run.
---

# Implementation Notes

Use this skill to preserve what the agent learns while implementing. The notes
are a temporary map of where the actual territory differed from the plan.

## Workflow

1. Create or maintain `implementation-notes.md` only when useful or requested.
2. Record the plan snapshot:
   - Goal, key constraints, planned approach, and validation gates.
3. Log decisions made without user input:
   - Decision, reason, alternatives, and why the chosen option is conservative.
4. Log deviations:
   - Original plan, discovered edge case, new approach, and user-visible impact.
5. Log evidence:
   - Files inspected, commands run, tests, runtime observations, screenshots, or
     source links.
6. Log open questions:
   - Questions that remain after implementation, with whether they block
     release, review, or a follow-up.
7. Before final response, summarize the notes or package them into a handoff.

## Suggested File Shape

```md
# Implementation Notes

## Plan Snapshot

## Decisions

## Deviations

## Edge Cases

## Evidence

## Open Questions

## Next Prompt
```

## Rules

- Keep notes factual and short. Do not turn them into a diary.
- Surface deviations immediately when they change architecture, data shape,
  user-facing behavior, risk, or scope.
- If the deviation is local and conservative, log it and keep moving.
- Remove temporary notes if they are not meant to remain in the repo.
- If notes reveal the plan is wrong, update the plan before continuing.
