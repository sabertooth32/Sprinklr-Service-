# R7 · AI footprint in customer service
**Mission:** how much AI does this brand use in each support channel today, and how good is it? Be precise and fair. Advanced AI users are still prospects, but the pitch changes.
**Also read:** `framework/03-maturity-models.md` (AI maturity dimensions and levels).
**Output file:** `<work folder>/research/R7-ai-footprint.json`

## Find
| Area | Look for |
|---|---|
| Customer-facing AI | Chatbots, voice bots, virtual assistants: name, launch date, channels, languages, what it can complete, disclosed containment or usage numbers |
| Employee-facing AI | Agent assist, copilots, call summarisation, knowledge search for service staff: name, scale, disclosed impact |
| Routing and prediction | Intent-based routing, predictive service, proactive alerts |
| Insight and quality | Speech / text analytics, automated QA, complaint analytics |
| Governance | Responsible-AI frameworks, regulator guidance they follow, model risk statements |
| Build vs buy | In-house platforms, named LLM or cloud partners |
| Stated plans | AI targets, value numbers, job impact statements from leadership |
| Customer reaction | What users say about the bot (link to public reviews) |

## Then propose scores
For each live channel, propose a 0–5 score on each of the five AI dimensions. Each score needs: basis (`observed` / `disclosed` / `inferred`), finding ids, and a one-line reason. Use `null` where nothing is visible. When torn, take the lower score.

## Extra block
`ai_assets`: [{name, type: "customer-facing"|"employee-facing"|"routing"|"insight"|"governance", channels[], launched, what_it_does, disclosed_metrics, build_or_buy, partner, finding_ids[]}]
`ai_scores`: [{channel, self_service_ai{score,basis,reason,finding_ids}, agent_assist{...}, smart_routing{...}, insight_quality{...}, trust_control{...}}]
`ai_gaps`: [{channel, gap, evidence, finding_ids[]}]
`pitch_implication`: 3 bullets. If the brand builds AI in-house, say where a platform still adds value (channels, orchestration, governance, quality, speed).
