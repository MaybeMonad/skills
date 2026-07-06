---
name: design-workflow
description: Design workflow router for UI, page, app screen, prototype, deck, design-system, visual-direction, variation, or polish work. Use when the user asks for design help and the next step may be source-map extraction, aesthetic direction, options, prototyping, or final quality review.
---

# Design Workflow

Use this skill as the suite entrypoint for design work. The job is to keep the
artifact grounded in the real source system, the user's taste, and the medium
being designed for.

## Phase Map

Source-first setup:
- `design-source-map`: extract tokens, components, layout grammar, density,
  interaction patterns, assets, and gaps from an existing product, codebase,
  brand guide, screenshot set, Figma file, or reference site.

Direction setting:
- `design-direction`: commit to a concrete visual system when no existing
  design system applies, or when the user asks for a new look.

Exploration:
- `design-variations`: produce meaningfully different options when the user
  wants alternatives, wireframes, visual directions, or comparison before
  durable implementation.

Interactive build:
- `design-prototype`: build a clickable prototype or usable front-end slice
  with real state, transitions, validation, and feedback.

Review and repair:
- `design-polish`: run the final quality gate across source fidelity,
  accessibility, generic-AI tropes, hierarchy, rhythm, interaction states,
  responsiveness, and content fit.

## Selection Rules

- If a real system, brand, screenshot, Figma file, or existing codebase exists,
  start with `design-source-map` before inventing visuals.
- If no system exists, use `design-direction` before drawing hi-fi screens.
- If the user can judge taste only after seeing options, use
  `design-variations` before changing durable app code.
- If the user asks for a prototype, demo, mockup, clickable flow, or usable
  app-like artifact, use `design-prototype`.
- If a design is already built or about to be shown, shipped, screenshotted, or
  handed off, use `design-polish`.
- Do not run every skill by default. Choose the smallest chain that resolves
  the highest-cost unknown.

## Operating Rules

- Inspect available sources before asking questions that files, screenshots,
  docs, runtime, or current code can answer.
- Separate source facts, design judgments, assumptions, and uninspected areas.
- Preserve exact user-supplied product, legal, pricing, SEO, and marketing copy
  unless the user asks for rewriting.
- Match the medium. Apps, dashboards, decks, landing pages, games, documents,
  and prototypes need different density, hierarchy, and interaction standards.
- Verify visual and interactive work in the runtime when possible. A passing
  build is not a design acceptance test.

## Default Output

When asked to choose the design path, return:

1. Recommended path: the smallest skill chain.
2. Source context: inspected references and missing references.
3. Design constraints: tokens, components, audience, medium, and non-goals.
4. Immediate artifact: source map, direction, variation set, prototype, or
   polish report.
5. Blocking questions: only questions whose answers change the next step.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT). This version is adapted for the MaybeMonad skills repository and uses
this repo's source-first workflow style.
