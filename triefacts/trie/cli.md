---
trie_version: 0.1.2
source: trie/cli.py
file_fingerprint: ce0f276b82ff0f3ed744e9116e35a62ab02fff6dc7a5c1f9ac027e29cf18999e
last_synced_at: '2026-05-24T00:25:15Z'
defines:
- kind: module
  qualified_name: trie/cli:__module__
  lines: 1-2528
- kind: constant
  qualified_name: trie/cli:app
  lines: 72-75
- kind: constant
  qualified_name: trie/cli:console
  lines: 76-76
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 79-85
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 88-133
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 96-100
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 102-106
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 108-111
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 113-114
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 116-129
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 131-133
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 137-142
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 146-177
- kind: function
  qualified_name: trie/cli:_root
  lines: 181-219
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 222-234
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 238-359
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 362-369
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 372-377
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 373-374
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 376-377
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 381-480
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 484-496
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 500-550
- kind: function
  qualified_name: trie/cli:refresh_cmd
  lines: 554-664
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 667-681
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 685-745
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 748-764
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 767-784
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 787-798
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 801-867
- kind: constant
  qualified_name: trie/cli:_REASON_LABELS
  lines: 870-877
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 880-891
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 894-925
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 929-1057
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 1060-1066
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 1069-1133
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 1136-1181
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 1184-1217
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 1220-1277
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 1280-1329
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 1333-1507
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 1510-1580
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 1583-1609
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 1612-1616
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 1631-1649
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 1652-1676
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 1679-1746
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 1749-1796
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 1799-1849
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 1852-1864
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 1867-1929
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 1933-2036
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 2040-2071
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 2075-2117
- kind: function
  qualified_name: trie/cli:_print_plain
  lines: 2127-2141
- kind: function
  qualified_name: trie/cli:grep_str_cmd
  lines: 2145-2160
- kind: function
  qualified_name: trie/cli:grep_entry_points_cmd
  lines: 2164-2179
- kind: function
  qualified_name: trie/cli:grep_symbol_cmd
  lines: 2183-2198
- kind: function
  qualified_name: trie/cli:grep_symbol_neighbours_cmd
  lines: 2202-2217
- kind: function
  qualified_name: trie/cli:explain_symbol_cmd
  lines: 2221-2236
- kind: function
  qualified_name: trie/cli:explain_symbol_refs_cmd
  lines: 2240-2255
- kind: function
  qualified_name: trie/cli:trace_flow_cmd
  lines: 2259-2275
- kind: function
  qualified_name: trie/cli:explain_flow_cmd
  lines: 2279-2295
- kind: constant
  qualified_name: trie/cli:mcp_app
  lines: 2303-2310
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 2315-2317
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 2320-2330
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 2334-2403
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 2406-2421
- kind: function
  qualified_name: trie/cli:mcp_uninstall_cmd
  lines: 2425-2500
- kind: function
  qualified_name: trie/cli:_render_uninstall_plan
  lines: 2503-2523
incoming_refs: 82
outgoing_refs: 104
---
<!-- trie:section symbol=trie/cli:__module__ fingerprint=ef84c103f6fe2975bfda91084d2b78296c8b56a63a80cc2b2e177f308dad1691 body_fp=04b225e40dee1bd3dc46b0d2f764765c5ebfac106075450fbeabffada9007f0b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `trie/cli.py`

Define the `trie` CLI application: all subcommands, progress adapters, rendering helpers, and the `mcp` sub-app.

- `app`: root Typer application, entry point when run as `__main__`
- `mcp_app`: nested Typer group mounted at `trie mcp`
- `console`: shared Rich `Console` used by all reporters
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:app fingerprint=bd6ef12c875332ea01db62797e29cf2fb64ae5ac0be52a25d5f8aa08f5abb82c body_fp=07cea146910642a73fb4b751051bd6c70c0e9d0a32db4a2ee87b2ee8a0a9f8bd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `app = typer.Typer(name="trie", ...)`

Root Typer application instance that all `trie` subcommands are registered against.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:console fingerprint=dff6104fc5140b6d96afa42ceddb0c4c0d1e4b0cb6686a2debb687f087a24c7e body_fp=f8e23a47fcc2e7dffa55b92e35093b5febd3f4f19331709061f4e27e00996435 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `console = Console()`

