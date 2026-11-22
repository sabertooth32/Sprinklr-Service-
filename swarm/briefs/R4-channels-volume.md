# R4 · Support channels and volume
**Mission:** list every support channel the brand runs today and size the contact volume.
**Output file:** `<work folder>/research/R4-channels-volume.json`

## Part A — channel inventory
For the home market first, then each other major APJI market. Check each of these:
phone hotline(s) · IVR / voice bot · website help centre / FAQ · web chatbot · web live chat · in-app chat / in-app help · email / secure message / web form · WhatsApp · other messaging (WeChat, LINE, Telegram, SMS) · Facebook · X · Instagram · LinkedIn · community forum · branches / service centres · video banking · call-back booking.

For each live channel record: market, entry point URL or handle, hours, languages, login needed or not, who it serves (retail / wealth / business), stated response time, and the finding id.

## Part B — volume
1. Look for disclosed numbers: calls or contacts handled a year, chatbot conversations, digital users, customers, agents, contact-centre sites.
2. Then build an estimate per channel. Show the maths: `customers × contacts per customer per year × channel share`. Name each assumption. Give low / base / high.
3. Use proxies where helpful: help-site traffic (Semrush `traffic_overview` on the support domain), social mention volume (LunarCrush topic), app review counts.
4. Estimate service agents (FTE) if not disclosed: assisted contacts ÷ contacts per agent per year. State the productivity assumption.

## Rules
- Disclosed numbers are `disclosed`. Your estimates are `inferred` and must carry `method` and `inputs`.
- Do not give a single number when confidence is low. Give a range.

## Extra block
`channels`: [{channel, market, entry_point, hours, languages[], login_required, serves, stated_response_time, live: true|false, finding_ids[]}]
`disclosed_volumes`: [{metric, value, year, finding_id}]
`volume_estimates`: [{channel, annual_low, annual_base, annual_high, method, inputs[{name, value, basis, finding_id}], confidence}]
`agents_fte`: {low, base, high, method, basis}
`total_annual_contacts`: {low, base, high}
