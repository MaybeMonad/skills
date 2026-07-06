---
name: design-source-map
description: Source-map extraction for design systems, brands, UI kits, screenshots, Figma files, existing codebases, reference sites, tokens, components, layout grammar, and visual vocabulary. Use before matching or extending an existing design.
---

# Design Source Map

Use this skill when the design should inherit from something real. The source
map is the compact design brief that turns references into constraints the
implementation can follow.

## Workflow

1. Catalog sources:
   - Codebase theme files, CSS variables, Tailwind config, component library,
     stories, screenshots, Figma files, brand guides, live pages, decks, or
     reference products.
   - Completion criterion: every available source is listed or explicitly
     marked unavailable.
2. Inspect the richest layer first:
   - Prefer source code and design-system docs over screenshots.
   - For screenshots or live pages, inspect structure, spacing, density,
     responsive behavior, state, and content hierarchy.
   - Completion criterion: each major design claim points to a source path,
     URL, screenshot, or observed runtime surface.
3. Extract the system:
   - Color roles, typography, spacing, radii, elevation, border treatment,
     iconography, imagery, motion, breakpoints, container widths, and z-index
     patterns.
   - Reusable components, variants, empty/error/loading states, and layout
     templates.
   - Voice and copy rhythm when the design depends on writing tone.
   - Completion criterion: tokens and components are concrete values, not
     invented labels.
4. Mark the fault lines:
   - Gaps: missing tokens, unowned components, absent states, undocumented
     motion, unknown assets, inaccessible color pairs.
   - Inconsistencies: near-duplicate colors, off-scale spacing, mismatched
     radii, one-off typography, competing component patterns.
   - Completion criterion: gaps are not silently filled and inconsistencies are
     not silently merged.
5. Map onto the target:
   - Name the local files, components, token names, asset paths, libraries, and
     runtime constraints the next design step must use.
   - Completion criterion: the next artifact can be built without re-reading
     the full source set.

## Output Shape

- Sources inspected: files, URLs, screenshots, Figma nodes, or docs.
- Core vocabulary: the visual grammar to preserve.
- Token map: concrete values and source names.
- Component map: reusable pieces, variants, and states.
- Must match: invariants that define the system.
- Can adapt: details that may change without breaking the system.
- Gaps and inconsistencies: unresolved design-system work.
- Target mapping: local files and implementation constraints.

## Rules

- Do not invent tokens for missing categories. Mark them as decisions.
- Keep source names when they exist; do not rename a system casually.
- Treat screenshots as inference unless backed by code or design docs.
- Preserve exact user-provided copy when the reference is the source of truth.
- If a reference conflicts with local conventions, surface the tradeoff before
  implementation.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), especially its design-system and component extraction concerns.
