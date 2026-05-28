---
trie_version: 0.1.5
source: trie/cli.py
file_fingerprint: d8fb202b9deeac93286dd2c9e4b3bf28a9e4543ab08f00aa31a2df359d6c1c4d
last_synced_at: '2026-05-28T21:10:20Z'
defines:
- kind: module
  qualified_name: trie/cli:__module__
  lines: 1-2811
- kind: constant
  qualified_name: trie/cli:app
  lines: 73-76
- kind: constant
  qualified_name: trie/cli:console
  lines: 77-77
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 80-86
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 89-134
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 97-101
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 103-107
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 109-112
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 114-115
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 117-130
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 132-134
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 138-143
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 147-178
- kind: function
  qualified_name: trie/cli:_root
  lines: 182-220
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 223-235
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 239-360
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 363-370
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 373-378
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 374-375
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 377-378
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 382-481
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 485-497
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 501-551
- kind: function
  qualified_name: trie/cli:refresh_cmd
  lines: 555-665
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 668-682
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 686-746
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 749-765
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 768-785
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 788-799
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 802-868
- kind: constant
  qualified_name: trie/cli:_REASON_LABELS
  lines: 871-878
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 881-892
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 895-926
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 930-1058
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 1061-1067
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 1070-1134
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 1137-1182
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 1185-1218
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 1221-1278
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 1281-1330
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 1334-1508
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 1511-1581
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 1584-1610
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 1613-1617
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 1632-1650
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 1653-1677
- kind: function
  qualified_name: trie/cli:_patched_tag
  lines: 1680-1684
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 1687-1757
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 1760-1822
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 1825-1877
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 1880-1892
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 1895-1957
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 1961-2064
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 2068-2099
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 2103-2145
- kind: function
  qualified_name: trie/cli:_print_plain
  lines: 2155-2169
- kind: function
  qualified_name: trie/cli:grep_str_cmd
  lines: 2173-2188
- kind: function
  qualified_name: trie/cli:grep_entry_points_cmd
  lines: 2192-2207
- kind: function
  qualified_name: trie/cli:grep_symbol_cmd
  lines: 2211-2226
- kind: function
  qualified_name: trie/cli:grep_symbol_neighbours_cmd
  lines: 2230-2245
- kind: function
  qualified_name: trie/cli:explain_symbol_cmd
  lines: 2249-2264
- kind: function
  qualified_name: trie/cli:explain_symbol_refs_cmd
  lines: 2268-2283
- kind: function
  qualified_name: trie/cli:trace_flow_cmd
  lines: 2287-2303
- kind: function
  qualified_name: trie/cli:explain_flow_cmd
  lines: 2307-2323
- kind: constant
  qualified_name: trie/cli:patch_app
  lines: 2331-2335
- kind: class
  qualified_name: trie/cli:_RichApplyProgress
  lines: 2339-2391
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.__init__
  lines: 2349-2351
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.stage
  lines: 2353-2354
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_start
  lines: 2356-2357
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_symbol
  lines: 2359-2365
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_generate
  lines: 2367-2369
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_fixup
  lines: 2371-2374
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_prose
  lines: 2376-2379
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_done
  lines: 2381-2385
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.refresh
  lines: 2387-2388
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.verify
  lines: 2390-2391
- kind: function
  qualified_name: trie/cli:patch_create_cmd
  lines: 2395-2423
- kind: function
  qualified_name: trie/cli:patch_apply_cmd
  lines: 2427-2472
- kind: function
  qualified_name: trie/cli:patch_preview_cmd
  lines: 2476-2510
- kind: function
  qualified_name: trie/cli:patch_list_cmd
  lines: 2514-2542
- kind: function
  qualified_name: trie/cli:patch_drop_cmd
  lines: 2546-2578
