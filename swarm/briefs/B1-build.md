# B1 · Build the pack
**Mission:** turn the validated dossier into the PDFs and pass the layout gate.
**Input:** `<work folder>/dossier.json`.

## Do
1. Run `python3 engine/build.py <work folder>/dossier.json`.
2. If it prints `LAYOUT FAIL`, a page overflows. Fix the **dossier text**, never the templates: shorten the longest text on that page, or cut the least important row. Keep the meaning. Re-run until the layout gate is clean.
3. If validation fails, fix the dossier as `swarm/briefs/S1-synthesise.md` describes and re-run.
4. Open each PDF page (Read tool) and look at it. Fix anything cut off, overlapping or empty by editing the dossier.

## Return
Paths of the three outputs, page counts, whether validation and layout both passed, and what you shortened.