Module-level Rich `Console` instance shared across all CLI output functions.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=10a790ccc7ed2bbb03682c3341bbc3a42df6143bfd1f6821ce6790c7beae95f0 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_get_reporter(ctx: typer.Context) -> Reporter`

Return the `Reporter` attached to the Typer context, falling back to a default MEDIUM `Reporter` if none is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=2a082055da35a933023958cf947cba96cae1e82663b8e55faf4a477b4aadbea8 body_fp=ab72199342cd15c5f6fab100c77c718d24c5e87e19950564721d370b971bc8f0 source_ref=81ec453e27d219340630c14d41a7b913b703d744 -->
## `_ProgressAdapter`

Bridge sync's `ProgressCallback` protocol to a `Reporter` `ProgressHandle`, lazily initialising the handle on the first `on_start` call.

- `handle`: created on first `on_start`; `None` until then.
- `on_done`: derives per-file cost from the running total delta before forwarding token/symbol stats.
- `close`: exits the `ProgressHandle` context manager and clears the reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=c14510df06e779a0b951076cf2cdcdef0c659fee5633432e88909b4376fd8e69 body_fp=c3be3a3e7bd95e5e83a97943b80f25a7c4aab8be9aa22ca664468efdfef761c5 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter.__init__(self, reporter: Reporter, label: str)`

Initialise a `_ProgressAdapter`, storing the reporter and label and setting handle to `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=38d28d902742473e5586cd4e13c06722e5d5096339015b40b5ff70355c49b986 body_fp=e19355c6d529cec44af8a513a2f72667ff670cbd7d879f51444f6b37b200fa84 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter._ensure(self, total: int) -> ProgressHandle`

Lazily initialise and return the `_ProgressAdapter`'s `ProgressHandle`, creating it on first call.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=dc200b186b54a1470f63b2aca103e096d0595706a29045a8d183d0483e75fabe source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter.close(self) -> None`

Tear down the `_ProgressAdapter`'s underlying `ProgressHandle` if one was created.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=0551e92b9a693655ab4b5f9d5bc3e8d459cf9b102ddcad2451c29652d843496c body_fp=f46ce3f22c9438ebc2f762d6232873be52f498632d31e3d872f677bd55c83d1d source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter.on_start(self, rel_path: str, idx: int, total: int) -> None`

Initialise the `_ProgressAdapter` progress handle if needed and mark `rel_path` as started.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=bcf971d088106d8d8225c61dc66e94822eb2c8b17c1fc105ff77e6ec9813e81d source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter.on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Advance the `_ProgressAdapter` progress handle after a file sync completes, forwarding per-file cost and token telemetry.

- `running_cost_usd`: cumulative total; per-file cost is derived by subtracting the previous value.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=ddaaf6ad94c811557bb62e3259796502a8a180df45d23c87b39368930d7278b1 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_ProgressAdapter.on_skip(self, rel_path: str, reason: str) -> None`

Forward a skip notification to the `_ProgressAdapter`'s underlying `ProgressHandle`, if one exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=b206a847f45a42ad63ecd91560c70ee510749067256954286d2f0c71d6772e1a source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_progress_callback(reporter: Reporter, label: str) -> Iterator[ProgressCallback]`

Context manager yielding a `_ProgressAdapter` as a `ProgressCallback`, closing it on exit.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=3ae553a9c7f238f7b80d985c0aa027e15c51ac29b1e281d7444eecc167631911 body_fp=ecbc616fec1cb64c0bc725d33f10f8add80b9c35eaf11d10163fa4c5d997434f source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_acquire_write_lock_or_exit(project_root: Path, reporter: Reporter, command_name: str) -> Iterator[None]`

Hold the refresh lock for a write-side command's duration, or exit loudly with code 2 if already held.

- `command_name`: included in the error message and telemetry event.
- Exit code 2 signals transient lock contention (retry); exit code 1 signals non-transient config errors elsewhere.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=b7e45d13cc5e5c8b1e29a8bfa928f7be2fd13a0d6438d49325eda17d5fd9008e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_root(ctx, version, quiet, verbose) -> None`

Typer root callback that initialises the shared `Reporter` on `ctx.obj` and handles `--version`.

