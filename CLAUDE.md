# Account Radar — working rules for this repo

This repo is a tool for Sprinklr Service SDRs in APJI. One account name in, one validated account pack out.

## Map

| Path | What |
|---|---|
| `.claude/skills/account-radar/SKILL.md` | The SDR entry point: `/account-radar <company>` |
| `.claude/workflows/account-radar.js` | Orchestration: research → validate → synthesise → build → QA |
| `swarm/briefs/` | One plain-text brief per agent. Change behaviour here, not in code |
| `framework/` | ICP, evidence standard, maturity models, value model, gates, capability map |
| `framework/data/sprinklr-service-facts.json` | The only Sprinklr facts agents may use |
| `engine/` | Schema, code gates (`validate.py`), value model, templates, PDF renderer |
| `accounts/_sample/` | Fictional sample account, safe to commit |
| `accounts/<slug>/` | Real account work. Git-ignored. Never commit |

## Commands

```
python3 engine/validate.py accounts/<slug>/dossier.json    # code gates G5, G6
python3 engine/build.py accounts/<slug>/dossier.json       # HTML + PDF + outreach kit, runs the layout gate
SHOTS=1 python3 engine/build.py accounts/_sample/dossier.json   # also writes page images to out/shots/
```

## Rules

1. Real account data never goes into git. This repository is public.
2. Every claim needs a source and a date. Follow `framework/02-evidence-standard.md`.
3. Agents read public information only. They never contact a prospect or its support channels.
4. Never send outreach for an SDR. Draft only.
5. Prospect-facing text: no people, no vendor names, no inferred facts, sentences under 20 words.
6. Fix content in the dossier, not in the templates. Change templates only to improve every account.
7. After changing a template or the engine, rebuild `accounts/_sample` and look at the pages.
8. Writing style everywhere: short sentences, plain words, tables before paragraphs.
