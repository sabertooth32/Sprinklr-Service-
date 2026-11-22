# R2 · Buying centres and people
**Mission:** map who owns customer service decisions, by department, with real named people.
**Also read:** `framework/01-icp.md` (buying centres and deal roles).
**Output file:** `<work folder>/research/R2-buying-centres.json`

## Find
1. The org shape: which group / business unit runs customer service, contact centres, digital channels, conversational AI, CX, social care, and contact-centre technology. Home market first, then other APJI markets.
2. For each buying centre in the ICP table: 2–4 named people. Aim for 15–25 people in total across seniority (C-level, head-of, director, senior manager).
3. For each person: full name, exact current title, location, LinkedIn URL if found, deal role (economic buyer, champion, technical evaluator, user leader, blocker, influencer), one line on why they matter, and how you know they are in the role (finding id).

## Connector plays
- Lusha `decision_makers_buying_group_search` with the company domain.
- Lusha `prospecting_contact_filters` then `prospecting_contact_search` with department / seniority / title keywords: customer service, contact centre, customer experience, digital, conversational AI, operations, transformation, technology, social media.
- WebSearch: leadership pages, press releases, conference speaker lists, interviews, "<title> <company> LinkedIn".
- Do NOT reveal emails or phones. Keep each Lusha contact id in `lusha_id` so a later step can reveal.

## Rules
- Only people with evidence of the current role. Mark `role_confidence` high / medium / low.
- No personal data beyond professional role.

## Extra block
`org_notes`: [short bullets on how service is organised]
`buying_centres`: [{centre, why_it_matters, people: [{name, title, location, linkedin_url, lusha_id, deal_role, why_they_matter, role_confidence, finding_id}]}]
`top_contacts`: [names of the 8 best first contacts, in priority order, with one line each on why]
