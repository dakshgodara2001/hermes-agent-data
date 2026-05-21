# TradePilot landing + Telegram MVP session pattern

This reference captures the reusable pattern from building TradePilot, an agentic trading copilot landing page for NSE/BSE retail traders.

## Product positioning

- Core line: “Not tips. A trading framework.”
- Category: agentic trading discipline/copilot for Indian markets.
- Safety posture: educational, research-led, decision-support only; not SEBI-registered investment advice and no guaranteed returns.
- First product loop: plan before entry, define invalidation, review after market.

## Static landing MVP structure

Project shape:

```text
agentic-trading-landing/
  index.html
  api/telegram-webhook.js
  supabase-waitlist.sql
  supabase-add-biggest-struggle.sql
  supabase-telegram-mvp.sql
  TELEGRAM_MVP.md
```

Use a single `index.html` for rapid iteration when the MVP does not need a framework yet. For premium fintech pages, use a dark visual system with:

- Sticky header.
- Hero with clear anti-positioning.
- Product preview card.
- Framework cards.
- Sandbox/product-loop section.
- Waitlist form.
- Disclaimer.

## Supabase waitlist pattern

Table fields used:

```sql
id uuid primary key default gen_random_uuid(),
name text not null,
email text not null unique,
trading_style text not null,
market text not null,
biggest_struggle text,
created_at timestamptz not null default now()
```

RLS pattern:

- Enable RLS.
- Add `insert` policy for `anon` only.
- Validate name, email regex, enumerated trading style, enumerated market.
- Avoid public `select`.

Frontend insert pattern:

- Direct PostgREST `POST /rest/v1/waitlist` with anon key.
- `Prefer: return=minimal`.
- Duplicate email: treat HTTP 409 / Postgres `23505` as friendly “already on waitlist”.
- Keep `localStorage` backup and CSV export.

## Adding an onboarding question safely

When adding `biggest_struggle` after launch:

1. Add required textarea to the page with `minlength` and `maxlength`.
2. Add field to local CSV backup.
3. Send analytics metadata only, e.g. `struggle_length`; do not send raw answer text.
4. Create a migration file for Supabase.
5. If you cannot run the migration yourself, add a fallback insert path without the new field so live signups continue to work.
6. Tell the user clearly that Supabase will not persist the new answer until the migration is run.

Fallback detection used:

- `PGRST204`, or
- error text mentioning the missing column name.

## Vercel analytics pattern

Frontend snippet:

```html
<script>
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

Event helper:

```js
function trackEvent(name, properties = {}) {
  if (typeof window.va === 'function') {
    window.va('event', name, properties);
  }
}
```

Track button clicks and waitlist outcomes, but avoid personal data and free text.

## Telegram-first MVP webhook pattern

Vercel serverless file:

```text
api/telegram-webhook.js
```

Env vars:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_WEBHOOK_SECRET`
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`

Health GET endpoint should return booleans only:

```json
{
  "ok": true,
  "service": "tradepilot-telegram-webhook",
  "configured": {
    "telegram_bot_token": true,
    "supabase_service_role_key": true,
    "telegram_webhook_secret": true
  }
}
```

Webhook safety:

- If `TELEGRAM_WEBHOOK_SECRET` is configured, require `x-telegram-bot-api-secret-token`.
- Return HTTP 200 even for internal handling errors so Telegram does not repeatedly hammer the endpoint while debugging.
- Log server-side errors with `console.error`.

Bot commands:

- `/start` or `/help`: explain the loop and safety boundary.
- `/plan`: collect symbol, timeframe, setup, entry plan, invalidation/stop, exit logic.
- `/review`: collect post-market review text.
- `/cancel`: clear current session.

Supabase tables:

- `telegram_sessions`: keyed by `chat_id`, stores mode, step, answers JSON.
- `telegram_trade_plans`: completed plans.
- `telegram_reviews`: post-market review notes.

Use service role key from the serverless function only. Do not expose it in frontend JS.

## Deployment and activation sequence

1. Write/patch files.
2. Check JS syntax: `node --check api/telegram-webhook.js`.
3. Deploy: `npx vercel --prod --yes`.
4. Visit production page and verify content.
5. Visit webhook GET health endpoint.
6. Add Vercel env vars.
7. Redeploy.
8. Register Telegram webhook with `setWebhook` and `secret_token`.
9. Test `/start`, `/plan`, `/review` in Telegram.

## Common activation commands

```bash
npx vercel env add TELEGRAM_BOT_TOKEN production
npx vercel env add SUPABASE_URL production
npx vercel env add SUPABASE_SERVICE_ROLE_KEY production
npx vercel env add TELEGRAM_WEBHOOK_SECRET production
npx vercel --prod --yes
```

```bash
curl -sS "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setWebhook" \
  -H 'Content-Type: application/json' \
  -d "{\"url\":\"${WEBHOOK_URL}\",\"secret_token\":\"${TELEGRAM_WEBHOOK_SECRET}\",\"allowed_updates\":[\"message\"]}"
```
