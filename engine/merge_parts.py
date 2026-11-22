#!/usr/bin/env python3
"""Assemble dossier.json from the synthesis parts and the evidence digest.

Usage: python3 engine/merge_parts.py accounts/<slug>

Reads   accounts/<slug>/parts/*.json    each part is an object holding some top-level dossier sections
        accounts/<slug>/digest/evidence.jsonl and stats.json
Writes  accounts/<slug>/dossier.json

Agents only reference evidence ids. This script copies the matching records from the digest, so verdicts and
prospect_safe flags cannot be changed by hand. A part may add:
  "extra_evidence":    new records of type "inferred" with a "method" (for example a channel volume estimate)
  "not_prospect_safe": ids to hold back from prospect content (agents may restrict, never widen)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate import walk_evidence_refs  # noqa: E402

KEEP = ("id", "claim", "evidence_type", "source_url", "source_title", "source_date", "quote", "method",
        "confidence", "verdict", "via", "stale", "prospect_safe", "category")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    work = Path(sys.argv[1])
    digest = {}
    for line in (work / "digest" / "evidence.jsonl").read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            digest[r["id"]] = r
    stats = json.loads((work / "digest" / "stats.json").read_text())

    dossier, extra, hold = {}, {}, set()
    for p in sorted((work / "parts").glob("*.json")):
        part = json.loads(p.read_text())
        for r in part.pop("extra_evidence", []):
            if r.get("evidence_type") != "inferred" or not r.get("method"):
                sys.exit(f"{p.name}: extra_evidence {r.get('id')} must be type 'inferred' with a 'method'. Facts come from the digest only.")
            extra[r["id"]] = {**r, "verdict": r.get("verdict", "unverified"), "confidence": r.get("confidence", "low"),
                              "prospect_safe": False, "source_date": r.get("source_date", stats.get("run_date", "undated"))}
        hold.update(part.pop("not_prospect_safe", []))
        for key, value in part.items():
            if key in dossier and isinstance(value, dict) and isinstance(dossier[key], dict):
                dossier[key] = {**dossier[key], **value}
            else:
                dossier[key] = value

    used, missing = [], []
    for _, refs in walk_evidence_refs(dossier):
        for r in refs:
            if r not in used:
                used.append(r)
    evidence = []
    for r in used:
        rec = digest.get(r) or extra.get(r)
        if not rec:
            missing.append(r)
            continue
        rec = {k: rec[k] for k in KEEP if k in rec}
        if r in hold:
            rec["prospect_safe"] = False
        evidence.append(rec)
    dossier["evidence"] = evidence

    v = dossier.setdefault("meta", {}).setdefault("validation", {})
    v.update({"facts_checked": stats["facts_checked"], "confirmed": stats["confirmed"], "corrected": stats["corrected"],
              "dropped": stats["dropped"], "people_checked": stats["people_checked"], "people_removed": stats["people_removed"]})
    v.setdefault("gates", [])

    (work / "dossier.json").write_text(json.dumps(dossier, ensure_ascii=False, indent=1))
    print(f"merged {len(list((work / 'parts').glob('*.json')))} parts -> {work / 'dossier.json'}: "
          f"{len(evidence)} evidence records ({sum(1 for e in evidence if e.get('prospect_safe'))} prospect-safe)")
    if missing:
        print("UNKNOWN evidence ids (not in the digest, not in extra_evidence): " + ", ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
