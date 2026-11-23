---
title: "1. What is an agent?"
nav_order: 2
---

# 1. What is an agent?

## Chatbot vs. agent

**Scenario:** Suppose a Python script you wrote crashes, and you ask a chatbot such as ChatGPT to fix it. The chatbot can only reply with text, so you do every step outside the chat yourself: you paste in the code and the error, it suggests a change, you make the edit, run the script again, and paste back any new error. An agent hands those steps to a program, called the **harness**. The harness gives the model a list of actions (**tools**) it can ask for (reading a file, running a command, searching a database), runs whichever action the model requests, and sends the result back. Because the model sees each result before deciding what to do next, it can work through a problem step by step and correct its own mistakes.

2 common definitions of agents describe the same thing from different angles:

- **By what it does** ([Anthropic](https://www.anthropic.com/research/building-effective-agents)): a system where a language model chooses its own steps and tool calls in a loop, using feedback from its **environment** (such as a code repository, browser, database, or lab instrument).
- **By what it is made of** ([Trivedy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)): **agent = model + harness**, where the harness is all the surrounding software that runs the loop ([page 6](06-the-harness.md)).

## The agent loop
In general terms, the loop is:

1. Start a message list that holds your request.
2. Send the model the system prompt, the list of tools, and the whole message list.
3. Add the model's reply to the message list.
4. If the reply asks for no tools, show it to you and stop.
5. Otherwise, run each tool the model asked for and add each result to the message list.
6. Go back to step 2.

Two things about this loop matter for the rest of the primer:

- **The model never runs anything itself.** It only writes a text request asking for an action, and the harness runs it, so the harness decides what the agent is allowed to do ([page 6](06-the-harness.md)).
- **Every pass through the loop is a fresh call to the model** that sends the whole message list again, because the model remembers nothing between calls ([page 2](02-the-model.md)). The list grows with every tool result, and the model's accuracy drops as its input gets longer ([page 3](03-context.md)).
- **WE TYPICALLY** do not have to write the agent loop, its already included in the query() function in Claude SDK.

Even the strongest coding agents run this same loop. What separates a good agent from a weak one is the model, the tools, the instructions, and how the harness manages that growing list of messages.

## Workflows vs. agents

Anthropic groups both under **agentic systems**, separated by who decides the sequence of steps:

|              | Who picks the steps                                                                                                   | Best for                                                       | Tradeoff                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Workflow** | The programmer fixes the steps in code (e.g., summarize a paper → list the compounds it tested → add them to a table) | Known, repeatable pipelines                                    | Predictable and cheap; rigid on open-ended tasks                                     |
| **Agent**    | The model chooses each next step on the fly                                                                           | Open-ended tasks where you cannot predict the steps in advance | Flexible; makes more model calls (so costs more), and one early mistake can snowball |

The standard advice ([Anthropic](https://www.anthropic.com/research/building-effective-agents)): start with the simplest setup that works (often a single call to the model, or a fixed workflow), and add an autonomous agent loop only when the task genuinely needs one.

## Why this primer focuses on the harness  

A better agent does not just mean a newer model. The harness often matters about as much as the model's raw ability ([Weng](https://lilianweng.github.io/posts/2026-07-04-harness/)); for example, LangChain raised its coding agent's benchmark score from 52.8% to 66.5% by changing only the system prompt, tools, and checks around the same model ([Trivedy](https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering); [page 6](06-the-harness.md)).

## Sources

- Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Dec 2024)
- Vivek Trivedy, [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (Mar 2026)
- Lilian Weng, [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Jul 2026)
- Vivek Trivedy, [Improving Deep Agents with Harness Engineering](https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering) (Feb 2026)

Next: [2. LLMs](02-the-model.md)
