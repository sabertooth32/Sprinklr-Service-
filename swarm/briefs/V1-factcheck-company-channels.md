# V1 · Fact check — company, channels, volume, triggers
**Mission:** try to break the findings in R1, R4, R6 and R8. You are a sceptic, not a fan.
**Input:** `<work folder>/research/R1-company.json`, `R4-channels-volume.json`, `R6-journey-walk.json`, `R8-why-now.json`.
**Also read:** `framework/05-validation-gates.md`.
**Output file:** `<work folder>/validation/V1-factcheck-company-channels.json`

## Method
1. Rank findings by how much the SDR pack will lean on them. Check the top 35 at least. Always check: every number, every channel's existence and hours, every trigger date, every quote.
2. For each: search again independently. Does a source say this? Is the date right? Is there a second, independent source?
3. Re-do the volume maths. Are the assumptions reasonable against any disclosed numbers? Give your own low / base / high if you disagree.
4. Give a verdict per finding: `confirmed`, `corrected` (give the corrected claim), `unverified`, `stale`, `refuted`.

## Extra block
`verdicts`: [{finding_ref, verdict, note, corrected_claim, second_source_url}]
`volume_review`: {agree: true|false, comment, suggested{low, base, high}}
`not_checked`: [finding ids you did not get to — no silent caps]
