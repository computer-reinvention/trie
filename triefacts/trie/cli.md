---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: f3b5d5585e2d7a9dfc63ffb8756984e551aec83dea4a7f665571e96901d01bbb
last_synced_at: '2026-05-14T17:18:45Z'
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
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=b4f1d7bff0bc8e455ed6de5c56b9e0c884e01c1dc12eba107d91abe90e5b8584 body_fp=23e3977b36e61df533c2203e1c2173587273d300ad7232e9a682755bc1aafd9d -->
## `init_cmd(ctx, root, force, install_hooks, run_scan) -> None`

Initialize a trie project: write `trie.toml`, update `.gitignore`, optionally scan, and install pre-commit hooks.

- `root`: project directory to initialize; defaults to `Path.cwd()`.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: tri-state; prompts interactively in a tty, defaults to `False` in CI.
- `run_scan`: builds the symbol graph immediately after writing config.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=b443a8e75a4561a3b46ece5f8fb678fe766e19a1565481ad16a80636b87de2dd body_fp=064333ff29b11de0ec40a8fdd8302aae9df9d10901c83118a164307997169129 -->
## `plan_cmd(ctx: typer.Context, model: str | None, all_: bool) -> None`

Scan the project, count tokens, and print a cost estimate without generating any triefacts.

- `model`: overrides the configured model used for token counting.
- `all_`: forces a full re-bootstrap cost view even when triefacts already exist.
- Runs an offline drift check first; warnings are shown but do not abort.
- Auto-selects incremental or full-bootstrap mode based on whether triefacts exist.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=7e53deb328e082791efe83f54f36b9744d8bae0789ffe2150787a6728327293b -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline drift check and exit 1 if any triefact has drifted from its source.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=fa4a984982fd7da361719c731982521093b761228ce0fd0ec1aa0d24ea193753 body_fp=974aa98e01e1cc04f6f1b8226810b3d7fcbdc8e2a250c95e3715ccc8fa9317a5 -->
## `sync_cmd(ctx, file, all_, budget, limit, dry_run, model) -> None`

Generate or refresh triefacts, auto-selecting single-file, dry-run, full-bootstrap, or incremental mode.

- `file`: sync exactly one source file; mutually exclusive with `--all`.
- `all_`: force full re-pass over every in-scope file.
- `budget`: USD cap; stops once cumulative actual cost reaches this value.
- `limit`: maximum number of files to sync.
- `dry_run`: write previews to `.trie/preview/` and print unified diffs without updating the live tree.
- `model`: overrides the configured model string.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=f6e87043d32e3a9bfe993957da9934d895d20a0eb666bd42b4cde01b9eab51bd body_fp=d5c2c343a5206cf5e9362d45093dc9e4cd7c9a09e7c9a1c83874226aec883557 -->
## `mcp_serve() -> None`

Hidden stdio MCP server entry point spawned directly by agent snippets written by `trie mcp install`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=fcd9e36d186ab8f16a78a876b81f5b1da6f9043a3d2dbfeeb64e753ce1428cda -->
## `mcp_install_cmd(ctx, target, install_all, scope, print_only, dry_run)`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

- `target`: repeat `--target` to install for multiple named agents.
- `install_all`: installs for every known target, skips per-target detection.
- `scope`: `'project'` or `'user'`; controls config file location.
- `print_only`: prints the snippet without writing any files.
- `dry_run`: resolves file paths and shows changes without writing.
- Exits 1 if any install result carries `action == "error"`.
<!-- trie:end -->