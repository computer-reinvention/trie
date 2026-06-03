---
trie_version: 0.1.5
source: trie/cli.py
file_fingerprint: d8fb202b9deeac93286dd2c9e4b3bf28a9e4543ab08f00aa31a2df359d6c1c4d
last_synced_at: '2026-06-03T21:05:57Z'
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
<!-- trie:section symbol=trie/cli:__module__ fingerprint=d16be5917b98ff58f36f3487c349d240fc53396bc24bb9e0d8903c2f9e48f690 body_fp=10f0e1573012e0fc76e1358d4da306bc2ba6e70254a41da3bf25ef8b26e41199 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Main CLI module for trie providing comprehensive project management, triefact synchronization, and agent integration commands.

- `app`: Root Typer application with commands for init, sync, verify, plan, refresh, audit, setup, grep/read/trace
- `patch_app`: Sub-application for posting and applying edit patches against symbols  
- `mcp_app`: Sub-application for MCP server installation and stdio serving
- `console`: Rich Console instance for colored terminal output
- `_ProgressAdapter`: Bridge between sync ProgressCallback and Reporter ProgressHandle interfaces
- `_RichApplyProgress`: Rich progress reporter for patch application with threaded file processing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:app fingerprint=bd6ef12c875332ea01db62797e29cf2fb64ae5ac0be52a25d5f8aa08f5abb82c body_fp=c0d1c1eee55e99f2a10dc06d4d381e1ff1d1a7a253b539152d249ce441cb7a55 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Top-level Typer application instance that defines the trie CLI interface.

Configured with name "trie" and help text describing trie as an artefact tree that mirrors source trees with LSP-aware cascade coherence.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:console fingerprint=dff6104fc5140b6d96afa42ceddb0c4c0d1e4b0cb6686a2debb687f087a24c7e body_fp=e2c2c01956b6de43e5d529c487368909586063344bab7f6e2a55e75a75c243fe source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Creates a Rich Console instance for styled terminal output across CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=7240f20d1b3e432db5d778b116dc67f2c55ecf02f06a13c215c592b514f5bbc9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Resolves the Reporter instance from the typer Context, returning a default MEDIUM verbosity Reporter if none exists.

- Returns a default Reporter() when invoked outside normal typer dispatch (e.g., tests)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=2a082055da35a933023958cf947cba96cae1e82663b8e55faf4a477b4aadbea8 body_fp=1aac8c0aa0d749668a7c027b7bd2ea6e916558af72f93ee406ec747aa96139bd source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Adapts sync's ProgressCallback Protocol to a Reporter ProgressHandle with lazy initialization.

• Creates ProgressHandle on first `on_start` call when total count is known
• Tracks running cost differences to report per-file costs
• Bridges between sync module's progress callbacks and reporter's display layer
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=c14510df06e779a0b951076cf2cdcdef0c659fee5633432e88909b4376fd8e69 body_fp=9b1a72a920212f9432c2c4aa3f2584591dab05a7e4d1ef294ebfdd974dda96ae source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Initializes the _ProgressAdapter with a reporter, label, and resets the progress handle and running cost tracker.

- `reporter`: Reporter instance for creating the underlying ProgressHandle
- `label`: Display label for the progress bar
- `handle`: Initially None, lazily created on first `on_start` call
- `_prev_running_cost`: Tracks cumulative cost to calculate per-file deltas
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=38d28d902742473e5586cd4e13c06722e5d5096339015b40b5ff70355c49b986 body_fp=d484af0d670380586c4865913157449b5b5630c0e0162a7469639925df570774 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
_ProgressAdapter._ensure creates and enters the underlying ProgressHandle lazily on first call.

- Returns the existing handle if already initialized
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=0a0babb0cb7e0707b4b10478d10624ac2ef8b7645048e09d2b85e0aa92b652b0 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Tears down the _ProgressAdapter by exiting the underlying ProgressHandle context manager and clearing the handle reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=0551e92b9a693655ab4b5f9d5bc3e8d459cf9b102ddcad2451c29652d843496c body_fp=047c0e51caf2116e0536f9b70bafbb1902ca80a5c3218755afbb07aad6165ced source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Starts progress tracking for a file by ensuring the progress handle exists and calling its start_file method.

- **rel_path**: relative path of the file being processed
- **idx**: current file index in the batch (unused in implementation)
- **total**: total number of files, used to initialize the progress handle if needed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=d027b8d68698a0feb649e720de9c37e9de1a7b103e44b851ecb79390b6689dd9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Reports file completion to the progress bar with cost and token metrics from FileSyncResult.

• per_file_cost: computed as the delta between running_cost_usd and the previous total
• cost_usd: only passed if positive, otherwise None to avoid showing zero costs
• tokens: includes input/output counts plus cache read/write statistics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=42c5646050616548a525fc8f2fe85e0dd7825303d0c9f14d898e9e60a768456c source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Records a skipped file by forwarding to the underlying ProgressHandle if it exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=f79b5fb9407ac52eee93b63fb3438cca1fd00d566b7a1a035bec3e038702ea65 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Creates a context-managed _ProgressAdapter that bridges Reporter progress bars with sync ProgressCallback protocol.

