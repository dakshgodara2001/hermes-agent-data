---
name: serverless-telegram-bots
description: Build and operate Telegram bot webhooks on serverless platforms such as Vercel, with Supabase persistence and safe webhook verification.
version: 1.0.0
platforms: [linux, macos, windows]
tags: [telegram, bot, webhook, vercel, serverless, supabase, postgres, mvp]
---

# Serverless Telegram Bots

Archived during umbrella consolidation into `startup-mvp-launch`.

Use this skill when building or troubleshooting a Telegram bot that receives updates via webhook on Vercel/serverless functions and stores state in Supabase/Postgres.

Typical use cases include Telegram-first MVPs, accountability/check-in bots, lead qualification flows, trade planning or journaling bots, and lightweight command bots backed by Supabase.

## Core pattern

1. Create a Telegram bot with `@BotFather` and collect the bot token.
2. Add a serverless webhook route, e.g. `api/telegram-webhook.js` on Vercel.
3. Store bot state in Supabase tables, not process memory.
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

## Webhook endpoint checklist

- GET health check returns whether required env vars are configured, without exposing values.
- POST handles Telegram updates.
- Optional secret validation via `X-Telegram-Bot-Api-Secret-Token`.
- Idempotent or harmless handling for retried updates.
- Log internal errors but return `200` when handled enough to avoid retry storms.

## Supabase persistence pattern

Use separate tables for sessions/current conversation state and completed domain objects. Enable RLS and create no public policies for private bot tables. The serverless webhook writes with `SUPABASE_SERVICE_ROLE_KEY`, which bypasses RLS. Never expose the service role key in frontend JS. Use `chat_id` as text.

## Security pitfalls

- Rotate pasted tokens or service keys after testing.
- Do not store bot tokens, service role keys, or webhook secrets in skill files, memory, checked-in docs, or frontend code.
- Use a random secret such as `openssl rand -hex 32`.
- Avoid `curl | python` or `curl | bash` patterns.

## References

- `references/tradepilot-telegram-mvp.md`
