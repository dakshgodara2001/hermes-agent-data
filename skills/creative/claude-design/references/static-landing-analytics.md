# Static landing page analytics

Use this reference when a deployed static landing page needs basic funnel analytics: visits, CTA clicks, waitlist attempts, completed signups, duplicate emails, and failures.

## Vercel Web Analytics pattern

For a static HTML page deployed on Vercel, add Vercel Insights directly near the end of `<body>`:

```html
<script defer src="/_vercel/insights/script.js"></script>
```

This records page views in Vercel Web Analytics after deployment. The script path is served by Vercel; it will not behave the same from a plain local file or non-Vercel static server.

## Custom event helper

Use a small defensive helper so the page still works if Analytics is unavailable or the account plan does not support custom events:

```html
<script>
  function trackEvent(name, properties = {}) {
    try {
      if (window.va) window.va('event', { name, data: properties });
    } catch (error) {
      console.debug('Analytics event skipped', name, error);
    }
  }
</script>
```

Keep event names product-readable, not implementation-only. Good examples:

- `Header waitlist clicked`
- `Hero early access clicked`
- `Hero framework clicked`
- `Waitlist submit attempted`
- `Waitlist signup completed`
- `Waitlist duplicate email`
- `Waitlist signup failed`

For CTAs, attach attributes like `data-track="Hero early access clicked"` and bind one listener to all `[data-track]` elements:

```js
document.querySelectorAll('[data-track]').forEach((element) => {
  element.addEventListener('click', () => trackEvent(element.dataset.track));
});
```

For waitlist forms, emit events around actual outcomes:

```js
trackEvent('Waitlist submit attempted', { market, trading_style });

if (response.ok) {
  trackEvent('Waitlist signup completed', { market, trading_style });
} else if (isDuplicateEmail) {
  trackEvent('Waitlist duplicate email', { market, trading_style });
} else {
  trackEvent('Waitlist signup failed', { status: response.status });
}
```

Avoid sending raw emails, phone numbers, names, or other PII in analytics payloads.

## Verification checklist

After deployment, verify analytics without overclaiming dashboard data that may lag:

1. Redeploy to production with `npx vercel --prod --yes`.
2. Open the production URL, not only localhost.
3. Check the browser console for JavaScript errors.
4. Confirm `/_vercel/insights/script.js` loads on the production page.
5. Click tracked CTAs and submit the form once with a test email.
6. Confirm the form still writes to the backend and duplicate handling still works.
7. Tell the user custom events may require a paid Vercel plan; page views should still be available where Web Analytics is enabled.

## Common pitfalls

- Do not put PII in analytics events.
- Do not claim Vercel dashboard numbers immediately; analytics ingestion can lag.
- Do not break the waitlist flow while instrumenting it. Re-test backend success and duplicate-email behavior after adding analytics.
- Do not treat local failure of `/_vercel/insights/script.js` as a production failure; verify on the deployed Vercel URL.
