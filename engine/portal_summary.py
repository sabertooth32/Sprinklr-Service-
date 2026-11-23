#!/usr/bin/env python3
"""Print the short summary the SDR portal shows for a finished pack.

Usage: python3 engine/portal_summary.py accounts/<slug>/dossier.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build  # noqa: E402
import validate as gates  # noqa: E402


def main():
    d = json.loads(Path(sys.argv[1]).read_text())
    idx = gates.indexes(d)
    n = len(d["channels"])
    seen = lambda block, dims: sum(1 for ch in d["channels"] for k, _ in dims if (ch[block].get(k) or {}).get("score") is not None)
    exp_ok = seen("experience", build.EXP) / (n * 5) >= build.MIN_COVERAGE
    ai_ok = seen("ai", build.AI) / (n * 5) >= build.MIN_COVERAGE
    e, a = idx["experience"] or 0, idx["ai"] or 0
    p1 = [c for c in d["contacts"] if c["priority"] == 1]
    print(json.dumps({
        "fit": f"Tier {d['icp']['tier']} · {round(d['icp']['total'])}",
        "experience": f"{e} · {gates.exp_level(e)[1]}" if exp_ok else "Early read",
        "ai": f"{a} · {gates.ai_level(a)[1]}" if ai_ok else "Early read",
        "contacts": f"{len(p1)} people",
        "ways": [ep["title"] for ep in d["entry_points"]][:3],
        "why_now": d["snapshot"]["why_now_headline"],
        "open_points": len(d.get("open_questions", [])),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
