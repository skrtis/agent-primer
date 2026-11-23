---
title: "11. Self-improvement and RSI"
nav_order: 12
---

# 11. Self-improvement and RSI

## Agents that improve agents

Once an agent can write and test code, people naturally ask whether it can improve itself or its own harness. Over time, the target being optimized has widened: prompt wording → context contents → whole workflows → the harness code itself ([Weng](https://lilianweng.github.io/posts/2026-07-04-harness/)). Early research systems already do this without changing model weights:

- **ACE** treats context as a playbook of strategies that the agent grows and refines from experience ([Zhang et al.](https://arxiv.org/abs/2510.04618)).
- **Darwin Gödel Machine** rewrote its own agent code to raise coding benchmark scores with the underlying model unchanged ([Weng](https://lilianweng.github.io/posts/2026-07-04-harness/)).

These gains show up mainly where success can be checked automatically (such as code with unit tests). Adding a self-improvement loop does not always help; with weaker models it can make results worse.

## Three levels of improvement

Public discussion often mixes together three very different ideas ([Schmid](https://www.philschmid.de/recursive-self-improvement)):

| Level | What changes | Test bar | Where we are today |
|---|---|---|---|
| **Iteration** | Output is revised until tests pass | Fixed | Routine |
| **Self-improvement** | System keeps a lasting change (new skill, updated memory, edited harness) | Fixed | Where most current demos live |
| **Recursive self-improvement** | Improves both task performance *and* its own ability to make further improvements | Getting harder | Unproven |

## What AI labs mean by RSI

In frontier lab safety frameworks, **recursive self-improvement (RSI)** has a narrower meaning than in public discussion.

> **Recursive self-improvement (RSI):** AI fully autonomously designing and building its own successor ([Anthropic](https://www.anthropic.com/institute/recursive-self-improvement)).

Anthropic's view is that this has not happened and is not inevitable; AI already writes most code at Anthropic and speeds up research, but humans still choose goals and supply research judgment.

An [independent assessment by METR](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment) estimated that capability progress on well-defined tasks at Anthropic was running at roughly **2×** its earlier pace, mostly due to AI. METR noted clear limits to that estimate: key internal evidence was withheld, it could not test unreleased models, and speedups may concentrate on tasks that can be graded automatically.

## Reasons for caution

- **Capped by human-written tests:** current gains optimize against fixed tests that humans wrote, with little evidence that self-modifying systems get better at finding their *next* improvement ([Schmid](https://www.philschmid.de/recursive-self-improvement)).
- **Reward hacking:** systems told to raise a score often find shortcuts instead of solving the task (for example, editing the unit tests instead of fixing the code).
- **Saved lessons often fail to transfer:** memory written for future use frequently does not help on new tasks.

In short, automated self-improvement only works as well as the grading behind it ([page 10](10-evals.md)).

## Sources

- Lilian Weng, [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Jul 2026)
- Zhang et al., [ACE: Agentic Context Engineering](https://arxiv.org/abs/2510.04618) (ICLR 2026)
- Philipp Schmid, [Recursive Self-Improvement](https://www.philschmid.de/recursive-self-improvement) (Aug 2026)
- Anthropic, [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) (Sep 2026)
- METR, [Independent Assessment of AI R&D Acceleration at Anthropic](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment) (Nov 2026)

Next: [12. Core principles](12-what-the-sources-agree-on.md)
