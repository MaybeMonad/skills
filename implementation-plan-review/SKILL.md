---
name: implementation-plan-review
description: Implementation planning workflow focused on the decisions most likely to change before coding starts. Use when the user asks for an implementation plan, plan in HTML, review the plan before implementation, focus on data models, type interfaces, UX flows, architecture choices, validation gates, or wants to reduce rework before touching code.
---

# Implementation Plan Review

Use this skill when the work is close to implementation but the user should
review high-impact decisions first. The plan should make likely pivots visible,
not bury them under mechanical task lists.

## Workflow

1. Inspect the territory:
   - Current code paths, schemas, components, tests, runtime constraints,
     product behavior, and relevant docs.
2. Identify high-change decisions:
   - Data model or schema.
   - Type interfaces or API contracts.
   - State ownership and persistence.
   - UX flow, copy, permissions, error states.
   - Migration, rollout, compatibility, or performance constraints.
3. Present decision points before the mechanical plan.
4. State the recommended path and alternatives.
5. Include validation gates:
   - Unit or integration tests.
   - Typecheck/build/lint.
   - Browser/runtime/manual checks when user-visible.
   - Data or migration verification when relevant.
6. Add pivot triggers: discoveries that should update the plan before
   continuing.
7. Put routine edits and refactors at the bottom.

## Output Shape

Use this order:

1. Goal and assumptions.
2. Decisions to review.
3. Recommended implementation path.
4. Files or modules likely touched.
5. Validation gates.
6. Pivot triggers.
7. Mechanical task list.

## Rules

- Do not over-specify mechanical implementation when the agent can infer it
  safely from local patterns.
- Do not hide uncertain decisions in a task checklist.
- If a prototype, interview, or reference pass would materially change the
  plan, recommend that before implementation.
- Use HTML only when the plan benefits from visual structure or reviewer
  scanning; otherwise Markdown is enough.
