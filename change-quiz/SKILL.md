---
name: change-quiz
description: Post-implementation learning and quiz workflow for making the user understand a code change before merge, release, review, or handoff. Use when the user asks for a quiz, wants to understand what changed, says merge only when I pass, or needs a report with context, intuition, behavior, risks, and verification followed by comprehension questions.
---

# Change Quiz

Use this skill when the user wants to understand a completed change deeply
enough to review, merge, or hand it off. The quiz should test behavior and
risk, not trivia.

## Workflow

1. Inspect the actual change:
   - Diff, touched files, tests, runtime checks, implementation notes, and
     relevant existing code paths.
2. Explain the change:
   - Problem, previous behavior, new behavior, important files, data flow,
     edge cases, validation, and residual risk.
3. Build intuition:
   - Explain why the implementation works in the local architecture.
   - Call out non-obvious dependencies and failure modes.
4. Create the quiz:
   - Ask 5-10 questions depending on change size.
   - Prioritize behavior, tradeoffs, risk, and validation.
   - Include scenario questions, not just recall questions.
5. Hold the answer key unless the user asks for a self-study version.
6. Grade the user's answers against the behavior that actually shipped.

## Report Shape

1. Context.
2. What changed.
3. How it works.
4. Files and code paths.
5. Verification.
6. Residual risks.
7. Quiz.

## Rules

- Do not quiz on filenames unless the path matters to understanding behavior.
- Do not claim the user passed unless their answer covers the real risks.
- If verification is incomplete, include that in both the report and quiz.
- If the user fails, explain the gap and ask a follow-up question on that gap.
