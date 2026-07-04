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

## Skills

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
| `orchestrate-codex-workflow` | Plan, delegate, verify, and report complex Codex implementation workflows. |

## Publishing Notes

skills.sh does not require a separate publish command. It discovers GitHub
repositories through the `skills` CLI flow and ranks skills from anonymous
installation telemetry.

Useful checks before sharing:

```bash
npx skills add MaybeMonad/skills --list
npx skills use MaybeMonad/skills --skill map-territory-workflow
```

Search indexing on skills.sh may lag behind a successful install. If a valid
public repo still does not appear after the normal indexing delay, open a
listing/indexing issue in `vercel-labs/skills` with the repository URL and an
install command.
