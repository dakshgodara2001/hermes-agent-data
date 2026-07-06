---
name: research-monitoring-intelligence
description: "Use when discovering, monitoring, synthesizing, or operationalizing research/market information: arXiv search, blog/RSS monitoring, LLM wiki knowledge bases, Polymarket queries, market scanners, and research intelligence loops."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, monitoring, intelligence, arxiv, markets, synthesis]
    related_skills: []
---

# Research Monitoring Intelligence

## Overview

This umbrella covers evidence-gathering workflows over research and market information sources. The common pattern is query/monitor, collect grounded data, synthesize with citations/links, and optionally automate repeated scans.

## When to Use

- Search academic papers, especially arXiv, by topic, author, category, or ID.
- Monitor blogs/RSS feeds and summarize changes.
- Build/query an interlinked markdown knowledge base such as an LLM wiki.
- Query prediction markets, order books, prices, or market history.
- Build or maintain market scanners, pre-market briefings, post-market calibration loops, or research intelligence automation.

## Mode Selection

| Mode | Former narrow skill(s) | Output | Verification |
|---|---|---|---|
| Academic discovery | `arxiv` | Paper list, abstracts, IDs, PDFs, short synthesis | Include arXiv IDs/URLs and query terms. |
| Feed monitoring | `blogwatcher` | Changed posts, summaries, alerts | Confirm feed URL and last-seen/change state. |
| Knowledge base | `llm-wiki` | Local markdown wiki, graph, query result | Confirm files/index/server status. |
| Prediction markets | `polymarket` | Market metadata, prices, orderbook/history | Include market id/slug and endpoint/source time. |
| Market intelligence automation | `market-intelligence-automation` | Scanner, briefing, calibration report | Show data freshness, sources, and scheduled/manual run output. |

## Workflow

1. **Define the question and freshness requirement.** Is this a one-time literature search, current market state, or recurring monitor?
2. **Query source systems.** Use source-specific APIs/CLIs when available; keep raw handles (URLs, IDs, timestamps).
3. **Normalize evidence.** Deduplicate, group by theme, and separate facts from interpretation.
4. **Synthesize.** Provide citations/links and note uncertainty or stale data.
5. **Automate only if asked.** For recurring scans, create a self-contained cron prompt/script and verify a manual run first.

## Common Pitfalls

- Do not summarize current markets or feeds from memory; fetch live data.
- Do not bury source-specific commands in separate micro-skills; store bulky endpoint notes under `references/`.
- Do not overfit a market scanner to one session; keep configurable symbols, horizons, and thresholds.
- Do not omit source timestamps for time-sensitive intelligence.

## Verification Checklist

- [ ] Live/source data fetched or blocker stated.
- [ ] IDs/URLs/timestamps preserved.
- [ ] Synthesis distinguishes evidence from judgment.
- [ ] Automation verified manually before scheduling.
