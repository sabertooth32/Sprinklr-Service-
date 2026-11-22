#!/usr/bin/env python3
"""Build the SDR pack from a validated dossier.

Usage: python3 engine/build.py accounts/<slug>/dossier.json [--force] [--no-pdf]

Outputs in accounts/<slug>/out/:
  sdr-brief.html / .pdf            internal, step-by-step brief for the SDR
  prospect-infographic.html / .pdf  outside-in view to send to the prospect
  outreach-kit.md                   copy-and-paste messages
"""
import base64
import json
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import validate as gates  # noqa: E402
import value_model as vm  # noqa: E402

EXP = [("access", "Access"), ("speed", "Speed"), ("resolution", "Resolution"), ("continuity", "Continuity"), ("personal", "Personal")]
AI = [("self_service_ai", "Self-service AI"), ("agent_assist", "Agent assist"), ("smart_routing", "Smart routing"),
      ("insight_quality", "Insight & quality"), ("trust_control", "Trust & control")]
EXP_LEVELS = ["Fragmented", "Functional", "Connected", "Orchestrated", "Predictive"]
AI_LEVELS = ["No AI", "Rule-based", "Assisted", "Generative", "Agentic", "Autonomous"]
CHANNEL_TYPE_LABEL = {"voice": "Voice", "chat": "Chat", "messaging": "Messaging", "email": "Email / form", "social": "Social",
                      "self_service": "Self-service", "in_person": "In person"}
ROLE_ORDER = {"economic buyer": 0, "champion": 1, "technical evaluator": 2, "user leader": 3, "influencer": 4, "blocker": 5}


def chunks(seq, n):
    seq = list(seq)
    return [seq[i:i + n] for i in range(0, len(seq), n)] or [[]]


def initials(name):
    parts = [p for p in name.replace("-", " ").split() if p[0].isalpha()]
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


def cell(score):
    """CSS classes and text for one heatmap cell."""
    if not score or score.get("score") is None:
        return {"cls": "c na", "txt": "?", "title": "Not visible from outside. Confirm in discovery."}
    s = score["score"]
    lvl = max(0, min(5, round(s)))
    cls = f"c l{lvl}" + (" inf" if score.get("basis") == "inferred" else "")
    txt = f"{s:g}"
    return {"cls": cls, "txt": txt, "title": score.get("note", "")}


