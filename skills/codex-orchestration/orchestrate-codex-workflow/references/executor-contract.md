# Executor Contract

Use this reference when delegating work to an external model, subagent, or human executor. The executor may implement, inspect, or test, but Codex remains responsible for integration and final acceptance.

## Delegation Rules

- Assign a bounded task with a clear owner, file/module scope, acceptance criteria, and verification command.
- State that other workers may be editing nearby files and the executor must not revert unrelated changes.
- Forbid destructive git commands, broad formatting, dependency upgrades, generated churn, and edits outside the assigned scope unless explicitly approved.
- Require the executor to stop and report a blocker when the task needs secrets, production access, ambiguous product decisions, or a wider refactor.
- Require direct evidence. "Looks good" is not an acceptable verification result.

## Prompt Template

```text
You are an executor for this task. You are not alone in the codebase; do not revert unrelated changes and do not edit outside your assigned ownership.

Goal:
<one concrete outcome>

Frozen spec:
<interfaces, behavior, constraints, and non-goals>

Ownership:
<files, directories, modules, or read-only investigation scope>

Forbidden:
- No destructive git commands.
- No unrelated refactors or formatting.
- No dependency changes unless explicitly required by the frozen spec.
- No edits outside ownership without reporting a blocker first.

Acceptance criteria:
- <observable behavior>
- <tests/builds/browser checks>
- <edge cases>

Return exactly this report:
## Summary
## Changed Files
## Verification
## Blockers
## Residual Risk
```

## Required Report Shape

```markdown
## Summary
- What was done in 2-5 bullets.

## Changed Files
- `path/to/file`: why it changed.
- `None`: use only for read-only tasks.

## Verification
- `command`: pass/fail/not run, with the key output or reason.
- Browser/API/manual check: pass/fail/not run, with the observed result.

## Blockers
- `None`, or a concrete blocker with the next required action.

## Residual Risk
- `None`, or the specific behavior that remains unproven.
```

## Review Checklist

- Confirm every changed file is inside the assigned ownership.
- Confirm the report names actual commands or checks, not generic confidence.
- Confirm blockers and residual risks are credible.
- Inspect the diff before integrating. Executor reports are inputs, not proof.
