# trie quickstart

Run trie on a Python project in five minutes.

## 1. Install

```bash
git clone https://github.com/pankajgarkoti/trie /tmp/trie
cd /tmp/trie && uv build
uv tool install --force ./dist/trie-0.1.2-py3-none-any.whl
trie --version   # → trie 0.1.2
```

`trie sync` and `trie plan` make Anthropic API calls, so you'll need `ANTHROPIC_API_KEY` in your environment. Everything else (`init`, `verify`, `mcp install`, `mcp serve`) runs entirely offline.

## 2. Initialise in your project

```bash
cd ~/code/your-python-project
trie init
```

`init` drops a `trie.toml` in the project root, adds `.trie/` to `.gitignore`, builds the symbol graph, and (interactively) offers to install a pre-commit hook. Pass `--install-hooks` / `--no-install-hooks` to skip the prompt.

Open `trie.toml` and tighten `[scope]` if you only want trie pointed at a subdirectory:

```toml
[scope]
include = ["src/**/*.py"]
exclude = ["**/tests/**", "**/__pycache__/**"]
```

## 3. Preview the bill

```bash
trie plan       # scan the project + show ranked worklist with cost estimate
```

`plan` ranks files by `LOC × public_symbol_count`. The cost estimate accounts for prompt caching, so the real bootstrap usually comes in under the estimate. It uses Anthropic's free `count_tokens` endpoint — no `messages.create` calls.

## 4. Generate triefacts

Pick the mode that matches what you want:

```bash
# One file — cheapest, good for a first taste
trie sync --file src/some_module.py

# Bootstrap the whole project, capped
trie sync --limit 20         # top 20 ranked files
trie sync --budget 5.00      # spend at most $5

# Incremental refresh (after a first pass exists)
trie sync                    # re-syncs stale files + cascades to their callers

# Force a full re-pass even when triefacts already exist
trie sync --all --budget 5.00
```

`trie sync` auto-detects whether to bootstrap or run an incremental cascade. In a fresh project, it runs the bootstrap path; once `triefacts/` exists, it switches to the cascade. In MEDIUM verbosity (default) you'll see per-file progress with a running ETA.

Generated triefacts land under `triefacts/<source path>.md`. Hand-written prose between trie's section sentinels survives regeneration — go ahead and add narrative.

Two flavours of preview before committing:

```bash
trie sync --dry-run              # regenerate to .trie/preview/, print unified diffs
trie verify                      # offline drift check, exits 1 on drift, no LLM
```

Drift detection is bidirectional: `verify` catches both source changes that haven't been propagated into triefacts (Code → Triefact) and tampering with triefact bodies between sentinels (Triefact → Code).

Verbosity is global:

```bash
trie -q sync     # mute (errors only)
trie sync        # medium (per-file progress + ETA, default)
trie -v sync     # chatty (token / cache breakdown per file)
```

## 5. Lock the invariant with pre-commit

If you let `trie init` install the hook, you're done. Otherwise add to your `.pre-commit-config.yaml`:

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

Then `pre-commit install`. Commits with stale or tampered triefacts will now fail until you re-run `trie sync`.

## 6. Plug into your agent (optional)

```bash
trie mcp install --target claude-code        # registers in <project>/.mcp.json
trie mcp install --target cursor             # writes <project>/.cursor/mcp.json
trie mcp install --all --print-only          # preview snippets for every known target
trie mcp install --scope user --target claude-desktop   # write to ~/Library/.../Claude/...
```

Supported targets: `claude-code`, `claude-desktop`, `cursor`, `windsurf`, `vscode`, `codex`. Without a `--target`, the installer auto-detects which agents are present on your system.

Restart your agent. It can now call `get_triefact`, `find_symbol`, `references_to`, and `references_from` over your project's symbol graph.

## Troubleshooting

- **`trie sync` re-runs the whole file even when only one symbol changed**: known v0.1 limitation. The cascade picks the right _files_; per-section regen within a file lands in v0.2.
- **The cascade missed a connection**: v0.1 uses tree-sitter + import detection, not SCIP. It catches `from foo import bar` and same-module name matches, but misses `import foo; foo.bar()` style and method dispatch. SCIP precision is v0.2.
- **PR diffs are noisy**: add `triefacts/** linguist-generated=true` to `.gitattributes` — GitHub will collapse the triefact tree by default.
- **`trie verify` reports `tampered_body`**: someone (you, an editor plugin, an agent) edited inside a `<!-- trie:section -->` / `<!-- trie:end -->` block. Re-run `trie sync` to regenerate, or revert the edit.
- **`trie verify` reports `legacy_section`**: the section was written by trie ≤ 0.1 and has no body fingerprint to verify. Re-run `trie sync` once to migrate.
- **Edits inside a section sentinel get overwritten**: by design — those blocks are owned by the generator. Put hand-written prose _between_ sections (it's preserved verbatim across regen).

That's the loop: `init → plan → sync → verify`. Everything else is variations.
