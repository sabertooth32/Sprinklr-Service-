# S1c · Synthesise — commercial case, outreach and the prospect view
**Runs after S1a and S1b.** Read `<work folder>/parts/a.json` and `parts/b.json` first. Build on them. Do not contradict them.
**Read first:** `swarm/briefs/S1-synthesise.md`. It is your guide: evidence rules, outreach rules, prospect-view rules, code gates.
**Your evidence:** the two parts, `digest/blocks/V4-icp-judge.json` (entry points), `digest/blocks/V5-red-team.json` (issues, safe list, tone guidance), any `digest/index-*.md` you need, and `framework/data/sprinklr-service-facts.json`.
**Output file:** `<work folder>/parts/c.json` with top-level keys `entry_points`, `business_case`, `outreach`, `discovery_questions`, `objections`, `do_not_say`, `prospect_view`, and `meta` holding only `{"validation": {"gates": [...], "limits": [...]}}`.

## Notes
- `entry_points`: exactly 3, from V4's ranked list, adjusted for V5's blocks. Each names a pain, a buying centre, a why-now and Sprinklr capabilities by id, with one proof point from the facts file.
- `business_case`: country code for agent cost, agent estimate, 4 to 7 KPIs, assumptions, upside not counted. Never write a value number: the engine computes them from the channel volumes in part b.
- `outreach`: 2 to 4 sequences by persona, named for the buying centres in part a. Follow V5's tone guidance for this account. Lead with respect for what they built.
- `prospect_view`: use only ids marked SAFE in the index. Strengths first. Observations are phrased as what a customer sees and as questions to test, never as verdicts. Opportunities are "what good looks like".
- `do_not_say`: include every V5 `block` that an SDR could repeat by accident, the banned Sprinklr claims, and the live-test rule.
- `meta.validation.gates`: G1 Facts, G2 People, G3 ICP, G4 Red team. Status and a one-line note each, using the numbers in `digest/stats.json`.
- `meta.validation.limits`: what this run could not do.
- `open_questions` (top level, max 12): points only a person can settle before sending. One short, actionable sentence each. Start with a verb: "Open...", "Read...", "Check...".
- `glossary` (top level, max 8): account-specific words a new SDR will not know, such as the regulator's name or the brand's product names. `{term, meaning}`, meaning max 8 words.
- `prospect_view.opportunities_title` and `opportunities_subtitle` (optional): a respectful page-two headline for this account.

## Then
Run the code gates as the guide describes: merge, validate, fix, repeat until `engine/validate.py` exits 0.
