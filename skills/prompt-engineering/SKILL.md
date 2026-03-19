---
name: prompt-engineering
description: "Craft and refine prompts for generative AI tools. Use before launching coding agents, image generators, or other AI tools. Triggered when user asks to generate code, create app, build something, write code, create image, or use AI tools."
---

# Prompt Engineering Skill

## When to Use This Skill

This skill triggers when:
- User asks to "generate code", "create app", "build something", "write code"
- User asks to "create image", "generate image", "make image"
- User asks to use any AI tool (coding agent, image generator, etc.)
- Any task that will be executed by another AI model

## Workflow

1. **Analyze the user's task** — Break down what they want into clear requirements
2. **Craft a detailed prompt** — Include context, constraints, format, examples
3. **Show the prompt to user** — Get confirmation before execution
4. **Execute the AI tool** — Only after user approves the prompt

## Prompt Structure Guide

When crafting prompts for coding agents, include:

```
## Task
[What to build/create]

## Context
[Any background info, existing code, constraints]

## Requirements
- [Specific requirement 1]
- [Specific requirement 2]

## Output Format
[How the code/output should be structured]

## Examples
[Any specific examples of desired output]
```

## Anthropic API (for coding agent)

When executing coding tasks, use Claude Code with API key:
```bash
ANTHROPIC_API_KEY=sk-ant-... claude "Your prompt here"
```

The API key will be provided by the user.

## Confirmation Template

Before executing, show user:

---
**Prompt for AI Tool:**

```
[Your crafted prompt here]
```

**Confirm?** Reply with "yes" to execute, or describe changes you want.
---

## Rules

- Never execute AI tools without user confirmation of the prompt
- Make prompts specific and actionable
- Include context about the project/environment
- Specify output format expectations
- Add constraints or requirements clearly
