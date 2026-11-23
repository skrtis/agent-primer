---
title: "9. Multi-agent systems"
nav_order: 10
---

# 9. Multi-agent systems

## How they work and why they help

A **multi-agent system** splits one task across several agents, each running its own loop and its own context window. The most common setup is the **orchestrator-worker pattern**: a lead agent (**orchestrator**) plans the work, launches **subagents** with fresh contexts and separate instructions, and combines their condensed summaries into a final answer.

Two main advantages drive the gains:

- **Context isolation:** a subagent can read dozens of files or papers while returning only a short summary, keeping the lead agent's context small and focused.
- **Parallelism:** independent subtasks run at the same time.

On an internal research benchmark, a Claude Opus 4 lead agent with Claude Sonnet 4 subagents outperformed a single Opus 4 agent by **90.2%** ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)). The cost is tokens: single agents use roughly **4×** the tokens of chat, and multi-agent runs use roughly **15×**. On one benchmark, total token count explained most of the performance gap, suggesting much of the gain comes simply from spending more total compute on the problem.

Because a subagent knows only what its **brief** tells it, vague instructions lead subagents to duplicate each other's work. Good briefs state the exact goal, the expected output format, which tools or sources to use, and clear task boundaries; the lead agent also needs guidance on how much effort a question deserves so it does not spin up a fleet of subagents for a simple query ([Anthropic](https://www.anthropic.com/research/multi-agent-research-system)).

## Why multi-agent systems fail

Every action an agent takes carries implicit decisions. When closely connected work is split among isolated agents that cannot see each other's reasoning, those decisions conflict (for example, two subagents building a game draw mismatched visual styles for the background and character) ([Cognition](https://cognition.com/blog/dont-build-multi-agents)). Letting agents communicate directly can help align those decisions, but adds coordination overhead and extra tokens.

Cognition's [updated report](https://cognition.com/blog/multi-agents-working) narrowed this view: keep a **single agent responsible for writing changes**, while separate agents in clean contexts give advice and review the finished work (catching mistakes the writer missed). Having multiple agents edit the same code at the same time still breaks down.

## What the evidence shows

- **Task structure decides everything:** testing 260 setups across tasks, models, and multi-agent designs found effects ranging from **+81%** on tasks that split cleanly into independent parts to **-70%** on tasks requiring careful step-by-step planning ([Kim et al.](https://arxiv.org/abs/2512.08296)).
- **Common failure modes:** analyzing 1,600+ failed multi-agent runs grouped errors into three buckets: poor system design, misunderstandings between agents, and inadequate checking of results ([Cemri et al.](https://arxiv.org/abs/2503.13657)).

| Good fit for multi-agent | Bad fit for multi-agent |
|---|---|
| Broad, parallel, read-heavy work (literature search, codebase exploration, independent review) | Closely connected, step-by-step work where one change affects every other part (most coding) |

## Sources

- Anthropic, [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (Jun 2025)
- Walden Yan (Cognition), [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) (Jun 2025)
- Cognition, [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working) (Apr 2026)
- Kim et al., [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Dec 2025)
- Cemri et al., [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (NeurIPS 2025)

Next: [10. Evals](10-evals.md)
