# Static landing pages with waitlist backends

Use this reference when building/deploying a one-page landing page with an email/waitlist form.

## Recommended workflow

1. Build a self-contained HTML/CSS/JS landing page first.
2. Keep the first waitlist implementation frontend-simple, but do not leave it as a fake form:
   - Supabase REST is enough for MVP waitlists.
   - Use the public anon key only, never the service-role key.
   - Keep Row Level Security enabled.
3. Create a dedicated `waitlist` table, usually:
   - `id uuid primary key default gen_random_uuid()`
   - `name text not null`
   - `email text not null unique`
   - `trading_style text` or other qualification field
   - `market text` or audience segment field
   - `created_at timestamptz not null default now()`
4. Add only an INSERT policy for anonymous site visitors unless there is a real need for public reads or updates.
   - Do not add public SELECT for a waitlist.
   - Avoid frontend upsert unless you intentionally add safe UPDATE policies.
5. In frontend code:
   - `POST ${SUPABASE_URL}/rest/v1/waitlist`
   - headers: `apikey`, `Authorization: Bearer <anon key>`, `Content-Type: application/json`, `Prefer: return=minimal`
   - treat duplicate email errors (`409` or Postgres code `23505`) as a friendly success-like state: “You’re already on the waitlist.”
6. Verify in two layers:
   - direct `curl` to Supabase REST should return HTTP 201
   - browser form on the deployed site should show success and produce no console errors
7. Deploy static pages with Vercel when the user asks for a quick public URL:
   - `npx vercel login` if needed
   - decline optional plugin prompts unless user asked for them
   - `npx vercel --prod --yes`
   - open the final `*.vercel.app` URL and submit a real test signup
8. Add analytics before considering the landing page ready for iteration:
   - page views via Vercel Web Analytics when deployed on Vercel
   - CTA click events for header/hero/button variants
   - waitlist attempt/completion/duplicate/failure events
   - no PII in event payloads
   - see `references/static-landing-analytics.md`

## Supabase pitfall

If the frontend uses `on_conflict=email` with `Prefer: resolution=merge-duplicates`, Supabase treats it as an upsert. With RLS enabled, this requires UPDATE policies and can fail with `42501 new row violates row-level security policy`. For a waitlist MVP, prefer simple INSERT plus friendly duplicate-email handling.

## UX copy pattern

For serious financial/trading products, avoid hype copy and fake promise language. Prefer:
- “decision-support”
- “educational research”
- “risk-aware”
- “not personalized financial advice”
- “not tips; a framework”

After signup:
- new email: “You’re on the waitlist. I’ll send early access updates when [product] opens up.”
- duplicate email: “You’re already on the waitlist. I’ll send early access updates when [product] opens up.”