- **adapter**: _ProgressAdapter instance that converts ProgressCallback calls to Reporter.start_progress operations
- **cleanup**: ensures adapter.close() is called to properly tear down the progress bar on context exit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=3ae553a9c7f238f7b80d985c0aa027e15c51ac29b1e281d7444eecc167631911 body_fp=2a7362fcca878752903807572d546e2ce268a98bd13ad916f775c21671a0dc2c source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Context manager that acquires a write lock for the duration of a command or exits with code 2 if contended.

- Operator-typed commands get loud failures with exit code 2 when lock is held
- Hook-driven refresh commands get queuing semantics instead
- Exit code 2 is transient (retry), exit code 1 is non-transient (fix input)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=30478076061d35f2a9a917ba0945b818725557a1425a472d66b47c3ecb27af7e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Root Typer callback that sets up global verbosity, handles --version, and initializes telemetry before dispatching to subcommands.

- Validates that --quiet and --verbose are mutually exclusive (exits with code 2 if both are set)
- Creates a Reporter with the appropriate verbosity level and stores it in ctx.obj for subcommands
- Prints version and exits if --version is provided
- Shows help and exits if no subcommand is invoked
- Calls _telemetry_bootstrap to emit a 'cli' event with the subcommand name and argv tail
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=f3a40c9f16db60e4660ec4c1670dc066e71d4e0d90c0eeafbdf048ae11362284 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Configures telemetry from trie.toml debug settings and emits a CLI invocation event.

• Silently handles missing config files since `trie init` runs before trie.toml exists
• Emits "cli" event with subcommand name and argv tail for usage tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=1d3815663e939a183a3615fa14bce2303216da8109575c962b16755709c45c26 body_fp=1e721f00f18c1320eebcf87ead4914d8ef86ea5ea1286ebf80f02b2ecd3e7c5d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Create trie.toml config, update .gitignore, build symbol graph, optionally install pre-commit hook, and offer to run setup.

- `root`: Project directory to initialize (defaults to current directory)
- `force`: Skip Python project detection and overwrite existing config
- `install_hooks`: Install pre-commit hook (prompts in interactive mode if None)
- `run_scan`: Build symbol graph after config creation (default True)

Materializes `.trie/graph.db` when scanning, acquires write lock to prevent concurrent initialization, reports success/failure for each step, displays next-step recommendations, and offers to run `trie setup` interactively.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=5099d8aaf3feec3989a06e12a790bd7622b9cff2ccd17a0557f36de69be14319 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Checks if stdin is a tty to determine if interactive prompts are safe.

• Returns `True` when stdin is connected to a terminal
• Returns `False` for non-interactive environments (CI, pipes, redirected input)
• Gracefully handles environments where `sys.stdin.isatty()` is unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=d790cb8c8d4f3ea375951462dfe2095143e9a766cb0eb0e6b95154f3237889ca source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Context manager that does nothing; used to conditionally skip status indicators.

Implements the context manager protocol with no-op enter/exit methods, allowing code to use `with _NoOpStatus():` when a status indicator should be skipped while maintaining the same control flow structure as when a real status manager is used.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=08d221cc7a674a413ae90dd3f89994efdfbea0d74604458cd0f0198abd7e45ed source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
_NoOpStatus.__enter__ returns self to implement the context manager protocol as a no-op.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=7fcaa154ca4cba7b928bdfd4e5d6ed7394387fc74c2aa227a857e1321eeb9cf3 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
`_NoOpStatus.__exit__` implements the context manager exit protocol, taking exception parameters and returning None.

- Always returns None regardless of exception arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=373611a9d3e4483138772bfb37fc6df782949064514db26f320d72889ab86b34 body_fp=096967cbfb059eb00835ca8b327e555e0b3ad960d1a1450c36a0341c921cbd9b source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Scans project for drift, computes either incremental or full-bootstrap worklist, and displays estimated cost before any LLM work begins.

- Auto-detects incremental mode (stale files + cascade) vs full re-bootstrap based on existing triefacts unless `--all` forces full mode
- Uses free token counting API rather than generation to estimate costs
- Performs drift check first but continues on drift (informational, not a gate)
- Acquires write lock to ensure consistent store snapshot during planning
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=404a8a489ac3dff8f8a175632d07fbefd00f73f95de59264aab035c20b6af2c9 body_fp=b1be616430a9b201bca45907bd2e1500a648b462e02f4479997676e0a0b1812a source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Runs bidirectional drift check and exits with code 1 if triefacts have diverged from source code.

- Detects both code→triefact drift (source changed without regeneration) and triefact→code drift (tampered sections or deleted symbols)
- Designed for pre-commit hooks and CI environments - no LLM calls, no database writes
- Same drift detection logic used by `plan` and `sync` commands, exposed as standalone verification gate
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=b2588d0ec23978e9e8f4b7732d307584d0bad5d7227cee2cf553c7f4c21bf287 body_fp=5be4484291527e6b893fe68513dde9387fbf0c1357a0d9d0ad8741b1d3d163f3 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Probe whether another trie process holds the project's write lock, exiting 2 if contended.

