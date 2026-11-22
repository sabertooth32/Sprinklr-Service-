"""Illustrative business case for a Sprinklr Service account dossier.

Five levers, applied in order on what is left, so nothing is counted twice.
See framework/04-value-model.md. All rates live in value_defaults.json.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).parent
SCENARIOS = ("low", "base", "high")


def load_defaults():
    return json.loads((HERE / "value_defaults.json").read_text())


def sig2(x):
    """Round to two significant figures. No false precision."""
    if not x:
        return 0
    digits = 1 - int(math.floor(math.log10(abs(x))))
    return round(x, digits)


def money(x, symbol="US$"):
    x = sig2(x)
    if x >= 1e9:
        return f"{symbol}{x / 1e9:.1f}B".replace(".0B", "B")
    if x >= 1e6:
        s = f"{x / 1e6:.1f}" if x < 1e7 else f"{x / 1e6:.0f}"
        return f"{symbol}{s.removesuffix('.0')}M"
    if x >= 1e3:
        return f"{symbol}{x / 1e3:.0f}K"
    return f"{symbol}{x:.0f}"


def count(x):
    x = sig2(x)
    if x >= 1e6:
        s = f"{x / 1e6:.1f}" if x < 1e7 else f"{x / 1e6:.0f}"
        return f"{s.removesuffix('.0')}M"
    if x >= 1e3:
        return f"{x / 1e3:.0f}K"
    return f"{x:.0f}"


def compute(dossier, defaults=None):
    d = defaults or load_defaults()
    bc = dossier.get("business_case", {})
    over = bc.get("overrides", {})
    unit = {k: v["value"] for k, v in d["cost_per_contact_usd"].items()}
    unit.update(over.get("cost_per_contact_usd", {}))
    assisted = d["assisted_types"]
    repeat_share = over.get("repeat_share", d["repeat_share"]["value"])
    realisation = over.get("handle_time_realisation", d["handle_time_realisation"]["value"])
    per_agent = over.get("contacts_per_agent_per_year", d["contacts_per_agent_per_year"]["value"])
    qa_span = over.get("agents_per_qa_analyst", d["agents_per_qa_analyst"]["value"])
    country = bc.get("agent_cost_country", "default")
    loaded = over.get("loaded_cost_per_agent_usd", d["loaded_cost_per_agent_usd"].get(country, d["loaded_cost_per_agent_usd"]["default"]))

    out = {"scenarios": {}, "unit_costs": unit, "loaded_cost_per_agent_usd": loaded}
    for s in SCENARIOS:
        vol = {t: 0.0 for t in assisted}
        for ch in dossier.get("channels", []):
            t = ch.get("type")
            v = (ch.get("volume") or {}).get(s)
            if t in vol and v:
                vol[t] += float(v)
        assisted_total = sum(vol.values())
        cost_today = sum(vol[t] * unit[t] for t in assisted)
        agents = (bc.get("agents_fte") or {}).get(s) or assisted_total / per_agent
        r = {k: over.get("levers", {}).get(k, {}).get(s, lv[s]) for k, lv in d["levers"].items()}

        levers = {}
        # 1 AI resolution
        contained = {t: vol[t] * r["ai_resolution"] for t in assisted}
        levers["ai_resolution"] = sum(contained[t] * max(unit[t] - unit["ai_resolved"], 0) for t in assisted)
        for t in assisted:
            vol[t] -= contained[t]
        # 2 Fewer repeat contacts
        removed = {t: vol[t] * repeat_share * r["repeat_reduction"] for t in assisted}
        levers["repeat_reduction"] = sum(removed[t] * unit[t] for t in assisted)
        for t in assisted:
            vol[t] -= removed[t]
        # 3 Voice to messaging
        shift = vol["voice"] * r["voice_shift"]
        levers["voice_shift"] = shift * max(unit["voice"] - unit["messaging"], 0)
        vol["voice"] -= shift
        vol["messaging"] += shift
        # 4 Faster handling
        remaining_cost = sum(vol[t] * unit[t] for t in assisted)
        levers["handle_time"] = remaining_cost * r["handle_time"] * realisation
        # 5 Automated quality
        levers["quality_automation"] = (agents / qa_span) * r["quality_automation"] * loaded

        total = sum(levers.values())
        out["scenarios"][s] = {
            "assisted_contacts": assisted_total,
            "cost_to_serve": cost_today,
            "agents_fte": agents,
            "levers": levers,
            "total": total,
            "pct_of_cost": (total / cost_today) if cost_today else 0,
            "ai_resolved_contacts": sum(contained.values()),
            "rates": r,
        }
    out["lever_labels"] = {k: v["label"] for k, v in d["levers"].items()}
    out["lever_meta"] = d["levers"]
    out["credibility_note"] = d["credibility_note"]
    out["defaults"] = d
    return out


if __name__ == "__main__":
    import sys
    dossier = json.loads(Path(sys.argv[1]).read_text())
    res = compute(dossier)
    for s in SCENARIOS:
        sc = res["scenarios"][s]
        print(f"{s:>5}: contacts {count(sc['assisted_contacts'])}, cost to serve {money(sc['cost_to_serve'])}, "
              f"value {money(sc['total'])} ({sc['pct_of_cost']:.0%})")
        for k, v in sc["levers"].items():
            print(f"        {res['lever_labels'][k]:<26} {money(v)}")
