# TradePilot Decision Card Live Paper-Test Pattern

Use this reference when taking a trading decision-card engine from code-complete to a real-market paper test.

## Trigger

The user wants to test a decision-support/agentic trading framework on the actual market session, not just run unit tests or demo payloads.

## Workflow

1. **Verify code health first**
   - Run the project test suite for the decision engine/API.
   - Confirm the API accepts market/candidate/user payloads and returns a card with decision, risk gate, audit trail, and disclaimer.

2. **Check market data freshness**
   - Read the scanner cache and inspect `generated_at`.
   - If stale, rerun the silent scanner before generating cards.
   - Do not use prior-session picks for a live test unless the user explicitly asks for backtesting.

3. **Build live card inputs**
   - Use current broad-market inputs: Nifty/Gift proxy, US close, Asia, crude, and VIX.
   - Map each scanner pick into a candidate payload:
     - symbol
     - style: momentum / swing / long-term / watchlist
     - fundamentals score + notes
     - technical trend, RSI, 20-day return, intraday range
     - sentiment/sector alignment
     - stop/invalidation proxy
   - Preserve high-volatility and overextension warnings as bear-thesis or risk-gate inputs.

4. **Interpret risk-off days correctly**
   - If the market regime is risk-off, all or most cards may return `WAIT`.
   - This is still a real test: it tests discipline and capital protection, not stock-picking excitement.
   - Do not override the engine to force actionable longs. Instead, save the decisions and evaluate after close.

5. **Persist the test set**
   - Save a machine-readable JSON file containing:
     - test date/time
     - market inputs
     - decision cards
     - key evidence/risk fields
     - review plan
   - Use a predictable path such as `~/.hermes/cache/tradepilot_decision_card_test_YYYY-MM-DD.json`.

6. **Schedule or run post-market calibration**
   - After close, compare each symbol’s test price/open/close/high/low.
   - Judge whether `WAIT` avoided bad longs or missed exceptional setups.
   - If logic gaps are found, patch the decision engine or scanner immediately and rerun tests.

## Output Style

For Telegram, keep it direct:

- State whether live testing started.
- State code/test status.
- State current market regime.
- List each card with symbol + decision + one-line reason.
- Emphasize that `WAIT` can be a valid live-test outcome.
- Include the saved cache path and post-market review timing if scheduled.
- Include a non-advice disclaimer.

## Pitfalls

- Avoid framing a risk-off `WAIT` result as failure or inaction.
- Avoid using stale scanner data just because it is available.
- Avoid over-explaining implementation details to the user during market hours; give the actionable state first.
- Avoid hard-coding a dependency failure as a durable rule. If a generic runtime lacks a finance library, use the existing scanner/project runtime that already fetches market data.
