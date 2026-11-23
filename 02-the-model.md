---
title: "2. LLMs"
nav_order: 3
---

# 2. LLMs

## Next-token prediction

An LLM predicts one **token** at a time (a short piece of text, roughly 3 to 4 English characters), appends it to the text so far, and predicts the next token until it outputs a stop token. Plain prose, code, and structured requests to run a tool are all generated in this exact same way.

## Training stages that matter for agents

- **Pretraining:** next-token prediction over huge text datasets; this gives the model language, facts, and general reasoning patterns.
- **Post-training:** teaches the model to follow instructions and hold a conversation using **RLHF** (reinforcement learning from human feedback, rewarding replies people prefer) and **RLVR** (reinforcement learning from verifiable rewards, rewarding answers that can be automatically checked, such as code passing tests or exact math answers). RLVR drove much of the recent jump in step-by-step reasoning and long tasks ([Karpathy](https://karpathy.bearblog.dev/year-in-review-2025/)).
- **Tool-use training:** supervised fine-tuning on recorded tool-use examples followed by RL inside simulated environments where the model must call tools to finish tasks ([Lambert](https://rlhfbook.com/teach/course/lec11-chap13-tools/)). Because a model is often trained inside one specific harness, it can perform noticeably better in that harness than in an unfamiliar one. 
	- **IMPORTANT Consequence:** an agent benchmark score measures the model and its harness together, not the model alone.

Once training finishes, the model's weights do not change while you use it. Anything the model appears to "learn" during a session lives only in its input text, never in its weights.

## LLMs are stateless: 
> Stateless: the model keeps nothing from one call to the next. Every call starts fresh, so the model has only its training and the text sent in that call to work with.

Using an LLM means sending it input text and getting output text back (one **call**). When you send a 10-message conversation plus one new message, the model reads all 11 messages from scratch, writes a reply, and forgets everything again. If an agent read a file ten steps ago and that file is no longer in the input, the model has no idea what it said.

Context management ([page 3](03-context.md)), harnesses ([page 6](06-the-harness.md)), and memory ([page 8](08-memory.md)) all exist to work around this single limit.

## Strengths and Weaknesses 

LLMs are strong at summarizing, writing and fixing code, reasoning over provided data, and choosing which tool to use next. Each of their hard limits maps directly to a job the harness does instead:

| What the model cannot do                                              | How the harness handles it                                                 |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Run code or take actions                                              | Runs tools and commands on the model's behalf                              |
| See anything outside its input text                                   | Gathers and loads relevant information before each call                    |
| Remember earlier calls                                                | Keeps the conversation history and saves long-term notes outside the model |
| Know events after its **knowledge cutoff** (when training data ended) | Supplies up-to-date facts via search, files, or external tools             |

## Extended thinking
Many current models write out a stretch of step-by-step reasoning (**extended thinking**) before giving their final answer. This is still ordinary generated text, trained via RL to act as scratch paper before the model commits to an answer or tool call. Allowing more thinking tokens (often controlled by an **effort level** setting) gives the model more compute at test time and usually improves accuracy on hard problems.

## Sources

- Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (Mar 2023)
- Andrej Karpathy, [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) (Dec 2025)
- Nathan Lambert, [Lecture 11: Basics of LLM Tool Use](https://rlhfbook.com/teach/course/lec11-chap13-tools/)

Next: [3. Context and the context window](03-context.md)
