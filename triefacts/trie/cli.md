---
trie_version: 0.1.9
source: trie/cli.py
file_fingerprint: 52c53e032d7dbe333d37e2b814e706bbbb7d989ac2e77c24c47bc8967d6089bb
last_synced_at: '2026-07-25T11:02:26Z'
defines:
- kind: module
  qualified_name: trie/cli:__module__
  lines: 1-4283
- kind: constant
  qualified_name: trie/cli:app
  lines: 77-80
- kind: constant
  qualified_name: trie/cli:console
  lines: 81-81
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 84-90
- kind: function
  qualified_name: trie/cli:_cli_session_id
  lines: 93-113
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 116-188
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 124-129
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 131-136
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 138-141
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_plan
  lines: 143-155
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_section
  lines: 157-166
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 168-169
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 171-184
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 186-188
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 192-197
- kind: function
  qualified_name: trie/cli:_activity_progress
  lines: 201-229
- kind: class
  qualified_name: trie/cli:_JsonlProgress
  lines: 232-278
- kind: method
  qualified_name: trie/cli:_JsonlProgress.__init__
  lines: 253-254
- kind: method
  qualified_name: trie/cli:_JsonlProgress._emit
  lines: 256-260
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_start
  lines: 262-265
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_done
  lines: 267-275
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_skip
  lines: 277-278
- kind: function
  qualified_name: trie/cli:emit_jsonl_event
  lines: 281-291
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 295-326
- kind: function
  qualified_name: trie/cli:_root
  lines: 330-368
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 371-383
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 387-508
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 511-518
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 521-526
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 522-523
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 525-526
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 530-647
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 651-663
- kind: function
  qualified_name: trie/cli:status_cmd
  lines: 667-786
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 790-840
- kind: function
  qualified_name: trie/cli:refresh_cmd
  lines: 844-1002
- kind: function
  qualified_name: trie/cli:_refresh_progress
  lines: 1006-1027
- kind: function
  qualified_name: trie/cli:_emit_freshness_json
  lines: 1030-1047
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 1050-1071
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 1075-1135
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 1138-1154
- kind: function
  qualified_name: trie/cli:intent_cmd
  lines: 1158-1208
- kind: function
  qualified_name: trie/cli:index_cmd
  lines: 1212-1236
- kind: function
  qualified_name: trie/cli:diff_cmd
  lines: 1240-1490
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 1493-1510
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 1513-1524
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 1527-1593
- kind: constant
  qualified_name: trie/cli:_REASON_LABELS
  lines: 1596-1603
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 1606-1617
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 1620-1651
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 1655-1812
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 1815-1821
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 1824-1895
- kind: function
  qualified_name: trie/cli:_refresh_index_quietly
  lines: 1898-1905
- kind: function
  qualified_name: trie/cli:_report_sync_errors
  lines: 1908-1929
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 1932-1977
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 1980-2013
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 2016-2073
- kind: function
  qualified_name: trie/cli:_run_roles_only_sync
  lines: 2076-2115
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 2118-2182
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 2186-2402
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 2405-2475
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 2478-2504
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 2507-2511
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 2526-2544
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 2547-2571
- kind: function
  qualified_name: trie/cli:_patched_tag
  lines: 2574-2578
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 2581-2651
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 2654-2741
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 2744-2796
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 2799-2811
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 2814-2876
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 2880-2983
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 2987-3054
- kind: function
  qualified_name: trie/cli:_render_read_dispatch
  lines: 3057-3070
- kind: function
  qualified_name: trie/cli:_render_read_source
  lines: 3073-3082
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 3086-3128
- kind: function
  qualified_name: trie/cli:blast_radius_cmd
  lines: 3132-3162
- kind: function
  qualified_name: trie/cli:_render_blast_radius
  lines: 3165-3195
- kind: function
  qualified_name: trie/cli:_print_plain
  lines: 3205-3219
- kind: function
  qualified_name: trie/cli:grep_str_cmd
  lines: 3223-3249
- kind: function
  qualified_name: trie/cli:find_cmd
  lines: 3253-3282
- kind: function
  qualified_name: trie/cli:write_cmd
  lines: 3286-3326
- kind: function
  qualified_name: trie/cli:_render_write
  lines: 3329-3338
- kind: function
  qualified_name: trie/cli:_render_find
  lines: 3341-3356
- kind: function
  qualified_name: trie/cli:grep_entry_points_cmd
  lines: 3360-3375
- kind: function
  qualified_name: trie/cli:grep_symbol_cmd
  lines: 3379-3394
- kind: function
  qualified_name: trie/cli:grep_symbol_neighbours_cmd
  lines: 3398-3413
- kind: function
  qualified_name: trie/cli:explain_symbol_cmd
  lines: 3417-3438
- kind: function
  qualified_name: trie/cli:explain_symbol_refs_cmd
  lines: 3442-3463
- kind: function
  qualified_name: trie/cli:trace_flow_cmd
  lines: 3467-3483
- kind: function
  qualified_name: trie/cli:explain_flow_cmd
  lines: 3487-3503
- kind: constant
  qualified_name: trie/cli:patch_app
  lines: 3511-3515
- kind: class
  qualified_name: trie/cli:_RichApplyProgress
  lines: 3519-3571
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.__init__
  lines: 3529-3531
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.stage
  lines: 3533-3534
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_start
  lines: 3536-3537
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_symbol
  lines: 3539-3545
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_generate
  lines: 3547-3549
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_fixup
  lines: 3551-3554
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_prose
  lines: 3556-3559
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_done
  lines: 3561-3565
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.refresh
  lines: 3567-3568
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.verify
  lines: 3570-3571
- kind: function
  qualified_name: trie/cli:patch_create_cmd
  lines: 3575-3633
- kind: function
  qualified_name: trie/cli:patch_create_batch_cmd
  lines: 3637-3751
- kind: function
  qualified_name: trie/cli:patch_create_symbol_cmd
  lines: 3755-3797
- kind: function
  qualified_name: trie/cli:patch_delete_symbol_cmd
  lines: 3801-3828
- kind: function
  qualified_name: trie/cli:patch_rename_symbol_cmd
  lines: 3832-3861
- kind: function
  qualified_name: trie/cli:patch_apply_cmd
  lines: 3865-3915
- kind: function
  qualified_name: trie/cli:patch_preview_cmd
  lines: 3919-3962
- kind: function
  qualified_name: trie/cli:patch_list_cmd
  lines: 3966-4008
- kind: function
  qualified_name: trie/cli:patch_drop_cmd
  lines: 4012-4050
- kind: constant
  qualified_name: trie/cli:mcp_app
  lines: 4058-4065
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 4070-4072
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 4075-4085
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 4089-4158
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 4161-4176
- kind: function
  qualified_name: trie/cli:mcp_uninstall_cmd
  lines: 4180-4255
- kind: function
  qualified_name: trie/cli:_render_uninstall_plan
  lines: 4258-4278
incoming_refs: 91
outgoing_refs: 159
---
<!-- trie:section symbol=trie/cli:__module__ fingerprint=d16be5917b98ff58f36f3487c349d240fc53396bc24bb9e0d8903c2f9e48f690 body_fp=10f0e1573012e0fc76e1358d4da306bc2ba6e70254a41da3bf25ef8b26e41199 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Main CLI module for trie providing comprehensive project management, triefact synchronization, and agent integration commands.

- `app`: Root Typer application with commands for init, sync, verify, plan, refresh, audit, setup, grep/read/trace
- `patch_app`: Sub-application for posting and applying edit patches against symbols  
- `mcp_app`: Sub-application for MCP server installation and stdio serving
- `console`: Rich Console instance for colored terminal output
- `_ProgressAdapter`: Bridge between sync ProgressCallback and Reporter ProgressHandle interfaces
- `_RichApplyProgress`: Rich progress reporter for patch application with threaded file processing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:app fingerprint=bd6ef12c875332ea01db62797e29cf2fb64ae5ac0be52a25d5f8aa08f5abb82c body_fp=c0d1c1eee55e99f2a10dc06d4d381e1ff1d1a7a253b539152d249ce441cb7a55 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Top-level Typer application instance that defines the trie CLI interface.

Configured with name "trie" and help text describing trie as an artefact tree that mirrors source trees with LSP-aware cascade coherence.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:console fingerprint=dff6104fc5140b6d96afa42ceddb0c4c0d1e4b0cb6686a2debb687f087a24c7e body_fp=e2c2c01956b6de43e5d529c487368909586063344bab7f6e2a55e75a75c243fe source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Creates a Rich Console instance for styled terminal output across CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=6a81fd6366ce2ab0fe15313c84f131e2dfc0e44a12c799be0c174b7dd13febf6 source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=util -->
Resolve the `Reporter` stored on `ctx.obj` by the root callback, falling back to a default `MEDIUM` reporter when none is set.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_cli_session_id fingerprint=dcf3fe8c7e922ef3d9466b25f8ca9207e6ab499a2182dd92a3538dbda5f6aa23 body_fp=b366a089840eb64d5fd80d72a2b8002334fc0e1d86a0c4f31a791d34bcfcc85b source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=util -->
Generates a stable session ID for CLI patch operations, reused across multiple invocations.

