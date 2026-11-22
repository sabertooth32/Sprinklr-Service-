# 06 · The swarm — who does what

One account name in. Eighteen specialists. Eight gates. One pack out.

```
 SDR types the logo
        │
        ▼
┌─ RESEARCH (9 agents, parallel) ────────────────────────────────────────────┐
│ R1 Company & strategy   R2 Buying centres ──► R9 People (personal level)   │
│ R3 Incumbent tech       R4 Channels & volume  R5 Voice of customer         │
│ R6 Journey walk         R7 AI footprint       R8 Why now                   │
└───────────────────────────────┬────────────────────────────────────────────┘
                                ▼
┌─ VALIDATE (5 agents, parallel) ────────────────────────────────────────────┐
│ V1 Fact check: company, channels, volume    V2 Fact check: tech, AI, voice │
│ V3 People check    V4 ICP judge (gate)      V5 Red team                    │
└───────────────────────────────┬────────────────────────────────────────────┘
              Tier C or hard stop? ──► STOP. No content.
                                ▼
┌─ SYNTHESISE (3 agents + code gates) ────────────────────────────────────────┐
│ S1a + S1b + S1c write parts ─► code joins verdicts ─► validate.py (G5, G6)  │
└───────────────────────────────┬────────────────────────────────────────────┘
                                ▼
┌─ BUILD (code) ─────────────────────────────────────────────────────────────┐
│ build.py: SDR brief PDF · prospect infographic PDF · outreach kit          │
│ render.mjs: layout gate — no page may overflow                             │
└───────────────────────────────┬────────────────────────────────────────────┘
                                ▼
┌─ CONTENT QA (3 agents, parallel) ──────────────────────────────────────────┐
│ Q1 Completeness & traceability   Q2 Plain English   Q3 Prospect's eyes     │
└───────────────────────────────┬────────────────────────────────────────────┘
                                ▼
                    SDR: five human checks, then send
```

## Research agents

| Agent | Level | Answers | Main sources and connectors |
|---|---|---|---|
| R1 Company & strategy | Account | Is this our ICP? What does leadership want? | Annual report, results, web search, Lusha, Alpha Vantage |
| R2 Buying centres | Department | Who owns service decisions? | Lusha buying-group and contact search, leadership pages, press |
| R9 People | Personal | What has each person said? What is a true first line? | Interviews, talks, bylines, public posts |
| R3 Incumbents | Account | Which vendors run the stack today? | Vendor case studies, job adverts, press, technographics |
| R4 Channels & volume | Channel | Which channels exist? How many contacts? | Contact pages, disclosures, Semrush, LunarCrush |
| R5 Voice of customer | Channel | What do customers complain about and praise? | App stores, review sites, forums, news, regulators |
| R6 Journey walk | Journey | What does a customer meet at each stage? | Public help content. Writes the SDR's live-test script |
| R7 AI footprint | Channel | How much AI, how good, built or bought? | Press, executive talks, reviews |
| R8 Why now | Account | Why this quarter? | News, regulator notices, hiring signals, events |

## Validators

| Agent | Gate | Stance |
|---|---|---|
| V1, V2 Fact checkers | G1 | Try to break each claim. Re-search independently |
| V3 People check | G2 | Is each person still in role? Are quotes and openers true? |
| V4 ICP judge | G3 | Score from evidence only. Can stop the run |
| V5 Red team | G4 | Read as the prospect's service head and their lawyer |
| Q1–Q3 Content QA | G7 | Check the finished PDFs, not the data |

## Design rules

1. **Agents write files, not chat.** Each agent saves one JSON file. The next agent reads it.
2. **Briefs are plain text.** Change a brief in `swarm/briefs/` and the next run follows it. No code change.
3. **Validators did not do the research.** A separate agent, a separate search.
4. **Code decides what code can decide.** Maths, freshness, layout and content rules are scripts, not opinions.
5. **Re-runs are cheap.** An agent that finds its file already written for this run date skips the work.
6. **Agents read. Humans talk.** Agents never contact the prospect. Live tests are the SDR's job.
