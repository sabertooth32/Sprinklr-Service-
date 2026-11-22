#!/usr/bin/env python3
"""Join research findings with validator verdicts. Code decides what code can decide.

Usage: python3 engine/digest.py accounts/<slug>

Reads   accounts/<slug>/research/*.json and validation/*.json
Writes  accounts/<slug>/digest/evidence.jsonl   one compact record per finding, verdicts merged, prospect_safe computed
        accounts/<slug>/digest/index-<agent>.md one line per finding: the slim view synthesis agents read first
        accounts/<slug>/digest/blocks/*.json    each research and validation file without its bulky findings list
        accounts/<slug>/digest/stats.json       counts for the validation stamp

A finding is prospect_safe only if ALL hold: a fact checker confirmed or corrected it; it is not inferred;
confidence is not low; it has a date and is inside the freshness window; the red team did not block it or
mark it internal-only; the ICP judge did not mark it irrelevant.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import MAX_AGE, months_old  # noqa: E402

CATEGORY = {"R1": "strategy", "R2": "person", "R3": "technology", "R4": "channel", "R5": "customer_voice",
            "R6": "channel", "R7": "ai", "R8": "trigger", "R9": "person"}
ID = re.compile(r"\b([RV]\d-\d+)\b")
TYPES = {"first_hand", "disclosed", "third_party", "inferred"}
SEVERITY = {"note": 1, "fix": 2, "block": 3}


def load(path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"skip {path.name}: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    work = Path(sys.argv[1])
    research = {p.stem: load(p) for p in sorted((work / "research").glob("*.json"))}
    validation = {p.stem: load(p) for p in sorted((work / "validation").glob("*.json"))}
    research = {k: v for k, v in research.items() if v}
    validation = {k: v for k, v in validation.items() if v}
    run = date.fromisoformat(next(iter(research.values()))["run_date"])

    verdicts, red, internal, safe_hint, irrelevant = {}, {}, {}, {}, set()
    people_checked = people_removed = 0
    icp = {}
    for name, v in validation.items():
        for row in v.get("verdicts", []):
            for i in ID.findall(str(row.get("finding_ref", ""))):
                verdicts[i] = row
        for row in v.get("issues", []):
            for i in ID.findall(str(row.get("finding_ref_or_field", ""))):
                if SEVERITY.get(row.get("severity"), 0) >= SEVERITY.get(red.get(i, {}).get("severity"), 0):
                    red[i] = {"severity": row.get("severity"), "why": row.get("why", ""), "fix": row.get("fix", "")}
        for row in v.get("internal_only", []):
            for i in ID.findall(str(row.get("finding_ref", ""))):
                internal[i] = row.get("why", "")
        for row in v.get("safe_for_prospect", []):
            for i in ID.findall(str(row.get("finding_ref", ""))):
                safe_hint[i] = row.get("why", "")
        irrelevant.update(i for x in v.get("irrelevant_findings", []) for i in ID.findall(str(x)))
        if "remove_from_outreach" in v:
            people_checked = len(v.get("people", []))
            people_removed = len(v.get("remove_from_outreach", []))
        if "scorecard" in v and "tier" in v:
            icp = {"total": v.get("total"), "tier": v.get("tier")}

    records, dropped = [], []
    counts = {"confirmed": 0, "corrected": 0, "unverified": 0, "stale": 0, "refuted": 0, "not_checked": 0}
    sources = {**research, **validation}
    for name, doc in sources.items():
        is_research = name in research
        for f in doc.get("findings", []):
            fid = f.get("id")
            if not fid:
                continue
            row = verdicts.get(fid)
            verdict = (row or {}).get("verdict", "unverified")
            if is_research:
                counts[verdict if row else "not_checked"] = counts.get(verdict if row else "not_checked", 0) + 1
            if verdict == "refuted":
                dropped.append({"id": fid, "claim": f.get("claim"), "why": row.get("note", "")})
                continue
            etype = f.get("evidence_type") if f.get("evidence_type") in TYPES else "third_party"
            conf = f.get("confidence") if f.get("confidence") in ("high", "medium", "low") else "low"
            cat = CATEGORY.get(fid.split("-")[0], "other")
            if etype == "inferred" and cat == "channel":
                cat = "volume"
            sdate = str(f.get("source_date") or "undated")
            if not re.match(r"^\d{4}(-\d{2}){0,2}$", sdate):
                m = re.search(r"\d{4}(-\d{2}){0,2}", sdate)
                sdate = m.group(0) if m else "undated"
            age = months_old(sdate, run)
            stale = bool(f.get("stale")) or verdict == "stale" or (age is not None and age > MAX_AGE.get(cat, 24))
            if stale and verdict in ("confirmed", "corrected"):
                verdict = "stale"
            claim = (row or {}).get("corrected_claim") if verdict == "corrected" and (row or {}).get("corrected_claim") else f.get("claim", "")
            rt = red.get(fid)
            ok = (verdict in ("confirmed", "corrected") and etype != "inferred" and conf != "low" and sdate != "undated"
                  and not stale and fid not in internal and not (rt and rt["severity"] == "block") and fid not in irrelevant
                  and str(f.get("source_url", "")).startswith("http"))
            rec = {
                "id": fid, "claim": claim, "evidence_type": etype, "source_url": f.get("source_url", ""),
                "source_title": f.get("source_title", ""), "source_date": sdate, "quote": str(f.get("quote", ""))[:200],
                "confidence": conf, "verdict": verdict, "via": f.get("via", ""), "stale": stale, "category": cat,
                "prospect_safe": ok,
            }
            if etype == "inferred":
                rec["method"] = f.get("method") or str(f.get("detail", ""))[:200] or "Estimate. See the research file."
            notes = {}
            if row and row.get("note"):
                notes["fact_check"] = row["note"]
            if rt:
                notes["red_team"] = f"{rt['severity']}: {rt['fix'] or rt['why']}"
            if fid in internal:
                notes["internal_only"] = internal[fid]
            if fid in safe_hint:
                notes["safe_for_prospect"] = safe_hint[fid]
            if fid in irrelevant:
                notes["irrelevant"] = True
            if notes:
                rec["notes"] = notes
            records.append(rec)

    out = work / "digest"
    (out / "blocks").mkdir(parents=True, exist_ok=True)
    with (out / "evidence.jsonl").open("w") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    # A slim, greppable index per agent prefix: what synthesis agents read first.
    by_prefix = {}
    for r in records:
        by_prefix.setdefault(r["id"].split("-")[0], []).append(r)
    for prefix, rows in by_prefix.items():
        lines = [f"# Evidence index {prefix} — id | verdict | prospect | type | confidence | date | claim | notes",
                 "Full records are in evidence.jsonl. Reference ids only; merge_parts.py copies the records.", ""]
        for r in rows:
            n = r.get("notes", {})
            note = " ; ".join(f"{k}: {str(v)[:110]}" for k, v in n.items() if k != "safe_for_prospect")
            lines.append(f"{r['id']} | {r['verdict']} | {'SAFE' if r['prospect_safe'] else 'internal'} | {r['evidence_type']} | "
                         f"{r['confidence']} | {r['source_date']} | {r['claim']}" + (f" | {note}" if note else ""))
        (out / f"index-{prefix}.md").write_text("\n".join(lines) + "\n")
    for name, doc in sources.items():
        slim = {k: v for k, v in doc.items() if k not in ("findings", "verdicts", "not_checked")}
        (out / "blocks" / f"{name}.json").write_text(json.dumps(slim, ensure_ascii=False, indent=1))
    checked = counts["confirmed"] + counts["corrected"] + counts["unverified"] + counts["stale"] + counts["refuted"]
    stats = {
        "facts_total": sum(len(d.get("findings", [])) for d in research.values()),
        "facts_checked": checked, "confirmed": counts["confirmed"], "corrected": counts["corrected"],
        "dropped": counts["refuted"], "unverified_or_stale": counts["unverified"] + counts["stale"], "not_checked": counts["not_checked"],
        "people_checked": people_checked, "people_removed": people_removed,
        "prospect_safe": sum(1 for r in records if r["prospect_safe"]),
        "red_team": {s: sum(1 for v in red.values() if v["severity"] == s) for s in SEVERITY},
        "via": {k: sum(1 for r in records if r["via"] == k) for k in sorted({r["via"] for r in records})},
        "icp": icp, "refuted": dropped,
    }
    (out / "stats.json").write_text(json.dumps(stats, indent=1))
    print(f"digest: {len(records)} evidence records, {stats['prospect_safe']} prospect-safe, "
          f"{checked} fact-checked ({counts['confirmed']} confirmed, {counts['corrected']} corrected, {counts['refuted']} dropped), "
          f"{counts['not_checked']} not checked -> {out}")


if __name__ == "__main__":
    main()