- Returns `TRIE_SESSION_ID` environment variable if set
- Otherwise persists a 12-character UUID in activity database for project-wide reuse
- Ensures `trie patch --session drop` works by maintaining consistent session identity
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=461508833971d6960227589e60e8d0554cca8d9567c3036ade7cdbf2512b7a95 body_fp=441186a4466e461e3d32a2f9e639160f821a075ab40c9811045341078e50ca35 source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=util -->
Bridges sync's ProgressCallback Protocol to a Reporter ProgressHandle with lazy initialization.

- Creates underlying ProgressHandle on first `on_start` call to avoid requiring total upfront
- Tracks per-file cost delta by comparing running costs across files
- Thread-safe via internal lock protecting handle initialization
- Prints worklist summary and section separators at MEDIUM+ verbosity
- Delegates file progress events (start, done, skip) to the underlying handle when present
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=62d7f3387263067099a16c5c411db665b3dabb0d0c2701008d99dd22a9a9d982 body_fp=20812b8efc8c28b2a799159dd09984d718a0d1de6177efe6a440eab285948a32 source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=util -->
Initialise `_ProgressAdapter` with a `Reporter`, a display label, a null `ProgressHandle`, a running-cost accumulator, and a threading lock.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=67aef789d4a34e8f4c519362a59b70a41784bc0e2039ff8ee536353e1ab334ac body_fp=2b9ab181186d3a4784511cf0c24bbd7afe3afc3c240577d1b3875950f4836ebc source_ref=085640f358eb2ab2e288a4afb6fcf64a4d2c2fb5 role=util -->
_ProgressAdapter._ensure creates and enters the underlying ProgressHandle lazily on first call.

- Returns the existing handle if already initialized
- Thread-safe via internal lock
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=0a0babb0cb7e0707b4b10478d10624ac2ef8b7645048e09d2b85e0aa92b652b0 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Tears down the _ProgressAdapter by exiting the underlying ProgressHandle context manager and clearing the handle reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_plan fingerprint=3566ccad9e5759fea947fdc6b8c297970c97a7799fcbb38f5da54fb81da4c43b body_fp=ba599faa9f925a95321ad3f61dfd3172b23e3778eec398f8108a520cb2be3ad9 source_ref=fedc9d376ebe9fb7982ec359446446aec13ddf21 role=util -->
Prints a sync worklist summary before any file processing begins in `_ProgressAdapter`.

- `direct`: count of directly stale files
- `cascade`: count of files pulled in by the cascade
- Skips output when verbosity is below MEDIUM or total is zero
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_section fingerprint=ae4688be43ab22bbc7b9daf029a1af7eb1c021910f566633cf30240275e849f8 body_fp=b04721d507b543f4d4017b6eaeb0f640571887e2fdf558d6ebe0e3ed18bb439e source_ref=fedc9d376ebe9fb7982ec359446446aec13ddf21 role=util -->
Prints a section separator line with label and count before each file group.

- Skips output when verbosity is below MEDIUM or count is zero
- Routes through progress handle when available, otherwise directly to reporter console
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=34f538a7492b05dc2bf2f4087401ea296cd9a705571e3b4bf4aa7d16635d9a6b body_fp=0a39b6196711286e94aa605e42551927fbe86774933e915e0ee3522ec8df21f9 source_ref=6a32793dd5d15de513aca8021c43ef229e3559ac role=util -->
Starts progress tracking for a file by ensuring the progress handle exists and calling its start_file method.

- **rel_path**: relative path of the file being processed
- **idx**: current file index in the batch (unused in implementation)
- **total**: total number of files, used to initialize the progress handle if needed
- **cascade**: whether this file is being processed due to cascade logic
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=d027b8d68698a0feb649e720de9c37e9de1a7b103e44b851ecb79390b6689dd9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Reports file completion to the progress bar with cost and token metrics from FileSyncResult.

• per_file_cost: computed as the delta between running_cost_usd and the previous total
• cost_usd: only passed if positive, otherwise None to avoid showing zero costs
• tokens: includes input/output counts plus cache read/write statistics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=42c5646050616548a525fc8f2fe85e0dd7825303d0c9f14d898e9e60a768456c source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Records a skipped file by forwarding to the underlying ProgressHandle if it exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=f79b5fb9407ac52eee93b63fb3438cca1fd00d566b7a1a035bec3e038702ea65 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Creates a context-managed _ProgressAdapter that bridges Reporter progress bars with sync ProgressCallback protocol.

- **adapter**: _ProgressAdapter instance that converts ProgressCallback calls to Reporter.start_progress operations
- **cleanup**: ensures adapter.close() is called to properly tear down the progress bar on context exit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_activity_progress fingerprint=a726b6afa59c2f96e691e9c76681f54e58b530b04a54883ce643507000603e4b body_fp=54130f75f53bb5a67927197d760d97bb5447f55889a0e4b510ca22f77713b6ff source_ref=84c720dde0db098bca20b772035551888e51bdc6 role=util -->
Context manager that provides progress reporting mirrored to both Rich console and shared activity state.

• Yields a ProgressCallback that routes to both the Rich progress bar and `.trie/status.json` + `activity.jsonl`
• Advances the attention-store watermark after sync/refresh operations complete (best-effort)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress fingerprint=f08debf0678c64626af5cd8e2f16669e3e9a31a522c14583d4e991d64749ef94 body_fp=52ae8873a80503a64877712ca8cdccb30e9df4cdb08cfec7f63d540c27e5188c source_ref=6a32793dd5d15de513aca8021c43ef229e3559ac role=util -->
Emits structured JSON Lines progress events to a stream for machine consumption.

Implements the ProgressCallback protocol by writing one JSON object per line to stdout (or a specified stream). Designed for hosts that drive trie as a subprocess and need to parse progress in real time rather than scraping Rich terminal output.

• **Event schema**: Each line contains `{"kind": "start"|"done"|"skip", ...}` with file progress data
• **Immediate flush**: Lines are flushed after each write so pipe readers see events in real time
• **Machine-readable counterpart**: to `_ProgressAdapter` which renders Rich progress bars for humans
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.__init__ fingerprint=4ed2aa9e0869d49d8e23949ed8110d89b7a871df3e40583ca4a3255f3e640612 body_fp=63fd935cc1fa9dd3745982c537ce8aaabb5aa5257899ac296642bec1da5e848d source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=model -->
Initialize _JsonlProgress with an output stream, defaulting to stdout if not provided.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress._emit fingerprint=ef26c79f59223ced602854e80b0eb04c17df7245ec17fdecd03c03779caa872a body_fp=0216a14f743c027f049b097cb1f60372f5b07a7de955275a0c25355a6741a6f4 source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=util -->
Serializes `_JsonlProgress` event payload to JSON and immediately flushes to the stream.

- `payload`: Event data containing `kind` field plus event-specific attributes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_start fingerprint=74eaca981cfa70b628b1cc1cc5426cc694fcfebb59fbf12062bea307de95476f body_fp=30e18f5ca426383e4109b470151fdf9deef07f52a7c6455995529fc2ac9b31c3 source_ref=6a32793dd5d15de513aca8021c43ef229e3559ac role=util -->
Emits a `start` JSONL event for a file beginning processing with current index and total count.

- `cascade`: whether the file is being processed due to cascade propagation rather than direct staleness
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_done fingerprint=3d84dfc675811299240d4290075310a4604fadec0ae7979b800b7a010db19e3d body_fp=1541a4ba51b93db1a0203cbe9c5fe80be1f15795b42ebf033051f567df6d7900 source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=util -->
Emits a JSONL "done" event when _JsonlProgress completes processing a file.

- `result`: extracts `symbols_generated` for the event payload
- `running_cost_usd`: cumulative cost across all files processed so far
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_skip fingerprint=2bbfaf11160d7d62cb1a5ed009bfba8e930785a96ecae21c175c3c2296531599 body_fp=421272821e56cdccde6876e3dba8d8fa647db367209d4271ddf361834e2adde7 source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=util -->
Emits a skip event to the JSON-Lines stream when a file is skipped during progress tracking.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:emit_jsonl_event fingerprint=376721b7cfba875cf18dba24b9a39760deddb6042f3ef16032fa0f771876b330 body_fp=5b492e582788825bae5ca1e14dc61955a64ac91288db0655f656aae19f8ade43 source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=util -->
Emits a single JSONL event to stdout or specified stream for machine-readable progress reporting.

