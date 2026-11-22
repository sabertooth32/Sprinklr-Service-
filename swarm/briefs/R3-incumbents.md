# R3 · Incumbent technology
**Mission:** find which vendors run the customer service stack today. This shapes the entry point and the objections.
**Output file:** `<work folder>/research/R3-incumbents.json`

## Find, layer by layer
| Layer | Examples of what to look for |
|---|---|
| Voice / contact-centre platform | Genesys, NICE, Avaya, Cisco, Amazon Connect, Five9, Talkdesk |
| CRM / case management | Salesforce, Microsoft Dynamics, Pega, ServiceNow, in-house |
| Live chat / messaging | LivePerson, Genesys, Salesforce, Zendesk, in-house |
| Chatbot / conversational AI / voice bot | Kasisto, IBM, Google, Microsoft, in-house LLM builds |
| WhatsApp / messaging provider | |
| Social care / listening | Sprinklr, Khoros, Sprout, Meltwater, Emplifi |
| Knowledge management | |
| Workforce and quality management | NICE, Verint, Calabrio |
| Speech / text analytics, voice of customer | Medallia, Qualtrics, Verint, CallMiner |
| Outsourcers (BPO) running contact centres | |

## Where the evidence lives
Vendor case studies and press releases · conference talks · job adverts naming tools · LinkedIn profiles of staff naming tools · analyst notes · tender notices · tech-stack databases.

## Connector plays
WebSearch ("<company> Genesys", "<company> contact centre platform", "<company> chatbot vendor", job adverts). Lusha / Sprouts / Vibe Prospecting technographics if available without heavy spend.

## Rules
- A vendor named in a job advert or one staff profile is `inferred`, confidence low or medium. A vendor press release or case study is `disclosed`.
- Date everything. A 2019 case study does not prove 2026 usage: mark `stale`.
- Note anything in-house. A strong in-house build changes the pitch.

## Extra block
`stack`: [{layer, vendor, product, status: "confirmed"|"likely"|"possible"|"historic", since, basis, confidence, finding_ids[], so_what}]
`in_house_builds`: [{name, what, finding_ids[]}]
`consolidation_view`: 3 bullets on how fragmented the stack looks and where Sprinklr could land without a rip-and-replace.
