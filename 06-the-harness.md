---
title: "6. The harness"
nav_order: 7
---

# 6. The harness

## What the harness is

The harness is all the software around the model that turns it into an agent. Vivek Trivedy's post "The Anatomy of an Agent Harness" puts it most simply: if you're not the model, you're the harness. The source-code study by Barbaste and colleagues, which examined eleven production coding agents including Claude Code, Codex CLI and Gemini CLI, describes the harness as the runtime that connects a model to its environment. It lists the harness's jobs as running the loop, exposing tools, managing context, enforcing safety controls, coordinating work and providing ways to extend it.

The word is used at two scales, and it helps to know both. In the broad sense used above, the harness is everything except the model. Anthropic's "Scaling Managed Agents" uses it in a narrower sense, for just the loop that calls the model and routes its tool calls, and gives separate names to the other parts (described below). Birgitta Böckeler's article on Martin Fowler's site adds a further distinction. The inner harness is the part the agent's makers build and ship, such as the system prompt, the built-in tools and the loop. The outer harness is the part you add for your own project, such as instruction files, skills, hooks and checks. When a source says "harness", it is worth checking which of these it means.

## What the harness does

Each of the harness's jobs exists to make up for one of the model's limits from page 2. The model cannot act, so the harness runs tools on its behalf. The model sees only its context, so the harness assembles that context on every call from the system prompt, the tool definitions, any project instructions and the conversation so far. The model remembers nothing between calls, so the harness keeps the record of what has happened and stores anything that must outlast the session in files, logs or version control. The model can make mistakes with real consequences, so the harness enforces permissions, for example by asking the user before running a command that deletes files. It also runs code in a sandbox, which is an isolated environment where mistakes cannot damage the rest of the system. The context window is limited, so the harness shortens long tool outputs and summarizes old parts of the conversation when the window fills. Finally, for larger tasks the harness can coordinate several model calls or several agents, and it offers extension points such as MCP servers, skills and hooks.

## The agent loop in detail

With those jobs in mind, the loop from page 1 can be described more completely.

1. The harness assembles the context: the system prompt, the tool definitions, project instructions such as CLAUDE.md, the conversation so far and the user's task.
2. It sends this to the model in one call.
3. The model returns either a final answer, or one or more tool calls.
4. If there is no tool call, the loop ends and the answer goes to the user.
5. Otherwise the harness checks each tool call against its permissions and runs it, in the sandbox where appropriate.
6. It captures the result or the error, shortens it or saves it to a file if it is very large, and adds it to the conversation.
7. It checks the size of the context, compacting or trimming it if needed, and records what happened in the session log.
8. It returns to step 1.

Anthropic's description of its SWE-bench agent shows how little is needed for this to work. That agent had a short prompt, one tool for running shell commands and one for editing files, and it simply kept calling the model and returning tool results until the model said it was finished or the context window filled up. The study of eleven production harnesses found the same simplicity at their core. Their loops were plain hand-written code, and none of the systems was built on a general-purpose agent framework.

## Session, harness and sandbox

Anthropic's "Scaling Managed Agents" splits a running agent into three parts, each of which can fail or be replaced without losing the others. The session is a permanent, append-only log of everything that has happened, stored outside the model's context. The harness, in the narrow sense, is the loop that reads the session, builds the context, calls the model and routes tool calls. The sandbox is where code actually runs and files are edited. Keeping these apart means that a crashed sandbox does not lose the session, that a summarized context can be rebuilt from the full log, and that credentials can be kept outside the sandbox, where code written by the model cannot reach them.

## Long-running agents (relevant)

A single context window is not enough for a task that takes many hours or several days, and each new session starts with no knowledge of the previous ones. Anthropic's "Effective harnesses for long-running agents" describes one solution. An initializer agent runs once at the start and sets up the project. It writes a script for starting the application, a progress file, and a list of every feature with each one marked as failing, and it makes a first commit in version control. In every later session, a coding agent reads the progress file and the version history to learn where things stand, works on one feature, tests it, marks it as passing, commits, and updates the progress notes for the next session. The feature list exists so that the agent cannot declare the project finished early, and working on one feature at a time keeps each session's changes small and easy to check.

