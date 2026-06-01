# Daksh portfolio refresh notes — 2026

These notes are session-specific context for future portfolio website refresh work.

## Site/repo context

- Public site: `https://dakshgodara2001.github.io/`
- Local repo used in this session: `/Users/dakshgodara/Desktop/webportfolio/dakshgodara2001.github.io`
- Work happened on branch: `redesign/product-case-study-portfolio`
- User rejected a full redesign and preferred the original dark cyan/purple UI.

## Durable user preferences observed

- Preserve the old/original UI unless he explicitly asks for a redesign.
- Improve one section at a time.
- Suggest copy/structure first, then implement only after approval.
- Show local preview before any GitHub push.
- Keep Git diffs small and reviewable.
- Do not remove important technical skills while reorganizing stack labels; Python should remain visible.

## Approved portfolio positioning examples

Hero tagline approved in this session:

`Building 0→1 fintech, insurance & AI products that move business metrics`

About stack direction approved:

1. Product & Strategy
2. Fintech, Insurance & Wealth
3. AI & Automation
4. Analytics, Systems & Tools

AI & Automation should reflect current AI/product interests and interactions, but keep tags unique and non-overlapping. Final approved compact set from this session:

- Agentic AI
- RAG Products
- LLM Workflows
- Prompt Design
- Evaluation Loops
- LangGraph
- Agent Harness
- Multi-agent Workflows

Do not include AI Assistants or Decision Support Systems in this stack unless Daksh asks to re-add them. Avoid adding both broad and near-duplicate labels like Agentic AI + AI Agents + AI Assistants.

Analytics/Systems/Tools should keep Python visible along with SQL, Mixpanel, Grafana, NewRelic, APIs & Integrations, System Design, Figma, Balsamiq, Jira, Postman, Cursor, Claude Code, and Excel.

## Experience copy direction approved

For Daksh's INDmoney experience, preserve the existing timeline/card UI and improve only approved copy blocks.

Approved Product Manager summary direction:

`Leading 0→1 fintech, insurance and AI products at INDmoney — owning discovery, roadmap, GTM, CRM workflows and execution with engineering, design, sales and operations teams.`

Approved Term Life Insurance positioning:

- Lead with end-to-end ownership of INDmoney’s term life funnel.
- Mention insurer integrations, recommendation journeys, riders/add-ons, CRM workflows and sales-agent tooling.
- Use metrics around 3rd largest digital aggregator by revenue, high term-life conversion rates, 50+ sales agents supported, 30% call-connectivity lift, and higher ATV through riders/add-ons.

AI insurance assistant should not be framed as only a “RAG-based chatbot.” Daksh clarified it was a proper workflow-based assistant/product with tool integrations plus a complete knowledge base using RAG technology. Preferred phrasing:

`Built a workflow-based insurance assistant powered by RAG, tool integrations and a complete policy knowledge base — handling application support, family-cover recommendations, plan comparisons, policy wording explanations and FAQs across the life insurance journey.`

Useful metric phrasing:

- Improved DIY funnel completion
- 20% reduction in support queries
- Tool-integrated workflows for policy and application support

Approved Associate Product Manager / INDwheels direction:

- Reframe as `INDwheels — Vehicle Tracking + Motor Insurance`.
- Explain the product sequence: vehicle garage / repeat-engagement utility first, then motor-insurance monetization.
- Include vehicle value, insurance, PUCC, FASTag and challans.
- Useful metrics/tags: `1M+ active vehicles tracked`, `Industry-leading motor insurance conversion rates`, `Created repeat-engagement utility before insurance monetization`.

Approved 8Bins startup direction in Experience:

- Reframe as co-founder experience, not just a college project.
- Use `IoT + computer vision startup for smart waste management`.
- Mention OpenCV-based waste-classification workflows and hardware/software prototype for automated waste segregation.
- Combine recognition line: `Top 12 at NASSCOM CienaHack 2020; mentored by PadUp Ventures`.

## Projects section direction approved

Current approved direction: Projects should represent selected products, systems and experiments aligned with Daksh's current profile — PM + fintech/insurance + agentic AI + Indian markets — not merely a list of older public GitHub repos.

Approved section intro:

