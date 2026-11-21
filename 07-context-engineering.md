---
title: "7. Context engineering"
nav_order: 8
---

# 7. Context engineering

## What it is

Page 3 established that the context is everything the model sees in one call, and that more context is not always better. Context engineering is the work of deciding what goes into the context on each call. Anthropic defines it as curating and maintaining the best set of tokens while the model is running, and sums up its aim as finding the smallest set of high-signal tokens that gives the best chance of the outcome you want. It differs from prompt engineering in that it is not done once. In an agent, the context changes on every turn of the loop as tool results arrive and the conversation grows, so these decisions are made over and over, mostly by the harness.

## How context goes wrong

Drew Breunig names the common ways in which a context fails, and naming them makes them easier to spot. Context poisoning happens when a mistake or a hallucination enters the context and the model keeps building on it, because to the model everything in its context looks like established fact. Context distraction happens when the context becomes so long that the model leans on it too heavily, for example by repeating its earlier actions, instead of using what it learned in training. Context confusion happens when irrelevant material, such as the definitions of many tools the task does not need, steers the model toward poor choices. Context clash happens when parts of the context contradict each other, as when two sets of instructions disagree. Context rot (page 3) runs underneath all of these, since each of them gets worse as the context grows.

## The main techniques

The sources describe a small set of techniques that between them handle most of these problems.

Just-in-time retrieval means keeping short references in the context, such as file paths, links or search queries, and loading the full content only when it is needed. Claude Code works this way. Instead of loading a whole codebase into the context, it keeps the names of the files it has seen and uses search tools to read specific files when it needs them. This keeps the context small, at the price of some extra tool calls.

Compaction means summarizing a long conversation when the context nears its limit and then continuing with the summary in place of the full history. Anthropic recommends tuning the summary so that it keeps the important things, such as the decisions made, unresolved problems and recently used files. It also notes that the lightest form of compaction is simply clearing out old tool results that are no longer needed.

Structured note-taking means having the agent write its progress, plans and findings to files outside the context, such as a NOTES.md file or a to-do list, and read them back when needed. Notes survive compaction and even the end of a session, which is how the long-running agents on page 6 keep their place.

Subagents give a piece of work to a separate agent with its own fresh context. The subagent may read dozens of files or pages, but only its short summary comes back to the main agent, so the main context stays clean. Page 9 discusses this further.

Offloading means saving large tool outputs to files instead of placing them in the context, leaving only a short reference behind. Choosing a small, relevant set of tools for a task is the same idea applied to tool definitions.

## Lessons from building Manus

The post "Context Engineering for AI Agents: Lessons from Building Manus" adds three practical lessons from running an agent at scale. Agents on long tasks tend to drift from their original goal, so Manus has the agent rewrite its to-do list regularly, which places the current plan at the end of the context, where the model attends to it most. Failed actions and error messages should be left in the context, because seeing them helps the model avoid repeating the mistake. And a context full of very similar past actions can lead the model to copy the pattern without thinking, so a little variation in how actions and results are recorded helps.

## Where context engineering meets memory

Several of these techniques, especially note-taking and offloading, work by moving information out of the context into files and bringing it back later. That is also exactly what memory is, and the next page picks up from here.

## Key vocabulary

- **Context engineering**: deciding what goes into the context on every call of an agent's loop.
- **Context poisoning**: a mistake or hallucination enters the context and the model keeps building on it.
- **Context distraction**: a very long context makes the model lean on it too heavily, for example by repeating earlier actions.
- **Context confusion**: irrelevant material in the context steers the model toward poor choices.
- **Context clash**: parts of the context contradict each other.
- **Just-in-time retrieval**: keeping short references in the context and loading the full content only when it is needed.
- **Structured note-taking**: the agent writing its progress and plans to files outside the context and reading them back later.
- **Offloading**: saving large tool outputs to files and leaving only a short reference in the context.

## Sources

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Drew Breunig, [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) (Oct 2026)
- Chroma, [Context Rot](https://www.trychroma.com/research/context-rot) (Jul 2025)
- Yichao Ji, [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) (Jul 2025)

Next: [8. Memory](08-memory.md)
