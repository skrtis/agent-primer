---
title: "3. Context and the context window"
nav_order: 4
---

# 3. Context and the context window

## What goes into context

> **Context:** the entire block of text (tokens) the model receives in a single call ([Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)). 

Because the model remembers nothing between calls, the context is its entire world for that turn.

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

> **Context window:** the maximum number of tokens a model can handle in one call, counting both input and output (typically 200,000 to 1,000,000 tokens today).

Agents fill this quickly because every tool result stays in the message list. Reading 20 files and running a test suite a dozen times can fill a window within one task, forcing the harness to trim or summarize older turns ([page 7](07-context-engineering.md)).

Even before you hit the hard limit, packing more text into context hurts accuracy. Three terms describe how:

> **Context rot:** the drop in a model's accuracy as its input gets longer, even when the task itself stays equally easy.

[Chroma](https://www.trychroma.com/research/context-rot) tested 18 models, holding task difficulty fixed and only adding more input text, and performance dropped steadily as inputs got longer, even on simple tasks.

> **Lost in the middle:** a model uses information at the start or end of a long input more reliably than information buried in the middle.

[Liu et al.](https://arxiv.org/abs/2307.03172) found this on question answering over many documents, where accuracy was highest when the document holding the answer came first or last. The size of the effect varies across newer models and tasks.

> **Attention budget:** the limited attention a model spreads across everything in its input, so each extra token takes a little attention away from the rest.

[Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) uses this to explain why irrelevant text is not free: it competes with the relevant text for the model's attention.

The goal is not fitting as much as possible into the window, but keeping the signal-to-noise ratio high on every call.

## Context is scratch paper, not saved storage

Context is rebuilt on every call and thrown away when a session ends. Think of it as working memory (what you are holding in mind right now), not long-term storage. Information that needs to last until tomorrow has to be saved outside the model and read back later ([page 8](08-memory.md)).

## Sources

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Chroma, [Context Rot](https://www.trychroma.com/research/context-rot) (Jul 2025)
- Liu et al., [Lost in the Middle](https://arxiv.org/abs/2307.03172) (TACL 2024)
- Anthropic, [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) (Agent SDK docs)

Next: [4. Prompts](04-prompts.md)
