---
title: "1. What an agent is"
nav_order: 2
---

# 1. What an agent is

## Starting from a chatbot

Most people first meet a language model through a chat interface. You type a message, the model writes a reply, and nothing more happens until you type again. In that setting the model only ever produces text for a person to read. If you ask it to fix a bug, it can describe the fix or write the corrected code, but it cannot open your files, apply the change, or run the tests to check that the fix works. You have to do those steps yourself and paste the results back into the chat.

An agent takes the person out of that middle step. Instead of a human copying text back and forth between the model and the computer, a program does it. The program gives the model a list of actions it may request, such as reading a file, running a command or searching the web. When the model's reply asks for one of those actions, the program performs it and returns the result to the model, which can then decide what to do next. Because the model sees the result of each action before it chooses the next one, it can work through a task step by step and correct itself along the way, without a person in the loop.

## The definition

Anthropic's post "Building effective agents" gives the definition that most sources now follow. An agent is a system in which a language model directs its own process and its own use of tools, deciding which steps to take and in what order, rather than following a sequence that a programmer fixed in advance. The same post adds that in practice an agent is usually just a model using tools in a loop, getting feedback from its environment at each step. The environment here means whatever the actions touch, such as a code repository, a web browser, a database or a lab instrument.

A second, shorter definition comes from the harness sources: an agent is a model plus a harness. The harness is all the software around the model that runs this loop, and page 6 covers it in detail. The two definitions describe the same thing from different sides. The first says what an agent does (it decides its own steps), and the second says what it is made of (a model and the code around it).

## The loop

The core of every agent is the same loop. To see it concretely, imagine asking a coding agent to fix a failing test.

The harness first sends the model a request that contains its instructions, descriptions of the tools it can use, and your task. The model replies that it wants to run the test suite. The harness runs the tests and sends the output back to the model, and the output shows an error in one function. The model asks to read the file that contains that function, and the harness sends back the file's contents. The model then asks to replace one line, the harness makes the edit, and the model asks to run the tests again. This time they pass, so the model replies with a short summary instead of another request, and the harness ends the loop and shows you the summary.

Every step in that story has the same shape. The model receives everything that has happened so far and produces either a request for an action or a final answer. The harness then either carries out the action and goes around the loop again, or stops. Even the most capable agents are doing nothing more complicated than this. What makes one agent better than another is mostly the quality of the model, the tools, the instructions, and how the harness manages the growing record of what has happened.

## Workflows and agents

Anthropic draws a useful line between two kinds of systems that use language models with tools. In a workflow, the programmer decides the sequence of steps in code. A workflow might always translate a document, then summarize the translation, then check the summary against a style guide, calling the model once at each stage. The model does the work inside each step, but it never chooses what the next step is. In an agent, the model makes that choice itself, as in the bug-fixing example, where nobody decided in advance how many files it would read or how many times it would run the tests.

Anthropic calls both of these agentic systems. Workflows are more predictable and cheaper, and they suit tasks whose steps are known in advance. Agents suit open-ended tasks where the number and kind of steps cannot be predicted, at the cost of more tokens and a greater chance that one error leads to the next. The post's main advice is to start with the simplest system that works, which is often a single well-written call to the model, and to move toward an agent only when the task needs one.

## The classic parts: planning, memory and tools

Before the current generation of coding agents, Lilian Weng's 2023 post "LLM Powered Autonomous Agents" described an agent as a language model acting as the brain, supported by three components. Planning is how the agent breaks a large task into smaller steps and reflects on its mistakes so it can correct its course. Memory is how it keeps information, which Weng splits into short-term memory, meaning whatever is currently in the model's input, and long-term memory, meaning information stored outside the model and looked up when needed. Tool use is how it acts on the world and gets information that the model itself does not contain. These three parts still map well onto modern agents, and pages 5 and 8 return to tools and memory.

The CoALA paper (Sumers and colleagues) made this picture more precise by borrowing ideas from cognitive science. It describes an agent by three things. The first is its memory, which it divides into working, episodic, semantic and procedural memory (page 8 explains these). The second is its action space, meaning the set of things it can do, which CoALA divides into external actions on the world and internal actions such as retrieving from memory, reasoning and learning. The third is its decision cycle, in which the agent proposes possible actions, evaluates them, chooses one, carries it out and observes the result. You do not need CoALA's full vocabulary to build agents, but it is the clearest map of the parts if you want one.

## Why the code around the model matters

It is tempting to think that an agent is only as good as its model, so that a better agent simply means a newer model. The sources consistently say otherwise. Weng's 2026 post on harness engineering argues that the layer between the model and the outside world matters about as much as the model's raw ability, and later pages give examples where changing only the instructions or the tools moved an agent's results by several percentage points. This is why the rest of the primer spends as much time on the software around the model as on the model itself.

## Key vocabulary

- **Agent**: a system in which a language model decides its own steps and tool use, usually by calling tools in a loop until the task is done. Also described as a model plus a harness.
- **Environment**: whatever the agent's actions touch, such as a code repository, a browser, a database or a lab instrument.
- **Agent loop**: the repeated cycle in which the model reads everything so far and either asks for an action or gives an answer, and the harness carries out the action and sends back the result.
- **Workflow**: a system in which code, not the model, decides the sequence of steps.
- **Agentic system**: Anthropic's umbrella term for both workflows and agents.
- **Planning**: breaking a task into smaller steps and correcting course after mistakes.
- **Action space**: the set of things an agent can do in one step. CoALA splits it into external actions on the world and internal actions such as retrieving, reasoning and learning.
- **Decision cycle**: CoALA's name for one turn of the loop, in which the agent proposes actions, evaluates them, chooses one, carries it out and observes the result.

## Sources

- Anthropic, [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Dec 2024)
- Lilian Weng, [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Jun 2023)
- Sumers et al., [CoALA: Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) (TMLR 2024)
- Vivek Trivedy, [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (Mar 2026)
- Lilian Weng, [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Jul 2026)

Next: [2. The model](02-the-model.md)
