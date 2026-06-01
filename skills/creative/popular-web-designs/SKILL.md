---
name: popular-web-designs
description: 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS.
version: 1.0.0
author: Hermes Agent + Teknium (design systems sourced from VoltAgent/awesome-design-md)
license: MIT
tags: [design, css, html, ui, web-development, design-systems, templates]
platforms: [linux, macos, windows]
triggers:
  - build a page that looks like
  - make it look like stripe
  - design like linear
  - vercel style
  - create a UI
  - web design
  - landing page
  - dashboard design
  - website styled like
---

# Popular Web Designs

54 real-world design systems ready for use when generating HTML/CSS. Each template captures a
site's complete visual language: color palette, typography hierarchy, component styles, spacing
system, shadows, responsive behavior, and practical agent prompts with exact CSS values.

## Related design skills

- **`claude-design`** — use for the design *process and taste* (scoping a brief,
  producing variants, verifying a local HTML artifact, avoiding AI-design slop).
  Pair it with this skill when the user wants a thoughtfully-designed page styled
  after a known brand: `claude-design` drives the workflow, this skill supplies
  the visual vocabulary.
- **`design-md`** — use when the deliverable is a formal DESIGN.md token spec
  file, not a rendered artifact.

## How to Use

1. Pick a design from the catalog below
2. Load it: `skill_view(name="popular-web-designs", file_path="templates/<site>.md")`
3. Use the design tokens and component specs when generating HTML
4. Pair with the `generative-widgets` skill to serve the result via cloudflared tunnel

Each template includes a **Hermes Implementation Notes** block at the top with:
- CDN font substitute and Google Fonts `<link>` tag (ready to paste)
- CSS font-family stacks for primary and monospace
- Reminders to use `write_file` for HTML creation and `browser_vision` for verification

## Portfolio / Static Site Redesign Pitfalls

When redesigning a static portfolio or landing page for local preview, make scroll animations progressive enhancement only:
- Content must be visible by default in CSS. Do **not** set sections/cards to `opacity: 0` unless a JS-enabled class and visible fallback guarantee they render.
- Browser screenshots, crawlers, accessibility snapshots, slow JS, and user previews can otherwise show huge blank sections even though the DOM contains text.
- Recommended pattern: base `.reveal { opacity: 1; transform: none; }`; if animation is desired, add it only after JS initializes, and keep a no-JS / reduced-motion fallback visible.
- Always verify with a local server + browser visual check before asking the user to approve.

## HTML Generation Pattern

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Title</title>
  <!-- Paste the Google Fonts <link> from the template's Hermes notes -->
  <link href="https://fonts.googleapis.com/css2?family=..." rel="stylesheet">
  <style>
    /* Apply the template's color palette as CSS custom properties */
    :root {
      --color-bg: #ffffff;
      --color-text: #171717;
      --color-accent: #533afd;
      /* ... more from template Section 2 */
    }
    /* Apply typography from template Section 3 */
    body {
      font-family: 'Inter', system-ui, sans-serif;
      color: var(--color-text);
      background: var(--color-bg);
    }
    /* Apply component styles from template Section 4 */
    /* Apply layout from template Section 5 */
    /* Apply shadows from template Section 6 */
  </style>
</head>
<body>
  <!-- Build using component specs from the template -->
