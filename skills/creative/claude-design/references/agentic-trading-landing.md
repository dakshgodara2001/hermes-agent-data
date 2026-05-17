# Agentic trading landing page pattern

Use when designing a landing page for an AI/agentic trading copilot, scanner, trading sandbox, or retail trader education product.

## Positioning that worked

Lead with discipline, not predictions:

- "Stop chasing tips. Train your trading process."
- "Not tips. A trading framework."
- "Decision-support copilot and practice sandbox"
- "Educational research first"
- "Risk before entries"
- "Post-market accountability"

Avoid hype framing:

- guaranteed returns
- multibagger promises
- buy/sell signal bot language
- "profit machine" tone
- fake performance metrics

## Core sections

1. Hero
   - Clear anti-tip headline.
   - Explain the product as a decision-support copilot and sandbox.
   - Primary CTA: get early access / join waitlist.
   - Secondary CTA: see the framework.

2. Product preview
   - Show an agent decision card, not a generic dashboard.
   - Include market context, setup decision, invalidation logic, and a "NOT A TIP" badge.
   - Example labels: Global cue, Sector pulse, Mode, Setup decision, Copilot asks, Review loop.

3. Framework
   - Pre-market context before stock picks.
   - Setup validation by style: momentum, swing, long-term.
   - Post-market review that compares suggestions against actual outcomes.

4. Sandbox / learning gym
   - Historical scenario practice.
   - User decisions: enter, wait, avoid.
   - Feedback on risk/reward, invalidation, patience, and stop placement.

5. Waitlist
   - Capture name, email, trading style, and market.
   - For local prototypes, localStorage + CSV export is a useful first waitlist implementation.
   - Public-facing helper copy should say "No spam. Early access updates only" rather than sounding like an unfinished prototype.

6. Compliance disclaimer
   - For Indian trading products, include a visible disclaimer that the product is not a SEBI-registered investment adviser, does not provide guaranteed returns, and is for education/research/journaling/decision-support unless a compliant advisory setup exists.

## Visual direction

Good fit:

- Dark fintech / Linear-like precision.
- High contrast type.
- Sparse violet/green accents.
- Subtle dashboard mockup with real decision logic.
- Serious and calm rather than crypto/gambling energy.

Pitfalls:

- Secondary gray text can become too low-contrast on dark fintech pages; verify and brighten if needed.
- Large empty hero gaps can feel premium but may reduce density; tune after visual review.
- Public landing pages should not expose internal implementation notes like "connect to Formspree later" unless explicitly intended for a prototype handoff.
