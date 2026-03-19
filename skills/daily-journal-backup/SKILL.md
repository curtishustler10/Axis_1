---
name: daily-journal-backup
description: Compile daily journal from MEMORY.md and active-tasks.md, write a fresh summary, append to a Google Doc, and notify Curtis via Telegram.
---

# Daily Journal Backup

When triggered, do the following steps in order:

## Step 1 — Compile the journal entry
Read these files from your workspace:
- MEMORY.md (extract anything added or updated today)
- active-tasks.md (capture current state of all tasks)

## Step 2 — Write a fresh summary
Synthesise a daily journal entry in this format:

---
## Daily Journal — {today's date, Brisbane time}

### ✅ Achievements Today
(List anything completed or meaningfully progressed today based on MEMORY.md)

### 🔄 Pending Tasks
(List all active tasks from active-tasks.md with their current status)

### 🧠 Notes & Observations
(Any patterns, blockers, or insights worth remembering)
---

## Step 3 — Append to Google Doc
Use the browser tool to open Google Docs.
Navigate to the doc titled "OpenClaw Daily Journal" (create it if it doesn't exist).
Append today's journal entry to the top of the document.
Save.

## Step 4 — Notify via Telegram
Send Curtis a Telegram message in this format:

"📓 Daily Journal backed up — {date}

✅ [X tasks completed]
🔄 [X tasks pending]

Entry saved to Google Docs."
