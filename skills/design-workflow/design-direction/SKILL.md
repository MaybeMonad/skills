---
name: design-direction
description: Aesthetic direction workflow for greenfield UI, brandless screens, new visual systems, redesign concepts, or designs that need a concrete typography, color, density, component, imagery, and motion thesis before hi-fi work.
---

# Design Direction

Use this skill when there is no design system to inherit from, or when the user
explicitly wants a new look. Direction turns vague taste into a concrete visual
contract before hi-fi work spreads across many screens.

## Workflow

1. Confirm the blank slate:
   - Check for brand guides, tokens, codebase components, screenshots, Figma
     files, existing product UI, and reference products.
   - Completion criterion: either an existing source is ruled out, or the work
     switches to `design-source-map`.
2. Name the intent:
   - Audience, product category, emotional tone, trust level, content density,
     novelty appetite, and explicit off-limits tropes.
   - If the user is unsure, propose 2-3 distinct directions and ask them to
     pick or combine.
   - Completion criterion: the direction can be summarized as a specific
     thesis, not "modern and clean."
3. Commit the visual contract:
   - Typography: families, weights, scale, line heights, and fallback plan.
   - Color: primary, accent if needed, neutrals, semantic colors, surfaces, and
     contrast expectations.
   - Density: spacing scale, layout rhythm, container widths, and information
     density.
   - Shape and elevation: radii, borders, shadows, dividers, and focus rings.
   - Components: button, input, card, nav, tab, menu, modal, table, and empty
     state direction where relevant.
   - Imagery and icons: real assets, icon library, placeholders, or asset gaps.
   - Motion: timing, easing, state transitions, entry/exit motion, and reduced
     motion behavior.
   - Completion criterion: every axis has a concrete default or an explicit
     open decision.
4. Prove it small:
   - Build or specify one representative surface: hero, toolbar, card set,
     form, dashboard slice, mobile screen, or slide.
   - Completion criterion: the proof surface exercises type, color, spacing,
     component style, and at least one interaction state.
5. Verify the direction:
   - Check contrast, text fit, responsive constraints, palette balance,
     hierarchy, and whether the surface reads as the intended thesis.
   - Completion criterion: unresolved design judgments are named before the
     direction is reused.

## Output Shape

- Direction thesis: audience, tone, and design promise.
- Token contract: type, color, spacing, shape, elevation, motion.
- Component contract: core UI defaults and state expectations.
- Proof surface: file, screenshot, or described slice.
- Open decisions: what the user should sign off before scaling the direction.

## Rules

- Do not use a single-hue palette as the whole design unless the brand demands
  it; introduce restrained neutral and semantic structure.
- Do not default to decorative gradients, emoji, weak custom SVG scenes, or
  generic SaaS card patterns as the visual idea.
- Do not make a landing page when the user asked for an app, dashboard, tool,
  or game. Build the primary experience first.
- Add new values to the direction before using them in an artifact; avoid
  one-off inline styling.
- When the direction is for production code, map it to the project's token
  format instead of leaving it as prose.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), adapted into a smaller direction-setting workflow.
