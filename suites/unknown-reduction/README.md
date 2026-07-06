# Unknown Reduction Workflow Suite

This folder is the logical package for the nine map-vs-territory skills that
reduce unknowns before, during, and after implementation. The installable skill
directories live under `skills/unknown-reduction/`; this suite folder is
metadata and navigation only.

## Entrypoints

- `skills/unknown-reduction/map-territory-workflow/`: suite-level router across the whole process.
- `skills/unknown-reduction/blindspot/`: pre-implementation unknown-unknown pass.

## Supporting Skills

- `skills/unknown-reduction/brainstorm-prototype/`
- `skills/unknown-reduction/interview-unknowns/`
- `skills/unknown-reduction/reference-alignment/`
- `skills/unknown-reduction/implementation-plan-review/`
- `skills/unknown-reduction/implementation-notes/`
- `skills/unknown-reduction/pitch-explainer/`
- `skills/unknown-reduction/change-quiz/`

## Publishing Contract

Do not add installable `SKILL.md` files under this folder. Keep the actual skill
directories under `skills/unknown-reduction/` and keep category membership in
`catalog/skills.json`.
