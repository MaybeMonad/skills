---
name: interview-unknowns
description: Clarifying interview workflow for resolving ambiguities that can change architecture, data models, APIs, UX flows, acceptance criteria, or implementation scope. Use when the user asks to be interviewed, says ask me questions, says there are still unknowns, or when a small number of user answers would materially change the plan.
---

# Interview Unknowns

Use this skill to ask only the questions that matter. The goal is not to gather
all possible preferences; it is to resolve ambiguities that could change the
work.

## Workflow

1. Inspect first when the answer may exist in the repo, docs, screenshots,
   prior decisions, or runtime behavior.
2. List the decisions that are still ambiguous.
3. Rank questions by impact:
   - Architecture or data shape.
   - User-facing behavior.
   - Scope boundary.
   - Validation and acceptance.
   - Taste or copy preference.
4. Ask one question at a time when the answer blocks the next step.
5. Ask up to 3 grouped questions when the answers are helpful but not blocking.
6. After each answer, update the working assumptions and state whether enough
   is known to proceed.

## Question Quality

Good questions:
- Change the implementation path depending on the answer.
- Offer concrete choices when choices are known.
- Explain why the answer matters.
- Avoid asking the user to restate information already available in files.

Poor questions:
- Ask for generic preference without consequence.
- Offload repo inspection to the user.
- Ask many low-impact questions before the high-impact one.
- Hide a recommendation when one option is clearly safer.

## Output Shape

When starting an interview, return:

1. What I can infer already.
2. The next highest-impact question.
3. Why the answer changes the work.
4. What I will assume if we need to proceed without an answer.

## Stop Rule

Stop interviewing when the remaining ambiguity is cheaper to resolve by a
prototype, reference read, implementation note, or normal validation.
