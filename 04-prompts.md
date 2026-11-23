---
title: "4. Prompts"
nav_order: 5
---

# 4. Prompts

## Prompt engineering and in-context learning

What works in a **prompt** depends heavily on the specific model, so **prompt engineering** means testing prompts rather than guessing ([Weng](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)).

> **Prompt:** the text you give a model to steer its output.

> **Prompt engineering:** writing prompts that reliably produce the behavior you want, without changing the model's weights.

Prompting works because of **in-context learning (ICL)**.

> **In-context learning (ICL):** a model picking up a new task solely from instructions or examples in its input, with its weights unchanged.

ICL comes in two main forms:

| **Zero-shot** | **Few-shot** |
|---|---|
| Describes the task with no examples. | Includes a handful of worked input-output examples. Often more accurate, but sensitive to which examples you pick, how you format them, and what order they appear in ([Weng](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)). |

Inside an agent, this learning continues through the whole run: error messages, the existing code style in a repository, and earlier tool outputs all shape the model's next turn, which is also why mistakes or clutter in context degrade later steps.

A widely used prompting technique is **chain-of-thought (CoT)**.

> **Chain-of-thought (CoT):** prompting the model to write out its reasoning step by step before answering.

Newer reasoning models already do this automatically through extended thinking ([page 2](02-the-model.md)), so you rarely need to ask for it explicitly.

## The system prompt

Every agent has a **system prompt**.

> **System prompt:** the standing instructions sent in the `system` role at the start of every call.

While a user message says what to do right now, the system prompt sets general behavior: role, rules, tone, working habits (such as inspecting files before editing, keeping edits small, running tests afterward, and making independent tool calls at the same time), and facts like today's date.

The system prompt has a large effect on behavior. Swapping Codex's and Claude Code's system prompts on the exact same model switched it between methodical plan-first work and faster try-and-fix iteration ([Sriraman & Breunig](https://blog.nilenso.com/blog/2026/02/10/how-system-prompts-define-agent-behaviiour/)). Both solved the tasks, via very different paths. The model sets the upper limit on capability; the system prompt determines how much of that ability gets used and corrects training habits (for example, reminding a model trained to call tools one by one to run independent calls in parallel).

Remember that the system prompt is not the only place instructions come from: project files like `CLAUDE.md` are inserted into conversation messages rather than the `system` role.

## Writing a good system prompt

- **Aim for the right altitude** ([Anthropic](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)): avoid rigid `if/else` rules for every corner case (brittle on unforeseen situations) and avoid vague advice (assumes shared context). Give clear principles and leave room for judgment.
- **Explain why a rule exists:** telling the model the reason behind an instruction helps it apply the rule sensibly rather than blindly ([Anthropic prompting docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
- **Keep it structured and direct:** organize long prompts with headings or XML tags, written as you would brief a capable new colleague.
- **Add rules only for real failures:** start minimal on a strong model and add instructions only when you observe specific problems. Use a few varied examples rather than long lists of edge cases.

## Treat prompts like code

Small wording changes can cause large swings in either direction:

- **+20% jump:** adding three short reminders to GPT-4.1's prompt (keep going until solved, use tools instead of guessing, plan before acting) raised its internal SWE-bench Verified score by nearly 20% ([OpenAI](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)).
- **-3% drop from one line:** adding a single line to Claude Code's system prompt capping text between tool calls at 25 words passed early checks but lowered performance by ~3% on one evaluation ([Anthropic](https://www.anthropic.com/research/april-23-postmortem)). Anthropic reverted it and now tests system prompt changes line by line for each model.

## How the field's name kept widening

The same job has been renamed twice as scope grew ([Breunig](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html)): **prompt engineering** (2023, wording a single prompt) → **context engineering** (2025, deciding everything in the input on every turn) → **harness engineering** (2026, building the full software around the model). Each new term includes the ones before it.

## Sources

- Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (Mar 2023)
- Srihari Sriraman and Drew Breunig, [How System Prompts Define Agent Behavior](https://blog.nilenso.com/blog/2026/02/10/how-system-prompts-define-agent-behaviiour/) (Feb 2026)
- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (docs)
- OpenAI, [GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) (Apr 2025)
- Anthropic, [An update on Claude Code quality reports](https://www.anthropic.com/research/april-23-postmortem) (Apr 2026)
- Drew Breunig, [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) (Oct 2026)

Next: [5. Tools](05-tools.md)