- `--quiet` and `--verbose` are mutually exclusive; violating this exits with code 2.
- Sets `ctx.obj` to a `Reporter` at `MUTE`, `VERBOSE`, or `MEDIUM` verbosity accordingly.
- Prints help and exits when no subcommand is given.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=b319bed05c9207bf1499b6a47cc87f3a3670f5a8669a2307c81c77a3d8463a43 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_telemetry_bootstrap(subcommand: str | None, argv_tail: list[str]) -> None`

Apply `[debug]` config from `trie.toml` (if present) and emit the `cli` telemetry event.

- Silently swallows all errors; telemetry never blocks a command.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=1d3815663e939a183a3615fa14bce2303216da8109575c962b16755709c45c26 body_fp=2feb3ea84625b80f2fd4bc733a31663a4e5cb37dc90ba8cd818d62bdc1ee8296 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `init_cmd(ctx, root, force, install_hooks, run_scan)`

Create `trie.toml`, update `.gitignore`, optionally build the symbol graph, and install a pre-commit hook.

- `root`: project directory to initialise; defaults to `cwd`.
- `force`: overwrites existing `trie.toml` and skips Python-project detection.
- `install_hooks`: tri-state; prompts in a tty, skips in CI when `None`.
- `run_scan`: builds the symbol graph immediately after writing `trie.toml`.
- Holds the write lock for the duration; exits 2 on lock contention, 1 on `InitError`.
- Offers to invoke `setup_cmd` interactively when stdin is a tty.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=ae09697407f8eed5d369bb95c5fdc1eba2a7ab8148ab77c37e3adfae5a85321c source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_is_interactive() -> bool`

Return `True` when `stdin` is a TTY, enabling safe interactive prompts.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=e32cb110bee3d81871bc1486bcc5875e32492b62b46771502ee4ce287c563037 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_NoOpStatus`

Context manager no-op substitute for `reporter.status(…)` when no progress display is needed.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=682d69eeea33c0afd0c5a78672b62bdc059c50084889cc2d5c53244373f2746d source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_NoOpStatus.__enter__(self) -> _NoOpStatus`

Enter the `_NoOpStatus` context manager, returning itself.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=3e08571397a8cbac5ee6fbe5f13ea7cf2e1e47c20536cfd90c6a4b68cbe9992e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_NoOpStatus.__exit__(self, *exc: object) -> None`

No-op context manager exit for `_NoOpStatus`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=373611a9d3e4483138772bfb37fc6df782949064514db26f320d72889ab86b34 body_fp=95e59ce750424be17e72f24a70943c07dfd239b35d4e4ed87f547fd628f7359d source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `plan_cmd(ctx, model, all_) -> None`

Scan the project, report drift, and print the worklist with token-counted cost estimates without generating any triefacts.

- `model`: overrides `config.models.bootstrap` for token counting.
- `all_`: forces full re-bootstrap cost view even when triefacts already exist.
- Uses `count_tokens` only (no `messages.create`); makes API calls but incurs no generation cost.
- Auto-selects incremental mode when triefacts exist and `--all` is absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=0dba98c471cfd8f4e14a74fa80b48c751ce7710f2284cb7735f370057ed824fb source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `verify_cmd(ctx: typer.Context) -> None`

Run an offline, bidirectional drift check and exit 1 if any triefact has drifted from its source.

- No LLM calls, no DB writes; safe for pre-commit hooks and CI.
- Detects both source-changed-but-not-regenerated and tampered/orphaned triefact sections.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=b2588d0ec23978e9e8f4b7732d307584d0bad5d7227cee2cf553c7f4c21bf287 body_fp=897714d09b05fb159c1b025b4794e73943a5e4519c951d47dfaded44ea9423fa source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `lock_check_cmd(ctx: typer.Context) -> None`

Probe whether another trie process holds the project's write lock without blocking or interfering.

- Exit 0: lock free, or no `trie.toml` found.
- Exit 2: lock held; caller should retry after the writer finishes.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:refresh_cmd fingerprint=9650ac7742d77ff500365c3ea2b7d0c224376d86b3bf256763d5591ecf94d749 body_fp=e1639e7ebff8d4494a8d00a51ac6d3c73074f09292b1951c9e5de9c123a1f427 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `refresh_cmd(ctx, before_turn, after_turn, model) -> None`

Sync the graph and triefact tree with the working tree, serialising concurrent hook invocations via the write lock.

- `--before-turn`: cheap gate; full sync only when HEAD or mtimes changed.
- `--after-turn`: picks up filesystem changes since the last refresh; default when neither flag given.
- Concurrent refresh: queued, not rejected; at most one tail pass runs after the lock holder finishes.
- Exits 1 outside a git repo or on config error; never exits 2 (contention is silently queued).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=39c12516433ffd01deaf7e6d4dc9d72f23e588c64a16997bc815624ddc2aeb44 body_fp=e4b15eb7b3df567c86b96f25c6918f8f011c169cd17e2fd008e8dbb300462717 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None`

