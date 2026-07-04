---
name: blindspot
description: Pre-implementation blind spot pass for finding unknown unknowns before agentic coding, design, research, or domain work. Use when the user says blindspot pass, unknown unknowns, help me prompt better, I am new to this codebase/domain, I do not know what questions to ask, or wants relevant risks, hidden constraints, and cheap probes before implementation.
---

# Blindspot

Use this skill to expose the unknowns that may make the user's prompt or plan
misrepresent the real territory. The goal is to help the user prompt better and
choose a safer next step before implementation gets expensive.

## Workflow

1. Establish the starting point:
   - What the user explicitly wants.
   - What they know, do not know, and can judge by taste.
   - The codebase, domain, runtime, data, references, or real-world system that
     forms the territory.
2. Inspect before asking:
   - Search local files, docs, examples, screenshots, logs, or current external
     sources when those can answer factual unknowns.
   - State what was inspected and what is still uninspected.
3. Classify important unknowns using `references/unknowns-taxonomy.md`.
4. Prioritize only unknowns that can change architecture, scope, UX,
   correctness, safety, cost, or validation.
5. For each major blindspot, give the cheapest probe: code search, reference
   read, prototype, user question, runtime check, test, or source lookup.
6. End with a better prompt, plan constraint, or next artifact for the user to
   use.

## Output Shape

Use this structure unless the user asks for another format:

1. Starting point
2. Territory inspected
3. Top blindspots
4. Cheap probes
5. Better prompt
6. Blocking questions

## Rules

- Lead with the unknowns that could most change the work.
- Separate unknowns from risks. A risk is a known possible failure; an unknown
  is missing information that may reveal a different path.
- Do not ask a broad questionnaire. Ask only questions whose answers change the
  next step.
- Teach just enough vocabulary for the user to recognize better options.
- If the right next step is not implementation, say so and name the artifact:
  brainstorm, prototype, interview, reference analysis, or plan review.

## Resources

- `references/unknowns-taxonomy.md`: read when producing the blindspot pass or
  when the task needs a structured unknown-card format.
