# R5 · Voice of the customer
**Mission:** what do real customers say about getting help from this brand? Find where the experience breaks, with proof.
**Also read:** `framework/03-maturity-models.md` (journey stages).
**Output file:** `<work folder>/research/R5-voice-of-customer.json`

## Find
| Source | What to capture |
|---|---|
| App stores (iOS, Android), per market | Rating, review count, date, service-related themes |
| Review sites (Trustpilot, Google, ProductReview, MouthShut, etc.) | Rating, count, top complaint themes |
| Forums and Reddit | Recurring service complaints. Quote short, no usernames |
| Social replies to the brand's care handles | Typical complaint types, visible reply behaviour |
| News | Outages, service failures, scam handling, long waits, branch closures |
| Regulators and ombudsman | Penalties, directions, complaint statistics |
| Awards and positive proof | Customer-service awards, satisfaction rankings. Be fair |

## Build
- `complaint_themes`: cluster into 5–8 themes. For each: channel, journey stage (1–7), how often it appears, one short quote, severity 1–3, finding ids.
- `strengths`: what customers and independent rankings praise. We need balance. The prospect will not trust a one-sided view.
- Last 12 months matter most. Mark older items `stale`.

## Connector plays
WebSearch (extended mode helps here). LunarCrush topic / posts for social sentiment if it covers the brand.

## Extra block
`ratings`: [{platform, market, app_or_page, rating, review_count, as_of, finding_id}]
`complaint_themes`: [{theme, channel, journey_stage, frequency: "common"|"recurring"|"occasional", example_quote, severity, finding_ids[]}]
`incidents`: [{date, what_happened, customer_impact, regulator_action, finding_ids[]}]
`strengths`: [{strength, proof, finding_id}]