Emit a single reporter line per `FreshnessResult`, including synced file count and cost when a sync ran.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=5756d1b7e32899d278d6ffb9c3d820058831de9e933722d87f89c248c1fbabcf body_fp=8d41e299fc979a9912ce297128555977b65d5e903a91899aeeba40b149f69f58 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `audit_cmd(ctx, log, compare, as_json) -> None`

Summarise a `debug.jsonl` telemetry log: MCP usage, sync activity, retries, and CLI invocations.

- `log`: path to log file; defaults to `[debug].log_path` from `trie.toml` or `./debug.jsonl`.
- `compare`: second log rendered as candidate in a side-by-side delta comparison against `log`.
- `as_json`: dump `AuditSummary` as JSON to stdout; mutually exclusive with `--compare`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=4ab3109b9d683e6ca19b2d3ca58be8b4786f2b6cd400e90d36febea52dcfd2d7 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_resolve_audit_log_path(log: Path | None, reporter: Reporter) -> Path`

Resolve the `debug.jsonl` path for `trie audit` using a three-tier fallback.

- Falls back to `[debug].log_path` from `trie.toml`, then `./debug.jsonl` if no config exists.
- Relative `log_path` values are resolved relative to `project_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=aeef0912727dddb2fbbda76ff66295d13af486a974e5c42951cb01a0e8ac4fdd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_print_scan_breakdown(reporter: Reporter, scan_result, db_path: Path, project_root: Path) -> None`

Print a colour-coded file-count summary and symbol/edge detail line after a project scan.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=c6f05bd2f9e3cb0c30e4332509892b6b2b7e2d7bf6dff4683dea7b2c248215f4 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_print_plan(reporter: Reporter, plan: BootstrapPlan, model_id: str) -> None`

Print a full-bootstrap plan summary: total file count, estimated cost, and up to 10 per-file lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=3e78b1ee0151b322a7663b4ef9e7581422535ebccdd390f4c56fac133a44f08d source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_print_incremental_plan(reporter: Reporter, plan: BootstrapPlan, worklist: IncrementalWorklist, model_id: str) -> None`

Print the incremental sync plan: summary line, up to 10 files ordered stale-first then cascade-by-hop, and orphan triefacts to remove.

- `plan`: cost-estimated worklist from `build_plan`.
- `worklist`: carries directly-stale, cascaded, orphan, and hop-distance data.
- Files absent from `regen_qnames_by_file` show full symbol count; present entries show `regen/total`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_REASON_LABELS fingerprint=ec482101fe58286effe17023a43479424dfb2b828cee44ffb3f99e8b9adbf8bb body_fp=bf03d4c1f9f6434dcde94f38567fd9a05bf91dcb28b29869868a90a95f55a798 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_REASON_LABELS: dict[StaleReason, str]`

Map each `StaleReason` enum member to its human-readable drift label for drift detail rendering.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=fdc33281041fc5c1fa23bd235bed5af081b08319d9c6605f012d591bb17634e1 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_print_drift_detail(reporter: Reporter, items: list) -> None`

Render grouped drift items to the console, one triefact file header per group with labelled per-symbol reasons beneath.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=4092914b8860b3a286fc5cae87fa58cac357a1027df765200aebbcf3d9a2cfba source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool`

Run an offline drift check and report results, returning `True` if clean.

