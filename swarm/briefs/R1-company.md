# R1 · Company and strategy
**Mission:** the facts that decide ICP fit and frame every message.
**Also read:** `framework/01-icp.md`.
**Output file:** `<work folder>/research/R1-company.json`

## Find
| Item | Notes |
|---|---|
| Legal name, HQ, listing / ticker, fiscal year end | |
| Industry and business lines | Which lines generate service contacts |
| Revenue, profit, employees | Latest full year, with currency |
| Customer base | Number of retail / business customers, by market if disclosed |
| APJI markets and service languages | |
| Top 5 stated strategic priorities | Exact wording from annual report, results call, CEO letter |
| What leadership says about customer service, CX, cost, AI | Quotes with speaker and date |
| Cost or productivity programmes | Targets, timelines |
| Existing relationship with Sprinklr | Any public mention as a Sprinklr customer, in any product |

## Connector plays
WebSearch first. Lusha `companies_search` for firmographics. Alpha Vantage `COMPANY_OVERVIEW` / `EARNINGS_CALL_TRANSCRIPT` if the ticker is covered.

## Extra block
`profile`: {legal_name, hq, ticker, fiscal_year_end, industry, business_lines[], revenue{value,currency,year,finding_id}, employees{value,finding_id}, customers{value,scope,finding_id}, markets[], service_languages[], strategic_priorities[{priority, quote, finding_id}], leadership_quotes[{speaker, title, quote, date, finding_id}], sprinklr_relationship{status: "known customer"|"none found"|"unclear", finding_id}}
