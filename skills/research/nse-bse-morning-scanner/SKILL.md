---
name: nse-bse-morning-scanner
description: >
  Daily Nifty 50 / Bank Nifty intelligence system: a silent 8 AM scanner builds a conviction-ranked
  cache from only Nifty 50 + Bank Nifty constituent stocks, and a 9:05 AM pre-market pulse delivers
  focused commentary on Nifty 50, Bank Nifty, and qualifying underlying stocks before the bell.
  Use this skill when setting up or maintaining the morning index-focused stock scan cron system for Indian markets.
version: 1.0.0
author: Hermes Agent
tags: [stocks, NSE, BSE, India, markets, trading, cron, scanner, pre-market]
---

# NSE/BSE Morning Scanner

A two-stage daily market intelligence pipeline focused on Nifty 50, Bank Nifty, and their underlying constituent stocks.

## Architecture

```
8:00 AM  →  nse_stock_scanner.py --silent  →  cache JSON (no delivery)
9:05 AM  →  premarket_pulse.py             →  combined report → Telegram
```

**Output rule:** The delivered 9:05 AM message should contain only Nifty 50 commentary, Bank Nifty commentary, and qualifying underlying constituent stocks. Global indicators may be fetched internally for bias scoring, but should not be printed as standalone US/Asia/commodity sections unless the user asks for them.

---

## File Locations

| File | Purpose |
|------|---------|
| `~/.hermes/bin/nse_stock_scanner.py` | Stock screener — scores only Nifty 50 + Bank Nifty constituents |
| `~/.hermes/bin/premarket_pulse.py` | Pre-market pulse — Nifty 50 + Bank Nifty commentary + filtered constituent watchlist |
| `~/.hermes/cache/stock_scan_cache.json` | Ephemeral cache shared between the two scripts |

---

## Cron Jobs

```
Job 1 — Silent scanner (8 AM, Mon–Fri, local delivery)
  schedule: 0 8 * * 1-5
  prompt: run nse_stock_scanner.py --silent → saves cache, no report
  deliver: local

Job 2 — Pre-market pulse (9:05 AM, Mon–Fri, Telegram delivery)
  schedule: 5 9 * * 1-5
  prompt: run premarket_pulse.py → full report
  deliver: origin
```

---

## Stock Scoring Framework (nse_stock_scanner.py)

Weighted composite score across 4 pillars:

| Pillar | Weight | Signals |
|--------|--------|---------|
| Fundamentals | 30% | PE, P/B, ROE, D/E ratio, revenue growth, earnings growth, profit margin |
| Technicals | 35% | RSI (14), MA20/50/200, MACD, 20d return, volume surge, 52w breakout |
| Sector/Macro | 20% | Sector tailwind score (hardcoded per sector, update seasonally) |
| Sentiment | 15% | Institutional ownership %, insider %, analyst rec, unusual volume |

**Liquidity filter:** avg daily volume > 500K AND market cap > ₹2000 Cr

**Conviction threshold:** only stocks scoring ≥ 5.5/10 are included

**Trade type classification:**
- Long-term Hold: fundamentals > 6.5 AND technicals > 5.5
- Momentum Trade: 20d return > 5%, volume surge > 1.3x, tech > 6.5, fundamentals ≥ 6.0, RSI ≤ 78
- Swing Trade: tech score 4.5–7.5 AND RSI 40–65
- Watchlist Only: overextended setups (e.g. RSI > 78) that should not be chased intraday

**Post-market review rules (added after May 14, 2026 review):**
- RSI > 78 is exhaustion risk, not clean momentum; penalize heavily and avoid auto Swing/Momentum tags.
- Momentum tags require minimum business quality (fund_score ≥ 6.0) to avoid low-quality volume spikes.
- Technology picks require tech_score ≥ 6.5; do not recommend IT names from fundamentals alone.
- Flag high-volatility names when 30d high-low range exceeds 18% of price; bump risk and add sizing warning.
- Pulse-side global adjustment must penalize Energy picks when crude is falling meaningfully.

See `references/post-market-review-loop.md` for the outcome-review workflow and the May 14 lessons that produced these guards.

---

## Intraday Index Chart Review

When the user asks how Nifty 50 / Bank Nifty are performing now, or asks for a chart-based strategy, do not rely on the morning pulse alone. Fetch fresh intraday data and derive actionable levels:

1. Use yfinance 5-minute data for `^NSEI`, `^NSEBANK`, and `^INDIAVIX`.
2. Compute and report: LTP, % change vs previous close, day high/low, 15-minute opening range high/low, 5-minute EMA20/EMA50, 5-minute RSI, and whether price is above/below those EMAs.
3. For strategy, translate levels into conditional triggers, not predictions:
   - Long only after reclaim/sustain above opening-range high or key reclaim zone.
   - Short only after breakdown or failed pullback below opening-range low / day low.
   - If price is between triggers, explicitly say “no fresh directional trade / avoid chop.”