- kind: constant
  qualified_name: trie/cli:mcp_app
  lines: 2586-2593
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 2598-2600
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 2603-2613
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 2617-2686
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 2689-2704
- kind: function
  qualified_name: trie/cli:mcp_uninstall_cmd
  lines: 2708-2783
- kind: function
  qualified_name: trie/cli:_render_uninstall_plan
  lines: 2786-2806
incoming_refs: 91
outgoing_refs: 122
---
<!-- trie:section symbol=trie/cli:__module__ fingerprint=d16be5917b98ff58f36f3487c349d240fc53396bc24bb9e0d8903c2f9e48f690 body_fp=5b23e74cd68861f7bc16b3d47b732f6128777f4f83dcca97fd745ea9a0b40c39 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `trie/cli.py`

Define and wire the `trie` CLI: all subcommands, progress adapters, renderers, and the Typer app entry point.

- `app`: root `typer.Typer` instance; `patch` and `mcp` sub-apps are added as nested typers.
- `console`: shared `rich.Console` used by all reporters.
- Exit code 1: config/logic error (non-transient). Exit code 2: write-lock contention (transient, retry).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:app fingerprint=bd6ef12c875332ea01db62797e29cf2fb64ae5ac0be52a25d5f8aa08f5abb82c body_fp=07cea146910642a73fb4b751051bd6c70c0e9d0a32db4a2ee87b2ee8a0a9f8bd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `app = typer.Typer(name="trie", ...)`

Root Typer application instance that all `trie` subcommands are registered against.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:console fingerprint=dff6104fc5140b6d96afa42ceddb0c4c0d1e4b0cb6686a2debb687f087a24c7e body_fp=f8e23a47fcc2e7dffa55b92e35093b5febd3f4f19331709061f4e27e00996435 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `console = Console()`

Module-level Rich `Console` instance shared across all CLI output functions.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=6da6abc4aac5b0a32d39df4b4a74b4451c7a5de9890e0e2d677e4dc54bbdcc23 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_get_reporter(ctx: typer.Context) -> Reporter`

Retrieve the `Reporter` stored on the Typer context, falling back to a default MEDIUM `Reporter` when none is set.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=2a082055da35a933023958cf947cba96cae1e82663b8e55faf4a477b4aadbea8 body_fp=ab72199342cd15c5f6fab100c77c718d24c5e87e19950564721d370b971bc8f0 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_ProgressAdapter`

Bridge sync's `ProgressCallback` protocol to a `Reporter` `ProgressHandle`, lazily initialising the handle on the first `on_start` call.

- `handle`: created on first `on_start`; `None` until then.
- `on_done`: derives per-file cost from the running total delta before forwarding token/symbol stats.
- `close`: exits the `ProgressHandle` context manager and clears the reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=c14510df06e779a0b951076cf2cdcdef0c659fee5633432e88909b4376fd8e69 body_fp=694082be8623298df6fbe56c00d9400f30480e2fa4c412b82a576adb9ce9385c source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_ProgressAdapter.__init__(self, reporter: Reporter, label: str)`

Initialise a `_ProgressAdapter`, storing the reporter and label and setting the progress handle to `None`.
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
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=908beda1fb317bf42bcdc06e0e172709f12e3fe68fb9e34b02cf6d8ba13a0a09 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_root(ctx, version, quiet, verbose)`

Typer root callback that configures verbosity, stores a `Reporter` on `ctx.obj`, and emits the telemetry bootstrap before any subcommand runs.

- `--quiet` / `--verbose` are mutually exclusive; exits 2 if both given.
- `--version` prints `trie <version>` and exits 0.
- No subcommand: prints help and exits 0.
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
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=373611a9d3e4483138772bfb37fc6df782949064514db26f320d72889ab86b34 body_fp=59949cf35045f1828c8d9d6049e4c5c2790ea414f58f642a3b6681a4d4c17489 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `plan_cmd(ctx, model, all_) -> None`

Scan the project, check drift, count tokens, and print the worklist with estimated LLM cost.

