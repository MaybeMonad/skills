# Agent Workflow Skills

[![skills.sh](https://skills.sh/b/MaybeMonad/skills)](https://skills.sh/MaybeMonad/skills)

Reusable agent skills for reducing unknowns in long-horizon coding work. The
core idea is to keep the agent's map, its prompt, plan, and context, aligned
with the territory: the real codebase, domain, runtime, data, constraints, and
review expectations.

## Install

List the skills in this repository:

```bash
npx skills add MaybeMonad/skills --list
```

Install the full set:

```bash
npx skills add MaybeMonad/skills --all
```

Install a specific skill:

```bash
npx skills add MaybeMonad/skills --skill map-territory-workflow
```

Use one skill without installing it:

```bash
npx skills use MaybeMonad/skills --skill map-territory-workflow
```

## Classification

Installable skill directories live under `skills/<category>/<skill>/`, matching
the category-first layout used by repos such as `mattpocock/skills`.
`catalog/skills.json` is the machine-readable map, and `suites/` keeps
human-facing notes for each category.

Folder map:

- `skills/unknown-reduction/`: map-vs-territory skills for reducing unknowns before, during, and after implementation.
- `skills/codex-orchestration/`: Codex planning, delegation, verification, and reporting.
- `skills/design-workflow/`: source-first design workflow, visual direction, variations, prototypes, and polish gates.
- `skills/web-reconstruction/`: source-first website cloning and web-effect reconstruction.
- `skills/search-growth/`: search-facing product surfaces, canonical URL policy, indexing inventory, and submission evidence.

## Skills

### Unknown Reduction Workflow

Suite metadata: `suites/unknown-reduction/`

| Skill | Purpose |
| --- | --- |
| `map-territory-workflow` | Choose the smallest unknown-reduction workflow across before, during, and after implementation. |
| `blindspot` | Run a pre-implementation blind spot pass to find unknown unknowns and cheap probes. |
| `brainstorm-prototype` | Explore multiple options or disposable prototypes before touching durable app code. |
| `interview-unknowns` | Ask high-leverage questions that can change architecture, data models, APIs, UX, or scope. |
| `reference-alignment` | Extract requirements from source code, screenshots, docs, libraries, or prior examples. |
| `implementation-plan-review` | Write implementation plans that foreground decisions likely to change. |
| `implementation-notes` | Log decisions, deviations, edge cases, and evidence during implementation. |
| `pitch-explainer` | Package work into a reviewer-ready explainer for buy-in and approval. |
| `change-quiz` | Explain a completed change and quiz the user before merge, release, or handoff. |

### Codex Orchestration

Suite metadata: `suites/codex-orchestration/`

| Skill | Purpose |
| --- | --- |
| `orchestrate-codex-workflow` | Plan, delegate, verify, and report complex Codex implementation workflows. |

### Design Workflow

Suite metadata: `suites/design-workflow/`

Credit: inspired by
[Trystan-SA/claude-design-system-prompt](https://github.com/Trystan-SA/claude-design-system-prompt)
(MIT), adapted into this repository's source-first skills format.

| Skill | Purpose |
| --- | --- |
| `design-workflow` | Choose the smallest useful design path across source maps, direction, variations, prototypes, and polish. |
| `design-source-map` | Extract tokens, components, layout grammar, states, and constraints from real design sources. |
| `design-direction` | Commit to a concrete greenfield visual system before hi-fi work. |
| `design-variations` | Produce meaningful options for layout, hierarchy, visual treatment, flow, or interaction choices. |
| `design-prototype` | Build and verify clickable, stateful prototypes with real feedback and interaction states. |
| `design-polish` | Run a final design quality gate and fix accessibility, hierarchy, state, responsiveness, and trope issues. |

### Web Reconstruction

Suite metadata: `suites/web-reconstruction/`

| Skill | Purpose |
| --- | --- |
| `web-clone` | Clone, study, and remix websites from real source/runtime evidence, including static mirrors and WebGL/Canvas effect reconstruction. |

### Search Growth

Suite metadata: `suites/search-growth/`

| Skill | Purpose |
| --- | --- |
| `technical-seo` | Run a canonical technical SEO workflow across metadata, routes, redirects, sitemap, robots, structured data, crawlability, and indexing evidence. |

## Publishing Notes

skills.sh does not require a separate publish command. It discovers GitHub
repositories through the `skills` CLI flow and ranks skills from anonymous
installation telemetry.

This repo also has an automated GitHub release publisher in
`.github/workflows/publish-skills.yml`. Pull requests run discovery and
`gh skill publish --dry-run`; pushes to `main` validate the same way and then
publish non-interactively with `gh skill publish --tag v0.0.<run_number>`.
Manual workflow runs can override the tag.

The workflow uses `GITHUB_TOKEN` by default. If GitHub blocks release or
repository-topic writes for the default token, add a `SKILLS_PUBLISH_TOKEN`
secret with the repository permissions needed by `gh skill publish`.

Useful checks before sharing:

```bash
npx skills add MaybeMonad/skills --list
npx skills use MaybeMonad/skills --skill map-territory-workflow
npx skills use MaybeMonad/skills --skill web-clone
npx skills use MaybeMonad/skills --skill technical-seo
npx skills use MaybeMonad/skills --skill design-workflow
```

Do not put installable `SKILL.md` files under `suites/`; default discovery finds
`skills/<category>/<skill>/SKILL.md` and treats `suites/` as metadata only.

Search indexing on skills.sh may lag behind a successful install. If a valid
public repo still does not appear after the normal indexing delay, open a
listing/indexing issue in `vercel-labs/skills` with the repository URL and an
install command.
