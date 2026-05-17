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

1. Define positioning
   - State the category and the anti-positioning.
   - Example: “Not tips. A trading framework.”
   - Keep the page outcome-specific, not feature soup.

2. Build the static page first
   - Prefer a single `index.html` for the first MVP if the user wants speed.
   - Use a premium design system skill if visual taste matters, e.g. `popular-web-designs`.
   - Include disclaimers for regulated/sensitive domains.

3. Add waitlist persistence
   - Use Supabase PostgREST directly for a one-page MVP instead of adding a heavy SDK.
   - Create a table with a unique `email` column.
   - Enable RLS.
   - Add only an anon `insert` policy; do not add public `select`.
   - Handle duplicate email as a friendly success-like state.
   - Keep a localStorage CSV fallback for quick recovery and testing.

4. Add onboarding signal capture
   - Add one high-signal question after basic lead fields.
   - Store it in Supabase when the migration exists.
   - If deploying before the migration is run, use graceful fallback so signups do not break.
   - Do not send raw free-text answers to analytics; send only metadata like answer length.

5. Add analytics
   - Use Vercel Web Analytics for a Vercel-hosted static MVP.
   - Track page views and key conversion events.
   - For privacy, avoid sending raw emails, names, or free-text answers.
   - Verify the analytics script loads on production.

6. Deploy and verify
   - Deploy with `npx vercel --prod --yes` from the project directory.
   - Verify the canonical production URL, not only the preview URL.
   - Browser-check: page loads, form exists, required fields validate, submit path succeeds/fails gracefully, and console has no errors.

7. Add the first product loop
   - For a Telegram-first MVP, add a Vercel serverless webhook under `api/`.
   - Store state in a Supabase session table keyed by Telegram `chat_id`.
   - Store completed artifacts in separate tables, e.g. trade plans and reviews.
   - Use service role key only server-side in Vercel env vars.
   - Add a health GET endpoint that reports whether required env vars are configured, without exposing values.

## Telegram-first MVP pattern

For early-stage products, Telegram can be the first product surface:

- `/start` or `/help`: explain the loop and safety boundaries.
- `/plan`: collect structured pre-action intent.
- `/review`: collect post-action feedback.
- `/cancel`: clear current session.

Implementation notes:

- Use a serverless function like `api/telegram-webhook.js`.
- Verify Telegram webhook requests with `x-telegram-bot-api-secret-token` when `TELEGRAM_WEBHOOK_SECRET` is configured.
- Use Supabase service role key server-side to bypass RLS; never expose it in frontend JS.
- Keep frontend waitlist anon key separate from server-side service role key.
- Persist in-progress sessions separately from completed records.

## Pitfalls

- Do not claim Supabase persistence works for a newly added column until the SQL migration has actually been run.
- If the user is not logged into Supabase, create a migration file and clearly state it must be run manually.
- Avoid breaking live signups when adding optional onboarding columns; use fallback insert if the column is missing.
- Do not send sensitive lead data or free-text answers to analytics.
- Vercel env vars require redeploy before serverless functions see them.
- `setWebhook` should be run only after env vars and the production deployment are ready.

## Verification checklist

- `node --check api/<webhook>.js` for serverless JS syntax.
- Production landing page loads.
- Production page includes new sections/forms.
- Form validates required fields.
- Submit flow succeeds or fails gracefully with a useful message.
- `/_vercel/insights/script.js` loads if using Vercel Analytics.
- Webhook GET health endpoint responds and reports configuration booleans.
- No browser console errors after loading and testing the page.

## References

- `references/tradepilot-landing-telegram-mvp.md` — concrete session pattern for TradePilot: static waitlist page, Supabase migration files, Vercel analytics, and Telegram accountability webhook.
