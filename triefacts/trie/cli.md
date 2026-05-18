---
trie_version: 0.1.0
source: trie/cli.py
file_fingerprint: e718ab72b285003cd1ee31b51a512c5957fa7a6339cc8d5e7f10c21837345e46
last_synced_at: '2026-05-18T22:49:01Z'
defines:
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 81-87
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 90-135
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 98-102
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 104-108
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 110-113
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 115-116
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 118-131
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 133-135
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 139-144
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 148-179
- kind: function
  qualified_name: trie/cli:_root
  lines: 183-221
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 224-236
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 240-361
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 364-371
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 374-379
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 375-376
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 378-379
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 383-479
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 483-495
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 499-549
- kind: function
  qualified_name: trie/cli:refresh_cmd
  lines: 553-660
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 663-677
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 681-741
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 744-760
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 763-780
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 783-794
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 797-863
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 876-887
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 890-921
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 925-1041
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 1044-1050
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 1053-1117
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 1120-1165
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 1168-1196
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 1199-1256
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 1259-1308
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 1312-1478
- kind: function
  qualified_name: trie/cli:_resolve_override_consent
  lines: 1481-1553
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 1556-1626
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 1629-1655
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 1658-1662
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 1677-1689
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 1692-1716
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 1719-1786
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 1789-1836
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 1839-1889
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 1892-1904
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 1907-1969
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 1973-2076
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 2080-2111
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 2115-2157
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 2174-2176
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 2179-2189
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 2193-2262
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 2265-2280
incoming_refs: 0
outgoing_refs: 96
---
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=d73031440715902c67093bb14ec87479ecf1944b2e51c463133717c61d5f6642 body_fp=1c6cb5970e42afec64d45fece9df84f2b942bcf006c8b3719bb909e4270c3956 source_ref=ffa92f1d383e5f724d6bb3ddbf91a524903f8f73 -->
## `init_cmd(ctx, root, force, install_hooks, run_scan) -> None`

Create `trie.toml`, update `.gitignore`, optionally build the symbol graph, and install a pre-commit hook.

- `root`: project directory to initialise; defaults to cwd.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: tri-state; prompts interactively in a tty, skips in CI.
- `run_scan`: builds the symbol graph immediately after writing config.
- Offers to run `setup_cmd` interactively after completion.
- Exits 1 on `InitError`; exits 2 if the write lock is contended.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=1f9525fd75f6e14df3b9d54f2f02446677e7a0ab7562b7c1f66684cca46ca390 body_fp=32fffe4d193e74de627e39221f5eb3bfaa3b7f4c96da580f43b27821eff37f29 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `plan_cmd(ctx, model=None, all_=False)`

Scan the project, surface drift, and print the worklist with estimated LLM cost before committing to a sync.

- `model`: overrides the configured model for token-count estimation only.
- `all_`: forces the full re-bootstrap view even when triefacts already exist.
- Exits 1 on config errors; drift is reported as a warning but does not abort.
- Uses Anthropic's free `count_tokens` endpoint; never calls `messages.create`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=7e53deb328e082791efe83f54f36b9744d8bae0789ffe2150787a6728327293b source_ref=f9896112d3c74faa4a548ca30df39e8106603df3 -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline drift check and exit 1 if any triefact has drifted from its source.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=c08b2a86195dc0b7272c5f6c6ff6df2e7761fa27119ca2232fae50cbea7a3c51 body_fp=3d7fcfd41176e308116f3e9524eb49b108831af2aec47f7fd7b357ac838880a3 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `sync_cmd(ctx: typer.Context, file: Path | None, all_: bool, budget: float | None, limit: int | None, dry_run: bool, metadata_only: bool, model: str | None) -> None`

Generate or refresh triefacts, auto-selecting bootstrap, incremental, single-file, dry-run, or metadata-only mode.

- `file`: sync exactly one source file; mutually exclusive with `--all`.
- `all_`: force full re-pass over every in-scope file even if triefacts exist.
- `budget`: stop once cumulative actual USD cost reaches this value.
- `limit`: cap total files synced.
- `dry_run`: write regenerated triefacts to `.trie/preview/` and print unified diffs; makes API calls.
- `metadata_only`: rewrite front matter from live store only; no LLM, incompatible with all other flags.
- Exits 1 on config errors; exits 2 if write lock is held by another process.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=c93e3469bbad48c77068e625d2c914a89a1e108a8747e920d1f2d45194952fda source_ref=e48506a40b0b3397d184473a43843345d0706887 -->
## `mcp_serve() -> None`

