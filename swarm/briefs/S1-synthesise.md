# S1 · Synthesis guide (shared by S1a, S1b and S1c)

**Mission:** turn validated research into `<work folder>/dossier.json`. The engine builds every SDR page and the prospect infographic from it. A junior SDR will act on every word.

Three agents each write one part. Code joins them:

| Agent | Writes | Sections |
|---|---|---|
| S1a Account and people | `<work folder>/parts/a.json` | `meta`, `snapshot`, `icp`, `why_now`, `buying_centres`, `contacts` |
| S1b Experience audit | `<work folder>/parts/b.json` | `channels`, `incumbents`, `journey`, `maturity`, `gap_map`, `mystery_shop` |
| S1c Commercial and content | `<work folder>/parts/c.json` | `entry_points`, `business_case`, `outreach`, `discovery_questions`, `objections`, `do_not_say`, `prospect_view`, and the gates in `meta.validation` |

## How evidence works (read this twice)
1. Run `python3 engine/digest.py <work folder>` once. It joins every finding with the validators' verdicts.
2. Read `<work folder>/digest/index-*.md` for your areas. One line per finding: id, verdict, SAFE or internal, type, confidence, date, claim, validator notes.
3. Read `<work folder>/digest/blocks/*.json` for the structured blocks (channels, stack, journey, people, scorecard, red-team issues).
4. In your part, **reference evidence by id only** (`"evidence": ["R4-25", "R7-04"]`). Do not write an `evidence` section. `engine/merge_parts.py` copies the records, so nobody can change a verdict or a prospect-safe flag by hand.
5. Need an estimate of your own, such as a channel volume? Add it under `extra_evidence` in your part: `{"id": "S-01", "claim": "...", "evidence_type": "inferred", "method": "how you worked it out", "source_date": "<run date>", "confidence": "low", "category": "volume"}`.
6. To hold a SAFE record back from the prospect, list its id under `not_prospect_safe`. You may restrict. You may never widen.
7. Records marked `internal` can support internal sections. They can never support `prospect_view`.
8. If every record is `via: search_summary`, no page was opened. Paraphrase facts. Never present a quote as verbatim in prospect content.

## Read first
1. `framework/01-icp.md`, `03-maturity-models.md`, `04-value-model.md`, `05-validation-gates.md`, `08-live-test-rules.md`.
2. `framework/data/sprinklr-service-facts.json` — the only Sprinklr capabilities, proof points and analyst facts you may use. Use capability `id`s exactly. Its `unverified` list is banned.
3. `engine/schema/dossier.schema.json` — the contract. `accounts/_sample/dossier.json` is a complete, passing example.

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
The digest already applies fact-check verdicts and red-team blocks to each finding. You apply them to the structured blocks: people, vendors, scores, themes. The counts in `meta.validation` are filled by code. S1c lists the gates G1 to G4 with status and a one-line note, and writes `meta.validation.limits`: 2 to 4 plain sentences on what this run could not do (for example: no page was opened, so every quote needs a live check).

## Section guide
| Section | What goes in | Limits |
|---|---|---|
| `snapshot` | One-liner, 4–6 headline facts, 2–4 strategic priorities with a "so what for service" | One-liner max 25 words. Fact values max 20 characters, e.g. "18.4M", "SGD 22.9B" |
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
| `mystery_shop` | 5–8 live tests from R6 the SDR runs as an ordinary member of the public. Follow `framework/08-live-test-rules.md`: general questions only, no claimed account, card, transaction or complaint, never the word Sprinklr | |
| `discovery_questions` | 6–10 open questions that test our hypotheses | |
| `objections` | 4–6 likely objections with a two-sentence response | Include "we build AI in-house" if true |
| `do_not_say` | Claims that would embarrass us. Always include banned Sprinklr claims that apply, plus: never say we tested or audited their contact centre; never share test screenshots or name their staff | |
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
- Mention the outside-in view as the reason to talk: "we looked at your service journey the way a customer sees it". Never write "we tested", "we audited" or "we mystery-shopped".
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

## Then pass the code gates (S1c does this, after a.json and b.json exist)
1. `python3 engine/merge_parts.py <work folder>` builds `dossier.json`. Fix any unknown evidence id in the part that used it.
2. `python3 engine/validate.py <work folder>/dossier.json`. Fix every FAIL in the part file that owns the section, merge again, and re-run until it exits 0.
3. Read the warnings and fix the cheap ones. Never weaken a fact to pass: remove the claim instead.

## Return
Your part's path, what you left out and why, and open questions for the SDR. S1c also returns whether the validator passed and its last lines.
