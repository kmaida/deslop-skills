# Deslop Skills for AI agents

[![skills.sh](https://skills.sh/b/kmaida/deslop-skills)](https://skills.sh/kmaida/deslop-skills)

Skills are invoked with `/deslop-` and are designed to help AI agents produce frontend designs (`/deslop-ui`) and written content (`/deslop-writing`) that avoid common gen-AI patterns.

## Deslop UI

Avoids tells like side accent bars, eyebrows, excessive rounded corners, status indicators, etc. Can and should be used in conjunction with other design skills, such as [Impeccable](https://impeccable.style).

## Deslop Writing

Avoids tells like parataxis, em dashes, unnecessary qualifiers, decorative headings, banned words, etc. Can and should be used in conjunction with your own writing guide, which you should train on samples of your personal writing, blogging, speaking, docs, etc.

## Installation

Install with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add kmaida/deslop-skills
```

This prompts you to pick skills and target agents (Claude Code, Codex, Cursor, and others). To install one skill, pass `--skill`:

```bash
npx skills add kmaida/deslop-skills --skill deslop-ui
```

```bash
npx skills add kmaida/deslop-skills --skill deslop-writing
```

Add `-g` to install globally (user directory) instead of the current project.

For platforms that can use zip uploads (such as claude.ai), you can alternately zip the `/deslop-ui` and/or `/deslop-writing` folders individually and upload them to your skills source.
