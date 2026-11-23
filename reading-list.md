---
title: "Reading list"
nav_order: 15
---

# Agent reading list

Compiled 2026-11-19. Every link was opened and checked.

## Weekend core (in order)
- Lilian Weng, [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) (2023). The classic split into planning, memory and tool use.
- Barbaste et al., [Harness Engineering: Anatomy, Architecture, and Evolution of Coding Agents](https://arxiv.org/abs/2609.00006) (Jul 2026, preprint). Defines a harness (loop, tools, context management, safety, orchestration, extensions) and maps it across 11 production harnesses from their source code.
- Drew Breunig, [The State of Context Engineering](https://www.dbreunig.com/2026/10/24/the-state-of-context-engineering.html) (Oct 2026). Four ways context fails and the fixes. Pair with Chroma, [Context Rot](https://www.trychroma.com/research/context-rot): 18 models, task held fixed, only input length varied.
- Hu et al., [Memory in the Age of AI Agents](https://arxiv.org/abs/2512.13564) (Dec 2025, preprint). Separates memory from RAG and context; classifies it by form, function and how it changes.
- Nathan Lambert, [Lecture 11: Basics of LLM Tool Use](https://rlhfbook.com/teach/course/lec11-chap13-tools/). Textbook-level: tool use vs function calling vs code execution, MCP roles, RL training for tools.
- Kim et al., [Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296) (Dec 2025). Across 260 setups, multi-agent ranged from +81% on decomposable tasks to -70% on sequential planning.
- Kapoor et al., [AI Agents That Matter](https://arxiv.org/abs/2407.01502) (TMLR 2025), then Zhu et al., [the Agentic Benchmark Checklist](https://arxiv.org/abs/2507.02825) (NeurIPS 2025).
- RSI: Lilian Weng, [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Jul 2026), then Anthropic, [When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement) (Sep 2026), then METR, [Independent Assessment of AI R&D Acceleration at Anthropic](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment) (Nov 2026).

## Anthropic engineering blog (in order)
- [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (Dec 2024). Base vocabulary: augmented LLM, workflows vs agents, five workflow patterns.
- [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (Sep 2025)
- [Writing effective tools for agents](https://www.anthropic.com/research/writing-tools-for-agents) (Sep 2025)
- [Code execution with MCP](https://www.anthropic.com/research/code-execution-with-mcp) (Nov 2025)
- [Scaling Managed Agents](https://www.anthropic.com/research/managed-agents) (Apr 2026). Session (append-only log), harness (the loop that calls the model and routes tool calls), sandbox (where code runs).
- [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) (Nov 2025)
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps) (Mar 2026)
- [The components of agent memory](https://www.anthropic.com/research/components-of-agent-memory) (Nov 2026)
- [Introducing Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) (Sep 2024). RAG primer.
- [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (Jun 2025)
- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents) (Jan 2026)

## LLM as the agent's core
- Lambert's lecture above. A benchmark score measures the model and the harness together.
- Andrej Karpathy, [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) (Dec 2025). Opinion.

## Harness
- Birgitta Böckeler (Thoughtworks), [Harness engineering for coding agent users](https://martinfowler.com/articles/harness-engineering.html) (Apr 2026). Inner harness (vendor) vs outer harness (yours); guides (act before) vs sensors (check after).
- Vivek Trivedy (LangChain), [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (Mar 2026). Source of "agent = model + harness"; each part and why it exists.
- Yang et al., [SWE-agent](https://arxiv.org/abs/2405.15793) (NeurIPS 2024). The agent-computer interface: changing only the interface changes performance.
- Liu et al., [What Does a Harness Buy? Tokens, Mostly](https://arxiv.org/abs/2610.04433) (Oct 2026, preprint). Swapping the harness changed about as many results as rerunning the same one, so harness gains need a rerun baseline.
- Cursor, [Continually improving our agent harness](https://cursor.com/blog/continually-improving-agent-harness) (Apr 2026). How a production harness is measured.

## Tools, MCP, skills
- Schick et al., [Toolformer](https://arxiv.org/abs/2302.04761) (NeurIPS 2023). Where tool use starts.
- Wang et al., [CodeAct](https://arxiv.org/abs/2402.01030) (ICML 2024). Code as the action beats JSON tool calls.
- Hou et al., [MCP: Landscape, Security Threats, and Future Research Directions](https://arxiv.org/abs/2503.23278) (ACM TOSEM). What MCP standardizes, plus 16 threat scenarios.
- [MCP 2026-07-28 specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/). MCP becomes stateless.
- Philipp Schmid (Google DeepMind), [Why Agents Are Soon Only Going to Have 1 Tool](https://www.philschmid.de/code-mode) (Nov 2026). One code-running tool whose scripts call the other tools.
- Simon Willison, [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/) (Oct 2025). Clearest account of progressive disclosure.

## Context
- Liu et al., [Lost in the Middle](https://arxiv.org/abs/2307.03172) (TACL 2024). Where information sits in the context matters.
- Yichao Ji (Manus), [Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) (Jul 2025). Production lessons.
- Kang et al., [ACON: Optimizing Context Compression for Long-horizon LLM Agents](https://arxiv.org/abs/2510.00615) (ICML 2026)
- Cursor, [Improved token efficiency for longer agent runs](https://cursor.com/blog/improved-token-efficiency) (Sep 2026). A/B-tested context changes.

## Memory
- Lewis et al., [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) (NeurIPS 2020)
- Packer et al., [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560) (2023). Context window as RAM, external storage as disk.
- Park et al., [Generative Agents](https://arxiv.org/abs/2304.03442) (UIST 2023)
- He et al., [MemoryArena](https://arxiv.org/abs/2602.16313) (ICML 2026). Test memory by the decisions it supports, not by recall.
- Zhang et al., [Useful Memories Become Faulty When Continuously Updated by LLMs](https://arxiv.org/abs/2605.12978) (2026). Memory the LLM keeps rewriting ends up worse than no memory; keep raw episodes and consolidate only with checks.
- Letta, [Benchmarking AI Agent Memory: Is a Filesystem All You Need?](https://www.letta.com/blog/benchmarking-ai-agent-memory) (Aug 2025). A plain folder of files beat a dedicated memory product.

## Multi-agent
- Cemri et al., [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657) (NeurIPS 2025). 14 failure modes from more than 1,600 traces.
- Walden Yan (Cognition), [Don't Build Multi-Agents](https://cognition.com/blog/dont-build-multi-agents) (Jun 2025) and [Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working) (Apr 2026)

## Evals
- Yao et al., [τ-bench](https://arxiv.org/abs/2406.12045) (ICLR 2025). Introduced pass^k: success on all k attempts.
- Rabanser et al., [Towards a Science of AI Agent Reliability](https://arxiv.org/abs/2602.16666) (ICML 2026)
- Hamel Husain and Shreya Shankar, [AI Evals: Everything You Need to Know](https://hamel.dev/blog/posts/evals-faq/) (Sep 2026). Error analysis on traces; check LLM judges before trusting them.

## RSI
- Anthropic, [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy). The "Automated R&D" threshold.
- OpenAI, [Preparedness Framework v2](https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf) (Apr 2025). The "AI Self-improvement" category.
- Google DeepMind, [Frontier Safety Framework v3.1](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3-1.pdf) (Apr 2026). ML R&D levels.
- Forecasting Research Institute, [How Close is Recursive Self-Improvement? A Review of the Evidence](https://forecastingresearch.org/research/recursive-self-improvement-v1) (Nov 2026). Skeptical counterweight.
- Narayanan and Kapoor, [AI as Normal Technology](https://knightcolumbia.org/content/ai-as-normal-technology) (Apr 2025). Skeptical counterweight.
- Philipp Schmid, [Recursive Self-Improvement](https://www.philschmid.de/recursive-self-improvement) (Aug 2026). Bounded vs truly recursive self-improvement.

## Agents for biology
- Huang et al., [Biomni](https://www.science.org/doi/10.1126/science.adz4351) (Science, Jul 2026). 150 tools mined from papers; the main agent works by writing code; wet-lab validated.
- Gottweis et al., [Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y) (Nature, May 2026). Hypothesis tournament; ranks plausibility, not truth.
- Ghareeb et al., [Robin](https://www.nature.com/articles/s41586-026-10652-y) (Nature, May 2026). Humans run experiments; the agent analyses results and proposes the next round.
- Mitchener et al., [Kosmos](https://arxiv.org/abs/2511.02824) (Nov 2025). Every statement cites code or a paper.
- Wei et al., [Fleming](https://www.biorxiv.org/content/10.1101/2025.04.01.646719v1) (2025). Closest antibiotic agent; wraps the authors' own validated models as tools.
- Roberts et al., [OpenScientist](https://www.medrxiv.org/content/10.64898/2026.03.15.26348338v1) (2026). Tested against randomized negative controls; did not fully reject false hypotheses.
- Cao et al., [Mozi](https://arxiv.org/abs/2603.03655) (2026). Target-to-lead pipeline with human checkpoints at uncertain decisions.
- Benchmarks: [BixBench](https://arxiv.org/abs/2503.00096), [LABBench2](https://arxiv.org/abs/2604.09554)

## Not incorporated yet
Recommended readings from Stanford's [CS 329Z: Engineering AI Agents](https://cs329z.stanford.edu/) (Fall 2026) that the primer pages don't use yet, in course order. The course's other 17 readings are already in the sections above (for the MCP spec and Anthropic's RSP, as newer versions).

- Zaharia et al., [The Shift from Models to Compound AI Systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) (BAIR, Feb 2024). Top results come from systems of models, retrievers and tools, not single models.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (NeurIPS 2017). The Transformer.
- Katharopoulos et al., [Transformers are RNNs](https://arxiv.org/abs/2006.16236) (ICML 2020). Linear attention; why long context is costly.
- Karpukhin et al., [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906) (EMNLP 2020). Embedding search beat keyword search (BM25) by 9–19% on top-20 retrieval.
- Khattab and Zaharia, [ColBERT](https://arxiv.org/abs/2004.12832) (SIGIR 2020). Fast token-level retrieval.
- Patil et al., [Gorilla](https://arxiv.org/abs/2305.15334) (NeurIPS 2024). Writing correct API calls; bad retrieved docs can be worse than none.
- Khattab et al., [DSPy](https://arxiv.org/abs/2310.03714) (ICLR 2024). Tune prompts against a metric instead of writing them by hand.
- LangChain, [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) (docs). Checkpoint and resume for long runs.
- Pan et al. (Arena and Berkeley), [HarnessTax: How Much Does the Harness Matter for Coding Agents?](https://arena.ai/blog/coding-agents-harness-tax) (Sep 2026). 21 model–harness pairs, 3 runs per task: the harness moved success by ±2–5% but cost by up to 5×.
- Yao et al., [ReAct](https://arxiv.org/abs/2210.03629) (ICLR 2023). Reasoning steps interleaved with tool actions.
- LangChain, [Context Engineering](https://www.langchain.com/blog/context-engineering-for-agents) (Jul 2025). Write, select, compress, isolate.
- Shinn et al., [Reflexion](https://arxiv.org/abs/2303.11366) (NeurIPS 2023, optional). Self-critique helps only when the check it relies on is reliable.
- Sumers et al., [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427) (TMLR 2024). CoALA.
- Wu et al., [AutoGen](https://arxiv.org/abs/2308.08155) (COLM 2024). Agents that talk to each other; a narrow safety-checker agent helped.
- Agrawal et al., [GEPA](https://arxiv.org/abs/2507.19457) (ICLR 2026). Evolves prompts from written feedback on runs; beat RL fine-tuning with far fewer runs.
- Opsahl-Ong et al., [MIPRO](https://arxiv.org/abs/2406.11695) (EMNLP 2024). Tunes instructions and examples together.
- Shao et al., [DeepSeekMath](https://arxiv.org/abs/2402.03300) (2024). Introduced GRPO.
- [Terminal-Bench leaderboard](https://www.tbench.ai/). Scores with confidence intervals and cost per model and harness.
- Merrill et al., [Terminal-Bench](https://arxiv.org/abs/2601.11868) (ICLR 2026). How to build and audit hard agent tasks; at least 5 runs per setup.
- Shreya Shankar, [Data Flywheels for LLM Applications](https://www.sh-reya.com/blog/ai-engineering-flywheel/) (Jul 2024). Choose metrics by reading real outputs.
- Tan et al., [Large Language Models for Data Annotation and Synthesis: A Survey](https://aclanthology.org/2024.emnlp-main.54/) (EMNLP 2024, optional).
- Yang et al., [SWE-smith](https://arxiv.org/abs/2504.21798) (NeurIPS 2025). Thousands of tasks made by planting bugs in real code.
- Shankar et al., [Who Validates the Validators?](https://arxiv.org/abs/2404.12272) (UIST 2024). Grading outputs changes your criteria; check judges against your own grades.
- Zhou et al., [LIMA](https://arxiv.org/abs/2305.11206) (NeurIPS 2023, optional). 1,000 hand-picked examples were enough.
- Ofir Press, [How to Build Good Language Modeling Benchmarks](https://ofir.io/How-to-Build-Good-Language-Modeling-Benchmarks/) (2024, optional). Real tasks, automatic scoring, never publish the answers.
- Polo et al., [tinyBenchmarks](https://arxiv.org/abs/2402.14992) (ICML 2024, optional). Small subsets that predict full benchmark scores.
- Zheng et al., [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685) (NeurIPS 2023). Judge biases (answer order, length, self-preference) and fixes.
- Ryan et al., [AutoMetrics](https://arxiv.org/abs/2512.17267) (ICLR 2026). Metrics built from under 100 human ratings.
- Zhu et al., [AutoLibra](https://arxiv.org/abs/2505.02820) (ICLR 2026, optional). Turns free-text feedback on runs into metrics a judge scores.
- Jimenez et al., [SWE-bench](https://arxiv.org/abs/2310.06770) (ICLR 2024). Real GitHub issues; compares issues from before and after the training cutoff to check for memorization.
- Shao et al., [PrivacyLens](https://arxiv.org/abs/2409.00138) (NeurIPS 2024). Agents leak private data in action even when they answer privacy questions correctly.
- Zhang and Yang, [Searching for Privacy Risks in LLM Agents via Simulation](https://arxiv.org/abs/2508.10880) (2025). Attacks and defenses evolved against each other.
- Li, [Agentic LLMs as Powerful Deanonymizers](https://arxiv.org/abs/2601.05918) (Jan 2026). Web agents traced anonymized scientist interviews to their papers.
- Wen et al., [Contextualized Privacy Defense for LLM Agents](https://arxiv.org/abs/2603.02983) (2026, optional).
- OpenAI, [Understanding prompt injections](https://openai.com/index/prompt-injections/) (Nov 2025, optional).
- Wang et al., [OpenHands](https://arxiv.org/abs/2407.16741) (ICLR 2025). Open coding-agent platform; its benchmarks include BioCoder.
- Anthropic, [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices) (docs, optional). The course's 2025 post now redirects here.
- Shaikh et al., [Creating General User Models from Computer Use](https://arxiv.org/abs/2505.10831) (UIST 2025).
- Shaikh et al., [Learning Next Action Predictors from Human-Computer Interaction](https://arxiv.org/abs/2603.05923) (2026, optional).
- [OpenClaw](https://github.com/openclaw/openclaw) (optional). Open-source personal assistant.

## Not checked yet
- OpenAI blocked automated fetches. Open these yourself: "Harness engineering" (Lopopolo) and "Unrolling the Codex agent loop" (Bolin).
