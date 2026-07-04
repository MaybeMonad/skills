---
name: pitch-explainer
description: Post-implementation pitch and explainer workflow for packaging a prototype, spec, implementation notes, verification evidence, and resolved unknowns into a reviewer-ready document. Use when the user asks for a Slack-ready summary, buy-in doc, explainer, launch note, approval packet, or wants reviewers to see the context, demo, decisions, tradeoffs, and remaining risks.
---

# Pitch Explainer

Use this skill to accelerate reviewer understanding and approval. The output
should answer the unknowns reviewers are likely to have before they need to ask.

## Workflow

1. Gather source material:
   - Prototype, spec, plan, implementation notes, diff summary, screenshots,
     demo GIF/video, commands run, tests, runtime checks, and unresolved risks.
2. Identify the audience:
   - Product, design, engineering, security, data, leadership, or a mixed
     review group.
3. Lead with the demo or visible outcome when one exists.
4. Explain the problem and why the chosen approach is appropriate.
5. Include alternatives rejected and why.
6. Show which unknowns were resolved and which remain.
7. Include verification evidence and reviewer asks.

## Output Shape

Use this structure:

1. Demo or outcome.
2. Problem.
3. What changed.
4. Decisions and tradeoffs.
5. Unknowns resolved.
6. Verification evidence.
7. Remaining risk.
8. Reviewer asks.

## Rules

- Write for approval, not for archival completeness.
- Lead with the most concrete artifact: demo, screenshot, prototype, or user
  flow.
- Do not hide residual risk. State it with its mitigation or follow-up.
- Do not paste long diffs. Explain behavior and link or reference files.
- Keep stakeholder text crisp enough to drop into Slack or a review doc.
