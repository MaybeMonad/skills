# Unknowns Taxonomy

Use this reference when the user asks for a blindspot pass or when the task is
unfamiliar enough that ordinary planning may miss the important constraints.

## Four Buckets

Known knowns:
- What the user explicitly put in the prompt.
- Examples: requested feature, exact copy, named files, screenshots, deadline,
  constraints, non-goals.

Known unknowns:
- Questions the user already knows they have.
- Examples: "I do not know the auth module", "I am unsure which data model is
  right", "I need to choose between these flows".

Unknown knowns:
- Criteria the user would recognize but has not articulated.
- Examples: visual taste, acceptable latency, expected admin workflow, brand
  tone, "this feels right", legacy behavior everyone assumes.

Unknown unknowns:
- Missing context the user has not considered.
- Examples: hidden integration constraints, runtime-only auth state,
  historical migrations, production data shape, accessibility requirements,
  compliance constraints, model/tool behavior limits, cost or queue bottlenecks.

## Intake

Capture the starting point before advising:

- User's experience with the codebase, domain, tool, or design space.
- What the user can judge confidently and what they cannot judge yet.
- What would make the solution unacceptable even if it technically works.
- The real territory to inspect: files, modules, runtime path, docs, data,
  screenshots, examples, external facts, or production behavior.
- The cost of being wrong: easy copy tweak, painful migration, user-facing
  regression, security risk, data loss, reputational risk.

## Unknown Card

For each high-leverage unknown, use this compact shape:

- Unknown: the concrete thing not yet known.
- Bucket: known unknown, unknown known, unknown unknown, or known risk.
- Evidence: what has been inspected and what has not.
- Why it matters: how a wrong assumption changes architecture, UX, cost, or
  correctness.
- Cheap probe: the smallest search, prototype, test, interview question, or
  reference read that can reduce it.
- Branch impact: what changes if the answer is A vs B.
- Decision rule: proceed, ask the user, prototype first, inspect more, or stop.

## Heuristics For Finding Blindspots

Look harder when any of these are true:

- The task enters an unfamiliar module, product surface, domain, or toolchain.
- The user gives taste-based criteria but no examples.
- The implementation crosses auth, billing, permissions, data migrations,
  queues, deployment, caching, or production data.
- The prompt is highly specific but may overfit a guessed solution.
- The prompt is highly vague and may invite generic best practices that do not
  fit the actual system.
- The task is long-horizon enough that discoveries during implementation may
  invalidate the plan.
- The user needs buy-in from reviewers who know failure modes the prompt did
  not name.

## Blindspot Pass Shape

Use this default output:

1. Starting point: what is known from the prompt and what was inspected.
2. Territory signals: important facts from code/docs/runtime/references.
3. Blindspots: prioritized unknown cards, sorted by impact.
4. Cheap probes: the next actions that reduce the most uncertainty.
5. Better prompt: a revised prompt or spec the user can give the agent next.
6. Blocking questions: only the questions whose answers would change the work.
