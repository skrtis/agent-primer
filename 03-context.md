---
title: "3. Context and the context window"
nav_order: 4
---

# 3. Context and the context window

## What goes into context

Because the model remembers nothing between calls, everything it can use in a call has to be in that call's **context**.

> **Context:** the entire block of text (tokens) the model receives in a single call ([Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)).

In a chat app, context is mostly the conversation so far. In an agent, one call usually includes:

- The **system prompt** (standing instructions for how the agent should behave, [page 4](04-prompts.md)).
- All **tool definitions** (names, descriptions, and expected inputs for every available tool, [page 5](05-tools.md)).
- Everything that has happened in the current run: your messages, the model's earlier replies, every tool request it made, and every tool result that came back.
- **Extra text added by the harness**, such as project instruction files (e.g., `CLAUDE.md`), automated hook outputs, or today's date.

## Messages and roles

Context is formatted as a list of messages, each labeled with a **role** showing where it came from:

- `system`: instructions from the developer or harness.
- `user`: messages from the person.
- `assistant`: the model's own earlier replies and tool requests.
- `tool result`: the output returned after running a tool (in Anthropic's interface, these are placed inside `user` messages).

Harnesses often insert their own text (such as `CLAUDE.md`, hook outputs, and reminders) inside `user`-role messages ([Agent SDK docs](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)). So a `user` message is not always typed by the human, and instructions do not come only from the system prompt.

## The context window and why longer inputs hurt

Every call also has to fit inside the model's **context window**.

> **Context window:** the maximum number of tokens a model can handle in one call, counting both input and output (typically 200,000 to 1,000,000 tokens today).

Agents fill their context windows quickly because every tool result stays in the message list. Reading 20 files and running a test suite a dozen times can fill a window within one task, forcing the harness to trim or summarize older turns ([page 7](07-context-engineering.md)).

Even before you hit the hard limit, packing more text into context hurts accuracy. [Chroma](https://www.trychroma.com/research/context-rot) tested 18 models, holding task difficulty fixed and only adding more input text, and performance dropped steadily as inputs got longer, even on simple tasks. They call this **context rot**.

> **Context rot:** the drop in a model's accuracy as its input gets longer, even when the task itself stays equally easy.

Where information sits in a long input also matters. [Liu et al.](https://arxiv.org/abs/2307.03172) found that on question answering over many documents, accuracy was highest when the document holding the answer came first or last, an effect they named **lost in the middle**. The size of the effect varies across newer models and tasks.

> **Lost in the middle:** a model uses information at the start or end of a long input more reliably than information buried in the middle.

[Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) explains why extra text is never free with the idea of an **attention budget**: irrelevant text competes with relevant text for the model's attention.

> **Attention budget:** the limited attention a model spreads across everything in its input, so each extra token takes a little attention away from the rest.

The goal is not fitting as much as possible into the window, but keeping the signal-to-noise ratio high on every call.

## Context is scratch paper, not saved storage

Context is rebuilt on every call and thrown away when a session ends. Think of it as working memory (what you are holding in mind right now), not long-term storage. Information that needs to last until tomorrow has to be saved outside the model and read back later ([page 8](08-memory.md)).

## Sources

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Chroma, [Context Rot](https://www.trychroma.com/research/context-rot) (Jul 2025)
- Liu et al., [Lost in the Middle](https://arxiv.org/abs/2307.03172) (TACL 2024)
- Anthropic, [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) (Agent SDK docs)

Next: [4. Prompts](04-prompts.md)
