---
title: "12. Core principles"
nav_order: 13
---

# 12. Core principles

Across engineering blogs and research papers, people use different terminology, but eight core principles come up again and again:

1. **The model only produces text; the harness does everything else.** Running tools, checking permissions, isolating code in sandboxes, building the context, and saving records all live in ordinary software. That is why the same model behaves differently in different harnesses and why benchmark scores belong to the model and harness together.
2. **Context is the scarce resource.** Models see only their current input, windows have limits, and irrelevant text actively lowers accuracy. Consolidated tools, on-demand skills, writing code instead of serial tool calls, compaction, subagents, and just-in-time retrieval are all ways of keeping the context small and clean.
3. **Anything that needs to last belongs outside the model.** Models forget everything between calls and sessions end. Progress, plans, and knowledge should live in files, logs, and version control, loaded back into context only when needed.
4. **Start simple and make every layer earn its place.** Prefer a single call or fixed workflow over an open-ended agent loop, plain hand-written loops over heavy frameworks, plain files plus text search over specialized memory stacks, and one writer over parallel multi-agent editing unless measurements show a real win.
5. **Separate doing from checking.** Models judge their own work too kindly. Pair upfront rules (guides) with independent checks (sensors: exact code tests and linters first, separate clean-context reviewers or calibrated model judges second). Reliable checking is also the main limit on self-improvement.
6. **Tool design matters as much as prompting.** Tool names, descriptions, input formats, return values, and error messages are all read by the model and steer its choices just as strongly as the system prompt.
7. **Harness tricks are workarounds for current model limits, and they go stale.** Every guardrail assumes something today's model cannot do reliably on its own. Re-test assumptions whenever the model upgrades and delete scaffolding that no longer helps.
8. **Measure and read real runs.** Small edits cause surprising drops, and claimed harness gains often sit inside normal run-to-run noise. Read raw failure logs before designing tests, run repeated trials, and report cost alongside accuracy.

## Where the literature still differs

Most disagreements are about scope or task mix rather than the basic picture:

- **What "harness" covers:** everything outside the model vs. just the loop itself.
- **What "memory" covers:** saved cross-session experience only vs. weights, context, and external files together.
- **When multi-agent pays off:** big gains on parallel read-heavy tasks vs. drops on closely connected step-by-step tasks.
- **Position in context:** how strongly "lost in the middle" shows up depends on the model and task.

Next: [13. Glossary](13-glossary.md)
