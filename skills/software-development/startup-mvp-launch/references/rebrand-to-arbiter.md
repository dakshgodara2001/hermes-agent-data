# Rebrand pass example: TradePilot → Arbiter

Use this as a compact checklist for renaming a static landing-page product without leaving stale brand references.

## Context

A trading waitlist landing page was renamed from `TradePilot` to `Arbiter`. The stronger positioning was not only a name swap; it shifted the narrative from generic trading copilot to a decision/courtroom metaphor:

- Hero: `Put every trade on trial.`
- Product category: `agentic decision system for Indian traders`
- Product promise: test every trade before entry through bull case, bear case, risk, market context, and trader behavior.
- Avoided framing: tips app, auto-trader, profit machine, signal group.

## Files/surfaces updated

- `index.html` brand text and nav accessible label.
- `<title>` and meta description.
- Hero eyebrow, headline, subcopy, proof chips.
- Product preview labels: `arbiter.agent`, `Verdict`, `Arbiter asks`.
- Framework copy: process, debate, restraint, decision review.
- Telegram loop copy: accountability loop, put the trade on trial before entry.
- Waitlist heading/lead/principles/disclaimer.
- Success and duplicate-email messages.
- Download filename: `arbiter-waitlist.csv`.
- Browser local backup key: `arbiter_waitlist`.
- Footer.

## Verification pattern

1. Search the landing page for old brand variants (`TradePilot`, `tradepilot`, spaced/cased variants).
2. Run the project test suite if present.
3. Serve locally and inspect via browser snapshot; check console errors.
4. Commit/push only intended edits.
5. Deploy production with the project tool (`npx vercel --prod --yes` in this case).
6. Verify the canonical URL; if stale content appears immediately after aliasing, open a cache-busted URL like `?v=<commit>` to distinguish CDN/cache lag from deployment failure.

## Naming lesson

For behavior/risk products, generic names like `TradePilot` can sound like a normal broker feature. Stronger names often come from a product metaphor:

- `Arbiter`: judge between bull case, bear case, and risk case.
- `TradeCourt`: put every trade on trial.
- `NoEntry`: the AI that tells traders when not to trade.

Translate the metaphor into the page copy, not just the logo.