</body>
</html>
```

Write the file with `write_file`, serve with the `generative-widgets` workflow (cloudflared tunnel),
and verify the result with `browser_vision` to confirm visual accuracy.

## Font Substitution Reference

Most sites use proprietary fonts unavailable via CDN. Each template maps to a Google Fonts
substitute that preserves the design's character. Common mappings:

| Proprietary Font | CDN Substitute | Character |
|---|---|---|
| Geist / Geist Sans | Geist (on Google Fonts) | Geometric, compressed tracking |
| Geist Mono | Geist Mono (on Google Fonts) | Clean monospace, ligatures |
| sohne-var (Stripe) | Source Sans 3 | Light weight elegance |
| Berkeley Mono | JetBrains Mono | Technical monospace |
| Airbnb Cereal VF | DM Sans | Rounded, friendly geometric |
| Circular (Spotify) | DM Sans | Geometric, warm |
| figmaSans | Inter | Clean humanist |
| Pin Sans (Pinterest) | DM Sans | Friendly, rounded |
| NVIDIA-EMEA | Inter (or Arial system) | Industrial, clean |
| CoinbaseDisplay/Sans | DM Sans | Geometric, trustworthy |
| UberMove | DM Sans | Bold, tight |
| HashiCorp Sans | Inter | Enterprise, neutral |
| waldenburgNormal (Sanity) | Space Grotesk | Geometric, slightly condensed |
| IBM Plex Sans/Mono | IBM Plex Sans/Mono | Available on Google Fonts |
| Rubik (Sentry) | Rubik | Available on Google Fonts |

When a template's CDN font matches the original (Inter, IBM Plex, Rubik, Geist), no
substitution loss occurs. When a substitute is used (DM Sans for Circular, Source Sans 3
for sohne-var), follow the template's weight, size, and letter-spacing values closely —
those carry more visual identity than the specific font face.

## Design Catalog

### AI & Machine Learning

| Template | Site | Style |
|---|---|---|
| `claude.md` | Anthropic Claude | Warm terracotta accent, clean editorial layout |
| `cohere.md` | Cohere | Vibrant gradients, data-rich dashboard aesthetic |
| `elevenlabs.md` | ElevenLabs | Dark cinematic UI, audio-waveform aesthetics |
| `minimax.md` | Minimax | Bold dark interface with neon accents |
| `mistral.ai.md` | Mistral AI | French-engineered minimalism, purple-toned |
| `ollama.md` | Ollama | Terminal-first, monochrome simplicity |
| `opencode.ai.md` | OpenCode AI | Developer-centric dark theme, full monospace |
| `replicate.md` | Replicate | Clean white canvas, code-forward |
| `runwayml.md` | RunwayML | Cinematic dark UI, media-rich layout |
| `together.ai.md` | Together AI | Technical, blueprint-style design |
| `voltagent.md` | VoltAgent | Void-black canvas, emerald accent, terminal-native |
| `x.ai.md` | xAI | Stark monochrome, futuristic minimalism, full monospace |

### Developer Tools & Platforms

| Template | Site | Style |
|---|---|---|
| `cursor.md` | Cursor | Sleek dark interface, gradient accents |
| `expo.md` | Expo | Dark theme, tight letter-spacing, code-centric |
| `linear.app.md` | Linear | Ultra-minimal dark-mode, precise, purple accent |
| `lovable.md` | Lovable | Playful gradients, friendly dev aesthetic |
| `mintlify.md` | Mintlify | Clean, green-accented, reading-optimized |
| `posthog.md` | PostHog | Playful branding, developer-friendly dark UI |
| `raycast.md` | Raycast | Sleek dark chrome, vibrant gradient accents |
| `resend.md` | Resend | Minimal dark theme, monospace accents |
| `sentry.md` | Sentry | Dark dashboard, data-dense, pink-purple accent |
| `supabase.md` | Supabase | Dark emerald theme, code-first developer tool |
| `superhuman.md` | Superhuman | Premium dark UI, keyboard-first, purple glow |
| `vercel.md` | Vercel | Black and white precision, Geist font system |
| `warp.md` | Warp | Dark IDE-like interface, block-based command UI |
| `zapier.md` | Zapier | Warm orange, friendly illustration-driven |

### Infrastructure & Cloud

| Template | Site | Style |
|---|---|---|
| `clickhouse.md` | ClickHouse | Yellow-accented, technical documentation style |
| `composio.md` | Composio | Modern dark with colorful integration icons |
| `hashicorp.md` | HashiCorp | Enterprise-clean, black and white |
| `mongodb.md` | MongoDB | Green leaf branding, developer documentation focus |
| `sanity.md` | Sanity | Red accent, content-first editorial layout |
| `stripe.md` | Stripe | Signature purple gradients, weight-300 elegance |

### Design & Productivity

| Template | Site | Style |
|---|---|---|
| `airtable.md` | Airtable | Colorful, friendly, structured data aesthetic |
| `cal.md` | Cal.com | Clean neutral UI, developer-oriented simplicity |
| `clay.md` | Clay | Organic shapes, soft gradients, art-directed layout |
| `figma.md` | Figma | Vibrant multi-color, playful yet professional |
| `framer.md` | Framer | Bold black and blue, motion-first, design-forward |
| `intercom.md` | Intercom | Friendly blue palette, conversational UI patterns |
| `miro.md` | Miro | Bright yellow accent, infinite canvas aesthetic |
| `notion.md` | Notion | Warm minimalism, serif headings, soft surfaces |
| `pinterest.md` | Pinterest | Red accent, masonry grid, image-first layout |
| `webflow.md` | Webflow | Blue-accented, polished marketing site aesthetic |

### Fintech & Crypto

| Template | Site | Style |
|---|---|---|
| `coinbase.md` | Coinbase | Clean blue identity, trust-focused, institutional feel |
| `kraken.md` | Kraken | Purple-accented dark UI, data-dense dashboards |
| `revolut.md` | Revolut | Sleek dark interface, gradient cards, fintech precision |
| `wise.md` | Wise | Bright green accent, friendly and clear |

### Enterprise & Consumer

| Template | Site | Style |
|---|---|---|
| `airbnb.md` | Airbnb | Warm coral accent, photography-driven, rounded UI |
| `apple.md` | Apple | Premium white space, SF Pro, cinematic imagery |
| `bmw.md` | BMW | Dark premium surfaces, precise engineering aesthetic |
| `ibm.md` | IBM | Carbon design system, structured blue palette |
| `nvidia.md` | NVIDIA | Green-black energy, technical power aesthetic |
| `spacex.md` | SpaceX | Stark black and white, full-bleed imagery, futuristic |
| `spotify.md` | Spotify | Vibrant green on dark, bold type, album-art-driven |
| `uber.md` | Uber | Bold black and white, tight type, urban energy |

## Choosing a Design

Match the design to the content:

- **Developer tools / dashboards:** Linear, Vercel, Supabase, Raycast, Sentry
- **Documentation / content sites:** Mintlify, Notion, Sanity, MongoDB
- **Marketing / landing pages:** Stripe, Framer, Apple, SpaceX
- **Dark mode UIs:** Linear, Cursor, ElevenLabs, Warp, Superhuman
- **Light / clean UIs:** Vercel, Stripe, Notion, Cal.com, Replicate
- **Playful / friendly:** PostHog, Figma, Lovable, Zapier, Miro
- **Premium / luxury:** Apple, BMW, Stripe, Superhuman, Revolut
- **Data-dense / dashboards:** Sentry, Kraken, Cohere, ClickHouse
- **Monospace / terminal aesthetic:** Ollama, OpenCode, x.ai, VoltAgent

## Existing Site / Portfolio Refinement Workflow

When improving an existing portfolio or personal site, do **not** default to a full redesign unless the user explicitly asks for one. Prefer a section-by-section refinement loop:

1. Inspect the live/local site visually and structurally.
2. Preserve the existing visual language if the user likes it; improve copy, hierarchy, spacing, and content packaging inside that style.
3. Suggest changes for one section at a time, with clear options and exact replacement copy.
4. Wait for approval/rejection before editing that section.
5. Make the smallest approved diff first; avoid bundling unrelated redesign changes.
6. Preview locally and verify visually before proposing commit/push.

Pitfall: A polished wholesale redesign can still be wrong if the user prefers the original UI. For portfolios, the first pass should often be “same UI, sharper content” rather than “new design system.”

### Section-by-section portfolio copy guardrails

When the user asks to proceed to the “next section,” inspect that section and propose concrete copy/structure changes first; do not edit until they approve. Keep each iteration narrowly scoped to the section under discussion.

For capability/skill-tag sections:
- Preserve important existing tags unless the user explicitly removes them; do not drop core tools such as Python just because you are reordering categories.
- Avoid near-duplicate tags in the same category. Pick the sharpest distinct labels (for example, prefer a concise AI set like `Agentic AI`, `RAG Products`, `LLM Workflows`, `Prompt Design`, `Evaluation Loops`, `LangGraph`, `Agent Harness`, `Multi-agent Workflows` rather than overlapping `AI Agents` + `AI Assistants` + `Agentic AI`).
- If the user corrects tag wording/removals, apply exactly that small change, then verify visually and do not push/commit without approval.

For Experience sections in PM portfolios:
- Preserve the existing timeline/card UI unless a design change is requested.
- Improve content around ownership, product surface, cross-functional execution, and measurable outcomes.
- Write entries in a compact “owned/built → scope → impact” style rather than generic responsibility bullets.