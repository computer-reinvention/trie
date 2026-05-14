---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: a930f693e72634c2db2ac36528f6c1a73b43c30310fd3cd01be207ff63c9364e
last_synced_at: '2026-05-14T19:42:56Z'
defines:
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 165-248
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 270-357
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 361-373
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 530-613
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 843-846
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 863-932
incoming_refs: 0
outgoing_refs: 54
---
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=b4f1d7bff0bc8e455ed6de5c56b9e0c884e01c1dc12eba107d91abe90e5b8584 body_fp=a30e268f60bb85196fe5055818affc8f1a117b80c3e981aed18fd2751c260c76 source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `init_cmd(ctx, root, force, install_hooks, run_scan) -> None`

Initialize a trie project: write `trie.toml`, update `.gitignore`, optionally scan, and install a pre-commit hook.

- `root`: project directory to initialize; defaults to `Path.cwd()`.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: tri-state; prompts interactively when `None` in a tty, skips in CI.
- `run_scan`: builds the symbol graph immediately when `True`.
- Exits 1 on `InitError`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=b443a8e75a4561a3b46ece5f8fb678fe766e19a1565481ad16a80636b87de2dd body_fp=af1d74a1810288774ed0c1932ad367c34f87c13336873513c41faba32047ce6b source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `plan_cmd(ctx: typer.Context, model: str | None, all_: bool) -> None`

Scan the project, estimate token costs, and print the sync worklist without writing any triefacts.

- `model`: overrides `config.models.bootstrap` for cost estimation only.
- `all_`: forces full re-bootstrap cost view even when triefacts already exist.
- Runs offline drift check first; warns but does not abort on drift.
- Auto-selects incremental or full-bootstrap path based on existing triefacts.
- Uses Anthropic's `count_tokens` endpoint — networked but never `messages.create`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=7e53deb328e082791efe83f54f36b9744d8bae0789ffe2150787a6728327293b source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline drift check and exit 1 if any triefact has drifted from its source.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=fa4a984982fd7da361719c731982521093b761228ce0fd0ec1aa0d24ea193753 body_fp=47e255dc306f02490c03988f58f292b152f6303ce46518f9e33e547ca44e656a source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `sync_cmd(ctx: typer.Context, file: Path | None, all_: bool, budget: float | None, limit: int | None, dry_run: bool, model: str | None) -> None`

Generate or refresh triefacts, auto-detecting full bootstrap vs. incremental cascade mode.

- `file`: sync a single source file; mutually exclusive with `--all`.
- `all_`: force full re-pass over every in-scope file.
- `budget`: stop once cumulative actual spend reaches this USD value.
- `limit`: cap total files processed.
- `dry_run`: write previews to `.trie/preview/` and print unified diffs instead of updating live triefacts.
- `model`: overrides the configured model slug.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=f6e87043d32e3a9bfe993957da9934d895d20a0eb666bd42b4cde01b9eab51bd body_fp=c93e3469bbad48c77068e625d2c914a89a1e108a8747e920d1f2d45194952fda source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `mcp_serve() -> None`

Launch the stdio MCP server; hidden from help output and invoked directly by agent-installed snippets.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=2cc66f9f96d4842d8cc30188c10793327db51598b8fce5aa5bb261b842117677 source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `mcp_install_cmd(ctx, target, install_all, scope, print_only, dry_run)`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

- `target`: repeat `--target` to install for multiple named agents; mutually exclusive with `--all`.
- `install_all`: installs for every known target, skipping per-target detection.
- `scope`: `'project'` writes into the current project; `'user'` writes to `~/.<agent>/...`.
- `print_only`: prints the snippet without writing any files.
- `dry_run`: resolves file paths and shows changes without writing.
- Exits 1 if any install result has action `"error"`.
<!-- trie:end -->