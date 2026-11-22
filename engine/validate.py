#!/usr/bin/env python3
"""Code gates G5 (dossier) and G6 (content rules). See framework/05-validation-gates.md.

Usage: python3 engine/validate.py accounts/<slug>/dossier.json
Exit 0 = pass (warnings allowed). Exit 1 = errors. Writes validation_report.json next to the dossier.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

import jsonschema

sys.path.insert(0, str(Path(__file__).parent))
import value_model  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FACTS = ROOT / "framework" / "data" / "sprinklr-service-facts.json"
SCHEMA = Path(__file__).parent / "schema" / "dossier.schema.json"

# Maximum age in months by evidence category (framework/02-evidence-standard.md)
MAX_AGE = {"person": 6, "trigger": 12, "channel": 12, "customer_voice": 12, "ai": 24,
           "technology": 24, "strategy": 24, "volume": 24, "other": 24}
EXP_DIMS = ["access", "speed", "resolution", "continuity", "personal"]
AI_DIMS = ["self_service_ai", "agent_assist", "smart_routing", "insight_quality", "trust_control"]
WARN_WORDS, MAX_WORDS = 20, 30  # sentence length: warn above 20, error above 30 in prospect-facing text


def months_old(source_date, run):
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$", source_date or "")
    if not m:
        return None
    y, mo = int(m.group(1)), int(m.group(2) or 12)
    return (run.year - y) * 12 + (run.month - mo)


def sentences(text):
    text = re.sub(r"https?://\S+", "link", text or "")
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def walk_strings(node, path=""):
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from walk_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, f"{path}[{i}]")


def walk_evidence_refs(node, path=""):
    if isinstance(node, dict):
        for k, v in node.items():
            p = f"{path}.{k}" if path else k
            if k == "evidence" and isinstance(v, list) and all(isinstance(x, str) for x in v):
                yield p, v
            else:
                yield from walk_evidence_refs(v, p)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_evidence_refs(v, f"{path}[{i}]")


def channel_index(scores, dims):
    vals = [scores[d]["score"] for d in dims if scores.get(d) and scores[d].get("score") is not None]
    return (sum(vals) / len(vals) * 20, len(vals)) if vals else (None, 0)


def indexes(dossier):
    """Volume-weighted Experience and AI indexes. Shared with the builder so both show the same number."""
    out = {"channels": [], "experience": None, "ai": None}
    acc = {"experience": [0.0, 0.0], "ai": [0.0, 0.0]}
    for ch in dossier.get("channels", []):
        e, en = channel_index(ch["experience"], EXP_DIMS)
        a, an = channel_index(ch["ai"], AI_DIMS)
        w = ((ch.get("volume") or {}).get("base") or 0) or 1
        out["channels"].append({"id": ch["id"], "experience": e, "experience_dims": en, "ai": a, "ai_dims": an, "weight": w})
        for key, val in (("experience", e), ("ai", a)):
            if val is not None:
                acc[key][0] += val * w
                acc[key][1] += w
    for key in acc:
        out[key] = round(acc[key][0] / acc[key][1]) if acc[key][1] else None
    return out


def exp_level(i):
    for top, n, name in ((39, 1, "Fragmented"), (54, 2, "Functional"), (69, 3, "Connected"), (84, 4, "Orchestrated"), (100, 5, "Predictive")):
        if i <= top:
            return n, name


def ai_level(i):
    for top, n, name in ((14, 0, "No AI"), (34, 1, "Rule-based"), (54, 2, "Assisted"), (69, 3, "Generative"), (84, 4, "Agentic"), (100, 5, "Autonomous and governed")):
        if i <= top:
            return n, name


def validate(dossier):
    errors, warnings = [], []
    E, W = errors.append, warnings.append

    # --- G5.1 schema
    for err in sorted(jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(dossier), key=lambda e: list(e.path)):
        E(f"schema: {'/'.join(map(str, err.path)) or '(root)'}: {err.message[:160]}")
    if errors:
        return errors, warnings, {}

    run = date.fromisoformat(dossier["meta"]["run_date"])
    ev = {}
    for e in dossier["evidence"]:
        if e["id"] in ev:
            E(f"evidence: duplicate id {e['id']}")
        ev[e["id"]] = e

    # --- G5.2 every evidence record is traceable and fresh
    for e in dossier["evidence"]:
        i = e["id"]
        if e["evidence_type"] == "inferred":
            if not e.get("method"):
                E(f"evidence {i}: inferred facts must show their method")
        elif not re.match(r"^https?://", e.get("source_url", "")):
            E(f"evidence {i}: missing source_url")
        age = months_old(e["source_date"], run)
        limit = MAX_AGE.get(e.get("category", "other"), 24)
        if age is None and e["evidence_type"] != "inferred" and e["source_date"] != "undated":
            E(f"evidence {i}: source_date '{e['source_date']}' must be YYYY, YYYY-MM, YYYY-MM-DD or 'undated'")
        too_old = age is not None and age > limit
        if too_old and not e.get("stale"):
            E(f"evidence {i}: {age} months old, limit {limit} for '{e.get('category', 'other')}'. Mark stale: true")
        if e.get("prospect_safe"):
            why = []
            if e["verdict"] not in ("confirmed", "corrected"):
                why.append(f"verdict is {e['verdict']}")
            if e["evidence_type"] == "inferred":
                why.append("inferred")
            if e["confidence"] == "low":
                why.append("low confidence")
            if e.get("stale") or too_old:
                why.append("stale")
            if e["source_date"] == "undated":
                why.append("undated")
            if why:
                E(f"evidence {i}: marked prospect_safe but {', '.join(why)}")

    # --- G5.3 every reference resolves
    used = set()
    for path, refs in walk_evidence_refs({k: v for k, v in dossier.items() if k != "evidence"}):
        for r in refs:
            used.add(r)
            if r not in ev:
                E(f"{path}: unknown evidence id {r}")
    orphan = sorted(set(ev) - used)
    if orphan:
        W(f"evidence: {len(orphan)} records are never referenced ({', '.join(orphan[:6])}{'…' if len(orphan) > 6 else ''})")

    caps = {c["id"] for c in json.loads(FACTS.read_text())["capabilities"]} if FACTS.exists() else None
    if caps is not None:
        def check_caps(node, path=""):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k == "capability_ids":
                        for c in v:
                            if c not in caps:
                                E(f"{path}.capability_ids: unknown Sprinklr capability '{c}'")
                    else:
                        check_caps(v, f"{path}.{k}" if path else k)
            elif isinstance(node, list):
                for n, v in enumerate(node):
                    check_caps(v, f"{path}[{n}]")
        check_caps(dossier)

    # --- G5.4 scores carry evidence
    ch_ids = set()
    for ch in dossier["channels"]:
        ch_ids.add(ch["id"])
        for block, dims in (("experience", EXP_DIMS), ("ai", AI_DIMS)):
            scored = 0
            for d in dims:
                s = ch[block].get(d)
                if not s or s.get("score") is None:
                    continue
                scored += 1
                if s["basis"] == "not_visible":
                    E(f"channel {ch['id']}.{block}.{d}: has a score but basis is not_visible. Use null")
                if not s.get("evidence"):
                    E(f"channel {ch['id']}.{block}.{d}: score {s['score']} has no evidence")
            if scored == 0:
                W(f"channel {ch['id']}: no {block} dimension scored")
        v = ch.get("volume")
        if v and not (v["low"] <= v["base"] <= v["high"]):
            E(f"channel {ch['id']}: volume must satisfy low <= base <= high")
        if v and v["basis"] == "estimate" and not v.get("method"):
            E(f"channel {ch['id']}: estimated volume needs a method")
    for st in dossier["journey"]["stages"]:
        for bp in st["break_points"]:
            if bp["channel_id"] not in ch_ids:
                E(f"journey stage {st['n']} break point {bp['id']}: unknown channel_id {bp['channel_id']}")
            if not bp["evidence"]:
                E(f"journey break point {bp['id']}: no evidence")
            if bp["prospect_safe"] and not all(ev.get(r, {}).get("prospect_safe") for r in bp["evidence"]):
                E(f"journey break point {bp['id']}: prospect_safe but rests on evidence that is not")
    if [s["n"] for s in dossier["journey"]["stages"]] != list(range(1, 8)):
        E("journey: stages must be numbered 1 to 7 in order")
    for g in dossier["gap_map"]:
        if g["channel_id"] not in ch_ids:
            E(f"gap_map '{g['gap'][:30]}': unknown channel_id {g['channel_id']}")
        if not g["capability_ids"]:
            E(f"gap_map '{g['gap'][:30]}': no Sprinklr capability mapped")

    # --- G5.5 ICP maths
    icp = dossier["icp"]
    total = sum(l["points"] for l in icp["scorecard"])
    if abs(total - icp["total"]) > 0.01:
        E(f"icp: scorecard adds to {total}, total says {icp['total']}")
    for l in icp["scorecard"]:
        if l["points"] > l["max"]:
            E(f"icp: '{l['line']}' scores {l['points']} above its maximum {l['max']}")
    want = "A" if total >= 75 else "B" if total >= 55 else "C"
    if icp["tier"] != want:
        E(f"icp: {total} points is tier {want}, dossier says {icp['tier']}")
    if any(h["triggered"] for h in icp["hard_stops"]):
        E("icp: a hard stop is triggered. This account must not get a pack")
    if want == "C":
        E("icp: tier C. This account must not get a pack")

    for ch in dossier["channels"]:
        if len(ch["name"]) > 30:
            E(f"channel {ch['id']}: name \"{ch['name']}\" is {len(ch['name'])} characters. Keep channel names to 30. Put detail in strengths or headline_gap")
    for c in dossier["contacts"]:
        for field in ("best_channel",):
            if len(c[field].split()) > 14:
                W(f"contact {c['name']}: {field} is long. Keep it to 14 words")
    for f in dossier["snapshot"]["facts"]:
        if len(f["label"]) > 32:
            E(f"snapshot fact label \"{f['label']}\" is {len(f['label'])} characters. Keep labels to 32")
        if len(f["value"]) > 20:
            E(f"snapshot fact '{f['label']}': value \"{f['value']}\" is {len(f['value'])} characters. Keep headline values to 20, e.g. \"6.1M\" or \"SGD 22.9B\"")

    # --- G5.6 people
    names = []
    for c in dossier["contacts"]:
        names.append(c["name"])
        if not c["evidence"]:
            E(f"contact {c['name']}: no evidence for the role")
        if c["priority"] == 1 and c["role_status"] != "current":
            W(f"contact {c['name']}: priority 1 but role only 'likely_current'. Check LinkedIn before sending")
        if re.search(r"\b(mystery[- ]shopp\w*|we (tested|audited|tried|asked|called|messaged|chatted)|our (audit|test)s?)\b", c["opener"].lower()):
            E(f"contact {c['name']}: opener describes a test of their channels. Say what a customer sees, not what we did")
        for field, limit in (("hook", 24), ("opener", 30)):
            n = len(c[field].split())
            if n > limit:
                E(f"contact {c['name']}: {field} is {n} words, limit {limit}")
    if len([c for c in dossier["contacts"] if c["priority"] == 1]) < 3:
        W("contacts: fewer than 3 priority-1 contacts")

    # --- G5.7 business case computes
    country = dossier["business_case"]["agent_cost_country"]
    if country not in value_model.load_defaults()["loaded_cost_per_agent_usd"]:
        W(f"business_case: no agent cost for country '{country}'. Using the default. Add it to engine/value_defaults.json")
    result = value_model.compute(dossier)
    sc = result["scenarios"]
    if sc["base"]["total"] <= 0:
        E("business_case: no volume on assisted channels, so no value can be computed")
    if not (sc["low"]["total"] <= sc["base"]["total"] <= sc["high"]["total"]):
        E("business_case: scenarios out of order")
    if sc["base"]["pct_of_cost"] > 0.45:
        W(f"business_case: base value is {sc['base']['pct_of_cost']:.0%} of cost to serve. That will not be believed")

    # --- G6 content rules: what the prospect may see
    pv = dossier["prospect_view"]
    for path, refs in walk_evidence_refs(pv, "prospect_view"):
        for r in refs:
            if r in ev and not ev[r].get("prospect_safe"):
                E(f"{path}: uses evidence {r}, which is not prospect_safe")
        if not refs:
            E(f"{path}: prospect-facing statement has no evidence")
    pv_text = " ".join(s for _, s in walk_strings(pv)).lower()
    for n in names:
        if n.lower() in pv_text:
            E(f"prospect_view: names a contact ({n}). People never appear in prospect content")
    for inc in dossier["incumbents"]:
        if inc["status"] != "in-house" and len(inc["vendor"]) > 3 and re.search(rf"\b{re.escape(inc['vendor'].lower())}\b", pv_text):
            E(f"prospect_view: names incumbent vendor '{inc['vendor']}'")
    for bad in ("fail", "fails", "failed", "failure", "terrible", "worst", "broken", "poor", "bad"):
        if re.search(rf"\b{bad}\b", pv_text):
            W(f"prospect_view: contains '{bad}'. Phrase gaps as opportunities")
    crisp = [("prospect_view", pv, True), ("outreach", dossier["outreach"], True),
             ("contacts", dossier["contacts"], False), ("entry_points", dossier["entry_points"], False),
             ("journey", dossier["journey"], False), ("gap_map", dossier["gap_map"], False)]
    long_count = 0
    for label, node, strict in crisp:
        for path, text in walk_strings(node, label):
            for s in sentences(text):
                n = len(s.split())
                if n > MAX_WORDS and strict:
                    E(f"{path}: sentence of {n} words (limit {MAX_WORDS}): \"{s[:60]}…\"")
                elif n > WARN_WORDS:
                    long_count += 1
    if long_count:
        W(f"plain English: {long_count} sentences are longer than {WARN_WORDS} words")
    for seq in dossier["outreach"]["sequences"]:
        for st in seq["steps"]:
            words = len(st["body"].split())
            cap = {"email": 120, "linkedin": 60, "call": 90, "event": 90}[st["channel"]]
            if words > cap:
                E(f"outreach '{seq['persona']}' day {st['day']} {st['channel']}: {words} words, limit {cap}")
            if st["channel"] == "email" and not st.get("subject"):
                E(f"outreach '{seq['persona']}' day {st['day']}: email needs a subject")

    # --- live-test rules (framework/08-live-test-rules.md)
    for t in dossier["mystery_shop"]:
        q = t["opening_question"].lower()
        if "sprinklr" in " ".join(str(v) for v in t.values()).lower():
            E(f"mystery_shop {t['id']}: mentions Sprinklr. Live tests are run as an ordinary member of the public")
# "What should I do if I see a transaction I do not recognise?" is honest. "I have a fraudulent transaction" is not.
        stated = re.sub(r"\b(if|when|in case|suppose)\b[^?.!]*", "", q)  # drop hypothetical clauses, keep what is asserted
        if re.search(r"\bi (have|had|see|saw|lost|made|sent|paid|was charged|was debited|got charged|want to (make|file|lodge) a complaint|want to complain)\b", stated) or \
                re.search(r"\b(my|our) (card|account|transaction|payment|transfer|money|bill|order|booking|policy|claim|complaint|refund)\b", stated):
            E(f"mystery_shop {t['id']}: the question claims a personal case (\"{t['opening_question'][:60]}\"). Ask a general question instead")
    for seq in dossier["outreach"]["sequences"]:
        for st in seq["steps"]:
            if re.search(r"\b(mystery[- ]shopp\w*|we (tested|audited)|our audit)\b", st["body"].lower()):
                E(f"outreach '{seq['persona']}' day {st['day']}: do not say we tested, audited or mystery-shopped them")

    # --- gates recorded by the swarm
    for g in dossier["meta"]["validation"]["gates"]:
        if g["status"] == "fail":
            E(f"gate {g['gate']} failed: {g.get('note', '')}")

    idx = indexes(dossier)
    stats = {
        "evidence_total": len(ev),
        "evidence_prospect_safe": sum(1 for e in ev.values() if e.get("prospect_safe")),
        "evidence_by_verdict": {v: sum(1 for e in ev.values() if e["verdict"] == v) for v in ("confirmed", "corrected", "unverified", "stale")},
        "experience_index": idx["experience"], "ai_index": idx["ai"],
        "value_low": result["scenarios"]["low"]["total"], "value_base": result["scenarios"]["base"]["total"],
        "value_high": result["scenarios"]["high"]["total"],
    }
    return errors, warnings, stats


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    try:
        dossier = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        print(f"FAIL  dossier is not valid JSON: {e}")
        sys.exit(1)
    errors, warnings, stats = validate(dossier)
    report = {"dossier": str(path), "passed": not errors, "errors": errors, "warnings": warnings, "stats": stats}
    (path.parent / "validation_report.json").write_text(json.dumps(report, indent=1))
    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    print(f"\n{'PASS' if not errors else 'FAIL'}: {len(errors)} errors, {len(warnings)} warnings")
    if stats:
        print(f"evidence {stats['evidence_total']} ({stats['evidence_prospect_safe']} prospect-safe) · "
              f"Experience index {stats['experience_index']} · AI index {stats['ai_index']} · "
              f"value {value_model.money(stats['value_low'])}–{value_model.money(stats['value_base'])}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
