# landing

A static, dependency-free scroll-down story comparing two code searches:
the same question answered with `grep`/`bash`/`read` (11 calls) versus
with trie's MCP tools (3 calls).

## Running

```bash
open landing/index.html
```

No build step. No package manager. Three files:

- `index.html` — structure and copy
- `style.css` — all styling, including the 3-column race grid and the
  animated divider
- `story.js` — scroll-triggered reveals, progress bar, chapter marker,
  count-up numbers

## Structure

The page is a sequence of full-viewport scenes:

1. **hero** — title and scroll cue
2. **the question** — three possible outcomes for stale symbols
3. **two paths** — `11` vs `3` count-up
4. **the race** — the heart of the page. A 3-column grid (slow lane |
   animated divider | fast lane). Each row is one "beat" of the slow
   agent; rows 1–3 carry real trie calls on the right, rows 4–11 carry
   "waiting" placeholders so the empty space on the trie side becomes
   the story.
5. **the reveal** — answer + scoreboard + `3.6×` ratio
6. **why it works** — four cards on what makes trie's tools different
7. **the loop** — the bootstrapping diagram
8. **outro** — back-to-top

## Accessibility

- All animation honours `prefers-reduced-motion`.
- Layout collapses to a single column below 900px; the divider hides
  on mobile and the lanes stack.
- Color isn't the only signal — every red/green cue is paired with a
  text label (`without trie`, `with trie`, `+1`, `precise`, etc.).
