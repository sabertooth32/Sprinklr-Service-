# 07 · Capability map — customer problem to Sprinklr Service capability

Use the exact capability name. The engine reads the same list from `framework/data/sprinklr-service-facts.json`.

## Problem → capability

| If you see this | Lead with | What it does |
|---|---|---|
| customers bounced between teams; long queue and wait times; separate routing rules per channel | **Omnichannel Routing (Unified Routing)** | Assigns each voice or digital case to the best-fit agent using skills, capacity and past performance. |
| agents toggling between many tools; no single view of the customer; customers repeating themselves | **Unified Agent Desktop** | Shows customer history, CRM data and voice plus digital conversations on one agent screen. |
| ageing on-premise telephony; voice and digital run on separate platforms; rigid IVR menus | **Sprinklr Voice** | Cloud contact-centre voice with IVR, ACD, call controls, dialers and monitoring, without a separate CPaaS provider. |
| high volume of repetitive contacts; low chatbot containment; 24x7 coverage cost | **Sprinklr AI Agents** | Customer-facing AI agents that resolve issues autonomously on chat and voice and hand over to humans with context. |
| call volume peaks; robotic or slow voice bots; IVR abandonment | **Voice AI Agents** | Voice-enabled AI agents that respond fast, handle caller interruptions and filter background noise. |
| AI projects stuck in pilot; dependence on vendor or IT to change bots; no central place to manage AI use cases | **Sprinklr AI+ Studio** | No-code workspace, housing AI Agent Studio, to build, bulk-test, deploy and monitor AI agents and workflows. |
| slow AI agent build cycles; SOPs not reflected in bots; ungoverned agent sprawl | **Agent Architects** | Environment to design, test, deploy and govern enterprise AI agents from plain-language briefs or SOPs. |
| cannot prove AI answers are safe; regulator and risk-team scrutiny of AI; fear of hallucinated answers reaching customers | **Autonomous Evaluation** | Gives test-backed, explainable validation and logs of how AI agents behave before wider rollout. |
| mandated enterprise LLM standard; data-residency and model-control requirements; existing LLM contracts going unused | **Bring Your Own Model (BYOM) / Bring Your Own Key (BYOK) in AI+ Studio** | Lets customers run Sprinklr AI features on their own LLM provider keys or self-hosted models. |
| unmonitored generative AI use; brand and compliance risk from AI replies; no audit trail for AI decisions | **Sprinklr AI+ (governance controls)** | Applies input and output guardrails, approval workflows, access controls, usage logs and monitoring to generative AI. |
| long handle and wrap-up time; inconsistent answers; slow new-agent ramp-up | **Agent Copilot** | GenAI assistant that drafts replies, summarises cases and surfaces cited knowledge for agents in real time. |
| expensive phone-only support; no in-app or web support; customers abandoning online journeys | **Live Chat** | Adds chat to websites, mobile apps and kiosks with a no-code builder and bot-to-agent handoff. |
| customers prefer WhatsApp over calling; separate WhatsApp BSP tool; no bot-to-agent handover on messaging | **Messaging Channels (WhatsApp, SMS, Telegram, Apple business messaging)** | Handles WhatsApp, SMS, Telegram and other messaging conversations in one inbox with cross-channel context. |
| public complaints missed or answered late; social care run by marketing tools; no SLA tracking on social | **Social Media Customer Service** | Manages care across 25+ social channels, classifying messages by intent, urgency and sentiment. |
| outdated or duplicated help content; agents and bots giving different answers; content gaps nobody sees | **Knowledge Base** | Single AI-assisted knowledge source for customer self-service, agents and AI agents, with version control and localisation. |
| repeat how-to questions hitting agents; no peer-to-peer support; low self-service adoption | **Community (Community Forum software)** | Branded, moderated forum where customers answer each other, with gamification and SEO-indexed content. |
| process non-compliance; long training time; inconsistent troubleshooting | **Guided Workflows** | Step-by-step resolution flows for agents and customers, usable in chat, bots, knowledge articles and the agent desktop. |
| QA samples only a few percent of calls; compliance breaches found late; subjective manual scoring | **Quality Management (AI-driven)** | Uses AI to score 100% of interactions across voice and digital channels for quality and compliance. |
| over- or under-staffing; spreadsheet scheduling; missed service levels | **Workforce Management** | Forecasting, capacity planning, scheduling, time-off management and real-time adherence for contact-centre staff. |
| no visibility into why customers contact; insights limited to survey respondents; product issues spotted late | **Conversational Analytics (contact-centre analytics)** | AI analyses all conversations to surface contact drivers, sentiment and emerging issues. |
| low survey response rates; feedback tool separate from service desk; no CSAT on unsurveyed contacts | **Omnichannel Surveys** | Builds CSAT and NPS surveys once and deploys them across channels, with AI-predicted CSAT on conversations. |
| low connect rates; manual dialling; no proactive service notifications | **Outbound Voice** | Runs outbound campaigns with predictive, progressive and preview dialers, outbound IVR and scheduled callbacks. |
| escalations spotted too late; no real-time view of remote teams; CSAT drops unnoticed during a shift | **Supervisor Console** | Live view of cases and agents with AI alerts, letting supervisors listen in, whisper or take over. |
| point-solution sprawl; data silos between service and marketing; many vendors, contracts and SLAs | **Sprinklr Unified-CXM platform** | One AI-native platform and common data foundation shared by service, social, marketing and insights products. |

