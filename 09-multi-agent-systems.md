---
title: "9. Multi-agent systems"
nav_order: 10
---

# 9. Multi-agent systems

## What they are

A multi-agent system uses several agents, each running its own loop with its own context, to work on one task. The most common design is the orchestrator-worker pattern. A lead agent, also called the orchestrator, reads the task, makes a plan and starts several subagents, giving each one a piece of the work and its own instructions. Each subagent works in its own fresh context and returns a condensed result. The lead agent then combines the results into a final answer.

## Why use several agents

The main benefit is context isolation. A subagent can read dozens of documents or files while it explores its part of the problem, but only its short summary returns to the lead agent, so the lead's context stays small and focused. A second benefit is parallelism, since subagents with independent pieces of work can run at the same time.

Anthropic's "How we built our multi-agent research system" gives the best-known numbers. On an internal research evaluation, a system with a lead agent running on Claude Opus 4 and subagents running on Claude Sonnet 4 performed 90.2 percent better than a single Opus 4 agent working alone. The price was tokens. Anthropic reports that agents typically use about four times as many tokens as a chat, and multi-agent systems about fifteen times as many. In its analysis of one benchmark, the number of tokens used explained most of the difference in performance, which suggests that much of the gain comes from being able to spend more total effort on the problem.

The same post gives practical advice on briefing subagents, since a subagent knows only what the lead agent tells it. Each subagent needs a clear objective, a description of what its output should look like, guidance on which tools and sources to use, and clear limits on its task. When the briefs were vague, subagents duplicated each other's work. The lead agent also needs guidance on how much effort a task deserves, because otherwise it may start many subagents for a simple question.

## Why multi-agent systems fail

Cognition, the company behind the Devin coding agent, made the opposite case in "Don't Build Multi-Agents". Its argument is that every action an agent takes carries implicit decisions, and when work is split among agents that cannot see each other's reasoning, those decisions conflict. The post's example was a simple game split between two subagents, where one drew the background in one visual style and the other drew the character in a completely different one, so the pieces did not fit together. Cognition recommended a single agent working through the task in one continuous context.

- my own note: if the agents could communicate that these implicity decisions can be steered to coherence together

Its later post, "Multi-Agents: What's Actually Working", narrowed this view rather than reversing it. What works, Cognition found, is to keep a single agent responsible for writing changes while other agents contribute advice and review rather than actions. A reviewer agent that sees only the finished change, in a clean context, catches mistakes that the writing agent missed. What still does not work is several agents editing the same code in parallel.

## What the evidence says

Two research papers support a middle position. Kim and colleagues tested 260 configurations across several tasks, model families and multi-agent designs. They found that the effect of using multiple agents ranged from an 81 percent improvement on a task that split naturally into independent parts to a 70 percent decline on a task that required careful step-by-step planning. Cemri and colleagues analysed more than 1,600 recorded runs of multi-agent systems and grouped their failures into three kinds: problems with how the system was designed, misunderstandings between agents, and failures to check the work properly.

Anthropic and Cognition, despite their different headlines, agree on where the line falls. Multiple agents help with work that is broad, can be split into independent pieces and mostly involves reading, such as research. They hurt with work whose pieces depend closely on each other and share state, such as most coding, where one agent's change affects what every other agent should do.

## Key vocabulary

- **Multi-agent system**: several agents, each with its own loop and context, working on one task.
- **Orchestrator (lead agent)**: the agent that plans the work, starts subagents and combines their results.
- **Subagent**: an agent started by another agent to do one piece of work in its own context.
- **Orchestrator-worker pattern**: the design in which a lead agent hands pieces of work to subagents and combines what they return.
- **Context isolation**: keeping a subagent's work out of the lead agent's context, so that only its summary comes back.
- **Parallelism**: running independent pieces of work at the same time.
- **Brief**: the instructions a lead agent gives a subagent, which are all the subagent knows about its task.

## Sources

- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (Jun 2025)
- Walden Yan (Cognition), [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) (Jun 2025)
- Cognition, [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working) (Apr 2026)
- Kim et al., [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Dec 2025)
- Cemri et al., [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (NeurIPS 2025)

Next: [10. Evals](10-evals.md)
