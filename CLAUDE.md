# Flava Pulse — Newsletter Agent

## What This Is
An automated newsletter generation system for Flava, a preference intelligence platform targeting the restaurant and hospitality industry. Subject-agnostic: swap config and sources for any industry.

## Directory Structure
```
Flava-agent/
├── CLAUDE.md
├── skills/
│   ├── parent/
│   │   └── newsletter-orchestrator.md   # Master orchestrator skill
│   ├── research/
│   │   ├── research-protocol.md         # Shared research methodology
│   │   ├── tech-ai.md                   # Agent 1: Tech & AI
│   │   ├── hospitality.md               # Agent 2: Restaurant & Hospitality
│   │   ├── pos-competitors.md           # Agent 3: POS & Competitors
│   │   ├── taste-preference.md          # Agent 4: Taste Science
│   │   └── seo-painpoints.md            # Agent 5: SEO & Pain Points
│   ├── synthesis/
│   │   └── synthesize.md                # Scoring, dedup, 5 Whys, cost-benefit
│   ├── writing/
│   │   └── write-swedish.md             # Swedish writing rules, AI-slop filter
│   ├── verification/
│   │   └── verify.md                    # QA pass: sources, claims, language
│   └── delta-tracking/
│       └── delta-tracker.md             # Cross-edition intelligence
├── templates/
│   └── newsletter.html                  # Things 3-inspired HTML template
├── scripts/
│   ├── generate-newsletter.md           # Generation protocol
│   ├── synthesis-prompt.md              # Synthesis engine prompt
│   └── story-template.html              # Story card HTML component
├── sources/
│   └── registry.json                    # 48+ verified source registry
└── output/
    ├── flava-pulse-*.html               # Generated newsletters
    ├── flava-pulse-*.json               # Archived data for delta tracking
    └── delta-log.json                   # Cross-edition tracking state
```

## Execution: `/newsletter`

### Phase 0: PREPARE
Load source registry, load prior edition for delta tracking, determine date.

### Phase 1: RESEARCH (5 agents in parallel)
Each agent follows `skills/research/research-protocol.md`:
1. Tech & AI (voice, avatars, LLMs, real-time tech)
2. Restaurant & Hospitality (Sweden primary, then DE, UK, US cities, CA)
3. POS & Competitors (Trivec ecosystem, Toast, market intelligence)
4. Taste Science & Preference Intelligence (flavor profiling, food innovation)
5. SEO & Pain Points (what restaurant managers search for, forum sentiment)

### Phase 2: SYNTHESIZE (after ALL agents return)
- Deduplicate, score (temporal + impact + reader value), threshold (>= 15)
- 5 Whys on top stories (>= 22), cost-benefit on actionable items
- Delta detection vs. prior edition
- See `skills/synthesis/synthesize.md`

### Phase 3: WRITE (Swedish, AI-slop certified)
- Natural Swedish, zero em-dashes, active voice, short sentences
- Informed-colleague tone, no corporate speak
- See `skills/writing/write-swedish.md`

### Phase 4: VERIFY
- Source URLs, claim double-check, 5 Whys validation, language QA
- See `skills/verification/verify.md`

### Phase 5: ASSEMBLE
- Fill HTML template, generate edition number, output HTML + JSON archive

## Critical Rules
1. **Temporal anchoring**: Every search includes date context
2. **Delta tracking**: Compare against prior editions, track arcs
3. **Swedish output**: Native-level, down-to-earth Swedish
4. **AI-slop certified**: Zero em-dashes, no filler, no corporate speak
5. **Source verification**: 2+ independent sources per story
6. **5 Whys**: Applied to all feature stories (score >= 22)
7. **Cost-benefit**: Applied to all actionable findings
8. **Reusable**: Subject/topic is parameterized

## Research Methodology
See `skills/research/research-protocol.md` for:
- Source qualification tiers (1-4)
- Claim verification standards
- 5 Whys analysis framework
- Cost-benefit analysis framework
- Delta tracking protocol
- Temporal anchoring rules
- Output format specification
