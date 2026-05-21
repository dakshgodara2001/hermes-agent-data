---
name: static-landing-waitlists
description: Build static landing pages with waitlist forms, Supabase/PostgREST persistence, privacy-safe analytics, and Vercel deployment.
version: 1.0.0
author: Hermes Agent
tags: [landing-page, waitlist, supabase, vercel, analytics, static-site, forms]
platforms: [linux, macos, windows]
triggers:
  - landing page waitlist
  - add waitlist form
  - connect supabase to static site
  - deploy landing page to vercel
  - add onboarding question
  - collect early access signups
  - privacy-safe analytics
---

# Static Landing Waitlists

Archived during umbrella consolidation into `startup-mvp-launch`.

Use this skill when building or modifying a static landing page that collects early-access or waitlist signups, especially with Supabase/PostgREST and Vercel.

## Core principles

1. Preserve conversion flow first. Do not break the signup path while backend migrations are pending.
2. Keep the frontend lightweight for MVPs: static HTML/CSS/JS is enough until the product needs auth or a dashboard.
3. Treat analytics as product telemetry, not surveillance. Track CTA/form states and non-sensitive metadata; do not send free-text answers, emails, names, or financial details to analytics.
4. For fintech/trading products, avoid profit-hype. Include education/research/decision-support disclaimers and avoid claiming personalized financial advice.
5. Verify both local behavior and deployed production behavior before declaring done.
6. For naming/rebrand passes, update the full conversion surface, not just the hero: `<title>`, meta description, nav labels, hero, preview cards, waitlist success/duplicate text, CSV filenames, localStorage keys, disclaimers, footer, and any analytics/download labels.

## Standard workflow

1. Inspect current files: form fields, submit handler, persistence, local backup/export logic, analytics hooks, and deployment target.
2. Add or modify form fields across HTML labels, validation, CSS, JavaScript payload construction, and local backup/CSV headers.
3. Keep a full schema file for fresh setup plus one-time migration files for existing deployments.
4. Avoid schema-migration downtime with graceful fallback for missing-column errors such as PostgREST `PGRST204`.
5. Add privacy-safe analytics that never includes raw emails, names, free-text answers, or financial details.
6. Verify locally with a static server.
7. Deploy and verify production, including cache-busted URL if needed.
8. Commit and push intended files when the project is Git-backed and the user asked for a live update.

## Supabase/PostgREST checklist

- Table has a unique `email` if duplicate signups should be prevented.
- RLS is enabled.
- Public insert policy allows anonymous inserts but does not add public SELECT unless intentionally needed.
- Insert policy validates required enum-like fields and text length.
- Frontend handles HTTP 409 / Postgres `23505` as friendly duplicate signup state.
- If using a browser anon key, only expose the anon key, never a service-role key.

## Vercel analytics checklist

- Inject the Vercel Web Analytics script if the project uses Vercel Analytics.
- Use a guarded helper such as `trackEvent(name, properties)`.
- Verify `/_vercel/insights/script.js` loads in production.

## References

- `references/tradepilot-waitlist-onboarding.md`
- `references/rebrand-to-arbiter.md`
