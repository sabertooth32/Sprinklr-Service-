# F1 · Apply content QA and finish
**Mission:** apply what the three content reviewers found, rebuild, and leave a pack that passes every gate.
**Input:** `<work folder>/validation/Q1-completeness.json`, `Q2-plain-english.json`, `Q3-prospect-lens.json`, and `<work folder>/dossier.json`.

## Do
1. Read all three reviews. Apply every `block` and `fix` item by editing the dossier. Apply rewrites from Q2 where they keep the meaning.
2. If Q3 found a statement that is no longer true, remove it and anything built on it.
3. Never add a new fact. If a fix needs new evidence, remove the claim instead and list it under open questions.
4. Run `python3 engine/build.py <work folder>/dossier.json`. It must pass validation and the layout gate.
5. Add a gate entry `G7 Content QA` to `meta.validation.gates` with status and a one-line note, then rebuild once more.

## Return
Paths of the outputs, whether validation and layout passed, the fixes applied, and the fixes you declined with reasons.
