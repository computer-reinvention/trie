# trie

A documentation tree that mirrors your source tree, kept honest by a reference-graph cascade and gated by a pre-commit invariant. trie turns your codebase into a living self-description — prose at every node, graph between them — that humans can read at a glance and agents can reason over instead of reading code.

## Status

Pre-alpha. v0.1 in active development. Not ready for general use.

## The idea

Coding agents today read **code**. Code is the executable form of intent, not the explanatory form — every read is the agent re-deriving "what does this do" from syntax, under context pressure, with the wrong abstraction. That's where hallucinations come from. Not a lack of intelligence; the wrong artifact.

The human side has the mirror problem. Reviewing an agent's pass means reading a diff — syntax-level change with no semantic context. To know what a change _means_ you must already hold the system in your head. Which is exactly the population that needs agents the least. That's the adoption gap among hardcore devs.

trie's bet: **the codebase should describe itself in prose, and that description should be the surface both humans and agents work against.**

```
src/auth/middleware.py   ────  source, executable form
         ▲
         │  trie keeps these in sync,
         ▼  cascade-aware, sentinel-preserving
triefacts/src/auth/middleware.md  ────  prose, explanatory form
   ├─ § require_auth          (what it does, why, invariants)
   ├─ § extract_token
   └─ § <hand-written notes>  (preserved verbatim across regeneration)
```

A **triefact** (`trie` + `artifact`) is the per-file prose description above — one Markdown file mirroring one source file, with a paragraph per public symbol. The whole tree of them lives under `triefacts/`. Hand-written prose between `<!-- trie:section -->` sentinels is preserved across regeneration — no agent ever overwrites human judgment. And the same reference graph the code has is made first-class: edges between symbols, traversable by humans and agents alike. # comment: adoption hurdle shall be opptional and not necessary for most common use cases, only niche topics where the system lacks domain knowledge

## What a pass looks like

The artifact a human reviews changes. Agents don't hand you a code diff and ask you to reconstruct intent. They change the regions of your codebase's self-description that are now different — and you read your system, with the touched parts highlighted. # comment: it should look and feel like obsidian's graph view + claude code's legitimate well loved child

```
your repo, after one agent pass:

triefacts/
├── src/
│   ├── auth/
│   │   ├── middleware.md   [*]  edited this pass
│   │   ├── session.md      [~]  cascade — caller of middleware
│   │   └── token.md        [~]  cascade — caller of session
│   ├── api/
│   │   └── handler.md      [ ]
│   └── parse/
│       └── config.md       [ ]

  [*] direct change   [~] cascade-affected   [ ] untouched
```

A change that lights up three nodes in one module looks completely different from one that fans across the graph. You see scope before reading a line. You see whether the agent's change reaches further than it should. **Ramifications aren't computed — they are the lit region.**

The reviewer no longer needs to hold the system in their head, because the artifact they're reviewing _is_ the system, kept current by construction. A senior dev who has never seen the repo can look at a pass and ask the right question — "why did editing the config loader reach into auth?" — without prior context.

A proposed change becomes a proposed paragraph. If the paragraph is wrong, the human edits the _paragraph_, and the code conforms to it. Spec and implementation invert: prose becomes the source of truth, code becomes its executable form.

## How agents read it

When an agent answers a question or plans a change, it doesn't grep code and reconstruct intent. It walks the graph and joins paragraphs.

```
question: "what happens when an unauthenticated request hits /admin?"

  ├── find_symbol("admin")
  │     → api.handler:admin_route
  │
  ├── get_triefact("src/api/handler.md") § admin_route
  │     "Routes admin endpoints. Wrapped by require_auth before any
  │      handler body runs. Returns 401 if auth fails…"
  │
  ├── references_from("api.handler:admin_route")
  │     → auth.middleware:require_auth
  │
  ├── get_triefact("src/auth/middleware.md") § require_auth
  │     "Validates the session cookie via session.validate(). On any
  │      ValidationError, raises HTTPUnauthorized — never returns None…"
  │
  └── get_triefact("src/auth/session.md") § validate
        "Loads the session record, checks expiry, rotates the refresh
         token if within 5 minutes of expiry…"

  → a coherent narrative, in your team's words, that explains the flow.
```