def build_context(dossier, theme):
    facts = json.loads((ROOT / "framework" / "data" / "sprinklr-service-facts.json").read_text())
    caps = {c["id"]: {**c, "name": c["name"].split(" (")[0]} for c in facts["capabilities"]}  # short names for pills
    ev = {e["id"]: e for e in dossier["evidence"]}
    idx = gates.indexes(dossier)
    by_id = {c["id"]: c for c in idx["channels"]}
    val = vm.compute(dossier)
    sc = val["scenarios"]

    channels = []
    max_vol = max([(c.get("volume") or {}).get("base") or 0 for c in dossier["channels"]] + [1])
    for ch in dossier["channels"]:
        ci = by_id[ch["id"]]
        v = ch.get("volume") or {}
        channels.append({
            **ch,
            "type_label": CHANNEL_TYPE_LABEL[ch["type"]],
            "exp_cells": [cell(ch["experience"].get(k)) for k, _ in EXP],
            "ai_cells": [cell(ch["ai"].get(k)) for k, _ in AI],
            "exp_index": None if ci["experience"] is None else round(ci["experience"]),
            "ai_index": None if ci["ai"] is None else round(ci["ai"]),
            "exp_partial": ci["experience_dims"] < 3, "ai_partial": ci["ai_dims"] < 3,
            "vol_fmt": vm.count(v["base"]) if v.get("base") else "n/a",
            "vol_range": f"{vm.count(v['low'])}–{vm.count(v['high'])}" if v.get("base") else "",
            "vol_pct": round(100 * (v.get("base") or 0) / max_vol),
        })
    chan = {c["id"]: c for c in channels}

    e_i, a_i = idx["experience"] or 0, idx["ai"] or 0
    e_lvl, a_lvl = gates.exp_level(e_i), gates.ai_level(a_i)
    lever_rows = []
    top = max(sc["high"]["levers"].values()) or 1
    for k, label in val["lever_labels"].items():
        meta = val["lever_meta"][k]
        lever_rows.append({
            "label": label, "applies": meta["applies"], "reference": meta["reference"],
            "low": vm.money(sc["low"]["levers"][k]), "base": vm.money(sc["base"]["levers"][k]), "high": vm.money(sc["high"]["levers"][k]),
            "low_pct": round(100 * sc["low"]["levers"][k] / top), "base_pct": round(100 * sc["base"]["levers"][k] / top),
            "high_pct": round(100 * sc["high"]["levers"][k] / top),
            "rates": f"{meta['low']:.0%} / {meta['base']:.0%} / {meta['high']:.0%}",
        })
    d = val["defaults"]
    unit_rows = [{"label": CHANNEL_TYPE_LABEL.get(k, "AI-resolved contact"), "value": f"US${val['unit_costs'][k]:.2f}",
                  "basis": "benchmark" if v["basis"] == "benchmark" else "assumption", "source": v["source"]}
                 for k, v in d["cost_per_contact_usd"].items()]
    value = {
        s: {"total": vm.money(sc[s]["total"]), "cost": vm.money(sc[s]["cost_to_serve"]), "contacts": vm.count(sc[s]["assisted_contacts"]),
            "agents": vm.count(sc[s]["agents_fte"]), "pct": f"{sc[s]['pct_of_cost']:.0%}", "ai_contacts": vm.count(sc[s]["ai_resolved_contacts"])}
        for s in vm.SCENARIOS
    }

    contacts = sorted(dossier["contacts"], key=lambda c: (c["priority"], ROLE_ORDER.get(c["deal_role"], 9)))
    for c in contacts:
        c["initials"] = initials(c["name"])
    centres = []
    for bc in dossier["buying_centres"]:
        centres.append({**bc, "people": [c for c in contacts if c["centre"] == bc["centre"]]})
    stray = [c for c in contacts if c["centre"] not in {b["centre"] for b in dossier["buying_centres"]}]
    if stray:
        centres.append({"centre": "Other", "what_they_own": "", "our_angle": "", "people": stray})

    stages = []
    for st in dossier["journey"]["stages"]:
        bps = sorted(st["break_points"], key=lambda b: -b["severity"])
        stages.append({**st, "break_points": [{**b, "channel": chan[b["channel_id"]]["name"],
                                                "caps": [caps[c]["name"] for c in b["capability_ids"] if c in caps]} for b in bps]})
    all_bps = [b for st in stages for b in st["break_points"]]

    gaps = sorted(dossier["gap_map"], key=lambda g: g["priority"])
    for g in gaps:
        g["channel"] = chan[g["channel_id"]]["name"]
        g["caps"] = [caps[c]["name"] for c in g["capability_ids"] if c in caps]
    for ep in dossier["entry_points"]:
        ep["caps"] = [caps[c]["name"] for c in ep["capability_ids"] if c in caps]
    pv = dossier["prospect_view"]
    for o in pv["opportunities"]:
        o["caps"] = [caps[c] for c in o["capability_ids"] if c in caps]
    pv_sources = []
    for block in (pv["strengths"], pv["observations"]):
        for item in block:
            for r in item["evidence"]:
                if ev[r] not in pv_sources:
                    pv_sources.append(ev[r])
    obs_by_stage = {}
    for o in pv["observations"]:
        obs_by_stage.setdefault(o["stage"], []).append(o)

    report_path = None
    logo = None
    if theme.get("logo_path"):
        p = (ROOT / theme["logo_path"])
        if p.exists():
            mime = "image/svg+xml" if p.suffix == ".svg" else f"image/{p.suffix.lstrip('.')}"
            logo = f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

    evidence_used = [e for e in dossier["evidence"]]
    return {
        "d": dossier, "theme": theme, "logo": logo, "caps": caps, "ev": ev, "chan": chan, "channels": channels,
        "EXP": EXP, "AI": AI, "EXP_LEVELS": EXP_LEVELS, "AI_LEVELS": AI_LEVELS,
        "exp_index": e_i, "ai_index": a_i, "exp_level": e_lvl, "ai_level": a_lvl,
        "value": value, "lever_rows": lever_rows, "unit_rows": unit_rows, "credibility_note": val["credibility_note"],
        "loaded_cost": f"US${val['loaded_cost_per_agent_usd']:,.0f}",
        "contacts": contacts, "p1": [c for c in contacts if c["priority"] == 1], "centres": centres,
        "contact_pages": chunks([c for c in contacts if c["priority"] == 1], 6),
        "stages": stages, "all_bps": all_bps, "gaps": gaps,
        "sequence_pages": dossier["outreach"]["sequences"],
        "evidence_pages": chunks(evidence_used, 22),
        "pv": pv, "pv_sources": pv_sources, "obs_by_stage": obs_by_stage,
        "facts": facts, "report_path": report_path,
        "analyst_safe": [a for a in facts.get("analyst_recognition", []) if "NOT" not in a["what"] and "not included" not in a["what"]][:3],
    }


