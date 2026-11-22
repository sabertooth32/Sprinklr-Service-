# S1 · Synthesise the dossier

**Mission:** turn validated research into ONE file, `<work folder>/dossier.json`. The engine builds every SDR page and the prospect infographic from it. A junior SDR will act on every word.

## Read first
1. `framework/01-icp.md`, `03-maturity-models.md`, `04-value-model.md`, `05-validation-gates.md`.
2. `framework/data/sprinklr-service-facts.json` — the only Sprinklr capabilities, proof points and analyst facts you may use. Use capability `id`s exactly. Read its `unverified` list: those claims are banned.
3. Everything in `<work folder>/research/` and `<work folder>/validation/`.
4. `engine/schema/dossier.schema.json` — the contract. `accounts/_sample/dossier.json` shows a complete example if it exists.

## Apply the validators before you write anything
| Validator said | You do |
|---|---|
| `refuted` | Delete the finding. Do not use it anywhere |
| `corrected` | Use the corrected claim |
| `unverified`, `stale` | Internal sections only. `prospect_safe: false` |
| V3 `moved` / `unknown` / in `remove_from_outreach` | Leave the person out of `contacts` |
| V4 `irrelevant_findings` | Drop |
| V5 `block` | Fix or delete. V5 `internal_only` → `prospect_safe: false` |
| V2 score review | Take the lower score |
Count what you did for `meta.validation` (facts checked, confirmed, corrected, dropped, people checked, people removed). List the gates G1–G4 with status and a one-line note.

## Section guide
| Section | What goes in | Limits |
|---|---|---|
| `evidence` | Only findings you actually reference. Keep the research ids (`R4-07`). Set `category`, `verdict`, `stale`, `prospect_safe` | `prospect_safe` only if confirmed or corrected, not inferred, not low confidence, dated, fresh |
| `snapshot` | One-liner, 4–6 headline facts, 2–4 strategic priorities with a "so what for service" | One-liner max 25 words |
| `icp` | V4's scorecard. Nine lines, in framework order | Verdict max 25 words |
| `why_now` | 3–7 dated triggers, most urgent first | `so_what` max 18 words |
| `entry_points` | Exactly 3. Pain + buying centre + why now + Sprinklr capability + one proof point from the facts file | Title max 8 words |
| `buying_centres` | 3–7 centres present at this account | |
| `contacts` | Validated people only. Priority 1 = contact this week (5–8 people), 2 = second wave, 3 = map only | Hook max 20 words. Opener max 25 words |
| `channels` | 4–9 channels that carry real volume. `type` drives the value model. Scores per the maturity rubric, each with evidence. `null` when not visible | `headline_gap` and `strengths` max 14 words |
| `incumbents` | One row per stack layer found. Honest status | |
| `journey` | Exactly 7 stages. Verdict per stage. Break points with channel, severity, capability, evidence. Bright spots too | `what_breaks` max 16 words |
| `maturity` | Two headlines, 2–4 genuine strengths, one confidence note | |
| `gap_map` | 4–8 gaps → Sprinklr capability → outcome → proof. Priority 1 = lead with this | |
| `business_case` | Country code for agent cost, agent estimate, 4–7 KPIs (today → target), assumptions, upside not counted | Never put value numbers in text. The engine computes them |
| `outreach` | 2–4 sequences by persona. 4–5 steps each over about 10 working days: email, LinkedIn, call | Email max 90 words, 4 short paragraphs. LinkedIn max 45 words. Call opener max 70 words |
| `mystery_shop` | 5–8 live tests from R6 the SDR runs personally | |
| `discovery_questions` | 6–10 open questions that test our hypotheses | |
| `objections` | 4–6 likely objections with a two-sentence response | Include "we build AI in-house" if true |
| `do_not_say` | Claims that would embarrass us. Always include banned Sprinklr claims that apply | |
| `prospect_view` | Outside-in infographic content | See below |

## Scoring rules
- Score every channel on the 5 experience and 5 AI dimensions using the rubric. Half points allowed.
- `basis`: `observed`, `disclosed`, `inferred`, or `not_visible` with `score: null`.
- When torn, take the lower score. Never score without an evidence id.
- Be fair. If the account is strong somewhere, score it high and say so. A credible pack names strengths.

## Outreach writing rules
- Lead with what we observed about their customers' experience, not with Sprinklr.
- One idea per message. One clear, small ask.
- No flattery. No "I hope this finds you well". No hype words: revolutionary, game-changing, leverage, synergy, cutting-edge, seamless.
- Mention the outside-in view as the reason to talk: "we mapped your service journey from the outside".
- Never quote a value number in outreach. Offer to walk through the model.
- Use `{{first_name}}` and `{{sdr_name}}` as merge fields.

## Prospect view rules (this is what the customer sees)
- Framing: respectful, outside-in, "a first view to test with you".
- 2–3 strengths first. Real ones, with evidence.
- 3–5 observations, each tied to a journey stage and to `prospect_safe` evidence only.
- 3 opportunities phrased as "what good looks like".
- No people. No vendor names. No internal scores they could dispute as fact; indexes are labelled outside-in estimates.
- No words like fail, broken, poor, bad, worst.
- Sentences max 20 words.

## Then pass the code gates
Run `python3 engine/validate.py <work folder>/dossier.json`. Fix every FAIL and re-run until it exits 0. Read the warnings and fix those that are cheap. Do not weaken a fact or flip `prospect_safe` just to pass: remove the claim instead.

## Return
The dossier path, whether the validator passed, its last lines, what you dropped and why, and open questions for the SDR.
