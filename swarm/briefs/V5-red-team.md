# V5 · Red team
**Mission:** read all research as two hostile readers and find what would embarrass Sprinklr.
- Reader A: the account's Head of Customer Service. Proud of the team. Knows the real numbers.
- Reader B: the account's legal and communications lead.
**Input:** every file in `<work folder>/research/`.
**Also read:** `framework/02-evidence-standard.md`, `framework/05-validation-gates.md`.
**Output file:** `<work folder>/validation/V5-red-team.json`

## Hunt for
| Risk | Example |
|---|---|
| Overclaim | An estimate written as a fact |
| Provably wrong | A channel said to be missing that exists |
| Unfair | One angry review used to describe a whole channel |
| Stale | A 2023 incident presented as today's state |
| Disrespect | Wording the reader would find insulting |
| Ignored strengths | The brand is a recognised leader in something we call a gap |
| Privacy | Anything personal about a named person |
| Confidentiality | Anything that looks leaked or non-public |
| Competitive misstep | Attacking an incumbent the reader chose |

## Output
For each issue: where it is, why it is a risk, and the fix (rewrite, downgrade to internal-only, or delete).
Then list the 5 claims you consider safest and strongest for prospect-facing content, and the 5 that must never leave the building.

## Extra block
`issues`: [{finding_ref_or_field, risk_type, why, fix, severity: "block"|"fix"|"note"}]
`safe_for_prospect`: [{finding_ref, why}]
`internal_only`: [{finding_ref, why}]
`tone_guidance`: 3 bullets for how to talk to this specific account.
