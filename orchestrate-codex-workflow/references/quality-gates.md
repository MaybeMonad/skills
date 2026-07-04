# Quality Gates

Use these gates to choose verification for the frozen spec. Select the smallest gate set that proves the requested behavior, then rerun affected gates after every fix.

## Baseline Gates

- Repo state: inspect `git status --short` before and after work.
- Static checks: run the repo's targeted lint/typecheck commands for touched files or packages.
- Tests: run the narrowest meaningful test first, then broader tests when shared behavior changed.
- Build: run package or app builds when imports, route boundaries, bundling, or generated assets changed.
- Runtime smoke: call API routes, start dev servers, or run CLI commands that prove the changed path works.

## Browser And UI Gates

- Use browser checks when behavior is visual, interactive, layout-sensitive, auth/session-dependent, or route-driven.
- Verify the actual route and mode named by the user.
- Capture concrete observations: visible text, state changes, network/API results, console errors, screenshots when useful.
- If auth blocks browser verification, say that clearly and use API or code-level evidence only when it genuinely proves the path.

## Executor Output Gates

- Validate the executor report shape before relying on it.
- Review diffs for out-of-scope edits, dead code, unused files, hidden TODOs, and mismatched contracts.
- Re-run verification locally when the executor changed code or when their environment may differ.

## Stop Conditions

- Stop and report a blocker when required secrets, production credentials, paid services, or user decisions are unavailable.
- Stop when the frozen spec is contradicted by repo evidence and the decision changes product behavior.
- Do not stop merely because one attempt failed. Diagnose, adjust, and retry within the agreed scope.
