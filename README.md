# trie

> **Your codebase, in prose. Kept in sync with the code by a reference-graph cascade.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: pre-alpha](https://img.shields.io/badge/status-pre--alpha-orange.svg)](#status)
[![Tests](https://img.shields.io/badge/tests-267%20passing-brightgreen.svg)](#)

trie generates a Markdown description of every source file in your project. The descriptions live in a tree that mirrors your source tree, joined by the same reference graph the code has. Edit a function and the cascade regenerates the descriptions of every caller too. Humans review English prose; agents read the same prose instead of grepping code under context pressure.

```
src/auth/middleware.py   ────►  triefacts/src/auth/middleware.md
                                  ├─ § require_auth          (what it does, why, invariants)
                                  ├─ § extract_token
                                  └─ § <hand-written notes>  (preserved across regen)
```

A pre-commit gate (`trie verify`) refuses to merge when the tree drifts. The check is bidirectional — it catches both source changes that haven't propagated into triefacts and tampering with triefact bodies. An MCP server (`trie mcp serve`, registered into your agent via `trie mcp install`) exposes the tree to coding agents — Claude Code, Cursor, Codex, etc. — as a persistent, structured context layer.

> **Status:** pre-alpha · v0.1 in active development · not ready for general use.

---

## The idea

Coding agents today read **code**. Code is the executable form of intent, not the explanatory form — every read is the agent re-deriving "what does this do" from syntax, under context pressure, with the wrong abstraction. That's where hallucinations come from. Not a lack of intelligence; the wrong artifact.

The human side has the mirror problem. Reviewing an agent's pass means reading a diff — syntax-level change with no semantic context. To know what a change _means_ you must already hold the system in your head. Which is exactly the population that needs agents the least. That's the adoption gap among hardcore devs.

trie's claim: **the codebase should describe itself in prose, and that description should be the surface both humans and agents work against.**

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

A **triefact** (`trie` + `artifact`) is the per-file prose description above — one Markdown file mirroring one source file, with a paragraph per public symbol. The whole tree of them lives under `triefacts/`. Hand-written prose between `<!-- trie:section -->` sentinels is preserved across regeneration — no agent ever overwrites human judgment. And the same reference graph the code has is made first-class: edges between symbols, traversable by humans and agents alike.

## What a pass looks like

The artifact a human reviews changes. Agents don't hand you a code diff and ask you to reconstruct intent. They change the regions of your codebase's self-description that are now different — and you read your system, with the touched parts highlighted.

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

  ├── locate({ name_contains: "admin", kind: "function" })
  │     → api.handler:admin_route   (one-liner: "Routes admin endpoints…")
  │
  ├── explain("api.handler:admin_route")
  │     prose: "Routes admin endpoints. Wrapped by require_auth before any
  │             handler body runs. Returns 401 if auth fails…"
  │     callees: [{ auth.middleware:require_auth, one_liner: "Validates the
  │             session cookie via session.validate()…" }]
  │
  └── explain("auth.middleware:require_auth")
        prose: "Validates the session cookie via session.validate(). On any
                ValidationError, raises HTTPUnauthorized — never returns None…"
        callees: [{ auth.session:validate, one_liner: "Loads the session
                record, checks expiry, rotates the refresh token…" }]

  → a coherent narrative, in your team's words, that explains the flow,
    assembled in 3 round-trips instead of 5+.
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

A pre-commit gate (`trie verify`) refuses to merge when fingerprints don't match. Drift is a build break, not a TODO. The check is fast and offline — every section sentinel carries two SHA-256 hashes (over the source symbol and over the triefact body) so drift is detected in both directions: source changes that haven't been regenerated, and triefact bodies that were edited or corrupted between sentinels. No LLM in the loop.

The hub-symbol cap matters: a `utils.py` referenced everywhere can't invalidate the world on every edit. trie skips cascade through symbols with more than ~20 inbound references by default, configurable per project.

## Quick start

```bash
# 1. Install (pick one)
uv tool install git+ssh://git@github.com/pankajgarkoti/trie    # persistent, on $PATH
uvx --from git+ssh://git@github.com/pankajgarkoti/trie trie    # ephemeral, run-anywhere

# 2. Initialise your project
cd /path/to/your/project
export ANTHROPIC_API_KEY=...             # default model is anthropic/claude-sonnet-4-6
trie init                                # writes trie.toml, scans, prompts for pre-commit hook

# 3. Smoke test the LLM path on a single file
trie sync --file src/some_module.py

# 4. Preview the bootstrap plan + cost (free count_tokens calls, no generation)
trie plan

# 5. Bootstrap with a guardrail — auto-detected on first run
trie sync --limit 10                     # top-ranked 10 files
trie sync --budget 5.00                  # OR spend at most $5
trie sync                                # OR commit to the full plan

# 6. Day-to-day: incremental cascade
trie sync                                # re-syncs stale + cascade
trie sync --dry-run                      # preview unified diffs (makes API calls)

# 7. Drift gate — fast, offline, pre-commit-friendly
trie verify

# 8. Wire up your agent
trie mcp install                         # auto-detects installed agents
```

### Recommended workflow

- **First run:** `trie init` → `trie plan` (see the bill) → `trie sync --limit 10` (sample
  the quality) → review one or two triefacts → `trie sync` to complete the bootstrap.
- **After every code change:** `trie sync` regenerates exactly the stale sections plus
  their cascade. Run it before opening a PR so reviewers see the prose change too.
- **In CI / pre-commit:** `trie verify` only — it's deterministic, offline, and
  exits non-zero on drift. Never let CI call the LLM path.
- **For agents:** `trie mcp install` once, then forget about it. The MCP server is
  read-only; agents query the graph, you own writes via `trie sync`.

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
last_synced_at: '2026-05-08T14:21:09Z'
description: Pure-function library.
defines:
  - kind: function
    qualified_name: src/slugify:slugify
    lines: 6-9
incoming_refs: 1
outgoing_refs: 0
---

<!-- trie:section symbol=src/slugify:slugify fingerprint=693808c2… body_fp=4f1c2d8e… -->

## `slugify(text: str, max_len: int = 60) -> str`

Lowercase, replace non-word runs with hyphens, strip leading/trailing hyphens, truncate to `max_len`.

- `max_len`: clamp on the returned length; defaults to 60.
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
last_synced_at: '2026-05-08T14:21:09Z'
description: One-line summary lifted from the module docstring.
defines:
  - kind: function
    qualified_name: src/foo:bar
    lines: 5-12
  - kind: function
    qualified_name: src/foo:baz
    lines: 15-22
incoming_refs: 4
outgoing_refs: 2
---

<!-- trie:section symbol=src/foo:bar fingerprint=1d10d565… body_fp=4f1c2d8e… -->

## `bar(s: str) -> str`

Generated description.

<!-- trie:end -->

## Hand-written notes

This prose lives between sentinels and is preserved across regeneration.

<!-- trie:section symbol=src/foo:baz fingerprint=f351c011… body_fp=8c9b3a44… -->

## `baz()`

…

<!-- trie:end -->
```

- The `fingerprint=` field is a SHA-256 of the symbol's body with whitespace and comments normalized away — formatting churn doesn't trip staleness, but real changes do.
- The `body_fp=` field is a SHA-256 of the section body itself, so the check catches manual tampering with the Markdown between sentinels.
- The front-matter `defines` list, ref counts, and description are agent-navigation metadata: they let an agent decide whether to open a triefact at all without parsing every section.
- `trie sync` regenerates only the sections whose source fingerprint has drifted; everything between sentinels is preserved byte-for-byte.
- `trie verify` compares stored fingerprints — fast, deterministic, no LLM in the loop, exits non-zero on drift.

## Pre-commit hook

Add to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pankajgarkoti/trie
    rev: v0.1.0
    hooks:
      - id: trie-verify
```

Or use a local hook if you'd rather pin trie via your own venv:

```yaml
repos:
  - repo: local
    hooks:
      - id: trie-verify
        name: trie verify
        entry: trie -q verify
        language: system
        pass_filenames: false
        always_run: true
```

`trie verify` exits non-zero on any of: a source symbol whose fingerprint no longer matches its section, a public symbol with no section, a section whose body was edited between sentinels (`tampered_body`), a section pointing at a deleted symbol (`orphan`), or a missing triefact file. Failures point at the specific symbol, so you know exactly what regenerated and why.

## Agent integration (MCP)

trie ships an MCP server so coding agents read your codebase's prose self-description as a separate, durable context layer — not chat memory, not retrieved chunks, but a structured tree they can navigate. Three verbs, exposed over stdio, that match how agents reason about a codebase: _find it_, _understand it_, _trace it_.

| Tool                                          | What it returns                                                                       |
| --------------------------------------------- | ------------------------------------------------------------------------------------- |
| `locate(predicate, rank_by?, limit=10)`       | Symbols matching a predicate (name, kind, scope, edge counts), with a one-line summary on each hit so the agent can pick without re-reading |
| `explain(qname)`                              | A symbol's prose plus one-liners for every immediate caller and callee                |
| `walk(from_qname, direction, depth=2)`        | Topology beyond one hop — signatures + one-liners across a depth-bounded graph slice  |

Every response carries `one_liner` fields pulled from the section body at sync time, so an agent walking the graph never has to open a triefact just to decide whether to open it. Errors return `{error: {code, message, suggestion?}}` — fuzzy-matched suggestions on `not_found` mean recovery is one round-trip, not three. The full contract lives in [`docs/agent_interface.md`](docs/agent_interface.md).

Register trie with your agent in one command:

```bash
trie mcp install --target claude-code     # writes <project>/.mcp.json
trie mcp install --target cursor          # writes <project>/.cursor/mcp.json
trie mcp install --all --print-only       # preview snippets for every supported target
```

Supported targets: `claude-code`, `claude-desktop`, `cursor`, `windsurf`, `vscode`, `codex`. Without a `--target`, the installer auto-detects which agents are present.

The snippet `install` writes is the standard MCP server form:

```json
{
  "mcpServers": {
    "trie": {
      "command": "trie",
      "args": ["mcp", "serve"],
      "cwd": "/path/to/your/project"
    }
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
- **M2** ✓ — symbol-graph scan, first-run bootstrap with budget/limit
- **M3** ✓ — drift check (`trie verify`), preview (`trie sync --dry-run`), pre-commit hook
- **M4** ✓ — heuristic cascade (tree-sitter imports + same-module name matching) _(the wedge)_
- **M5** ✓ — MCP server (`trie mcp serve`) with three verbs: `locate`, `explain`, `walk`
- **M6** ✓ — README golden example, packaging, `trie plan`, `.gitattributes` recipe
- **M7** ✓ — CLI redesign: auto-detect bootstrap, streaming progress + ETA, three-level verbosity, `trie mcp install` for six agents/IDEs
- **v0.2** — SCIP precision (replace tree-sitter heuristic with `scip-python` for type-aware references), TypeScript support, vector-over-triefacts retrieval, `trie watch` daemon, rename detection in reconcile

## License

MIT — see [LICENSE](./LICENSE).
