---
title: "8. Memory"
nav_order: 9
---

# 8. Memory

## Why agents need memory

Two facts from earlier pages create the need for memory. The model keeps nothing between calls (page 2), and the context, which is the only thing it sees, is limited in size and is thrown away when a session ends (page 3). An agent that must pick up a project tomorrow, remember a user's preferences, or avoid repeating a mistake it made last week needs a way to store information outside the model and bring it back later. That is what memory means for agents.

## Definitions differ

Sources draw the boundaries of memory in different places, so it helps to see the main versions side by side. Anthropic's "The components of agent memory" uses a narrow definition. In it, memory is knowledge an agent gains from experience, such as from working with a user or on a task, that is kept across sessions and saved as context the agent can read later. Under this definition three things are not memory: what is in the model's weights, what the model picks up within one conversation through in-context learning, and the summaries that compaction produces within a session. The survey "Memory in the Age of AI Agents" (Hu and colleagues) uses a much broader definition, which counts all of these as forms of memory. Older sources use a simpler two-way split. Weng's 2023 post calls the context short-term memory, and calls anything stored outside the model long-term memory.

These are differences of scope rather than real disagreements. The narrow definition is the most useful one when you are building an agent, because it picks out exactly the part you have to design yourself.

## Where memory lives

A clear way to understand memory is to ask where a piece of information physically sits, and how it gets back to the model.

Information can live in the model's weights, where it was put during training. This is how the model knows facts and skills, and it needs no retrieval step, but it cannot be updated while the agent is running.

Information can live in the context. This is the agent's working memory for the current task. It is immediately available to the model, but it is limited in size and gone at the end of the session.

Information can live in files. This is the most common form of long-term memory in coding agents. Notes, project instruction files, progress logs, saved transcripts and version-control history are all files that the agent can read and write with its ordinary tools.

Information can live in a database or search index, such as a vector store (described in the RAG section below), from which relevant pieces are retrieved by searching.

The point that ties these together is that stored information only helps when it is read back into the context. A note in a file the agent never opens has no effect at all. There are two ways to bring it back. The harness can inject a small amount automatically at the start of every session, as Claude Code does with CLAUDE.md and with the first part of its memory index file. Or the agent can look things up when it needs them, using tools such as search, just as it would for any other information.

## Kinds of memory

CoALA, borrowing from psychology, sorts memory by what it contains. Episodic memory is a record of specific past events, such as the transcript of an earlier session or the steps taken on a previous task. Semantic memory holds facts, such as a user's preferences or the structure of a project. Procedural memory holds knowledge of how to do things; in an agent it lives partly in the model's weights and partly in code, instructions and skills. Working memory, in CoALA's terms, is the information that is active in the current step. Anthropic's post describes the layers of a practical memory system in similar terms. Raw transcripts sit at the bottom, notes written during sessions sit above them, organized representations such as a wiki of linked pages sit above those, and at the top is a small amount of context that the harness loads at the start of every session.

## Writing, organizing and reading memory

A memory system has to do three things. It has to decide what to write down, keep what is written in good shape, and find the right part when it is needed. Each step can go wrong.

Writing is a judgment about what will matter later. Anthropic's post describes an agent playing a video game that saved notes on everything it saw and did worse than an agent that saved only a few notes about things it could not see on screen. The post also reports that telling the model what its memory is for works better than giving it rigid rules about what to save.

Keeping memory in good shape usually involves consolidation, also called reflection, in which raw records are periodically turned into shorter summaries or general lessons. The Generative Agents paper (Park and colleagues) used reflection in this way, and **Anthropic describes an offline pass it calls dreaming, in which an agent reviews its notes against the original transcripts, corrects them and reorganizes them.** Consolidation carries a real risk, however. A 2026 paper by Zhang and colleagues found that when a model repeatedly rewrites its own memories, their usefulness first rises and then falls, sometimes below having no memory at all, because **each rewrite can lose or distort details.** Their recommendation is to keep the raw records as the primary evidence and to consolidate only with checks.

Reading is the problem of retrieval, which leads to RAG.

## RAG

