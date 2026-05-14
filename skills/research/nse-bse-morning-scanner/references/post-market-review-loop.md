# Post-Market Review Loop for NSE/BSE Scanner

Use this after market close to compare the 8 AM/9:05 AM recommendations with actual outcomes and improve the rules.

## Review workflow

1. Load the morning cache from `~/.hermes/cache/stock_scan_cache.json`.
2. Fetch same-day OHLC close data for each pick via yfinance.
3. Compare both:
   - scan price → close return (did the pick work from recommendation price?)
   - open → close return (did it work as an intraday trade?)
4. Bucket results:
   - Winner: > +1%
   - Flat: -0.5% to +1%
   - Loser: < -0.5%
5. For each miss, identify a repeatable failure mode, not just a story.
6. Patch the scanner or pulse only when the failure mode is generalizable.
7. Re-run `python3 -m py_compile nse_stock_scanner.py premarket_pulse.py`, then run both scripts end-to-end.

## May 14, 2026 lessons

Outcome summary: 10/15 positive, 7/15 winners, average scan→close return about +1.14%, but several avoidable misses.

What worked:
- Healthcare/pharma strength was correctly captured: CIPLA, SUNPHARMA, LUPIN, MANKIND, AUROPHARMA were positive.
- CIPLA worked especially well because bullish MAs + volume surge + reasonable RSI confirmed the move.
- PIDILITIND, NMDC, and BHEL showed that the technical framework could catch strong directional names.

What failed and the rule added:
- COFORGE: fundamentals looked good, but tech score was weak. Rule: Technology names require tech_score ≥ 6.5.
- COALINDIA: broad global bias was ok, but crude weakness conflicted with Energy. Rule: falling crude penalizes Energy picks in the pulse.
- HFCL: RSI ~86 and huge 20d run signaled exhaustion. Rule: RSI > 78 is not Momentum/Swing; mark Watchlist Only or penalize.
- TATACONSUM/SAIL style volume spikes: volume alone is not enough. Rule: Momentum Trade requires fund_score ≥ 6.0 plus RSI guard.
- High intraday/30d range names need position sizing warnings. Rule: 30d range > 18% triggers HIGH_VOLATILITY warning and prevents Low risk label.

## Guardrails

Do not overfit to one day. Add rules only when they address a broad class of repeatable misses: overextension, weak technical confirmation, macro conflict, low-quality momentum, or volatility/risk sizing.

Keep the user-facing report concise: top picks, reason, conviction, risk, trade type, and specific warnings. Avoid long explanations in the morning report; save detailed analysis for post-market review.
