# TradePilot Telegram MVP reference

This reference captures the reusable pattern from building a Telegram-first accountability-loop MVP for a static Vercel landing page backed by Supabase.

## Product shape

The bot deliberately avoided financial tips. It acted as a process/accountability tool:

- `/start` or `/help` explains the loop.
- `/plan` collects a rule-based trade plan before entry.
- `/review` collects a post-market review.
- `/cancel` clears the current flow.

For trading products, keep the bot SEBI/financial-advice safe: capture context, risk, invalidation, and review notes; do not produce personalized buy/sell advice.

## Minimal Supabase schema

Private tables with RLS enabled and no public policies:

```sql
create table if not exists public.telegram_sessions (
  chat_id text primary key,
  telegram_user_id text,
  username text,
  mode text not null check (mode in ('plan', 'review')),
  step integer not null default 0,
  answers jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

create table if not exists public.telegram_trade_plans (
  id uuid primary key default gen_random_uuid(),
  chat_id text not null,
  telegram_user_id text,
  username text,
  symbol text not null,
  timeframe text not null,
  setup text not null,
  entry_plan text not null,
  risk_plan text not null,
  target_plan text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.telegram_reviews (
  id uuid primary key default gen_random_uuid(),
  chat_id text not null,
  telegram_user_id text,
  username text,
  review_text text not null,
  created_at timestamptz not null default now()
);

alter table public.telegram_sessions enable row level security;
alter table public.telegram_trade_plans enable row level security;
alter table public.telegram_reviews enable row level security;
```

The Vercel function writes with `SUPABASE_SERVICE_ROLE_KEY`; never expose that key to client-side JavaScript.

## Serverless implementation notes

- Use `chat.id` as the session key.
- Store `answers` as JSONB while stepping through multi-question flows.
- On each answer, update the session with `on_conflict=chat_id`.
- On the final answer, insert the completed object and delete the session.
- For a one-message `/review`, create a review session first, then persist the next user message as `review_text`.

## Verification sequence used

1. Add Vercel env vars via stdin:
   - `TELEGRAM_BOT_TOKEN`
   - `SUPABASE_URL`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `TELEGRAM_WEBHOOK_SECRET`
2. Redeploy with `npx vercel --prod --yes`.
3. Visit the webhook `GET` health endpoint and confirm configured flags are true.
4. Register Telegram webhook with `setWebhook` and `secret_token`.
5. Confirm `getWebhookInfo` has the expected URL, zero/low pending updates, and no `last_error_message`.
6. Send a synthetic Telegram update using the secret header:

```bash
curl -sS "$WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -H "X-Telegram-Bot-Api-Secret-Token: $TELEGRAM_WEBHOOK_SECRET" \
  -d '{"update_id":100000,"message":{"message_id":1,"from":{"id":123456789,"is_bot":false,"first_name":"Test","username":"test_user"},"chat":{"id":123456789,"type":"private"},"date":1778990000,"text":"/plan"}}'
```

7. Step through synthetic answers and query Supabase for the expected row.
8. Delete test rows by `chat_id` when done.

## Gotchas learned

- Vercel env vars being present in the dashboard is not enough; redeploy production before testing the function.
- The webhook `GET` endpoint is useful for verifying secrets are configured without leaking them.
- Telegram webhook registration should include `allowed_updates` to keep the bot focused and lower noise.
- If credentials are pasted into a chat or logs during setup, tell the user to rotate them after testing.
- Avoid saving service keys in docs or code snippets. Use placeholders in durable references.
