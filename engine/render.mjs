// Render the built HTML pages to PDF and run the layout gate: no page may overflow its frame.
// Usage: node engine/render.mjs <out dir> <name> [<name> ...]
import { createRequire } from 'node:module';
import path from 'node:path';
import fs from 'node:fs';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [outDir, ...names] = process.argv.slice(2);
const browser = await chromium.launch();
let failed = false;
for (const name of names) {
  let bad = false;
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('file://' + path.resolve(outDir, `${name}.html`));
  await page.evaluate(() => document.fonts.ready);
  // Layout gate: any element that spills out of its page, or any clipped text block.
  const problems = await page.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, i) => {
      const box = pg.getBoundingClientRect();
      const limit = box.bottom - 34; // keep clear of the footer
      let worst = 0, who = '';
      pg.querySelectorAll('.body *').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.height && r.bottom - limit > worst) { worst = r.bottom - limit; who = (el.className || el.tagName) + ': ' + (el.textContent || '').trim().slice(0, 50); }
        if (r.width && r.right > box.right - 20 && !el.closest('td')) out.push(`page ${i + 1}: element runs off the right edge (${(el.textContent || '').trim().slice(0, 40)})`);
      });
      // A box whose own content spills out of it will overlap its neighbours.
      pg.querySelectorAll('.card, .opp, .msg, .person, .pin, .obs, .stage, .chip').forEach(el => {
        if (el.scrollHeight - el.clientHeight > 3) out.push(`page ${i + 1} "${pg.dataset.title || ''}": a box is too small for its text (${(el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 50)})`);
      });
      if (worst > 1) out.push(`page ${i + 1} "${pg.dataset.title || ''}": content overflows by ${Math.round(worst)}px (${who})`);
    });
    return out;
  });
  if (problems.length) { failed = true; bad = true; console.log(`LAYOUT FAIL ${name}\n  ` + [...new Set(problems)].slice(0, 12).join('\n  ')); }
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: path.resolve(outDir, `${name}.pdf`), width: '1280px', height: '720px', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  const pages = await page.locator('.page').count();
  console.log(`${bad ? 'built (with layout issues)' : 'ok'}  ${name}.pdf  ${pages} pages`);
  if (process.env.SHOTS) {
    const dir = path.resolve(outDir, 'shots'); fs.mkdirSync(dir, { recursive: true });
    await page.emulateMedia({ media: 'print' });
    const els = await page.locator('.page').all();
    for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(dir, `${name}-${String(i + 1).padStart(2, '0')}.png`) });
  }
  await page.close();
}
await browser.close();
process.exit(failed ? 2 : 0);