- Designed for pre-commit hooks to detect racing `trie refresh` or `trie sync` operations
- Exit code 0: lock is free or project has no trie.toml
- Exit code 2: lock held by another process, caller should retry
- Uses acquire-then-immediately-release pattern that never blocks or interferes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:refresh_cmd fingerprint=9650ac7742d77ff500365c3ea2b7d0c224376d86b3bf256763d5591ecf94d749 body_fp=58c5251674c536348ab3153343f6290b736a1642297dc6a39a408e048985574e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Brings graph and triefacts up to date with the working tree as an agent turn hook.

- `before_turn`: cheap freshness gate (no-op unless HEAD/mtimes moved)  
- `after_turn`: post-turn sweep picking up agent edits (default mode)
- Uses refresh lock to serialize concurrent runs and coalesce rapid contests
- Runs tail pass to handle queued requests that arrived during execution
- Requires git repository (fails if `git rev-parse HEAD` unavailable)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=39c12516433ffd01deaf7e6d4dc9d72f23e588c64a16997bc815624ddc2aeb44 body_fp=6210bfc8bd3005b4ba7ce4ea835a58ed3d8960672545486790012ff7076f858e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders a single status line for a refresh operation outcome.

- Prints "already fresh" if nothing changed
- Shows sync statistics and cost when files were actually refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=5756d1b7e32899d278d6ffb9c3d820058831de9e933722d87f89c248c1fbabcf body_fp=213f5531341311c835c7814ef9e9223a1c86a702a3f28839dae069dd206598bc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Summarise telemetry logs with MCP usage, sync activity, retries, and CLI invocations.

• `--log`: Path to debug.jsonl file (defaults to configured debug.log_path)
• `--compare`: Render side-by-side comparison with deltas (candidate vs baseline)
• `--json`: Output as JSON instead of human-readable format
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=82168e8ec7edc73bd791d28e3cfc2b65fbcde418535265e5ac087321c1cee77f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Resolves the audit log path for `trie audit` command.

• Falls back through: explicit `--log` flag → config's `debug.log_path` → `./debug.jsonl`
• Returns absolute paths, resolving relative config paths against project root
• Allows cross-project audit by not requiring trie.toml when explicit path given
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=34ad2b8e98bf414eaf8a533a8b75ac271dbae3edca2b2d73052de585e4b60969 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a colored breakdown of files scanned by status and symbols/edges count.

- Renders new/updated/unchanged/removed file counts with color coding
- Falls back to "no files in scope" when no categorizable files exist
- Shows total symbols and edges written to the database file
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=a3fad1a65c7d23db83f84ab7550e57151bb55d0228a974dae2657c75b00605bd source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a bootstrap plan summary showing model, file count, total cost, and top 10 files with their symbol counts and estimates.

- Displays total estimated cost formatted to 4 decimal places
- Shows first 10 plan items with file path, symbol count, score, and per-file cost
- Adds "… and N more" footer when plan exceeds 10 files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=7d25e63d4726fe5f82eb8328587f26dafdb4888e59a3a3fec7f1f3399867bea1 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Print incremental sync plan emphasizing actual work order and symbol-level impact.

- Displays files grouped by directly stale vs cascaded, ordered by execution priority
- Shows symbol-level breakdown (how many symbols will hit LLM vs total documented)
- Lists orphan triefacts that would be removed, truncated at 10 items
- Preserves bootstrap ranking within each execution tier for cost visibility
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_REASON_LABELS fingerprint=ec482101fe58286effe17023a43479424dfb2b828cee44ffb3f99e8b9adbf8bb body_fp=123a827e0262d8e3a181380a9897a2c5da3dc4d08143cfb49405fb3a26ff4584 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Maps StaleReason enum values to human-readable labels for drift reporting.

- Used by `_print_drift_detail` to render per-file drift items in a user-friendly format
- Keys are StaleReason enum members; values are descriptive strings for CLI output
- Provides consistent labeling across all drift-related commands (verify, plan, sync)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=698bcad70ac9d737c38314e3d26f0d384ff76f3b86cdcad26f47397e3c262b21 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders drift check items grouped by triefact file with colored status indicators and indented issue details.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=44a3fd1a2641e2f490a4bf9aee8fdbe0559b48519186574ee8b46b64c96516b8 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Checks triefact tree coherence and reports drift, returning True if clean.

- `exit_on_drift`: When True, raises `typer.Exit(1)` on drift (for `verify` command); when False, warns and continues (for `plan`/`sync`)
- Returns False if drift detected, True if tree is coherent
- Reports detailed drift items when verbosity is MEDIUM or higher
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=304f6c1245eb2f8cd864c080d949ec805171293731bbbcda0fbea9cafab47691 body_fp=3f672de8c54242678e8e778f9b5783fbeebfcf5cc0fb852367ecc489d0e9e0ad source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Generate or refresh triefacts across multiple modes determined by CLI flags.

