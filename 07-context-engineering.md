---
title: "7. Context engineering"
nav_order: 8
---

# 7. Context engineering

## What it is

A prompt is written once, but an agent's input changes on every turn as tool results pile up. Managing that changing input is **context engineering**, and the harness handles most of it.

> **Context engineering:** deciding what goes into the model's input on every turn of the loop, aiming for the smallest set of high-signal tokens that gets the job done ([Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)).

## How context goes wrong

All four failure modes below get worse as the context grows and context rot sets in ([page 3](03-context.md); [Breunig](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html)):

- **Context poisoning:** a mistake or hallucination enters the context and snowballs, because the model treats everything already in its context as established fact.
- **Context distraction:** the history gets so long that the model leans too heavily on past turns (for example, repeating earlier actions) instead of reasoning freshly.
- **Context confusion:** irrelevant material (like definitions for dozens of unused tools) pulls the model toward worse choices.
- **Context clash:** two parts of the context contradict each other (such as conflicting instructions).

## Core techniques

- **Just-in-time retrieval:** keep short pointers in context (file paths, links, search tools) and load full contents only when needed. Claude Code keeps track of file names and searches on demand rather than loading a whole codebase upfront, trading a few extra tool calls for a much cleaner context.
- **Compaction:** summarize older parts of the conversation when approaching the window limit and continue from the summary, keeping key decisions, open problems, and recently used files. The simplest version just clears out old tool outputs that are no longer needed ([Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)).
- **Structured note-taking:** have the agent write its plans, progress, and findings to external files (like `NOTES.md` or a to-do list) so they survive compaction and session restarts.
- **Subagents:** hand noisy exploration (reading dozens of files or web pages) to a separate agent with its own fresh context, returning only a short summary to the main agent ([page 9](09-multi-agent-systems.md)).
- **Offloading and minimal tool sets:** save huge tool outputs to files and leave only a file path and short snippet in context; only give the agent tools relevant to the current task.

## Practical lessons from Manus

Three findings from running long-horizon agents in production ([Ji](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)):

- **Rewrite the to-do list regularly:** placing the current plan at the very end of the context keeps the goal where the model pays the most attention, preventing drift on long tasks.
- **Keep failed attempts in context:** leaving errors and failed actions visible helps the model avoid repeating the exact same mistake.
- **Avoid overly repetitive formatting:** a long history of identically formatted actions can cause the model to copy the pattern blindly; small wording variations help break the habit.

Moving information out of context into files and loading it back later is where context engineering overlaps with memory ([page 8](08-memory.md)).

## Sources

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Drew Breunig, [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) (Oct 2026)
- Chroma, [Context Rot](https://www.trychroma.com/research/context-rot) (Jul 2025)
- Yichao Ji, [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) (Jul 2025)

Next: [8. Memory](08-memory.md)
