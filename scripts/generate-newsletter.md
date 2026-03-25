# Flava Pulse — Newsletter Generation Protocol

## Overview
This document is the master prompt for generating a Flava Pulse newsletter edition.
It is designed to be **subject-agnostic** — swap `config.subject` and `config.sources` to generate newsletters for any industry.

---

## Configuration

```yaml
subject:
  name: "Flava"
  industry: "Restaurant & Hospitality AI / Preference Intelligence"
  primary_market: "Sweden"
  secondary_markets: ["Germany", "UK (London)", "US (LA, Vegas, Houston, NYC, Miami)", "Canada (Toronto, Ottawa, Montreal)"]
  language: "sv"  # Newsletter output language

temporal:
  anchor: "runtime"  # Always uses current date at execution time
  recency_tiers:
    breaking: "0-24h"
    fresh: "1-7d"
    recent: "7-30d"
    background: "30-90d"
  delta_tracking: true  # Compare against prior editions

quality:
  min_sources_per_story: 2
  ai_slop_check: true
  max_em_dashes: 0
  tone: "down-to-earth, sharp, no jargon unless truly warranted"
  voice: "informed colleague, not a press release"
```

---

## Phase 1: Research (5 Parallel Explorer Agents)

Each agent runs independently, searching sources from the registry + dynamic web search.
All queries MUST include temporal context: "since [date]", "March 2026", "this week", etc.

### Agent 1: Tech & AI
- Search all `tech_ai` sources
- Focus: Voice AI updates, avatar tech, LLM developments, real-time processing
- Temporal: What shipped in the last 7 days? What was announced? What failed/pivoted?
- Track: ElevenLabs, HeyGen, LiveKit, D-ID, Synthesia, OpenAI voice, Google Gemini voice

### Agent 2: Restaurant & Hospitality Markets
- Search all `hospitality_*` sources
- Focus: Sweden FIRST, then Germany, UK/London, US target cities, Canada target cities
- Temporal: New openings, closings, policy changes, franchise news, seasonal trends
- Track: Visita reports, DEHOGA updates, NRA data, city-specific developments

### Agent 3: POS, Competitors & Market Intelligence
- Search all `pos_competitors` and `market_investment` sources
- Focus: Trivec/Caspeco competitor moves, POS market shifts, funding rounds in restaurant tech
- Temporal: New product launches, acquisitions, partnerships, pricing changes
- Track: Toast, Square, Lightspeed, Sunday, Mr Yum, Popmenu, Dynamic Yield, Tastewise

### Agent 4: Taste Science, Food Innovation & Preference Intelligence
- Search all `taste_science` sources
- Focus: Flavor profiling research, food personalization tech, sensory science, menu analytics
- Temporal: New studies, product launches, consumer behavior shifts
- Track: Academic papers, Tastewise updates, food trend reports, Nordic food innovation

### Agent 5: SEO Trends, Pain Points & Opportunities
- Search all `seo_painpoints` sources + Google Trends + Reddit + forums
- Focus: What are restaurant managers/franchise owners searching for RIGHT NOW?
- Temporal: Trending queries this week, recurring pain points, emerging needs
- Track: Reddit threads, forum discussions, search volume shifts, AI chat trends

---

## Phase 2: Synthesis (After ALL agents complete)

### 2.1 Deduplication & Cross-referencing
- Merge overlapping findings from multiple agents
- Verify claims against 2+ independent sources
- Flag single-source stories as "obekraftad" (unconfirmed)

### 2.2 Relevance Scoring
For each finding, score on:
- **Temporal relevance** (0-10): How recent? Is this breaking or background?
- **Flava relevance** (0-10): How directly does this affect Flava's product/market/strategy?
- **Reader value** (0-10): Would a Flava team member want to know this?

Threshold: Combined score >= 15 to make the newsletter. Top stories get expanded detail.

### 2.3 Delta Detection
- Compare against prior edition (if exists in `/output/`)
- Flag: "Previously reported: [topic] — UPDATE: [what changed]"
- Track narrative arcs across editions

### 2.4 Story Shaping
Each story must have:
1. **Headline** (max 12 words, Swedish, no clickbait)
2. **TL;DR** (1 sentence, what happened and why it matters)
3. **Detail** (2-4 paragraphs for the curious, expandable in HTML)
4. **Flava Relevance** (1 sentence: what this means for Flava specifically)
5. **Sources** (2+ URLs with publication names)
6. **Recency tag** (breaking / fresh / recent / background)

---

## Phase 3: Writing (Swedish, AI-Slop Certified)

### Writing Rules
1. **Swedish throughout** — native-level, not translated-feeling
2. **Zero em-dashes** — use commas, periods, or semicolons instead
3. **No "dessutom", "faktiskt", "intressant nog"** — filler words are banned
4. **No passive voice** unless quoting someone
5. **Short sentences** — max 25 words per sentence as a guideline
6. **Specific over vague** — "12% okning" not "en markant okning"
7. **Lead with the news** — first sentence is the story, not the context
8. **No corporate speak** — "de lanserade" not "de har genomfort en lansering av"
9. **Numbers in digits** — "3 restauranger" not "tre restauranger"
10. **Active subjects** — "ElevenLabs slappte" not "en ny version slapptes"

### Tone Check
Read every paragraph aloud (mentally). Does it sound like:
- A smart colleague telling you something over coffee? GOOD.
- A press release or LinkedIn post? REWRITE.
- A Wikipedia article? REWRITE.
- An AI chatbot? REWRITE IMMEDIATELY.

---

## Phase 4: Assembly (HTML Generation)

1. Load template from `templates/newsletter.html`
2. Fill placeholders with synthesized content
3. Generate unique edition number (YYYYMMDD-NN format)
4. Output to `output/flava-pulse-{edition}.html`
5. Also output raw data to `output/flava-pulse-{edition}.json` for archival/delta tracking

---

## Phase 5: Verification

Before publishing:
- [ ] All source URLs resolve (no dead links)
- [ ] Every story has 2+ sources
- [ ] No em-dashes in output
- [ ] Swedish reads naturally
- [ ] Expandable sections work
- [ ] All dates are correct relative to generation date
- [ ] Delta notes reference actual prior editions
- [ ] Source count in footer matches actual count