Supports single-file sync, dry-run preview, metadata-only refresh, forced full re-pass, and auto-detected first-run vs incremental modes. Validates flag combinations, acquires a write lock, then delegates to specialized helper functions based on the selected mode. All modes run drift detection first and handle configuration loading consistently.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=0a62d5928c91a171e378bd5fab17ad701335a6b91b910ea6c795000ccad9b267 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Returns True if the triefacts directory exists and contains at least one markdown file.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=699927ac70525f46f13cd69b8026fe5e3da3102e36ae1ab84a1694719543c46c body_fp=7c17976d70c9682150ff0443869009d4a52025874736d78de244ea3f280fd319 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Executes first-run or forced full re-pass bootstrap sync for all in-scope files.

- Scans project to build symbol graph and token estimation plan
- Requires interactive confirmation or explicit budget/limit for cost control
- Reports actual vs estimated costs and files synced/skipped due to caps
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=aef73997fa835e6c4cb57d5089fed793e34be8fbd933335d2ba9ff6d1f88985f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Implements `trie sync --dry-run` by regenerating stale triefacts into `.trie/preview/` and printing unified diffs.

- **model**: Uses `models.bootstrap` if not overridden
- **budget/limit**: Caps LLM cost and file count
- **output**: Prints per-file diffs or notes fingerprint-only changes
- **exit**: Reports total cost and skipped files due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=17df35b7143b22bb3651c9e3571e4496066301f0b00f39213054f3b892dbda71 body_fp=c35712090a9c65e3a57bcfb675c014574380f58867ea42c70aa201a7be19af8b source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Sync a single file specified by `--file` option in the `sync` command.

- `file`: Path to the source file to sync; must exist
- `model`: Optional override for the configured bootstrap model  
- `force`: Bypass diff-aware path and cold-regenerate all symbols in the file
- Validates file existence and loads config from file's parent directory
- Creates LLM client and opens graph store, then calls `sync_single_file`
- Reports success with triefact path, symbol counts, and token usage details
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=ab88ff6a5f8617fcb6bbcc42dae27974d38c2d4d9d9e8f5df2a4c2dcd0f4ad19 body_fp=eb1f4ef332c83227c8796367c61641906b4bf42a0777d7799d2ca2aaa79f1ee2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Refreshes triefact front matter from the live store without LLM calls, designed for post-graph-change updates.

- Rescans project to pick up new edges from resolver changes
- Updates ref counts and defines entries for each in-scope triefact
- Skips files outside source_root and no-ops when metadata already matches
- Reports changed count vs total processed files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=c0296f53afdae836d3646b2af7059167e69e09ce2828ef92af30e3df36f33e9a body_fp=ee9900d814666a7f8585022e33341b21b417de10bc75485d95a21eb7a0aebeff source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Executes incremental sync after drift detection, regenerating only stale triefacts and their cascade dependencies.

- Loads project config and resolves model from `--model` flag or `config.models.cascade`
- Calls `run_incremental` to detect drift and regenerate affected triefacts within budget/limit constraints
- Reports orphan triefact cleanup, sync counts (directly stale vs cascaded), and actual cost
- Exits early with success message if no work needed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=0051558e5dd44636f47dea98a8f82c433c1de0f0d9efa31fbd1dd98e4cd9d1e1 body_fp=2c404ef25f92f2844eb0bf457b69f65575ebc192368579bb130b4198137c29af source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Integrates trie into coding agents by installing hooks, tool overrides, and documentation.

Orchestrates multiple install steps in sequence:
- MCP server registration (optional, via `--with-mcp`)
- Turn-boundary hooks for automatic refresh after agent edits
- Tool wrapper overrides that replace agent built-in `grep`/`read` with trie equivalents
- Agent-facing documentation (TRIE.md and pointer updates)

Target auto-detection resolves which agents to configure; `--target` or `--all` override this. The process is idempotent - re-running safely overwrites existing configurations. Agents without automation support emit manual setup instructions.

- `--no-overrides`: Skip tool wrapper installation, leave agent built-ins unchanged
- `--scope`: Install in project directory or user agent configs
- `--dry-run`/`--print-only`: Preview mode without file modifications
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=9c0c752d54c3dcfa921629d39973d8145b811fdd047a21cf7002c9a974f78517 body_fp=00d3d6b6fe11ea59d9146ce4c158ed543a0cdce62c72547fc54a4a6c833a62d5 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders a combined setup plan report grouping MCP, hook, and override results by target with a separate docs section.

- Groups results by target slug, showing each target's MCP/hook/override outcomes indented under its display name
- Emits manual setup warnings and JSON previews inline where applicable
- Renders docs section separately since it's target-independent
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=1ede2878bb98b6df394615cdd58ab4ecae185270f43cadf83ab95df212d1565d body_fp=ba615a58540e306c9db7664acb2bee499d1e8cd67c59c83657c1c5497905c5a2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders tool-override install outcomes for a single agent target within the setup command output.

- Prints summary line showing override action status
- Lists per-file outcomes indented beneath the summary  
- Handles manual setup notices for unsupported agent harnesses
- Uses Rich markup for consistent visual formatting with hook install output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=33f2a0af34ece204faf67aa6c95cef95a890aaeba6f93c9a8f92484e6ee2a603 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Formats an installation action result as a display string with optional path suffix.

