---
name: serverless-telegram-bots
description: Build and operate Telegram bot webhooks on serverless platforms such as Vercel, with Supabase persistence and safe webhook verification.
version: 1.0.0
platforms: [linux, macos, windows]
tags: [telegram, bot, webhook, vercel, serverless, supabase, postgres, mvp]
---

# Serverless Telegram Bots

Use this skill when building or troubleshooting a Telegram bot that receives updates via webhook on Vercel/serverless functions and stores state in Supabase/Postgres.

Typical use cases:
- Telegram-first MVPs
- Accountability/check-in bots
- Lead qualification flows
- Trade planning or journaling bots
- Lightweight command bots backed by Supabase

## Core pattern

1. Create a Telegram bot with `@BotFather` and collect the bot token.
2. Add a serverless webhook route, e.g. `api/telegram-webhook.js` on Vercel.
3. Store bot state in Supabase tables, not process memory. Serverless functions are stateless.
4. Use a `TELEGRAM_WEBHOOK_SECRET` and verify Telegram's `X-Telegram-Bot-Api-Secret-Token` header.
5. Add production env vars to Vercel.
6. Redeploy after env var changes.
7. Register the webhook with Telegram's `setWebhook` endpoint.
8. Verify `getWebhookInfo`, then run a synthetic POST through the webhook and confirm persistence.

## Vercel env vars

Use stdin so secrets are not echoed interactively:

```bash
printf '%s\n' "$TELEGRAM_BOT_TOKEN" | npx vercel env add TELEGRAM_BOT_TOKEN production
printf '%s\n' "$SUPABASE_URL" | npx vercel env add SUPABASE_URL production
printf '%s\n' "$SUPABASE_SERVICE_ROLE_KEY" | npx vercel env add SUPABASE_SERVICE_ROLE_KEY production
printf '%s\n' "$TELEGRAM_WEBHOOK_SECRET" | npx vercel env add TELEGRAM_WEBHOOK_SECRET production
npx vercel --prod --yes
```

Important: Vercel env vars do not affect already-deployed functions. Always redeploy after adding or changing them.

If an env var already exists, use Vercel's remove/pull/update flow or the dashboard; do not blindly create duplicates.

## Webhook endpoint checklist

The webhook route should support:
- `GET` health check returning whether required env vars are configured, without exposing values.
- `POST` for Telegram updates.
- optional secret validation via `X-Telegram-Bot-Api-Secret-Token`.
- idempotent or harmless handling for retried Telegram updates where possible.
- logging internal errors, but responding `200` to Telegram if the update was handled enough to avoid retry storms.

## Supabase persistence pattern

Use separate tables for:
- sessions / current conversation state (`chat_id`, `mode`, `step`, `answers`, `updated_at`)
- completed domain objects (plans, reviews, leads, etc.)

Enable RLS and create no public policies for private bot tables. The serverless webhook should write with `SUPABASE_SERVICE_ROLE_KEY`, which bypasses RLS. Never expose the service role key in frontend JS.

Use `chat_id` as text, not integer, to avoid cross-language integer edge cases and to support group IDs.

For session upserts via PostgREST:

```js
await fetch(`${SUPABASE_URL}/rest/v1/telegram_sessions?on_conflict=chat_id`, {
  method: 'POST',
  headers: {
    apikey: SUPABASE_SERVICE_ROLE_KEY,
    Authorization: `Bearer ${SUPABASE_SERVICE_ROLE_KEY}`,
    'Content-Type': 'application/json',
    Prefer: 'resolution=merge-duplicates,return=representation'
  },
  body: JSON.stringify(session)
});
```

## Register Telegram webhook

```bash
curl -sS "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/setWebhook" \
  -H 'Content-Type: application/json' \
  -d "{\"url\":\"${WEBHOOK_URL}\",\"secret_token\":\"${TELEGRAM_WEBHOOK_SECRET}\",\"allowed_updates\":[\"message\"]}"
```

Then verify:

```bash
curl -sS "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getWebhookInfo"
```

Check at least:
- `ok: true`
- `result.url` is the deployed webhook route
- `pending_update_count` is reasonable
- `last_error_message` is absent/null
- `allowed_updates` contains expected update types

## Verification workflow

1. Hit the webhook `GET` health endpoint and confirm configured flags are true.
2. Call Telegram `getMe` to confirm the bot token maps to the expected username.
3. Send a synthetic Telegram update to the webhook with the secret header.
4. Query Supabase with the service role key to confirm the session/object row was written.
5. Complete a full flow with synthetic answers.
6. Clean up synthetic rows by test `chat_id`.
7. Ask the user to test `/start`, `/plan`, or the relevant commands from the real Telegram client.

## Security pitfalls

- If a token or service key is pasted into chat/logs, recommend rotation after testing.
- Do not store bot tokens, service role keys, or webhook secrets in skill files, memory, checked-in docs, or frontend code.
- Use a random secret, e.g. `openssl rand -hex 32`.
- Avoid `curl | python` or `curl | bash` patterns. If parsing JSON from curl, save to a file first or use a safe parser command that does not execute downloaded content.

## References

- `references/tradepilot-telegram-mvp.md` — concrete session pattern: Vercel webhook + Supabase tables + Telegram accountability-loop verification.