Retrieval-augmented generation (RAG), introduced by Lewis and colleagues in 2020, means retrieving relevant passages from a collection of documents and placing them in the context before the model answers. This lets the model answer from current, specific sources rather than only from what it learned in training.

A standard RAG system works in a few steps, which Anthropic's "Introducing Contextual Retrieval" explains well. The documents are first split into chunks, which are short passages that can be retrieved individually. Each chunk is converted into an embedding, a list of numbers produced by a model in such a way that passages with similar meanings get similar numbers. The embeddings are stored in a vector store, which is a database built to find the stored embeddings closest to a given one. When a question arrives, it is converted into an embedding too, and the chunks closest to it are retrieved. Embeddings capture meaning but can miss exact terms such as an ID number or an error code, so systems usually also run BM25, a long-established keyword-matching method, and combine the two sets of results. A reranking model then reads the best candidates more carefully and keeps the most relevant few.

Anthropic's improvement was to have a model write a sentence or two of context for each chunk before indexing it, since a chunk such as "revenue grew 3 percent" means little without knowing which company and which period it refers to. This cut retrieval failures roughly in half, and by about two thirds when combined with reranking. The same post notes that if the whole collection is smaller than about 200,000 tokens, it is simpler to put all of it in the context and skip retrieval entirely.

RAG and memory share their retrieval machinery but differ in what they retrieve from. In RAG the collection is usually fixed and written by someone else, like a company's documentation. Memory is written by the agent itself, from its own experience, and it keeps changing.

## Simple approaches often win

A recurring finding is that plain files and ordinary search tools work surprisingly well. Letta, a company that makes memory software, reported that an agent with nothing more than file-reading and search tools over a conversation history scored higher on a memory benchmark than a specialized memory product, although this was a single benchmark run by an interested party. The study of eleven production coding agents (page 6) found that none of them used embeddings to search code; they all used plain text search. And the MemoryArena benchmark (He and colleagues) found that agents that score well on tests of simply recalling facts often do poorly when they must actually use stored experience to make later decisions. This is a reminder that memory should be judged by whether it improves what the agent does, not by whether it can repeat what it saved.

## Key vocabulary

- **Memory**: information an agent stores outside the model and its current context and reads back later. In the narrow sense, knowledge from experience that is kept across sessions.
- **Working memory**: the information active in the current step, held in the context.
- **Long-term memory**: information kept outside the context that survives across sessions.
- **Episodic memory**: records of specific past events, such as earlier transcripts.
- **Semantic memory**: stored facts, such as a user's preferences or a project's structure.
- **Procedural memory**: knowledge of how to do things, held in the model's weights, in code, in instructions and in skills.
- **Consolidation (reflection)**: periodically turning raw memory records into shorter summaries or lessons. Useful, but it can distort memory.
- **RAG (retrieval-augmented generation)**: retrieving relevant passages from a document collection and putting them in the context before the model answers.
- **Chunk**: a short passage of a document, the unit that RAG stores and retrieves.
- **Embedding**: a list of numbers that represents a piece of text, made so that texts with similar meanings get similar numbers.
- **Vector store**: a database that finds the stored embeddings closest to a given one.
- **BM25**: a long-established keyword-matching method, used to catch exact terms that embeddings miss.
- **Reranking**: a second model rescoring retrieved candidates and keeping the most relevant.

## Sources

- Anthropic, [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) (Nov 2026)
- Hu et al., [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) (Dec 2025)
- Sumers et al., [CoALA](https://arxiv.org/abs/2309.02427) (TMLR 2024)
- Lilian Weng, [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Jun 2023)
- Park et al., [Generative Agents](https://arxiv.org/abs/2304.03442) (UIST 2023)
- Zhang et al., [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978) (2026)
- Lewis et al., [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (NeurIPS 2020)
- Anthropic, [Introducing Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) (Sep 2024)
- Letta, [Benchmarking AI Agent Memory: Is a Filesystem All You Need?](https://www.letta.com/blog/benchmarking-ai-agent-memory) (Aug 2025)
- He et al., [MemoryArena](https://arxiv.org/abs/2602.16313) (ICML 2026)

Next: [9. Multi-agent systems](09-multi-agent-systems.md)
