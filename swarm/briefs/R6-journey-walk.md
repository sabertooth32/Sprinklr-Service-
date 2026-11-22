# R6 · Journey walk (public touchpoints)
**Mission:** walk the support journey as an outsider would see it, using public pages only. Record what a customer meets at each stage. Then write the live tests the SDR must run personally.
**Also read:** `framework/03-maturity-models.md` (journey stages and experience dimensions) and `framework/08-live-test-rules.md`.
**Output file:** `<work folder>/research/R6-journey-walk.json`

## Scenario set
Walk these four everyday needs for the home market:
1. "I see a card transaction I do not recognise." (urgent)
2. "I want to change my address / contact details." (routine)
3. "My payment or transfer failed. Where is my money?" (anxious)
4. "I want to make a complaint about service." (emotional)
Adapt the wording to the industry if the account is not a bank. Keep four: urgent, routine, anxious, emotional.

## For each scenario, at each of the 7 journey stages, record
- What the public help content tells the customer to do, and through which channel.
- How many steps or hand-offs it takes on paper.
- Whether self-service can finish the job, or sends the customer to another channel.
- Whether a human is reachable, when, and how.
- Anything that works well. Be fair.

Use the official help centre, contact page, FAQ articles, chatbot description pages, app-store descriptions, and official social care profiles. If direct page reads are blocked, work from search summaries and mark `via: search_summary`.

## You must NOT
Start a chat, submit a form, call, message, or log in. You only read.

## Then write the SDR mystery-shop script
6–8 live tests a human SDR can do in 20 minutes as a genuine member of the public. For each: channel, exact opening question, what to time, what to look for, how to score it (1–5 on the experience dimensions), and what a break point would look like. Follow `framework/08-live-test-rules.md`. The SDR tests as an ordinary member of the public and never mentions Sprinklr. Write every opening question as a general question ("What should I do if...", "How do I..."). Never write a question that claims an account, card, transaction, loss or complaint. Stop every test before any identity check or form.

## Extra block
`journey`: [{scenario, stage, channel, what_happens, steps_or_handoffs, self_service_completes: true|false|"unknown", verdict: "works"|"friction"|"breaks"|"unknown", severity: 0-3, finding_ids[]}]
`break_points`: [{stage, channel, what_breaks, customer_feels, severity, finding_ids[]}]
`bright_spots`: [{stage, channel, what_works, finding_ids[]}]
`mystery_shop_tests`: [{id, channel, opening_question, time_this, look_for, score_dimensions[], break_point_looks_like}]