Tokens carry meaning instead of boilerplate. Invariants and _why_ travel with the node, written into the human sentinel sections. The agent reasons over the right abstraction — narrative — instead of inferring narrative from syntax under pressure.

And it compounds. Every agent pass extends the description. The next pass starts from the current self-model of the system, not from re-reading code cold. The codebase accumulates a coherent story that every agent shares and every human ratifies, with the human-edited sentinel sections as ground truth that no regeneration overwrites.

Where meaning is written, the agent reads it. Where meaning isn't written, the _absence is visible_ — a node with no prose is a thing the system doesn't yet understand about itself, which is honest. That's completely different from today, where agents confidently fabricate because syntax doesn't tell them what they don't know.

## The cascade — what keeps it honest

A self-describing codebase only works if the description stays true. The naive "triefact per file" approach rots the moment you refactor — one edit invalidates triefacts in places you didn't touch, nobody notices, drift compounds, triefacts become lies, everyone stops trusting them.

trie's cascade is the load-bearing wall against that. When a symbol changes, the reference graph determines which _other_ triefact files also need regenerating — not just the triefact for the file you edited.

```
edit slugify() in src/slugify.py
         │
         ▼
graph query: who references slugify?
         │
         ├─ src/posts.py:make_url      → triefacts/src/posts.md must regen
         ├─ src/feeds.py:item_url      → triefacts/src/feeds.md must regen
         └─ utils.py:_canonicalize     → hub symbol (>20 inbound), capped

regen plan:
  triefacts/src/slugify.md   (the change itself)
  triefacts/src/posts.md     (cascade)
  triefacts/src/feeds.md     (cascade)
```

A pre-commit gate (`trie check`) refuses to merge when fingerprints don't match. Drift is a build break, not a TODO. The check is fast and offline — it compares fingerprints embedded in the triefact files' section sentinels against fingerprints derived from the current source, no LLM involved.

The hub-symbol cap matters: a `utils.py` referenced everywhere can't invalidate the world on every edit. trie skips cascade through symbols with more than ~20 inbound references by default, configurable per project.

## Quick start

```bash
uv pip install -e /path/to/trie  # or `pipx install ./trie` once published

cd /path/to/your/project
trie init

# generate triefacts for one file
trie sync --file src/some_module.py

# bootstrap the whole project (capped by budget or file count)
trie scan
trie sync --bootstrap --dry-run        # preview the plan + cost
trie sync --bootstrap --limit 10        # generate triefacts for the top 10 files
trie sync --bootstrap --budget 5.00     # spend at most $5

# verify coherence (fast, no API calls — designed for pre-commit)
trie check

# preview what `sync` would change (makes API calls; honors --budget/--limit)
trie diff
```

## Golden example

Source file (`src/slugify.py`):

```python
"""Pure-function library."""

import re

_NON_WORD = re.compile(r"\W+")


def slugify(text: str, max_len: int = 60) -> str:
    """Lowercase, strip non-word chars, collapse whitespace, truncate to max_len."""
    cleaned = _NON_WORD.sub("-", text.lower()).strip("-")
    return cleaned[:max_len]
```

After `trie sync --file src/slugify.py`, `triefacts/src/slugify.md`:

```markdown
---
trie_version: 0.1.0
source: src/slugify.py
file_fingerprint: 9d4f374adc9a843c…
---

<!-- trie:section symbol=src/slugify:slugify fingerprint=693808c2… -->

## `slugify(text: str, max_len: int = 60) -> str`

Generates a URL-safe slug from arbitrary text. Lowercases the input, replaces
runs of non-word characters with single hyphens, trims leading/trailing
hyphens, and truncates to `max_len` characters.

- **`text`**: The string to slugify.
- **`max_len`**: Maximum character count of the returned slug; defaults to 60.
- **Returns**: The slugified string, no longer than `max_len`.
<!-- trie:end -->
```

Now suppose another file imports it:

