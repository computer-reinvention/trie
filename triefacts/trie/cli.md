---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: 42b4d64de7305e8b6a3abd2e178c1ca37dea896dc9819230590f66613ef560ae
last_synced_at: '2026-05-15T13:04:58Z'
defines:
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 41-47
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 50-95
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 58-62
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 64-68
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 70-73
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 75-76
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 78-91
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 93-95
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 99-104
- kind: function
  qualified_name: trie/cli:_root
  lines: 108-146
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 149-161
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 165-248
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 251-258
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 261-266
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 262-263
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 265-266
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 270-363
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 367-379
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 382-399
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 402-413
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 416-482
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 495-506
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 509-540
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 544-627
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 630-636
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 639-703
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 706-751
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 754-782
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 785-834
- kind: function
  qualified_name: trie/cli:_mcp_root
  lines: 847-853
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 857-860
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 863-873
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 877-946
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 949-964
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

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=c26236341e0a2732ce5b6908eacd4e2989ab283b0664ce6042dc9271e3541b54 body_fp=d1f62ac0e7cb4f54c4664c87191ea9e2fa4549acd9888b92839636963ae78f8a source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `plan_cmd(ctx: typer.Context, model: str | None, all_: bool) -> None`

Scan the project, estimate token costs, and print the sync worklist without writing any triefacts.

- `model`: overrides `config.models.bootstrap` for cost estimation only.
- `all_`: forces full re-bootstrap cost view even when triefacts already exist.
- Runs offline drift check first; warns but does not abort on drift.
- Auto-selects incremental or full-bootstrap path based on existing triefacts.
- Uses Anthropic's `count_tokens` endpoint — networked but never `messages.create`.
- Incremental path passes per-file symbol regen counts to `build_plan` for symbol-level cost accuracy.
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

<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=f2d9816e4fd6a1b9e8627705664b4486fc5697b833ab0480b4b0e600936e9bcb source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_get_reporter(ctx: typer.Context) -> Reporter`

Resolve the `Reporter` stored in `ctx.obj`, returning a default `MEDIUM` reporter if none is set.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=2a082055da35a933023958cf947cba96cae1e82663b8e55faf4a477b4aadbea8 body_fp=2b5bba84d37e9a1765c05f6d3b75d22da408bf01f82087c25b1def6b0a59f314 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_ProgressAdapter`

Bridge `ProgressCallback` protocol events from sync internals to a `Reporter` `ProgressHandle`.

- `reporter`: receives progress display calls.
- `label`: displayed in the progress bar header.
- `handle`: lazily created on first `on_start` call using the reported total.
- `on_done`: computes per-file cost as delta from previous running total.
- `close`: must be called to flush the progress handle; used automatically via `_progress_callback`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=c14510df06e779a0b951076cf2cdcdef0c659fee5633432e88909b4376fd8e69 body_fp=752a66466c3e38e7952cd68cb2310bc0afe26e3a57272c712d238240ad1fea2d source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_ProgressAdapter.__init__(self, reporter: Reporter, label: str)`

Initialise the adapter with a reporter, progress label, and zeroed cost accumulator.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=38d28d902742473e5586cd4e13c06722e5d5096339015b40b5ff70355c49b986 body_fp=91b753edd23ca74ca8b9a26ed8f509cd33e0e8ccabe050003996ce94c2654508 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_ensure(self, total: int) -> ProgressHandle`

Lazily initialise and enter the `ProgressHandle`, creating it on first call with `total` as the step count.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=392ce38c0e4f4c301e58e63e9098c30faccbf9a19b05bc9a04755e1604b0f353 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `close(self) -> None`

Flush and tear down the active `ProgressHandle`, if one exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=0551e92b9a693655ab4b5f9d5bc3e8d459cf9b102ddcad2451c29652d843496c body_fp=b60e4a3431dcfece9ef072dea1eadae3e2a2bb324cb999e8db815336799b01b2 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `on_start(self, rel_path: str, idx: int, total: int) -> None`