- `exit_on_drift`: if `True`, raises `typer.Exit(1)` on drift; otherwise warns and returns `False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=304f6c1245eb2f8cd864c080d949ec805171293731bbbcda0fbea9cafab47691 body_fp=f84887e8e1605d886aaf993584b931fb9a17f0d20e071175b0fcb944e19ec87a source_ref=81ec453e27d219340630c14d41a7b913b703d744 -->
## `sync_cmd(ctx, file, all_, budget, limit, dry_run, metadata_only, model, force) -> None`

Generate or refresh triefacts, auto-selecting bootstrap, incremental, single-file, dry-run, or metadata-only mode.

- `file`: sync exactly one source file; mutually exclusive with `--all`.
- `all_`: force full re-pass even when triefacts already exist.
- `budget`: USD cap; stops once cumulative actual cost is reached.
- `limit`: maximum number of files to sync.
- `dry_run`: writes previews to `.trie/preview/` and prints unified diffs; makes API calls.
- `metadata_only`: rewrites front matter only; no LLM, no section changes; incompatible with all other flags.
- `force`: bypass diff-aware path and cold-regenerate every symbol; only valid with `--file`.
- Exits 2 if the write lock is held by another process; exits 1 for config errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=b53a2527bd97a08cfe0d474565d8e82cf7c8bdbbbe7b690f88e4a356fefaf011 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_has_existing_triefacts(triefacts_root: Path) -> bool`

Return `True` if `triefacts_root` exists as a directory containing at least one `.md` file.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=699927ac70525f46f13cd69b8026fe5e3da3102e36ae1ab84a1694719543c46c body_fp=454a2773bdfe8d9a5501ac6d53a61815b27916474077775be58a4d55db78545e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_run_full_pass(*, reporter, project_root, config, model, budget, limit) -> None`

Scan, plan, optionally confirm, then run a full bootstrap sync for every in-scope file.

- `budget`/`limit`: if both are `None` in a non-interactive environment, exits with code 1.
- Prompts for confirmation in interactive mode when no cap is set.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=2954e846707299dcf1034673910e08d26cb784d3667a2d75877d11a2e254278e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_run_dry_run_diff(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Regenerate stale triefacts into `.trie/preview/` and print unified diffs against the live tree.

- `budget`: USD cap passed to `diff_project`; files exceeding it are skipped and counted.
- `limit`: maximum number of files to diff.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=17df35b7143b22bb3651c9e3571e4496066301f0b00f39213054f3b892dbda71 body_fp=f410a821fe1037c148b216a2124a86b2ea00f285f4306f5d4246032053a4ee1a source_ref=81ec453e27d219340630c14d41a7b913b703d744 -->
## `_run_single_file_sync(reporter: Reporter, file: Path, model: str | None, force: bool = False) -> None`

Sync a single source file to its triefact, writing symbols and reporting token usage.

- `file`: must exist; exits with code 1 otherwise.
- `model`: falls back to `config.models.bootstrap` when `None`.
- `force`: passed to `sync_single_file` to bypass diff-aware regen and cold-regenerate all symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=ab88ff6a5f8617fcb6bbcc42dae27974d38c2d4d9d9e8f5df2a4c2dcd0f4ad19 body_fp=ac450cf664db0e4a0e7af3fbc7e9766fc97f67aa71be4b0aa3d30d202878edb7 source_ref=81ec453e27d219340630c14d41a7b913b703d744 -->
## `_run_metadata_only_refresh(reporter: Reporter) -> None`

Re-scan the project and rewrite triefact front matter from the live store without calling the LLM.

- Skips files outside `config.triefacts.source_root`; reports them as skipped in the progress bar.
- Writes a triefact only when bytes have changed; idempotent on subsequent runs.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=c0296f53afdae836d3646b2af7059167e69e09ce2828ef92af30e3df36f33e9a body_fp=ebbb94a94980656db322e78952538e20a9c8924c022591fce31c5b50ccd48bfb source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_run_incremental_sync(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Run incremental cascade sync, removing orphan triefacts and reporting stale/cascaded file counts.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=0051558e5dd44636f47dea98a8f82c433c1de0f0d9efa31fbd1dd98e4cd9d1e1 body_fp=dee9e7adbe59215b4427eb1c0bb99e55a84441dbef73ea40406cd160ba7a55a5 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `setup_cmd(ctx, target, install_all, scope, print_only, dry_run, no_overrides, with_mcp) -> None`

Wire trie into a coding agent by installing a turn-boundary hook, tool overrides, and agent-facing docs.

- `target`: repeat to install for multiple named agents; mutually exclusive with `--all`.
- `with_mcp`: also registers the MCP server; off by default since tool overrides suffice.
- `no_overrides`: skips replacement of the agent's built-in `grep`/`read` tools.
- `scope`: `"project"` writes into the repo; `"user"` writes to `~/.<agent>/...`.
- All steps are idempotent; exits 1 if any step errors.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=9c0c752d54c3dcfa921629d39973d8145b811fdd047a21cf7002c9a974f78517 body_fp=b19f808ac0dd45a2410f0540c9629bdbeef4af2c9491787ee7b2e4b27f9f6cba source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_setup_plan(reporter, mcp_plan, hook_plan, docs_plan, override_plan=None)`