4. Cross-check Nifty with Bank Nifty. If Bank Nifty is below its opening range or EMAs while Nifty is holding up, label the setup as weak/mixed and avoid aggressive longs.
5. Keep the output focused on Nifty 50, Bank Nifty, India VIX, and current watchlist stocks; avoid broad unrelated market commentary unless the user asks.

See `references/intraday-index-strategy-and-events.md` for the exact probe pattern and event-check workflow used in the May 21 session.

---

## Global Indicators (premarket_pulse.py)

Fetched via yfinance each morning:

| Category | Tickers |
|----------|---------|
| US Markets | ^GSPC, ^IXIC, ^DJI, ^VIX |
| Asian Markets | ^N225, ^HSI, 000001.SS |
| India | ^NSEI, ^NSEBANK, ^INDIAVIX |
| Commodities | CL=F (WTI), BZ=F (Brent), GC=F (Gold), SI=F (Silver) |
| Forex | USDINR=X, DX-Y.NYB (DXY) |
| FII Proxy | INDA (iShares MSCI India ETF), EEM |

**Global bias score:** weighted average of all signals → -1.0 (bearish) to +1.0 (bullish)

**Conviction adjustment:** global bias adds ±0.5 to stock conviction scores.
Defensive sectors (Healthcare, FMCG) get boosted in bearish environments;
cyclicals (Metals, Energy, Industrials) get penalized. Add explicit cross-asset sector penalties when a cue directly conflicts with a pick, e.g. falling crude should penalize Energy names even if broad global bias is neutral/bullish.

**Sector implications:** automatic detection of crude/gold/INR/Nasdaq moves
and their impact on relevant sectors (e.g. Nasdaq up → IT tailwind, crude down → paints/aviation boost and Energy caution).

---

## Dependencies

```bash
pip install yfinance ta requests beautifulsoup4 lxml
```

---

## Running Manually

```bash
# Full report (prints to stdout)
python3 ~/.hermes/bin/nse_stock_scanner.py

# Silent mode (cache only, used by 8 AM cron)
python3 ~/.hermes/bin/nse_stock_scanner.py --silent

# Pre-market pulse (reads today's cache + fetches global cues)
python3 ~/.hermes/bin/premarket_pulse.py
```

---

## Updating the Stock Universe

Edit the `UNIVERSE` list in `nse_stock_scanner.py`. Use `.NS` suffix for NSE.
Known broken tickers (as of May 2026): `HDFC.NS` (merged into HDFCBANK),
`TATAMOTORS.NS` (check symbol), `LTIM.NS`, `APL.NS`, `DALMIACEME.NS`, `BERGERPAINTS.NS`.

---

## Updating Sector Scores

Edit `SECTOR_SCORES` dict in `nse_stock_scanner.py` to reflect current macro tailwinds.
Scale is 1–10. Update seasonally or when macro regime shifts.

---

## Pitfalls

- **Google News RSS fallback:** If `web_search` is unavailable or quota-limited, use Google News RSS directly via `requests` + XML parsing for current market-moving headlines.
- **NSE event calendar:** For earnings/board-meeting schedules, call `https://www.nseindia.com/api/event-calendar` with browser-like headers and an initial cookie request to `https://www.nseindia.com`, then filter by date.
- **Intraday strategy discipline:** For chart-reading requests, fetch live 5-minute data and give conditional levels. Do not convert a morning bias into a fresh intraday recommendation without checking opening range, EMAs, RSI, and Bank Nifty confirmation.
- **Cache staleness:** `premarket_pulse.py` rejects cache older than 4 hours.
  If the 8 AM job fails, the pulse will show a warning instead of picks.
- **yfinance rate limits:** scanning 100 stocks takes ~2–3 minutes. Don't reduce
  the universe below ~50 or the ranking loses diversity.
- **Shanghai ticker:** `000001.SS` sometimes returns NaN on yfinance — safe to ignore,
  report handles it gracefully.
- **India VIX:** `^INDIAVIX` has delayed data on yfinance — treat as indicative only.
- **Gift Nifty:** not directly available on yfinance. `^NSEI` (spot) is used as proxy.
  For true Gift Nifty, scrape NSE website or use a paid data provider.
- **FII/DII actual data:** NSE publishes provisional FII/DII data after 6 PM the prior day.
  The INDA ETF is used as a real-time proxy for FII interest direction.
