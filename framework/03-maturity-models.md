# 03 · Maturity models — Experience and AI

Two scores per channel. Both are **outside-in**: built from public evidence, labelled as a first view, confirmed in discovery.

## A. Experience maturity (per channel)

Score five dimensions from 1 to 5. Channel score = average × 20 (0–100).

| Dimension | Question | 1 | 3 | 5 |
|---|---|---|---|---|
| **Access** | Can I find and reach this channel when I need it? | Hidden, limited hours, login wall | Easy to find, business hours | Obvious, 24/7, in my language |
| **Speed** | How fast is the first useful reply? | Hours or days, long holds | Minutes, stated SLA | Near instant, wait time shown |
| **Resolution** | Is it solved here, first time? | Told to go elsewhere | Common requests solved | End-to-end, including transactions |
| **Continuity** | Does context follow me across channels? | Repeat everything | Some history kept | Seamless hand-off, no repeat |
| **Personal** | Does it know me and sound human? | Generic scripts | Uses my name and product | Proactive, tailored, empathetic |

### Levels

| Level | Index | Name | What it feels like |
|---|---|---|---|
| 1 | 0–39 | Fragmented | Channels exist but do not help |
| 2 | 40–54 | Functional | Works for simple needs, breaks on complex ones |
| 3 | 55–69 | Connected | Good in-channel, weak across channels |
| 4 | 70–84 | Orchestrated | Context carries, most issues solved first time |
| 5 | 85–100 | Predictive | Anticipates needs, resolves before contact |

**Overall Experience Index** = average of channel scores, weighted by estimated volume share.

## B. AI maturity (per channel)

Score five dimensions from 0 to 5. Channel score = average × 20 (0–100).

| Dimension | Question | 0–1 | 2–3 | 4–5 |
|---|---|---|---|---|
| **Self-service AI** | Can AI resolve the request? | None, or menu / FAQ bot | Understands intent, answers from knowledge | Completes tasks end-to-end, agentic |
| **Agent assist** | Does AI help the human agent? | None | Suggested replies, summaries | Real-time guidance, auto wrap-up |
| **Smart routing** | Does AI send me to the right place? | Static menu / IVR tree | Intent-based routing | Predictive, skill and sentiment based |
| **Insight and quality** | Does AI learn from every contact? | Manual sampling | Speech / text analytics on some channels | 100% scored, drivers fed back |
| **Trust and control** | Is AI safe, disclosed, easy to escape? | No disclosure, dead ends | Clear hand-off to a human | Guardrails, audit, tested before release |

### Levels

| Level | Index | Name |
|---|---|---|
| 0 | 0–14 | No AI |
| 1 | 15–34 | Rule-based |
| 2 | 35–54 | Assisted |
| 3 | 55–69 | Generative |
| 4 | 70–84 | Agentic |
| 5 | 85–100 | Autonomous and governed |

## C. How each score is marked

| Basis | Meaning | Shown as |
|---|---|---|
| Observed | We saw it on a public touchpoint | Solid |
| Disclosed | The company stated it | Solid |
| Inferred | Deduced from indirect evidence | Hatched, "estimate" |
| Not visible | Cannot be judged from outside | Blank, "confirm in discovery" |

Rules:

1. Every score needs at least one finding ID as evidence.
2. No evidence → `null`, not a guess. Agent-assist and routing are often `null` from outside.
3. A channel with fewer than 3 scored dimensions shows "partial view".
4. Never round up. When torn between two scores, take the lower one and say why.

## D. Journey stages (for the break-point map)

| Stage | Customer goal | Typical break points |
|---|---|---|
| 1 Find help | Know where to go | Buried contact options, too many doors |
| 2 Self-serve | Solve it alone | FAQ dead end, bot loop, login wall |
| 3 Reach a human | Get to a person | No escape from bot, long wait, limited hours |
| 4 Explain | Tell my story once | Re-authenticate, repeat details |
| 5 Resolve | Get it fixed | Transfer, "call us instead", no ownership |
| 6 Follow up | Know it is done | No confirmation, no proactive update |
| 7 Speak up | Complain or praise in public | Slow or scripted social reply |

Each break point records: stage, channel, what breaks, evidence ID, severity (1–3), and the Sprinklr capability that fixes it.
