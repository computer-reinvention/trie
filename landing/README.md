# landing

A static, dependency-free landing page for trie, written for the
agent-first pitch: two indexes (meaning + intent) that live in the repo
as plain Markdown, kept fresh by `trie sync` and kept honest by the
pre-commit gate — no external product or service involved.

Design: single white theme, no animation, terse copy.

## Running

```bash
open landing/index.html
```

No build step. No package manager. Three files:

- `index.html` — structure and copy
- `style.css` — all styling; one light theme, no media-query theming
- `story.js` — copy-to-clipboard on the install command, nothing else

## Structure

1. **nav** — sticky, anchors to each section, GitHub link
2. **hero** — "Context infrastructure for coding agents", install
   command with copy button, fact strip
3. **the problem** — one lede: agents burn context reconstructing
   intent from code
4. **two indexes** — meaning (`triefacts/`) and intent
   (`triefacts/triediffs/`) side by side, each with a real file excerpt
5. **the loop** — five numbered steps: edit → record intent → gate →
   digest ships with the commit → sync regenerates what drifted;
   payoff is `trie read <symbol> --history`
6. **tools** — `grep` / `read` / `trace`, plus the self-hosting proof
7. **in your repo** — repo tree figure + versioned/reviewed/merged/
   gated-like-code checklist
8. **install** — the quickstart command sequence
9. **footer**