- Returns `action` alone when `path` is None, otherwise `"action → path"`
- Used by setup command renderers for consistent MCP and hook line formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=21c17059efeb9d659493f91f06cd3aea63b05d387ef3446792e9d5aa97a2a34e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Resolves project root from trie.toml and returns TrieTools instance configured for CLI telemetry.

• Returns TrieTools with event_name="cli_call" to distinguish CLI usage from MCP calls in audit logs
• Caller must close() the returned instance to release SQLite handle
• Raises typer.Exit(1) if trie.toml not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=cbf61b9c556d479acf0bd9aed32381243ee9cfdf00343a76c3dd1ad871c43a26 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints envelope as raw JSON or via provided renderer, exits with code 1 on errors.

- `as_json=True`: dumps to stdout without ANSI codes for agent parsing
- `as_json=False`: delegates to the provided renderer function
- Error envelopes always render through the renderer for human diagnostics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_patched_tag fingerprint=dc648bd9f208afe7454d79f5eebafca65d77f7014569d3999b97bf3f93928efe body_fp=9be02189078c57ce4a27212a4894416ac6166c915a7c4f9a97ad4f402d2f6f8b source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Returns a yellow `[patched: N]` tag for count > 0, empty string otherwise.

Used in grep and trace output rendering to visually mark symbols with pending edit patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=132ccb4bbce0becd4dd07923c83487b62bfacf65d4d6de4322cf4cd215509709 body_fp=369e31a5a8bafb00a4d8a963697ddbfb898a214f7a33ef8e0d30086879f4e613 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders human-readable output for `trie grep` command results.

- Displays symbol hits as a Rich table with qname, kind, location, and one-liner columns
- Falls back to candidate matches table when no exact hits found
- Shows pending patch counts as yellow tags on qnames
- Routes errors to `_render_error_envelope` for consistent error formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=efa646ea62572923bc7a181b70207498948525b24907f473c1698ecc1450813b body_fp=f4212416e628a2324798bb4255ba8e1ed2ec936a6376bf1959bca4c05ce4e9a2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders human-readable output for `trie read` command responses, displaying symbol metadata, prose, pending patches, and caller/callee relationships.

- **envelope**: MCP response dict containing qname, signature, source_pointer, prose, callers, callees, pending_patches, and notes
- **reporter**: Console output handler for styled text rendering

The function formats the symbol's qualified name and signature at the top, followed by prose content (or a fallback message if missing), any pending patches with their origins and notes, then caller and callee lists with one-liners, and finally any warning notes. Error responses are delegated to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=1af973f434ca837af6bd3bf7f5f4a14871b62746089ef1d6845c6f30cd474b15 body_fp=08321fb0893b819f18aa414844c848fb130b915d9321331e40e4d9e000bc7bc8 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders human-readable output for `trie trace` command responses.

- Displays root symbol with its one-liner description if present
- Lists all nodes in the trace with qnames, one-liners, and pending patch indicators
- Shows edges with directional arrows (→ for outbound, ← for inbound)
- Reports truncated hubs and any diagnostic notes from the trace operation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=29e06ccfb00bd8f211685d85fb3a46d9de82717423194f02d0f6dea1b11b353f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders standardized error envelope from MCP tools into human-readable form via Reporter.

- **err**: error envelope dict containing `code`, `message`, and optional `suggestion`
- **reporter**: Reporter instance for formatted console output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=7f410b69de496539d7948c4e8a86a399d45babc4ab7286234153ca799a704dc5 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Assembles a search predicate dictionary from CLI flags for the `trie grep` command.

- `predicate_json`: Base JSON predicate; individual flags override matching fields
- Constructs nested `inbound_count`/`outbound_count` objects when min/max bounds provided
- Exits with code 2 on invalid JSON to distinguish from other error types
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=8c43a494fcb2e3b2468d86052eaee440d5a34a0ab7bad2281fbdf8a0f1dbeb87 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
CLI command that finds symbols matching predicates through the TrieTools.grep method.

- **name**: substring match against symbol's local name (case-insensitive)
- **kind**: restrict to function, class, method, constant, module, or any
- **scope_prefix**: filter by file path prefix (e.g. 'trie/')
- **scope_exclude**: file path prefixes to skip (repeatable flag)
- **public_only**: exclude symbols starting with underscore
- **inbound_min/max**: filter by incoming edge count (find hubs/leaves)
- **outbound_min/max**: filter by outgoing edge count
- **predicate_json**: full predicate as JSON (same shape as MCP grep)
- **rank_by**: sort order (public_first, inbound_count, alphabetical)
- **limit**: maximum hits to return (default 10)
- **as_json**: emit raw MCP envelope instead of human-readable table
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:read_cmd fingerprint=17492b277aded6e3ff96eab437be39b135df14a26859018d4e3d5bdce03eeb0f body_fp=41b92f87259a62729a7fa288c1c6f67e81bbe8b977a16b0cb5e76ca379eee672 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
CLI command for reading a symbol's prose plus its immediate callers and callees.