- `payload`: event dictionary to serialize as JSON
- `stream`: output target, defaults to `sys.stdout`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=3ae553a9c7f238f7b80d985c0aa027e15c51ac29b1e281d7444eecc167631911 body_fp=2a7362fcca878752903807572d546e2ce268a98bd13ad916f775c21671a0dc2c source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Context manager that acquires a write lock for the duration of a command or exits with code 2 if contended.

- Operator-typed commands get loud failures with exit code 2 when lock is held
- Hook-driven refresh commands get queuing semantics instead
- Exit code 2 is transient (retry), exit code 1 is non-transient (fix input)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=859e3d6404385b287b81cd355ad8cafa07d0c07eae791ae3813f22012c2a8aab source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=entrypoint -->
Typer root callback that initialises the shared `Reporter`, enforces mutual exclusivity of `--quiet`/`--verbose`, prints the version, and bootstraps telemetry before any subcommand runs.

- `--quiet` / `-q`: sets `Verbosity.MUTE`; mutually exclusive with `--verbose`, exits 2 if both given.
- `--verbose` / `-v`: sets `Verbosity.VERBOSE`.
- Stores the configured `Reporter` on `ctx.obj` so subcommands retrieve it via `_get_reporter`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=f3a40c9f16db60e4660ec4c1670dc066e71d4e0d90c0eeafbdf048ae11362284 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=monitoring-telemetry -->
Configures telemetry from trie.toml debug settings and emits a CLI invocation event.

• Silently handles missing config files since `trie init` runs before trie.toml exists
• Emits "cli" event with subcommand name and argv tail for usage tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=1d3815663e939a183a3615fa14bce2303216da8109575c962b16755709c45c26 body_fp=1e721f00f18c1320eebcf87ead4914d8ef86ea5ea1286ebf80f02b2ecd3e7c5d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Create trie.toml config, update .gitignore, build symbol graph, optionally install pre-commit hook, and offer to run setup.

- `root`: Project directory to initialize (defaults to current directory)
- `force`: Skip Python project detection and overwrite existing config
- `install_hooks`: Install pre-commit hook (prompts in interactive mode if None)
- `run_scan`: Build symbol graph after config creation (default True)

Materializes `.trie/graph.db` when scanning, acquires write lock to prevent concurrent initialization, reports success/failure for each step, displays next-step recommendations, and offers to run `trie setup` interactively.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=5099d8aaf3feec3989a06e12a790bd7622b9cff2ccd17a0557f36de69be14319 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Checks if stdin is a tty to determine if interactive prompts are safe.

• Returns `True` when stdin is connected to a terminal
• Returns `False` for non-interactive environments (CI, pipes, redirected input)
• Gracefully handles environments where `sys.stdin.isatty()` is unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=d790cb8c8d4f3ea375951462dfe2095143e9a766cb0eb0e6b95154f3237889ca source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Context manager that does nothing; used to conditionally skip status indicators.

Implements the context manager protocol with no-op enter/exit methods, allowing code to use `with _NoOpStatus():` when a status indicator should be skipped while maintaining the same control flow structure as when a real status manager is used.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=08d221cc7a674a413ae90dd3f89994efdfbea0d74604458cd0f0198abd7e45ed source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
_NoOpStatus.__enter__ returns self to implement the context manager protocol as a no-op.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=7fcaa154ca4cba7b928bdfd4e5d6ed7394387fc74c2aa227a857e1321eeb9cf3 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
`_NoOpStatus.__exit__` implements the context manager exit protocol, taking exception parameters and returning None.

- Always returns None regardless of exception arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=392a35fcab27024390840bdc07a64b1d2275bc23f49e4982eb90baf4d9a5d597 body_fp=d2f0fae6485eff39c83dba42ae8758cf55d2fcf0fa824a54e45e0d8f8584f75c source_ref=5bdecfdcdf08068297fc189392e6001d3f8200e2 role=api -->
Scans project for drift, computes either incremental or full-bootstrap worklist, and displays estimated cost before any LLM work begins.

- Auto-detects incremental mode (stale files + cascade) vs full re-bootstrap based on existing triefacts unless `--all` forces full mode
- `--offline` skips the `count_tokens` network call by substituting a zero-token stub, printing the worklist with all cost estimates as $0
- Performs drift check first but continues on drift (informational, not a gate)
- Acquires write lock to ensure consistent store snapshot during planning
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=3182dc32d5135484a723e7e1259b7fa50871036159d113c4aa82c3257476827a body_fp=b1be616430a9b201bca45907bd2e1500a648b462e02f4479997676e0a0b1812a source_ref=991a2f7fd89566ae4e650bd979e2cf9a5a9b69b4 role=api -->
Runs bidirectional drift check and exits with code 1 if triefacts have diverged from source code.

- Detects both code→triefact drift (source changed without regeneration) and triefact→code drift (tampered sections or deleted symbols)
- Designed for pre-commit hooks and CI environments - no LLM calls, no database writes
- Same drift detection logic used by `plan` and `sync` commands, exposed as standalone verification gate
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:status_cmd fingerprint=743f438f810f49924c63a442dc9cff41a2f466d7f5286e147e2015f73d070725 body_fp=cf11fd8570f5d3137ade34e34c578dd0541e41e9f58f7a74f0c25ffba04d3096 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Reports trie's working state including active writer status, stale triefacts, and pending edit patches.

- Performs offline content-drift scan using same checks as `trie verify`
- Unions drift results with refresh-computed pending set for complete stale file list
- Queries graph store for patch summary including modify/create patch counts
- Outputs either JSON object (with patches field) or formatted prose based on `--as-json` flag
- Safe to run during active sync operations as it only reads status files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=b2588d0ec23978e9e8f4b7732d307584d0bad5d7227cee2cf553c7f4c21bf287 body_fp=5be4484291527e6b893fe68513dde9387fbf0c1357a0d9d0ad8741b1d3d163f3 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Probe whether another trie process holds the project's write lock, exiting 2 if contended.

- Designed for pre-commit hooks to detect racing `trie refresh` or `trie sync` operations
- Exit code 0: lock is free or project has no trie.toml
- Exit code 2: lock held by another process, caller should retry
- Uses acquire-then-immediately-release pattern that never blocks or interferes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:refresh_cmd fingerprint=36681f941b735fea43dbb79b8fe4f1ebec74c7dac32dfbb7cd157e00d598086c body_fp=63174663dd5c1843bb2300b1fbc0756ece2730568c1e12ab01ae137c99053051 source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=api -->
Handles the `trie refresh` command, which brings the symbol graph and triefact tree current with filesystem changes.

Runs in two modes:
- `--before-turn`: Pre-turn freshness gate that no-ops if nothing changed since last refresh
- `--after-turn`: Post-turn sweep that detects and syncs filesystem changes from agent edits

By default runs graph-only refresh (fast) unless `--sync` forces prose regeneration. Uses a file lock to serialize concurrent refresh processes and implements tail-pass coalescing to handle rapid successive invocations. Supports `--json` mode for machine-readable progress output.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_refresh_progress fingerprint=a7a68c1865cf0d4dd8de503731d2996168a5c600ba65cda8fbb577fc17bf8005 body_fp=db51678de4e0f2c2e33478ca2b4db672eabdf8b923a1fa2f0cc8e3957ceeeadb source_ref=085640f358eb2ab2e288a4afb6fcf64a4d2c2fb5 role=orchestration -->
Context manager that selects the appropriate progress sink for refresh operations, wrapping it to mirror events into the shared `.trie/` activity state.

- **as_json=True**: routes events through `_JsonlProgress` for machine-readable stdout
- **as_json=False**: uses Rich-backed `_ProgressAdapter` for live terminal progress
- Both modes write to `status.json` + `activity.jsonl` so `trie status` and editors see live progress
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_freshness_json fingerprint=0034385441b1a9da6627d562a7d41955dec313852d2732f766fc732c083fe963 body_fp=b99b4cdffb1cdc42666abaab94dc7b3f0a0ef636e6edda72c78b0f36fc457875 source_ref=54bb25e22500728d52451f98288c954f8ca94023 role=io -->
Emits the terminal `summary` JSONL event for a refresh outcome with mode, sync statistics, and cost data.

