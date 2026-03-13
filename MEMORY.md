# MEMORY.md - AXIS Knowledge Base

---

## About Curtis

- **Name:** Curtis (Curt), based in Brisbane, Australia
- **Business experience:** ~5 years in e-commerce and digital marketing
- **Revenue:** Generated millions in e-commerce, spent millions on paid ads
- **Current businesses:**
  - **Digital Agency** — web dev, CRO, automation, funnels for SMBs
  - **COOLLOOKS23** — barbershop in Slacks Creek, QLD (client project, $900)
  - **Dropshipping** — high-ticket, Meta + TikTok traffic
- **Technical:** Builds with AI tools, runs everything with AI assistance
- **Work style:** High standards, values speed, prefers CLI-first
- **Language:** French native — refine English in client-facing content
- **Personality:** Builder, fast iteration, automation-focused

---

## Active Projects

### COOLLOOKS23 (Barbershop Website)
- **Status:** Deployed on Netlify, linked to CB23FAA repo
- **Last action:** Updated booking modal to match brand (black/gold), removed border-radius
- **Next step:** Verify deployment, check booking modal rendering

### Fidelis Agency (Copywriting)
- **Status:** Trained on Harry Dry framework
- **Next step:** Awaiting swipe file URLs from Curt (Phase 9)

### Booking System (PocketBase + n8n)
- **Status:** Running on DigitalOcean (170.64.153.193)
- **Last action:** Booking widget styled to match brand
- **Blocking:** Needs domain with SSL for HTTPS (frontend on Netlify can't call HTTP API)

### Admin Dashboard
- **Status:** Built and pushed to CB23FAA
- **URL:** /admin.html
- **Login:** coollooks123

---

## Ongoing Tasks

| Task | Status | Last Update | Next Action |
|------|--------|-------------|-------------|
| Phase 9: Content Swipe File | ⏳ Waiting | Mar 11 | Need 3-10 URLs from Curt |
| Stripe API Integration | ⏳ Waiting | Mar 9 | Need API keys from Curt |
| Booking API SSL fix | ⏳ Waiting | Mar 9 | Need domain with SSL |
| Browser automation | ⚠️ Blocked | Mar 11 | Headless Chrome blocked by bot protection |

---

## Decisions & Preferences

### Technical Stack
- **No OpenAI** — prefer Anthropic, open-source, or other providers
- **Preferred:** n8n, Supabase, React, Cloudflare, DigitalOcean
- **CLI-first** approach

### Rules
- **Always get approval first** — show prompt/plan, wait for Curt's go, then execute
- **Don't improvise** — If you cannot achieve a task the way it was requested, do NOT do it your way. Ask for clarification first.
- **Never execute externally** (emails, DMs, public posts) without confirmation
- **Refine, don't copy-paste** — client-facing content needs polishing

### Design Standards
- **COOLLOOKS23 brand:** Black (#000) + Gold (#D4AF37), sharp edges, italic gold headers
- **Booking modal:** Must match website landing page aesthetic

---

## Pending From Curtis

1. **3-10 URLs** for Phase 9 (content swipe file)
2. **Stripe API keys** for booking system
3. **Domain with SSL** to fix booking API (HTTPS → HTTP issue)

---

## Recent Commits (CB23FAA)

- `e333e11` — Remove border-radius from success icon
- `c226edd` — Update booking widget to match website brand
- `beeeb29` — Update gallery with Cloudinary images

---

## Session History

- **Mar 12, 15:20 UTC** — Session wrap-up: Added approval-first rule, session end triggers (thanks/done/bye = auto wrap-up), created session-wrap-up skill
- **Mar 12, 15:27 UTC** — Added Credentials & Keys section to MEMORY.md
- **Mar 12, 15:53 UTC** — Reviewed Code Editing Rules from AGENTS.md, confirmed understanding
- **Mar 13, 03:35 UTC** — Cleaned up AGENTS.md (removed duplicate Code Editing Rules), added HARD STOP RULE

---

## Credentials & Keys

### Servers
- **DigitalOcean droplet:** 170.64.153.193
- **SSH:** [NEEDED - user, key location]

### AI & APIs
- **MiniMax API key:** [NEEDED]
- **Gemini API key:** [NEEDED]
- **Google Cloud service account:** [NEEDED]

### Telegram
- **Bot:** @Openclaw88axisbot
- **Token:** 8638578625:AAGDlsocxSplP0nvIBmz5t2ia9Cq1QE0C_8

### Services (on droplet)
- **LiteLLM:** localhost:4000
- **Ollama shim:** localhost:11434
- **Chrome CDP:** localhost:18800
- **OpenClaw gateway:** localhost:18789
- **PocketBase:** 170.64.153.193:8090
- **n8n:** 170.64.153.193:5678
