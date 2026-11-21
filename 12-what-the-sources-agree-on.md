---
title: "12. What the sources agree on"
nav_order: 13
---

# 12. What the sources agree on

The sources behind this primer were written by different people at different companies over several years, and they often use different words. Underneath those differences, the same handful of ideas comes up again and again. This page collects them, because together they are a good summary of how to think about agents.

The first idea is that the model only produces text and the harness does everything else. The model writes a request, and the harness runs the tool, applies the permissions and keeps the records. This division explains why the same model can behave very differently in different harnesses, and why so much engineering effort goes into the software around the model rather than into the model itself.

The second is that context is the scarce resource. Every source on tools, harnesses, context and memory comes back to three facts: the model sees only its context, the context is limited, and filling it with irrelevant material makes performance worse. Many techniques that look unrelated, such as consolidated tools, skills that load on demand, code execution, compaction, subagents and just-in-time retrieval, are all ways of keeping the context small and relevant.

The third is that lasting state belongs outside the model. Because the model forgets everything between calls and every session starts fresh, agents keep their progress, plans and knowledge in files, logs and version control, and bring back only what they need. The long-running agents on page 6, Manus's to-do list, Claude Code's memory files and Anthropic's session log are all versions of this one idea.

The fourth is to start simple and add complexity only when it is shown to help. Anthropic's advice on choosing between workflows and agents, the minimal SWE-bench agent, the simple loops found inside production harnesses, the success of plain files over specialized memory systems, and the mixed record of multi-agent systems all point the same way. Each extra component should earn its place through measurement.

The fifth is that checking should be separate from doing. Models tend to judge their own work too kindly, so the sources repeatedly separate the agent that produces work from whatever checks it. Böckeler's sensors, Anthropic's evaluator agent, Cognition's reviewer with a clean context and the graders of an eval are all examples. Verification is also the main limit on self-improvement.

The sixth is that the interface between the model and the world deserves real design work. Tool names, descriptions, parameters, outputs and error messages are all read by the model and shape its behaviour as much as the system prompt does. SWE-agent's agent-computer interface, Anthropic's guidance on writing tools and the attention given to tool descriptions all make this point.

The seventh is that harness components are workarounds for model weaknesses, and they go out of date. Each piece of scaffolding assumes the model cannot do something on its own, and as models improve, some of those assumptions stop being true. Good harnesses are re-tested with each new model and simplified when they can be.

The eighth is that intuition is not enough, so you have to measure and read transcripts. The system prompt line that passed early tests but cost performance, the finding that differences between harnesses are often no larger than the noise between repeated runs, and the advice to begin evaluation by reading real runs all say the same thing. The only reliable way to know whether a change helps is to test it and to look closely at what the agent actually did.

The sources do disagree in a few places, and these are worth remembering. They define "harness" at different scales, from the whole system down to only the loop. They define "memory" narrowly or broadly. They differ on how much multi-agent systems help, although they agree on the kind of task where they help. And early findings about where information sits in the context have not held up equally for every model. Where sources disagree, the disagreement is usually about scope or about which tasks were tested, not about the basic picture.

## Key vocabulary

- **Scaffolding**: another word for the parts of a harness built around the model, especially the parts that make up for a weakness of the model.
- **Verification**: checking whether the agent's work is actually correct, done separately from the work itself.

Next: [13. Glossary](13-glossary.md)
