# Q1 · Content QA — completeness and traceability
**Mission:** check the built pack has everything an SDR needs and nothing that is not in the dossier.
**Input:** `<work folder>/out/sdr-brief.pdf`, `<work folder>/out/prospect-infographic.pdf`, `<work folder>/out/outreach-kit.md`, `<work folder>/dossier.json`, `<work folder>/validation_report.json`.
**Also read:** `framework/05-validation-gates.md` (completeness checklist).
**Output file:** `<work folder>/validation/Q1-completeness.json`

## Check
1. Every item on the completeness checklist is present in the SDR brief. Name the page.
2. The prospect infographic has every "must have" and none of the "must not have".
3. Pick 15 facts from the PDFs at random. Trace each to an evidence id in the dossier. Flag any you cannot trace.
4. Numbers agree everywhere: ICP score, indexes, volumes, value range.
5. Layout: read every page. Flag cut-off text, overlaps, empty areas, unreadable tables.

## Extra block
`checklist`: [{item, present: true|false, page, note}]
`trace`: [{fact, page, evidence_id, ok}]
`layout_issues`: [{file, page, issue}]
`verdict`: "pass" | "fix" and `fixes`: [{where, what}]
