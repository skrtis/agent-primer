---
title: "10. Evals"
nav_order: 11
---

# 10. Evals

## Why agents need dedicated testing

An **eval** (short for evaluation) is a test suite measuring how well an AI system performs. Intuition fails for agents for two reasons:

1. **Run-to-run randomness:** giving the exact same agent the exact same task twice can lead to different steps and different final answers.
2. **High sensitivity:** small wording changes to a prompt or tool can cause unexpected drops (such as the -3% Claude Code drop from one line on [page 4](04-prompts.md)).

## Core terms

Standard definitions from [Anthropic](https://www.anthropic.com/research/demystifying-evals-for-ai-agents):

- **Task:** one test case (an input, a starting environment, and a definition of success).
- **Trial:** one attempt at a task; each task is usually run several times to measure consistency.
- **Transcript (trace / trajectory):** the complete record of a trial, including every model reply, tool request, and tool result.
- **Outcome:** the final state after the trial finishes (for example, whether the tests pass or what is now in the database).
- **Grader:** whatever decides whether a trial succeeded.
- **Evaluation harness:** the test software that runs tasks and grades them (separate from the agent harness being tested).

Remember that every score measures the model and its harness together, never the model alone.

## Graders

| Grader type | How it works | Strengths | Limits |
|---|---|---|---|
| **Code-based** | Unit tests, assertions, exact checks | Fast, cheap, repeatable | Only checks rules you can write in code |
| **Model-based (`LLM-as-judge`)** | A language model grades against a rubric | Can judge open-ended quality like clarity | Less consistent; needs checking |
| **Human** | Expert review | Most trustworthy | Slow and expensive; mainly used to check the other two |

For `LLM-as-judge`, ask a **single yes/no question** about one specific failure mode rather than a 1 to 5 rating scale, and check the judge against human labels before trusting its verdicts ([Husain & Shankar](https://hamel.dev/blog/posts/evals-faq/)).

## `pass@k` vs. `pass^k`

Two metrics summarize repeated trials, and they move in opposite directions as `k` grows:

- **`pass@k`:** chance that *at least one* of `k` trials succeeds. Useful when you can try several times and keep any working answer.
- **`pass^k`:** chance that *all* `k` trials succeed ([τ-bench](https://arxiv.org/abs/2406.12045)). Useful when the agent has to be reliable every single time.

If an agent succeeds 75% of the time on a single try:

- `pass@3 = 1 - 0.25^3 ≈ 98%`
- `pass^3 = 0.75^3 ≈ 42%`

The same agent looks nearly perfect under `pass@3` and unreliable under `pass^3`. Always note which metric is reported.

## Capability vs. regression evals

- **Capability evals:** tasks the agent currently struggles on (low pass rate), giving you a clear target to improve toward.
- **Regression evals:** tasks the agent already passes near 100%, catching changes that accidentally break working behavior ([Anthropic](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)).

## Practical rules

- **Start small and real:** begin with 20 to 50 tasks drawn from real failures rather than invented prompts.
- **Do error analysis before writing graders:** read real transcripts, list what went wrong, and group failures into categories so you test bugs that actually happen ([Husain & Shankar](https://hamel.dev/blog/posts/evals-faq/)).
- **Grade outcomes, not exact steps:** check the final result instead of forcing one specific path, because strong agents often find valid routes you did not anticipate.
- **Start every trial clean:** isolate each run so leftover files or changes never affect the next trial.
- **Check 0% tasks first:** if every single trial fails, suspect a bug in the task or grader before blaming the agent.
- **Report cost alongside accuracy:** an agent that scores slightly higher at 10× the token cost may not be better ([Kapoor et al.](https://arxiv.org/abs/2407.01502)).
- **Be careful with public benchmarks:** flaws in how benchmark tasks and grading rules are built can misstate performance by up to 100% in relative terms ([Zhu et al.](https://arxiv.org/abs/2507.02825)).

## Sources

- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (Jan 2026)
- Hamel Husain and Shreya Shankar, [AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) (Sep 2026)
- Yao et al., [τ-bench](https://arxiv.org/abs/2406.12045) (ICLR 2025)
- Kapoor et al., [AI Agents That Matter](https://arxiv.org/abs/2407.01502) (TMLR 2025)
- Zhu et al., [Agentic Benchmark Checklist](https://arxiv.org/abs/2507.02825) (NeurIPS 2025)

Next: [11. Self-improvement and RSI](11-self-improvement.md)
