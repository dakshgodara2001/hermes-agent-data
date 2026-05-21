# TradePilot waitlist onboarding example

Context: Static HTML/JS landing page for a fintech/trading MVP, with Supabase PostgREST waitlist persistence, local CSV backup, Vercel deployment, and Vercel Web Analytics.

## User/product constraints

- Premium dark fintech landing page.
- Indian NSE/BSE trading audience.
- Positioning: “Not tips. A trading framework.”
- SEBI/financial-advice-safe disclaimers.
- Static HTML/JS for MVP; no framework unless needed.

## Change made

Added a required onboarding question to the waitlist form:

```html
<label for="struggle">Biggest trading struggle</label>
<textarea
  id="struggle"
  name="struggle"
  minlength="8"
  maxlength="500"
  placeholder="Example: I enter too early, overtrade after losses, or don’t know when to skip a setup."
  required
></textarea>
```

Frontend payload field:

```js
biggest_struggle: data.struggle.trim()
```

Local CSV backup headers must include the new field:

```js
['name', 'email', 'trading_style', 'market', 'biggest_struggle', 'created_at']
```

Analytics should not send the free-text answer. Send derived metadata only:

```js
const trackingProps = {
  market: entry.market,
  trading_style: entry.trading_style,
  struggle_length: entry.biggest_struggle.length
};
```

## Supabase migration pattern

Create a one-time migration for existing deployments:

```sql
alter table public.waitlist
add column if not exists biggest_struggle text;

drop policy if exists "Anyone can join waitlist" on public.waitlist;
create policy "Anyone can join waitlist"
on public.waitlist
for insert
to anon
with check (
  length(trim(name)) > 0
  and email ~* '^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}$'
  and trading_style in ('Swing trader', 'Momentum trader', 'Long-term investor', 'Still learning')
  and market in ('NSE/BSE', 'Crypto', 'US equities', 'Multiple markets')
  and biggest_struggle is not null
  and length(trim(biggest_struggle)) between 8 and 500
);
```

## Live-schema fallback pattern

If admin credentials/login are unavailable and the migration cannot be run immediately, keep the production form from breaking:

1. Try inserting the full entry including `biggest_struggle`.
2. If Supabase/PostgREST returns a missing-column error such as `PGRST204` or error text mentioning `biggest_struggle`, retry without that field.
3. Save the full entry to local backup.
4. Track a non-sensitive `Waitlist onboarding column missing` event.
5. Tell the user the signup works, but the onboarding answer will not persist in Supabase until the migration is run.

This is a temporary compatibility bridge, not a substitute for the migration.

## Verification

- Local static server loads page.
- Browser snapshot shows the new required textarea.
- Native validation enforces required/minlength.
- Test signup displays success.
- Production deploy aliases to canonical URL.
- Production page shows the textarea.
- Analytics script `/_vercel/insights/script.js` loads.
- Browser console has no errors after submission.