- `model`: overrides `config.models.bootstrap` for token counting.
- `all_`: forces full re-bootstrap view even when triefacts already exist.
- Uses `count_tokens` only (no `messages.create`); safe to run before `trie sync`.
- Auto-selects incremental vs full-bootstrap based on whether triefacts exist.
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
<!-- trie:section symbol=trie/cli:refresh_cmd fingerprint=9650ac7742d77ff500365c3ea2b7d0c224376d86b3bf256763d5591ecf94d749 body_fp=b6e668a8143646a19ebd3dfdd595419289caaa55a0d4b7232b72e7c3a2ca4c81 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `refresh_cmd(ctx, before_turn, after_turn, model) -> None`

Bring the graph and triefacts up to date with the working tree, serialising concurrent hook invocations via the write lock.

- `--before-turn`: cheap gate; full sync only if HEAD or mtimes moved.
- `--after-turn`: post-turn sweep; default when neither flag is given.
- Contended lock: queues a tail pass rather than failing, coalescing concurrent hook fires.
- Exits 1 outside a git repo or on config error; requires `git rev-parse HEAD`.
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
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=a418f447e5350e881a7b5aa8e39a13e15297d5bb5a97f7e78e55ad824d6a7d9f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool`

Run an offline drift check and report results, optionally aborting on drift.

- `exit_on_drift`: when `True`, raises `typer.Exit(1)` on drift; when `False`, warns and returns `False`.
- Returns `True` if the triefact tree is clean, `False` if drift was found and `exit_on_drift` is `False`.
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
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=699927ac70525f46f13cd69b8026fe5e3da3102e36ae1ab84a1694719543c46c body_fp=ea822b0d7771e297fc8c4efacaa00b30921e559fc03fffe4db7d97f00cc623cd source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_run_full_pass(*, reporter, project_root, config, model, budget, limit) -> None`

Scan the project, build a bootstrap plan, confirm with the user if no cap is set, then run full bootstrap with streaming progress.

