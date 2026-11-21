---
title: "11. Self-improvement and RSI"
nav_order: 12
---

# 11. Self-improvement and RSI

## Agents that improve agents

Once an agent can write and test code, an obvious question is whether it can improve itself, or improve the harness it runs in. Lilian Weng's "Harness Engineering for Self-Improvement" describes how the thing being optimized has moved over time, from the wording of prompts, to the contents of the context, to whole workflows, and now to the harness code itself. Several research systems already do this. ACE treats an agent's context as a playbook of strategies that the agent grows and refines from experience. The Darwin Gödel Machine rewrote its own agent code and improved its score on a coding benchmark without any change to the underlying model. Weng's main observation is that these gains appear mostly where success can be checked automatically, such as code with tests, and that adding a self-improvement loop does not guarantee improvement; with weaker models it can make things worse.

## Three kinds of improvement

Philipp Schmid's post "Recursive Self-Improvement" offers a helpful way to separate claims that are often run together. The simplest kind is iteration, in which an agent revises its output until it passes a test. The next is self-improvement, in which the system itself changes in a lasting way, for example by saving a new skill, updating its memory or editing its own harness, and then does better on a fixed test. The strongest kind is recursive self-improvement. Here the system improves not only its performance but also its ability to make further improvements, and the standard it is judged by gets harder as well. Most of what is called self-improvement today belongs to the second kind.

## RSI as the labs define it

In the safety frameworks of the large AI labs, recursive self-improvement (RSI) has a more specific meaning. Anthropic's "When AI builds itself" defines it as AI fully autonomously designing and developing its own successor. Anthropic's position in that piece is that this has not happened and is not inevitable. AI already writes most of the code at Anthropic and considerably speeds up AI research, but humans still set the goals, and the main gap is the judgment needed to choose which research directions to pursue.

An independent assessment by METR, published in November 2026, estimated that capability progress on well-defined tasks at Anthropic was running at roughly twice its earlier rate, and judged that most of this acceleration was due to AI. METR was careful to list the limits of that conclusion. Much of the most informative evidence was withheld from it, it did not have access to unreleased models, and the gains may apply mainly to tasks that can be graded automatically.

## The skeptical view

Schmid and others give reasons for caution. Current gains are bounded, because they are measured against tests that humans wrote and still control, and there is little evidence that a system which improves itself also gets better at finding its next improvement. Systems told to raise a score often find ways to raise the score without doing the intended work, a problem called reward hacking; editing the tests instead of fixing the code is a common example. And memory saved for future use often turns out not to help later. The common thread is that self-improvement works only as well as the evaluation behind it, which connects this page back to page 10.

## Key vocabulary

- **Iteration**: an agent revising its output until it passes a test.
- **Self-improvement**: a lasting change to the system itself, such as a new skill, updated memory or an edited harness, that improves its results on a fixed test.
- **Recursive self-improvement**: improvement that also improves the system's ability to make further improvements, while the standard it is judged by gets harder too.
- **RSI (lab sense)**: AI fully autonomously designing and developing its own successor.
- **Reward hacking**: raising a score without doing the intended work, such as editing tests instead of fixing code.

## Sources

- Lilian Weng, [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Jul 2026)
- Zhang et al., [ACE: Agentic Context Engineering](https://arxiv.org/abs/2510.04618) (ICLR 2026)
- Philipp Schmid, [Recursive Self-Improvement](https://www.philschmid.de/recursive-self-improvement) (Aug 2026)
- Anthropic, [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) (Sep 2026)
- METR, [Independent Assessment of AI R&D Acceleration at Anthropic](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment) (Nov 2026)

Next: [12. What the sources agree on](12-what-the-sources-agree-on.md)
