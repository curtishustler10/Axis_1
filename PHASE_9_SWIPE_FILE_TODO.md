# Phase 9 TODO: Content Swipe File System

## Overview
Build an automated content swipe file system that:
- Scrapes competitor/industry content using Chrome automation
- Categorizes + tags using Claude AI
- Stores in searchable database
- Reusable for future content type additions

---

## PRE-FLIGHT (Get Input from Curt)

### Input Checklist
- [ ] **Sources to scrape** (3-10 URLs)
  - Competitor websites
  - Industry leaders
  - Ad copy libraries
  - Email sequences
  - Landing pages
  - _Example: "HubSpot blog, ConvertKit landing pages, Unbounce case studies"_

- [ ] **Content types to categorize**
  - Email subject lines
  - Ad headlines
  - Landing page copy
  - Social media hooks
  - Product descriptions
  - _Example: "Email openers, cold DMs, sales pages, testimonials"_

- [ ] **Tagging system preferences**
  - By tone (conversational, formal, urgent, etc.)
  - By framework (AIDA, PAS, storytelling, etc.)
  - By length (short, medium, long)
  - By industry/niche
  - _Example: "tag as #urgent-hook, #harry-dry, #short, #saas"_

---

## PHASE 9 EXECUTION

### Stage 1: Setup & Planning

- [ ] Create `/swipe-files/` directory structure:
  ```
  swipe-files/
  ├── raw/ (scraped content)
  ├── categorized/ (organized by type)
  ├── tagged/ (tagged with metadata)
  ├── database.json (searchable index)
  └── README.md (usage guide)
  ```

- [ ] Define tagging schema in JSON:
  ```json
  {
    "content_id": "email-001",
    "source": "HubSpot",
    "url": "https://...",
    "content_type": "email_subject",
    "text": "5 things nobody tells you about...",
    "tone": "curiosity",
    "framework": "listicle",
    "length": "short",
    "industry": "saas",
    "tags": ["#curiosity-hook", "#listicle", "#short"],
    "scraped_date": "2026-03-07",
    "rating": null
  }
  ```

- [ ] Set up Chrome automation config for scraping

---

### Stage 2: Scraping

**For each source URL:**

- [ ] Open URL with browser automation
- [ ] Extract all copyable text (headlines, subject lines, body copy)
- [ ] Save raw content to `/swipe-files/raw/{source_name}.json`
- [ ] Log metadata: URL, date scraped, content count
- [ ] Handle pagination if needed
- [ ] Store screenshots of high-converting sections

**Output:** Raw JSON files with source data

---

### Stage 3: Claude Analysis & Categorization

For each piece of scraped content, use Claude to:

- [ ] **Classify content type:**
  - Email subject / body
  - Ad headline / body
  - Landing page hero / CTA
  - Social media post
  - Cold outreach
  - Other

- [ ] **Identify tone:**
  - Conversational
  - Formal
  - Urgent
  - Humorous
  - Curiosity-driven
  - Pain-focused
  - Benefit-focused

- [ ] **Identify framework (Harry Dry):**
  - Problem-Agitate-Solve
  - AIDA
  - Storytelling
  - Listicle
  - How-to
  - Social proof
  - Scarcity/Urgency
  - Other

- [ ] **Extract key phrases:**
  - Opening hook
  - Main benefit
  - CTA text
  - Emotional trigger words

- [ ] **Auto-generate tags:**
  - Framework tags (#pas, #storytelling)
  - Tone tags (#urgent, #curious)
  - Length tags (#short, #medium)
  - Industry tags (if applicable)

**Output:** Categorized JSON with Claude annotations

---

### Stage 4: Database Organization

- [ ] Merge all categorized content into single `database.json`
- [ ] Index by:
  - Content type
  - Tone
  - Framework
  - Tags
  - Length
  - Industry

- [ ] Create metadata index:
  ```json
  {
    "total_items": 147,
    "by_type": {
      "email_subject": 45,
      "ad_headline": 52,
      "landing_page": 30,
      "cold_dm": 20
    },
    "by_tone": {...},
    "by_framework": {...},
    "last_updated": "2026-03-07"
  }
  ```

**Output:** Searchable JSON database

---

### Stage 5: Search Interface (CLI/Script)

Create `search-swipes.sh` script that allows:

```bash
# By tone
./search-swipes.sh --tone "urgent" --type "email_subject"

# By framework
./search-swipes.sh --framework "storytelling" --length "short"

# By tags
./search-swipes.sh --tags "harry-dry,curiosity-hook"

# Random sample
./search-swipes.sh --random --count 5
```

**Output:** Command-line tool for quick swipe retrieval

---

### Stage 6: Documentation & Training

- [ ] Create `SWIPE_FILE_README.md`:
  - How to search
  - How to add new content
  - Framework explanations
  - Best practices for using swipes

- [ ] Create `SWIPE_FILE_EXAMPLES.md`:
  - Top 10 highest-rated swipes
  - Broken down by category
  - Why they work (Harry Dry analysis)

- [ ] Update AGENTS.md with swipe file location + access

**Output:** User-facing docs

---

### Stage 7: Integration with Copywriting Workflow

- [ ] Add Claude prompt that references swipe database:
  ```
  "When writing copy, reference the swipe file database for similar successful frameworks.
  Search by tone/framework that matches the goal."
  ```

- [ ] Create workflow:
  1. Curt specifies goal (e.g., "urgent product launch email")
  2. I query swipe database for matching samples
  3. I show top 3 examples
  4. I write new copy using similar patterns
  5. Curt rates output (improves future matches)

---

## DELIVERABLES (Phase 9 Complete)

- [x] Scraped content from 3-10 sources (raw JSON)
- [x] Categorized database (database.json)
- [x] Search CLI tool (search-swipes.sh)
- [x] Documentation (SWIPE_FILE_README.md)
- [x] Integration with copywriting agent
- [x] Git commit with full phase

---

## REUSABILITY TEMPLATE

**When Curt says "add swipes for X":**

1. Get source URLs + content type from Curt
2. Run Stage 2 (Scraping) for new sources
3. Run Stage 3 (Claude Analysis) on new content
4. Merge into existing database.json
5. Regenerate metadata index
6. Commit to git

**Estimated time:** 20 mins per new source

---

## SUCCESS METRICS

- [ ] Database contains 100+ pieces of tagged content
- [ ] Search tool returns relevant results in <1s
- [ ] All content categorized across 3+ frameworks
- [ ] At least 80% of content has Harry Dry tags
- [ ] Copywriting workflow integrates swipe searches

---

## NOTES FOR FUTURE

- **Maintenance:** Update swipe database monthly with new sources
- **Ratings:** Add Curt's manual ratings to improve search ranking
- **Expansion:** Add video script swipes, SMS copy, etc. later
- **API:** Could build web interface if needed (later phase)
