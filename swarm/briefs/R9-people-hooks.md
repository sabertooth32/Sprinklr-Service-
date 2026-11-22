# R9 · People — personal-level research
**Mission:** for each top contact, find what they have said in public and care about at work, so the SDR's first line is specific and true.
**Input:** read `<work folder>/research/R2-buying-centres.json`. Take the `top_contacts` (up to 8), plus up to 4 more senior names if time allows.
**Output file:** `<work folder>/research/R9-people-hooks.json`

## For each person find
| Item | Notes |
|---|---|
| Current role check | Confirm title and employer again from a source dated in the last 6 months |
| Remit | What they own in plain words |
| Career path | Previous roles and employers. Useful for shared-history hooks |
| Public voice | Interviews, conference talks, podcasts, bylined articles, public LinkedIn posts visible in search. Quote exactly, with date and URL |
| Stated priorities | What they say they are working on |
| Language and tone | How they talk: numbers, customers, people, technology |
| Upcoming appearances | Events in the next 90 days |

## Then write, per person
- `hook`: the single most relevant true fact to open with. Max 20 words.
- `opener`: one first line an SDR could send. Max 25 words. Specific, respectful, no flattery, no fake familiarity.
- `care_about`: 3 bullets.
- `avoid`: anything the SDR should not raise.
- `best_channel`: email / LinkedIn / event / referral, with reason.

## Rules
- Professional, public information only. Nothing about family, health, home, religion, politics.
- If you find nothing public for a person, say so. Do not pad.
- If the role check fails, set `role_check: "failed"` and explain.

## Extra block
`people`: [{name, title, role_check: "confirmed"|"unconfirmed"|"failed", role_check_source, remit, career[], public_statements[{date, where, quote, url}], care_about[], hook, opener, avoid[], best_channel, finding_ids[]}]
