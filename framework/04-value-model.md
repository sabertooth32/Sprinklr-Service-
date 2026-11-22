# 04 · Value model — the business case in the SDR brief

**Purpose:** turn channels + volume + gaps into a credible "value at stake" range.
**Tone:** illustrative, conservative, every input visible. It opens a conversation. It is not a quote.

## Flow

```
Channels + volume  →  Cost to serve today  →  5 value levers  →  3 scenarios  →  KPIs that move
   (estimated)         (volume × unit cost)     (applied in order)   (low / base / high)
```

## Inputs

| Input | Where it comes from | If unknown |
|---|---|---|
| Annual contacts per channel | Channel agent estimate, with method | Mark "estimate", show range |
| Cost per contact per channel | Benchmarks in `engine/value_defaults.json` | Use default, label as benchmark |
| Share of contacts that repeat | Benchmark | Use default |
| Service agents (FTE) | Disclosed, or volume ÷ productivity | Derive, label as estimate |
| Loaded cost per agent | Benchmark by country | Use default |

## The five levers (applied in this order, on what is left — no double counting)

| # | Lever | Formula | Sprinklr capability |
|---|---|---|---|
| 1 | **AI resolution** | Assisted contacts × uplift % × (assisted cost − AI cost) | AI Agents, knowledge |
| 2 | **Fewer repeat contacts** | Remaining assisted contacts × repeat share × reduction % × cost | Unified desktop, customer history, routing |
| 3 | **Voice to messaging shift** | Remaining voice contacts × shift % × (voice cost − messaging cost) | Messaging channels, call deflection |
| 4 | **Faster handling** | Remaining assisted cost × handle-time reduction % × realisation % | Agent copilot, auto summary, guided workflows |
| 5 | **Automated quality** | QA analysts × automation % × loaded cost | AI quality management |

Not counted in the number (named as upside): tool consolidation, retention, cross-sell, regulator risk.

## Scenarios

| Scenario | Use | Rates |
|---|---|---|
| Low | Default in all prospect content | Bottom of each range |
| Base | Internal planning | Mid-point |
| High | Only with discovery data | Top of range |

Rates live in `engine/value_defaults.json`. Each rate carries a source or the label "planning assumption".

## Outputs

| Output | Shown to |
|---|---|
| Estimated cost to serve today | SDR only |
| Value at stake per year: low – base – high | SDR. Prospect sees the low–base band, rounded |
| Value by lever | SDR |
| KPI table: today → target | Both |
| Assumption list | Both |

## KPIs the case speaks to

| KPI | Direction | Lever |
|---|---|---|
| AI resolution rate | Up | 1 |
| First contact resolution | Up | 2 |
| Cost per contact | Down | 1, 3, 4 |
| Average handle time | Down | 4 |
| Quality coverage (% of contacts scored) | Up to 100% | 5 |
| Social / messaging first response time | Down | 3 |
| CSAT / NPS | Up | All |

## Rules

1. Round hard. Two significant figures. Never show false precision.
2. Always show the low scenario first.
3. Every number has a label: **disclosed**, **benchmark** or **estimate**.
4. Say "illustrative, to validate with your data" on every page that shows value.
5. If total volume confidence is low, show a range and no single number.
