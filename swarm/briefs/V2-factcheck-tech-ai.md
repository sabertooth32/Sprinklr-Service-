# V2 · Fact check — incumbents, AI and customer voice
**Mission:** try to break the findings in R3, R5 and R7. Vendor claims and AI claims are where sales packs most often embarrass the sender.
**Input:** `<work folder>/research/R3-incumbents.json`, `R5-voice-of-customer.json`, `R7-ai-footprint.json`.
**Also read:** `framework/05-validation-gates.md`, `framework/03-maturity-models.md`.
**Output file:** `<work folder>/validation/V2-factcheck-tech-ai.json`

## Method
1. Every vendor in the stack: is there dated proof it is in use now? Has the account since moved to another vendor or in-house? Downgrade `status` where proof is thin.
2. Every AI asset and number: confirm name, launch date, scope and metrics against a second source. Watch for pilots described as full roll-outs.
3. Every rating and complaint theme: confirm the rating and date. Are quotes real and recent? Is the theme fair, or cherry-picked?
4. Review the proposed AI scores. For each channel say `agree` or give your score with a reason. Take the lower score when unsure.
5. Verdict per finding: `confirmed`, `corrected`, `unverified`, `stale`, `refuted`.

## Extra block
`verdicts`: [{finding_ref, verdict, note, corrected_claim, second_source_url}]
`stack_review`: [{layer, vendor, your_status, note}]
`ai_score_review`: [{channel, dimension, proposed, yours, reason}]
`not_checked`: []