- Opens TrieTools session and calls `tools.read(qname)` to retrieve symbol metadata
- Emits response as JSON (`--json`) or human-readable format via `_render_read`
- Mirror of the MCP `read` tool for agents that prefer CLI over MCP protocol
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=4163cf535b50888684695017b4ba5cf75abd1a6767961b77d6fca069e7504675 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Trace call graph from a symbol outward up to specified depth, mirroring MCP `trace` tool.

- `qname`: fully-qualified symbol name to start tracing from
- `direction`: "callers", "callees", or "both" (default: "callers")
- `depth`: maximum BFS depth, clamped by config trace_max_depth (default: 2)
- `as_json`: emit raw MCP envelope as JSON instead of human-readable summary
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plain fingerprint=73b737045796027c85e5cc8cadae182504d8d70c294160d047c87451d9359465 body_fp=994c0fd50f2844e2c0f9a2ea3a1614065754533fc0327dcc5f83c98110dc988f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders MCP tool response envelopes as human-readable JSON output. Checks for error envelopes first and delegates to `_render_error_envelope`, otherwise prints the full envelope as formatted JSON.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_str_cmd fingerprint=69ea560601cfa6f1a741609b0663572f95f39802e4321bb47f8708bf7dc6529d body_fp=32602f2d14ff61b11bc5c3093b20ce8b4e49bc6ad04e029a06be8020567af6d6 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
CLI command that searches source file bodies with a regex pattern and attributes hits to their enclosing symbols.

- Uses TrieTools.grep_str to perform the search
- Always renders output in human-readable format (no --json option)
- Closes the tools connection in a finally block to ensure cleanup
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_entry_points_cmd fingerprint=1a9f9b71faac201e98831ba75798e16ab0a9a61cf6461f80a76bede7e9b46b63 body_fp=86af0c27c7a6ee9cd58f91e6ab7c43338c2f7f72d5911942fa08110a2f8a58fb source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Provides the `trie grep-entry-points` CLI command that searches for architectural entry points by topic.

- `query`: Topic or concept to match against symbol prose in entry points
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_cmd fingerprint=4b925e05b1ef0842ffd6862a088f06f315888e9a54b2ad2ed6d7ad0b17407e4c body_fp=7570b063a93abbedf36eed837046ca587a43cf8378044121ad264e59e4f39882 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Executes fuzzy symbol name lookup via TrieTools.grep_symbol and renders results as structured JSON.

- Uses `_open_tools` to create TrieTools session with project root from nearest trie.toml
- Calls `tools.grep_symbol(sym)` to find best match and similar symbols for the fragment
- Always renders output via `_print_plain` (structured JSON format, not human tables)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_neighbours_cmd fingerprint=27d88a48d69a0bace10cac46278c7472e07d9febc837407321656de44beb0fdd body_fp=9d5189effab527a6b20a26e377befda85dac6b252def86aca18964d988e5b485 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Implements `trie grep-symbol-neighbours` CLI command that performs fuzzy symbol lookup and returns immediate caller/callee metadata.

- Takes a symbol name fragment to fuzzy-match against the graph
- Calls `TrieTools.grep_symbol_and_neighbours()` to get the symbol plus trimmed neighbor data  
- Renders output in plain text format via `_print_plain`
- Example: `trie grep-symbol-neighbours sync_single_file`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_cmd fingerprint=7c4c47493a79b82df8d4b2885616ef105d670c38c1e9e0ffa5b822b1973066a8 body_fp=bd3a5aaf5b8a40edcb9e36b25463ffde7536321d2ed6e3c14d7c1426568e75be source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Provide detailed explanation of a symbol including its prose and reference narrative via CLI.

CLI command that wraps the MCP `explain_symbol` tool for terminal use. Takes a symbol qname or name fragment, opens a TrieTools session, calls the explain method, and renders the result in human-readable format. Always uses plain text output rather than JSON.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_refs_cmd fingerprint=0ac13e0a39fbbaba07077fa05a176cf6ff226f8514f824c702183d9adf388565 body_fp=60ca4e736ae7a3d5c74b1de6715f7bb1c002287675b35a5e08a4673fc252d227 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Typer command that explains how a symbol is used by its callers with their prose.

- Calls `TrieTools.explain_symbol_references()` with the provided symbol name or fragment
- Always outputs human-readable format (no JSON option unlike other commands)
- Uses generic `_print_plain` renderer for output formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_flow_cmd fingerprint=159e9cac61ba82f744521d2dcc8f53ec1ebd5f1aa4fbc36c96b5eae8755520ed body_fp=a7f3fdfb0e79f548335e637502e92fbe5646e047ae3b433494946addc1fe7065 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
CLI command that finds call chains between two symbols via TrieTools.trace_flow.

- **symbol1**: starting symbol qualified name or name fragment
- **symbol2**: target symbol qualified name or name fragment
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_flow_cmd fingerprint=c840efc39861b94757c6288e677187040a32e2c5b69ab95bfb93600dc7a03f4c body_fp=74baf831dd85839c025a3ced1a9564864a5ffd4c631f0fafd2a844471fce7119 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
CLI command that traces call chains between two symbols and narrates each step.

- `symbol1`: starting symbol qualified name or name fragment
- `symbol2`: target symbol qualified name or name fragment

