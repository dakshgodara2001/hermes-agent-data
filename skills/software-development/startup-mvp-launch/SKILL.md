---
name: startup-mvp-launch
description: "Use when building or packaging an early startup MVP launch: landing/waitlist pages, Supabase/Vercel persistence and analytics, Telegram-first product loops, and accelerator/pitch application copy."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [startup, mvp, landing-page, waitlist, supabase, vercel, telegram, accelerator, pitch, launch]
    related_skills: [popular-web-designs]
---

# Startup MVP Launch

## Overview

Use this skill for the class of early startup launch work where the user needs to turn a product idea into a credible public surface and first operating loop: positioning, a premium static landing page, a waitlist or early-access form, privacy-safe analytics, lightweight persistence, a channel-first product loop such as Telegram/email, and concise accelerator or grant application copy.

The default target is the narrowest real launch loop, not only a pretty page: proof-oriented positioning, one primary conversion action, durable lead capture, live deployment, and an initial workflow users can actually exercise.

## When to Use

Use for requests like:

- Build or modify a startup landing page, early-access page, or waitlist.
- Add Supabase/PostgREST persistence to a static site.
- Deploy a landing page or serverless MVP to Vercel.
- Add Vercel Web Analytics or privacy-safe conversion telemetry.
- Build a Telegram-first MVP before a full dashboard exists.
- Write or tighten accelerator, grant, pitch-form, or founder-profile answers.
- Rebrand or reposition an early product and update the whole conversion surface.

Do not use this as a substitute for a full product architecture plan, regulated financial/legal advice, or production compliance review. For visually polished one-off HTML, pair it with a design skill such as `popular-web-designs`.

## Core Launch Pattern

1. **Position the wedge**
   - State the category and anti-positioning.
   - Prefer concrete workflow language over hype.
   - For sensitive domains like trading/fintech, avoid profit promises and include education/research/decision-support boundaries.

2. **Ship the static conversion surface**
   - A single static `index.html` is often enough for the first MVP.
   - Keep one primary CTA.
   - Update every conversion surface during rebrands: `<title>`, meta description, nav, hero, cards, form labels, success/duplicate copy, localStorage keys, CSV filenames, disclaimers, footer, analytics/download labels.

3. **Persist signups safely**
   - Use Supabase/PostgREST directly for lightweight static MVPs instead of adding a heavy frontend SDK.
   - Use a unique `email` column if duplicates should collapse.
   - Enable RLS.
   - Add anon insert policies only; do not add public select unless intentionally required.
   - Expose only the anon key in frontend code; keep service-role keys server-side.
   - Treat duplicate email as friendly success-like UX.

4. **Capture one high-signal onboarding answer**
   - Add at most one required high-signal question early.
   - Store it when the migration exists.
   - If deploying before the migration is applied, use graceful fallback so signups do not break.
   - Never send raw free text, emails, names, or financial details to analytics.

5. **Add privacy-safe analytics**
   - Track page views and conversion events: CTA clicked, submit attempted, signup completed, duplicate signup, failed signup, fallback path used.
   - Track only derived metadata for text answers, such as length or selected category.
   - Verify the Vercel analytics script loads in production when used.

6. **Deploy and verify live**
   - Deploy from the project directory, commonly with `npx vercel --prod --yes`.
   - Verify the canonical production URL, not just a preview URL.
   - If the live site looks stale after aliasing, check a cache-busted URL like `?v=<commit-or-slug>` before assuming deploy failure.
   - Browser-check page load, form validation, submit behavior, success/error state, analytics script, and console errors.

7. **Add the first product loop**
   - For channel-first MVPs, Telegram/email/Discord can be the first product surface.
   - For Telegram, use a Vercel/serverless webhook route under `api/` and Supabase session tables keyed by `chat_id`.
   - Persist in-progress sessions separately from completed domain objects.
   - Add a health GET endpoint that reports required env-var presence without exposing values.

## Static Landing + Waitlist Subsection

Use this subsection when the work is mostly a static page plus waitlist form.

Workflow:

1. Inspect current HTML/CSS/JS for form fields, submit handler, persistence, local fallback/export logic, analytics hooks, and deployment target.
2. Prefer surgical edits over introducing a framework when the project is already static.
3. Add fields across HTML labels, accessible names, validation, CSS, JS payload construction, and backup/CSV headers.
4. Keep a full schema file for fresh setup plus a one-time migration for existing deployments.
5. For live Supabase forms, handle missing-column errors such as PostgREST `PGRST204` by retrying without the new optional field and clearly noting the migration still needs to run.
6. Verify locally with a static server, then verify production with the browser and console.
7. If the project is Git-backed and the user asked to update the live site, check status/remote, commit only intended files, push to the deployment branch, and verify deployment.

Supabase/PostgREST checklist:

- Table has unique email where expected.
- RLS is enabled.
- Public insert policy validates required enum-like fields and text length.
- Frontend handles HTTP 409 / Postgres `23505` as a friendly duplicate state.
- Browser anon key is allowed; service-role key is never exposed client-side.

## Telegram-First MVP Subsection

Use this subsection when the first product loop is a Telegram bot or serverless webhook.

