---
title: "2. The model"
nav_order: 3
---

# 2. The model

## What a language model does

A large language model (LLM) is a neural network trained on a very large amount of text to do one thing: given some text, predict what comes next. It works on tokens rather than whole words. A token is a short piece of text, often a whole common word or part of a longer one, and in English a token averages roughly three to four characters. When the model writes a reply, it predicts one token, adds it to the end of the text, and then predicts the next token from the longer text. It repeats this until it produces a token that means stop. Everything a model writes, whether an essay, a block of code or a request to run a tool, is produced this way.

## Weights and training

The model's behaviour is set by its weights, which are the billions of numbers inside the network that were adjusted during training. Training happens in stages. In pretraining, the model learns to predict the next token across a huge collection of text, and this is where it picks up language, facts and general patterns of reasoning. In post-training, it is trained further to follow instructions, hold a conversation and behave helpfully. One common method is reinforcement learning from human feedback (RLHF), in which the model is rewarded for responses that people prefer. Another is reinforcement learning from verifiable rewards (RLVR), in which the model is rewarded for answers that can be checked as correct, such as code that passes its tests or a math problem solved correctly. Andrej Karpathy's review of 2025 describes RLVR as the major development of that year, and it is a large part of why recent models reason step by step and handle long tasks well.

Modern models are also trained specifically to use tools. Nathan Lambert's lecture on tool use explains that models are first trained on recorded examples of tool use and then trained with reinforcement learning in simulated environments, where they must call tools to finish tasks. Because a model is often trained inside a particular harness, it can perform better in that harness than in an unfamiliar one. This is one reason why a benchmark score describes a model and its harness together rather than the model alone.

Once training is finished, the weights do not change while the model is in use. Anything the model appears to learn during a conversation is not stored in its weights.

## One call to the model

Using a model means sending it input text and receiving output text. One such exchange is called a call, or an inference call. The most important fact about a call, and the one that explains most of the rest of this primer, is that the model keeps nothing between calls. In other words, it is stateless. If you send it a conversation, it reads the whole conversation from the beginning, writes its reply, and then retains nothing. When you next send it the same conversation plus one new message, it reads all of it again from scratch.

This means that whatever the model knows during a task must be present in the input of each call. If an agent read a file ten steps ago and that file's contents are no longer in the input, the model has no way of knowing what the file said. The context (page 3), the harness (page 6) and memory (page 8) all exist because of this one property.

## What the model can and cannot do

A model is good at reading and writing text, and that covers a lot: explaining, summarizing, writing and fixing code, reasoning through a problem, and deciding which tool would help next. What it cannot do is just as important. It cannot execute anything, so when an agent "runs a command", the model has only written text asking for the command to be run. It cannot see anything that is not in its input. It does not remember earlier calls. And it knows nothing about events after its training data was collected, a date called its knowledge cutoff, unless that information is placed in its input. Each of these limits is handled by some part of the harness, which runs commands on the model's behalf, gathers the information it needs, keeps records between calls and supplies up-to-date facts.

## Thinking

Many current models can write out a stretch of reasoning before they give their answer, a feature usually called extended thinking or reasoning. This reasoning is also just generated text, but the model has been trained to use it to work through a problem before committing to a reply. Spending more tokens on thinking generally improves results on hard problems, which is why harnesses often let you set an effort level that controls how much the model thinks.

## Key vocabulary

- **Large language model (LLM)**: a neural network trained on large amounts of text to predict the next token.
- **Token**: the unit of text a model reads and writes, roughly three to four characters of English.
- **Weights**: the learned numbers inside the model, fixed once training ends.
- **Pretraining**: the first stage of training, in which the model learns to predict the next token across a huge collection of text.
- **Post-training**: later training that teaches the model to follow instructions, hold a conversation and use tools.
- **RLHF**: reinforcement learning from human feedback, which rewards responses that people prefer.
- **RLVR**: reinforcement learning from verifiable rewards, which rewards answers that can be checked as correct.
- **Inference call**: one exchange in which input text is sent to the model and output text comes back.
- **Stateless**: keeping nothing between calls, which is true of the model itself.
- **Knowledge cutoff**: the date after which the model's training data contains nothing.
- **Extended thinking**: reasoning text the model writes before its answer, which improves results on hard problems.

## Sources

- Lilian Weng, [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) (Mar 2023)
- Andrej Karpathy, [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) (Dec 2025)
- Nathan Lambert, [Lecture 11: Basics of LLM Tool Use](https://rlhfbook.com/teach/course/lec11-chap13-tools/)

Next: [3. Context and the context window](03-context.md)