- Mirrors `_report_freshness` but as structured JSON for the desktop app to parse
- Includes files_synced and cost_usd from incremental result when available, otherwise zero
- Outputs stale_files as a list for downstream processing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=72454c399fb8977e4e0672bbb4a809308a080baf1f9f46614730e060c0159a33 body_fp=9086de862e5d391003c9b94d6738eacb7486a5c90893356842f5e348ab696c70 source_ref=54bb25e22500728d52451f98288c954f8ca94023 role=util -->
Renders a single status line for a refresh operation outcome.

- Prints "already fresh" if nothing changed
- For graph-only refreshes, shows stale file count and suggests `trie sync` when files need regeneration
- Shows sync statistics and cost when files were actually refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=5756d1b7e32899d278d6ffb9c3d820058831de9e933722d87f89c248c1fbabcf body_fp=213f5531341311c835c7814ef9e9223a1c86a702a3f28839dae069dd206598bc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=monitoring-telemetry -->
Summarise telemetry logs with MCP usage, sync activity, retries, and CLI invocations.

• `--log`: Path to debug.jsonl file (defaults to configured debug.log_path)
• `--compare`: Render side-by-side comparison with deltas (candidate vs baseline)
• `--json`: Output as JSON instead of human-readable format
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=82168e8ec7edc73bd791d28e3cfc2b65fbcde418535265e5ac087321c1cee77f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Resolves the audit log path for `trie audit` command.

• Falls back through: explicit `--log` flag → config's `debug.log_path` → `./debug.jsonl`
• Returns absolute paths, resolving relative config paths against project root
• Allows cross-project audit by not requiring trie.toml when explicit path given
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:intent_cmd fingerprint=d9a80927ea8581340ec7555b4e174afeed3d4aea28c0ec0db8e37050a1040f5b body_fp=173050fdb17d406d2dc6ca566b85533ba3498d0eb2a06758e443c668057ab815 source_ref=3e9be5f9b264b622f8cbeaac1f07240bdf8e1aa9 role=api -->
Enforce that every symbol changed vs HEAD has a patch note on record; exits 1 with a copy-pasteable worklist when coverage is missing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:index_cmd fingerprint=03be3ee88a8f66b5d0fcb774638b5784f0ff798428a46ca21c6d844027dd6ab2 body_fp=8d3aba6f7dd4eb53e26e97a40b98242febf33e4be4b24044ab45b1a13661414e source_ref=94ab54ce4fed9d45419aed45facacce5dc1f37cc role=api -->
Regenerate the triefact-tree index (`<triefacts.root>/README.md`) from the live graph store without calling the LLM.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:diff_cmd fingerprint=8717e8f40f14f3cbce8b5f33b7db58fc53991bd573216967d830218e124c3051 body_fp=08b0ec3f23536af41bc1612fa3e7c18d42ee269ebbf51c4664ce111a34fd06bf source_ref=803982f6e9b4a09af5ec33e6a15eb99bf222e510 role=api -->
Typer `diff` command that collects session evidence (triefact git diff + patch notes) and either synthesises an LLM narrative, dumps raw evidence, emits JSON, or writes a digest entry to the configured `diff.write_path`.

- `--session`: restrict evidence collection to one session id; defaults to all activity
- `--base`: git ref used as the diff baseline; defaults to `HEAD`
- `--raw` / `--json`: mutually exclusive; skip LLM and print raw notes or JSON envelope
- `--write`: pre-commit hook mode — calls `write_digest` (routing output through a per-commit file under `config.diff.diffs_dir` with a symlink at `config.diff.write_path`, reusing the same file when re-running on the same parent commit) and advances the digest cursor with `file=written_file`; mutually exclusive with `--json`
- `--model`: overrides `config.models.cascade` for narrative synthesis only
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=34ad2b8e98bf414eaf8a533a8b75ac271dbae3edca2b2d73052de585e4b60969 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Prints a colored breakdown of files scanned by status and symbols/edges count.

- Renders new/updated/unchanged/removed file counts with color coding
- Falls back to "no files in scope" when no categorizable files exist
- Shows total symbols and edges written to the database file
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=a3fad1a65c7d23db83f84ab7550e57151bb55d0228a974dae2657c75b00605bd source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Prints a bootstrap plan summary showing model, file count, total cost, and top 10 files with their symbol counts and estimates.

- Displays total estimated cost formatted to 4 decimal places
- Shows first 10 plan items with file path, symbol count, score, and per-file cost
- Adds "… and N more" footer when plan exceeds 10 files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=7d25e63d4726fe5f82eb8328587f26dafdb4888e59a3a3fec7f1f3399867bea1 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Print incremental sync plan emphasizing actual work order and symbol-level impact.

- Displays files grouped by directly stale vs cascaded, ordered by execution priority
- Shows symbol-level breakdown (how many symbols will hit LLM vs total documented)
- Lists orphan triefacts that would be removed, truncated at 10 items
- Preserves bootstrap ranking within each execution tier for cost visibility
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_REASON_LABELS fingerprint=a74cd9fa61964b8516ebff4efdf8859fa2ff50596c2b3765caf8b2d964d0c5cd body_fp=41637c91a10ea3f8163d99b0cca22671a00d986f7952e841c2440a25a9887c8e source_ref=991a2f7fd89566ae4e650bd979e2cf9a5a9b69b4 role=model -->
Maps StaleReason enum values to human-readable labels for drift reporting.

- Used by `_print_drift_detail` to render per-file drift items in a user-friendly format
- Keys are StaleReason enum members; values are descriptive strings for CLI output
- `TAMPERED_BODY` label now includes actionable guidance directing users to move prose outside sentinels and run `trie sync`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=698bcad70ac9d737c38314e3d26f0d384ff76f3b86cdcad26f47397e3c262b21 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders drift check items grouped by triefact file with colored status indicators and indented issue details.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=f89fbd7b24f02c1114b3df4a32ee4fb2d48667c85a33b093eb01d3f64becede3 body_fp=44a3fd1a2641e2f490a4bf9aee8fdbe0559b48519186574ee8b46b64c96516b8 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=change-detection -->
Checks triefact tree coherence and reports drift, returning True if clean.

- `exit_on_drift`: When True, raises `typer.Exit(1)` on drift (for `verify` command); when False, warns and continues (for `plan`/`sync`)
- Returns False if drift detected, True if tree is coherent
- Reports detailed drift items when verbosity is MEDIUM or higher
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=53808eca641489248c69e0878e0a4d684d5f7cfbde142076f477435415ac5ed4 body_fp=5487f76a86e534e1672b6643ef2cc5e8a292224698e0d0f2345412a3a551f5bc source_ref=173b70d2a0789e0a1b8d64b4c2eeb18dc6a5a50c role=api -->
Generate or refresh triefacts across multiple modes determined by CLI flags.

Supports single-file sync, dry-run preview, metadata-only refresh, roles-only classification, forced full re-pass, and auto-detected first-run vs incremental modes. Validates flag combinations including new roles-only restrictions, acquires a write lock, then delegates to specialized helper functions based on the selected mode. All modes run drift detection first and handle configuration loading consistently.

- `--roles-only`: (re)infer architectural role tags without regenerating prose
- `--rederive-taxonomy`: force role vocabulary re-derivation (requires --roles-only)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=0a62d5928c91a171e378bd5fab17ad701335a6b91b910ea6c795000ccad9b267 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Returns True if the triefacts directory exists and contains at least one markdown file.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=310d9b9367e302ff3c3768ed538bc8587b16f09cbab1873b014d1ae7e79b7e8e body_fp=66cee14485bb66797beb5c1db2aad70e333562e341f5eb5b9bd1c06e6296fd6b source_ref=94ab54ce4fed9d45419aed45facacce5dc1f37cc role=orchestration -->
Executes first-run bootstrap sync: scans project, builds plan, prompts for confirmation, then generates triefacts and refreshes the index.

- Requires budget/limit or interactive confirmation when no cap is set
- Scans project and builds token estimation plan before proceeding
- Calls `_refresh_index_quietly` after a successful sync if any files were synced
- Reports per-file errors via `_report_sync_errors`; exits with code 1 if any occurred
- Reports final cost comparison (estimated vs actual) and files processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_refresh_index_quietly fingerprint=d529f7105e01e70c95ec0edde7ecd5d69d83d6a4b700b9586c39ec54c6ad83d6 body_fp=157f92062beabea3f06f4d4fb44d43034a1b6fdc4bb0eed344927dec5d9dbe30 source_ref=94ab54ce4fed9d45419aed45facacce5dc1f37cc role=util -->
Regenerate the triefact index after a sync, silently swallowing all exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_sync_errors fingerprint=728c6f436fd1675b4a5e8b61b79f8776946aa9129a1e2634405f94b84d5323ba body_fp=dfd62a66da3f7a3aaa2ed6f59513040657558f6b4af2e41c5de6ac6e8d04adc7 source_ref=4f0622786b51d5b9394fc2a9e83adfb56969c440 role=util -->
Report per-file sync failures to `reporter`, printing up to 5 errors plus a credential hint when error text suggests a missing API key.

