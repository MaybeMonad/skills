---
name: design-prototype
description: Interactive design prototype workflow for clickable flows, mockups, demos, app screens, stateful UI, form validation, loading/error/success feedback, keyboard behavior, and design handoff prototypes.
---

# Design Prototype

Use this skill when the artifact needs to behave, not just look right. A
prototype tests flow, state, feedback, and interaction quality before or during
implementation.

## Workflow

1. Map the flow:
   - Entry point, screens, states, transitions, success path, failure path,
     backtracking, empty state, and exit state.
   - Completion criterion: every primary action has a destination or visible
     result.
2. Set fidelity and frame:
   - Mid-fi for flow validation, hi-fi for visual validation, production slice
     for codebase implementation.
   - Pick the target frame: desktop app, web page, dashboard, mobile screen,
     tablet, deck interaction, or embedded widget.
   - Completion criterion: fidelity matches the decision being tested.
3. Ground the prototype:
   - Use `design-source-map` outputs, existing components, real tokens, and
     real-looking sample data.
   - If no system exists, use `design-direction` first.
   - Completion criterion: the prototype does not rely on generic placeholder
     visuals or lorem ipsum when real content is needed.
4. Build statefully:
   - Navigation, form values, validation errors, dirty/pristine states,
     selections, filters, modal/popover open state, disabled states, loading,
     success, and failure feedback.
   - Fake network behavior with controlled local state when backend work is out
     of scope.
   - Completion criterion: important interactions are wired, not implied by
     static screens.
5. Make interactions accessible:
   - Semantic controls, visible focus, keyboard navigation, Escape behavior for
     dismissible layers, labels, hit targets, reduced motion, and status
     announcements where relevant.
   - Completion criterion: keyboard use reaches the same flow as pointer use.
6. Verify in runtime:
   - Run the local preview or app, exercise the flow, inspect console errors,
     check desktop and mobile sizes when relevant, and capture screenshots if
     visual fit matters.
   - Completion criterion: every claimed behavior was tried or is explicitly
     marked unverified.

## Output Shape

- Prototype scope: real behavior, fake behavior, and out-of-scope behavior.
- Flow map: screens, states, and transitions.
- How to view: file path, route, or local URL.
- Verification: commands, browser paths, and remaining caveats.
- Decisions for user: visual or interaction calls needing signoff.

## Rules

- A prototype with dead primary controls is not complete.
- Do not create separate v1/v2/v3 files for small variants; use one artifact
  with tabs, toggles, a canvas, or a tweak panel when comparison matters.
- Do not wire real payments, emails, production mutations, auth changes, or
  migrations unless explicitly requested.
- If the prototype sits inside a real app, follow existing component and route
  patterns instead of creating an isolated aesthetic island.

## Credit

Inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), adapted around runtime-verifiable Codex prototypes.
