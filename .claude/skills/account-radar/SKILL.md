---
name: account-radar
description: Build a validated Sprinklr Service account pack for one enterprise logo. Use when an SDR gives an account name or says "run account radar", "research <company> for Sprinklr Service", "build a pack for <company>", or "/account-radar <company>". Produces an SDR brief PDF, a prospect-facing infographic PDF and an outreach kit.
---

# Account Radar — one logo in, one validated pack out

The SDR gives you an account name. You run the swarm, pass the gates, build the pack and hand it over. Speak to the SDR in short, plain sentences. Show progress as a table.

## 1. Take the input

- Input: the account name. Optional: market focus, notes ("we already sell them Social").
- Make the slug: lowercase, hyphens, e.g. `dbs-bank`.
- If the name is ambiguous (a group with many brands, or two companies with the same name), ask one question. Otherwise do not ask anything.
- If `accounts/<slug>/dossier.json` exists and is less than 30 days old, ask: refresh, or just rebuild the pack?

## 2. Run the swarm

Call the Workflow tool with the saved workflow:

```
Workflow({ name: "account-radar", args: { account: "<name>", slug: "<slug>", run_date: "<today YYYY-MM-DD>", region: "<markets>", notes: "<SDR notes>" } })
```

It runs in the background: 9 research agents, 5 validators, synthesis, build and 3 content reviewers. Tell the SDR it takes roughly 60 to 120 minutes and that they can keep working.

To run in stages, add `stop_after: "validate"` or `stop_after: "synthesise"`, then resume with `resumeFromRunId`.

### If agents report "search budget ran out"

Web search is a shared, limited allowance. When several agents report unsearched queries in their `gaps`:

1. Let the phase finish. Do not start validation on thin research.
2. Re-run the workflow with the same args and `resumeFromRunId`. Finished agents are skipped. For a thin file, delete it first so its agent runs again, or send that agent a gap-fill message listing its unsearched queries.
3. Tell the SDR in one line that a second pass is running and why.

## 3. Read the result

| Result | What you do |
|---|---|
| `stopped: "ICP gate"` | Tell the SDR the tier, the score and the reason. Do not build content. Suggest a re-score date |
| `stopped: "code gates"` | Run `python3 engine/validate.py accounts/<slug>/dossier.json`, fix the dossier per `swarm/briefs/S1-synthesise.md`, then build |
| `final.validation_passed` and `final.layout_passed` | Go to step 4 |
| Anything else | Read `accounts/<slug>/validation/*.json`, fix the dossier, run `python3 engine/build.py accounts/<slug>/dossier.json` |

Never edit templates to make one account fit. Shorten the dossier text.

## 4. Look before you hand over

1. Run `SHOTS=1 python3 engine/build.py accounts/<slug>/dossier.json` and view a few page images in `out/shots/`.
2. Read the prospect infographic once as the prospect. If any line would embarrass Sprinklr, fix it and rebuild.

## 5. Contact details (only if the SDR asks)

Emails and phones are never revealed by the swarm. If the SDR wants them:
1. Say what it costs first. Check the balance (`Lusha account_usage`).
2. Reveal emails for priority-1 contacts only, with Lusha `prospecting_contact_enrich` using the stored `lusha_id`.
3. Give them to the SDR in chat or push to their sales tool. Do not write them into the dossier or any committed file.

## 6. Hand over

Send the three files with SendUserFile:
`accounts/<slug>/out/sdr-brief.pdf`, `prospect-infographic.pdf`, `outreach-kit.md`.

Then give this summary, nothing longer:

| Item | Value |
|---|---|
| ICP fit | Tier and score |
| Experience index / AI index | Two numbers and level names |
| Three ways in | One line each |
| Contact this week | Count and names |
| Value at stake | Low to base, "illustrative" |
| Checked | Facts checked, corrected, dropped; people removed |
| Your next step | "Open the brief, page 2. Do the five checks before you send." |

## Guardrails

- Never send an email, message or connection request for the SDR. Draft only, and only when asked.
- Never contact the prospect's support channels. Live tests are the SDR's job, as an ordinary member of the public who never mentions Sprinklr. Rules: `framework/08-live-test-rules.md`.
- Never put contact details, or anything from `accounts/`, in git. `.gitignore` enforces this. Do not override it.
- Never present an estimate as a fact. Never claim a Gartner CCaaS Magic Quadrant position. See `framework/07-capability-map.md`.
- If a connector is unavailable or out of credits, continue without it and say what is missing.