```python
# src/posts.py
from slugify import slugify

def make_url(title: str) -> str:
    return "/posts/" + slugify(title)
```

Edit `slugify`'s body — say, change the regex to also handle Unicode — and run `trie sync`. The cascade pulls in `triefacts/src/posts.md` automatically because `posts:make_url` references `slugify:slugify`. Both triefacts regenerate to stay coherent.

## How it works (anatomy of a trie triefact)

A trie-managed Markdown triefact looks like this:

```markdown
---
trie_version: 0.1.0
source: src/foo.py
file_fingerprint: 0830b9bb…
---

<!-- trie:section symbol=src/foo:bar fingerprint=1d10d565… -->

## `bar(s: str) -> str`

Generated description.

<!-- trie:end -->

## Hand-written notes

This prose lives between sentinels and is preserved across regeneration.

<!-- trie:section symbol=src/foo:baz fingerprint=f351c011… -->

## `baz()`

…

<!-- trie:end -->
```

- The fingerprint is a SHA-256 of the symbol's body with whitespace and comments normalized away — formatting churn doesn't trip staleness, but real changes do.
- `trie sync` regenerates only the sections whose fingerprint has drifted; everything between sentinels is preserved byte-for-byte.
- `trie check` compares stored fingerprints to current source — fast, deterministic, no LLM in the loop.

## Pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pankajgarkoti/trie
    rev: v0.1.0
    hooks:
      - id: trie-check
```

Or use a local hook if you'd rather pin trie via your own venv:

```yaml
repos:
  - repo: local
    hooks:
      - id: trie-check
        name: trie check
        entry: trie check --quiet
        language: system
        pass_filenames: false
        always_run: true
```

`trie check` exits non-zero if any source file's symbol doesn't match its documented section. Failures point at the specific symbol, so you know exactly what regenerated and why.

## Agent integration (MCP)

trie ships an MCP server so coding agents read your codebase's prose self-description as a separate, durable context layer — not chat memory, not retrieved chunks, but a structured tree they can navigate. Four tools, exposed over stdio:

| Tool                              | What it returns                                 |
| --------------------------------- | ----------------------------------------------- |
| `get_triefact(source_path)`            | Markdown triefact for a source file             |
| `find_symbol(name)`               | Substring search over symbol names + signatures |
| `references_to(qualified_name)`   | Symbols that reference the given one (callers)  |
| `references_from(qualified_name)` | Symbols the given one references (callees)      |

For Claude Code, add to your `~/.claude/mcp_servers.json` (or per-project `.mcp.json`):

```json
{
  "trie": {
    "command": "trie",
    "args": ["mcp"],
    "cwd": "/path/to/your/project"
  }
}
```

The server is read-only. Agents can query the graph and join paragraphs; only `trie sync` (run by you, in your shell) modifies the triefact tree. Humans gate writes. Agents read freely.

## Reducing PR noise from generated triefacts

Generated Markdown can drown human review in PR diffs. On GitHub, mark the triefact tree as `linguist-generated` so the diff is collapsed by default:

```
# .gitattributes
triefacts/** linguist-generated=true
```

Hand-written prose between sentinels is still indexed by GitHub's search; only the side-by-side diff renders are collapsed.

## Roadmap

- **M1** ✓ — `trie sync --file <path>` with section-sentinel writer
- **M2** ✓ — `trie scan`, `trie sync --bootstrap` with budget/limit and dry-run
- **M3** ✓ — `trie check`, `trie diff`, pre-commit hook
- **M4** ✓ — heuristic cascade (tree-sitter imports + same-module name matching) _(the wedge)_
- **M5** ✓ — MCP server (`trie mcp`) with `get_triefact`, `find_symbol`, `references_to/from`
- **M6** ✓ — README golden example, packaging, `trie plan` alias, `.gitattributes` recipe
- **v0.2** — SCIP precision (replace tree-sitter heuristic with `scip-python` for type-aware references), TypeScript support, vector-over-triefacts retrieval, `trie watch` daemon, rename detection in reconcile

## License

MIT — see [LICENSE](./LICENSE).
