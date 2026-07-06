---
name: creative-visual-artifacts
description: "Use when designing static or mostly-static visual artifacts: landing pages, HTML mockups, architecture diagrams, Excalidraw sketches, infographics, design tokens, and style-system-inspired web visuals. Consolidates visual design workflows into one class-level skill with labeled modes."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [creative, design, html, diagrams, infographics, mockups]
    related_skills: []
---

# Creative Visual Artifacts

## Overview

Use this umbrella when the user wants a designed artifact rather than a long-running app: a landing page, a polished HTML/SVG concept, an architecture diagram, an Excalidraw-style sketch, an infographic, a design-token specification, or a style reference based on well-known product sites.

The class-level workflow is: clarify the artifact type only if the request is ambiguous, pick the correct labeled mode below, produce a real file when possible, then verify it by opening/rendering/linting/exporting rather than only describing it.

## When to Use

- Static landing pages, one-off HTML/CSS concepts, comparison mockups, pitch posters, technical explainers, dashboards, and prototypes.
- Architecture/cloud/infra diagrams, flow diagrams, sequence diagrams, and hand-drawn Excalidraw JSON.
- Infographics with explicit layout/style systems.
- DESIGN.md token specs or design-system documentation.
- Requests to imitate a recognized web/product design style as a starting point.

Don't use this for generative-code animation, video rendering, TouchDesigner scenes, or ComfyUI model workflows; use `creative-media-production` for those.

## Mode Selection

| Mode | Former narrow skill(s) | Use when | Output pattern |
|---|---|---|---|
| HTML artifact / landing page | `claude-design`, `sketch` | User wants a one-off web page, prototype, deck-like HTML, or 2-3 visual variants. | Create `index.html` or named HTML files; prefer self-contained CSS; run a local preview or syntax check. |
| Architecture diagram | `architecture-diagram` | User asks for system, cloud, infra, or data-flow diagrams. | Dark themed SVG/HTML diagram; label components and data paths; verify dimensions/readability. |
| Excalidraw-style diagram | `excalidraw` | User wants hand-drawn, editable, or collaborative diagram JSON. | Generate `.excalidraw`/JSON or HTML export; keep elements grouped and labeled. |
| Infographic | `baoyu-infographic` | User wants visual teaching, comparison, roadmap, breakdown, or Chinese 信息图/可视化. | Pick a layout + style, compress text into visual chunks, and deliver an image/HTML artifact. |
| Design system docs | `design-md` | User asks for DESIGN.md, tokens, palettes, spacing, typography, or exportable design spec. | Produce/validate a DESIGN.md-style token document. |
| Popular style reference | `popular-web-designs` | User wants something in the spirit of Stripe, Linear, Vercel, Notion, Apple, etc. | Extract 3-5 style traits; apply them without claiming brand affiliation. |
| Text-as-layout demo | `pretext` | User wants a creative browser demo around typography, ASCII-like flow, or text geometry. | Build a small HTML demo using the appropriate text layout library/pattern. |
| Humanized copy | `humanizer` | User wants text to sound more natural, less AI-ish, or more voiceful inside an artifact. | Preserve facts and intent; remove generic AI phrasing; add concrete rhythm and human texture. |

## Always-Needed Process

1. **Name the artifact contract.** State the mode, deliverable filename/type, and whether it is meant for direct use, comparison, or inspiration.
2. **Gather only necessary constraints.** If missing, choose sensible defaults: desktop-first 1440px, dark/light based on request tone, self-contained file, no external secrets.
3. **Build the artifact.** Prefer a real file over prose. Keep CSS/design tokens explicit so the user can edit them.
4. **Verify mechanically.** Use browser/renderer/syntax/lint/export checks where available. For HTML, at least ensure the file exists and can be served/opened; for JSON, parse it.
5. **Summarize design decisions.** Explain the visual system and the exact file(s) produced.

## Pitfalls

- Do not create three separate skills for three visual artifact types; use this mode table and labeled subsections.
- Do not leave large style/template banks always-visible. Put bulky examples under `templates/` or `references/` when resurrecting archived material.
- Do not copy brand assets or imply affiliation when using a popular product as design inspiration.
- Do not stop at a description when the user asked to make something; produce and verify the artifact.

## Verification Checklist

- [ ] Selected the correct mode and output format.
- [ ] Produced a concrete file or explicitly explained why not possible.
- [ ] Ran a render, parse, syntax, or existence check.
- [ ] Reported filenames and any assumptions.