Launch the stdio MCP server; hidden from help output and invoked directly by agent-installed snippets.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=2cc66f9f96d4842d8cc30188c10793327db51598b8fce5aa5bb261b842117677 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
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

<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=5321640521e297cd44691f6243ca18fec2fa0460b77d497845375a07a3dfbb71 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
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

<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=ef3e367c95de6ba08711713a641d033313ab831ffe560665fbc803de70c77e28 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool`

Run an offline drift check and report results; return `True` if clean, `False` if drift found.

- `exit_on_drift`: when `True`, raises `typer.Exit(1)` on any drift instead of returning `False`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=4d8df1e255716e256f8a37ee27da5f370d9a4773f5546b3d35aaa306554c3229 source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_has_existing_triefacts(triefacts_root: Path) -> bool`

Return `True` if `triefacts_root` exists and contains at least one `.md` file.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=699927ac70525f46f13cd69b8026fe5e3da3102e36ae1ab84a1694719543c46c body_fp=b2d11d1112a24d9d0385e8e077c108a5d429207beb909a7f5bdf346c163ff21b source_ref=01455b75f5ce687baf9f3308e56ac1b4b24427bd -->
## `_run_full_pass(*, reporter: Reporter, project_root: Path, config: Config, model: str | None, budget: float | None, limit: int | None) -> None`

Scan, plan, optionally confirm, then run a full bootstrap sync with streaming per-file progress.