- `budget`: USD cap; skips files once cumulative cost reaches this.
- `limit`: max number of files to sync.
- Exits code 1 in non-interactive mode when neither `budget` nor `limit` is provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=cf0858e102fe74cc46bec51be845b8d2a948c755802e21ce1ff8b7c194a32e10 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_run_dry_run_diff(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Regenerate stale triefacts into `.trie/preview/` and print unified diffs against the live tree.

- `budget`: USD cap passed to `diff_project`; stops early when reached.
- `limit`: file count cap passed to `diff_project`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=17df35b7143b22bb3651c9e3571e4496066301f0b00f39213054f3b892dbda71 body_fp=f410a821fe1037c148b216a2124a86b2ea00f285f4306f5d4246032053a4ee1a source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
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
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=c0296f53afdae836d3646b2af7059167e69e09ce2828ef92af30e3df36f33e9a body_fp=70ee567dd043930e0346fd1fa1c730d35642be867aaaa2ca3c270e7f126863dd source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_run_incremental_sync(*, reporter: Reporter, model: str | None, budget: float | None, limit: int | None) -> None`

Run incremental cascade sync, reporting orphan removals, stale counts, and actual cost.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=0051558e5dd44636f47dea98a8f82c433c1de0f0d9efa31fbd1dd98e4cd9d1e1 body_fp=48c8e7d69ebac7e076f860601d75c5d838c8136e1a81c8aa4d141f7135fbb4a9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `setup_cmd(ctx, target, install_all, scope, print_only, dry_run, no_overrides, with_mcp) -> None`

Wire trie into one or more coding agents: turn-boundary hook, tool overrides, and agent-facing docs.

- `target`: repeat `--target` for multiple agents; auto-detected when omitted
- `install_all`: set up every known agent, skipping per-target detection
- `scope`: `"project"` writes into the repo; `"user"` writes to `~/.<agent>/`
- `no_overrides`: skip replacing the agent's built-in `grep`/`read` with trie wrappers
- `with_mcp`: also run `trie mcp install`; off by default since tool overrides suffice
- Idempotent: existing matching files are reported `skipped`; drift is overwritten
- Exits 1 if any install step produces an `"error"` result
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
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=589f44a30a25f5bbeb59e41d513b307850a081a01300e4e6a2c2b0765e7d16ce source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_open_tools(reporter: Reporter) -> TrieTools`

Resolve the project root and return an open `TrieTools` session tagged with `event_name="cli_call"`.

- Caller must call `.close()` on the returned `TrieTools` when done.
- Exits with code 1 if no `trie.toml` is found.
- Uses `"cli_call"` event name so telemetry distinguishes CLI from MCP invocations.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=82ecaea31834b5e50357aadc8f414abe51f90d1ba48c631c6f82a2087cfae4e9 source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `_emit_envelope(envelope, *, as_json, reporter, render)`

Print an MCP tool response envelope as raw JSON or via a human-readable renderer, then exit 1 on error envelopes.

- `as_json`: dumps to stdout via `typer.echo`; skips Rich to keep output clean for agents.
- `render`: called with `(envelope, reporter)` when `as_json` is False.
- Raises `typer.Exit(code=1)` if `"error"` key is present in the envelope.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_patched_tag fingerprint=dc648bd9f208afe7454d79f5eebafca65d77f7014569d3999b97bf3f93928efe body_fp=94fa94373ffb4a556299391ac247f114f7b1400a22a43b403384bf2a2fb1d90f source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `_patched_tag(count: int) -> str`

Return a Rich-formatted yellow `[patched: N]` tag string, or empty string when `count` is zero or negative.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=132ccb4bbce0becd4dd07923c83487b62bfacf65d4d6de4322cf4cd215509709 body_fp=2670e38d498db2f35e5d6f5168f00c35fe9e105bd0311551b418bb2b9115f2b6 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `_render_grep(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie grep` response envelope as human-readable Rich output.

- Hits present: prints a 4-column table (qname, kind, location, one-liner) with pending-patch tags.
- No hits: prints fallback kind/note and a candidate-matches table if available.
- Error envelope: delegates to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=efa646ea62572923bc7a181b70207498948525b24907f473c1698ecc1450813b body_fp=b8461ab86119db7df644bfbc3f6e07539de07c09ad4d93895590544290647380 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `_render_read(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie read` response envelope as human-readable terminal output.

- Delegates to `_render_error_envelope` on error envelopes.
- Prints qname, signature, source pointer, prose, pending patches, callers, callees, and notes in order.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=1af973f434ca837af6bd3bf7f5f4a14871b62746089ef1d6845c6f30cd474b15 body_fp=680120b1712e70cf4e4b740bb00d4e2b73005cfc673b6cf38fd71f536ff04445 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `_render_trace(envelope: dict[str, object], reporter: Reporter) -> None`

Render a `trie trace` MCP envelope in human-readable form: root symbol, nodes with one-liners, edge list, truncated hubs, and notes.

- `envelope`: MCP trace response; error envelope short-circuits to `_render_error_envelope`.
- Nodes with `has_pending_patches` are tagged with a yellow `[patched: 1]` label.
- Edges render directionally (`→` for out, `←` for in) using the `direction` field.
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
<!-- trie:section symbol=trie/cli:patch_app fingerprint=a01ba84281db5613dd9598b44b9572c2f52e7bf4a145def4e8140840006383da body_fp=05e2d7d11f6dcf7a0daa6cc590c76939e3daaf6a02f53ba401939da3a337e6be source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `patch_app`

Typer sub-application grouping the `patch` family of subcommands under `trie patch`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress fingerprint=88a444531b547feca55d4fda3ad1c55db173b88633bd149775faf38391c33b66 body_fp=c9b12eac92b82868ad853cac88c1cc02a5c12cb180e42ae727c15df6f9ca3dfd source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress(console: Console, *, verbose: bool = False)`

Rich-backed progress reporter satisfying the `apply_patches` progress protocol, printing structured per-stage and per-file lines to the console.

- `verbose`: when `False`, suppresses per-symbol and prose-generation detail lines.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.__init__ fingerprint=1c6ad7264d460fcc4f36e9524e2f5bc1f7ee6bc638d01590eca5e0f665ce4ae7 body_fp=4bdb70675874557fd222179c20e9d687e24631a1d788a336980186d90598f248 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.__init__(self, console: Console, *, verbose: bool = False)`

Initialise a `_RichApplyProgress` with a Rich `Console` and optional verbose flag.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.stage fingerprint=00a0e5b25af2600c917827df1316312556da14518c19c948a17c6b4f8105174f body_fp=38d1e06d2b5de63ccebdb8999aabae81019e6648b618b706b4d9364c055bc4c3 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.stage(self, msg: str) -> None`

Print a bold cyan section header to the `_RichApplyProgress` console.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_start fingerprint=1c9e2af52741b8ee459d4101628f36bc16552d1d167b3afdfa1cb25db55ae2d3 body_fp=08587f7457e130666c49ddb7f7f50c46564a5ff0f3aa765ad2472bc862d9ced3 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_start(self, fp: str, symbols: int) -> None`

Print a `_RichApplyProgress` progress line for a file beginning processing, showing its path and symbol count.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_symbol fingerprint=1fc9ef71af9d3e0f90361d13907c1059d449a1913c2acbac2a945251d0e7c24d body_fp=247720eee2816d4939c4a85b57c7d12a4c13561065c8b39cecfa5a87a77563e6 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_symbol(self, qn: str, notes: list[str]) -> None`

Print a symbol name and truncated notes to the console; no-op when `verbose` is false.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_generate fingerprint=132b41245a185b2af3aacb3c8c3a18c12c5b09ff296437cde359f630862c6105 body_fp=695d12dce1ba8defcd55e36e9c81343e87212bff09a65b2af855d176b7e1e1cc source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_generate(self) -> None`

No-op unless verbose; currently emits nothing even in verbose mode.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_fixup fingerprint=26be5de5ef710ac328e60f9b6eea26539ebdc8ecf0c1fd70a4eb97604c07d115 body_fp=3f12cea583268843d0391953b4e4a353b43077452683c71fc17952df437c57ec source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_fixup(self, iteration: int, count: int) -> None`

Print a `_RichApplyProgress` LSP fixup iteration line showing the iteration number and diagnostic count.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_prose fingerprint=12b3c9eda87bd14def97bc9c6c65327a7d23a45803d936cae5ab3330703ecb93 body_fp=bdb9193973e64a45383f8618f3905b3671acd2b3cf343b9305902ca839c29d08 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_prose(self, qn: str) -> None`

Print a prose-update line for a symbol when `_RichApplyProgress` verbose mode is active.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_done fingerprint=be1e14003b12fc05817ca35f7302feae8c628647d0b7cffb7cef9fef388f8c11 body_fp=7dc5b7a88939b29925d9ddcfbca02123ee5cbae4dc031af6c5c1da1e37079b89 source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.file_done(self, fp: str, ok: bool, error: str | None = None) -> None`

Print a green check or red cross for a completed file, with optional error text.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.refresh fingerprint=fa057109cbf67e48f2ca72e4736ffb716951fd64ecb1ac03f8c0afce10bfb4e2 body_fp=06fbcf997fe991fd89fd0b023d0772050a8bb5277758ac2165b1b8c79e38f52e source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.refresh(self, fp: str) -> None`

Print a refresh indicator line for a file path to the `_RichApplyProgress` console.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.verify fingerprint=9bb6073c0083b530e9d8a61ec3fe90bde21961bdcbb397e39268aa6d65db357c body_fp=a4e20c4a40d2c2ab1ade79b4980cf5fd1d4578e8328d7e1c9d54ad7d9b4aef2e source_ref=344c66a5effe71a97c7cf20c9e1661b2d92aebe9 -->
## `_RichApplyProgress.verify(self) -> None`

Print a "project consistent" confirmation line to the `_RichApplyProgress` console.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_cmd fingerprint=97c3989c1279036d82787e6b55d900e97ff19c4f008d5b5b52660f2e7a211a62 body_fp=ba2cc75cd21a3fa98b832fd4269d940b773df5da2c15750ce63964010f17e200 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `patch_create_cmd(ctx, qname, note, reason) -> None`

Post a fire-and-forget edit patch against a named symbol in the graph store.

- `qname`: must exist in the graph; exits 1 if not found.
- `reason`: why the cascade needs to know about the change; optional, defaults to empty string.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_apply_cmd fingerprint=9cf11ef78cef5d13cb4857a8bc0ecc6754882d3d1d57682b241f6af79429ae30 body_fp=4bc04cf9ef2534a47c1255e605cbab479d072bc621b11a6678df61a59d3aff92 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `patch_apply_cmd(ctx: typer.Context, model: str | None, verbose: bool) -> None`

Merge all pending patches, generate updated source and prose, cascade to neighbours, and commit.

- `model`: overrides `config.models.edits`; defaults to configured edit model.
- Exits 1 if `apply_patches` returns `ok=False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_preview_cmd fingerprint=5ecdfc45e6454337fb86ebe6924f33a93e19cdc782fe0ed3e553ac2199acaae7 body_fp=8d75373f0ad615eabc484c30efef2afb4b23decf6208d6171760979b69f88c95 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `patch_preview_cmd(ctx: typer.Context) -> None`

Show a dry-run table of what `trie patch apply` would do without executing it.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_list_cmd fingerprint=3320086dd19705392e7935182ebf8ff2761a7be1d93602c799e4c048768843ac body_fp=3f334b877e1bfa93fa62457fc6eb05bfb03bb441bef45bddf68a6ec9dbc08604 source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `patch_list_cmd(ctx: typer.Context) -> None`

List all pending patches as a Rich table showing each symbol's qname and patch count.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_drop_cmd fingerprint=95a11bc5f09447c761ae2a5fa72fd823863458efc160412c95f950625e8e589d body_fp=ee65646570c6c0c214e5eaf89a6a6b23452bc5de3d91f4929ca99c01ee4aec6b source_ref=a60457021a22d5090cab0f0443fdd6525e7ba75a -->
## `patch_drop_cmd(ctx, qname, session_id, all) -> None`

Drop pending patches filtered by symbol name, session ID, or all at once.

- `qname`: drop patches for one symbol; mutually exclusive with `session_id`/`all`.
- `session_id`: drop patches recorded under a specific session.
- `all`: drop every pending patch in the store.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_app fingerprint=0c83c10dbd09994c30dee74986deefeee9e7fbcba6d0fe9f936c328a8b332275 body_fp=dd0424d757b6fb851262f7e971db049aaae2663785ffcfabc087001a5125c39b source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_app`

Typer sub-application for the `trie mcp` command group (serve, install, uninstall).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=8afc888492b438f21ef1c4eefca162f6b3a23ce234af8bb05e2e984686c7dfdd source_ref=c8af07ada00c77f292b050874bbc0b6b597f3910 -->
## `mcp_serve() -> None`

Run the trie MCP server over stdio by delegating to `_run_mcp_serve`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=91e0b4c3951e8ceec442022392bd36823073f9b755bece499dbaced3b8fc7208 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
## `_run_mcp_serve() -> None`

Load project config and start the trie MCP server over stdio.

- Config errors print to stderr (not stdout) to avoid corrupting the MCP protocol.
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