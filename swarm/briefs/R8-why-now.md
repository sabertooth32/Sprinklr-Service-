# R8 · Why now — triggers and timing
**Mission:** find the events from the last 12 months that give an SDR a reason to reach out this quarter.
**Output file:** `<work folder>/research/R8-why-now.json`

## Find
| Trigger type | Examples |
|---|---|
| Leadership change | New CEO, COO, CIO, head of consumer, head of service or CX, in the last 12 months |
| Service incidents | Outages, disruptions, public apologies |
| Regulator pressure | Penalties, capital add-ons, directions, new rules on service, scams, AI, outsourcing |
| Cost and productivity programmes | Announced savings targets, headcount changes, AI-driven role changes |
| Strategy shifts | New markets, mergers, new digital bank, product launches that add service volume |
| Technology moves | New vendor deals, cloud migration, contact-centre or CRM changes, RFPs, tenders |
| Hiring signals | Open roles for contact-centre technology, conversational AI, CX, service transformation. Quote tools named |
| Events | Conferences where their leaders speak in the next 90 days. Results dates |

## Connector plays
WebSearch (extended for recent news). Lusha `signals_companies_search` if cheap. Job adverts via search.

## Rules
- Date every trigger. Older than 12 months = `stale`, keep only if still shaping decisions.
- For each trigger say why it matters for customer service in one line.
- Rank by urgency: now (0–90 days), soon (3–6 months), background.

## Extra block
`triggers`: [{date, type, what, why_it_matters_for_service, urgency, finding_ids[]}]
`upcoming_dates`: [{date, event, use}]
`hiring_signals`: [{role, location, posted, tools_named[], finding_id}]
`why_now_headline`: one sentence, max 20 words, an SDR can say aloud.