def outreach_md(ctx):
    d = ctx["d"]
    out = [f"# Outreach kit — {d['meta']['account']}", "",
           f"_Built {d['meta']['run_date']} by Account Radar. Internal. Do the five pre-send checks first._", "",
           f"**Positioning:** {d['outreach']['positioning']}", "", "## First lines by contact", "",
           "| Contact | Role | Hook | Opener |", "|---|---|---|---|"]
    for c in ctx["p1"]:
        out.append(f"| {c['name']}, {c['title']} | {c['deal_role']} | {c['hook']} | {c['opener']} |")
    for seq in d["outreach"]["sequences"]:
        out += ["", f"## Sequence — {seq['persona']}", "", f"For: {', '.join(seq['for_contacts']) or 'this persona'}", ""]
        for st in seq["steps"]:
            out.append(f"### Day {st['day']} · {st['channel'].title().replace('Linkedin', 'LinkedIn')}" + (f" · Subject: {st['subject']}" if st.get("subject") else ""))
            out += ["", "```", st["body"], "```", ""]
    return "\n".join(out) + "\n"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if not args:
        sys.exit(__doc__)
    path = Path(args[0]).resolve()
    dossier = json.loads(path.read_text())

    errors, warnings, stats = gates.validate(dossier)
    report = {"dossier": str(path), "passed": not errors, "errors": errors, "warnings": warnings, "stats": stats}
    (path.parent / "validation_report.json").write_text(json.dumps(report, indent=1))
    if errors and "--force" not in flags:
        print(f"Build refused: the dossier has {len(errors)} validation errors. Run engine/validate.py to see them.")
        sys.exit(1)

    theme = json.loads((HERE / "theme" / "sprinklr.json").read_text())
    env = Environment(loader=FileSystemLoader(HERE / "templates"), autoescape=select_autoescape(["html", "j2"]),
                      trim_blocks=True, lstrip_blocks=True)
    ctx = build_context(dossier, theme)
    ctx["report"] = report
    ctx["css"] = env.get_template("base.css").render(theme=theme)

    out = path.parent / "out"
    out.mkdir(exist_ok=True)
    built = []
    for tpl, name in (("brief.html.j2", "sdr-brief"), ("infographic.html.j2", "prospect-infographic")):
        html = env.get_template(tpl).render(**ctx)
        (out / f"{name}.html").write_text(html)
        built.append(name)
    (out / "outreach-kit.md").write_text(outreach_md(ctx))

    if "--no-pdf" not in flags:
        r = subprocess.run(["node", str(HERE / "render.mjs"), str(out), *built], text=True)
        if r.returncode:
            sys.exit(r.returncode)
    print(f"Built pack in {out}")


if __name__ == "__main__":
    main()