Print a merged per-target setup report covering hook, MCP (if run), tool-override, and docs install outcomes.

- `mcp_plan`: omit when MCP install was skipped; its results are merged only when present.
- `override_plan`: omit when `--no-overrides` was passed; delegates per-target rendering to `_render_override_target_block`.
- Docs section is rendered once at the end, independent of target count.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=1ede2878bb98b6df394615cdd58ab4ecae185270f43cadf83ab95df212d1565d body_fp=2ffaadced2d96cbc13faee1182b84fb9055b69f9be14bb706f1018249e27beca source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_override_target_block(reporter: Reporter, result: object) -> None`

Render one target's tool-override install outcome: a summary action line followed by per-file results indented beneath it.

- `result.action == "needs_manual_setup"`: emits a warning with `result.detail` and returns early.
- Per-file entries show action, relative path, optional description, and detail for `skipped`/`error` states.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=2205a7f7907ef86823060a286f0c58f461250f3d2a504b3afc7a48a4fd5001e9 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_format_action(action: str, path: Path | None) -> str`

Render an action label with an arrow-separated path suffix, returning just the action when path is `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=a38753c98b59bd7629ab6884ebcbe171c970dd9ccd7f9f698b45d43b589c1245 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_open_tools(reporter: Reporter) -> TrieTools`

Locate the project root and return an open `TrieTools` session tagged with `event_name="cli_call"`.

- Caller must call `.close()` on the returned `TrieTools` when done.
- Exits with code 1 if no `trie.toml` is found.
- Uses `"cli_call"` (not `"mcp_call"`) so telemetry distinguishes shelled-out CLI from MCP server calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=82ecaea31834b5e50357aadc8f414abe51f90d1ba48c631c6f82a2087cfae4e9 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_emit_envelope(envelope, *, as_json, reporter, render)`

Print an MCP tool response envelope as raw JSON or via a human-readable renderer, then exit 1 on error envelopes.

- `as_json`: dumps to stdout via `typer.echo`; skips Rich to keep output clean for agents.
- `render`: called with `(envelope, reporter)` when `as_json` is False.
- Raises `typer.Exit(code=1)` if `"error"` key is present in the envelope.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=868adb38d55c12e59d7a2b45d8f60f00fff09cafdddc5ed12610304a5621d8cd body_fp=453645d9827764deac0115740e4bd9ac655a1c6bc425dadd952a50860b320d1b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_grep(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie grep` response envelope as human-readable Rich output.

