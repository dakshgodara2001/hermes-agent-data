# NSE/BSE Premarket Scanner + Post-Market Calibration

This reference captures the durable workflow that emerged while building Daksh's daily Indian market scanner.

## Architecture

Use a two-stage morning flow:

1. **8:00 AM IST silent scan**
   - Scan liquid NSE/BSE universe.
   - Score fundamentals, technicals, sector/macro, and sentiment.
   - Save ranked picks to a local JSON cache.
   - Do not send the full report yet.

2. **9:05 AM IST pre-market pulse**
   - Read the 8 AM cached picks.
   - Fetch global/pre-market indicators.
   - Adjust conviction by market bias and sector-specific cues.
   - Send one combined briefing before 9:15 AM market open.

## Core Inputs

### Stock-level factors

- Fundamentals: revenue/profit growth, ROE/ROCE, debt, valuation, margins
- Technicals: moving averages, 20-day return, volume surge, RSI, MACD, 52-week proximity
- Sector/macro: sector tailwind/headwind
- Sentiment proxies: institutional ownership, ETF/FII proxy, unusual volume, analyst recs if available

### Global/pre-market factors

- US close: S&P 500, Nasdaq, Dow, VIX
- Asia: Nikkei, Hang Seng, Shanghai if reliable
- India: Nifty, Bank Nifty, India VIX
- Commodities: WTI/Brent crude, gold, silver
- FX: USD/INR, DXY
- Institutional proxies: INDA ETF, EM ETF

## Important Logic Rules Learned

### RSI overextension

Do not treat very high RSI as clean momentum. After post-market review, RSI > 78 should be treated as exhaustion risk.

Recommended rule:

- RSI 50–70: constructive
- RSI 70–78: mildly overbought but can continue
- RSI > 78: heavily penalize; avoid Momentum/Swing tags; mark as Watchlist/Pullback-only

### Momentum quality filter

A Momentum Trade label should require business quality too, not only price/volume.

Recommended minimums:

- 20-day return > 5%
- volume surge > 1.3x
- technical score > 6.5/10
- fundamental score >= 6.0/10
- RSI <= 78

### IT/Technology filter

Do not recommend IT names based on fundamentals alone when the intraday technical setup is weak. Require tech score >= 6.5/10 for Technology sector picks.

### Crude/Energy cross-check

When crude is falling meaningfully, explicitly penalize Energy stocks in the 9:05 pulse. A broad neutral/bullish market bias can mask sector-specific headwinds.

### High-volatility flag

Flag names with wide 30-day high-low ranges as higher-risk. A starting threshold of 18% of price is more useful than 12% for Indian equities; 12% was too noisy.

High-volatility flags should:

- Prevent Low-risk display
- Add a warning: smaller size / tighter risk controls
- Reduce adjusted conviction slightly

### Invalid-data hygiene

Some Yahoo Finance tickers go stale. Clean them rather than letting stderr noise leak into cron reports. Examples encountered:

- `HDFC.NS` delisted/merged; replace with a current financial name such as `JIOFIN.NS`
- `BERGERPAINTS.NS` should be `BERGEPAINT.NS`
- `DALMIACEME.NS` should be `DALBHARAT.NS`
- Avoid stale/deprecated symbols in scheduled jobs

Also discard indicator reads where price/change is NaN.

## Post-Market Calibration Loop

After market close, compare recommendations against actual outcomes:

- scan price → close return
- open → close intraday return
- high/low excursion
- winners > +1%
- flat between -0.5% and +1%
- losers < -0.5%
- sector hit rate
- which labels worked: Momentum, Swing, Long-term

Then update rules immediately. For Daksh, the expectation is not just a post-mortem summary but applying fixes to the automation.

## Reporting Style

Keep reports actionable:

- Top picks only
- Short reason
- conviction score
- risk level
- trade type: Swing / Momentum / Long-term / Watchlist Only
- explicit warnings for overextension, high volatility, and sector headwinds

Always include a non-advice disclaimer for market outputs.
