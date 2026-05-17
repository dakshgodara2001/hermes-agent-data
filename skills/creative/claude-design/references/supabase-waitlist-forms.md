# Supabase-backed waitlist forms for landing-page prototypes

Use this when a designed landing page needs a real waitlist backend but the artifact is still a static HTML/CSS/JS page.

## Recommended MVP shape

- Use Supabase REST API directly from the frontend with the project's **anon public key** only.
- Never embed the service role key in frontend code.
- Create a `public.waitlist` table with row-level security enabled.
- For a simple MVP, prefer plain `insert` over `upsert` unless you have deliberately added update policies.
- Keep a local browser backup/CSV export only as a convenience, not as the primary source of truth.

## Table shape

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
```

## Minimal insert policy

```sql
drop policy if exists "Anyone can join waitlist" on public.waitlist;
create policy "Anyone can join waitlist"
on public.waitlist
for insert
to anon
with check (
  length(trim(name)) > 0
  and email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$'
);
```

Add field allowlists inside `with check` if the frontend uses fixed dropdown values.

## Frontend request pattern

```js
await fetch(`${SUPABASE_URL}/rest/v1/waitlist`, {
  method: 'POST',
  headers: {
    apikey: SUPABASE_ANON_KEY,
    Authorization: `Bearer ${SUPABASE_ANON_KEY}`,
    'Content-Type': 'application/json',
    Prefer: 'return=minimal'
  },
  body: JSON.stringify(entry)
});
```

## Pitfalls

- If Supabase returns `PGRST205 Could not find the table ... in the schema cache`, the table has not been created yet or the schema cache has not picked it up. Create the table in SQL Editor and retry.
- If Supabase returns `42501 violates row-level security policy`, the table exists but the RLS policy does not allow the submitted operation/values.
- `upsert` with `on_conflict=email` is not just an insert. It may require update policies too. For waitlist MVPs, simple insert is usually easier and safer.
- A public SELECT policy is not needed for waitlist collection and would expose signups to visitors.

## Verification steps

1. Test a direct REST insert with `curl`; success should be HTTP 201 with `Prefer: return=minimal`.
2. Test the browser form and confirm the success state appears.
3. Check console errors after submission.
4. Confirm the row appears in Supabase Table Editor.
