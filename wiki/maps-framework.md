---
name: maps-framework
type: concept
tags: [ai, prompting, framework, strategy, guardrails]
sources: [youtube-maps-framework]
updated: 2026-06-04
---

# MAPS Framework

**Summary**: A structured prompting method for getting high-quality, precise outputs from LLMs — and the operating standard for every AI interaction in Joshua's business.

**Sources**: YouTube clip (MAPS framework explainer) — ingested 2026-06-04

**Last updated**: 2026-06-04

---

## What It Is

Most people use AI like a fancy Google search: basic input, generic output, manual cleanup. MAPS is the antidote — a four-part structure that gives the AI direction, task, context, and format so it returns something actually useful the first time.

It also scales up. As you move from basic LLMs to autonomous agentic systems (like [[vince-ai]] or the [[wih-app]] AI layer), MAPS stays the operating standard. When agents run end-to-end workflows, you're a "human on the loop" — and MAPS is how you keep the loop honest.

---

## The Four Components

### M — Mission
The ultimate outcome. Not just what you want done, but *why* — the strategic goal behind the request.

- **Weak**: "Find me leads"
- **Strong**: "I need 30 new customers a month to hit my revenue targets"

Mission gives the AI direction so it doesn't optimize for the wrong thing.

### A — Ask
The single, specific task. One request. Crystal clear.

- **Weak**: "Help me with some ideas around leads"
- **Strong**: "Give me 40 qualified leads — include name, email, and cell number"

One ask per prompt. If you have multiple tasks, split them into separate prompts.

### P — Parameters
The context and background the AI needs to do the job right. Includes:
- Ideal customer profile
- Examples of what has worked before
- Constraints, non-negotiables, known context

The more parameters, the sharper the output. Because Joshua uses [[Wispr Flow]] (voice-to-text), parameters are the easiest component to load fast — just talk through the context instead of typing it.

### S — Shape
Exactly what the final output looks and sounds like:
- **Format**: CSV, markdown, bullet points, table, prose
- **Tone**: conversational, formal, direct, casual-professional
- **Length**: one sentence, full doc, numbered list

Can include a screenshot of a reference example to show the AI precisely what the end product should look like.

---

## Why It Matters at Scale

MAPS is not just a prompting tip — it's the framework that governs how AI tools get used across the entire [[ai-automation-strategy]]:

1. **Basic LLM use**: MAPS keeps one-off requests sharp and prevents generic output
2. **Workflow automation**: Agents running in [[ghl]] need clear Mission + Parameters so they don't drift
3. **Agentic systems**: Full end-to-end agents (Vince, wih-app AI) require MAPS-structured inputs at setup so the agent knows what success looks like and can execute without constant correction

Joshua's rule: AI is a tool like a hammer — you have to know how to swing it. MAPS is the swing.

---

## Operating Standard

MAPS is the internal checklist for every significant AI interaction in this business. Before deploying a prompt, workflow trigger, or agent instruction, verify:

- [ ] **M**: Is the mission (the WHY) clear?
- [ ] **A**: Is the ask single and specific?
- [ ] **P**: Is the necessary context/background included?
- [ ] **S**: Is the output format defined?

If any component is missing, the output will be generic, misaligned, or require manual rework — the exact waste Joshua won't tolerate.

---

## Related pages
- [[ai-automation-strategy]]
- [[ai-operating-system]]
- [[vince-ai]]
- [[wih-app]]
- [[business-brain]]
- [[claude-code-workflow]]
- [[information-moat]]
