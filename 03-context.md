---
title: "3. Context and the context window"
nav_order: 4
---

# 3. Context and the context window

## What the context is

Anthropic's post on context engineering defines the context as the set of tokens the model sees when it produces its output. Put simply, the context is the full input of one call. Because the model is stateless (page 2), the context is its entire world for that call, and anything outside it does not exist as far as the model is concerned.

In a chat, the context is mostly the conversation so far. In an agent it holds more. A typical call from a coding agent includes the system prompt, which carries the harness's standing instructions (page 4), and the definitions of every tool the model may use (page 5). It also includes the conversation so far, meaning your messages, the model's earlier replies, every tool request it made and every result that came back. Finally, it includes any extra material the harness inserts, such as the contents of a project instruction file or a reminder of today's date.

## Messages and roles

Model interfaces organize the context as a list of messages, and each message has a role that tells the model where it came from. The system role carries the developer's or the harness's instructions. The user role carries messages from the person. The assistant role carries the model's own earlier replies, including its tool requests. Tool results come back as their own kind of message; in Anthropic's interface they travel inside user-role messages.

One detail is worth knowing early. Harnesses often put their own text inside user-role messages, alongside what the person typed. Claude Code, for example, inserts the contents of a project's CLAUDE.md file, the output of hooks and various reminders into the conversation this way, as the Agent SDK documentation describes. So a message in the user role is not proof that the user wrote it, and the system prompt is not the only place that instructions come from.

## The context window

The context window is the largest number of tokens the model can handle in one call, counting both the input and the output it writes. For current models it is typically hundreds of thousands of tokens, and some offer a million. That sounds like a lot, but agents fill it quickly. Every tool result stays in the conversation once it arrives, so an agent that reads twenty files and runs the tests a dozen times can build up a very long context within a single task. When the context approaches the limit, the harness has to do something about it, such as summarizing the older parts, which page 7 describes.

## Why more context is not always better

A natural assumption is that a larger window solves the problem, since you could simply give the model everything. The sources agree that this does not work. Chroma's "Context Rot" study tested 18 models on tasks whose difficulty was held fixed while only the length of the input changed, and it found that performance fell as the input grew longer, even on simple tasks. An older paper, "Lost in the Middle" (Liu and colleagues, 2023), found that models used information at the start and end of a long input more reliably than information in the middle, although later work suggests that the size of this effect depends on the model and the task. Anthropic describes the underlying idea as an attention budget. Each additional token draws on the model's limited capacity to attend to everything else, so irrelevant tokens are not free, because they make the relevant ones harder to use.

The practical consequence is that the goal is not to fit as much as possible into the context but to fit the right things into it. Deciding what those things are on every call is the subject of context engineering (page 7).

## Context is not memory

Because the context is rebuilt for every call and disappears when a session ends, it is not memory in the everyday sense. It is closer to what you are holding in mind at this moment than to what you could recall tomorrow. Information that must survive from one session to the next has to be stored somewhere else and loaded back into the context when it is needed, which is the subject of page 8.

## Key vocabulary

- **Context**: everything the model sees in one call.
- **Message and role**: the context is a list of messages, each marked as coming from the system (the developer or the harness), the user, or the assistant (the model itself).
- **Tool result**: the output of a tool, returned to the model as its own kind of message.
- **Context window**: the maximum number of tokens the model can handle in one call, input and output together.
- **Context rot**: the decline in a model's performance as its context grows longer, even on tasks of fixed difficulty.
- **Lost in the middle**: the finding that models use information at the start and end of a long input more reliably than information in the middle.
- **Attention budget**: the idea that each token uses up part of the model's limited capacity to attend, so irrelevant tokens have a cost.

## Sources

- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Chroma, [Context Rot](https://www.trychroma.com/research/context-rot) (Jul 2025)
- Liu et al., [Lost in the Middle](https://arxiv.org/abs/2307.03172) (TACL 2024)
- Anthropic, [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts) (Agent SDK docs)

Next: [4. Prompts](04-prompts.md)
