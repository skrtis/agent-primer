---
title: "4. Prompts"
nav_order: 5
---

# 4. Prompts

## Prompts and prompt engineering

A prompt is the text you give a model to steer what it writes. Prompt engineering is the practice of writing prompts that reliably produce the behaviour you want, without changing the model's weights. Lilian Weng's 2023 post on the subject stresses that it is an empirical craft. What works depends heavily on the model, and the only reliable way to know whether a prompt is good is to test it.

## In-context learning

One of the most surprising properties of large language models is that they can pick up a new task from their input alone. If you describe a task, or show a few examples of it, the model will usually do the task correctly even though it was never trained on that task specifically and its weights do not change. This is called in-context learning, because the learning happens inside the context of a single call rather than during training.

There are two basic ways to use it. A zero-shot prompt describes the task and gives no examples. A few-shot prompt adds a handful of examples, each showing an input and the desired output, so that the model can follow the pattern. Few-shot prompts often work better, but Weng notes that they are sensitive to details. Which examples you choose, how you format them and even the order they appear in can change the results considerably.

In-context learning is not only something you set up on purpose. In an agent it happens throughout the run. When a tool returns an error and the model adjusts its next request, or when the model notices how the code in a repository is written and follows the same style, it is learning from its context. This is also why the contents of the context matter so much, since the model learns from whatever is there, including mistakes and irrelevant material.

## Chain of thought

Chain-of-thought prompting asks the model to write out its reasoning step by step before it gives a final answer. For problems that need several steps of reasoning, this improves accuracy, because each step is written down and the model can build on it instead of jumping straight to an answer. Current reasoning models do this on their own through extended thinking (page 2), so you rarely need to ask for it, but the idea explains why thinking helps.

## The system prompt

The system prompt is a block of standing instructions that the developer or the harness sends at the start of every call, in the system role. A user message says what to do right now, while the system prompt sets how the model should behave throughout: its role, the rules it must follow, how it should approach tasks, what tone to use, how to use its tools, and facts it needs, such as the current date. In a coding agent, the system prompt typically describes a way of working. It might tell the model to gather information before changing code, to keep changes small, to run the tests after editing, and to make independent tool calls in parallel.

The system prompt has a large effect on how an agent behaves. In "How System Prompts Define Agent Behavior", Srihari Sriraman and Drew Breunig compared the system prompts of several coding agents and then swapped them between agents. When they ran the same model with Codex's system prompt in place of Claude Code's, it worked in a methodical, plan-first way, while with Claude Code's own prompt it worked in a quicker try-and-fix style. Both versions solved the test tasks, but by different routes. Their summary is that the model sets the ceiling on what an agent can do, and the system prompt largely decides how much of that ability the agent actually uses. They also found that much of a production system prompt exists to correct a model's habits. **One example is reminding the model to call tools in parallel, because its training pushed it toward calling them one at a time.**

It is worth being precise about where the system prompt sits. It is one part of the context, not the whole of it, and not every instruction the model receives comes from it. As page 3 mentioned, the CLAUDE.md file in Claude Code is not part of the system prompt; the harness inserts it into the conversation as a separate message.

## What makes a good system prompt

Anthropic's context engineering post describes the goal as writing at the right altitude. At one extreme, a prompt can try to spell out exact behaviour for every situation, like a long list of if-then rules. Such a prompt is brittle, because it breaks on cases the author did not foresee. At the other extreme, a prompt can be so general that it assumes the model already shares the author's understanding of the task. **A good system prompt sits between the two, specific enough to guide the model and general enough to let it use judgment.**

Anthropic's prompting documentation adds several practical rules. Write clearly and directly, as you would for a capable new colleague who knows nothing about your project. **Explain the reason behind an instruction rather than only stating the instruction, because a model that understands why a rule exists applies it more sensibly. Organize long prompts into sections with headings or XML tags.** **Start with a minimal prompt on a strong model and add instructions only when you see a specific failure, instead of trying to anticipate every problem in advance. And when you use examples, choose a few varied ones that show the intended behaviour, rather than a long list of edge cases.**

Small changes to a system prompt can have large effects in either direction. OpenAI's GPT-4.1 prompting guide reports that adding three short reminders to an agent's prompt raised its internal SWE-bench Verified score by close to 20 percent. The reminders told the model to keep going until the task was solved, to use its tools rather than guess, and to plan before each action. In the other direction, Anthropic published a postmortem in April 2026 explaining that one line added to Claude Code's system prompt to make it less wordy, which limited the text between tool calls to 25 words, lowered performance by about 3 percent on one of its evaluations, even though earlier tests had shown no problem. Anthropic reverted the line, and it now runs a broad set of evaluations on every system prompt change, for each model, and tests the effect of each line separately. The lesson shared by both examples is that a system prompt should be treated like code, with every change tested before it ships.

## From prompt engineering to context engineering

Drew Breunig points out that the same job has been renamed twice as the field has grown. In 2023 people spoke of prompt engineering, meaning the wording of a single prompt. By 2025 the focus had widened to context engineering, meaning everything placed in the context on every call of an agent's loop. By 2026 it had widened again to harness engineering, meaning the software that assembles that context and runs the loop. Each new name includes the one before it, and the next three pages follow the same widening.

## Key vocabulary

- **Prompt**: the text you give a model to steer what it writes.
- **Prompt engineering**: writing prompts that reliably produce the behaviour you want, without changing the model's weights.
- **In-context learning**: a model picking up a task from instructions or examples in its input, with no change to its weights.
- **Zero-shot prompt**: a prompt that describes the task and gives no examples.
- **Few-shot prompt**: a prompt that includes a handful of worked examples of the task.
- **Chain of thought**: having the model write out its reasoning step by step before it answers.
- **System prompt**: standing instructions sent at the start of every call that set how the model should behave throughout.
- **Right altitude**: Anthropic's phrase for a system prompt that is specific enough to guide the model but general enough to let it use judgment.
- **Context engineering**: deciding what goes into the context on every call of an agent's loop (page 7).
- **Harness engineering**: designing the software that assembles the context and runs the loop (page 6).

## Sources

- Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (Mar 2023)
- Srihari Sriraman and Drew Breunig, [How System Prompts Define Agent Behavior](https://blog.nilenso.com/blog/2026/02/10/how-system-prompts-define-agent-behaviiour/) (Feb 2026)
- Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (docs)
- OpenAI, [GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) (Apr 2025)
- Anthropic, [An update on Claude Code quality reports](https://www.anthropic.com/research/april-23-postmortem) (Apr 2026)
- Drew Breunig, [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) (Oct 2026)

Next: [5. Tools](05-tools.md)
