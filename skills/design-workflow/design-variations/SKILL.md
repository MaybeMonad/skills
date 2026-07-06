---
name: design-variations
description: Design variation workflow for options, alternatives, wireframes, multiple takes, visual explorations, layout comparisons, flow comparisons, or taste discovery before committing to one direction.
---

# Design Variations

Use this skill when seeing alternatives is the cheapest way to find the right
design. Variations should test real design decisions, not cosmetic swaps.

## Workflow

1. Define the decision surface:
   - Screen, component, flow, page, deck section, visual direction, interaction
     model, or content hierarchy.
   - Completion criterion: the scope and comparison unit are clear.
2. Establish the baseline:
   - Existing system to preserve, source-map constraints, user-supplied copy,
     target medium, audience, and fidelity level.
   - Completion criterion: each variation starts from the same real brief.
3. Pick axes worth testing:
   - Layout, hierarchy, density, visual tone, typography, interaction model,
     information architecture, copy strategy, component style, or motion.
   - Completion criterion: each axis can change the final implementation or
     product judgment.
4. Produce distinct options:
   - Prefer 3 options by default: safe, refined, and edge.
   - Use 2 when scope is narrow and 4-5 only when the user asked for breadth.
   - Completion criterion: any two options differ in more than color, radius,
     shadow, or accent treatment.
5. Present for comparison:
   - Keep options in one artifact when practical: one file, canvas, storyboard,
     toggle panel, or compact table.
   - Label each option by what it tests and the tradeoff it carries.
   - Completion criterion: the user can compare without opening scattered
     files or guessing what changed.
6. Recommend:
   - Pick a default and a backup.
   - Name what to borrow from rejected options if useful.
   - Completion criterion: the recommendation links design taste to execution
     cost, risk, and fit.

## Output Shape

- Decision surface.
- Axes tested.
- Options: label, design bet, what changes, tradeoffs, implementation impact.
- Recommendation: default, backup, and mix-and-match notes.
- Next step: direction lock, prototype, production implementation, or polish.

## Rules

- Do not pad with cosmetic variants. If the only difference is color, drop it.
- Preserve exact copy and required semantics across options unless copy is an
  explicit variation axis.
- Use low-fidelity wireframes when structure is the unknown; use hi-fi when
  visual taste is the unknown.
- Avoid durable backend, auth, payment, migration, or production data changes
  while the design choice is still unresolved.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), especially its variation and wireframe workflows.