- Prints a Rich table of hits when present; falls back to fallback-envelope text and candidate table when `hits` is empty.
- Delegates error envelopes to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=bd5e442551e9a4a5c99767903ee70eb72ece12ca2970bcd78b78d7a06ac19dd0 body_fp=41f6bf0a6344fd423031220f19da47a66d453b95d8a97b8f0330a5d684ba8002 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_read(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie read` response envelope as human-readable terminal output with signature, prose, and neighbour lists.

- `envelope`: MCP-shaped dict; error key triggers `_render_error_envelope` and early return.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=fc3af28c35192dc6686d551bf13ac8695eb77b0a4a30aa3fa400b42a1197d6b6 body_fp=8e1789db99038a5d508966dc6aca1749d2bd7a53227f00d8b7ef6d7642bf6799 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_trace(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie trace` envelope as human-readable output: root symbol, node list, edge list, truncated hubs, and notes.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=fee1f6d0f34f585f3bac41e67fdd12609a376996e772ff241a5c0f7aa8ed5003 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_error_envelope(err: dict[str, object], reporter: Reporter) -> None`

Print a `{code, message, suggestion?}` error envelope in human-readable form via `reporter`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=6025553cc54eb2e7dcd1e837bf56344b75efb528380fba576e10a03cfd63bf76 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_build_grep_predicate(name, kind, scope_prefix, scope_exclude, public_only, inbound_min, inbound_max, outbound_min, outbound_max, predicate_json, reporter) -> dict[str, object]`

Assemble a `TrieTools.grep` predicate dict from individual CLI flags, merging over an optional base JSON envelope.

- `predicate_json`: parsed first as the base; individual flags override matching keys.
- Flags override JSON fields when both are supplied ("more specific wins").
- Exits with code 2 if `predicate_json` is invalid JSON or not an object.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=710fe74fe62218408cec3e4d14016d8cb6d66dacdf7ec010ff2d22cfcd21579f source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `grep_cmd(ctx, name, kind, scope_prefix, scope_exclude, public_only, inbound_min, inbound_max, outbound_min, outbound_max, predicate_json, rank_by, limit, as_json) -> None`

Find symbols in the trie graph matching a predicate; CLI mirror of the MCP `grep` tool.

- `predicate_json`: full predicate JSON object; flag values override matching fields.
- `rank_by`: `public_first` | `inbound_count` | `alphabetical`; defaults to `public_first`.
- `as_json`: emits the raw MCP envelope; output is byte-equivalent to the MCP wire response.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:read_cmd fingerprint=17492b277aded6e3ff96eab437be39b135df14a26859018d4e3d5bdce03eeb0f body_fp=12b5d9be37805b0272c12328aeff62c85373ac49714b4927f521c6f42031e469 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `read_cmd(ctx: typer.Context, qname: str, as_json: bool = False) -> None`

Fetch a symbol's triefact prose, signature, source pointer, and one-hop caller/callee neighbourhood via `TrieTools.read`.

- `qname`: fully-qualified symbol name as indexed by trie.
- `as_json`: emit raw MCP envelope JSON instead of human-readable output.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=ced5ab79dfa93d2099ff86ccc2e8965f6d822b0c9271a529188d869d5c3aa125 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `trace_cmd(ctx, qname, direction="callers", depth=2, as_json=False)`

BFS-walk the call graph from a symbol, delegating to `TrieTools.trace`.

- `direction`: `callers`, `callees`, or `both`
- `depth`: hop limit, clamped server-side by `trace_max_depth`
- `as_json`: emit raw MCP envelope instead of human-readable output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plain fingerprint=73b737045796027c85e5cc8cadae182504d8d70c294160d047c87451d9359465 body_fp=3e6c10e9d6f4e0576a7e1b63da13eca26d1086db286c9db16cb7a01870b3abe8 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_print_plain(envelope: dict[str, object], reporter: Reporter) -> None`

Render an MCP tool response envelope as indented JSON, or delegate to `_render_error_envelope` on error.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_str_cmd fingerprint=69ea560601cfa6f1a741609b0663572f95f39802e4321bb47f8708bf7dc6529d body_fp=9b312c60be23c44d37a7d3cf91312d50d971eadae1161762a099e14f11df6837 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `grep_str_cmd(ctx: typer.Context, regexp: str) -> None`

Search source file bodies with a regex and attribute hits to their enclosing symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_entry_points_cmd fingerprint=1a9f9b71faac201e98831ba75798e16ab0a9a61cf6461f80a76bede7e9b46b63 body_fp=cf101487148773c06267a12755e1044ac23f8e5cd16999d6b8930057586e482e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `grep_entry_points_cmd(ctx: typer.Context, query: str) -> None`

Find architectural entry points whose triefact prose matches a topic query.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_cmd fingerprint=4b925e05b1ef0842ffd6862a088f06f315888e9a54b2ad2ed6d7ad0b17407e4c body_fp=55600f34dd34c4e2a4a92d3ebdb80582b385f6367003b449a7c5d213e2719357 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `grep_symbol_cmd(ctx: typer.Context, sym: str) -> None`

Fuzzy-match a symbol name fragment and return the best match plus similar symbols via `TrieTools.grep_symbol`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_neighbours_cmd fingerprint=27d88a48d69a0bace10cac46278c7472e07d9febc837407321656de44beb0fdd body_fp=fc74a1ba3d581fef44c9d227658d75995e17192f4c4816440e1687e40db14bae source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `grep_symbol_neighbours_cmd(ctx: typer.Context, sym: str) -> None`

Fuzzy-match a symbol name and return trimmed metadata for its immediate callers and callees.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_cmd fingerprint=7c4c47493a79b82df8d4b2885616ef105d670c38c1e9e0ffa5b822b1973066a8 body_fp=0b968486796468c1a6d76d0fc71a3507824927d1e98c43e41b6f79c18f59d5be source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `explain_symbol_cmd(ctx: typer.Context, sym: str) -> None`

Call `TrieTools.explain_symbol` and render full prose plus a narrative of the symbol's references.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_refs_cmd fingerprint=0ac13e0a39fbbaba07077fa05a176cf6ff226f8514f824c702183d9adf388565 body_fp=45c2d67dcb3a52938210020587a6a3ebb26b117d1d25fad5b71063be205acaa1 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `explain_symbol_refs_cmd(ctx: typer.Context, sym: str) -> None`

Invoke `TrieTools.explain_symbol_references` and render callers with their prose for a symbol name or fragment.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_flow_cmd fingerprint=159e9cac61ba82f744521d2dcc8f53ec1ebd5f1aa4fbc36c96b5eae8755520ed body_fp=7dd0fd78230bd782105cc4194ab6074191ec8ede521155dd9221d4660710de7b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `trace_flow_cmd(ctx: typer.Context, symbol1: str, symbol2: str) -> None`

Find call chain(s) between two symbols via `TrieTools.trace_flow`, rendering output with `_print_plain`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_flow_cmd fingerprint=c840efc39861b94757c6288e677187040a32e2c5b69ab95bfb93600dc7a03f4c body_fp=9e77a8960e0dd11516bddb7bb9cb904bedd98084c4eef9d57fd89ecfbc8dc90f source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `explain_flow_cmd(ctx: typer.Context, symbol1: str, symbol2: str) -> None`

Trace the call chain between two symbols and narrate each step via `TrieTools.explain_flow`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_app fingerprint=0c83c10dbd09994c30dee74986deefeee9e7fbcba6d0fe9f936c328a8b332275 body_fp=dd0424d757b6fb851262f7e971db049aaae2663785ffcfabc087001a5125c39b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_app`

Typer sub-application for the `trie mcp` command group (serve, install, uninstall).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=8afc888492b438f21ef1c4eefca162f6b3a23ce234af8bb05e2e984686c7dfdd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_serve() -> None`

Run the trie MCP server over stdio by delegating to `_run_mcp_serve`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=4258aa2fb272e1e8747b707a0e4e82fc26d60ca254d37530430360069014f332 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_run_mcp_serve() -> None`

Locate the project root and launch the stdio MCP server, writing config errors to stderr to avoid corrupting the MCP protocol.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=0a6c33b03d07b5dc7a9dfcd7cc18a7f4969bf35c80ca3988275db10bd5e02537 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_install_cmd(ctx, target, install_all, scope, print_only, dry_run) -> None`

Register `trie mcp serve` as a stdio MCP server with one or more coding agents.

- `target`: agent slug(s); mutually exclusive with `install_all`.
- `scope`: `"project"` or `"user"`; controls which config file is written.
- `print_only`: print the JSON snippet without writing files.
- `dry_run`: resolve paths and show changes without writing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=e551c94237e6552233ebecf9e2e08509fb886a886eace35b28e7478b2b2781fd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_install_plan(reporter: Reporter, plan: InstallPlan) -> None`

Print each MCP install result keyed by action: preview, created, updated, skipped, or error.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_uninstall_cmd fingerprint=e0cbf3e2e0174b8f33dbe0589e2c6908d67e5f5c49961500186aab26268bab2a body_fp=8fe46d478ef9810cc83e8e70568cd7137c419f76a6864282fdc03315affd195b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_uninstall_cmd(ctx, target, uninstall_all, scope, print_only, dry_run) -> None`

Remove the trie MCP server entry from one or more agent config files.

- `target`: repeat `--target` for multiple agents; mutually exclusive with `--all`.
- `scope`: `'project'` or `'user'`; controls which config file path is targeted.
- Exits 1 if any result has `action == "error"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_uninstall_plan fingerprint=982bba634aca721cfd1aaf145aba973af33cbd7f5cb22ab4f82d6c4f8ba7a692 body_fp=0cd5d8a8397a431007ef42ef8c2b9ec3ec878e4f5a13729ea43bee7e345e4b1e source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_render_uninstall_plan(reporter: Reporter, plan: UninstallPlan) -> None`

Render a `UninstallPlan` to the terminal, mirroring `_render_install_plan` with `removed` in place of `created`/`updated`.
<!-- trie:end -->