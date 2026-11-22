# 02 · Evidence standard — the rules every agent follows

**One line:** if we cannot show where it came from and when, it does not go to a prospect.

## The finding record

Every fact an agent reports is one record:

```json
{
  "id": "CH-03",
  "claim": "One short sentence. One fact.",
  "detail": "Optional. Numbers, context. Max 40 words.",
  "evidence_type": "first_hand | disclosed | third_party | inferred",
  "source_url": "https://...",
  "source_title": "Page or document title",
  "source_date": "YYYY-MM-DD, YYYY-MM, YYYY or undated",
  "quote": "Exact words from the source that support the claim. Max 40 words.",
  "confidence": "high | medium | low"
}
```

## Evidence types

| Type | Meaning | Example | May appear in prospect content? |
|---|---|---|---|
| `first_hand` | We saw it ourselves on a public touchpoint | Help page lists 6 contact options | Yes |
| `disclosed` | The company said it in an official source | Annual report, press release, executive interview | Yes |
| `third_party` | A credible outsider reported it | Regulator notice, major news outlet, app-store rating | Yes, with source |
| `inferred` | Our estimate or deduction | Volume estimate, tool guessed from a job advert | Internal only, shown as estimate |

## Confidence

| Level | Rule |
|---|---|
| High | Primary source, dated, and a second independent source agrees |
| Medium | One good source, dated |
| Low | Single weak source, old, or inferred |

## Freshness windows

| Fact type | Maximum age |
|---|---|
| Person in role, title | 6 months, or re-verified this run |
| Trigger events, incidents | 12 months |
| Channels, opening hours, bot behaviour | 12 months |
| Technology / incumbent vendors | 24 months, flagged if > 12 |
| Strategy, financials | Latest annual report or results |

Older than the window: keep it, mark `stale: true`, keep it out of prospect content.

## Hard rules

1. **Never invent.** No made-up names, numbers, quotes or URLs. "Unknown" is a valid answer.
2. **One claim, one source.** Do not merge two sources into one "fact".
3. **Estimates show their maths.** Volume = inputs × assumptions, each input sourced.
4. **Quote, do not paraphrase,** in the `quote` field.
5. **People data stays professional.** Role, public statements, public career history only. No family, health, home, politics, religion or private social accounts.
6. **No deception.** Agents do not pose as customers, open fake complaints, log in, call, or use anyone's identity. Agents read public pages only. Live channel tests are done by the SDR as a real person asking real questions.
7. **Respect the prospect.** Write what we observed, not insults. Every gap is phrased as an opportunity.
8. **Spend limits.** Search is fine. Reveal contact details only when the brief says so, and report credits used.
9. **Say what you could not find.** Every agent returns a `gaps` list.