`Selected products, systems and experiments across fintech, insurance, agentic AI and market intelligence — spanning 0→1 product builds, workflow automation, data analysis and startup prototypes.`

Approved six-card Option B order:

1. `Arbiter — Agentic Trading Decision System`
   - Description: Agentic trading copilot for Indian retail traders that turns every trade idea into a structured decision card — thesis, risk, invalidation, market context and post-trade feedback.
   - Impact/Role: Founder / Product Builder
   - Tags: Agentic AI, Trading, Risk Systems, Indian Markets

2. `AI Insurance Assistant`
   - Description: Workflow-based insurance assistant powered by RAG, tool integrations and a complete policy knowledge base — supporting plan comparison, family-cover recommendations, application support and policy FAQs.
   - Impact: Improved DIY completion; reduced support queries by 20%
   - Tags: RAG, LLM Workflows, Insurance, Tool Integrations

3. `NSE/BSE Market Intelligence Automation`
   - Description: Automated Indian market scanner focused on Nifty 50, Bank Nifty and underlying constituents — combining technical signals, sector context, fundamentals and pre-market cues into actionable watchlists.
   - Role: Built daily market intelligence workflow
   - Tags: Python, Market Data, Automation, NSE/BSE
   - Compliance tone: prefer “watchlists,” “signals,” “market intelligence,” and “decision support”; avoid claiming direct investment recommendations.

4. `Term Life Insurance Funnel`
   - Description: Owned INDmoney’s term insurance funnel across insurer integrations, recommendation journeys, riders/add-ons, CRM workflows and sales-agent tooling.
   - Impact: 3rd largest digital aggregator by revenue in India
   - Tags: Insurtech, Funnel Optimization, CRM, GTM

5. `8Bins — Smart Waste Management`
   - Description: Co-founded an IoT + computer vision startup for automated waste segregation, combining hardware prototyping with OpenCV-based waste classification workflows.
   - Impact: Top 12 at NASSCOM CienaHack; mentored by PadUp Ventures
   - Tags: Startup, IoT, Computer Vision, OpenCV

6. `AI Models vs Developer Activity`
   - Description: Time-series research project analyzing whether major LLM releases correlate with changes in GitHub commit activity and developer behavior patterns.
   - Role: Independent data analysis using GitHub activity data
   - Tags: Python, Data Analysis, AI Research, GitHub API

## Projects section direction

When refreshing Daksh's Projects section, keep it aligned to his current AI × Product × Systems positioning but respect whether he wants GitHub-backed projects versus product case studies.

Latest preferred Projects set from this session after user correction:

1. Arbiter — Agentic Trading Decision System
   - Keep as a project because it is central to his current agentic trading thesis.
   - Do not add a GitHub icon unless the repo is public/reachable. The local remote `dakshgodara2001/agentic-trading-landing` existed, but the public GitHub URL returned “Page not found” during this session.
2. NSE/BSE Market Intelligence Automation
   - Can link to public repo: `https://github.com/dakshgodara2001/Stock-Monitoring-Platform`.
   - Position as market intelligence / watchlists / decision support, not trading tips.
3. 8Bins — Smart Waste Management
   - Keep as founder/startup proof.
   - No public matching 8Bins/waste-management repo was visible on Daksh's GitHub profile in this session; do not link to a generic profile or wrong repo.
4. AI Models vs Developer Activity
   - Link to public repo: `https://github.com/dakshgodara2001/ai-models-vs-commits`.

User explicitly asked to remove the generic Projects intro paragraph:

`Selected products, systems and experiments across fintech, insurance, agentic AI and market intelligence — spanning 0→1 product builds, workflow automation, data analysis and startup prototypes.`

User also asked to remove company-product cards from Projects:

- AI Insurance Assistant
- Term Life Insurance Funnel

These remain appropriate in Experience, but should not be re-added to Projects unless Daksh explicitly asks for product case-study cards.

## Verification pattern used

- Run a simple HTML parse when editing static HTML.
- Keep local `python3 -m http.server` preview running.
- Open local preview with a cache-busting query string.
- Visually inspect About/section layout with browser vision.
- Check console for JS errors.
- Report `git status` and whether anything was committed/pushed.
- For sections using reveal animations, scroll within the section until each row/card enters view and verify the cards gain their visible/animate state before concluding the layout is blank or broken.
