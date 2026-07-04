---
name: reference-alignment
description: Reference-driven requirement extraction for behavior, design, architecture, workflows, or domain semantics that are hard to describe from scratch. Use when the user points to source code, a folder, docs, screenshots, diagrams, websites, examples, prior implementations, libraries, or says they cannot describe what they want but can provide a reference.
---

# Reference Alignment

Use this skill when the best specification is an example. The goal is to turn
references into precise requirements without forcing the user to invent
language for something they can recognize.

## Workflow

1. Catalog references:
   - Source code, library, existing component, screenshot, website, video,
     diagram, doc, issue, previous implementation, or product behavior.
2. Inspect the richest available layer:
   - Prefer source code and docs over screenshots alone.
   - For UI, inspect structure, state, interaction, spacing, density, copy, and
     responsive behavior where possible.
   - For behavior, inspect tests, edge cases, data flow, and error handling.
3. Extract requirements:
   - Must match.
   - Should adapt.
   - Must avoid.
   - Open unknowns.
4. Map the reference onto the target system:
   - Existing components, tokens, APIs, data models, permissions, runtime
     constraints, and validation gates.
5. Produce a reference brief the implementation can follow.

## Output Shape

Use this brief:

- References inspected: paths, URLs, screenshots, or docs.
- Core intent: what the reference is teaching.
- Must match: semantics or qualities that matter.
- Can adapt: details that may differ in this project.
- Avoid: properties that are not desired.
- Target mapping: local files, components, data, or constraints.
- Open questions: only what changes the implementation.

## Rules

- Do not copy blindly. Preserve the intent and required semantics, then adapt
  to the target codebase.
- When a screenshot is the only reference, state that structure and behavior are
  inferred unless verified elsewhere.
- If the reference conflicts with project conventions, surface the tradeoff
  before implementation.
- Preserve exact user-provided copy when the reference is the source of truth.
