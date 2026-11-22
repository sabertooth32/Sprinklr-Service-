# 05 · Validation gates — nothing reaches a prospect unchecked

Eight gates. Five by agents, two by code, one by the SDR.

| Gate | Who | Checks | Fails when | On fail |
|---|---|---|---|---|
| **G1 Facts** | Fact-check agents (2) | Re-open each key source. Does it say what we claim? Is the date right? Is there a second source? | Source missing, misread, or out of date | Correct, downgrade, or drop |
| **G2 People** | People-check agent | Is each contact still in that role today? Name, title, market | Moved, left, or cannot confirm | Remove from outreach list |
| **G3 ICP** | ICP judge agent | Scores the scorecard from evidence only. Applies hard stops | Tier C or a hard stop | Stop. No content |
| **G4 Red team** | Red-team agent | Reads as the prospect's lawyer and as their Head of Service. Hunts overclaims, insults, guesses shown as facts | Any claim the prospect could prove wrong | Rewrite or drop |
| **G5 Dossier** | `engine/validate.py` | Schema, sources, freshness, score ranges, evidence links, maths | Any error | Synthesis agent fixes and re-runs |
| **G6 Content rules** | `engine/validate.py` | Prospect content uses only confirmed, non-inferred facts. Sentence length. No internal data leaks | Any error | Rebuild |
| **G7 Content QA** | QA agents (3) | Completeness vs. checklist. Plain English. Prospect-lens read of the final PDF | Missing section, long sentence, risky wording | Fix and re-render |
| **G8 Human** | The SDR, 5 minutes | Five checks below | Any "no" | Do not send |

## What "validated" means for a single fact

| Verdict | Meaning | Prospect content? |
|---|---|---|
| `confirmed` | Source re-read, says it, fresh | Yes |
| `corrected` | Wrong in detail, fixed | Yes, corrected text |
| `unverified` | Could not re-open or find a second source | Internal only |
| `stale` | True once, too old | Internal only |
| `refuted` | Wrong | Deleted |

## G8 — the SDR's five checks before sending

| # | Check | Time |
|---|---|---|
| 1 | Open the contact's LinkedIn. Same role today? | 1 min |
| 2 | Do one live test as an ordinary customer (never as Sprinklr). Does the break point still happen? | 2 min |
| 3 | Open the source of each fact you use. Still true? Any news in the last 7 days? | 2 min |
| 4 | Check CRM. Open opportunity or existing owner? | 30 s |
| 5 | Read the message aloud. Would you send it to a friend who works there? | 30 s |

## Completeness checklist (G7)

**SDR brief must have:** account snapshot and ICP score · why now · buying centres · contacts with hooks · channels and volume · incumbents · journey map with break points · experience and AI maturity · gap-to-capability map · business case · step-by-step play · outreach copy · mystery-shop script · discovery questions · objections · evidence log · validation stamp.

**Prospect infographic must have:** outside-in framing · journey with break points · two maturity indexes · three opportunities · value band (low scenario) · sources · one clear call to action. **Must not have:** contact names, incumbent guesses, internal scores, anything inferred.