Initialise the progress handle if needed and mark the given file as started.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=88aacff9d93c15fe0aca4c2bc861b5109627d980ddeccbfc6bee92f9c04f0a42 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Forward per-file completion to the progress handle, computing incremental cost from the running total.

- `running_cost_usd`: cumulative cost so far; delta from previous call is passed as `cost_usd`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=9abd5987532a2382742ed53bab919a624430f11c23a4384cc561aa54681fa034 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `on_skip(self, rel_path: str, reason: str) -> None`

Forward a skipped-file notification to the underlying `ProgressHandle`, if one exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=eaed89948850e6fbf30baed6116d0efd427e20caffba1e0873e28737ec97f651 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_progress_callback(reporter: Reporter, label: str) -> Iterator[ProgressCallback]`

Context manager yielding a `ProgressCallback`-compatible `_ProgressAdapter`, closing it on exit.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=db1388861c9f7d8b09988a2bf00aa3f2002c259bf595e7bbab3bc86848f5d168 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_root(ctx, version=False, quiet=False, verbose=False)`

Root Typer callback; sets up the `Reporter` on `ctx.obj` and handles `--version`.

- `quiet` and `verbose` are mutually exclusive; exits with code 2 if both set.
- `ctx.obj` is populated with a `Reporter` at `MUTE`, `MEDIUM`, or `VERBOSE` level.
- Emits a telemetry `cli` event for every subcommand invocation.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=5321640521e297cd44691f6243ca18fec2fa0460b77d497845375a07a3dfbb71 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_telemetry_bootstrap(subcommand: str | None, argv_tail: list[str]) -> None`

Load config (if available) to configure telemetry, then emit a `cli` event.

- `subcommand`: the invoked subcommand name, or `None` if absent.
- `argv_tail`: raw CLI arguments after the binary name, recorded with the event.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=cd0f697e85e091853bbd4be366abecbf94ac20ffa5d534d1b43e3c7b3962ad71 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_is_interactive() -> bool`

Return `True` when `stdin` is a tty, enabling safe interactive prompts.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=07d3527e58981eccc7c84c92c1d2b69e41dc4d7f24b83285995d9fa5cc4a82f2 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `class _NoOpStatus`

Context manager no-op substitute for `reporter.status(…)` when status display is suppressed.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=f8fc393016c5c5d99e94bf77f682374d261c9837a6cb1bcc663233e37007b52d source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_NoOpStatus.__enter__(self) -> _NoOpStatus`

Return self without performing any setup.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=80b6a8e5ded02596df3914456dd8b612b8088249bdecde0132b07f19545f29a4 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_NoOpStatus.__exit__(self, *exc: object) -> None`

No-op context manager exit; does nothing and returns `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=c59572c056f8ad7fc119369b38fdb84edb9a5253329e549785e17470714ae766 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_print_scan_breakdown(reporter: Reporter, scan_result, db_path: Path, project_root: Path) -> None`

Print a colour-coded file-count breakdown and symbol/edge totals after a project scan.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=28b41642092c34dbd7ba77559fd6360b0e26e78c828a7d121e4bcea99cdaaf76 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_print_plan(reporter: Reporter, plan: BootstrapPlan, model_id: str) -> None`

Print a bootstrap plan summary showing model, file count, estimated cost, and up to 10 file entries.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=19b339ffc29355db813e61c8dc866e26253e2ea43b3934502256eed83f166fe3 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_print_incremental_plan(reporter: Reporter, plan: BootstrapPlan, worklist: IncrementalWorklist, model_id: str) -> None`

Render incremental-sync plan output, grouping files by stale vs. cascade and listing orphan triefacts.

