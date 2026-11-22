# Account Radar — Sprinklr Service pipeline tool for APJI SDRs

**Type one account name. Get a validated, ready-to-send account pack.**

```
/account-radar DBS Bank
```

| You give | You get | Time |
|---|---|---|
| A logo | SDR brief (PDF, ~17 pages) · Prospect infographic (PDF, 2 pages) · Outreach kit (copy-paste) | 60–120 min, in the background |

---

## The journey of one logo

```
 ① LOGO IN        ② RESEARCH          ③ VALIDATE         ④ SYNTHESISE       ⑤ BUILD + QA        ⑥ SDR SENDS
 ─────────  ──►  ─────────────  ──►  ─────────────  ──►  ─────────────  ──►  ──────────────  ──►  ───────────
 Account name     9 agents            5 agents            1 agent +          PDFs + layout        5 human checks
                  account level       fact check ×2       code gates         gate + 3 content     then email,
                  department level    people check        dossier.json       reviewers            LinkedIn, call
                  personal level      ICP gate ■ STOP
                  channels, AI,       red team
                  incumbents, why now
```

■ The ICP gate can stop the run. A weak-fit account gets no content.

## What the SDR receives

| Asset | For | What is inside |
|---|---|---|
| **SDR brief** | The SDR. Internal | Snapshot and ICP score · 10-day play, step by step · why now · buying centres and contacts with openers · channels, volume, incumbents · journey map with break points · experience and AI maturity heatmaps · gap-to-capability map · business case · outreach sequences · mystery-shop script · discovery questions · objections · validation stamp · evidence log |
| **Prospect infographic** | The prospect | Outside-in journey view · moments that matter · two maturity indexes · three opportunities · value band · sources. No people, no vendor names, no guesses |
| **Outreach kit** | Copy and paste | First lines per contact · email, LinkedIn and call sequences per persona |

Open `sdr-brief.html` in a browser for the same brief with navigation and copy buttons.

## Three levels of research

| Level | Question | Agents |
|---|---|---|
| **Account** | Is this our ICP? Why now? What runs their stack? | Company & strategy · Why now · Incumbents |
| **Department** | Which buying centres own service? Who sits in them? | Buying centres |
| **Personal** | What has each person said in public? What is a true first line? | People |
| **Experience audit** | Which channels, what volume, where does it break, how much AI? | Channels & volume · Voice of customer · Journey walk · AI footprint |

## Two maturity indexes

| Index | Scores each channel on | Levels |
|---|---|---|
| **Experience** | Access · Speed · Resolution · Continuity · Personal | Fragmented → Functional → Connected → Orchestrated → Predictive |
| **AI** | Self-service AI · Agent assist · Smart routing · Insight & quality · Trust & control | No AI → Rule-based → Assisted → Generative → Agentic → Autonomous |

Every score cites evidence. Anything not visible from outside is left blank and becomes a discovery question.

## Eight gates before anything is sent

| Gate | By | Stops |
|---|---|---|
| G1 Facts | 2 fact-check agents | Wrong, stale or single-source claims |
| G2 People | People-check agent | Contacts who moved or left |
| G3 ICP | ICP judge agent | Weak-fit accounts |
| G4 Red team | Red-team agent | Overclaims, unfair or risky wording |
| G5 Dossier | `validate.py` | Missing sources, bad maths, stale evidence |
| G6 Content rules | `validate.py` | Inferred facts, names or vendors in prospect content |
| G7 Content QA | 3 reviewer agents + layout gate | Gaps, long sentences, clipped pages |
| G8 Human | The SDR, 5 minutes | Anything that changed since the run |

## Business case

Five levers, applied in order, no double counting: AI resolution · fewer repeat contacts · voice to messaging · faster handling · automated quality.
Three scenarios. The SDR leads with **low**. Every input is labelled disclosed, benchmark or estimate. Rates live in `engine/value_defaults.json`.

## Connectors used

| Connector | Used by | For |
|---|---|---|
| Web search | All agents | Primary research and independent re-checks |
| Lusha | Buying centres, people check | Buying group, titles, current employer. Email reveal only on SDR request |
| Semrush · LunarCrush | Channels & volume, voice of customer | Help-site traffic and social volume as volume proxies |
| Alpha Vantage | Company & strategy | Listed-company overview and earnings calls |
| Apollo · Sprouts · Clay · Vibe Prospecting · G2 | Optional | Technographics, signals, sequences |
| Gmail | Optional, on request | Save outreach as drafts. Never auto-send |

A missing connector never blocks a run. The agent notes the gap and moves on.

## Run it

| Step | Command |
|---|---|
| Full run | `/account-radar <company>` in Claude Code or Cowork, opened on this repo |
| Rebuild a pack | `python3 engine/build.py accounts/<slug>/dossier.json` |
| Check a dossier | `python3 engine/validate.py accounts/<slug>/dossier.json` |
| Try the sample | `python3 engine/build.py accounts/_sample/dossier.json` |

Needs: Python 3 with `jinja2` and `jsonschema`, Node with Playwright and Chromium.

## Change it without code

| To change | Edit |
|---|---|
| What an agent looks for | `swarm/briefs/<agent>.md` |
| Who we sell to, how we score fit | `framework/01-icp.md` |
| Maturity rubrics | `framework/03-maturity-models.md` |
| Business-case rates and unit costs | `engine/value_defaults.json` |
| Sprinklr capabilities and proof points | `framework/data/sprinklr-service-facts.json` |
| Colours, font, logo | `engine/theme/sprinklr.json` |

## Know the limits

| Limit | What it means |
|---|---|
| Outside-in only | Scores and volumes are estimates from public evidence. The brief says so on every page that shows them |
| Agents do not test live channels | The brief gives the SDR a 20-minute script to test as a real person |
| Web access | Agents work from web search. Where direct page reads are blocked, evidence is marked "search summary" and capped at medium confidence |
| Brand | The theme approximates Sprinklr's look. Drop the official logo and colours into `engine/theme/sprinklr.json` |
| Privacy | Real account folders are git-ignored. Only the fictional `_sample` account is committed. Follow local marketing and privacy rules before outreach |
