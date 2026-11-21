---
title: "5. Tools"
nav_order: 6
---

# 5. Tools

## What a tool is

A tool is a function that lives outside the model and that the model can ask to have run. Running a shell command, reading or editing a file, searching the web, querying a database and calling a company's API are all typical tools. The essential point, which every source on tool use makes, is that the model never runs a tool itself. As page 2 explained, a model can only produce text. What it produces is a structured request that says which tool it wants and with which inputs. The harness reads that request, runs the real function and sends the result back.

## How a tool is described to the model

For the model to use a tool, it has to know that the tool exists and what it does. The harness provides this through a tool definition, which has three parts. The first is a name. The second is a description, written in plain language, that explains what the tool does and when to use it. The third is a schema that lists the tool's parameters and their types, usually written in a format called JSON Schema. For example, a file-reading tool might be named read_file, be described as returning the contents of the file at a given path, and have one required parameter called path, which must be a string.

Tool definitions are sent with every call as part of the context. The model decides whether and when to use a tool based on its name and description, so the description is really a piece of prompt text and deserves the same care as the system prompt. Anthropic has written that, while building its SWE-bench agent, it spent more time refining the tools than the overall prompt.

## One tool call, step by step

The exchange between the model and the harness during a tool call always follows the same steps.

1. The harness sends a call containing the system prompt, the tool definitions and the conversation so far.
2. The model decides that a tool would help and, instead of a final answer, writes a tool call: the tool's name and the inputs, formatted to match the schema. It then stops writing.
3. The harness reads the tool call, checks that it is valid and allowed (it may ask the user for permission first), and runs the actual function.
4. The harness takes the output, shortens it if it is very long, and adds it to the conversation as a tool result.
5. The harness calls the model again with the longer conversation, and the model either requests another tool or gives its final answer.

The term function calling is often used for this mechanism, and especially for step 2, because the model is in effect writing a call to a function, with arguments that must match the function's declared parameters.

## What makes a good tool

Anthropic's post "Writing effective tools for agents" collects the practical rules, and the other sources agree with them. It is better to have a few tools that each do a complete, meaningful job than many small tools that mirror every endpoint of an API. Every definition costs context, and overlapping tools leave the model unsure which one to choose. A good test is whether a person reading the tool list could say which tool fits a given task, because if a person cannot, neither can the model. Names should be clear and grouped by the service they belong to, descriptions should be written as if for a new colleague, and parameter names should be unambiguous (user_id rather than user). Tools should return information the model can use directly, such as names rather than opaque internal ID numbers, and they should limit how much they return, through options such as pagination or truncation. Error messages should explain what went wrong and how to fix the request, because the model will read them and try again.

An older line of research makes the same point in general terms. The SWE-agent paper (Yang and colleagues, 2024) argued that a language model is a new kind of computer user and needs its own interface, which the authors called the agent-computer interface. They showed that changing only that interface changed how well the same model performed on software tasks.

## MCP

Every application that wants to give a model access to a service, such as a calendar, a code host or a database, needs tool definitions for that service and code that runs them. Without a standard, each application would have to write its own integration for each service. The Model Context Protocol (MCP) is an open standard that solves this. A service is wrapped once as an MCP server, which offers tools the model can call, along with resources (data the model can read) and prompts (reusable templates). An application such as Claude Code acts as the host, and for each server it connects to, it runs a client that talks to that server. Any application that supports MCP can then use any MCP server. The protocol's July 2026 revision made it stateless, meaning that each request is self-contained like an ordinary web request, which makes servers easier to run at large scale.

MCP has a cost. Every tool from every connected server adds its definition to the context, and a single large server can take up tens of thousands of tokens before the agent has done anything.

## Code execution and skills

Two newer ideas reduce that cost and change how tools are used.

The first idea is to let the model write code instead of making tool calls one at a time. With an ordinary tool call, every result passes back through the model's context, even when the model needs only a small part of it. If the model can instead write a short program that calls several tools, filters their output and prints only what matters, the intermediate data never enters the context. Anthropic's "Code execution with MCP" describes a task whose token use fell from about 150,000 to about 2,000 in this way. The earlier CodeAct paper (Wang and colleagues, 2024) found that agents whose actions were written as Python code succeeded more often than agents that used fixed-format tool calls. Philipp Schmid argues that agents may eventually need only one real tool, a sandbox that runs code, with every other tool available as a function inside it. The cost of this approach is that running code written by a model safely requires a sandbox and careful limits.

The second idea is skills. A skill is a folder containing a file called SKILL.md, which holds instructions for a particular kind of task, together with any scripts or reference documents it needs. At the start of a session the harness loads only each skill's name and one-line description. When a task matches a skill, the model reads the full instructions. This pattern, in which the model sees a short summary first and loads the details only when they are needed, is called progressive disclosure. It appears throughout agent design as a way of keeping the context small, and Simon Willison's post on skills gives the clearest account of it.

## Key vocabulary

- **Tool**: a function outside the model that the model can ask the harness to run.
- **Tool definition**: a tool's name, plain-language description and parameter schema, sent to the model with every call.
- **JSON Schema**: a standard format for describing the parameters a tool accepts and their types.
- **Tool call**: the model's structured request to run a tool, naming the tool and giving its inputs.
- **Tool result**: the output the harness sends back to the model after running the tool.
- **Function calling**: the common name for this mechanism, since the model writes a call whose arguments match the tool's declared parameters.
- **Agent-computer interface (ACI)**: the tools and formats through which an agent works with a computer, designed for a model rather than a person.
- **MCP (Model Context Protocol)**: an open standard that lets any compatible application use the tools, resources and prompts offered by any compatible server.
- **MCP host, client and server**: the host is the application (such as Claude Code), the client is the connection it keeps to one server, and the server is the program that offers the tools.
- **Code execution (code mode)**: letting the model write a program that calls tools inside a sandbox, so that only the program's printed output returns to the context.
- **Skill**: a folder with a SKILL.md file of instructions, plus any scripts or references, that the model loads only when a task needs it.
- **Progressive disclosure**: showing the model a short summary first and loading the details only when they are needed.

## Sources

- Nathan Lambert, [Lecture 11: Basics of LLM Tool Use](https://rlhfbook.com/teach/course/lec11-chap13-tools/)
- Anthropic, [Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents) (Sep 2025)
- Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Dec 2024)
- Yang et al., [SWE-agent](https://arxiv.org/abs/2405.15793) (NeurIPS 2024)
- Hou et al., [MCP: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278)
- MCP blog, [2026-07-28 specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)
- Anthropic, [Code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp) (Nov 2025)
- Wang et al., [CodeAct](https://arxiv.org/abs/2402.01030) (ICML 2024)
- Philipp Schmid, [Why Agents Are Soon Only Going to Have 1 Tool](https://www.philschmid.de/code-mode) (Nov 2026)
- Simon Willison, [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/) (Oct 2025)

Next: [6. The harness](06-the-harness.md)
