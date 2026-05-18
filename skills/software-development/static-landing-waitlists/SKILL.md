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

Use this skill when building or modifying a static landing page that collects early-access or waitlist signups, especially with Supabase/PostgREST and Vercel.

## Core principles

1. Preserve conversion flow first. Do not break the signup path while backend migrations are pending.
2. Keep the frontend lightweight for MVPs: static HTML/CSS/JS is enough until the product needs auth or a dashboard.
3. Treat analytics as product telemetry, not surveillance. Track CTA/form states and non-sensitive metadata; do not send free-text answers, emails, names, or financial details to analytics.
4. For fintech/trading products, avoid profit-hype. Include education/research/decision-support disclaimers and avoid claiming personalized financial advice.
5. Verify both local behavior and deployed production behavior before declaring done.
6. For naming/rebrand passes, update the full conversion surface, not just the hero: `<title>`, meta description, nav labels, hero, preview cards, waitlist success/duplicate text, CSV filenames, localStorage keys, disclaimers, footer, and any analytics/download labels.

## Standard workflow

1. Inspect current files.
   - Identify the form fields, submit handler, persistence mechanism, local backup/export logic, analytics hooks, and deployment target.
   - If the project is static HTML, prefer surgical edits rather than introducing a framework.

2. Add or modify form fields.
   - Update HTML labels, required/minlength/maxlength validation, and accessible names.
   - Update CSS for new controls such as textarea.
   - Update JavaScript payload construction.
   - Update local backup/CSV headers if the app exports backup data.

3. Update backend schema separately.
   - Keep a full schema file for fresh setup.
   - Add a one-time migration file for existing deployments.
   - For Supabase with RLS, update insert policies to validate new required fields.

4. Avoid schema-migration downtime.
   - If adding a new Supabase column to a live form, consider a temporary graceful fallback: try the new payload first, detect missing-column errors such as PostgREST `PGRST204` or error text mentioning the column, then retry without the new field.
   - Track that fallback as a non-sensitive analytics event so the owner knows the migration is still needed.
   - Clearly tell the user that the form works but the new field will not persist until the migration runs.

5. Add privacy-safe analytics.
   - Track events such as CTA clicked, submit attempted, signup completed, duplicate email, signup failed.
   - For free-text onboarding questions, only track derived metadata such as answer length or category selected by the user. Never send the answer text to analytics.

6. Verify locally.
   - Serve the site with a local static server.
   - Use the browser to confirm the field appears and native validation works.
   - Submit a test signup and inspect success/error UI plus browser console errors.

7. Deploy and verify production.
   - Deploy with the project’s established deployment tool, often `npx vercel --prod --yes`.
   - Open the canonical production URL, not only the preview URL.
   - If production still appears stale after a successful alias, also verify with a cache-busted URL such as `?v=<commit-or-slug>` before assuming the deployment failed.
   - Confirm new UI exists, analytics script loads if relevant, form submission succeeds, and no console errors appear.

8. Commit and push if the project is Git-backed and the user asked to update the live website.
   - Check `git status`/remote first.
   - Commit only the intended files.
   - Push to the deployment branch and trigger the production deploy if auto-deploy has not picked it up.

## Supabase/PostgREST checklist

- Table has a unique `email` if duplicate signups should be prevented.
- RLS is enabled.
- Public insert policy allows anonymous inserts but does not add public SELECT unless intentionally needed.
- Insert policy validates required enum-like fields and text length.
- Frontend handles HTTP 409 / Postgres `23505` as a friendly duplicate signup state.
- If using a browser anon key, only expose the anon key, never a service-role key.

## Vercel analytics checklist

- Inject the Vercel Web Analytics script if the project uses Vercel Analytics.
- Use a helper such as `trackEvent(name, properties)` and guard for `typeof window.va === 'function'`.
- Verify `/_vercel/insights/script.js` loads in production.
- Remember custom events may depend on account plan; hooks can still be added safely.

## References

- `references/tradepilot-waitlist-onboarding.md` — concrete example of adding a Supabase-backed onboarding question to a static trading landing page.
- `references/rebrand-to-arbiter.md` — concrete example of a full static landing-page rebrand, including product metaphor, copy surfaces, localStorage/CSV names, deploy, and cache-busted verification.