Core pattern:

1. Create the bot with `@BotFather` and collect the token outside the skill/memory files.
2. Add a serverless webhook route such as `api/telegram-webhook.js`.
3. Store state in Supabase/Postgres, not process memory. Serverless functions are stateless.
4. Use `TELEGRAM_WEBHOOK_SECRET` and verify Telegram's `X-Telegram-Bot-Api-Secret-Token` header.
5. Add production env vars to Vercel and redeploy after changes.
6. Register the webhook with Telegram `setWebhook` only after env vars and production deployment are ready.
7. Verify `getWebhookInfo`, then send a synthetic POST and confirm persistence.

Typical Telegram command loop:

- `/start` or `/help`: explain the product loop and safety boundaries.
- `/plan`: collect structured pre-action intent.
- `/review`: collect post-action feedback.
- `/cancel`: clear current session.

Vercel env-var pattern:

```bash
printf '%s\n' "$TELEGRAM_BOT_TOKEN" | npx vercel env add TELEGRAM_BOT_TOKEN production
printf '%s\n' "$SUPABASE_URL" | npx vercel env add SUPABASE_URL production
printf '%s\n' "$SUPABASE_SERVICE_ROLE_KEY" | npx vercel env add SUPABASE_SERVICE_ROLE_KEY production
printf '%s\n' "$TELEGRAM_WEBHOOK_SECRET" | npx vercel env add TELEGRAM_WEBHOOK_SECRET production
npx vercel --prod --yes
```

Webhook endpoint checklist:

- GET health check returns configuration booleans, not secret values.
- POST handles Telegram updates.
- Secret validation is optional in dev but required in production when configured.
- Handling is idempotent or harmless for Telegram retries.
- Internal errors are logged; handled updates return `200` to avoid retry storms.

## Accelerator and Pitch Application Subsection

Use this subsection when the user needs paste-ready startup application answers.

Principles:

1. Answer the exact prompt first; do not write generic startup prose.
2. Respect word limits aggressively and state the word count when a limit is given.
3. Lead with strongest proof: shipped products, 0→1 launches, users served, systems built, measurable workflows, or process improvements.
4. Use concrete nouns and active verbs: built, shipped, launched, reduced, scaled, observed, validated.
5. Make the startup feel earned by connecting the founder's background to the problem through lived or professional exposure.
6. Be honest about team composition; do not invent cofounders, advisors, traction, users, metrics, or named experts.
7. Avoid legal and trust risk: do not imply guaranteed returns, proven alpha, private-data access, or regulated advice unless explicitly true and safe.

Team/founder questions:

- If solo, say so directly and make it sound intentional.
- Explain why the founder has the right intersection for the wedge.
- Mention real feedback loops if they exist.
- Acknowledge missing expertise constructively, e.g. actively looking for market/compliance/brokerage-side advisors.

Startup description shape:

1. One-line product definition.
2. Specific problem with current default behavior.
3. What the product does in workflow terms.
4. Why this differs from generic tools.
5. Concrete output or habit loop.

## Verification Checklist

- [ ] Positioning is specific, not feature soup.
- [ ] Sensitive-domain disclaimers are present where needed.
- [ ] Landing form validates required fields and handles duplicates gracefully.
- [ ] Supabase schema/migration and RLS policies match the frontend payload.
- [ ] No service-role key, bot token, webhook secret, email, name, or raw free text is sent to analytics or exposed client-side.
- [ ] Production URL is verified, not only local/preview.
- [ ] Browser console has no errors after loading and exercising the main path.
- [ ] Telegram webhook health, `getMe`, `getWebhookInfo`, synthetic update, and Supabase persistence are verified when applicable.
- [ ] Accelerator answers fit word limits and do not overclaim.

## Common Pitfalls

1. **Breaking live signups during schema changes.** Use fallback inserts for optional new columns and tell the user when migration is still required.
2. **Tracking sensitive data.** Analytics should record event names and derived metadata only.
3. **Forgetting Vercel redeploys.** Serverless functions do not see new env vars until redeployed.
4. **Registering Telegram webhooks too early.** Set the webhook after production env vars and deployment are ready.
5. **Updating only hero copy during rebrands.** Search and update metadata, labels, success states, exports, localStorage keys, disclaimers, and analytics names.
6. **Overclaiming in pitch copy.** High conviction should come from proof and clear thinking, not invented traction or regulated promises.
7. **Stopping at a pretty page.** A real MVP launch should have a captured lead, a verified deployment, and a first product loop or next action.

## References

- `references/tradepilot-waitlist-onboarding.md` — adding a Supabase-backed onboarding question to a static trading landing page.
- `references/rebrand-to-arbiter.md` — full static landing-page rebrand, product metaphor, copy surfaces, deploy, and cache-busted verification.
- `references/tradepilot-landing-telegram-mvp.md` — TradePilot static waitlist page, Supabase migrations, Vercel analytics, and Telegram accountability webhook.
- `references/tradepilot-telegram-mvp.md` — Vercel webhook + Supabase tables + Telegram accountability-loop verification.
- `references/arbiter-application-positioning.md` — Arbiter-specific accelerator application positioning notes.
