# Supabase waitlist pattern for landing pages

Use this when a standalone landing page includes a waitlist form and the user wants it connected to Supabase.

## Frontend behavior

- Use the project REST endpoint: `https://<project-ref>.supabase.co/rest/v1/<table>`.
- Use the anon public key only, never the service role key, in browser code.
- Submit with headers:
  - `apikey: <anon key>`
  - `Authorization: Bearer <anon key>`
  - `Content-Type: application/json`
  - `Prefer: return=minimal`
- If duplicate email signups should update instead of erroring, create a unique `email` column and POST to:
  - `/rest/v1/waitlist?on_conflict=email`
  - header `Prefer: resolution=merge-duplicates,return=minimal`
- Keep visitor-facing copy polished. Do not expose internal wording like “prototype stores to localStorage” on a public page unless explicitly requested. Better: “No spam. Early access updates only.”
- A localStorage CSV backup can be useful for local prototypes, but the primary public path should be Supabase once connected.

## Recommended table SQL

```sql
create table if not exists public.waitlist (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  email text not null unique,
  trading_style text not null,
  market text not null,
  created_at timestamptz not null default now()
);

alter table public.waitlist enable row level security;

drop policy if exists "Anyone can join waitlist" on public.waitlist;
create policy "Anyone can join waitlist"
on public.waitlist
for insert
to anon
with check (
  length(trim(name)) > 0
  and email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
);

-- Only add this if the frontend upserts duplicate emails.
drop policy if exists "Anyone can update waitlist row" on public.waitlist;
create policy "Anyone can update waitlist row"
on public.waitlist
for update
to anon
using (true)
with check (
  length(trim(name)) > 0
  and email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
);
```

Do not add public SELECT policies unless the product intentionally exposes signups. The owner can view rows in the Supabase dashboard.

## Verification pattern

Before finalizing:

1. Probe the REST endpoint with `curl` using the anon key.
2. Distinguish these common responses:
   - `401 PGRST301`: usually malformed/wrong JWT or mismatched Authorization/apikey value.
   - `404 PGRST205`: table does not exist or schema cache has not picked it up; provide SQL and ask user to run it.
   - RLS/policy errors: table exists but insert/update policy is missing or too restrictive.
3. Run the local page and submit a test row from the browser.
4. Check console errors and user-facing success/error messages.
5. If the table is not created yet, still wire the frontend and provide the exact SQL setup file/instructions.