- Returns `True` if any errors occurred, `False` if `file_errors` is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=aef73997fa835e6c4cb57d5089fed793e34be8fbd933335d2ba9ff6d1f88985f source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=domain -->
Implements `trie sync --dry-run` by regenerating stale triefacts into `.trie/preview/` and printing unified diffs.

- **model**: Uses `models.bootstrap` if not overridden
- **budget/limit**: Caps LLM cost and file count
- **output**: Prints per-file diffs or notes fingerprint-only changes
- **exit**: Reports total cost and skipped files due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=17df35b7143b22bb3651c9e3571e4496066301f0b00f39213054f3b892dbda71 body_fp=c35712090a9c65e3a57bcfb675c014574380f58867ea42c70aa201a7be19af8b source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=orchestration -->
Sync a single file specified by `--file` option in the `sync` command.

- `file`: Path to the source file to sync; must exist
- `model`: Optional override for the configured bootstrap model  
- `force`: Bypass diff-aware path and cold-regenerate all symbols in the file
- Validates file existence and loads config from file's parent directory
- Creates LLM client and opens graph store, then calls `sync_single_file`
- Reports success with triefact path, symbol counts, and token usage details
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=ab88ff6a5f8617fcb6bbcc42dae27974d38c2d4d9d9e8f5df2a4c2dcd0f4ad19 body_fp=eb1f4ef332c83227c8796367c61641906b4bf42a0777d7799d2ca2aaa79f1ee2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=documentation-sync -->
Refreshes triefact front matter from the live store without LLM calls, designed for post-graph-change updates.

- Rescans project to pick up new edges from resolver changes
- Updates ref counts and defines entries for each in-scope triefact
- Skips files outside source_root and no-ops when metadata already matches
- Reports changed count vs total processed files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_roles_only_sync fingerprint=22454bb15b78ae54b3e1a5b86539b90e887f62c4a09831c904b19c783d7248d5 body_fp=42115c362dad4734b761057c0fdea134a726f44d4334c1aa37664e793e736ae6 source_ref=531556cb2ca369f928920ff2e8a5af396c7dd9ee role=orchestration -->
Runs the roles-only sync mode: derives/loads role taxonomy then classifies every symbol against it without regenerating prose.

- Scans project first to ensure store reflects current source
- Uses cascade model (or override) for role classification
- Reports taxonomy derivation, symbols classified, and role changes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=5a229490f92f265dce89d7500267a7ea9a086deb87d637dfd006a782d18a5d31 body_fp=752def5710f8f5918529e99aedbf64da038f3be66e8ef1e30c94b40a11f39205 source_ref=94ab54ce4fed9d45419aed45facacce5dc1f37cc role=orchestration -->
Execute an incremental sync that regenerates only stale triefacts and their cascade dependencies.

- Loads project config and opens the SQLite store with activity progress tracking
- Calls `run_incremental` to sync directly stale files and their cascade neighbors; calls `_refresh_index_quietly` when any files were synced
- Reports orphan triefact removals and sync statistics to the user
- Calls `_report_sync_errors` after syncing; exits code 1 if all files failed or any file errored
- Honors budget/limit constraints and reports any files skipped due to those caps
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=615d05779419134debda9155f1be7e507d600b96d3a99aaff53e9c4ed96d6526 body_fp=bc02fe45b2a47cd34ee4fc2fac3ba0d90d9e7d51ee0b00496e3cad9a1a594d88 source_ref=b07b41bd042a833a471ca6cd324eb62f95c2d4ea role=api -->
Integrates trie into coding agents by installing hooks, tool overrides, documentation, and GitHub workflows.

Orchestrates multiple install steps in sequence:
- MCP server registration (optional, via `--with-mcp`)
- Turn-boundary hooks for automatic refresh after agent edits
- Tool wrapper overrides that replace agent built-in `grep`/`read` with trie equivalents
- Agent-facing documentation (TRIE.md and pointer updates)
- GitHub Actions workflow that comments the latest session digest on PRs
- Optional CI sync-bot workflow (opt-in via `--with-sync-bot`) that regenerates stale triefacts on PR branches

Target auto-detection resolves which agents to configure; `--target` or `--all` override this. The process is idempotent - re-running safely overwrites existing configurations. Agents without automation support emit manual setup instructions. Exits with code 1 if any install step errors, including either workflow install.

- `--no-overrides`: Skip tool wrapper installation, leave agent built-ins unchanged
- `--scope`: Install in project directory or user agent configs
- `--dry-run`/`--print-only`: Preview mode without file modifications
- `--with-sync-bot`: Also install a sync-bot CI workflow (spends API budget; opt-in)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=9c0c752d54c3dcfa921629d39973d8145b811fdd047a21cf7002c9a974f78517 body_fp=00d3d6b6fe11ea59d9146ce4c158ed543a0cdce62c72547fc54a4a6c833a62d5 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders a combined setup plan report grouping MCP, hook, and override results by target with a separate docs section.

- Groups results by target slug, showing each target's MCP/hook/override outcomes indented under its display name
- Emits manual setup warnings and JSON previews inline where applicable
- Renders docs section separately since it's target-independent
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=1ede2878bb98b6df394615cdd58ab4ecae185270f43cadf83ab95df212d1565d body_fp=ba615a58540e306c9db7664acb2bee499d1e8cd67c59c83657c1c5497905c5a2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders tool-override install outcomes for a single agent target within the setup command output.

- Prints summary line showing override action status
- Lists per-file outcomes indented beneath the summary  
- Handles manual setup notices for unsupported agent harnesses
- Uses Rich markup for consistent visual formatting with hook install output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=33f2a0af34ece204faf67aa6c95cef95a890aaeba6f93c9a8f92484e6ee2a603 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Formats an installation action result as a display string with optional path suffix.

- Returns `action` alone when `path` is None, otherwise `"action → path"`
- Used by setup command renderers for consistent MCP and hook line formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=21c17059efeb9d659493f91f06cd3aea63b05d387ef3446792e9d5aa97a2a34e source_ref=b07b41bd042a833a471ca6cd324eb62f95c2d4ea role=util -->
Resolves project root from trie.toml and returns TrieTools instance configured for CLI telemetry.

• Returns TrieTools with event_name="cli_call" to distinguish CLI usage from MCP calls in audit logs
• Caller must close() the returned instance to release SQLite handle
• Raises typer.Exit(1) if trie.toml not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=cbf61b9c556d479acf0bd9aed32381243ee9cfdf00343a76c3dd1ad871c43a26 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Prints envelope as raw JSON or via provided renderer, exits with code 1 on errors.

- `as_json=True`: dumps to stdout without ANSI codes for agent parsing
- `as_json=False`: delegates to the provided renderer function
- Error envelopes always render through the renderer for human diagnostics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_patched_tag fingerprint=dc648bd9f208afe7454d79f5eebafca65d77f7014569d3999b97bf3f93928efe body_fp=9be02189078c57ce4a27212a4894416ac6166c915a7c4f9a97ad4f402d2f6f8b source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Returns a yellow `[patched: N]` tag for count > 0, empty string otherwise.

Used in grep and trace output rendering to visually mark symbols with pending edit patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=132ccb4bbce0becd4dd07923c83487b62bfacf65d4d6de4322cf4cd215509709 body_fp=369e31a5a8bafb00a4d8a963697ddbfb898a214f7a33ef8e0d30086879f4e613 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders human-readable output for `trie grep` command results.

- Displays symbol hits as a Rich table with qname, kind, location, and one-liner columns
- Falls back to candidate matches table when no exact hits found
- Shows pending patch counts as yellow tags on qnames
- Routes errors to `_render_error_envelope` for consistent error formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=2b10e36d759a5d0ea615a7db338822b6231723a2963b138ff8997b4262a3a179 body_fp=3db1c6f1a65ef2556ff8fb722d590775f841997ccd4986e572e2cb470af0c10d source_ref=981512fbf7d02046ab79dbef03cb3cae1db948c0 role=util -->
Renders human-readable output for `trie read` command responses, displaying symbol metadata, notes (before prose), prose, pending patches, caller/callee relationships, and a history block.

- **envelope**: MCP response dict containing qname, signature, source_pointer, prose, callers, callees, pending_patches, history, and notes
- **reporter**: Console output handler for styled text rendering

