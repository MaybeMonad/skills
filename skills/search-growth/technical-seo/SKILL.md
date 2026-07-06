---
name: technical-seo
description: Technical SEO workflow for canonical metadata, public routes, redirects, sitemap, robots.txt, structured data, image alt text, SSR crawlability, indexing submission, and public discoverability. Use when changing SEO copy, route canonicals, search visibility, crawler access, sitemap inventory, IndexNow, Google Search Console, or Bing Webmaster Tools.
---

# Technical SEO

Use this skill to keep search-facing work **canonical**: one public URL, one copy
source, one indexing inventory, and one proof path for each SEO claim.

## Workflow

1. Name the SEO branch:
   - Metadata copy.
   - Canonical URL or redirect.
   - Sitemap or robots.
   - Structured data.
   - Public image alt text or generated HTML.
   - Dynamic public inventory.
   - Indexing submission or inspection.
   - Crawlability, SSR payload, or rendering performance.
   - Completion criterion: the affected public routes and SEO branch are
     explicit.
2. Inspect the current source of truth:
   - Search route files, copy constants, head helpers, sitemap, robots,
     redirects, footer/nav links, generated routes, and SEO tests.
   - If the task depends on search-engine behavior or indexing APIs, verify
     current official docs or webmaster tooling before acting.
   - Completion criterion: every assumption that affects SEO behavior is
     verified in current source or marked unknown.
3. Preserve copy authority:
   - Treat user-supplied SEO, legal, pricing, product, or landing copy as exact
     unless the user asks for a rewrite.
   - Prefer an existing shared copy object or route contract over route-local
     duplicate strings.
   - Check truncation rules before changing descriptions.
   - Completion criterion: the authoritative copy source and route consumer are
     named.
4. Make the route canonical:
   - Pick the canonical public URL.
   - Keep old URLs only as intentional redirects or compatibility aliases.
   - Sweep footer links, nav links, sitemap entries, internal rich-text links,
     runtime allowlists, and tests for stale paths.
   - Completion criterion: old-path and new-path searches have been reviewed,
     and every remaining old path has a reason.
5. Align metadata:
   - Emit title, description, canonical link, robots meta, Open Graph, Twitter
     card, and primary image consistently.
   - Use `noindex` for private, draft, unavailable, duplicate, admin,
     auth-only, or non-ready pages.
   - Add structured data only when the page content actually supports it.
   - Completion criterion: metadata matches the page's real public content and
     indexability state.
6. Align indexing inventory:
   - Ensure `robots.txt` allows intended crawlers and blocks private or
     non-public surfaces.
   - Ensure `sitemap.xml` contains only canonical, indexable public URLs.
   - Include `lastmod` only when the source timestamp is meaningful and
     formatted correctly.
   - Dynamic sitemap rows must be filtered by public visibility and readiness.
   - Completion criterion: sitemap and robots behavior match the canonical
     route policy.
7. Verify submission separately from indexing:
   - For IndexNow or similar push APIs, verify key-file reachability and
     request acceptance.
   - For Google, use sitemap submission or Search Console inspection according
     to the current supported workflow.
   - Never say a URL is indexed unless an inspection tool or search-engine
     source proves it.
   - Completion criterion: the report distinguishes submitted, accepted,
     crawled, and indexed.
8. Add guardrails:
   - Update focused tests for copy exactness, canonical paths, sitemap
     inventory, robots rules, redirects, structured data, and image alt text.
   - Regenerate route manifests after route-file changes.
   - Run the narrowest useful checks first, then broader checks when shared
     behavior changed.
   - Completion criterion: verification commands and residual risks are
     reported.

## Output Rules

- Lead with what changed and what was verified.
- State stale assumptions explicitly.
- Report indexing claims precisely: `submitted`, `accepted`, `inspected`, or
  `indexed`.
- If verification is blocked, name the missing tool, credential, live URL, or
  external source.

## Traps

- A route can be fixed while footer, sitemap, nav, generated routes, or tests
  still point to an old URL.
- Exact copy can be silently truncated by a shared metadata helper.
- A successful build does not prove crawler-visible HTML, canonical redirects,
  or indexing submission.
- Indexing submission acceptance is not indexing.
- Search-engine APIs and webmaster rules change, so verify current official
  behavior when it matters.
