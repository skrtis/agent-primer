---
title: "8. Memory"
nav_order: 9
---

# 8. Memory

## Why agents need memory and how people define it

Because a language model remembers nothing between calls and its context disappears when a session ends, an agent that needs to pick up a project tomorrow, remember user preferences, or avoid repeating last week's mistake must save information outside the model and read it back later.

Sources draw the line around **memory** at different widths (a difference in scope, not a real disagreement):

- **Narrow** ([Anthropic](https://www.anthropic.com/research/components-of-agent-memory)): knowledge gained from experience, saved across sessions, and read back into context later. Excludes model weights, within-session learning, and compaction summaries. Most useful when building an agent, because it singles out the part you have to design yourself.
- **Broad** ([Hu et al.](https://arxiv.org/abs/2512.13564)): counts weights, current context, and external storage all as forms of memory.
- **Two-part split** ([Weng](https://lilianweng.github.io/posts/2023-06-23-agent/)): **short-term memory** = the current context; **long-term memory** = anything stored outside the model.

## Where saved information physically lives

| Where it lives | Updates while running? | Survives across sessions? | How the model sees it |
|---|---|---|---|
| **Model weights** | No (fixed after training) | Yes | Always active; no lookup needed |
| **Current context** | Yes (each turn) | No | Already in the model's input |
| **Plain files** (notes, `CLAUDE.md`, logs, git) | Yes | Yes | Loaded at startup or opened with tools |
| **Database / search index** (e.g., vector store) | Yes | Yes | Looked up with search tools |

**Key rule:** stored information has no effect until it is read back into context. Harnesses load it either automatically at the start of a session (like `CLAUDE.md` and the top of Claude Code's memory index) or on demand via search tools.

Practical memory systems usually layer information from raw to distilled ([Anthropic](https://www.anthropic.com/research/components-of-agent-memory)): raw session logs at the bottom → session notes → organized knowledge (like a wiki of linked notes) → a small summary loaded automatically at session start.

## Writing, maintaining, and reading memory

Each step can go wrong:

- **Writing (deciding what to save):** saving everything hurts. In Anthropic's video-game test, an agent that logged everything it saw did worse than one that saved a few notes about things not visible on screen; explaining *what memory is for* worked better than rigid rules about what to save ([Anthropic](https://www.anthropic.com/research/components-of-agent-memory)).
- **Consolidation / reflection (keeping notes tidy):** periodically turning raw records into shorter summaries or general lessons ([Park et al.](https://arxiv.org/abs/2304.03442)), including offline passes like Anthropic's **dreaming**, where an agent checks its notes against raw logs to correct and reorganize them. **Major risk:** repeatedly letting a model rewrite its own memories causes usefulness to rise and then fall (sometimes below having no memory at all) because each rewrite can lose or distort details ([Zhang et al.](https://arxiv.org/abs/2605.12978)). Keep raw logs as the primary record and check consolidations carefully.
- **Reading (finding the right note):** leads directly to RAG.

## RAG (retrieval-augmented generation)

**RAG** looks up relevant passages from a collection of documents and puts them into the context before the model answers ([Lewis et al.](https://arxiv.org/abs/2005.11401)). The standard setup ([Anthropic](https://www.anthropic.com/research/contextual-retrieval)):

1. Split documents into short **chunks**.
2. Search with two methods combined: **embedding** search in a **vector store** (finds passages with similar meaning) plus **BM25** keyword search (catches exact IDs, gene names, or error codes that embeddings miss).
3. Pass the top candidates through a **reranking** model that scores them more carefully and keeps only the best few.

**Contextual Retrieval** ([Anthropic](https://www.anthropic.com/research/contextual-retrieval)) has a model add a 1 to 2 sentence context note to each chunk before indexing (so `"revenue grew 3%"` still names the company and quarter), cutting retrieval failures roughly in half alone and by about two thirds with reranking. If the whole document collection is under ~200,000 tokens, skip RAG completely and just put it in context.

RAG and memory use the same search machinery, but RAG searches a mostly fixed external library (like documentation) while memory searches changing notes written by the agent itself.

## Simple files often beat fancy memory systems

- **Plain files baseline:** Letta reported that an agent with only file-reading and text-search tools over conversation history beat a specialized memory product on a memory benchmark (caveat: a single benchmark run by an interested company) ([Letta](https://www.letta.com/blog/benchmarking-ai-agent-memory)).
- **Production coding agents:** 0 of 11 harnesses audited by Barbaste et al. ([page 6](06-the-harness.md)) used vector embeddings to search code; all used plain text search.
- **Recall is not enough:** **MemoryArena** ([He et al.](https://arxiv.org/abs/2602.16313)) found that agents scoring high on repeating saved facts often fail to actually *use* that stored experience when making later decisions. Judge memory by whether it improves final results, not by fact-recall quizzes.

## Sources

- Anthropic, [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) (Nov 2026)
- Hu et al., [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) (Dec 2025)
- Lilian Weng, [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (Jun 2023)
- Park et al., [Generative Agents](https://arxiv.org/abs/2304.03442) (UIST 2023)
- Zhang et al., [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978) (2026)
- Lewis et al., [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (NeurIPS 2020)
- Anthropic, [Introducing Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) (Sep 2024)
- Letta, [Benchmarking AI Agent Memory: Is a Filesystem All You Need?](https://www.letta.com/blog/benchmarking-ai-agent-memory) (Aug 2025)
- He et al., [MemoryArena](https://arxiv.org/abs/2602.16313) (ICML 2026)

Next: [9. Multi-agent systems](09-multi-agent-systems.md)
