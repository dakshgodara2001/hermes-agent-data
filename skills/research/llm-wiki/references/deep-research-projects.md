# Deep Research Projects in the Wiki

Use this reference when a user asks for a broad, source-heavy research project that should become durable wiki knowledge, not just a chat answer.

## Recommended workflow

1. Orient first
   - Read `SCHEMA.md`, `index.md`, and recent `log.md` before creating pages.
   - Check whether the topic should be a `queries/`, `concepts/`, `markets/`, `theses/`, or `comparisons/` page.

2. Make a visible research task breakdown
   - Official/regulatory/primary sources.
   - Industry/player/product sources.
   - News/blog/social/practitioner pain points.
   - Academic/research papers.
   - Synthesis model, dependencies, cracks, and opportunities.
   - Verification and wiki updates.

3. Use parallel agents carefully
   - Broad research subagents can time out if each tries to browse too much.
   - Prefer narrowly-scoped agents with explicit deliverable shape and source limits.
   - If subagents time out, do not abandon the project: fall back to scripted/batched search/extract calls, grouping queries by source class.

4. Preserve source classes explicitly
   - Separate high-confidence official sources from medium-confidence industry/news sources and anecdotal social/forum signals.
   - Mark social evidence as product-discovery signal, not authoritative fact.

5. Build from first principles
   - Identify blocks, inputs, outputs, dependencies, failure modes, and why the block matters.
   - Link blocks into a system map rather than dumping disconnected facts.

6. Convert cracks into opportunities
   - For each crack: name the problem, propose a startup/product wedge, rate attractiveness out of 10, and state whether AI is a game changer.
   - Distinguish deterministic safety-critical components from AI-assisted explanation, auditing, and triage.

7. File the result durably
   - Create a substantial `queries/<topic>.md` page for one-off deep dives, or a `concepts/`/`theses/` page if it will be a recurring reference.
   - Update `SCHEMA.md` tags only if the taxonomy lacks required class-level tags.
   - Update `index.md` and append to `log.md` in the same session.

## Pitfalls

- Do not let failed/timeout subagents become the endpoint; switch strategy and continue.
- Do not blend official regulatory facts with Reddit/X anecdotes without labeling confidence.
- Do not create many narrow pages for a single exploratory deep dive unless the topic will recur; prefer one rich query page plus links to existing concepts.
- Do not overstate AI as alpha generation in trading/finance research. In regulated, risk-heavy domains, AI is usually strongest as critic, auditor, explainer, compliance assistant, and incident investigator.