Formats the symbol's qualified name and signature at the top, then prints any `notes` entries early (⚠-prefixed notes in bold yellow, others in dim) before the prose block, followed by pending patches with their origins and notes, then caller and callee lists with one-liners, then a `history` block (date · change lines with optional title), and finally notes again as yellow-banged lines. Error responses are delegated to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=1af973f434ca837af6bd3bf7f5f4a14871b62746089ef1d6845c6f30cd474b15 body_fp=08321fb0893b819f18aa414844c848fb130b915d9321331e40e4d9e000bc7bc8 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders human-readable output for `trie trace` command responses.

- Displays root symbol with its one-liner description if present
- Lists all nodes in the trace with qnames, one-liners, and pending patch indicators
- Shows edges with directional arrows (→ for outbound, ← for inbound)
- Reports truncated hubs and any diagnostic notes from the trace operation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=29e06ccfb00bd8f211685d85fb3a46d9de82717423194f02d0f6dea1b11b353f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders standardized error envelope from MCP tools into human-readable form via Reporter.

- **err**: error envelope dict containing `code`, `message`, and optional `suggestion`
- **reporter**: Reporter instance for formatted console output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=7f410b69de496539d7948c4e8a86a399d45babc4ab7286234153ca799a704dc5 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Assembles a search predicate dictionary from CLI flags for the `trie grep` command.

- `predicate_json`: Base JSON predicate; individual flags override matching fields
- Constructs nested `inbound_count`/`outbound_count` objects when min/max bounds provided
- Exits with code 2 on invalid JSON to distinguish from other error types
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=8c43a494fcb2e3b2468d86052eaee440d5a34a0ab7bad2281fbdf8a0f1dbeb87 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
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
<!-- trie:section symbol=trie/cli:read_cmd fingerprint=658656804167b1ab001b1fae44c199006876251ce97e55828ca5821527066a70 body_fp=2a35bd35ab6d0ab332683838e820dc2e69799093a40ec2279e8192f1ce2fd81e source_ref=981512fbf7d02046ab79dbef03cb3cae1db948c0 role=api -->
CLI command that reads source code or trie's synthesised description — dispatches via a single `tools.read()` call.

- Accepts a symbol qname **or** a file path as the positional argument
- `--full`: for file paths, returns every section's full prose instead of the compact triefact view
- `--source` / `--offset` / `--limit`: force raw line-numbered source with optional windowing
- `--history` (`-H`): also retrieves the symbol's or file's intent trail from the session-digest archive
- Delegates rendering to `_render_read_dispatch`, which fans out to `_render_read_source`, plain output, or `_render_read` based on envelope shape
- `--json` emits the raw MCP envelope verbatim; mirrors the MCP `read` tool wire response
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_dispatch fingerprint=2259360f989712d808ec20d13c4379463c02d8176fc94e720e458dbbb7a384d9 body_fp=93d96bba49f5483e3faf0566d24c684b1c11e8e933601bf7aa130bac37f4d8f7 source_ref=b325efc3edba660c5ed59d60e141bf03e531c2cd role=util -->
Dispatch a `tools.read` response envelope to the correct human-readable renderer based on its shape.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_source fingerprint=fddcf9841287b22b0ffbf1e488f06c1ae46eacc63bd5bc0397b58066053c792b body_fp=2c21247aa600ab31b580d3ba509b35df8cbe2e05f7a97108985455e7adf1c980 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=util -->
Human-readable renderer for `read_source` tool envelope responses.

- **err**: renders error details via `_render_error_envelope` and exits early
- **lines**: prints the source content directly to console
- **more**: shows paging hint when result was truncated by offset/limit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=4163cf535b50888684695017b4ba5cf75abd1a6767961b77d6fca069e7504675 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Trace call graph from a symbol outward up to specified depth, mirroring MCP `trace` tool.

- `qname`: fully-qualified symbol name to start tracing from
- `direction`: "callers", "callees", or "both" (default: "callers")
- `depth`: maximum BFS depth, clamped by config trace_max_depth (default: 2)
- `as_json`: emit raw MCP envelope as JSON instead of human-readable summary
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:blast_radius_cmd fingerprint=894cae88c8d009e068480f6da6493330bd52972377fa29f98bafe7539b4018b8 body_fp=25631381b6dd206cf283cede3d0f81a3263ac20b190c1e5d4cf16cadecde0b60 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
CLI command that computes the cascade blast radius of editing a symbol using free graph traversal.

• `qname`: fully-qualified symbol name to analyze for edit impact
• `as_json`: when True, emits raw MCP envelope instead of human-readable output

Reports every symbol whose triefact/source would be regenerated if the target symbol changed, with BFS hop distances from the seed. Makes no LLM calls—pure graph mathematics for impact assessment before risky modifications.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_blast_radius fingerprint=beec4a79525cc1ed8a249725a02cdf21768f500a1f84520ed235826beb32b13e body_fp=4cfb51b9b368d85273371bdad8292123fc3a5450ff05480da297b345d0fef286 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=util -->
Renders blast_radius tool results in human-readable format for the CLI.

- First checks for error envelope and delegates to `_render_error_envelope`
- Prints the target symbol name and file location in bold
- Shows summary line with cascade count and direct caller count
- If cascade data exists, renders a Rich table with hop distance, symbol names, and file paths
- Falls back to "nothing else depends" message when cascade is empty
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plain fingerprint=73b737045796027c85e5cc8cadae182504d8d70c294160d047c87451d9359465 body_fp=994c0fd50f2844e2c0f9a2ea3a1614065754533fc0327dcc5f83c98110dc988f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders MCP tool response envelopes as human-readable JSON output. Checks for error envelopes first and delegates to `_render_error_envelope`, otherwise prints the full envelope as formatted JSON.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_str_cmd fingerprint=06d5d99001a7e1e6b779b756578538ae9e43b7bf4d004f75cf30df0795430407 body_fp=681496257e57e0b449de82992a6d539b50e2a2c1e6ec0a87f7ecd88430a0305b source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
CLI command that searches source file bodies with a regex pattern and attributes hits to their enclosing symbols.

- Supports `--all-files` flag to search the entire repo instead of just indexed source files
- Calls TrieTools.grep_str_all() when --all-files is enabled, otherwise TrieTools.grep_str()
- Always renders output in human-readable format (no --json option)
- Closes the tools connection in a finally block to ensure cleanup
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:find_cmd fingerprint=d5f94e0ba784d4e22c80f0ccc4a2021ae81fd1c1c78d7f75fe60c6a9f6a08405 body_fp=9fc74dac3e1ccdd081c3169a39ae9d3f8d01feabf377e50b1b5e38aa7f05fe79 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Searches project files by glob pattern, returning paths sorted by modification time.

• `pattern` — glob pattern like '**/*.ts' or 'Dockerfile'
• `indexed_only` — restrict to files in trie's scope (default searches whole tree)
• `limit` — maximum paths to return (default 100)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:write_cmd fingerprint=cf4b365e8c07b479bc6f52e78297ba187d19175ffac9258ec50a745b18964006 body_fp=e789613e78ddb1111405d8638189cee4355a1dfcf1fd834185e895e8d258c4e0 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Implements the `trie write` CLI command to create or overwrite arbitrary files under the project root.

• **path**: File path relative to project root
• **content**: File content (reads from stdin if omitted)  
• **overwrite**: Allow replacing existing files
• Uses `TrieTools.write_file` method and renders output via `_render_write`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_write fingerprint=7da15db852375b5f18b8f22176e76e410cc6233f4a875a3e7d1d6f634dffdfd2 body_fp=536304b144fdebc367a52dfefc2970f15a3e05408a42530d8e0486df9d4c4daf source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=util -->
Renders a write_file envelope in human-readable form for the write command.

- Delegates error envelopes to `_render_error_envelope`
- Reports "created" or "overwrote" based on the `created` field
- Shows file path and byte count from the envelope
- Advises running sync/refresh if the file needs indexing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_find fingerprint=33aeb9572d75fb7b54cc8ba23acd8213c8a6c087e002c5264d9d8b344a2825cb body_fp=a2c9e3a8a61ed32625159ebc89cdec25d3f64e2f6be0bf23f0413be8700c877d source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=util -->
Renders human-readable output for the `find_files` MCP tool envelope.

- Prints error details if the envelope contains an error
- Lists each matched file path on a separate line
- Shows file count with truncation notice when applicable
- Reports "no files match" for empty result sets
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_entry_points_cmd fingerprint=1a9f9b71faac201e98831ba75798e16ab0a9a61cf6461f80a76bede7e9b46b63 body_fp=86af0c27c7a6ee9cd58f91e6ab7c43338c2f7f72d5911942fa08110a2f8a58fb source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Provides the `trie grep-entry-points` CLI command that searches for architectural entry points by topic.

