---
title: "6. The harness"
nav_order: 7
---

# 6. The harness

## What the harness is

The **harness** is all the software wrapped around a language model to turn it into an agent: "if you're not the model, you're the harness" ([Trivedy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)). A source-code study of 11 production coding agents (including Claude Code, Codex CLI, and Gemini CLI) groups its jobs into six areas: running the loop, providing tools, managing context, enforcing safety checks, coordinating work, and supporting extensions like MCP servers, skills, and hooks ([Barbaste et al.](https://arxiv.org/abs/2609.00006)).

People use "harness" at three different scales:

| Usage | What it covers | Source |
|---|---|---|
| **Broad harness** | Everything outside the model itself | [Trivedy](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness); [Barbaste et al.](https://arxiv.org/abs/2609.00006) |
| **Narrow harness** | Just the loop that reads history, builds context, calls the model, and runs tool requests | [Anthropic Managed Agents](https://www.anthropic.com/research/managed-agents) |
| **Inner vs. outer harness** | **Inner:** what the agent's makers ship (loop, system prompt, built-in tools). **Outer:** what you add for your own project (`CLAUDE.md`, skills, hooks, checks) | [Böckeler](https://martinfowler.com/articles/harness-engineering.html) |

## The agent loop in full

Expanding the loop from [page 1](01-what-an-agent-is.md) to what real harnesses do:

1. Build the context: system prompt, tool definitions, project instructions (e.g., `CLAUDE.md`), conversation history, and user task.
2. Call the model.
3. If the reply asks for no tools, show it to the user and stop.
4. For each requested tool, check **permissions** (asking the user or blocking risky actions like deleting files) and run it inside a **sandbox** (an isolated environment where mistakes cannot harm the rest of the system) where appropriate.
5. Capture the output or error, trim or save huge outputs to a file, and add the result to the conversation.
6. Check context size (trimming or summarizing older turns if near the limit) and log what happened.
7. Go back to step 1.

Real production loops are surprisingly simple. Anthropic's SWE-bench agent used a short prompt, one tool to run shell commands, and one tool to edit files inside a plain loop ([Anthropic](https://www.anthropic.com/engineering/swe-bench-sonnet)). None of the 11 production harnesses studied by Barbaste et al. were built on a general-purpose agent framework; all used plain hand-written code for their loops.

## Separating session, harness, and sandbox

Anthropic's [Managed Agents design](https://www.anthropic.com/research/managed-agents) splits a running agent into three independent pieces so any one can crash or be replaced without losing the others:

- **Session:** a permanent record of every event (only adding new entries to the end), stored outside the model's context.
- **Harness (narrow):** the loop that reads the session, builds the context, calls the model, and routes tool requests.
- **Sandbox:** the isolated space where code actually runs and files are edited.

Separating these means a crashed sandbox does not wipe out the session history, a summarized context can be rebuilt from the full log, and passwords or API keys stay outside the sandbox where model-written code cannot reach them.

## Long-running agents

Tasks lasting hours or days outgrow a single context window. Two patterns from Anthropic's long-running agent studies address this:

- **Initializer + step-by-step worker sessions** ([Anthropic](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)): a one-time **initializer agent** sets up a startup script, a progress file, a checklist of every feature (all marked failing), and an initial version-control commit. Each later session reads the progress file and commit history, builds one feature, tests it, marks it passing, commits, and updates the progress file. The feature list stops the agent from quitting early, and working one feature at a time keeps changes small and easy to check.
- **Separate builder and evaluator + resets vs. compaction** ([Anthropic](https://www.anthropic.com/research/harness-design-long-running-apps)): models tend to grade their own work too generously, so splitting planning, building, and testing across separate agents catches mistakes self-review misses. When context fills, **compaction** summarizes the conversation in place, while a **reset** starts a fresh agent with an empty context and a structured handoff note. Resets helped a model that rushed near context limits, then became unnecessary on the next model generation.

## Guides and sensors (the outer harness)

For the project-specific outer harness you build yourself, [Böckeler](https://martinfowler.com/articles/harness-engineering.html) divides pieces by when they act:

- **Guides** act *before* the agent moves, steering it (`CLAUDE.md`, written conventions, skills).
- **Sensors** act *after* the agent acts, checking the result so it can fix mistakes (tests, linters, type checkers, review by another model).

Guides without sensors go unchecked; sensors without guides let the agent repeat the same mistake every run. Among sensors, prefer **computational checks** (unit tests, linters, type checkers: exact, fast, cheap) over **inferential checks** (review by another model: can judge meaning, but slower, costlier, and less consistent).

## Harnesses go stale as models improve

Every harness trick assumes there is something today's model cannot do on its own (such as resets for context-rushing, or Cursor's early rule forcing a lint check after every edit). When newer models stop needing a guardrail, keeping it wastes tokens, time, and complexity. Re-test your harness assumptions whenever the model upgrades and delete what is no longer helping ([Cursor](https://cursor.com/blog/continually-improving-agent-harness)).

## How much does the harness actually matter?

The evidence cuts both ways:

- **Big harness gain:** LangChain raised its coding agent from **52.8% to 66.5%** on Terminal Bench 2.0 by changing only the harness (system prompt, tools, and surrounding checks) ([Trivedy](https://www.vtrivedy.com/posts/improving-deep-agents-with-harness-engineering)).
- **Big model gain:** Anthropic's SWE-bench agent jumped **22% → 33% → 49%** across three successive models inside the exact same harness ([Anthropic](https://www.anthropic.com/engineering/swe-bench-sonnet)).
- **High run-to-run noise:** testing 7 models across 3 harnesses with repeated runs found no single best harness across all models, and swapping harnesses often changed scores by about as much as simply rerunning the same setup ([Liu & Han](https://arxiv.org/abs/2610.04433)).

Bottom line: the harness matters, its benefit depends on the model, and any claimed harness improvement should be tested against repeated runs.

## The Claude Agent SDK

The **Claude Agent SDK** is Claude Code packaged as a library for Python (`claude-agent-sdk`) and TypeScript. It gives your own code the same agent loop, built-in tools, and context management that run Claude Code ([Agent SDK docs](https://code.claude.com/docs/en/agent-sdk/overview)). It sits between two other ways of using Claude:

- **Messages API:** one request, one response. You write the loop from [page 1](01-what-an-agent-is.md) yourself and define every tool, which gives you exact control over what each request contains.
- **Claude Code:** the finished coding agent, used interactively.

With the SDK you start the loop with `query()` and choose which parts of the harness are switched on:

- **System prompt:** your own text replaces the whole prompt; a preset keeps Claude Code's prompt and adds yours.
- **Built-in tools:** `tools` sets which ones are available (reading and editing files, shell commands, search, web).
- **Custom tools:** Python functions exposed through an MCP server inside your script ([page 5](05-tools.md)). The model sees them as `mcp__<server>__<tool>`, and external MCP servers attach the same way.
- **Settings from disk:** `setting_sources=[]` loads no `CLAUDE.md` or local settings files, which keeps experiments controlled.
- **Subagents, skills, hooks, and permissions:** the same features Claude Code has ([page 9](09-multi-agent-systems.md)).
- **Long runs:** automatic compaction, turn and spending limits (`max_turns`, `max_budget_usd`), and resumable sessions saved as log files (`JSONL`).

A minimal agent with one custom tool:

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions, tool, create_sdk_mcp_server

@tool("lookup", "Look up a compound by ID", {"id": str})
async def lookup(args):
    return {"content": [{"type": "text", "text": compounds[args["id"]]}]}

options = ClaudeAgentOptions(
    system_prompt="You are a medicinal chemist.",
    setting_sources=[],                  # load nothing from disk
    tools=["Read", "Grep"],              # the only built-in tools available
    mcp_servers={"db": create_sdk_mcp_server("db", tools=[lookup])},
    allowed_tools=["mcp__db__lookup"],   # run this tool without asking
    max_turns=10,
)

async def main():
    async for message in query(prompt="...", options=options):
        print(message)                   # save every message to keep a full trace

asyncio.run(main())
```

The SDK also adds things you did not write yourself. Environment details (working directory, operating system) and any loaded `CLAUDE.md` arrive in the conversation rather than the system prompt, automatic compaction changes what the model sees partway through a run, and only a summary of the model's reasoning is returned ([Agent SDK docs](https://code.claude.com/docs/en/agent-sdk/overview)).

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
- Anthropic, [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) (read Nov 2026)
- Anthropic, [Agent SDK reference: Python](https://code.claude.com/docs/en/agent-sdk/python) (read Nov 2026)
- Anthropic, [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp) (read Nov 2026)

Next: [7. Context engineering](07-context-engineering.md)
