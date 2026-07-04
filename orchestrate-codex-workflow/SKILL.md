---
name: orchestrate-codex-workflow
description: Robust Codex orchestration workflow for complex implementation, planning, debugging, or audit tasks that need v1 planning, adversarial loophole checks, frozen execution specs, task ledgers, optional executor delegation, browser or command-line quality gates, fix loops, and final evidence-backed reports. Use when the user asks Codex to be autonomous, plan then execute, coordinate other executors such as DeepSeek or Kimi, harden a strategy until confident, run deep quality checks, continue through context loss, or avoid quitting in the middle of a multi-step task.
---

# Orchestrate Codex Workflow

Use this skill to run Codex as the planner, integrator, auditor, and final quality gate for complex work. Keep the workflow light for small tasks, but never skip the evidence loop for work that changes code, schemas, production behavior, or user-visible flows.

## Workflow

1. **Intake**
   - Restate the goal, success criteria, hard constraints, likely risk areas, and out-of-scope work.
   - Inspect the repo, docs, logs, or runtime before asking questions that local evidence can answer.
   - If the request is a dry run, strategy exercise, or no-modification task, do not mutate files. State any missing repo/runtime context as an assumption.
   - Identify whether external executors are useful. Treat DeepSeek, Kimi, and other models as optional execution backends, not as authorities.

2. **V1 plan**
   - Produce the smallest execution-ready plan that could satisfy the goal.
   - Include affected surfaces, expected interfaces, validation commands, browser checks when relevant, and rollback or blocker conditions.
   - Use `scripts/new_task_ledger.py` when a durable checklist would reduce context-loss risk. If file writes are forbidden, pipe the ledger to stdout or include a compact ledger summary in the response.

3. **Loophole loop**
   - Ask whether the plan can fail because of missing contracts, stale assumptions, hidden routes, auth/session state, async behavior, schema drift, user data, deployment gaps, or verification blind spots.
   - Patch the plan until remaining risks are explicit and accepted.
   - Do not claim "100% confidence" unless the necessary evidence is available. Say what is verified, what is inferred, and what remains untested.

4. **Freeze the executable spec**
   - Lock the current plan, schema/API decisions, file ownership, task list, and quality gates before implementation.
   - Record assumptions that executors must not reinterpret.
   - Split work into small tasks with one owner and one clear completion signal.

5. **Delegate only bounded work**
   - Use external executors or subagents only for independent, clearly owned tasks.
   - Read `references/executor-contract.md` before writing executor prompts or reviewing executor output.
   - Require every executor to return changed files, verification evidence, blockers, and residual risk.

6. **Integrate and audit**
   - Review executor output before accepting it. Check ownership boundaries, missing edge cases, accidental rewrites, dead code, unused files, and consistency with the frozen spec.
   - Validate executor reports with `scripts/validate_executor_report.py` when reports are file-based or copied into a local artifact.
   - Prefer shared control points over one-off patches when the repo already has shared schemas, stores, render filters, or helpers.

7. **Verify, fix, repeat**
   - Run the planned command-line gates and browser/UI checks. Read `references/quality-gates.md` for gate selection.
   - If a gate fails, diagnose the real failure, patch the spec if needed, fix the implementation, and rerun the relevant gate.
   - Do not stop at the first green command if the user-visible path still needs browser or runtime evidence.

8. **Report**
   - Use `references/report-format.md` for status updates and final reports.
   - Lead with what changed, what passed, what could not be verified, and exact blockers.
   - Keep folder structure clean. Remove placeholder, dead, duplicated, or unused files created during the workflow.

## Resource Use

- `references/executor-contract.md`: read before delegating to external models, subagents, or human executors.
- `references/quality-gates.md`: read before selecting validation commands, browser checks, or acceptance criteria.
- `references/report-format.md`: read before reporting status, executor handoffs, or final outcomes.
- `scripts/new_task_ledger.py`: generate a Markdown task ledger from a frozen plan.
- `scripts/validate_executor_report.py`: check that an executor report contains the minimum evidence needed for integration review.

## Operating Rules

- Keep one source of truth for the current plan. If reality invalidates the plan, update the plan before continuing.
- Keep a visible task list for multi-step work and update it as each item changes state.
- Respect explicit no-modification constraints. In dry-run mode, produce the orchestration artifacts in the conversation instead of creating files.
- Measure twice before changing fragile code: inspect call paths, contracts, generated output, and existing tests first.
- Make the smallest safe change that satisfies the frozen spec.
- Never outsource final judgment. Codex must review, test, and accept or reject executor output.
- Prefer concrete evidence over confidence language. Replace vague claims with command output, screenshots, browser observations, API responses, or file references.
