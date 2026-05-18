---
name: market-intelligence-automation
description: Build and maintain automated market scanners, pre-market briefings, and post-market calibration loops for trading/research workflows.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [markets, trading, automation, scanners, premarket, postmortem, finance]
---

# Market Intelligence Automation

## When to Use

Use this skill when the user wants to:

- Build a daily market scanner or ranked stock-pick report
- Schedule pre-market or post-market briefings
- Combine technicals, fundamentals, sentiment, and macro indicators
- Review what worked after market close and improve the logic
- Automate market research delivery to Telegram/email/etc.

## Core Pattern

Prefer a **two-stage workflow** for markets with a defined open:

1. **Early silent scan**
   - Score the trade universe before the final pre-open window.
   - Save results to a machine-readable cache.
   - Do not deliver a noisy early report unless the user explicitly wants it.

2. **Pre-market pulse**
   - Read the cached picks.
   - Fetch global/pre-market indicators.
   - Adjust conviction for broad market bias and sector-specific cues.
   - Send one concise actionable briefing shortly before market open.

3. **Live decision-card paper test**
   - Before treating picks as actionable, verify the scanner cache is fresh for the current trading day.
   - If stale, rerun the silent scanner first; do not test against old picks.
   - Convert top picks into structured decision-card payloads with market regime, candidate evidence, risk gates, invalidation/stop fields, and non-advice disclaimer.
   - A risk-off market regime should be treated as a valid test outcome: the framework may correctly output WAIT for all fresh longs. Do not force BUY candidates just to make the test look active.
   - Save the generated card set to a machine-readable cache so post-market review can compare decisions against actual close/intraday outcomes.

4. **Post-market calibration**
   - Compare recommendations against actual outcomes after close.
   - Identify which factors worked/failed.
   - Patch the scanner or decision-card logic immediately.

## Scoring Framework

A practical weighted framework:

- Fundamentals: revenue/profit growth, ROE/ROCE, debt, valuation, margins
- Technicals: moving averages, RSI, 20-day return, volume surge, MACD, breakouts
- Sector/macro: sector tailwind/headwind, commodities, currency, global indices
- Sentiment: institutional flows/proxies, insider/promoter activity, unusual volume, news activity

Filter out illiquid and low-quality names before ranking.

## Output Format

For each pick, include only:

- Stock/ticker
- Short reason
- Conviction score
- Risk level
- Trade type: Swing, Momentum, Long-term, or Watchlist Only
- Explicit warnings: overextended RSI, high volatility, sector headwind, data quality issue

Always include a non-advice disclaimer for market outputs.

## Post-Market Review Checklist

After close, compute:

- Scan/test price → close return
- Open → close return
- Intraday high/low excursion
- Winners > +1%
- Flat between -0.5% and +1%
- Losers < -0.5%
- Sector hit rate
- Hit rate by label: Momentum, Swing, Long-term
- For decision-card tests: whether each decision (`READY_TO_PLAN`, `WATCH`, `WAIT`) was directionally justified by the day’s action
- For all-`WAIT` risk-off days: whether WAIT avoided weak longs, or whether any exceptional setup should have bypassed the market-regime block

Then state:

1. What worked
2. What failed
3. Root causes
4. Specific rule changes
5. Whether the scanner/decision-card automation was patched

## Pitfalls

- Do not chase overextended RSI as momentum; distinguish continuation from exhaustion.
- Do not let broad global bias override sector-specific headwinds.
- Do not call a setup Low risk if recent range/volatility is wide.
- Do not recommend sector names from macro cues alone; require stock-level confirmation.
- Clean stale tickers and NaN indicator values so scheduled reports stay readable.
- Do not use stale scanner caches for live tests. Check `generated_at` first and rerun the scanner if it is not from the current trading day/session.
- Do not treat an all-`WAIT` decision-card output as a failed test on risk-off days. It may be the correct behavior; verify after close.
- When a project-specific market script already has dependencies/runtime working, run live-data probes with that same runtime instead of assuming the generic sandbox has every finance dependency installed.

## References

- `references/nse-bse-premarket-scanner.md` — NSE/BSE-specific implementation notes and lessons from Daksh's scanner.
- `references/tradepilot-decision-card-live-test.md` — pattern for live paper-testing Decision Card engines against real market sessions.
