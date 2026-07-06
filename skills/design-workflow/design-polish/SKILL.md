---
name: design-polish
description: Design polish quality gate for completed or near-completed UI, prototypes, pages, decks, screenshots, dashboards, or app screens. Use before handoff, shipping, stakeholder review, app-store capture, or when checking accessibility, hierarchy, interaction states, responsiveness, and AI-template tropes.
---

# Design Polish

Use this skill as the final design quality gate. Polish is not a vague pass for
"make it nicer"; it is a structured review, fix, and re-verification loop.

## Workflow

1. Confirm scope:
   - File, route, screenshot, prototype, deck, app screen, component, or flow.
   - Read referenced styles, tokens, components, and copy sources.
   - Completion criterion: the reviewed surface and its source dependencies are
     named.
2. Render before judging:
   - Open the real file, route, preview, or app when possible.
   - Check at relevant viewport sizes and states.
   - Completion criterion: layout-sensitive claims come from rendered evidence,
     not static code reading alone.
3. Run review passes:
   - Source fidelity: tokens, components, brand rules, copy exactness, and
     medium fit.
   - Accessibility: contrast, semantic controls, labels, headings, focus,
     keyboard path, hit targets, reduced motion, and color-only signaling.
   - Generic-AI trope scan: decorative gradients, emoji filler, weak custom SVG
     illustration, generic card styling, arbitrary colors, off-scale spacing,
     and ungrounded font choices.
   - Hierarchy and rhythm: primary/secondary/tertiary clarity, type scale,
     spacing scale, alignment, density, section rhythm, and scan path.
   - Interaction states: default, hover, active, disabled, focus-visible,
     loading, success, error, selected, and empty states.
   - Responsiveness and text fit: mobile/desktop constraints, overflow,
     clipping, wrapping, tap target size, and content overlap.
   - Completion criterion: every relevant pass has findings or an explicit
     clean result.
4. Prioritize:
   - Blockers: accessibility failures, broken layout, dead controls, unreadable
     text, content overlap, misleading copy, or missing required states.
   - Quality issues: weak hierarchy, generic tropes, arbitrary tokens, missing
     feedback, inconsistent component treatment.
   - Polish recommendations: taste refinements that are safe but not required.
   - Completion criterion: fixes are ordered by user impact, not ease.
5. Fix and re-verify:
   - Fix blockers and quality issues directly when in scope.
   - Apply polish recommendations only when they preserve the user's direction.
   - Re-render high-risk surfaces after edits.
   - Completion criterion: no fixed issue is reported without a re-check or a
     named reason verification was blocked.

## Output Shape

- Verdict: ready, ready after named decisions, or needs another design round.
- Changed files or reviewed files.
- Blockers fixed.
- Quality fixes applied.
- Open decisions for the user.
- Verification performed and remaining caveats.

## Rules

- Lead with findings before taste commentary when reviewing someone else's
  design.
- Do not add new sections, claims, stats, or decorative content to fill space
  without user approval.
- Keep exact user-supplied copy unless the task is copy polish.
- Treat screenshots as insufficient for interaction-state claims unless the
  runtime was also checked.
- If the surface is still structurally unresolved, say polish is premature and
  name the design decision that must settle first.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), adapted into a single Codex-friendly quality gate.