## Journey stage → usual capabilities

| Stage | Typical break | Capabilities |
|---|---|---|
| 1 Find help | Buried contact options, too many doors | Knowledge Base, Live Chat, Messaging Channels |
| 2 Self-serve | Bot loop, FAQ dead end | Sprinklr AI Agents, Knowledge Base, Guided Workflows, Community |
| 3 Reach a human | Long wait, no escape from bot | Omnichannel Routing, Sprinklr Voice, Voice AI Agents |
| 4 Explain | Repeat details, re-authenticate | Unified Agent Desktop, Sprinklr AI Agents (hand-over with context) |
| 5 Resolve | Transfers, inconsistent answers | Agent Copilot, Guided Workflows, Knowledge Base |
| 6 Follow up | No update, no confirmation | Outbound Voice, Messaging Channels, Omnichannel Surveys |
| 7 Speak up | Slow public reply | Social Media Customer Service, Conversational Analytics |
| Behind the scenes | Sampling QA, no view of contact drivers, AI risk | Quality Management, Conversational Analytics, Workforce Management, Autonomous Evaluation, Sprinklr AI+ |

## Proof points you may cite

| Customer | Industry · region | Result | Source date |
|---|---|---|---|
| Forrester Total Economic Impact study of Sprinklr Service (composite organisation, commissioned by Sprinklr) | Cross-industry composite · Global | 210% ROI over three years; payback in less than six months; legacy system cost reduction $799k; training cost reduction $78k (figures as shown on Sprinklr's 2024 TEI page; the same 210% / under-six-months result was first published on 2021-11-16 for 'Sprinklr Modern Care' with different supporting figures) | 2024-05 |
| Asia-based fintech company (unnamed) | Banking / fintech · APJI | 274K+ cases resolved by chatbot in eight months; 5.35 FTE-equivalent cost savings; live chat CSAT 4.51 out of 5 | undated |
| Vi (Vodafone Idea) | Telecom · APJI | 30% improvement in time saved from automated responses | undated |
| Marico | Consumer goods / retail · APJI | Response rate up 98%; response time / SLA down 82% | undated |
| boAt | Consumer electronics / retail · APJI | 140 employees onboarded; about 10,000 customer touchpoints tracked and analysed; more than 6,000 warranty claims validated in real time | undated |
| Unnamed telecom provider serving South Asia and Africa | Telecom · Global | 21x reduction in response time, from 420 to 20 minutes; 135-minute drop in wait time; 40% better advisor time optimisation | undated |
| Leading telecommunications provider (unnamed; region not stated) | Telecom · Global | 76.18% containment rate; 40,000+ customer interactions handled | undated |
| Leading European airline (unnamed) | Travel / airline · EMEA | AHT from 15 minutes to 10 minutes (33% reduction); $500,000 annual cost avoidance; 80% increase in bot containment | undated |
| Gulf Bank (Kuwait) | Banking · EMEA | From 58 minutes to under 6 minutes | undated |
| Leading Latin American bank (unnamed) | Banking · Americas | First response time halved, from 66.5 minutes to 30 minutes; NPS 81.29 | undated |
| Uber | Travel / mobility · Global | 33% reduction in first response time; 89 seconds reduction in average case handling time | undated |
| GO Telecom | Telecom · EMEA | Average handling time down 63%; first response time improved by 90% (54 minutes); average CSAT up 20% | undated |
| Umniah (Jordan) | Telecom · EMEA | 53% reduction in agent handover; chatbot average handling time from about 53 minutes to about 5 minutes (91% reduction) | undated |
| Middle Eastern e-commerce fashion retailer (unnamed) | Retail / e-commerce · EMEA | 50% decrease in customer service abandonment rate; case resolution time from six days to 1.8 days; about $8,000 saved per month in technology fees | undated |
| Cdiscount | Retail / e-commerce · EMEA | 15% increase in customer satisfaction scores | 2023-08-29 |

## Claims you must not make

| Do not say | Why |
|---|---|
| Any Gartner CCaaS Magic Quadrant position | Sprinklr is NOT among the ten vendors listed in the Gartner abstract (Amazon Web Services, Cisco, Content Guru, Five9, Genesys, Microsoft, NiCE, Talkd |
| Any Gartner CCaaS Magic Quadrant position | Sprinklr not included; CX Today's rundown names Sprinklr among prominent CCaaS providers that do not feature in the matrix. |
| Any number from the `unverified` list in the facts file | Seen once, not confirmed |
| "30% cost reduction" as a promise | Marketing claim with no named customer |

_Facts gathered 2026-11-21 from public sources. Product names change: refresh this file each quarter._
