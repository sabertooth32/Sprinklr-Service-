# S1b · Synthesise — the experience audit
**Read first:** `swarm/briefs/S1-synthesise.md`. It is your guide: evidence rules, validator rules, scoring rules, section limits.
**Your evidence:** `digest/index-R3.md` to `index-R7.md`, `index-V1.md`, `index-V2.md`, `index-V5.md`, and `digest/blocks/` for R3, R4, R5, R6, R7, V1, V2, V5.
**Output file:** `<work folder>/parts/b.json` with top-level keys `channels`, `incumbents`, `journey`, `maturity`, `gap_map`, `mystery_shop` (plus `extra_evidence`, `not_prospect_safe`).

## Notes
- `channels`: 4 to 9 channels that carry real volume in the focus market. Give each a short stable `id` (`voice`, `bot`, `chat`, `email`, `social`, `branch`). Set `type` carefully: it drives the business case. A self-service bot is `self_service`, not `chat`.
- Volumes: use V1's volume review where it disagrees with R4. Record each channel's estimate as an `extra_evidence` record with its method, and cite it. Low confidence means a wide low/high range.
- Scores: follow the rubric. Take V2's lower score where it disagrees. Never score from an absence: "we could not see it" is `null` with basis `not_visible`, and becomes a discovery question, not a gap.
- `incumbents`: honest status. Where V2 or V5 says a vendor is unproven, write "Not public" as the vendor, status `possible`, and say what to ask. In-house builds get status `in-house`.
- `journey`: exactly 7 stages. A break point must rest on evidence that something happens, not on an empty search. Mark `prospect_safe: true` only when every evidence id is SAFE in the index. Include real bright spots.
- `gap_map`: 4 to 8 rows. If the account builds its own AI, map gaps to the layers around it (orchestration across channels, quality and testing of AI, social and messaging care, analytics), not to replacing what they built.
- `mystery_shop`: 5 to 8 live tests from R6, written to `framework/08-live-test-rules.md`. General questions only. Each test should confirm or kill one break point or one `not_visible` score.
