---
title: "10. Evals"
nav_order: 11
---

# 10. Evals

## Why agents need evals

An eval, short for evaluation, is a test that measures how well an AI system performs. Agents need evals more than most software does, for two reasons. First, their behaviour varies, so the same agent given the same task twice can take different steps and reach different results. Second, as earlier pages showed, small changes to a prompt, a tool or the model can have large and unexpected effects, such as the one-line system prompt change on page 4 that passed early tests but lowered performance. Without evals, there is no reliable way to know whether a change made an agent better or worse.

## The vocabulary

Anthropic's "Demystifying evals for AI agents" sets out the standard terms. A task is a single test case: an input, such as a request and a starting environment, together with a definition of success. A trial is one attempt at a task, and because results vary, each task is usually run several times. The transcript, also called a trace or trajectory, is the complete record of a trial, including every model output and every tool call. The outcome is the final state of the environment at the end of the trial, such as whether the tests now pass or what is now in the database. A grader is whatever decides whether a trial succeeded. The software that runs the tasks and grades them is called the evaluation harness, which is separate from the agent harness being tested.

One point in that post is easy to overlook. When you evaluate an agent, you are evaluating the model and its harness together, so a score belongs to that combination, not to the model alone.

## Graders

There are three kinds of grader. Code-based graders check the outcome with ordinary code, for example by running a test suite or comparing a value. They are fast, cheap and objective, but they can only check what can be written down as a rule. Model-based graders, often called LLM-as-judge, have a language model assess the result against a written rubric. They can judge things that are hard to code, such as whether an explanation is clear, but they are less consistent and need checking. Human graders are the most trustworthy and are mainly used to check the other two.

Hamel Husain and Shreya Shankar's guide adds firm advice on model-based graders. A judge works best when it answers a single yes-or-no question about one specific kind of failure, rather than giving a score from one to five. It should also be checked against human judgments on a set of examples before its verdicts are trusted.

## pass@k and pass^k

Two measures describe how an agent does over repeated trials, and they answer different questions. The measure pass@k is the chance that at least one of k trials succeeds. It suits situations where one success is enough, for example when you can generate several solutions and keep any one that passes the tests. The measure pass^k, introduced with the τ-bench benchmark (Yao and colleagues), is the chance that all k trials succeed. It suits situations where the agent must be reliable every time, such as an agent that handles customer requests.

The two move in opposite directions as k grows. Suppose an agent succeeds on a task 75 percent of the time. Its pass@3 is the chance that not all three trials fail, which is 1 minus 0.25 cubed, or about 98 percent. Its pass^3 is the chance that all three succeed, which is 0.75 cubed, or about 42 percent. The same agent looks nearly perfect by one measure and unreliable by the other, which is why a reported score should always say which measure it uses.

## Capability evals and regression evals

Anthropic distinguishes two purposes for evals.  
A capability eval contains tasks the agent cannot yet do well. It starts with a low pass rate and gives you something to improve toward.  
A regression eval contains tasks the agent already does reliably, with a pass rate near 100 percent, and its job is to catch changes that break something that used to work.

## Practical rules

The sources agree on a short list of rules. Start small, with roughly 20 to 50 tasks drawn from real failures rather than invented ones. Before building graders, read transcripts. Husain and Shankar call this error analysis: you read real runs, write down what went wrong, and group the problems into categories, so that you end up testing for failures that actually happen. Grade the outcome rather than insisting on particular steps, because a capable agent may find a valid route you did not anticipate. Give each trial a clean environment, so that trials do not affect each other. If a task fails on every trial, suspect the task or the grader before the agent. Report cost alongside accuracy, as Kapoor and colleagues argue in "AI Agents That Matter", because an agent that is slightly more accurate at ten times the cost may not be the better agent. Finally, remember that public benchmarks have flaws of their own. The Agentic Benchmark Checklist paper (Zhu and colleagues) found that problems in how tasks and rewards were set up could misstate an agent's performance by as much as 100 percent in relative terms.

## Key vocabulary

- **Eval**: a test that measures how well an AI system performs.
- **Task**: a single test case, made of an input and a definition of success.
- **Trial**: one attempt at a task.
- **Transcript (trace, trajectory)**: the complete record of a trial, including every model output and tool call.
- **Outcome**: the final state of the environment at the end of a trial.
- **Grader**: whatever decides whether a trial succeeded. Graders can be code-based, model-based or human.
- **LLM-as-judge**: using a language model as a grader.
- **Evaluation harness**: the software that runs the tasks and grades them, separate from the agent harness being tested.
- **pass@k**: the chance that at least one of k trials succeeds.
- **pass^k**: the chance that all k trials succeed.
- **Capability eval**: tasks the agent cannot yet do well, used to measure improvement.
- **Regression eval**: tasks the agent already does reliably, used to catch changes that break something.
- **Error analysis**: reading real transcripts, noting failures and grouping them into categories before designing tests.
- **Benchmark**: a shared, fixed set of tasks and scoring rules used to compare systems.

## Sources

- Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (Jan 2026)
- Hamel Husain and Shreya Shankar, [AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) (Sep 2026)
- Yao et al., [τ-bench](https://arxiv.org/abs/2406.12045) (ICLR 2025)
- Kapoor et al., [AI Agents That Matter](https://arxiv.org/abs/2407.01502) (TMLR 2025)
- Zhu et al., [Agentic Benchmark Checklist](https://arxiv.org/abs/2507.02825) (NeurIPS 2025)

Next: [11. Self-improvement and RSI](11-self-improvement.md)
