# trie quickstart

Run trie on a project in five minutes. (The [README](README.md) is the
full reference; this is the short path.)

## 1. Install

```bash
uv tool install git+https://github.com/computer-reinvention/trie
trie --version
```

Prerequisites: Python 3.11+, [`uv`](https://docs.astral.sh/uv/), and
[ripgrep](https://github.com/BurntSushi/ripgrep) (`rg`) on PATH.

`trie sync` and the digest narrative make Anthropic API calls, so you'll
need `ANTHROPIC_API_KEY` in your environment. Everything else — the
gates, the graph, the query commands — runs entirely offline.

## 2. Initialise in your project

```bash
cd ~/code/your-project
trie init
```

`init` writes `trie.toml`, adds `.trie/` to `.gitignore`, builds the
symbol graph, and (interactively) offers to install the pre-commit hook.
Pass `--install-hooks` / `--no-install-hooks` to skip the prompt.

Open `trie.toml` and tighten `[scope]` if you only want trie pointed at
part of the tree:

```toml
[scope]
include = ["src/**/*.py"]
exclude = ["**/tests/**", "**/__pycache__/**"]
```

Languages indexed today: Python and TypeScript/TSX.

## 3. Preview the bill

```bash
trie plan             # ranked worklist + cost estimate (free token-count calls)
trie plan --offline   # worklist only: no key, no network
```

`plan` ranks files by `LOC × public_symbol_count`. The estimate accounts
for prompt caching, so the real bootstrap usually comes in under it.

## 4. Generate triefacts

```bash
trie sync --file src/some_module.py   # one file, cheapest first taste
trie sync --limit 20                  # top 20 ranked files
trie sync --budget 5.00               # spend at most $5
trie sync                             # the full plan / incremental after that
```

Generated triefacts land under `triefacts/<source path>.md`. Hand-written
prose *between* trie's section sentinels survives regeneration — go ahead
and add narrative.

Two flavours of preview before committing:

```bash
trie sync --dry-run   # regenerate to .trie/preview/, print unified diffs
trie verify           # offline drift check, exits 1 on drift, no LLM
```

## 5. The commit loop

If you let `trie init` install the hook, every commit now passes through
`trie gate`:

```
git commit  →  trie gate
                 ├─ lock-check    blocks if a trie writer is mid-flight       (offline)
                 ├─ verify        blocks if prose drifted from source         (offline)
                 ├─ intent        blocks if a changed symbol has no note      (offline)
                 └─ diff --write  writes + stages the commit's digest
```

Record intent as you work — one note per changed symbol:

```bash
trie patch create src/auth:require_auth -n "expired tokens must 401, not 500 (see #241)"
trie patch apply -N "harden session expiry"
```

Fix a `verify` failure with `trie sync`. Fix an `intent` failure by
recording the note it asks for — the error output is copy-pasteable
commands.

## 6. Plug into your agent (optional)

```bash
trie setup            # auto-detects opencode / claude-code / cursor / ...
```

`setup` installs the end-of-turn refresh hook, overrides the agent's
built-in `grep`/`read` with trie-backed versions, adds `trace` and the
explain/history tools, and writes `TRIE.md` (the usage contract). MCP
registration is opt-in via `--with-mcp`.

## 7. Query the indexes

```bash
trie grep --name require_auth
trie read src/auth/middleware:require_auth            # meaning
trie read src/auth/middleware:require_auth --history  # + intent trail
trie trace src/graph/store:Store.replace_all_edges --direction callers
```

That's the loop: `init → plan → sync → commit`. Everything else is
variations.

## Troubleshooting

- **`trie verify` reports `tampered_body`**: someone (you, an editor
  plugin, an agent) edited inside a `<!-- trie:section -->` /
  `<!-- trie:end -->` block. Re-run `trie sync` to regenerate, or revert
  the edit. Hand-written prose belongs *between* sections.
- **`trie sync` exits 2**: it collided with an in-flight refresh (the
  turn hook doing its job). Let the hook finish and retry.
- **The intent gate flags a symbol you didn't meaningfully change**: the
  gate compares normalized bodies, so the body really changed. Record a
  short note — "extracted helper, no behaviour change" is a valid intent.
- **PR diffs are noisy**: add `triefacts/** linguist-generated=true` to
  `.gitattributes` — GitHub will collapse the triefact tree by default.
- **The cascade missed a connection**: reference detection is
  tree-sitter + import based. It catches `from foo import bar` and
  same-module matches but can miss dynamic dispatch. SCIP/type-aware
  precision is on the roadmap.
