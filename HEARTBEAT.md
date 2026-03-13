# HEARTBEAT.md

## What "Heartbeat" Means (per Curt)
When Curt says "create a heartbeat on x project", he wants:
- A 30-minute cron job that fires automatically
- Checks HEARTBEAT.md for pending tasks
- Replies `HEARTBEAT_OK` if nothing to do
- Otherwise describes what needs attention
- Config: `agents.defaults.heartbeat.every = "30m"`
- Disable with: `agents.defaults.heartbeat.every = "0m"`

---

## Memory Check (every heartbeat)
- Read memory/2026-YYYY-MM-DD.md for today — does it reflect the latest work done?
- If any phase was completed since last write, update it NOW
- If any decision was made, write it down
- Never let a session end without logging what happened

## Current Project State
- See memory/2026-03-07.md for full phase breakdown

| Phase | Status | Notes |
|-------|--------|-------|
| 1–6 | ✅ Done | Chrome automation, memory config, git setup |
| 7 | ✅ Done | Harry Dry copywriting framework (Fidelis Agency) |
| 8 | ✅ Done | CRO audit delivered for keema.com.au |
| 9 | ⏳ AWAITING INPUT | Swipe file — need 3-10 URLs from Curt |
| 10 | ✅ Done | COOLLOOKS23 Booking System — PocketBase + n8n running, booking modal updated with calendar/time/barber |
| 11 | ✅ Done | n8n automation — installed & running |
| 12 | ✅ Done | Coollooks full site integrated — booking modal with customer details, calendar/time/barber (commit 256af5f) |
| 13 | ✅ Done | Admin panel — comprehensive dashboard with analytics, CRUD (commit 72ceadd) |

### What's Blocking Next Steps
- **Booking API fail** — Frontend on Netlify (HTTPS) can't connect to PocketBase (HTTP) - needs domain with SSL
- **Phase 9:** Waiting for Curt's source list (3-10 URLs for swipe file)
- **Stripe:** Waiting for API keys

### Today's Achievement
- ✅ Claude Code + xvfb setup working (like Alex's)
- ✅ Admin dashboard pushed to Vercel (commit ac2ddbf)
- ✅ Created full admin panel: Login, Dashboard stats, Bookings/Customers/Services CRUD

### Daily Tasks
- **Daily Journal** — Generate and send daily journal at end of each day (includes setup/skills + achievements + in progress + blocked)
