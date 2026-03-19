---
name: promptEngineering
description: "Craft and refine prompts before launching Claude Code or AI tools. Triggered when user asks to write code, fix code, build, create, edit files, or use any AI tool."
---

# Prompt Engineering Skill

## When to Use This Skill

Trigger this skill when:
- User asks to write, fix, debug, edit, or run code
- User asks to build or create something (app, page, feature)
- User asks to use Claude Code
- Any task that will be handed to Claude Code for execution

## Workflow

1. **Analyze the request** — identify the file(s) involved, the exact change needed, and any constraints
2. **Engineer the Claude Code prompt** — specific, surgical, no options
3. **Show the prompt** — get Curtis's approval before sending prompt to Claude
4. **Execute** — only after approval, using the correct command

## Claude Code Prompt Rules

These are HARD rules for prompts sent to Claude Code:

- **File-first**: Always start with "Read [filename] in full."
- **Exact targets**: Name the specific CSS class, function, or element — never say "check" or "verify"
- **No options**: Do NOT list alternative approaches. Pick the best one and specify it.
- **Exact changes**: Say exactly what value to set, what to add, what to remove.
- **End with**: "Run git diff and show me the output after changes."

## Prompt Structure for Claude Code

