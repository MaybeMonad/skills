# Report Format

Use these templates to keep long-running orchestration clear.

## Status Update

```markdown
Current state: <one sentence>

Done:
- <completed item with evidence>

In progress:
- <current item and why it matters>

Next:
- <next concrete action>

Risk/blocker:
- <None, or exact blocker>
```

## Frozen Spec Summary

```markdown
Goal:
<final outcome>

Success criteria:
- <observable result>

Implementation decisions:
- <locked interface, schema, file ownership, or behavior>

Quality gates:
- <command/browser/API check>

Assumptions:
- <assumption and fallback if wrong>
```

## Final Report

```markdown
Implemented:
- <high-signal change>

Verified:
- `<command>` passed.
- <browser/API/runtime check> passed.

Not verified:
- <None, or exact check that could not run and why>

Notes:
- <residual risk, migration note, or handoff>
```

Keep final reports concise. Include exact blockers and failed commands when something remains unresolved.
