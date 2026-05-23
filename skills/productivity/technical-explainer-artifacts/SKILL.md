---
name: technical-explainer-artifacts
description: Explain technical websites, specs, papers, or product documentation in simple language and produce useful learning artifacts (diagrams, mental models, flows, cheat sheets, glossaries). Use when the user asks to “read this and explain,” “make it easy,” “summarize this spec,” or requests artifacts for understanding.
---

# Technical Explainer Artifacts

## When to use

Use this skill when the user provides a technical URL, document, screenshot, article, spec, or repo docs and asks for an easy explanation, summary, or artifacts.

Typical triggers:
- “read this and explain it to me in easy way”
- “explain this spec”
- “make artifacts / diagrams / cheat sheet”
- “what does this protocol/product/docs mean?”
- “explain like I’m non-technical / founder / beginner”

## Outcome

Produce an explanation that helps the user quickly understand:
1. What the thing is.
2. Why it exists.
3. Who the actors/components are.
4. How the flow works.
5. What the implications are.
6. What to remember.

Add artifacts inline unless the user asks for deliverable files.

## Workflow

1. **Read enough source material first**
   - Prefer page extraction for simple pages.
   - If extraction fails or returns empty content, use the browser snapshot/DOM text path.
   - Follow key navigation links when the landing page is mostly marketing copy and the substance is in docs/spec pages.
   - Capture at least: homepage positioning, core concepts, architecture/roles, technical flow, roadmap/limitations if present.

2. **Build the explanation from the user’s perspective**
   - Start with a plain-language one-liner.
   - Use analogies before jargon.
   - Define acronyms and protocol names immediately.
   - Separate “what it does” from “why it matters.”

3. **Create artifacts that reduce cognitive load**
   Good default artifact set:
   - Simple mental model diagram.
   - Actor/component diagram.
   - Step-by-step flow.
   - Comparison table/list, e.g. `X vs Y`.
   - Glossary of terms.
   - Strategic takeaway / implications.

   On Telegram, avoid markdown tables; use bullets and labeled fields instead.

4. **Keep grounding clear**
   - State when something comes from the source docs.
   - Separate your interpretation/strategic takeaway from source claims.
   - If the source is a roadmap or draft spec, call out that it may change.

5. **End with a compact takeaway**
   - Include a “one-line explanation” or “if you remember only one thing” section.
   - If useful, add “what this means for builders/founders/users.”

## Artifact patterns

### Mental model

```text
Without the standard:
A connects separately to B, C, D, E.

With the standard:
A speaks one common language to B, C, D, E.
```

### Actor map

```text
User
  ↓
Agent / App
  ↓ standard protocol/API
Business / Service
  ↓
Payment / Identity / Fulfillment systems
```

### Flow

```text
1. Discover capabilities
2. Negotiate supported features
3. Execute the core task
4. Confirm/authorize sensitive action
5. Complete
6. Track/manage after completion
```

### Comparison

Use bullet groups, not pipe tables on Telegram:

- **Protocol A**: handles X, Y, Z.
- **Protocol B**: handles trust/payment/authorization.
- **Together**: enable safe end-to-end workflow.

## Pitfalls

- Do not only summarize marketing copy if docs/spec links are available.
- Do not over-index on jargon from the source; translate it.
- Do not produce a giant undifferentiated essay. Break with headings and artifacts.
- Do not imply a roadmap item is guaranteed; label it as planned/current direction.
- Do not claim implementation details not visible in the source.

## References

- `references/ucp-agentic-commerce.md` — distilled notes from explaining Universal Commerce Protocol (UCP): actors, capability negotiation, AP2 relationship, payment/security model, and artifact examples.