Calls `TrieTools.explain_flow` and renders output using the generic plain-text renderer.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_app fingerprint=a01ba84281db5613dd9598b44b9572c2f52e7bf4a145def4e8140840006383da body_fp=0297250842674ecd94a570ce93159fdff3eade05ffef0210ab52062e894e45f4 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Typer CLI application for managing edit patches against symbols.

- Provides subcommands: create (post patch), preview (show apply plan), apply (execute patches with cascade), list (show pending), drop (remove patches)
- Configured with `no_args_is_help=True` to show help when invoked without subcommands
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress fingerprint=88a444531b547feca55d4fda3ad1c55db173b88633bd149775faf38391c33b66 body_fp=fb6070f71b83ae157c59be4141d94e3edd3701f121e2b744d694cb24c26495bc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Rich-formatted progress reporter for apply_patches operations. Prints structured, thread-safe progress output with visual indicators for each stage.

- Methods called from worker threads, so output naturally interleaves
- verbose flag controls symbol-level detail display
- Uses Rich markup for colored icons and indented hierarchy
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.__init__ fingerprint=1c6ad7264d460fcc4f36e9524e2f5bc1f7ee6bc638d01590eca5e0f665ce4ae7 body_fp=a0f71d7355dc8f9d45ff40d01c4795e5e7c2dee41ec64dd2187f8e2ecf0b3a8e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Initializes _RichApplyProgress with a Rich console and optional verbose flag for detailed patch application reporting.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.stage fingerprint=00a0e5b25af2600c917827df1316312556da14518c19c948a17c6b4f8105174f body_fp=c1f5d9c07788f968d33182a77f2fbc33f519f9ba6937ea7b51665f4d886ed1a9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a stage header message with rich formatting to the console.

- Formats the message with bold cyan styling and a vertical bar prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_start fingerprint=1c9e2af52741b8ee459d4101628f36bc16552d1d167b3afdfa1cb25db55ae2d3 body_fp=8d280285ae0ba5941fbf5ddad5830d282b0415f9f869ef4d7b1963b0cc946fa7 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a file processing start message with file path and symbol count.

- `fp`: relative file path being processed
- `symbols`: number of symbols in the file that will be patched
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_symbol fingerprint=1fc9ef71af9d3e0f90361d13907c1059d449a1913c2acbac2a945251d0e7c24d body_fp=af56c37705685b73b7b01c3a996620bda3a9787bc1bb91fc6cfe71495f652a1d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints per-symbol progress during patch application when verbose mode is enabled.

- `qn`: qualified name displayed in cyan with indented bullet point
- `notes`: patch notes truncated to 100 chars and printed with "note:" prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_generate fingerprint=132b41245a185b2af3aacb3c8c3a18c12c5b09ff296437cde359f630862c6105 body_fp=e46e1034cc995556ab2ad34cc7aba5e7826c44445b1217c55696f5edc8e6b7c2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints generation progress for `_RichApplyProgress` when verbose mode is enabled.

- Only executes when `self.verbose` is `True`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_fixup fingerprint=26be5de5ef710ac328e60f9b6eea26539ebdc8ecf0c1fd70a4eb97604c07d115 body_fp=354f09f9566eeae08907a9a556595c9a875c735e1f8e767ee2d747ff96371cf9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a yellow gear icon with LSP fixup iteration number and diagnostic count.

- **iteration**: Zero-based fixup pass number
- **count**: Number of diagnostics found in this iteration
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_prose fingerprint=12b3c9eda87bd14def97bc9c6c65327a7d23a45803d936cae5ab3330703ecb93 body_fp=b0639bc61593899e87e2d508c8526ec8c715256200e4a5c909ebacb3cbdf35df source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a verbose prose generation indicator for the given symbol qname.

- Only prints when `verbose=True` was set during `_RichApplyProgress` construction
- Displays an indented line with a pen icon and the qname being processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_done fingerprint=be1e14003b12fc05817ca35f7302feae8c628647d0b7cffb7cef9fef388f8c11 body_fp=e83badb76dd48eb5f9f74567e452bf20d0c6fb5799a937051c55f5132cd99bcc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a completion status line for a file in `_RichApplyProgress` patch application progress.

- `ok`: determines green checkmark (success) vs red X (failure) icon
- `error`: failure message displayed in red when `ok` is False
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.refresh fingerprint=fa057109cbf67e48f2ca72e4736ffb716951fd64ecb1ac03f8c0afce10bfb4e2 body_fp=91777d45c485266abd077f253512020c315913a09ada1f89e811c761171e90d4 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a refresh indicator for the given file path during patch apply progress reporting.

- `fp`: File path being refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.verify fingerprint=9bb6073c0083b530e9d8a61ec3fe90bde21961bdcbb397e39268aa6d65db357c body_fp=88843d1669232469dd7a92f0b73d40fc967e947a1c92e8d576021241cb8f1664 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Prints a green checkmark indicating the project is consistent after patch application. Called by `apply_patches` at the end of its verification phase.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_cmd fingerprint=97c3989c1279036d82787e6b55d900e97ff19c4f008d5b5b52660f2e7a211a62 body_fp=5cb5eb6bb93dd80e3e457cd217e7b80fb4b78fe633a6404600f36b7ef797d9db source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Creates a fire-and-forget edit patch against a symbol in the trie graph store.