- `budget`: stops bootstrap once cumulative actual cost reaches this USD value.
- `limit`: caps the number of files synced.
- Prompts for confirmation in interactive mode when neither `budget` nor `limit` is set; exits 1 in non-interactive mode.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=ac70a5ec59f69172dc697f98497c599045405973789ca078ed9484b0f1d968dd source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_run_dry_run_diff(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Regenerate stale triefacts into `.trie/preview/` and print unified diffs against the live tree.

- `budget`: stops accumulating LLM calls once cumulative cost reaches this USD value.
- `limit`: caps the number of files diffed.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=19a520c5b19e8901f07865a60c1613fb5dcaef9ee1c50321c6316f4baa71608c body_fp=b09e34f407e668bb1f6b55b5c55b7f0215a7009c0fd81eb63bff9049050e421d source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_run_single_file_sync(reporter: Reporter, file: Path, model: str | None) -> None`

Sync a single source file to its triefact, writing results and token stats via the reporter.

- `model`: overrides the configured bootstrap model when provided.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=c0296f53afdae836d3646b2af7059167e69e09ce2828ef92af30e3df36f33e9a body_fp=22d50512b1fad776cf28d60527267edfe62e0292f68d9714cdf0ca68344b3926 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_run_incremental_sync(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Load config, build a client, and run incremental cascade sync, reporting orphan removals and cost.

- `budget`: USD cap; stops processing once cumulative actual cost reaches this.
- `limit`: maximum number of files to sync.
<!-- trie:end -->



<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=07eb42ce1a286e495b0cd202a9503cbd0cba66cff4cd5451e81254a12ac619a2 source_ref=577b5c634ebcbb90471bd6a1e8c66ae8c26b6a92 -->
## `_run_mcp_serve() -> None`

Load config from cwd and launch the stdio MCP server, exiting 1 if no config is found.

- Errors print to stderr to avoid corrupting the MCP protocol stream.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=b997f27bd9c17d08f4dd627e1973088c8c13f7f6f42ac00a09b8a647da8e5fcb source_ref=7190421a8bd3d24b87655e9ae289b7d639fa3f21 -->
## `_render_install_plan(reporter: Reporter, plan: InstallPlan) -> None`

Print each MCP install result (preview, created, updated, skipped, or error) via the reporter.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=5756d1b7e32899d278d6ffb9c3d820058831de9e933722d87f89c248c1fbabcf body_fp=eec19cb7b0326e95cab70d820ed0b13615c844cd6c2d14154c9c3369b230d6e9 source_ref=59a8f59eb43081192cbbe4499ed354aa9437ca29 -->
## `audit_cmd(ctx: typer.Context, log: Path | None, compare: Path | None, as_json: bool) -> None`

Summarise a telemetry `debug.jsonl` log; optionally compare two logs side-by-side or emit JSON.

- `log`: path to the log file; defaults to config's `debug.log_path` or `./debug.jsonl`.
- `compare`: second log rendered as candidate against `log` as baseline; mutually exclusive with `--json`.
- `as_json`: print `AuditSummary` as JSON to stdout; mutually exclusive with `--compare`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=0660b55daee64da526b9c6830a141120b802aa26aee944f9dcae8f8ab08cdfb5 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_resolve_audit_log_path(log: Path | None, reporter: Reporter) -> Path`

Resolve the `debug.jsonl` path from explicit arg, configured `log_path`, or cwd fallback.

- `log`: returned directly if provided; skips all config resolution.
- Returns cwd `debug.jsonl` if no `trie.toml` is found.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=ab88ff6a5f8617fcb6bbcc42dae27974d38c2d4d9d9e8f5df2a4c2dcd0f4ad19 body_fp=c777944aa3562954585519eb25a905a5e76f9dcbdda8d6edda859064d837e132 source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `_run_metadata_only_refresh(reporter: Reporter) -> None`

Refresh every triefact's front matter from the live store without calling the LLM.

- Rescans the project first so the graph reflects any resolver changes before rewriting metadata.
- Skips files outside `source_root`; reports changed vs already-current counts on completion.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:refresh_cmd fingerprint=95e65ccc97ba70699bc324ee65dfe871388eac222ef0b055579035abd808497d body_fp=05729acad5ed11d9e54b78144c94e261ccbcbfa92d62f8b87108a9858e2418de source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `refresh_cmd(ctx, before_turn, after_turn, model)`

Bring the graph and triefacts up to date with the working tree via a freshness-gated sync.

- `--before-turn`: cheap gate; full sync only if HEAD or mtimes changed since last refresh.
- `--after-turn`: detects filesystem changes since last refresh and syncs affected files.
- Neither flag: defaults to `--after-turn` behaviour.
- `--model`: overrides `config.models.cascade`; only used when a sync actually fires.
- Exits 1 outside a git repo; serialises concurrent refreshes via lock, coalescing queued callers into one tail pass.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=39c12516433ffd01deaf7e6d4dc9d72f23e588c64a16997bc815624ddc2aeb44 body_fp=7644c6fc037fd8d0e5e3762babb2135d704b50c9b5ee408b0e30fe27f4f364c2 source_ref=245a1b3bb69d531fc2880760ae9b2ca22d6e4815 -->
## `_report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None`

Render a single-line refresh outcome to the reporter, plus sync statistics when a sync ran.

- `mode`: label string (e.g. `"before-turn"` or `"after-turn"`) prepended to output.
- `result.refreshed`: if `False`, prints an "already fresh" success line and returns.
- `result.incremental`: used to report files synced and actual cost; skips detail if `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=7fe4447bde31d0cfb60c38e96883041566cfdecb2c9145bee18cc7c88438de04 body_fp=d4ea638b5c35481c3b0f0544531e69b848bf6d916263d8f2c4b45dc6342eaa8c source_ref=d1d50bb3b3ca812d5f20af628d688c8f98a4b62d -->
## `setup_cmd(ctx, target, install_all, scope, print_only, dry_run, override_builtins)`

Wire trie into an agent end-to-end: MCP registration, turn hooks, docs, and optional tool-override install.

- `target`: agent slug(s) to configure; auto-detected when omitted.
- `install_all`: configure every known agent, skipping detection.
- `scope`: `"project"` (writes into repo) or `"user"` (writes to `~/.<agent>/`).
- `print_only`: print would-be file contents without writing anything.
- `dry_run`: resolve paths and show changes without writing.
- `override_builtins`: `True` forces override install; `False` skips; `None` prompts interactively (or skips in CI).
- Exits `1` if any install step produces an error result.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=3e5b01ac92b109f053066da2201d46cb6cb10e544ab73ab4c3fb193743395c1b body_fp=c22cb466dba4cb9d7748425e323a9319d0e6736d782353f0838d7eac06d759c9 source_ref=d1d50bb3b3ca812d5f20af628d688c8f98a4b62d -->
## `_render_setup_plan(reporter: Reporter, mcp_plan: InstallPlan, hook_plan: HookInstallPlan, docs_plan: DocsInstallPlan, override_plan: ToolOverrideInstallPlan | None = None) -> None`

Print a merged per-target report showing MCP, hook, and optional tool-override install outcomes, with manual-setup warnings where applicable, plus a target-independent docs section.

- `mcp_plan`: MCP install results grouped by target slug.
- `hook_plan`: Hook install results grouped by target slug.
- `docs_plan`: Docs install results (TRIE.md / agent doc pointers); rendered as a single trailing section.
- `override_plan`: Optional tool-override install results; when provided, each target's override outcome is rendered via `_render_override_target_block`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=ae70c1dcc650d55b85c914d92499534930d66f081f32f21e7797135e8503ed84 source_ref=59a8f59eb43081192cbbe4499ed354aa9437ca29 -->
## `_format_action(action: str, path: Path | None) -> str`

Render an action label with an optional path suffix for display in install plan output.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=3ae553a9c7f238f7b80d985c0aa027e15c51ac29b1e281d7444eecc167631911 body_fp=a51d8a8232a5ba04fe6c145f2ce13ad8d75fe3add3190cd484908de246bea634 source_ref=df2eab34e273723a3bf42ae891020acd147e6bd4 -->
## `_acquire_write_lock_or_exit(project_root: Path, reporter: Reporter, command_name: str) -> Iterator[None]`

Context manager that holds the refresh lock for a write-side command, or exits with code 2 if already contended.

- `project_root`: determines which `.trie/` lock file to acquire.
- `command_name`: embedded in the error message and telemetry event.
- Exits code 2 (transient/retry) rather than 1 (config error) on contention.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=b2588d0ec23978e9e8f4b7732d307584d0bad5d7227cee2cf553c7f4c21bf287 body_fp=12bc621b6c9982cc36c217189f79c16b1b6b20cec48af033f129d4cb48ed76ae source_ref=707967fd5080b111a7f84fd2714d452f946c1ea5 -->
## `lock_check_cmd(ctx: typer.Context) -> None`

Probe whether another trie process holds the project's write lock, exiting 2 if contended.

- Exit 0: lock is free, or no `trie.toml` found.
- Exit 2: lock is held; caller should refuse to proceed and retry.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_open_tools fingerprint=7b6edc0030a5ca5cfcaff08eebbcc1ec1b3f7400cae950745b9ee7c8b5fbd7f7 body_fp=e2f620a0cd5115a0e30c4339de6bc184952fb0096209fcc42dabc6480de5c5b5 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_open_tools(reporter: Reporter) -> TrieTools`

Resolve project root and return an open `TrieTools` session; caller must call `.close()` when done.

- Exits with code 1 if no `trie.toml` is found.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=d15b5370874d8b94df0d2372a280fa7b658c2527166c0dd2a6a2feb996a61427 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_emit_envelope(envelope, *, as_json, reporter, render)`

Print an MCP response envelope as raw JSON or via a human-readable renderer, exiting 1 on error envelopes.

- `envelope`: MCP response dict, optionally containing an `"error"` key.
- `render`: callable that formats the envelope for human output.
- `as_json`: dumps to stdout verbatim, bypassing Rich formatting.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_grep fingerprint=868adb38d55c12e59d7a2b45d8f60f00fff09cafdddc5ed12610304a5621d8cd body_fp=936515847144cc5fa0c07943f2612d22a07bfedf1316d141fcdc4aee819dca97 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_render_grep(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `grep` response envelope in human-readable form: a Rich table of hits, or a fallback candidates table, or an error block.

- `envelope`: MCP-shaped dict with `hits`, `fallback`, or `error` key.
- Delegates error rendering to `_render_error_envelope`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_read fingerprint=bd5e442551e9a4a5c99767903ee70eb72ece12ca2970bcd78b78d7a06ac19dd0 body_fp=75fe3286b5b2cc3946792a8f360f6d1cfb7b45c77c1ace49df981e7b1a825ee1 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_render_read(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie read` MCP envelope in human-readable form: signature, source pointer, prose, and caller/callee neighbour lists.

- `envelope`: MCP response dict; error envelopes are dispatched to `_render_error_envelope`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_trace fingerprint=fc3af28c35192dc6686d551bf13ac8695eb77b0a4a30aa3fa400b42a1197d6b6 body_fp=226ac5a9214e1b3e7fb9b48835dee94129535b963d7f06f03946d0c9b6b43f23 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_render_trace(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie trace` MCP envelope in human-readable form: root node, full node list, edge list, truncated hubs, and notes.

- `envelope`: expected keys `root`, `nodes`, `edges`, `truncated_at`, `notes`, `error`.
- Error envelopes are forwarded to `_render_error_envelope`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=cce4798c6e380be011d07af7ddb8c9e2d79b0efa700301d8b8f3df97d2ff6db2 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_render_error_envelope(err: dict[str, object], reporter: Reporter) -> None`

Render a `{code, message, suggestion?}` error envelope to the terminal and exit with code 1.

- `err`: dict with keys `code`, `message`, and optional `suggestion`.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=382d42b923ee5774c3f51a00d2149603b1a3a515add1e69fa25f9064c1a35c14 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `_build_grep_predicate(name, kind, scope_prefix, scope_exclude, public_only, inbound_min, inbound_max, outbound_min, outbound_max, predicate_json, reporter) -> dict[str, object]`

Assemble a TrieTools grep predicate dict from CLI flags, optionally merging a base JSON envelope.

- `predicate_json`: parsed first as the base shape; explicit flags override matching fields.
- `scope_exclude`: converted to a plain list under `"scope_exclude"` key.
- `inbound_min`/`inbound_max`: merged into a single `"inbound_count"` sub-dict.
- `outbound_min`/`outbound_max`: merged into a single `"outbound_count"` sub-dict.
- Exits with code 2 if `predicate_json` is invalid JSON or not an object.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=7af0b3ce0797e936332bf7102a9595b0ff85a838a842365164cb0322625ef53c source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `grep_cmd(ctx, name, kind, scope_prefix, scope_exclude, public_only, inbound_min, inbound_max, outbound_min, outbound_max, predicate_json, rank_by, limit, as_json)`

Find symbols matching a predicate via `TrieTools.grep`; mirrors the MCP `grep` tool.

- `predicate_json`: full predicate JSON object; individual flags override matching fields.
- `rank_by`: `public_first` (default), `inbound_count`, or `alphabetical`.
- `as_json`: emit raw MCP wire envelope to stdout instead of a Rich table.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:read_cmd fingerprint=17492b277aded6e3ff96eab437be39b135df14a26859018d4e3d5bdce03eeb0f body_fp=628dfc7d37a32fb5d27ab71f096c8ec2563fd9b0f4d9ad63d8e3e3725e1ed45e source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `read_cmd(ctx: typer.Context, qname: str, as_json: bool = False) -> None`

Read a symbol's triefact prose, signature, source pointer, and one-hop caller/callee neighbourhood.

- `qname`: fully-qualified symbol name, e.g. `trie/sync/cascade:compute_cascade`.
- `as_json`: emit raw MCP envelope JSON instead of human-readable output.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=c903ff3d1a45112a45ca4c44e4cfc092dfc91326d4aba856a3a9de1609eddaa8 source_ref=b3dad490301085704dfd690db8d4e4c82b1f8971 -->
## `trace_cmd(ctx, qname, direction, depth, as_json)`

Trace the call graph from a symbol outward up to `depth` hops via the MCP `trace` tool.

- `direction`: `"callers"`, `"callees"`, or `"both"`.
- `depth`: BFS depth; clamped by `trace_max_depth` in config.
- `as_json`: dumps raw MCP envelope to stdout instead of human-readable output.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_resolve_override_consent fingerprint=aa5338e97363dd4891d4058bfac5e88d25f8a3f1b51a1eb6860038d2104b7c8b body_fp=4f0a8b23e292b5941b78e20e2d216fef1c9a384ee442521e4199e8932deb145e source_ref=d1d50bb3b3ca812d5f20af628d688c8f98a4b62d -->
## `_resolve_override_consent(reporter, *, override_builtins, target_names, print_only, dry_run) -> bool`

Decide whether to run the tool-override install step for a `setup` invocation.

- `override_builtins=True`: always returns `True`; `False`: always returns `False`.
- `print_only` or `dry_run` with no explicit flag: returns `True` (show preview, no writes).
- Non-interactive stdin with no explicit flag: returns `False` and emits an info message.
- Interactive TTY with no explicit flag: prints per-target summary and prompts; default answer is no.
<!-- trie:end -->

<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=c80b210bde2cc2ebe252cd36099bd080babac75fa8ea414d52267edef48c8058 body_fp=59ecd7a9421d8d1ac214923e0f932c2f4b2ee41d7d522a1161f5cdbb2e37f0e0 source_ref=d1d50bb3b3ca812d5f20af628d688c8f98a4b62d -->
## `_render_override_target_block(reporter: Reporter, result: object) -> None`

Render a single target's tool-override install outcome to the reporter, listing per-file results beneath a summary line.

- `result`: duck-typed install result with `.action`, `.files`, `.detail`, and per-file `.relative_path`, `.description`, `.detail` attributes.
<!-- trie:end -->