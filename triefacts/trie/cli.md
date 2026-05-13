---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: f3b5d5585e2d7a9dfc63ffb8756984e551aec83dea4a7f665571e96901d01bbb
last_synced_at: '2026-05-12T18:21:35Z'
defines:
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 144-227
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 249-336
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 340-352
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 493-576
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 806-809
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 826-895
incoming_refs: 0
outgoing_refs: 52
---
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=b4f1d7bff0bc8e455ed6de5c56b9e0c884e01c1dc12eba107d91abe90e5b8584 body_fp=b963f585747f421bd661fc632e2dba55e142a52c54b05da3dfca446eec1c9e26 -->
## `init_cmd(ctx, root, force, install_hooks, run_scan) -> None`

Initialize a project by writing `trie.toml`, updating `.gitignore`, optionally scanning, and optionally installing a pre-commit hook.

- `root`: project directory to initialise; defaults to `cwd`.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: prompts interactively when `None` and stdin is a tty; skips in CI.
- `run_scan`: builds the symbol graph immediately after writing config.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=b443a8e75a4561a3b46ece5f8fb678fe766e19a1565481ad16a80636b87de2dd body_fp=a2d0cb0aa09bcf825ef56a5ab591f929e43dfff4c8e00e2188daf790280abe1f -->
## `plan_cmd(ctx: typer.Context, model: str | None, all_: bool) -> None`

Scan the project, compute a token-counted cost estimate, and print the worklist without writing any triefacts.

- `model`: overrides `config.models.bootstrap` for pricing and token counting.
- `all_`: forces full re-bootstrap cost view even when triefacts already exist.
- Exits 0 silently when the incremental worklist is empty (tree is coherent).
- Never calls `messages.create`; uses only the free `count_tokens` endpoint.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=c350c8c3b9c49583daf708215684050327bac351ba89c27ce1d376c8a899d3bb -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline drift check and exit with code 1 if any triefact has drifted from its source.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=fa4a984982fd7da361719c731982521093b761228ce0fd0ec1aa0d24ea193753 body_fp=fe08b5940c711f4fbf975bb1b698e86b247cdd6978f14d3a9b98c85141e0a6df -->
## `sync_cmd(ctx, file, all_, budget, limit, dry_run, model) -> None`

Generate or refresh triefacts, auto-detecting single-file, dry-run, full-bootstrap, or incremental mode.

- `file`: sync exactly one source file; mutually exclusive with `--all`.
- `all_`: force full re-pass even when triefacts already exist.
- `budget`: USD cap; stops once cumulative actual cost reaches this value.
- `limit`: maximum number of files to sync.
- `dry_run`: write previews to `.trie/preview/` and print unified diffs instead of updating live triefacts.
- `model`: overrides the configured model slug.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=f6e87043d32e3a9bfe993957da9934d895d20a0eb666bd42b4cde01b9eab51bd body_fp=44b13857dffcc59e097f9d84af4dd184133aaf792c58dda3cffcd288bd1e3f8c -->
## `mcp_serve() -> None`

Start the stdio MCP server; hidden from help output as agents invoke it directly via installed snippets.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=6cadb8899604334fd8d39cb34dea994f2fe75a0e40ec1e21e86727b39c2ebd5f -->
## `mcp_install_cmd(ctx, target, install_all, scope, print_only, dry_run)`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

- `target`: repeat `--target` to install for multiple named agents; mutually exclusive with `--all`.
- `install_all`: skips per-target detection, installs for every known target.
- `scope`: `'project'` writes into the current project; `'user'` writes to `~/.<agent>/...`.
- `print_only`: prints the snippet that would be merged without writing files.
- `dry_run`: resolves file paths and shows changes without writing.
- Exits 1 if any per-target result has `action == "error"`.
<!-- trie:end -->