A related post, "Harness design for long-running application development", adds a second idea, which is to separate the agent that builds from the agent that judges. Models tend to rate their own work too highly, so the harness used one agent to write a plan, a second to build the application, and a third to test the running application and grade it against agreed criteria. The same post compares two ways of handling a full context. Compaction summarizes the conversation in place and continues, while a reset starts a fresh agent that picks up from a structured handoff note. Resets helped one model that tended to rush to finish as its context filled, and they became unnecessary with a later model.

## Guides and sensors

Böckeler's article is the most useful guide to the outer harness, the part you build yourself. She sorts its pieces into guides and sensors. Guides act before the agent does anything and steer it in the right direction; instruction files such as CLAUDE.md, written conventions and skills are all guides. Sensors act after the agent has done something and check the result, so that the agent can correct itself; tests, linters, type checkers and review by another model are all sensors. A harness with only guides never checks whether its rules were followed, and a harness with only sensors lets the agent repeat the same mistake every time, so both are needed. **She also distinguishes computational checks, such as tests, which are deterministic, fast and cheap, from inferential checks, such as review by a model, which can judge meaning but are slower, costlier and less reliable.**

## Harness pieces go stale when models become better

A principle that appears in several sources is that each part of a harness encodes an assumption about something the model cannot do on its own. The context resets above assumed a model that rushed near the end of its context, and they were dropped when a newer model no longer did. Cursor's post on improving its harness describes removing early guardrails, such as forcing a lint check after every edit, once models stopped needing them. The practical rule is to re-test these assumptions whenever the model changes and to remove what is no longer doing useful work, because every extra component costs tokens, time and complexity. 

## How much the harness matters

The evidence here is mixed, and it is worth keeping both sides in mind. LangChain improved its coding agent from 52.8 to 66.5 percent on the Terminal Bench 2.0 benchmark by changing only the harness, mainly the system prompt, the tools and the checks that run around the model's calls. On the other hand, Anthropic's SWE-bench agent scored 22, 33 and 49 percent with three successive models in an identical harness, so the model drove most of that gain. And a 2026 study by Liu and Han, which ran seven models in three different harnesses and repeated each run, found that no harness was best for every model, and that swapping harnesses usually changed results by about as much as simply running the same setup again. The reasonable conclusion is that the harness does matter, but its value depends on the particular model, and any claim that one harness is better should be tested against repeated runs.

## Key vocabulary

- **Harness**: all the software around the model that turns it into an agent. In narrower usage, only the loop that calls the model and routes its tool calls.
- **Inner harness**: the part the agent's makers build and ship, such as the system prompt, the built-in tools and the loop.
- **Outer harness**: the part you add for your own project, such as instruction files, skills, hooks and checks.
- **Permissions**: the harness's rules about which actions need the user's approval and which are not allowed.
- **Sandbox**: an isolated environment where an agent's code runs without being able to damage anything else.
- **Session**: in Anthropic's Managed Agents, the permanent, append-only log of everything that happened in a run.
- **Initializer agent**: an agent that runs once at the start of a long project to set up the progress file, the feature list and the repository.
- **Compaction**: summarizing a long conversation and continuing with the summary in place of the full history.
- **Reset**: starting a fresh agent with an empty context, which picks up from a structured handoff note.
- **Guides**: parts of the harness that steer the agent before it acts, such as CLAUDE.md, written conventions and skills.
- **Sensors**: parts of the harness that check the agent's work after it acts, such as tests, linters and review by another model.
- **Computational and inferential checks**: checks run by ordinary code, which are deterministic, fast and cheap, versus checks done by a model, which can judge meaning but are slower and less reliable.

## Sources

- Barbaste et al., [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents](https://arxiv.org/abs/2609.00006) (Jul 2026)
- Birgitta Böckeler, [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) (Apr 2026)
- Vivek Trivedy, [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (Mar 2026)
- Anthropic, [Scaling Managed Agents](https://www.anthropic.com/research/managed-agents) (Apr 2026)
- Anthropic, [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) (Nov 2025)
- Anthropic, [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps) (Mar 2026)
- Anthropic, [Raising the bar on SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) (Jan 2025)
- Cursor, [Continually improving our agent harness](https://cursor.com/blog/continually-improving-agent-harness) (Apr 2026)
- Vivek Trivedy, [Improving Deep Agents with Harness Engineering](https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering) (Feb 2026)
- Liu and Han, [What Does a Harness Buy? Tokens, Mostly](https://arxiv.org/abs/2610.04433) (Oct 2026)

Next: [7. Context engineering](07-context-engineering.md)
