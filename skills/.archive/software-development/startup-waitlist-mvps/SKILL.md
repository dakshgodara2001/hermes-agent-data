---
name: startup-waitlist-mvps
description: "Build lean startup MVP launch surfaces: premium static landing pages, waitlists, Supabase persistence, Vercel deployment/analytics, and lightweight channel-first product loops."
version: 1.0.0
author: Hermes Agent
tags: [startup, landing-page, waitlist, supabase, vercel, telegram, mvp, product]
platforms: [linux, macos, windows]
triggers:
  - build a startup landing page
  - make a waitlist page
  - add supabase waitlist
  - deploy landing page to vercel
  - add vercel analytics
  - build telegram-first MVP
  - productize a waitlist
  - early access page
---

# Startup Waitlist MVPs

Archived during umbrella consolidation into `startup-mvp-launch`.

Use this skill when building or iterating on a startup MVP surface: a focused landing page, waitlist capture, analytics, and the first lightweight product loop before a full app exists.

## Core principle

Ship the narrowest real loop, not just a pretty page:

1. Clear positioning and safety boundaries.
2. Premium landing page with one primary action.
3. Persistent waitlist storage.
4. Privacy-conscious analytics.
5. A channel-first MVP loop, usually Telegram/email/Discord, before a full dashboard.
6. Verification on the live deployment.

## Recommended workflow

1. Define positioning and anti-positioning.
2. Build the static page first, often as a single `index.html`.
3. Add waitlist persistence through Supabase/PostgREST, RLS, anon insert policy, duplicate handling, and localStorage CSV fallback.
4. Add one high-signal onboarding question with graceful fallback if migration is not yet run.
5. Add Vercel Web Analytics without sending raw PII or free-text answers.
6. Deploy with `npx vercel --prod --yes` and verify canonical production URL.
7. Add first product loop, commonly Telegram via `api/telegram-webhook.js` and Supabase session/completed-object tables.

## Telegram-first MVP pattern

Commands commonly include `/start`, `/help`, `/plan`, `/review`, and `/cancel`. Verify webhook requests with `x-telegram-bot-api-secret-token` when configured. Keep frontend waitlist anon key separate from server-side service-role key.

## Pitfalls

- Do not claim Supabase persistence works for a newly added column until the SQL migration has actually been run.
- If the user is not logged into Supabase, create a migration file and clearly state it must be run manually.
- Avoid breaking live signups when adding optional onboarding columns.
- Do not send sensitive lead data or free-text answers to analytics.
- Vercel env vars require redeploy before serverless functions see them.
- `setWebhook` should be run only after env vars and the production deployment are ready.

## References

- `references/tradepilot-landing-telegram-mvp.md`
