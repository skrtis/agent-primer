---
title: "Start here"
nav_order: 1
permalink: /
---

# Agent primer

This is a short introduction to how AI agents work. It is meant to be read before the sources in [agent reading list](reading-list.md), so that the papers and blog posts make sense the first time through. It starts from the most basic definitions and builds up, and each page assumes only what the earlier pages have explained. It was written on 2026-11-21 from the sources on the reading list, mainly Lilian Weng's posts, the CoALA paper, the harness, tool, context and memory sources, and Anthropic's engineering blog. Every page ends with the sources it draws on, so you can go to the original when you want more depth.

## The whole idea in one paragraph

A large language model is a program that reads text and predicts the text that should come next. By itself it can only produce text. It cannot run code, open a file or search the web, and it does not remember anything between one request and the next. An agent is what you get when ordinary software is wrapped around the model so that its text can have effects. That software, called the harness, tells the model which actions (tools) are available, sends it a task, and reads its reply. When the reply asks for an action, the harness carries it out and sends the result back to the model, and this repeats until the model says the task is done. Most of what the field talks about, including system prompts, context engineering, memory, multi-agent systems and evals, is about building this loop well and checking whether it works.

## Pages

1. [What an agent is](01-what-an-agent-is.md): the definition, the loop, and the difference between agents and workflows.
2. [The model](02-the-model.md): what a language model is, what it can and cannot do, and why it remembers nothing between calls.
3. [Context and the context window](03-context.md): everything the model sees in one call, and why more is not always better.
4. [Prompts](04-prompts.md): prompt engineering, in-context learning, few-shot examples, chain of thought and the system prompt.
5. [Tools](05-tools.md): how a model asks for an action, how tools are described, MCP, code execution and skills.
6. [The harness](06-the-harness.md): the software around the model, the agent loop in detail, and long-running agents.
7. [Context engineering](07-context-engineering.md): how agents decide what goes into the context on every call.
8. [Memory](08-memory.md): where information is kept between calls and sessions, how it gets back to the model, and RAG.
9. [Multi-agent systems](09-multi-agent-systems.md): when several agents help and when they hurt.
10. [Evals](10-evals.md): how to measure whether an agent works.
11. [Self-improvement and RSI](11-self-improvement.md): agents that improve agents, and where that stands.
12. [What the sources agree on](12-what-the-sources-agree-on.md): the ideas that come up in nearly every source.
13. [Glossary](13-glossary.md): short definitions of every term, with the page that explains it.

## How to read it

Read the pages in order the first time. Page 1 gives the whole shape quickly. Pages 2 to 5 explain the parts one at a time (the model, its context, prompts and tools), and page 6 puts them together as the harness. Pages 7 to 11 cover the topics built on top of that foundation, page 12 collects the ideas that almost every source shares, and page 13 is a glossary to come back to.

## A note on words

The field is young, and authors do not always use the same word for the same thing. The words "harness" and "memory" in particular mean slightly different things in different sources. Where that happens, the page says so and explains each meaning, rather than choosing one and hiding the others.

## Key vocabulary

- **Large language model (LLM)**: a program trained on huge amounts of text that predicts what text should come next.
- **Agent**: a model wrapped in software that lets it take actions in a loop until a task is done.
- **Harness**: the software around the model that runs that loop.
- **Tool**: an action the harness can carry out when the model asks for it, such as running a command or reading a file.

Next: [1. What an agent is](01-what-an-agent-is.md)