- Validates that the symbol exists in the graph database before creating the patch
- Generates a unique session ID for tracking related patches together
- Returns the patch ID after successful creation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_apply_cmd fingerprint=9cf11ef78cef5d13cb4857a8bc0ecc6754882d3d1d57682b241f6af79429ae30 body_fp=2cfec0d03c76b1ca7e5123e335fac1b16000a12f3ab244f9442352bd826db597 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Executes all pending patches by merging them, generating updated source and prose, cascading changes, and committing results.

- Uses configured edit model unless overridden via `--model`
- Shows detailed per-symbol progress when `--verbose` is enabled
- Exits with code 1 if patch application fails
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_preview_cmd fingerprint=5ecdfc45e6454337fb86ebe6924f33a93e19cdc782fe0ed3e553ac2199acaae7 body_fp=f94dacf003102922486a8b112e1d9578db6a53a1d39651c0ec99b1c7bc16c0ae source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Previews what `trie patch apply` would execute without running it.

Displays a Rich table showing pending patches grouped by symbol with cascade indicators. Reports zero patches with an info message if none are pending.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_list_cmd fingerprint=3320086dd19705392e7935182ebf8ff2761a7be1d93602c799e4c048768843ac body_fp=04722740f783475e858e2a74290cc11369139ec464073478b409c2edf2a78a41 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
List all pending patches in a table showing symbol names and patch counts.

Opens the graph store, retrieves all symbols with pending patches, and displays them in a Rich table with qualified names and patch counts per symbol. Exits with no output if no patches exist.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_drop_cmd fingerprint=95a11bc5f09447c761ae2a5fa72fd823863458efc160412c95f950625e8e589d body_fp=4e37256bfbe8e2c702ec6d71b823d88f72ca93e4ccaf39bd99ee27f4d9f755e0 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Drop pending patches from the graph store by qname, session ID, or all patches.

- Exactly one of the three selection criteria must be provided
- Exits with code 1 if no selection criteria specified or config not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_app fingerprint=0c83c10dbd09994c30dee74986deefeee9e7fbcba6d0fe9f936c328a8b332275 body_fp=58e6c3b276840293bcf335b4fd33dfabda523fafd5261b08491b0cb0134c417e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Typer sub-application for MCP (Model Context Protocol) server management commands.

- Provides `install`, `uninstall`, and `serve` subcommands for agent integration
- Shows help when invoked without arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=70fc24d5899708cd24382a7202d5b17748a63d20953b59c486d5f62a5ccc2d1d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Run the trie MCP server over stdio as a Typer command.

Delegates to `_run_mcp_serve()` for the actual server implementation.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=73c11dc03b04976bf9a2fc8e80637299abc238437977e34a37ba8ed763f61b6e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Starts the MCP server over stdio after validating the project configuration.

- Locates trie.toml and validates config structure without using its contents
- Prints config errors to stderr to avoid corrupting the MCP protocol stream
- Delegates to run_mcp_stdio for actual server implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=56b8a3b5140b45725192474cf54754a68433b6176f397804f637922c8ff8f7e2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Registers trie MCP server with one or more coding agents through their config files.

- `target`: specific agent names to install for (can be repeated)
- `install_all`: install for all known agents, skipping detection
- `scope`: "project" writes to current repo, "user" writes to ~/.<agent>/
- `print_only`: shows config snippet without writing files
- `dry_run`: shows file paths and changes without writing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=c59c0e62f61e8a6cbca9c3bc43e2245f6354f57fcf5c071f544b259056b7a493 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders human-readable output for MCP installation results, displaying per-target status and details.

- Formats each result with the target's display name and appropriate colored status indicators
- Shows JSON snippets for preview actions and error messages for failed operations
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_uninstall_cmd fingerprint=e0cbf3e2e0174b8f33dbe0589e2c6908d67e5f5c49961500186aab26268bab2a body_fp=0419c682c13f9af03e4f29b59768509b1970615524ec8ec4da9a6953dd9c1540 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Unregisters the trie MCP server from agent configuration files.

• Validates mutually exclusive flags and scope options
• Delegates uninstall execution to `mcp_run_uninstall` with validated parameters
• Renders the uninstall plan showing removed entries per target
• Exits with code 1 if any uninstall operation encounters errors
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_uninstall_plan fingerprint=982bba634aca721cfd1aaf145aba973af33cbd7f5cb22ab4f82d6c4f8ba7a692 body_fp=2191ea5bf60f2c3f0b81ff5998d0d99449fd63a3c5851c65644d3559c8e5b85f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 -->
Renders the output for `trie mcp uninstall` by iterating through uninstall plan results and printing status messages for each target using the Reporter console interface.

- Mirrors the install renderer with `removed` status replacing `created`/`updated`
- Prints JSON preview for dry-run mode, success/error messages for actual operations
- Shows skipped targets with explanatory detail when no action was needed
<!-- trie:end -->