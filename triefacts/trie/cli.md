---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: 080da1123f1a448bc97061126302f796750d8c28bbd70463971edf08c5e57795
last_synced_at: '2026-05-14T18:56:56Z'
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
  lines: 522-605
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 835-838
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 855-924
incoming_refs: 0
outgoing_refs: 54
---
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=b4f1d7bff0bc8e455ed6de5c56b9e0c884e01c1dc12eba107d91abe90e5b8584 body_fp=cc2435f9123178ce4340f10dd7aec5dee444fb0bc6550a159b7f3e748306d7de -->
## `init_cmd(ctx, root, force, install_hooks, run_scan) -> None`

Create `trie.toml`, update `.gitignore`, build the symbol graph, and optionally install a pre-commit hook.

- `root`: project directory to initialise; defaults to `Path.cwd()`.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: if `None`, prompts interactively in a tty, skips in CI.
- `run_scan`: when `True`, builds the symbol graph immediately after writing config.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=b443a8e75a4561a3b46ece5f8fb678fe766e19a1565481ad16a80636b87de2dd body_fp=14cf55b0f1376fb61ade9790736993455cfd65439c08adc9218f2ceca8ab0471 -->
## `plan_cmd(ctx: typer.Context, model: str | None, all_: bool) -> None`

Scan the project, count tokens via the free endpoint, and print the worklist plus estimated cost without generating triefacts.

- `model`: overrides `config.models.bootstrap` for cost estimation only.
- `all_`: forces the full re-bootstrap view even when triefacts already exist.
- Exits 1 if no `trie.toml` is found.
- Auto-selects incremental vs full-bootstrap mode based on whether `.md` triefacts exist.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=c350c8c3b9c49583daf708215684050327bac351ba89c27ce1d376c8a899d3bb -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline drift check and exit with code 1 if any triefact has drifted from its source.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=fa4a984982fd7da361719c731982521093b761228ce0fd0ec1aa0d24ea193753 body_fp=cdefae49108dbeced28035e8fce80187b8006081afd252e4d14ac37113a08270 -->
## `sync_cmd(ctx: typer.Context, file: Path | None, all_: bool, budget: float | None, limit: int | None, dry_run: bool, model: str | None) -> None`

Generate or refresh triefacts, auto-detecting full bootstrap vs incremental cascade.

- `file`: sync exactly one source file; mutually exclusive with `--all`.
- `all_`: force full re-pass even when triefacts already exist.
- `budget`: stop once cumulative actual USD cost reaches this value.
- `limit`: cap total number of files processed.
- `dry_run`: write previews to `.trie/preview/` and print unified diffs instead of updating live triefacts.
- `model`: override the configured model string.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=f6e87043d32e3a9bfe993957da9934d895d20a0eb666bd42b4cde01b9eab51bd body_fp=44089177ea66c7e1e059ff81c9dcea86b8f1d2c38af67a0859486a926650df2a -->
## `mcp_serve() -> None`

Hidden stdio MCP server entry point; delegates to `_run_mcp_serve()`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=effa1a95fc861b6826db423d11be76f752dcfbb06b76769b6e64b724aa4d3be4 -->
## `mcp_install_cmd(ctx, target, install_all, scope, print_only, dry_run)`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

- `target`: repeat `--target` to install for multiple named agents; mutually exclusive with `--all`.
- `install_all`: installs for every known MCP target, skipping per-target detection.
- `scope`: `'project'` writes into the current project; `'user'` writes to `~/.<agent>/...`.
- `print_only`: prints the config snippet without writing any files.
- `dry_run`: resolves file paths and shows planned changes without editing.
- Exits `1` if any install result has `action == "error"`.
<!-- trie:end -->