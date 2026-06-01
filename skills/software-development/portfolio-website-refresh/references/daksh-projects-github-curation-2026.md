# Daksh portfolio: GitHub project curation notes (2026)

Use when updating Daksh Godara's portfolio Projects section from his public GitHub profile.

## Positioning target

Daksh wants the portfolio to preserve the existing dark cyan/purple developer-style UI while strengthening his PM/product-builder positioning: fintech, insurance, agentic AI, Indian markets, workflow automation, and systems thinking. Projects should be curated, not a raw list of repos.

## Project-selection rules learned

- Prefer projects that show product intuition + systems/automation depth over generic older college repos.
- Add GitHub/source icons only for repos verified as public/reachable. If a local remote exists but the public URL returns GitHub 404/Page not found, omit the icon.
- Avoid adding company/internal product cards to Projects when the user asks specifically for GitHub-linked public projects. Keep confidential/company work in Experience instead.
- Preserve the existing project card structure, dark theme, icons, tags, and scroll reveal behavior; do not redesign the section unless explicitly asked.
- Before publishing, verify: HTML parses, project-card count is expected, GitHub links in DOM match real public repos, browser console is clean, and the visual layout reveals correctly after scrolling.

## Recommended 6-card order used in this session

1. Arbiter — Agentic Trading Decision System
   - Strategic fit: agentic AI + Indian retail trading + product thesis.
   - No GitHub icon unless `https://github.com/dakshgodara2001/agentic-trading-landing` becomes publicly reachable.
2. SunSeat — Route-based Seat Recommendation Engine
   - Repo: `https://github.com/dakshgodara2001/sunSeat`
   - Why: strong productized recommendation engine; route geometry, departure time, solar-position math, FastAPI/API/UI/tests/Docker.
   - Tags: Python, FastAPI, Route Intelligence, Recommendation Engine.
3. NSE/BSE Market Intelligence Automation
   - Repo: `https://github.com/dakshgodara2001/Stock-Monitoring-Platform`
   - Why: aligns with Indian markets, trading intelligence, Python automation.
4. Room Check Crawler
   - Repo: `https://github.com/dakshgodara2001/room-check-crawler`
   - Why: practical workflow automation with Playwright scheduling and Telegram alerts.
   - Tags: Python, Playwright, Automation, Telegram Alerts.
5. 8Bins — Smart Waste Management
   - Founder/startup + IoT/CV story; omit GitHub icon unless a public matching repo is found.
6. AI Models vs Developer Activity
   - Repo: `https://github.com/dakshgodara2001/ai-models-vs-commits`
   - Why: AI/data research angle.

## Candidate ranking from repo inspection

- Strong additions: `sunSeat`, `room-check-crawler`.
- Good but secondary: `log-monitoring` (real-time ops/WebSockets, PM engineering empathy), `Store-Monitoring` (Flask/SQLite reporting workflow).
- Lower priority for current positioning: `Number-Plate-Detector` (public CV project, but older/college-style).

## Implementation pattern

When adding project cards:

1. Check `git status --short --branch` first.
2. Patch only `index.html` unless UI changes are requested.
3. Insert cards in the approved order and reuse the existing GitHub SVG/link structure.
4. Run a lightweight HTML parse.
5. Confirm expected project-card count and DOM links.
6. Preview locally with a cache-busting query like `?projects-add-two=1#projects`.
7. Scroll the Projects section enough for reveal animations to fire before judging missing/invisible content.
8. Do not commit/push until Daksh explicitly approves publishing.
