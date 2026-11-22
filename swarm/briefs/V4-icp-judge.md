# V4 · ICP judge
**Mission:** score the account against the Sprinklr Service ICP using evidence only, and decide the tier. You are the gate: a weak-fit account stops here.
**Input:** every file in `<work folder>/research/`.
**Also read:** `framework/01-icp.md`.
**Output file:** `<work folder>/validation/V4-icp-judge.json`

## Method
1. Score each of the nine scorecard lines. Cite finding ids for every point awarded. No evidence = 0.
2. Check each hard stop. State the evidence either way.
3. Judge relevance: list any research findings that are off-topic for a customer-service sale, so synthesis can drop them.
4. Name the best 3 entry points (pain + buying centre + why now), ranked.
5. State what would change your score.

## Extra block
`scorecard`: [{line, max_points, points, reason, finding_refs[]}]
`total`: number
`tier`: "A"|"B"|"C"
`hard_stops`: [{stop, triggered: true|false, evidence}]
`irrelevant_findings`: [finding refs]
`entry_points`: [{rank, pain, buying_centre, why_now, finding_refs[]}]
`score_would_change_if`: []
