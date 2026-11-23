# Account Radar — Sprinklr Service pipeline tool for APJI SDRs

**Type one account name. Get a validated, ready-to-send account pack.**

New here? Read [START-HERE.md](START-HERE.md) first. It takes 3 minutes. Leading the team? Read [ROLLOUT.md](ROLLOUT.md).

```
/account-radar DBS Bank
```

| You give | You get | Time |
|---|---|---|
| A logo | SDR brief (PDF, 20–30 pages) · Prospect infographic (PDF, 2 pages) · Outreach kit (copy-paste) | About 2–3 hours, in the background |

---

## The journey of one logo

```
 ① LOGO IN        ② RESEARCH          ③ VALIDATE         ④ SYNTHESISE       ⑤ BUILD + QA        ⑥ SDR SENDS
 ─────────  ──►  ─────────────  ──►  ─────────────  ──►  ─────────────  ──►  ──────────────  ──►  ───────────
 Account name     9 agents            5 agents            3 agents +         PDFs + layout        5 human checks
                  account level       fact check ×2       code joins the     gate + 3 content     then email,
                  department level    people check        verdicts           reviewers + editor   LinkedIn, call
                  personal level      ICP gate ■ STOP
                  channels, AI,       red team
                  incumbents, why now
```

■ The ICP gate can stop the run. A weak-fit account gets no content.

## What the SDR receives

| Asset | For | What is inside |
|---|---|---|
| **SDR brief** | The SDR. Internal | Snapshot and ICP score · 10-day play, step by step · why now · buying centres and contacts with openers · channels, volume, incumbents · journey map with break points · experience and AI maturity heatmaps · gap-to-capability map · business case · outreach sequences · customer's-eye test script · discovery questions · objections · validation stamp · open questions only a person can close · evidence log |
| **Prospect infographic** | The prospect | Outside-in journey view · questions worth testing at each stage · two maturity scales (a number only when enough is visible) · three ideas · value band when it rests on solid volumes · sources. No people, no vendor names, no guesses |
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
| G7 Content QA | 3 reviewer agents + editor + layout gate | Gaps, unbacked lines, long sentences, clipped pages |
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
| Colours, font, logo | `engine/theme/sprinklr.json`, with logo and font files in `engine/theme/brand/` |

## Set up once, for best results

| Setting | Why | Where |
|---|---|---|
| Network access for the cloud environment | Agents read far more, first-hand, when they can open the brand's own web pages. With the default limited network they work from search summaries only | Cloud environment menu → Edit → Network access. Add the brand's domains, or choose a broader level |
| GitHub connection | So changes to this tool can be pushed | claude.ai/connect-github, then install the Claude GitHub App on the repository |
| Connectors | Lusha for people. Semrush and LunarCrush for volume proxies | claude.ai connector settings |

## What the DBS pilot taught us

| Finding | What changed in the tool |
|---|---|
| Six research agents hit the shared web-search allowance | Agents plan searches first and report what they could not search. The command explains how to run a second pass |
| No DBS page could be opened in the pilot environment | Every such fact is marked "search summary". Quotes are never shown as verbatim. The brief lists what to open before sending |
| The red team blocked 62 findings | Verdicts and red-team blocks are joined to evidence by code. Agents cannot mark anything prospect-safe by hand |
| Only 14 of 80 maturity scores were visible from outside | The prospect sees the scale, not a number, when under 35% is visible. The gaps become live tests and discovery questions |
| The "prospect's eyes" reviewer would have ignored the first draft | Observations are phrased as questions to test. The SDR's own live tests are what make the view first-hand |

## Know the limits

| Limit | What it means |
|---|---|
| Outside-in only | Scores and volumes are estimates from public evidence. The brief says so on every page that shows them |
| Agents never contact the brand | The brief gives the SDR a 20-minute script to test as an ordinary member of the public. Sprinklr is never mentioned in a test. See `framework/08-live-test-rules.md` |
| Web access | Agents work from web search. Where direct page reads are blocked, evidence is marked "search summary" and capped at medium confidence |
| Brand | Colours, gradient and type rules follow the Sprinklr Brand Style Guide 2026. The logo and Proxima Nova files are not in this public repository: place them in `engine/theme/brand/` (git-ignored). Without them, packs use a text wordmark and the Inter font |
| Privacy | Real account folders are git-ignored. Only the fictional `_sample` account is committed. Follow local marketing and privacy rules before outreach |

## The SDR portal (no Claude Code needed)

SDRs who cannot open Claude Code use a web page hosted on Claude. They type an account, and a background runner builds the pack.

| Piece | Where | What it does |
|---|---|---|
| Portal page | `web/portal/portal.html`, published as a private Claude artifact | Request form, live status, pack files, next steps, live-test notes |
| Queue | The page's own database, collection `requests` | One row per request |
| Runner | `.claude/skills/portal-runner/SKILL.md`, started by an hourly scheduled task | Takes the oldest request, runs the workflow, uploads the files |
| Access | The page's Share menu | Invite people by email. Only invited people can open it |
| Prototype | `web/prototype/index.html` | A clickable mock with sample data |
