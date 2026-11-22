# V3 · People check
**Mission:** make sure no SDR emails someone who has left, moved or never held the role. One wrong name destroys credibility.
**Input:** `<work folder>/research/R2-buying-centres.json` and `R9-people-hooks.json`.
**Output file:** `<work folder>/validation/V3-people-check.json`

## Method
For every person in `top_contacts` and every person R9 profiled, then as many of the rest as you can:
1. Search independently: "<name> <company>", "<name> LinkedIn", "<name> appointed", "<name> joins", "<name> leaves".
2. Find the most recent dated evidence of their role. Look hard for signs they moved, retired or changed remit.
3. Check each quote attributed to them in R9: right person, right date, right words?
4. Check the opener lines: true, respectful, not creepy, no private data?

Connector play: Lusha `contacts_search` by name + company can confirm current employer and title cheaply (search only, no reveal).

## Verdicts
`current` (dated proof within 6 months) · `likely_current` (proof 6–18 months old, no sign of change) · `moved` · `unknown`.

## Extra block
`people`: [{name, verdict, current_title, evidence_date, evidence_url, note, quotes_ok: true|false, opener_ok: true|false, fix}]
`remove_from_outreach`: [names]
`not_checked`: []
