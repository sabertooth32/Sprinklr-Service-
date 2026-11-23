# Rollout guide — for the sales leader

How to take Account Radar from one pilot to a tool your SDRs use every week.

## Where you are

```
 ✅ Built        ✅ Piloted         ⬜ Hardened          ⬜ Team pilot        ⬜ Rolled out
 Tool + docs     DBS Bank pack      Settings + review    2–3 SDRs, 2 weeks    All APJI SDRs
```

## How an SDR uses it

| Step | The SDR does | Time |
|---|---|---|
| 1 | Opens Claude Code on the web and picks this repository | 1 min |
| 2 | Types `/account-radar <company>` | 1 min |
| 3 | Keeps working. Claude says when the pack is ready | 2–3 hours, in the background |
| 4 | Reads the SDR brief. Pages 1 to 6 first | 15 min |
| 5 | Runs the customer's-eye tests as "Alex" | 20 min |
| 6 | Tells Claude what they saw: "here are my live-test notes for <company>" | 5 min |
| 7 | Does the five pre-send checks, then sends message 1 with the infographic | 10 min |
| 8 | Follows the 10-day play. Hands a booked meeting to the AE with the brief | Ongoing |

`START-HERE.md` is the SDR's 3-minute guide. Give them that page first.

### What an SDR can ask in plain words

| Need | Type this |
|---|---|
| Understand a page | `explain page 10 of the DBS brief in simple words` |
| Change a message | `rewrite email 1 for a Head of Digital, shorter` |
| Add what they saw | `here are my live-test notes for DBS Bank: ...` |
| Refresh an old pack | `refresh the pack for DBS Bank` |
| Get contact details | `reveal emails for my priority-1 contacts at DBS Bank` |
| Save drafts | `save sequence 1 as Gmail drafts` (drafts only, never sent) |

## What each SDR needs

| Need | Who sets it up | Note |
|---|---|---|
| A Claude seat with Claude Code on the web | Your Claude admin | Confirm seats and usage limits |
| Access to this GitHub repository | You | Add each SDR as a collaborator. The Claude GitHub App is already installed |
| Their own connectors: Lusha first, then Gmail | Each SDR, in claude.ai settings | Credits are spent from the SDR's own Lusha licence |
| A cloud environment with web access | You, once | See "Do these next", item 2 |
| The live-test rules | You, in a 30-minute kick-off | `framework/08-live-test-rules.md` |

## Do these next, in order

| # | Action | Why | Owner |
|---|---|---|---|
| 1 | **Make this repository private** | It is public today. Private lets you keep the logo, fonts and account packs in it, and share it with SDRs safely | You, in GitHub → Settings |
| 2 | **Open web access for the cloud environment** | The DBS pilot could not open any DBS page. With access, agents read pages first-hand and the audit gets much deeper | You: environment menu → Edit → Network access |
| 3 | **Check Sprinklr's CRM for DBS** | Public traces hint Sprinklr may already serve DBS marketing | You or the account owner |
| 4 | **Run the DBS live tests yourself** | It shows you what an SDR will do, and makes the DBS view first-hand | You, 20 minutes, as "Alex" |
| 5 | **Add the Proxima Nova font files** | PDFs are built in the cloud, where the brand font is not installed. They use Inter until you add the files | Brand team → `engine/theme/brand/fonts/` |
| 6 | **Have product marketing review the Sprinklr facts** | Capability names and proof points were gathered from public pages | PMM → `framework/data/sprinklr-service-facts.json` |
| 7 | **Have value engineering review the business-case rates** | They are planning assumptions with US and UK benchmarks | Value team → `engine/value_defaults.json` |
| 8 | **Run a second pilot in another industry** | DBS is a bank that builds its own AI. A telco or retailer will test the tool differently | You: `/account-radar <telco>` |
| 9 | **Team pilot: 2–3 SDRs, 5 accounts each, 2 weeks** | Real replies tell you what to change | You and the SDRs |
| 10 | **Review and roll out** | Decide with the numbers below | You |

## Measure the pilot

| Measure | Compare with | Good sign |
|---|---|---|
| Reply rate on message 1 | The SDR's usual cold outreach | Higher |
| Meetings booked per 10 accounts | Same | Higher |
| SDR prep time per account | Before: hours of manual research | About 1 hour of the SDR's own time |
| Facts an SDR had to correct | The "Still to check" page | Falling run by run |
| Complaints from any brand | Zero is the only acceptable number | Zero |

## Rules that protect Sprinklr

| Rule | Where it is enforced |
|---|---|
| Agents never contact a brand | Agent briefs |
| Live tests are run by a person, as an ordinary customer, never as Sprinklr | The brief, the test script, the code gate |
| No false claims, identity checks, forms or call recording in a test | `framework/08-live-test-rules.md` |
| Nothing is sent for the SDR. Drafts only | The command's guardrails |
| Prospect content carries only fact-checked, dated, non-inferred facts | Code: `digest.py`, `validate.py` |
| A weak-fit account gets no content | The ICP gate |
| Follow local marketing and privacy rules in each country | The SDR, with your legal team's guidance |

## Know what a run costs

| Item | What to expect |
|---|---|
| Time | 2–3 hours per account, unattended |
| Agents | 22 per account. This is heavy work. Use it for top-tier logos, not for every lead |
| Web search | A shared allowance. If agents report "not searched", Claude runs a second pass |
| Lusha | About 40 credits per account for searches. Email reveals are extra and only on request |

## When something needs changing

| You want to | Say to Claude |
|---|---|
| Change who we target or how fit is scored | `update the ICP scorecard: ...` |
| Add an industry-specific question to the research | `add to the journey-walk brief: ...` |
| Change the look | `update the theme: ...` |
| Add a new page to the brief | `add a page to the SDR brief that shows ...` |
| See what changed | `summarise the last 5 changes to this repo` |
