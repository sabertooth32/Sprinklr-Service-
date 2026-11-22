# F1 · Apply content QA and finish
**Mission:** apply what the three content reviewers found, rebuild, and leave a pack that passes every gate.
**Input:** `<work folder>/validation/Q1-completeness.json`, `Q2-plain-english.json`, `Q3-prospect-lens.json`, and `<work folder>/dossier.json`.

## Do
0. Edit `<work folder>/dossier.json` directly from here on. Do not run `engine/merge_parts.py` again: it would rebuild the dossier from the parts and undo your edits. Never change `verdict` or `prospect_safe` on an evidence record.
1. Read all three reviews. Apply every `block` and `fix` item by editing the dossier. Apply rewrites from Q2 where they keep the meaning.
2. If Q3 found a statement that is no longer true, remove it and anything built on it.
3. Never add a new fact. If a fix needs new evidence, remove the claim instead and list it under open questions.
4. Run `python3 engine/build.py <work folder>/dossier.json`. It must pass validation and the layout gate.
5. Add a gate entry `G7 Content QA` to `meta.validation.gates` with status and a one-line note, then rebuild once more.

6. Write every point a person must still check into the dossier's top-level `open_questions` (max 12, one short sentence each, starting with a verb). They print in the SDR brief.
7. List the reviewer items you could not fix because they sit in template text under `fixes_declined`, so the engine owner sees them.

## Return
Paths of the outputs, whether validation and layout passed, the fixes applied, and the fixes you declined with reasons.
