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
   - Fetch global/pre-open indicators.
   - Adjust conviction for broad market bias and sector-specific cues.
   - Send one concise actionable briefing shortly before market open.

3. **Post-market calibration**
   - Compare recommendations against actual outcomes after close.
   - Identify which factors worked/failed.
   - Patch the scanner logic immediately.

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

- Scan price → close return
- Open → close return
- Intraday high/low excursion
- Winners > +1%
- Flat between -0.5% and +1%
- Losers < -0.5%
- Sector hit rate
- Hit rate by label: Momentum, Swing, Long-term

Then state:

1. What worked
2. What failed
3. Root causes
4. Specific rule changes
5. Whether the automation was patched

## Pitfalls

- Do not chase overextended RSI as momentum; distinguish continuation from exhaustion.
- Do not let broad global bias override sector-specific headwinds.
- Do not call a setup Low risk if recent range/volatility is wide.
- Do not recommend sector names from macro cues alone; require stock-level confirmation.
- Clean stale tickers and NaN indicator values so scheduled reports stay readable.

## References

- `references/nse-bse-premarket-scanner.md` — NSE/BSE-specific implementation notes and lessons from Daksh's scanner.
