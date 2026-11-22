# Q3 · Content QA — the prospect's eyes
**Mission:** you are a senior customer-service leader at the account. A vendor you have never met emailed you this infographic. React honestly.
**Input:** `<work folder>/out/prospect-infographic.pdf` and the outreach emails in `<work folder>/out/outreach-kit.md`. Use the dossier only to check facts.
**Also read:** `framework/02-evidence-standard.md`.
**Output file:** `<work folder>/validation/Q3-prospect-lens.json`

## Check
1. First reaction in one line. Would you reply, ignore, or forward to legal?
2. Anything you could prove wrong with what an insider knows. Search the web to re-check the three boldest statements.
3. Anything that feels unfair, presumptuous or insulting. Anything that ignores a known strength.
4. Anything that reveals research on named people, or guesses about vendors.
5. Is the value band believable? Is "illustrative" clear enough?
6. Does it earn 30 minutes? What one change would most raise the reply chance?

## Extra block
`first_reaction`: string
`would`: "reply" | "ignore" | "escalate"
`issues`: [{where, problem, severity: "block"|"fix"|"note", fix}]
`recheck`: [{statement, still_true: true|false|"unsure", source_url}]
`one_change`: string
`verdict`: "pass" | "fix"
