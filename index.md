---
title: "Start here"
nav_order: 1
permalink: /
---

# Agent engineering primer

A concise guide to the ideas and terms behind LLM agents (~35 minutes to read, excluding the glossary). Full list of sources: [reading list](reading-list.md). This primer aims to introduce the techniques and concepts to build rigorous and effective agentic systems. 

## summary 

A language model takes in text and outputs text. On its own, it cannot run code, open files, search the web, or remember anything from one request to the next. An **agent** is just an LLM in addition to ordinary software (called the **harness**) which wraps the model in a loop: the software tells the model which actions (**tools**) are available, carries out whichever action the model asks for, sends the result back to the model, and repeats until the model finishes the task. Almost everything in agent engineering (prompts, tools, context management, memory, multi-agent setups, and evals) comes down to two limits of the model: it remembers nothing between calls, and its accuracy drops as its input gets long and crowded.

## Pages

1. [What is an agent?](01-what-an-agent-is.md) (3 min): the agent loop, `model + harness`, and workflows vs. agents.
2. [LLMs](02-the-model.md) (2 min): how models are trained for reasoning and tools, why they forget between calls, and extended thinking.
3. [Context and the context window](03-context.md) (2 min): what goes into each call, message roles, and why longer inputs hurt accuracy.
4. [Prompts](04-prompts.md) (3 min): in-context learning, system prompts, and why small wording edits need testing.
5. [Tools](05-tools.md) (3 min): how models request actions, tool design, MCP, writing code instead of calling tools, and skills.
6. [The harness](06-the-harness.md) (6 min): the software around the model, long-running tasks, checks and rules, why harness tricks go stale, and the Claude Agent SDK.
7. [Context engineering](07-context-engineering.md) (2 min): how context goes wrong, practical fixes, and lessons from Manus.
8. [Memory](08-memory.md) (3 min): where saved information lives, why rewriting memories can hurt, RAG, and why plain files often win.
9. [Multi-agent systems](09-multi-agent-systems.md) (2 min): when splitting work across agents helps and when it breaks down.
10. [Evals](10-evals.md) (3 min): testing agents, graders, `pass@k` vs. `pass^k`, and common benchmark traps.
11. [Self-improvement and RSI](11-self-improvement.md) (2 min): agents improving agents, what labs mean by RSI, and current limits.
12. [Core principles](12-what-the-sources-agree-on.md) (2 min): eight takeaways that hold up across the literature, plus open disagreements.
13. [Glossary](13-glossary.md) (reference): alphabetical definitions of every term, indexed by page.

Next: [1. What is an agent?](01-what-an-agent-is.md)
