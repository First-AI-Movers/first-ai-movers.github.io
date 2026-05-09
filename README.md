# first-ai-movers.github.io

Company GitHub Pages bridge site for **First AI Movers**.

- Live: <https://first-ai-movers.github.io/>
- Purpose: a small, static, executive-grade bridge from the company GitHub
  organization [`First-AI-Movers`](https://github.com/First-AI-Movers) to
  public AI strategy, governance, implementation, and public-innovation work.

This is a bridge, not a product site. For depth, follow the links on the
live page or in [`llms.txt`](./llms.txt).

## Stack

- Static HTML and CSS
- No JavaScript
- No build system, no framework, no external dependencies
- System fonts only
- Dark executive theme

## Files

| File | Purpose |
|---|---|
| `index.html` | Single-page bridge with hero, About, Intelligence Surfaces, Open Work, Workstreams, Contact |
| `styles.css` | Dark theme, system fonts, mobile-first responsive |
| `404.html` | Themed not-found page |
| `robots.txt` | Crawl + AI-agent allowlist with `Sitemap` directive |
| `sitemap.xml` | Single-URL sitemap |
| `llms.txt` | Machine-readable organizational profile and primary references for LLM agents |
| `.nojekyll` | Disables Jekyll processing on GitHub Pages |
| `README.md` | This file |

## SEO / GEO

The page advertises:

- Canonical `<link>` to `https://first-ai-movers.github.io/`
- Open Graph + Twitter Card metadata
- JSON-LD `Organization` + `Person` (founder) schema (Schema.org `@graph`)
- Semantic HTML, WCAG-friendly contrast, keyboard-accessible links
- `llms.txt` for AI answer-engine retrieval
- Explicit robots policy for major search and AI crawlers

## Scope discipline

This bridge intentionally links **only** to public, verified surfaces:

- `firstaimovers.com`, `www.firstaimovers.com`
- `radar.firstaimovers.com`
- `articles.firstaimovers.com`
- `github.com/First-AI-Movers`
- `github.com/First-AI-Movers/articles`
- `hpcosta.github.io`
- `drhernanicosta.com`
- `linkedin.com/in/hernani-costa-ai-ceo-firstaimovers`

Private internal repositories of the organization (covering content
intelligence, governance workflows, and public innovation research) are
intentionally **not** linked from this public bridge.

## Local preview

Open `index.html` directly, or:

```sh
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Validation

Before committing changes:

- One `<h1>`, monotonic heading order
- `xmllint --noout sitemap.xml`
- JSON-LD parses as valid JSON
- `robots.txt` includes `Sitemap:` directive
- Every `href` resolves (HEAD 200) except documented bot-protection cases
- No secrets, tokens, or local paths in tracked files

## License

Page content © First AI Movers. Code is public; quote with attribution.