- `query`: Topic or concept to match against symbol prose in entry points
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_cmd fingerprint=4b925e05b1ef0842ffd6862a088f06f315888e9a54b2ad2ed6d7ad0b17407e4c body_fp=7570b063a93abbedf36eed837046ca587a43cf8378044121ad264e59e4f39882 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Executes fuzzy symbol name lookup via TrieTools.grep_symbol and renders results as structured JSON.

- Uses `_open_tools` to create TrieTools session with project root from nearest trie.toml
- Calls `tools.grep_symbol(sym)` to find best match and similar symbols for the fragment
- Always renders output via `_print_plain` (structured JSON format, not human tables)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_neighbours_cmd fingerprint=27d88a48d69a0bace10cac46278c7472e07d9febc837407321656de44beb0fdd body_fp=9d5189effab527a6b20a26e377befda85dac6b252def86aca18964d988e5b485 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Implements `trie grep-symbol-neighbours` CLI command that performs fuzzy symbol lookup and returns immediate caller/callee metadata.

- Takes a symbol name fragment to fuzzy-match against the graph
- Calls `TrieTools.grep_symbol_and_neighbours()` to get the symbol plus trimmed neighbor data  
- Renders output in plain text format via `_print_plain`
- Example: `trie grep-symbol-neighbours sync_single_file`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_cmd fingerprint=5ac54530f72257c5d11086cb8329c87c18e4854c936ee61b8eda9aa13a67ab57 body_fp=945defb7ddf655ed721c1762b7e993a9a78b94867b5fa0ed24395a7e233581ec source_ref=981512fbf7d02046ab79dbef03cb3cae1db948c0 role=api -->
Provide detailed explanation of a symbol including its prose and reference narrative via CLI.

CLI command that wraps the MCP `explain_symbol` tool for terminal use. Takes a symbol qname or name fragment, opens a TrieTools session, calls the explain method, and renders the result in human-readable format. Always uses plain text output rather than JSON.

- `history`: when `True`, also passes the flag to `tools.explain_symbol` to include the symbol's intent trail from the digest archive.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_refs_cmd fingerprint=144754c21e109b2a9de843dc793483768c61aaf9518bd86db72f4d79b556927a body_fp=17070190e6f4012461c8b6a7735c43e968f47d6ca689a1fccda75d2cb415d2a7 source_ref=981512fbf7d02046ab79dbef03cb3cae1db948c0 role=api -->
Typer command that explains how a symbol is used by its callers with their prose.

- Accepts `--history`/`-H` to also include the symbol's intent trail from the digest archive
- Calls `TrieTools.explain_symbol_references()` with the symbol name/fragment and `history` flag
- Always outputs human-readable format (no JSON option unlike other commands)
- Uses generic `_print_plain` renderer for output formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_flow_cmd fingerprint=159e9cac61ba82f744521d2dcc8f53ec1ebd5f1aa4fbc36c96b5eae8755520ed body_fp=a7f3fdfb0e79f548335e637502e92fbe5646e047ae3b433494946addc1fe7065 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
CLI command that finds call chains between two symbols via TrieTools.trace_flow.

- **symbol1**: starting symbol qualified name or name fragment
- **symbol2**: target symbol qualified name or name fragment
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_flow_cmd fingerprint=c840efc39861b94757c6288e677187040a32e2c5b69ab95bfb93600dc7a03f4c body_fp=74baf831dd85839c025a3ced1a9564864a5ffd4c631f0fafd2a844471fce7119 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
CLI command that traces call chains between two symbols and narrates each step.

- `symbol1`: starting symbol qualified name or name fragment
- `symbol2`: target symbol qualified name or name fragment

Calls `TrieTools.explain_flow` and renders output using the generic plain-text renderer.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_app fingerprint=a01ba84281db5613dd9598b44b9572c2f52e7bf4a145def4e8140840006383da body_fp=0297250842674ecd94a570ce93159fdff3eade05ffef0210ab52062e894e45f4 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Typer CLI application for managing edit patches against symbols.

- Provides subcommands: create (post patch), preview (show apply plan), apply (execute patches with cascade), list (show pending), drop (remove patches)
- Configured with `no_args_is_help=True` to show help when invoked without subcommands
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress fingerprint=88a444531b547feca55d4fda3ad1c55db173b88633bd149775faf38391c33b66 body_fp=fb6070f71b83ae157c59be4141d94e3edd3701f121e2b744d694cb24c26495bc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Rich-formatted progress reporter for apply_patches operations. Prints structured, thread-safe progress output with visual indicators for each stage.

- Methods called from worker threads, so output naturally interleaves
- verbose flag controls symbol-level detail display
- Uses Rich markup for colored icons and indented hierarchy
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.__init__ fingerprint=1c6ad7264d460fcc4f36e9524e2f5bc1f7ee6bc638d01590eca5e0f665ce4ae7 body_fp=a0f71d7355dc8f9d45ff40d01c4795e5e7c2dee41ec64dd2187f8e2ecf0b3a8e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Initializes _RichApplyProgress with a Rich console and optional verbose flag for detailed patch application reporting.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.stage fingerprint=00a0e5b25af2600c917827df1316312556da14518c19c948a17c6b4f8105174f body_fp=c1f5d9c07788f968d33182a77f2fbc33f519f9ba6937ea7b51665f4d886ed1a9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Prints a stage header message with rich formatting to the console.

- Formats the message with bold cyan styling and a vertical bar prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_start fingerprint=1c9e2af52741b8ee459d4101628f36bc16552d1d167b3afdfa1cb25db55ae2d3 body_fp=8d280285ae0ba5941fbf5ddad5830d282b0415f9f869ef4d7b1963b0cc946fa7 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints a file processing start message with file path and symbol count.

- `fp`: relative file path being processed
- `symbols`: number of symbols in the file that will be patched
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_symbol fingerprint=1fc9ef71af9d3e0f90361d13907c1059d449a1913c2acbac2a945251d0e7c24d body_fp=af56c37705685b73b7b01c3a996620bda3a9787bc1bb91fc6cfe71495f652a1d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints per-symbol progress during patch application when verbose mode is enabled.

- `qn`: qualified name displayed in cyan with indented bullet point
- `notes`: patch notes truncated to 100 chars and printed with "note:" prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_generate fingerprint=132b41245a185b2af3aacb3c8c3a18c12c5b09ff296437cde359f630862c6105 body_fp=e46e1034cc995556ab2ad34cc7aba5e7826c44445b1217c55696f5edc8e6b7c2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints generation progress for `_RichApplyProgress` when verbose mode is enabled.

- Only executes when `self.verbose` is `True`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_fixup fingerprint=26be5de5ef710ac328e60f9b6eea26539ebdc8ecf0c1fd70a4eb97604c07d115 body_fp=354f09f9566eeae08907a9a556595c9a875c735e1f8e767ee2d747ff96371cf9 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints a yellow gear icon with LSP fixup iteration number and diagnostic count.

- **iteration**: Zero-based fixup pass number
- **count**: Number of diagnostics found in this iteration
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_prose fingerprint=12b3c9eda87bd14def97bc9c6c65327a7d23a45803d936cae5ab3330703ecb93 body_fp=b0639bc61593899e87e2d508c8526ec8c715256200e4a5c909ebacb3cbdf35df source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints a verbose prose generation indicator for the given symbol qname.

- Only prints when `verbose=True` was set during `_RichApplyProgress` construction
- Displays an indented line with a pen icon and the qname being processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_done fingerprint=be1e14003b12fc05817ca35f7302feae8c628647d0b7cffb7cef9fef388f8c11 body_fp=e83badb76dd48eb5f9f74567e452bf20d0c6fb5799a937051c55f5132cd99bcc source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints a completion status line for a file in `_RichApplyProgress` patch application progress.

- `ok`: determines green checkmark (success) vs red X (failure) icon
- `error`: failure message displayed in red when `ok` is False
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.refresh fingerprint=fa057109cbf67e48f2ca72e4736ffb716951fd64ecb1ac03f8c0afce10bfb4e2 body_fp=91777d45c485266abd077f253512020c315913a09ada1f89e811c761171e90d4 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Prints a refresh indicator for the given file path during patch apply progress reporting.

- `fp`: File path being refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.verify fingerprint=9bb6073c0083b530e9d8a61ec3fe90bde21961bdcbb397e39268aa6d65db357c body_fp=88843d1669232469dd7a92f0b73d40fc967e947a1c92e8d576021241cb8f1664 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=code-editing -->
Prints a green checkmark indicating the project is consistent after patch application. Called by `apply_patches` at the end of its verification phase.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_cmd fingerprint=72662c0d688f65a55be9ca8b56e205d87ae1b075cad1fdb6e7e5aff80b4eced5 body_fp=9d614697375f678fc968641bafbfce01900e627adaf2625e4fb4bdaa6a89854c source_ref=3e9be5f9b264b622f8cbeaac1f07240bdf8e1aa9 role=api -->
Creates a fire-and-forget edit patch against a symbol in the trie graph store.

