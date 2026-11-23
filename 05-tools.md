---
title: "5. Tools"
nav_order: 6
---

# 5. Tools

## How tools work

A **tool** is an external action (running a command, reading or editing a file, searching the web, querying a database) that the harness runs when the model asks for it. The model never runs tools itself. It only writes a structured text request, and the harness runs the actual code and sends the output back.

On every call, the harness sends a **tool definition** for each available tool containing three parts:

1. **Name** (e.g., `read_file`)
2. **Description** (plain text explaining what the tool does and when to use it)
3. **Input format** (usually written in **JSON Schema**, listing each input's name, type, and whether it is required)

One tool exchange (often called **function calling**) looks like this:

```json
// 1. Model outputs a structured tool request and stops writing
{ "tool": "read_file", "arguments": { "path": "src/train.py" } }

// 2. Harness checks permissions, runs the tool, trims huge outputs,
//    and sends the result back to the model in the next call
{ "tool_result": "def train(cfg):\n    ..." }
```

Because tool names and descriptions sit inside the context and guide which tool the model picks, they are effectively prompt text. For its SWE-bench coding agent, Anthropic spent more time refining tool descriptions than the system prompt itself ([Anthropic](https://www.anthropic.com/research/building-effective-agents)).

## Designing effective tools

The SWE-agent paper framed this as the **agent-computer interface (ACI)**: an LLM is a new kind of computer user, and changing only its tool interface changes performance on the exact same model ([Yang et al.](https://arxiv.org/abs/2405.15793)). Practical rules ([Anthropic](https://www.anthropic.com/research/writing-tools-for-agents)):

- **Use fewer, more complete tools:** prefer a small set of tools that each do a complete, meaningful job instead of dozens of tiny tools mirroring every function of a service. Extra definitions waste context and confuse the model. Good test: if a person cannot quickly tell which tool to pick, neither can the model.
- **Make names and inputs crystal clear:** group names by service, write descriptions as if for a new colleague, and use specific input names (`user_id`, not `user`).
- **Return clean, bounded outputs:** return readable names rather than cryptic internal ID numbers, and cap output size (via pagination or truncation) so one call cannot flood the context window.
- **Write helpful error messages:** the model reads errors and tries again, so explain what went wrong and how to fix the request.

## MCP (Model Context Protocol)

Without a common standard, every agent app has to write custom connector code for every external service (calendars, GitHub, databases). **MCP** is an open standard that avoids that duplicate work:

- **MCP server:** wraps a service once, exposing **tools** (actions), **resources** (readable data), and **prompts** (reusable templates).
- **MCP host and client:** the agent app (such as Claude Code) is the host, running one client connection for each server it talks to.

Any MCP-compatible app can connect to any MCP server. The [July 2026 spec revision](https://blog.modelcontextprotocol.io/posts/2026-07-28/) made MCP requests self-contained (like normal web requests, with no saved session state on the server), making servers easier to run at scale.

**The tradeoff is context cost.** Every tool from every connected server adds its definition to the context on every turn; one large server can use tens of thousands of tokens before the agent even starts working.

## Code execution and skills

Two newer approaches avoid crowding the context with tool definitions and huge intermediate outputs:

- **Code execution (code mode):** instead of calling tools one by one and passing every raw output through the model's context, the model writes a short script inside an isolated sandbox that calls several tools, filters the data, and prints only what matters. In Anthropic's [MCP code-execution study](https://www.anthropic.com/research/code-execution-with-mcp), this cut a task from ~150,000 tokens to ~2,000. Earlier CodeAct experiments likewise found that writing Python code as actions beat fixed-format tool calls ([Wang et al.](https://arxiv.org/abs/2402.01030)). [Schmid](https://www.philschmid.de/code-mode) argues agents may eventually need only one real tool (a sandbox that runs code), with all other tools exposed as functions inside it. The tradeoff is security: running model-written code safely requires tight isolation and limits.
- **Skills and progressive disclosure:** a **skill** is a folder containing a `SKILL.md` instruction file plus any scripts or reference files it needs. At the start of a session, the harness loads only each skill's name and one-line description; the model reads the full file only when a task matches ([Willison](https://simonwillison.net/2025/Oct/16/claude-skills/)). Showing a short summary upfront and loading details only on demand (**progressive disclosure**) keeps context small.

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
