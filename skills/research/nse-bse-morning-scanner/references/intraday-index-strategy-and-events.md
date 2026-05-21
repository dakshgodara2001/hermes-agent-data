# Intraday Index Strategy + Event Check Workflow

Session learning from May 21, 2026: after the morning cron was narrowed to Nifty 50 / Bank Nifty, the user asked for live chart strategy and market-moving events. Future runs should treat this as a class-level workflow: current index structure first, then event/news catalysts.

## 1) Intraday chart probe

Use fresh 5-minute yfinance data for:

- `^NSEI` — Nifty 50
- `^NSEBANK` — Bank Nifty
- `^INDIAVIX` — India VIX

For each index, calculate:

- Last timestamp and LTP
- % change vs previous daily close
- Day open, day high, day low
- 15-minute opening range high/low from first 3 five-minute candles
- EMA20 and EMA50 on 5-minute closes
- RSI14 on 5-minute closes
- Whether price is above/below/mixed around EMA20/EMA50

For daily context on Nifty, also useful:

- Previous close
- Previous-day pivot, R1/R2, S1/S2
- Daily SMA20/SMA50
- Daily RSI14 and ATR14
- Recent 20-day swing high/low

## 2) Strategy phrasing

Avoid deterministic calls like “market will go up.” Use conditional triggers:

- Bullish only if price reclaims/sustains above the opening-range high or a clearly stated reclaim zone.
- Bearish only if price breaks day low/opening-range low, or fails a pullback into resistance.
- If price sits between levels, say “no fresh directional trade; avoid chop.”
- If Bank Nifty is weaker than Nifty, downgrade the setup to mixed/weak and avoid aggressive Nifty longs.
- Mention India VIX as a position-sizing / stop-tightness modifier.

Example format:

- Nifty above X → long setup, targets Y/Z, stop below A.
- Nifty below B → short setup, targets C/D, stop above E.
- Between X and B → no-trade / range only.
- Bank Nifty reclaim level: M; weak below N.

## 3) Watchlist performance check

If a stock watchlist cache exists, compare the cached top picks against current intraday prices:

- Fetch each ticker as `<symbol>.NS`.
- Report LTP, % change vs previous daily close, day high, day low.
- Separate relative strength names from failed/weak names.
- Do not introduce non-index stocks; stay within Nifty 50 / Bank Nifty constituents.

## 4) Event/news catalyst check

When web_search fails or is unavailable, use direct sources:

- NSE event calendar JSON: `https://www.nseindia.com/api/event-calendar`
  - Needs browser-like headers and an initial request to `https://www.nseindia.com` for cookies.
  - Filter by dates like `21-May-2026`, `22-May-2026`.
- Google News RSS fallback:
  - `https://news.google.com/rss/search?q=<query>&hl=en-IN&gl=IN&ceid=IN:en`
  - Parse RSS XML titles and publication dates.

Useful queries:

- `Nifty today market moving events <date>`
- `Bank Nifty today news <date>`
- `NSE corporate results today <date> Nifty 50 Bank Nifty earnings`
- `India economic calendar <date>`
- `global markets <date> Fed oil dollar rupee`

Event categories to highlight for Nifty / Bank Nifty:

- Nifty heavyweight earnings/results: ITC, Reliance, HDFC Bank, ICICI Bank, Infosys/TCS/HCLTech, LT, etc.
- Bank/FI events and RBI announcements.
- Rupee/USD moves and FII-flow implications.
- Crude oil direction for India macro, OMCs, energy, aviation/paints.
- Fed/yield/dollar cues affecting FII risk appetite.
- Expiry day effects when the date is Thursday; treat as volatility/chop risk, not a directional signal.

## 5) User-facing summary style

The user wants trading-useful commentary, not a long news dump. Summarize as:

- “Major things that can move market today” with 3–5 bullets.
- “What matters most for intraday strategy now.”
- Tie event risk back to current Nifty/Bank Nifty levels.
- End with a concise bottom line: bullish/reclaim levels, weak/breakdown levels, and whether to avoid chasing.