- `--gone`: bypasses the graph store entirely; records the note directly to the session log as a `delete` op instead of queueing a patch
- Validates that the symbol exists in the graph database before creating the patch (non-`--gone` path)
- Uses a stable CLI session ID for tracking related patches together
- Returns the patch ID after successful creation (non-`--gone` path)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_batch_cmd fingerprint=e8e49da442695fe76c0d074020c7390caae868f905570564bc9678a174304a88 body_fp=f2b2c9232877c2aee649df8fdb2a4200e6b7666b107dac2ca4683917d156861a source_ref=85e57bbb035420774c33a2c6594da614a72f3d47 role=api -->
Stage multiple `patch` or `create` operations in one call, reading a JSON array from `--json-file` or stdin.

- `op`: `"patch"` (default) modifies an existing symbol; `"create"` stages a new symbol.
- Items are processed independently; failures are reported without aborting remaining items.
- Emits `{"staged": N, "failed": N, "results": [...]}` as JSON to stdout.
- Exits 1 if zero items were staged successfully.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_symbol_cmd fingerprint=eb7419a1e9a7e32d6229ca974f46c5ac781021bfa99e565ebad0910d60401c8a body_fp=79674ac48e601f3bff45ba7f2dcc544e031a970b69412f598d3d9f3bb01f3d3a source_ref=85e57bbb035420774c33a2c6594da614a72f3d47 role=api -->
Stage creation of a new symbol to be applied by `trie patch apply`.

- **qname**: intended qualified name like `pkg/mod:new_fn`
- **note**: what the new symbol should do (required)
- **file**: target source file; when omitted, resolved via `registry.resolve_create_target` (existing module wins, else language-inferred suffix)
- **anchor**: place the symbol after this existing qname
- **reason**: why the symbol is needed
- Validates qname doesn't already exist in the graph
- Stores create patch via `Store.add_create_patch` with session tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_delete_symbol_cmd fingerprint=d42b44a08aab95225aa29d2ef76a46ff4a907a793fda7b7ba45a30e5335c6d39 body_fp=b394a6512f0db2a67095c269a1a8cd3bfd16923d6c1f435524aab68ae659b289 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Command handler for `trie patch delete-symbol` that stages deletion of an existing symbol.

- Creates a delete patch against the symbol via `Store.add_delete_patch`
- Warns when the symbol has dependents that will reference a deleted symbol
- Raises `typer.Exit(1)` if the symbol is not found in the graph store
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_rename_symbol_cmd fingerprint=a2a8cc1e28f4751332966ccd372069f40de13ebbcbc3d5294d7e2cb0d4939183 body_fp=2712e95a2e06591d507d60547dcf06e7531337016d14b747db51f5f830cec1ee source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Stage a rename of an existing symbol for later application by `trie patch apply`.

- Validates the new name is a valid Python identifier
- Creates a rename patch in the graph database with optional reason
- Reports the number of existing references that will need updating
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_apply_cmd fingerprint=1f700192a89ef28464c7d0b52feb85fc8654bf0d8874a12d7c22994320c90447 body_fp=6396bc861e0a215761511ad811550f6cbaa4fa264ed6b6a8766bc3ad50c6dcea source_ref=b07b41bd042a833a471ca6cd324eb62f95c2d4ea role=api -->
Archive pending patch notes as intent via `record_intent` — always the `record` path, no code generation.

- `--note`: session-level unifying intent for the apply run.
- `--json`: dumps raw envelope to stdout and exits 1 if `ok` is falsy; non-JSON path exits 1 on failure or prints a per-symbol success list.
- Removed: `--model`, `--backend`, `--commit-mode` options and all `agent`/`llm` backend dispatch paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_preview_cmd fingerprint=bb43bb71a6141343c63226fcf7e8bf42a7bb400eedccecc762509629daa934f7 body_fp=e03e8a69221f0c07d9d3b8e4b3642f5e8c1ab04e8e8c08bd1c7333d523df64a7 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Previews what `trie patch apply` would execute without running it.

- Displays a Rich table with separate rows for patched symbols, create-symbol patches, and cascade neighbours
- Shows an "Origin" column distinguishing patch types rather than cascade indicators
- Reports zero patches with an info message if no patches or creates are pending
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_list_cmd fingerprint=8d8b6d21fbaecc39a83d4d22192f73d2d93ceb086194fcebedc17a8f0943f357 body_fp=80a151338dd9913e69e7c6b1df21c7fc758d2dbcadf93738a1defbc817295b13 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
List all pending patches and create-symbol patches in separate tables.

Opens the graph store, retrieves symbols with pending modification patches and staged symbol creations, then displays them in two Rich tables: "Pending Patches" shows qualified names with patch counts, and "Pending Creates" shows new symbol names with target files. Exits with no output if neither patch type exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_drop_cmd fingerprint=b456b5f77094c686bfb31765795cabfab769c5ad30c8de1e19416ea722b8f2be body_fp=878dc813f49b76f20fe7673a572c395ba89428564119edac46f0824e51b0cd50 source_ref=28797ad23f63ab76a0d693ea640c1de9c59f6c50 role=api -->
Drop pending patches from both modify/structural and create patch tables by qname, session ID, or all patches.

- Exactly one of the three selection criteria must be provided
- Clears from both patch tables so create-symbol patches don't linger after `drop --all`
- Exits with code 1 if no selection criteria specified or config not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_app fingerprint=0c83c10dbd09994c30dee74986deefeee9e7fbcba6d0fe9f936c328a8b332275 body_fp=58e6c3b276840293bcf335b4fd33dfabda523fafd5261b08491b0cb0134c417e source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Typer sub-application for MCP (Model Context Protocol) server management commands.

- Provides `install`, `uninstall`, and `serve` subcommands for agent integration
- Shows help when invoked without arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=70fc24d5899708cd24382a7202d5b17748a63d20953b59c486d5f62a5ccc2d1d source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Run the trie MCP server over stdio as a Typer command.

Delegates to `_run_mcp_serve()` for the actual server implementation.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=73c11dc03b04976bf9a2fc8e80637299abc238437977e34a37ba8ed763f61b6e source_ref=b07b41bd042a833a471ca6cd324eb62f95c2d4ea role=io -->
Starts the MCP server over stdio after validating the project configuration.

- Locates trie.toml and validates config structure without using its contents
- Prints config errors to stderr to avoid corrupting the MCP protocol stream
- Delegates to run_mcp_stdio for actual server implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=56b8a3b5140b45725192474cf54754a68433b6176f397804f637922c8ff8f7e2 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Registers trie MCP server with one or more coding agents through their config files.

- `target`: specific agent names to install for (can be repeated)
- `install_all`: install for all known agents, skipping detection
- `scope`: "project" writes to current repo, "user" writes to ~/.<agent>/
- `print_only`: shows config snippet without writing files
- `dry_run`: shows file paths and changes without writing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=c59c0e62f61e8a6cbca9c3bc43e2245f6354f57fcf5c071f544b259056b7a493 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders human-readable output for MCP installation results, displaying per-target status and details.

- Formats each result with the target's display name and appropriate colored status indicators
- Shows JSON snippets for preview actions and error messages for failed operations
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_uninstall_cmd fingerprint=e0cbf3e2e0174b8f33dbe0589e2c6908d67e5f5c49961500186aab26268bab2a body_fp=0419c682c13f9af03e4f29b59768509b1970615524ec8ec4da9a6953dd9c1540 source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Unregisters the trie MCP server from agent configuration files.

• Validates mutually exclusive flags and scope options
• Delegates uninstall execution to `mcp_run_uninstall` with validated parameters
• Renders the uninstall plan showing removed entries per target
• Exits with code 1 if any uninstall operation encounters errors
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_uninstall_plan fingerprint=982bba634aca721cfd1aaf145aba973af33cbd7f5cb22ab4f82d6c4f8ba7a692 body_fp=2191ea5bf60f2c3f0b81ff5998d0d99449fd63a3c5851c65644d3559c8e5b85f source_ref=836a095d74cebfc79fe1aef607c8dd820c222a92 role=cli-interface -->
Renders the output for `trie mcp uninstall` by iterating through uninstall plan results and printing status messages for each target using the Reporter console interface.

- Mirrors the install renderer with `removed` status replacing `created`/`updated`
- Prints JSON preview for dry-run mode, success/error messages for actual operations
- Shows skipped targets with explanatory detail when no action was needed
<!-- trie:end -->