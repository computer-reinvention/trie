# trie

A documentation tree that mirrors your source tree — kept coherent with the code by an LSP/SCIP-aware cascade and a pre-commit invariant. Exposed to coding agents (Claude Code, Codex, etc.) via MCP as a persistent, shared, versioned context layer.

## Status

Pre-alpha. v0.1 in active development. Not ready for general use.

## The wedge

When you edit a symbol, trie's reference graph determines which *other* doc files also need regenerating — not just the doc for the file you edited. That cascade, plus a pre-commit check that the doc tree is coherent at every commit, is what trie does that nothing else does.

## Quick start

```bash
# Install (editable, in your project's venv)
uv pip install -e /path/to/trie  # or `pipx install ./trie` once published

# Initialise in a Python project
cd /path/to/your/project
trie init

# Generate docs for one file
trie sync --file src/some_module.py

# Bootstrap the whole project (capped by budget or file count)
trie scan
trie sync --bootstrap --dry-run        # preview the plan + cost
trie sync --bootstrap --limit 10        # generate docs for the top 10 files
trie sync --bootstrap --budget 5.00     # spend at most $5

# Verify coherence (fast, no API calls — designed for pre-commit)
trie check

# Preview what `sync` would change (makes API calls; honors --budget/--limit)
trie diff
```

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

`trie check` is fast and offline — it compares fingerprints embedded in your doc files' section sentinels against fingerprints derived from the current source. It exits non-zero if any source file's symbol doesn't match its documented section.

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

After `trie sync --file src/slugify.py`, `docs/src/slugify.md`:

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

Edit `slugify`'s body — say, change the regex to also handle Unicode — and run `trie sync`. The cascade pulls in `docs/src/posts.md` automatically because `posts:make_url` references `slugify:slugify`. Both docs regenerate to stay coherent.

## How it works

A trie-managed Markdown doc looks like this:

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

## Agent integration (MCP)

Trie ships an MCP server so coding agents can consult the doc tree as a separate context layer from their own conversation memory. Run-time and exposed tools:

| Tool | What it returns |
|---|---|
| `get_doc(source_path)` | Markdown doc for a source file |
| `find_symbol(name)` | Substring search over symbol names + signatures |
| `references_to(qualified_name)` | Symbols that reference the given one (callers) |
| `references_from(qualified_name)` | Symbols the given one references (callees) |

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

The server is read-only. Agents can query the graph; only `trie sync` (run by you, in your shell) modifies the doc tree.

## Reducing PR noise from generated docs

Generated Markdown can drown human review in PR diffs. On GitHub, mark the doc tree as `linguist-generated` so the diff is collapsed by default:

```
# .gitattributes
docs/** linguist-generated=true
```

Hand-written prose between sentinels is still indexed by GitHub's search; only the side-by-side diff renders is collapsed.

## Roadmap

- **M1** ✓ — `trie sync --file <path>` with section-sentinel writer
- **M2** ✓ — `trie scan`, `trie sync --bootstrap` with budget/limit and dry-run
- **M3** ✓ — `trie check`, `trie diff`, pre-commit hook
- **M4** ✓ — heuristic cascade (tree-sitter imports + same-module name matching) *(the wedge)*
- **M5** ✓ — MCP server (`trie mcp`) with `get_doc`, `find_symbol`, `references_to/from`
- **M6** — polish, README golden example, packaging
- **v0.2** — SCIP precision (replace tree-sitter heuristic with `scip-python` for type-aware references), TypeScript support, vector-over-docs retrieval, watch mode

## License

MIT — see [LICENSE](./LICENSE).
