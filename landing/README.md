# landing

A static, dependency-free landing page for trie. Presents the tool the
way the README does: two indexes (meaning + intent) that live in the
repo as plain Markdown, kept fresh by `trie sync` and kept honest by
the pre-commit gate — no external product or service involved.

## Running

```bash
open landing/index.html
```

No build step. No package manager. Three files:

- `index.html` — structure and copy
- `style.css` — all styling; dark default, light theme via
  `[data-theme=light]`
- `story.js` — theme toggle, copy-to-clipboard on the install command,
  and a subtle reveal-on-scroll

## Structure

1. **nav** — sticky, anchors to each section, GitHub link, theme toggle
2. **hero** — one-line value prop, install command with copy button,
   "no services" fact strip
3. **the problem** — a short lede: docs rot, commit messages describe
   diffs not decisions
4. **two indexes** — meaning (`triefacts/`) and intent
   (`triefacts/triediffs/`) side by side, each with a real file excerpt
5. **the loop** — five numbered steps: edit → record intent → gate →
   digest ships with the commit → `trie sync` keeps prose fresh; the
   payoff is `trie read <symbol> --history`
6. **in your repo** — repo tree figure + checklist: versioned, reviewed,
   merged, and gated like code; readable with nothing installed
7. **agents** — the read-side tools (`grep`/`read`/`trace`) and the
   write-side gate; notes that trie is built with itself
8. **install** — the quickstart command sequence
9. **footer**

## Accessibility

- All animation honours `prefers-reduced-motion`.
- The theme respects `prefers-color-scheme` on first visit and persists
  the user's explicit choice in `localStorage`.