- `plan`: cost estimates per file; capped to 10 items in displayed output.
- `worklist`: provides `directly_stale`, `cascaded_files`, `hop_by_file`, `regen_qnames_by_file`, and `orphan_triefacts`.
- Files missing from `regen_qnames_by_file` are treated as full-file regenerations.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=5681f4dd4882cb48ea1f8d4be3e1d210d02d7f8f128bfb91007d2c3d426ce24b source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_print_drift_detail(reporter: Reporter, items: list) -> None`

Render per-file drift items grouped by triefact path, with labeled reasons, at MEDIUM+ verbosity.

- `items`: list of drift result objects with `triefact_path`, `reason`, `qualified_name`, and `source_path` attributes.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=ef3e367c95de6ba08711713a641d033313ab831ffe560665fbc803de70c77e28 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool`

Run an offline drift check and report results; return `True` if clean, `False` if drift found.

- `exit_on_drift`: when `True`, raises `typer.Exit(1)` on any drift instead of returning `False`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=4d8df1e255716e256f8a37ee27da5f370d9a4773f5546b3d35aaa306554c3229 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_has_existing_triefacts(triefacts_root: Path) -> bool`

Return `True` if `triefacts_root` exists and contains at least one `.md` file.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=c6533e3b2e50bdc28f9ca7d4c01807f528aee08fa13530c736ec9aa469f0a3dc body_fp=b2d11d1112a24d9d0385e8e077c108a5d429207beb909a7f5bdf346c163ff21b source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_run_full_pass(*, reporter: Reporter, project_root: Path, config: Config, model: str | None, budget: float | None, limit: int | None) -> None`

Scan, plan, optionally confirm, then run a full bootstrap sync with streaming per-file progress.

- `budget`: stops bootstrap once cumulative actual cost reaches this USD value.
- `limit`: caps the number of files synced.
- Prompts for confirmation in interactive mode when neither `budget` nor `limit` is set; exits 1 in non-interactive mode.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=508485b82253b57b7d8c744e0c9ff4ad4fda017a47c601097d8cfbc56eb6cbf6 body_fp=ac70a5ec59f69172dc697f98497c599045405973789ca078ed9484b0f1d968dd source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_run_dry_run_diff(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Regenerate stale triefacts into `.trie/preview/` and print unified diffs against the live tree.

- `budget`: stops accumulating LLM calls once cumulative cost reaches this USD value.
- `limit`: caps the number of files diffed.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=fb029b14fca1f85b7c3fad591caf8be50ee62e17579249ac84cef76d347012fc body_fp=b09e34f407e668bb1f6b55b5c55b7f0215a7009c0fd81eb63bff9049050e421d source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_run_single_file_sync(reporter: Reporter, file: Path, model: str | None) -> None`

Sync a single source file to its triefact, writing results and token stats via the reporter.

- `model`: overrides the configured bootstrap model when provided.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=ed18dd696aabf0fa346c31c725444100a8182c9c8f98f43efc8c16a5ec409e11 body_fp=22d50512b1fad776cf28d60527267edfe62e0292f68d9714cdf0ca68344b3926 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_run_incremental_sync(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Load config, build a client, and run incremental cascade sync, reporting orphan removals and cost.

- `budget`: USD cap; stops processing once cumulative actual cost reaches this.
- `limit`: maximum number of files to sync.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_mcp_root fingerprint=0d2be7c1cf311937fb8eee2f77ea130c45b0cf766836314f5e4c52c31152ec47 body_fp=f840b81b1a756cd15d5fc77c8e8bf463cbfe355fda71d17715922f66a84cefd0 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_mcp_root(ctx: typer.Context) -> None`

Fall through to `_run_mcp_serve()` when the `mcp` subcommand is invoked with no subcommand, preserving back-compatibility with `trie mcp` from v0.1.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=07eb42ce1a286e495b0cd202a9503cbd0cba66cff4cd5451e81254a12ac619a2 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_run_mcp_serve() -> None`

Load config from cwd and launch the stdio MCP server, exiting 1 if no config is found.

- Errors print to stderr to avoid corrupting the MCP protocol stream.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=b997f27bd9c17d08f4dd627e1973088c8c13f7f6f42ac00a09b8a647da8e5fcb source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_render_install_plan(reporter: Reporter, plan: InstallPlan) -> None`

Print each MCP install result (preview, created, updated, skipped, or error) via the reporter.
<!-- trie:end -->