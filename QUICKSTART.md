# trie quickstart

Run trie on a Python project in five minutes.

## 1. Install

```bash
git clone https://github.com/pankajgarkoti/trie /tmp/trie
cd /tmp/trie && uv build
uv tool install --force ./dist/trie-0.1.0-py3-none-any.whl
trie --version   # → trie 0.1.0
```

`sync` and `diff` make Anthropic API calls, so you'll need `ANTHROPIC_API_KEY` in your environment. The other commands (`init`, `scan`, `plan`, `check`, `mcp`) run entirely locally — no API calls - trie refers to such operations as "free" operations.

## 2. Initialise in your project

```bash
cd ~/code/your-python-project
trie init
```

This drops a `trie.toml` in the project root and adds `.trie/` to `.gitignore`. Open `trie.toml` and tighten `[scope]` if you only want trie pointed at a subdirectory:

```toml
[scope]
include = ["src/**/*.py"]
exclude = ["**/tests/**", "**/__pycache__/**"]
```

## 3. Preview the bill

```bash
trie scan       # build the symbol graph (no API calls)
trie plan       # show ranked worklist + cost estimate
```

`plan` ranks files by `LOC × public_symbol_count`. The cost estimate accounts for prompt caching, so a real bootstrap usually comes in under the estimate.

## 4. Generate docs

Three modes, pick one:

```bash
# Just one file (cheapest, good for a first taste)
trie sync --file src/some_module.py

# Bootstrap the whole project, capped
trie sync --bootstrap --limit 20         # top 20 ranked files
trie sync --bootstrap --budget 5.00      # spend at most $5

# Incremental (after the first bootstrap)
trie sync                                 # re-syncs whatever's stale + cascades
```

Generated docs land under `docs/<source path>.md`. Hand-written prose between trie's section sentinels survives regeneration — go ahead and add narrative.

## 5. Lock the invariant with pre-commit

Add to your `.pre-commit-config.yaml`:

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

Then `pre-commit install`. Commits with stale docs will now fail until you re-run `trie sync`.

## 6. Plug into your agent (optional)

Add to `~/.claude/mcp_servers.json` (or `.mcp.json` per-project):

```json
{
  "trie": {
    "command": "trie",
    "args": ["mcp"],
    "cwd": "/absolute/path/to/your/project"
  }
}
```

Restart your agent. It can now call `get_doc`, `find_symbol`, `references_to`, and `references_from` over your project's symbol graph.

## Troubleshooting

- **`trie sync` re-runs the whole file even when only one symbol changed**: known v0.1 limitation. The cascade picks the right _files_; per-section regen within a file lands in v0.2.
- **The cascade missed a connection**: v0.1 uses tree-sitter + import detection, not SCIP. It catches `from foo import bar` and same-module name matches, but misses `import foo; foo.bar()` style and method dispatch. SCIP precision is v0.2.
- **PR diffs are noisy**: add `docs/** linguist-generated=true` to `.gitattributes` — GitHub will collapse the doc tree by default.
- **`trie check` fails after a manual hand-edit**: only edit _between_ `<!-- trie:section -->` and `<!-- trie:end -->` sentinels. Edits inside a section will be overwritten by the next `sync`.

That's the loop: `init → scan → plan → sync → check`. Everything else is variations.
