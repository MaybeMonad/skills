---
name: brainstorm-prototype
description: Pre-implementation brainstorming and disposable prototyping for unknown knowns, taste, product direction, UX layout, visual design, workflow choices, and solution discovery. Use when the user says brainstorm, prototype before wiring, show options, I will know it when I see it, I do not know what is possible, or wants multiple approaches before touching durable app code.
---

# Brainstorm Prototype

Use this skill when the user needs to see or compare possibilities before
choosing a direction. The output should make implicit criteria visible early,
while changes are still cheap.

## Workflow

1. Identify the decision surface:
   - Product strategy, UI layout, data view, interaction model, technical
     approach, workflow, copy, or visual style.
2. Name the comparison axes:
   - Cost, ambition, risk, reversibility, UX density, implementation path,
     maintenance burden, time to validate, or taste direction.
3. Generate meaningfully different options:
   - Prefer 3-5 distinct directions over small variations.
   - Label each option by the intuition it tests.
4. Prototype only as much as needed:
   - Use static HTML, fake data, sketches, local mock state, or a minimal
     isolated component when that helps the user react.
   - Do not wire backend routes, migrations, durable state, payments, auth, or
     production side effects unless explicitly asked.
5. Explain what each option teaches and what implementation path it implies.
6. Ask the user to react to tradeoffs, not just pick a favorite.

## Output Shape

For brainstorming:
- Options table: direction, what it optimizes, tradeoffs, implementation
  implications, unknowns it tests.
- Recommendation: one default and one backup.
- Next probe: the cheapest prototype or reference check.

For prototyping:
- Prototype scope: what is real and what is fake.
- How to view it, if a file or local server is created.
- Reaction prompts: 3-5 concrete things the user should judge.

## Rules

- Make options genuinely different. Do not pad with cosmetic variants.
- Preserve exact user copy, screenshots, and semantics.
- Prefer cheap throwaway artifacts over changing the real app when the user's
  criteria are still forming.
- If prototyping would take longer than a narrow code change, say why and offer
  the smallest useful alternative.
