---
name: portfolio-website-refresh
description: Incrementally improve a personal portfolio website while preserving the user-approved visual identity, previewing locally, and using Git safely.
---

# Portfolio Website Refresh

Use this skill when updating Daksh's or another user's personal portfolio/resume website, especially when the user asks to improve copy, sections, project presentation, skills, or visual polish without a full rebuild.

## Core principles

1. Preserve the approved UI unless the user explicitly asks for a redesign.
   - Do not replace an existing style system after the user says they like it.
   - For Daksh, preserve the dark cyan/purple developer-style UI unless he explicitly changes direction.
2. Work section-by-section.
   - Suggest changes first.
   - Implement only the approved scope.
   - Keep diffs small and easy to review.
3. Preview before publishing.
   - Run a local server when possible.
   - Inspect the result visually.
   - Check console errors.
   - Do not push/deploy until the user approves the preview.
4. Keep Git safe.
   - Check branch/status before editing.
   - Use a feature branch for portfolio refresh work.
   - Show `git diff` / `git status` after each meaningful edit.

## Workflow

1. Inspect current site and repo.
   - Open the live site or local preview.
   - Read the relevant source files.
   - Check `git status --short --branch`.
2. Recommend targeted improvements.
   - Prioritize hero, about/positioning, experience, projects/case studies, contact.
   - Explain the reason for each change in product/reader terms.
3. Edit narrowly.
   - Patch only the approved text/section.
   - Avoid broad CSS/JS rewrites unless requested.
4. Verify.
   - Parse HTML or run available build/tests.
   - Reload local preview with a cache-busting query string.
   - Use browser visual inspection for layout/readability.
   - Check browser console for errors.
   - For portfolio project links, verify GitHub URLs are publicly reachable before adding icons; do not link to private/local remotes that 404 for public visitors.
5. Report.
   - State exact files changed.
   - Summarize only the approved changes.
   - Mention preview URL and verification result.
   - Confirm no commit/push if the user has not approved publishing.

## Copy guidance for product portfolios

- Prefer concrete product outcomes over generic capability lists.
- Keep claims credible and aligned to demonstrated experience.
- For fintech/insurance/wealth portfolios, make domain expertise visible in About and Experience sections.
- For Projects sections, distinguish between public GitHub projects and product/case-study work. If the user asks to use GitHub/profile projects, keep company-confidential product work out of Projects unless they explicitly approve case-study cards.
- Only show GitHub/source icons for real public repositories found on the user's GitHub profile or otherwise verified as reachable. If a local repo remote exists but the public URL 404s, omit the icon rather than creating a broken link.
- For AI work, include modern but specific terms only when they match the user's real work/interests, and avoid overlapping/duplicate tags. For Daksh's AI & Automation stack, prefer a compact unique set such as: Agentic AI, RAG Products, LLM Workflows, Prompt Design, Evaluation Loops, LangGraph, Agent Harness, Multi-agent Workflows.
- Do not remove meaningful technical skills without asking. For Daksh, keep Python visible in the stack.
- In Experience sections, frame major PM work as ownership + product surface + business/user impact. Prefer “owned/built/led X end-to-end across Y workflows” over generic “worked on/built a chatbot.”
- For AI insurance work, do not undersell it as merely “RAG-based chatbot” when the actual product involved workflow orchestration, tool integrations, and a complete policy knowledge base. Use wording like “workflow-based insurance assistant powered by RAG, tool integrations and a complete policy knowledge base.”
- For Projects sections in a PM/AI/fintech portfolio, do not default to a flat list of GitHub repos. Curate “selected products, systems and experiments” that match the current positioning: company product case studies, founder/startup projects, automation systems, market intelligence workflows, and independent research. Use GitHub links only where public source is actually helpful.
- For Daksh's Education section, keep it senior and compact: emphasize B.Tech/NSIT plus meaningful achievements; do not spend portfolio real estate on Class X/XII unless he explicitly asks. If achievements are light, fold them into an “Other Achievements” card inside Education rather than keeping a standalone achievements section.
- When consolidating small sections, also renumber downstream section labels and verify nav/anchor behavior so the page does not show stale numbering.

## UI pattern: compact achievements card

When adding achievements inside an Education card, avoid plain two-column list rows that look like a default resume table. Prefer a designed summary card that still matches the existing dark cyan/purple UI:

1. Use a small eyebrow such as “Beyond Work” above the heading.
2. Add a compact count badge when there are 2-4 achievements.
3. Render each achievement as a small row/card with a numeric badge (`01`, `02`, `03`) plus title and short detail.
4. Keep the same card background/border language as the rest of the site, with subtle cyan/purple gradients only; do not introduce a new visual style.
5. Verify visually at the section anchor because scroll-reveal animations can hide cards until the section is in view.

## Pitfalls

- Do not do a full redesign when the user asked for improvements.
- Do not push to GitHub just because the preview works.
- Do not remove prior credible skills/tools while reorganizing stack labels.
- Do not overstuff headings with too many categories if the current layout has limited space.
- Do not treat animations/reveal effects as proof content is missing until you inspect after scrolling/clicking the relevant nav item. For project grids with reveal animations, scroll far enough for each row/card to enter view and verify opacity/class changes before deciding content is missing.

## References

- See `references/daksh-portfolio-2026.md` for session-specific details from Daksh's portfolio refresh preferences, approved positioning, and project-section link handling.
- See `references/daksh-projects-github-curation-2026.md` for the approved GitHub-project curation rules, recommended six-card project order, repo links, and verification pattern used for Daksh's Projects section.

