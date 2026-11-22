# Q2 · Content QA — plain English and SDR usability
**Mission:** you are a junior SDR in your first month, English is your second language. Can you act on this brief today?
**Input:** `<work folder>/out/sdr-brief.pdf`, `<work folder>/out/outreach-kit.md`, `<work folder>/out/prospect-infographic.pdf`.
**Output file:** `<work folder>/validation/Q2-plain-english.json`

## Check
1. Any sentence over 20 words. Any jargon, idiom or acronym not explained. Give the rewrite.
2. Each page: what is the one thing I should take away? If you cannot tell in 5 seconds, flag it.
3. The step-by-step play: could you follow it with no help? What is missing or unclear?
4. Outreach copy: would a busy executive read past the first line? Is the ask small and clear? Any hype words? Any claim you could not back if challenged?
5. Each opener: specific and true, or generic?

## Extra block
`rewrites`: [{where, original, rewrite, why}]
`unclear_steps`: [{step, problem, fix}]
`page_takeaways`: [{page, takeaway, clear: true|false}]
`verdict`: "pass" | "fix"
