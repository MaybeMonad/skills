---
name: map-territory-workflow
description: Full development workflow for matching the user's prompt or plan to the real codebase, domain, runtime, and constraints. Use when the user wants a complete unknowns-reduction process across before, during, and after implementation; asks for map vs territory thinking; wants to choose among blindspot pass, brainstorm/prototype, interview, references, implementation plan, implementation notes, pitch/explainer, or quiz; or needs a long-horizon agentic coding process that handles unknowns iteratively.
---

# Map Territory Workflow

Use this skill as the suite entrypoint. The map is the prompt, plan, context,
and artifacts. The territory is the actual codebase, domain, runtime, data,
users, constraints, and reviewer expectations. The job is to keep the map and
territory close enough that agentic work can proceed without hidden drift.

## Phase Map

Pre-implementation:
- `blindspot`: find relevant unknown unknowns and cheap probes.
- `brainstorm-prototype`: generate options or disposable prototypes when the
  user has taste or criteria they can recognize but not yet describe.
- `interview-unknowns`: ask high-leverage questions that can change the plan.
- `reference-alignment`: extract requirements from examples, source code,
  screenshots, docs, or prior work.
- `implementation-plan-review`: write a plan that foregrounds decisions likely
  to change.

During implementation:
- `implementation-notes`: log deviations, edge cases, conservative choices, and
  evidence while continuing through the work.

After implementation:
- `pitch-explainer`: package the prototype, spec, notes, decisions, and
  verification for reviewer buy-in.
- `change-quiz`: explain the change and quiz the user before merge or handoff.

## Selection Rules

- If the user is unfamiliar with the codebase/domain or asks what they may be
  missing, start with a blindspot pass.
- If the user will know the right answer only after seeing options, use
  brainstorm/prototype before durable implementation.
- If one answer can change architecture, schema, API, UX flow, or acceptance
  criteria, interview before planning.
- If the user cannot describe the target but can point to an example, analyze
  references before planning.
- If the approach seems ready but the cost of rework is high, create an
  implementation plan focused on high-change decisions.
- If implementation is underway and the territory invalidates the plan, keep
  implementation notes and surface any user-facing or architectural pivot.
- If the work is done but reviewers need confidence, create an explainer.
- If the user wants to understand the change before merging, create a quiz.

## Operating Rules

- Do not run every artifact by default. Choose the smallest chain that reduces
  the highest-cost unknown.
- Inspect local evidence before asking questions that files, docs, runtime, or
  current sources can answer.
- Separate what is known, what is assumed, what is uninspected, and what needs
  user judgment.
- Let new evidence change the path. If the territory contradicts the map,
  update the map before continuing.
- Carry forward what was learned: blindspots become plan constraints, plan
  deviations become implementation notes, and notes become explainers or quiz
  material.

## Default Output

When asked to choose a workflow, return:

1. Recommended path: the smallest artifact chain.
2. Why this path: the unknowns it reduces.
3. Do now: the immediate artifact or question.
4. Defer: artifacts that are useful later but premature now.
