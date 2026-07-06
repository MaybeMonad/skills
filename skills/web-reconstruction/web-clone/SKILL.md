---
name: web-clone
description: >
  Website cloning and web-effect reconstruction workflow. Use when the user says
  clone this website, reproduce this site, rebuild this page, reverse-engineer a
  WebGL/Canvas/Three.js effect, copy a website for local learning, visual clone,
  content remix, 复刻网站, 克隆网站, 抄个站, 仿站, 照着这个站做一个, or 把这个站搬下来改成我的.
metadata:
  origin: Adapted from Jane-xiaoer/claude-skill-web-clone, MIT.
  local_version: "1.0.0"
---

# Web Clone

Use this skill to clone, study, or remix a website without inventing fake source
code. The operating rule is simple: real source or real runtime evidence first.
Treat AI-generated clone plans as hypotheses until they are checked against
source, deployed assets, browser captures, screenshots, and working local code.

## Start Here

1. Create a clone workspace:
   ```bash
   node "$SKILL_DIR/scripts/init-clone.mjs" <slug> --url <url> [--root <dir>]
   ```
   If `SKILL_DIR` is not already known, resolve it as the directory containing
   this `SKILL.md` or the downloaded supporting files for this skill.
   The default clone root is `$WEB_CLONE_ROOT`, falling back to
   `~/projects/website-clones`.
2. Search for the real source before scraping:
   ```bash
   gh api "search/repositories?q=<site-or-product-keyword>" \
     | jq -r '.items[] | "\(.full_name) ⭐\(.stargazers_count) \(.description)"' \
     | head -10
   ```
3. If source is not found, run browser probes:
   ```bash
   node "$SKILL_DIR/scripts/recon-site.mjs" --url <url> --out <clone>/RECON --label original
   node "$SKILL_DIR/scripts/route-crawl.mjs" --url <url> --out <clone>/RECON/routes --label original
   node "$SKILL_DIR/scripts/interaction-probe.mjs" --url <url> --out <clone>/RECON/interactions --label original
   node "$SKILL_DIR/scripts/network-capture.mjs" --url <url> --out <clone>/RECON/network --label original
   node "$SKILL_DIR/scripts/sourcemap-hunt.mjs" --recon <clone>/RECON/original-recon.json --out <clone>/RECON/sourcemaps
   ```
4. Pick the cloning path from the evidence.
5. Build the clone, remove tracking, write notes, and verify in a real browser.
6. Replace content, media, and brand tokens only after the clone boundary is
   clear.

## Decision Tree

| Evidence | Path |
| --- | --- |
| Static HTML/CSS, few scripts | Mirror/download, remove tracking, replace content. |
| React/Vue/Next content site | Rebuild the templates and use local JSON fixtures for content/API. |
| SPA or SaaS/data-driven page | Capture XHR/fetch responses first; mock private writes, auth, payment, and permissions. |
| Multi-page marketing/CMS site | Crawl routes, identify repeated templates, implement representative page types. |
| Complex animation site | Capture scroll/hover/click states; preserve rhythm and visual language, document approximations. |
| WebGL/Canvas/Three.js heavy site | Find source/source maps first; otherwise capture runtime evidence and build a baseline replay before refactoring. |
| Static-built Astro/Vite SSG/Hugo site | Use `mirror-site.mjs` to capture deployed assets, including runtime-fetched binary assets. |
| Visual clone or content remix | Produce `design-dna.json` from recon, then keep the visual grammar while changing the content. |

## Evidence Discipline

- Mark technical claims as `SOURCE`, `PARTIAL`, or `GUESS`.
- `SOURCE` means direct evidence from source, source maps, network bodies,
  runtime dumps, frame captures, or verified screenshots.
- `PARTIAL` means a useful clue that still needs confirmation.
- `GUESS` means visual fitting, naming inference, default assumptions, or
  hand-tuned values.
- Do not compensate for unknown rendering, timing, color, or state bugs by
  adjusting unrelated parameters until it looks close. Record the gap.
- For WebGL/Canvas effects, create a minimal raw replay first. Only refactor
  after the baseline visually matches the original.

## Required Deliverables

- `NOTES.md`: source, license, mode, complexity, run command, replacement map,
  validation evidence, and unresolved gaps.
- `TEARDOWN.md`: required for complex interactive/WebGL clones; every important
  technical claim should include evidence level and source/file reference.
- `RECON/`: screenshots, route maps, network captures, interaction states,
  source-map results, visual diffs, and optional `design-dna.json`.
- `CLONE_REPORT.md`: original vs clone comparison when reporting quality.
- `CLONE_AUDIT.md`: tracking scripts, original-brand residue, external links,
  placeholders, and license/deploy risks.

Templates and scoring rules live in:
- `references/assessment.md`
- `references/deliverables.md`
- `references/reverse-engineering.md`
- `references/effect-extraction.md`
- `references/static-mirror.md`
- `references/design-dna.md`
- `references/complex-playbooks.md`

## Script Runtime

The scripts are plain Node `.mjs` files. Browser scripts require Playwright.
Install it in the clone project when needed:

```bash
npm install -D playwright
```

Run scripts via the skill directory:

```bash
SKILL_DIR=/path/to/web-clone
node "$SKILL_DIR/scripts/recon-site.mjs" --url https://example.com --out ./RECON --label original
```

If Playwright is installed somewhere else, set:

```bash
PLAYWRIGHT_MODULE_PATH=/absolute/path/to/node_modules/playwright
```

## Boundaries

- High-confidence: static pages, marketing sites, content frontends, and sites
  with accessible source or complete deployed assets.
- Partial or approximate: complex scroll narratives, custom WebGL effects
  without source, third-party embeds, CMS-backed content, and private APIs.
- Out of scope by default: real auth, payments, orders, recommendations,
  proprietary backends, private data, and copyrighted assets for public reuse.
- Public deployment requires license and asset checks. Public source on GitHub
  is not the same as a permissive license.

## Attribution

This skill is adapted from
`Jane-xiaoer/claude-skill-web-clone` under the MIT license. Keep
`LICENSE` and `NOTICE.md` with redistributed copies.
