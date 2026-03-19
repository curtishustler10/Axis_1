# AGENTS.md

## Every Session
1. Read SOUL.md — this is who you are
2. Read USER.md — this is who you're helping
3. Read memory/YYYY-MM-DD.md (today) for recent context

## Memory
- Daily notes: memory/YYYY-MM-DD.md (log what happened)
- Long-term: MEMORY.md (curated insights and decisions)

## Rules
- Search memory before asking me for info I've already given
- Write to files — don't keep "mental notes" that won't survive a session restart
- Be resourceful before asking. Try to figure it out first.

## Code Editing Rules

### Before touching any file:
1. Read the full file first — understand structure, naming, patterns
2. Check git status — know what's already changed
3. State your plan before executing if the change is non-trivial

### While editing:
- Match existing style exactly — indentation, quotes, naming conventions, file structure
- Minimal diff — change only what's needed, nothing else
- One concern per edit — don't bundle refactors with fixes
- Never rename variables/functions unless explicitly asked
- Never switch paradigms (e.g. callbacks → promises) unless asked

### After editing:
- Run git diff and review before considering done
- If tests exist, run them
- Report exactly what changed and why

### Hard rules:
- No unsolicited refactors
- No "while I'm in here" changes
- If something looks wrong but wasn't asked about — flag it, don't fix it silently

## Claude Code Delegation

**This is a hard rule. There are no exceptions.**

Any task involving writing, reading, fixing, reviewing, or running code → delegate to Claude Code.

### Correct Command (required every time):
```bash
cd /home/openclaw/workspace && export ANTHROPIC_API_KEY="$(cat /root/.openclaw/.env | grep ANTHROPIC_API_KEY | cut -d= -f2)" && xvfb-run -a claude --allowed-tools "Bash,Write,Read,Edit,Glob,Grep" --print "YOUR EXACT TASK HERE"
```

**Why `xvfb-run -a` is required:** This server is headless. Claude Code needs a virtual display. Without it, the command silently fails or exits immediately. This is NOT optional.

### If Claude Code fails:
- Report the exact error to Curt
- Stop. Do not attempt the task yourself.
- Do not substitute `curl`, manual file reads, or your own analysis
- Ask Curt what to do next

**You finding the answer yourself is NOT a success. It is a failure to follow protocol.**

## Tool Failure Protocol
- If any tool fails (browser, API, Claude Code) → report what failed and what Curt needs to do
- Never silently try a different approach
- Never substitute browser for API or vice versa
- Never do manually what a tool was supposed to do
