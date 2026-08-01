---
trie_version: 0.2.1
source: trie/cli.py
file_fingerprint: e958c03676c10913cb855a80243675c074571565842973bce8ec26efe7c1bb4c
last_synced_at: '2026-08-01T09:20:31Z'
defines:
- kind: module
  qualified_name: trie/cli:__module__
  lines: 1-4678
- kind: constant
  qualified_name: trie/cli:app
  lines: 87-90
- kind: constant
  qualified_name: trie/cli:console
  lines: 91-91
- kind: function
  qualified_name: trie/cli:_get_reporter
  lines: 94-100
- kind: function
  qualified_name: trie/cli:_cli_session_id
  lines: 103-123
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 126-198
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 134-139
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 141-146
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 148-151
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_plan
  lines: 153-165
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_section
  lines: 167-176
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 178-179
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 181-194
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 196-198
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 202-207
- kind: function
  qualified_name: trie/cli:_activity_progress
  lines: 211-228
- kind: class
  qualified_name: trie/cli:_JsonlProgress
  lines: 231-277
- kind: method
  qualified_name: trie/cli:_JsonlProgress.__init__
  lines: 252-253
- kind: method
  qualified_name: trie/cli:_JsonlProgress._emit
  lines: 255-259
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_start
  lines: 261-264
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_done
  lines: 266-274
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_skip
  lines: 276-277
- kind: function
  qualified_name: trie/cli:emit_jsonl_event
  lines: 280-290
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 294-325
- kind: function
  qualified_name: trie/cli:_root
  lines: 329-367
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 370-382
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 386-507
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 510-517
- kind: function
  qualified_name: trie/cli:_prompt_select_targets
  lines: 520-578
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 581-586
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 582-583
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 585-586
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 590-707
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 711-723
- kind: function
  qualified_name: trie/cli:status_cmd
  lines: 727-849
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 853-903
- kind: function
  qualified_name: trie/cli:_run_graph_only_sync
  lines: 906-1011
- kind: function
  qualified_name: trie/cli:_graph_sync_progress
  lines: 1015-1036
- kind: function
  qualified_name: trie/cli:_emit_freshness_json
  lines: 1039-1053
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 1056-1070
- kind: constant
  qualified_name: trie/cli:_AUDIT_TAIL_BYTES
  lines: 1073-1073
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 1080-1154
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 1157-1173
- kind: function
  qualified_name: trie/cli:_run_intent_gate
  lines: 1176-1218
- kind: function
  qualified_name: trie/cli:_warn_on_version_skew
  lines: 1221-1251
- kind: function
  qualified_name: trie/cli:gate_cmd
  lines: 1255-1312
- kind: function
  qualified_name: trie/cli:intent_cmd
  lines: 1316-1334
- kind: function
  qualified_name: trie/cli:index_cmd
  lines: 1338-1362
- kind: function
  qualified_name: trie/cli:diff_cmd
  lines: 1366-1498
- kind: function
  qualified_name: trie/cli:_run_digest_write
  lines: 1501-1638
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 1641-1658
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 1661-1672
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 1675-1741
- kind: constant
  qualified_name: trie/cli:_REASON_LABELS
  lines: 1744-1751
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 1754-1765
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 1768-1802
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 1806-2033
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 2036-2042
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 2045-2121
- kind: function
  qualified_name: trie/cli:_refresh_index_quietly
  lines: 2124-2131
- kind: function
  qualified_name: trie/cli:_report_sync_errors
  lines: 2134-2155
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 2158-2203
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 2206-2280
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 2283-2343
- kind: function
  qualified_name: trie/cli:_run_roles_only_sync
  lines: 2346-2388
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 2391-2460
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 2464-2674
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 2677-2747
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 2750-2776
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 2779-2783
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 2798-2816
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 2819-2843
- kind: function
  qualified_name: trie/cli:_patched_tag
  lines: 2846-2850
- kind: function
  qualified_name: trie/cli:_grep_output_is_tty
  lines: 2853-2866
- kind: function
  qualified_name: trie/cli:_print_grep_records
  lines: 2869-2890
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 2893-2984
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 2987-3074
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 3077-3129
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 3132-3144
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 3147-3209
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 3213-3316
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 3320-3387
- kind: function
  qualified_name: trie/cli:_render_read_dispatch
  lines: 3390-3403
- kind: function
  qualified_name: trie/cli:_render_read_source
  lines: 3406-3415
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 3419-3461
- kind: function
  qualified_name: trie/cli:blast_radius_cmd
  lines: 3465-3495
- kind: function
  qualified_name: trie/cli:_render_blast_radius
  lines: 3498-3528
- kind: function
  qualified_name: trie/cli:_print_plain
  lines: 3538-3547
- kind: function
  qualified_name: trie/cli:grep_str_cmd
  lines: 3551-3580
- kind: function
  qualified_name: trie/cli:find_cmd
  lines: 3584-3613
- kind: function
  qualified_name: trie/cli:write_cmd
  lines: 3617-3657
- kind: function
  qualified_name: trie/cli:_render_write
  lines: 3660-3669
- kind: function
  qualified_name: trie/cli:_render_find
  lines: 3672-3687
- kind: function
  qualified_name: trie/cli:grep_entry_points_cmd
  lines: 3691-3709
- kind: function
  qualified_name: trie/cli:grep_symbol_cmd
  lines: 3713-3731
- kind: function
  qualified_name: trie/cli:grep_symbol_neighbours_cmd
  lines: 3735-3753
- kind: function
  qualified_name: trie/cli:explain_symbol_cmd
  lines: 3757-3781
- kind: function
  qualified_name: trie/cli:explain_symbol_refs_cmd
  lines: 3785-3809
- kind: function
  qualified_name: trie/cli:trace_flow_cmd
  lines: 3813-3832
- kind: function
  qualified_name: trie/cli:explain_flow_cmd
  lines: 3836-3855
- kind: constant
  qualified_name: trie/cli:patch_app
  lines: 3863-3867
- kind: class
  qualified_name: trie/cli:_RichApplyProgress
  lines: 3871-3923
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.__init__
  lines: 3881-3883
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.stage
  lines: 3885-3886
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_start
  lines: 3888-3889
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_symbol
  lines: 3891-3897
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_generate
  lines: 3899-3901
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_fixup
  lines: 3903-3906
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_prose
  lines: 3908-3911
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_done
  lines: 3913-3917
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.refresh
  lines: 3919-3920
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.verify
  lines: 3922-3923
- kind: function
  qualified_name: trie/cli:_close_qname_suggestions
  lines: 3926-3940
- kind: function
  qualified_name: trie/cli:patch_create_cmd
  lines: 3944-4000
- kind: function
  qualified_name: trie/cli:patch_create_batch_cmd
  lines: 4004-4128
- kind: function
  qualified_name: trie/cli:patch_create_symbol_cmd
  lines: 4132-4180
- kind: function
  qualified_name: trie/cli:patch_delete_symbol_cmd
  lines: 4184-4211
- kind: function
  qualified_name: trie/cli:patch_rename_symbol_cmd
  lines: 4215-4244
- kind: function
  qualified_name: trie/cli:patch_apply_cmd
  lines: 4248-4310
- kind: function
  qualified_name: trie/cli:patch_preview_cmd
  lines: 4314-4357
- kind: function
  qualified_name: trie/cli:patch_list_cmd
  lines: 4361-4403
- kind: function
  qualified_name: trie/cli:patch_drop_cmd
  lines: 4407-4445
- kind: constant
  qualified_name: trie/cli:mcp_app
  lines: 4453-4460
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 4465-4467
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 4470-4480
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 4484-4553
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 4556-4571
- kind: function
  qualified_name: trie/cli:mcp_uninstall_cmd
  lines: 4575-4650
- kind: function
  qualified_name: trie/cli:_render_uninstall_plan
  lines: 4653-4673
incoming_refs: 127
outgoing_refs: 392
---
<!-- trie:section symbol=trie/cli:__module__ fingerprint=c05f8eb3576ed41757ae174e63dc2dc1455b0a5e028a7129a133f50f32b938f3 body_fp=f367e42959a17d8bb06467ebd02f37016b756f9dbe725ed778ed2cf61ed5a824 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=entrypoint -->
Main CLI module for trie providing comprehensive project management, triefact synchronization, and agent integration commands.

- `app`: Root Typer application with commands for init, sync, verify, plan, refresh, audit, setup, grep/read/trace
- `patch_app`: Sub-application for posting and applying edit patches against symbols
- `mcp_app`: Sub-application for MCP server installation and stdio serving
- `console`: Rich Console instance for colored terminal output
- `_ProgressAdapter`: Bridge between sync ProgressCallback and Reporter ProgressHandle interfaces
- `_RichApplyProgress`: Rich progress reporter for patch application with threaded file processing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:app fingerprint=bd6ef12c875332ea01db62797e29cf2fb64ae5ac0be52a25d5f8aa08f5abb82c body_fp=c0d1c1eee55e99f2a10dc06d4d381e1ff1d1a7a253b539152d249ce441cb7a55 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=entrypoint -->
Top-level Typer application instance that defines the trie CLI interface.

Configured with name "trie" and help text describing trie as an artefact tree that mirrors source trees with LSP-aware cascade coherence.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:console fingerprint=dff6104fc5140b6d96afa42ceddb0c4c0d1e4b0cb6686a2debb687f087a24c7e body_fp=e2c2c01956b6de43e5d529c487368909586063344bab7f6e2a55e75a75c243fe source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=config -->
Creates a Rich Console instance for styled terminal output across CLI commands.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=6a81fd6366ce2ab0fe15313c84f131e2dfc0e44a12c799be0c174b7dd13febf6 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Resolve the `Reporter` stored on `ctx.obj` by the root callback, falling back to a default `MEDIUM` reporter when none is set.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_cli_session_id fingerprint=dcf3fe8c7e922ef3d9466b25f8ca9207e6ab499a2182dd92a3538dbda5f6aa23 body_fp=b366a089840eb64d5fd80d72a2b8002334fc0e1d86a0c4f31a791d34bcfcc85b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Generates a stable session ID for CLI patch operations, reused across multiple invocations.

- Returns `TRIE_SESSION_ID` environment variable if set
- Otherwise persists a 12-character UUID in activity database for project-wide reuse
- Ensures `trie patch --session drop` works by maintaining consistent session identity
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=461508833971d6960227589e60e8d0554cca8d9567c3036ade7cdbf2512b7a95 body_fp=441186a4466e461e3d32a2f9e639160f821a075ab40c9811045341078e50ca35 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Bridges sync's ProgressCallback Protocol to a Reporter ProgressHandle with lazy initialization.

- Creates underlying ProgressHandle on first `on_start` call to avoid requiring total upfront
- Tracks per-file cost delta by comparing running costs across files
- Thread-safe via internal lock protecting handle initialization
- Prints worklist summary and section separators at MEDIUM+ verbosity
- Delegates file progress events (start, done, skip) to the underlying handle when present
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=62d7f3387263067099a16c5c411db665b3dabb0d0c2701008d99dd22a9a9d982 body_fp=20812b8efc8c28b2a799159dd09984d718a0d1de6177efe6a440eab285948a32 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Initialise `_ProgressAdapter` with a `Reporter`, a display label, a null `ProgressHandle`, a running-cost accumulator, and a threading lock.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=67aef789d4a34e8f4c519362a59b70a41784bc0e2039ff8ee536353e1ab334ac body_fp=6ec185bd407c25c9f716dc001368004f6d2225848ba04a37b0b2915106619242 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Lazily initialise and return `_ProgressAdapter.handle`, creating it via `reporter.start_progress` on the first call.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=0a0babb0cb7e0707b4b10478d10624ac2ef8b7645048e09d2b85e0aa92b652b0 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Tears down the _ProgressAdapter by exiting the underlying ProgressHandle context manager and clearing the handle reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_plan fingerprint=3566ccad9e5759fea947fdc6b8c297970c97a7799fcbb38f5da54fb81da4c43b body_fp=ba599faa9f925a95321ad3f61dfd3172b23e3778eec398f8108a520cb2be3ad9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a sync worklist summary before any file processing begins in `_ProgressAdapter`.

- `direct`: count of directly stale files
- `cascade`: count of files pulled in by the cascade
- Skips output when verbosity is below MEDIUM or total is zero
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_section fingerprint=ae4688be43ab22bbc7b9daf029a1af7eb1c021910f566633cf30240275e849f8 body_fp=b04721d507b543f4d4017b6eaeb0f640571887e2fdf558d6ebe0e3ed18bb439e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a section separator line with label and count before each file group.

- Skips output when verbosity is below MEDIUM or count is zero
- Routes through progress handle when available, otherwise directly to reporter console
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=34f538a7492b05dc2bf2f4087401ea296cd9a705571e3b4bf4aa7d16635d9a6b body_fp=a49b7814b890c8f06125a7a2e9b64c2518f863ce892c6e48c0c561fbc47a23f1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Ensure the `_ProgressAdapter` progress handle exists for `total` files, then delegate to `ProgressHandle.start_file`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=d027b8d68698a0feb649e720de9c37e9de1a7b103e44b851ecb79390b6689dd9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Reports file completion to the progress bar with cost and token metrics from FileSyncResult.

• per_file_cost: computed as the delta between running_cost_usd and the previous total
• cost_usd: only passed if positive, otherwise None to avoid showing zero costs
• tokens: includes input/output counts plus cache read/write statistics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=42c5646050616548a525fc8f2fe85e0dd7825303d0c9f14d898e9e60a768456c source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Records a skipped file by forwarding to the underlying ProgressHandle if it exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=f79b5fb9407ac52eee93b63fb3438cca1fd00d566b7a1a035bec3e038702ea65 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Creates a context-managed _ProgressAdapter that bridges Reporter progress bars with sync ProgressCallback protocol.

- **adapter**: _ProgressAdapter instance that converts ProgressCallback calls to Reporter.start_progress operations
- **cleanup**: ensures adapter.close() is called to properly tear down the progress bar on context exit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_activity_progress fingerprint=18bb44ffa9a5e83286e0aafd8a4ba6edafdce5d003c59f5560efa39703f3c523 body_fp=96e0e0acb7f283fd38726697a1aaf12e05b6653bbd67504adf04d3002dd22023 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Context manager that provides progress reporting mirrored to both Rich console and shared activity state.

- Yields a `ProgressCallback` that routes to both the Rich progress bar and `.trie/status.json` + `activity.jsonl`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress fingerprint=fd935dfc306344a1ab7e8d1965eef70da05594cf71cadac05dafdb542c05825f body_fp=430e5e67d0aa6bec9e82b4e9dba6688044d4b532c9a3b04bce995aa27144c794 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Implement `ProgressCallback` by serialising each sync event as a newline-delimited JSON object to a stream, enabling subprocess hosts to parse progress without scraping Rich output.

- `stream`: defaults to `sys.stdout`; each line is flushed immediately
- Emits `{"kind": "start", ...}`, `{"kind": "done", ...}`, `{"kind": "skip", ...}`; `phase`/`summary` envelope events are emitted by the calling command, not here
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.__init__ fingerprint=4ed2aa9e0869d49d8e23949ed8110d89b7a871df3e40583ca4a3255f3e640612 body_fp=ed2f2597c8e22231b729447e9661770a81f9481bbcc41775ef1e8c7368f7ccc6 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=model -->
Initialise `_JsonlProgress`, storing the output stream and defaulting to `sys.stdout`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress._emit fingerprint=ef26c79f59223ced602854e80b0eb04c17df7245ec17fdecd03c03779caa872a body_fp=971beb4c9bddf0b6963006653790b34402a67003d5f1aa85b06b028d9508e7b9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Serialize `payload` to a JSON line and flush it to `_JsonlProgress._stream` immediately.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_start fingerprint=74eaca981cfa70b628b1cc1cc5426cc694fcfebb59fbf12062bea307de95476f body_fp=2683db1dcf250f0ee3f0ad394a740d81c390dc978e03e7f6211da796d3a8ed5b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Emit a `{"kind": "start", ...}` JSONL event when a file sync begins.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_done fingerprint=3d84dfc675811299240d4290075310a4604fadec0ae7979b800b7a010db19e3d body_fp=f62a0fd4e069a7df2f7c4abc4948bea04ce382df9838ad604e617a9f122f760a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Emit a `{"kind": "done"}` JSONL event when a file finishes syncing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_skip fingerprint=2bbfaf11160d7d62cb1a5ed009bfba8e930785a96ecae21c175c3c2296531599 body_fp=9bea8ebcac4394a952febe994c9f62e34a3de72294bfef4abc075f8707692326 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Emit a `{"kind": "skip"}` JSONL event on `_JsonlProgress`'s stream when a file is skipped during sync.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:emit_jsonl_event fingerprint=376721b7cfba875cf18dba24b9a39760deddb6042f3ef16032fa0f771876b330 body_fp=52fc86c50bc5b738dfb9cece5881ce42b0cdd1d81442f747996d374c86fd481f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
Serialize `payload` as a JSON line and flush it to `stream` (defaults to stdout).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=a5d28922bc774eedf46b515668c61a5a97ca0ba9ba85c53cf9973ad7a6638fbc body_fp=2a7362fcca878752903807572d546e2ce268a98bd13ad916f775c21671a0dc2c source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Context manager that acquires a write lock for the duration of a command or exits with code 2 if contended.

- Operator-typed commands get loud failures with exit code 2 when lock is held
- Hook-driven refresh commands get queuing semantics instead
- Exit code 2 is transient (retry), exit code 1 is non-transient (fix input)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=859e3d6404385b287b81cd355ad8cafa07d0c07eae791ae3813f22012c2a8aab source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=entrypoint -->
Typer root callback that initialises the shared `Reporter`, enforces mutual exclusivity of `--quiet`/`--verbose`, prints the version, and bootstraps telemetry before any subcommand runs.

- `--quiet` / `-q`: sets `Verbosity.MUTE`; mutually exclusive with `--verbose`, exits 2 if both given.
- `--verbose` / `-v`: sets `Verbosity.VERBOSE`.
- Stores the configured `Reporter` on `ctx.obj` so subcommands retrieve it via `_get_reporter`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=52afde59a26d405cc036b366b295146b0eed8023a9fac07aac13a10894a8eff1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Configures telemetry from trie.toml debug settings and emits a CLI invocation event.

- Silently handles missing config files since `trie init` runs before trie.toml exists
- Emits "cli" event with subcommand name and argv tail for usage tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=1d3815663e939a183a3615fa14bce2303216da8109575c962b16755709c45c26 body_fp=1e721f00f18c1320eebcf87ead4914d8ef86ea5ea1286ebf80f02b2ecd3e7c5d source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Create trie.toml config, update .gitignore, build symbol graph, optionally install pre-commit hook, and offer to run setup.

- `root`: Project directory to initialize (defaults to current directory)
- `force`: Skip Python project detection and overwrite existing config
- `install_hooks`: Install pre-commit hook (prompts in interactive mode if None)
- `run_scan`: Build symbol graph after config creation (default True)

Materializes `.trie/graph.db` when scanning, acquires write lock to prevent concurrent initialization, reports success/failure for each step, displays next-step recommendations, and offers to run `trie setup` interactively.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=5099d8aaf3feec3989a06e12a790bd7622b9cff2ccd17a0557f36de69be14319 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Checks if stdin is a tty to determine if interactive prompts are safe.

• Returns `True` when stdin is connected to a terminal
• Returns `False` for non-interactive environments (CI, pipes, redirected input)
• Gracefully handles environments where `sys.stdin.isatty()` is unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_prompt_select_targets fingerprint=e20665fd0430702ade14c0dda97ce30b4012c0f6588df62c8b92b2f894e9b5b6 body_fp=7ac5d6c31b7f730370093380bed88bbe9c6fcf5a612152e935235502ab99c6f1 source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=util -->
Prompt the user to select which detected agent harnesses `trie setup` should wire in, returning their slugs in detection order.

- `detected`: slugs of all auto-detected agents; caller guarantees len > 1 and tty
- Returns slugs in the order they appear in `detected`; re-prompts on unrecognised input
- Default selection is the single override-capable harness when exactly one exists, otherwise all detected
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=d790cb8c8d4f3ea375951462dfe2095143e9a766cb0eb0e6b95154f3237889ca source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Context manager that does nothing; used to conditionally skip status indicators.

Implements the context manager protocol with no-op enter/exit methods, allowing code to use `with _NoOpStatus():` when a status indicator should be skipped while maintaining the same control flow structure as when a real status manager is used.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=08d221cc7a674a413ae90dd3f89994efdfbea0d74604458cd0f0198abd7e45ed source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
_NoOpStatus.__enter__ returns self to implement the context manager protocol as a no-op.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=7fcaa154ca4cba7b928bdfd4e5d6ed7394387fc74c2aa227a857e1321eeb9cf3 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
`_NoOpStatus.__exit__` implements the context manager exit protocol, taking exception parameters and returning None.

- Always returns None regardless of exception arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=392a35fcab27024390840bdc07a64b1d2275bc23f49e4982eb90baf4d9a5d597 body_fp=d2f0fae6485eff39c83dba42ae8758cf55d2fcf0fa824a54e45e0d8f8584f75c source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Scans project for drift, computes either incremental or full-bootstrap worklist, and displays estimated cost before any LLM work begins.

- Auto-detects incremental mode (stale files + cascade) vs full re-bootstrap based on existing triefacts unless `--all` forces full mode
- `--offline` skips the `count_tokens` network call by substituting a zero-token stub, printing the worklist with all cost estimates as $0
- Performs drift check first but continues on drift (informational, not a gate)
- Acquires write lock to ensure consistent store snapshot during planning
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=3182dc32d5135484a723e7e1259b7fa50871036159d113c4aa82c3257476827a body_fp=b1be616430a9b201bca45907bd2e1500a648b462e02f4479997676e0a0b1812a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Runs bidirectional drift check and exits with code 1 if triefacts have diverged from source code.

- Detects both code→triefact drift (source changed without regeneration) and triefact→code drift (tampered sections or deleted symbols)
- Designed for pre-commit hooks and CI environments - no LLM calls, no database writes
- Same drift detection logic used by `plan` and `sync` commands, exposed as standalone verification gate
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:status_cmd fingerprint=e069c10392687d5c5efd6e5e66ab595767b99099008bcbf0388eab0623ce4462 body_fp=5863a3f9e9895b8576d760f66e31dd66005ae09376208a93c7cb8d024d773a76 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
Reports trie's working state including active writer status, stale triefacts, and pending edit patches.

- Performs offline content-drift scan using same checks as `trie verify`; passes an open `Store` as a fingerprint cache to `check_project`
- Unions drift results with refresh-computed pending set for complete stale file list
- Queries graph store for patch summary including modify/create patch counts
- Outputs either JSON object (with patches field) or formatted prose based on `--as-json` flag
- Safe to run during active sync operations as it only reads status files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=9ad893426718b3f4d7092ec0d27c95d453461a354f84ee952bc3592cc2ba64fc body_fp=41e06c95faf3887f89fd70aa5e49649a91bfaca2f7681d8a2c7be2ec6234ae31 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Probe whether another trie process holds the project's write lock, exiting 2 if contended.

- Designed for pre-commit hooks to detect racing `trie sync` operations
- Exit code 0: lock is free or project has no trie.toml
- Exit code 2: lock held by another process, caller should retry
- Uses acquire-then-immediately-release pattern that never blocks or interferes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_graph_only_sync fingerprint=4c5d863696f5ba2c929eb80cd8963d0843e467495348527317636c8cf3608a64 body_fp=4c2b64cf400e13ab6dfe4be416b02d464a0104ece3f0d26c5c7dec7bf618376d source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=orchestration -->
Rebuild the symbol graph and stamp freshness for `trie sync --graph-only`, without any LLM call.

- `before_turn` — selects `ensure_fresh_before_turn` (pre-turn gate) vs `ensure_fresh_after_turn` (post-turn sweep)
- `as_json` — mutes the Rich reporter and emits JSONL events to stdout instead
- Contention is handled by coalescing: on lock conflict, marks a queued tail pass rather than exiting 2 (hook semantics, not operator semantics)
- Raises `typer.Exit(1)` outside a git repo (`NotAGitRepoError`) or when config is missing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_graph_sync_progress fingerprint=ad4958aee008ab0926b0f9f63526e80c1a36229c413fc075ab443e29a18ae23a body_fp=6c864f4288010ffd072130b9de3d6f71b53c6bfa53299cf22c6dac0503ae3cbd source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=orchestration -->
Context manager that selects and yields the correct `ProgressCallback` for a graph-only sync, always mirroring into `.trie/` activity state.

- `as_json=True` yields `ActivityProgress` wrapping `_JsonlProgress`; `False` yields one wrapping `_ProgressAdapter` with a Rich live bar.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_freshness_json fingerprint=4597cfd483b0bdde0922cb779487e1ac288f00781eaef91d788b545437eace61 body_fp=0269407af2f7209cf7c1c479ba23b1266be1c1c8e63e623ee93d857c26b134d7 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=io -->
Emit a `{"kind": "summary"}` JSONL event encoding a `FreshnessResult` graph-sync outcome; drops the `files_synced` and `cost_usd` fields present in the previous version.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=5989cc5b45cbe487d1776d94c865e2201e4600c6aad044808cf51713be95ce49 body_fp=a5fc9e94a729a5c3ebea8db4e41b0ee47fe60872c0c6c1ec9f6cccf08a5704f3 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Render one line per graph-sync outcome with two clauses: graph state and prose freshness.

- Always emits both clauses regardless of `result.refreshed`; stale prose triggers `reporter.warn` instead of `reporter.success`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_AUDIT_TAIL_BYTES fingerprint=988e06fd434d4fb62e32a6167721980312ced4e8b1a3ff48967660d9677b18aa body_fp=cd2eb539e069c103b37acaf0996b1b8e6e274409a1411a7978b0b73635b43778 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=config -->
Default read window for `audit_cmd`: limits JSONL parsing to the trailing ~4 MB of the log file for speed; pass `--all` to override.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=67fc1fe9613a92bd595bf468ba64ed9927f1c36f87d5093efb78b9cc20b19767 body_fp=1a71be4dbdbbc0e64b2cd95586c628f18e208bd528d93fc8becbf0d0562f37cd source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
Summarise telemetry logs with MCP usage, sync activity, retries, and CLI invocations.

- `--log`: Path to debug.jsonl file (defaults to configured debug.log_path)
- `--compare`: Render side-by-side comparison with deltas (candidate vs baseline); always reads fully
- `--json`: Output as JSON instead of human-readable format
- `--all`: Parse the entire log; default reads only the last ~4MB tail
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=82168e8ec7edc73bd791d28e3cfc2b65fbcde418535265e5ac087321c1cee77f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Resolves the audit log path for `trie audit` command.

• Falls back through: explicit `--log` flag → config's `debug.log_path` → `./debug.jsonl`
• Returns absolute paths, resolving relative config paths against project root
• Allows cross-project audit by not requiring trie.toml when explicit path given
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_intent_gate fingerprint=124bbd271ea315303b54d48261532e35a866ad2e7d7913d204a3fa478a2d6042 body_fp=e1ad4abc89c1053c537eaabbea99e91bc2ee3f653640175b33eea9b73f0b09ba source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=domain -->
Evaluate the intent gate via `trie.intent_gate.evaluate`, render the outcome, and return `True` when all touched symbols have patch notes on record.

- Returns `False` and prints a copy-pasteable worklist when any touched symbol lacks a note.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_warn_on_version_skew fingerprint=8e948cb365beaa2acd7d3e27d9578d3316ddec7ba633ac2f3ee6bc6caff3422b body_fp=20377768ff9f56ccf3bb80bf2a09d4e75746898419d403090ef6431c0c5c7b0c source_ref=f803cb599a03936d496cac84820bfd4e78a600a2 role=util -->
Warn via `reporter` when the installed `trie` binary version differs from the version declared in the project root's `pyproject.toml`.

- Only fires when `pyproject.toml` exists and names `"trie"` as the project; silently no-ops otherwise.
- Advisory only — never raises or blocks the caller.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:gate_cmd fingerprint=0ca676558220b3e074f863daff5fa45ab48c8c376936521d5dffeec3dac3e140 body_fp=2d444fe4010bab8eeea43bfe983e9c53a1dd2aa25b38a30205015169ff7c39a6 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Run the full pre-commit guard sequence: version-skew check → lock-check → verify drift → intent gate → digest write.

- `--no-digest`: skip the digest write; runs only lock + verify + intent.
- Exit 0: all gates pass; exit 1: verify or intent failed; exit 2: write lock contended.
- No-ops cleanly when no `trie.toml` is found in the current directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:intent_cmd fingerprint=42b1f6bdceb860f506eafa96f140cd0d81b726b5c8f152de881e9094d76a99a0 body_fp=173050fdb17d406d2dc6ca566b85533ba3498d0eb2a06758e443c668057ab815 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Enforce that every symbol changed vs HEAD has a patch note on record; exits 1 with a copy-pasteable worklist when coverage is missing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:index_cmd fingerprint=03be3ee88a8f66b5d0fcb774638b5784f0ff798428a46ca21c6d844027dd6ab2 body_fp=8d3aba6f7dd4eb53e26e97a40b98242febf33e4be4b24044ab45b1a13661414e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Regenerate the triefact-tree index (`<triefacts.root>/README.md`) from the live graph store without calling the LLM.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:diff_cmd fingerprint=d688004861efa2c07fa47c916179ab285fa34e31c648c7201c1f7b2ab1eb4550 body_fp=0a1b18d7d3aed3ccee66210e5cd20d4ad0998ae56ad168722e750a727ec388ca source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Typer `diff` command that collects session evidence (triefact git diff + patch notes) and either synthesises an LLM narrative, dumps raw evidence, emits JSON, or writes a digest entry to the configured `diff.write_path`.

- `--base`: git ref used as the diff baseline; defaults to `HEAD`
- `--raw` / `--json`: mutually exclusive; skip LLM and print raw notes or JSON envelope
- `--write`: pre-commit hook mode — delegates to `_run_digest_write`; mutually exclusive with `--json`
- `--model`: overrides `config.models.cascade` for narrative synthesis only
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_digest_write fingerprint=0443c9cee11db826180b5a19cfe6e8377ec46a8cc8a7f88a5ba10069a5015774 body_fp=8ef19f610186221f5542b49c1330a8c505428da3210f04d01e26ac73d6259782 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=orchestration -->
Collect session evidence, render a digest section, write it to the configured diffs directory, and clear applied patches from the store via `store.delete_applied_patches()`; shared by `diff_cmd` and `gate_cmd`.

- `stage`: when `True`, also `git add -A`s the digest archive dir and symlink for an in-flight commit.
- Returns `False` only on hard `OSError`; returns `True` when a digest was written or there was nothing to record.
- `raw`: when `True`, skips LLM narrative synthesis regardless of config.
- Amend/retry: if a digest entry for the same parent commit already exists, its rows are folded into the evidence and the file is rewritten in place.
- No `session` parameter or digest cursor; evidence is consumption-based (pending-intent file + staging queue).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=34ad2b8e98bf414eaf8a533a8b75ac271dbae3edca2b2d73052de585e4b60969 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a colored breakdown of files scanned by status and symbols/edges count.

- Renders new/updated/unchanged/removed file counts with color coding
- Falls back to "no files in scope" when no categorizable files exist
- Shows total symbols and edges written to the database file
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=a3fad1a65c7d23db83f84ab7550e57151bb55d0228a974dae2657c75b00605bd source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a bootstrap plan summary showing model, file count, total cost, and top 10 files with their symbol counts and estimates.

- Displays total estimated cost formatted to 4 decimal places
- Shows first 10 plan items with file path, symbol count, score, and per-file cost
- Adds "… and N more" footer when plan exceeds 10 files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=7d25e63d4726fe5f82eb8328587f26dafdb4888e59a3a3fec7f1f3399867bea1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Print incremental sync plan emphasizing actual work order and symbol-level impact.

- Displays files grouped by directly stale vs cascaded, ordered by execution priority
- Shows symbol-level breakdown (how many symbols will hit LLM vs total documented)
- Lists orphan triefacts that would be removed, truncated at 10 items
- Preserves bootstrap ranking within each execution tier for cost visibility
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_REASON_LABELS fingerprint=a74cd9fa61964b8516ebff4efdf8859fa2ff50596c2b3765caf8b2d964d0c5cd body_fp=41637c91a10ea3f8163d99b0cca22671a00d986f7952e841c2440a25a9887c8e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=config -->
Maps StaleReason enum values to human-readable labels for drift reporting.

- Used by `_print_drift_detail` to render per-file drift items in a user-friendly format
- Keys are StaleReason enum members; values are descriptive strings for CLI output
- `TAMPERED_BODY` label now includes actionable guidance directing users to move prose outside sentinels and run `trie sync`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=698bcad70ac9d737c38314e3d26f0d384ff76f3b86cdcad26f47397e3c262b21 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders drift check items grouped by triefact file with colored status indicators and indented issue details.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=e1756d124c46c591211c8188a85a2319d1a72a9fdbabfbf20bad7e49e0c2ca75 body_fp=69c5e13eef8ad6f611dd0d4a1a02e05232db6960b5e9e7b9ffe5b6aa62c82ae9 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=domain -->
Checks triefact tree coherence and reports drift, returning True if clean.

- `exit_on_drift`: When True, raises `typer.Exit(1)` on drift (for `verify` command); when False, warns and continues (for `plan`/`sync`)
- Opens `graph.db` as a content-addressed parse cache to keep the check under budget
- Returns False if drift detected, True if tree is coherent
- Reports detailed drift items when verbosity is MEDIUM or higher
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=bd60267768471ecf35dc486645dbf74508e6972988b7daa520fe467f6bb3815b body_fp=9c813753a738c281515686cb83153e90d4a01e259438434894cdef2ca839d1d5 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Dispatch the `trie sync` CLI command to the appropriate sync sub-mode after validating mutually exclusive flags and acquiring the write lock.

- `--graph-only`: rebuild graph + freshness stamp only; no LLM; implied by `--before-turn` / `--after-turn`; incompatible with all LLM flags.
- `--before-turn` / `--after-turn`: hook modes that imply `--graph-only`; mutually exclusive with each other.
- `--json`: emit JSONL progress; only valid with `--graph-only`.
- `--file`: sync a single source file (stale symbols only by default); requires `--force` for full cold rewrite.
- `--all`: force full re-bootstrap even when triefacts already exist.
- `--budget`: USD cap; stops once cumulative actual cost reaches this value.
- `--limit`: maximum number of files processed before stopping.
- `--dry-run`: regenerates into `.trie/preview/` and prints unified diffs; still makes API calls.
- `--metadata-only`: rewrites front matter from the store only; no LLM, incompatible with most other flags.
- `--roles-only`: re-infers role tags without regenerating prose; `--rederive-taxonomy` forces vocab rebuild.
- `--force`: cold-regenerates every symbol in `--file`; invalid without `--file`.
- Default (no flags): bootstrap on a fresh project, incremental cascade otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=0a62d5928c91a171e378bd5fab17ad701335a6b91b910ea6c795000ccad9b267 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Returns True if the triefacts directory exists and contains at least one markdown file.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=e525efbf503ab98d85cc1594568ac0286bf2411e58b398b0043ec23c32dfb9b8 body_fp=b7c98a5dcfd7e9ad1ac2b9711601e782176f00d105d02f7bdba8f80ce6bb1675 source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
Executes first-run bootstrap sync: scans project, builds plan, prompts for confirmation, then generates triefacts and refreshes the index.

- Requires budget/limit or interactive confirmation when no cap is set
- Scans project and builds token estimation plan before proceeding
- Calls `_refresh_index_quietly` after a successful sync if any files were synced
- Calls `stamp_graph_fresh` after the store closes to mark the graph current for subsequent graph-only syncs
- Reports per-file errors via `_report_sync_errors`; exits with code 1 if any occurred
- Reports final cost comparison (estimated vs actual) and files processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_refresh_index_quietly fingerprint=d529f7105e01e70c95ec0edde7ecd5d69d83d6a4b700b9586c39ec54c6ad83d6 body_fp=157f92062beabea3f06f4d4fb44d43034a1b6fdc4bb0eed344927dec5d9dbe30 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Regenerate the triefact index after a sync, silently swallowing all exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_sync_errors fingerprint=728c6f436fd1675b4a5e8b61b79f8776946aa9129a1e2634405f94b84d5323ba body_fp=dfd62a66da3f7a3aaa2ed6f59513040657558f6b4af2e41c5de6ac6e8d04adc7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Report per-file sync failures to `reporter`, printing up to 5 errors plus a credential hint when error text suggests a missing API key.

- Returns `True` if any errors occurred, `False` if `file_errors` is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=aef73997fa835e6c4cb57d5089fed793e34be8fbd933335d2ba9ff6d1f88985f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=domain -->
Implements `trie sync --dry-run` by regenerating stale triefacts into `.trie/preview/` and printing unified diffs.

- **model**: Uses `models.bootstrap` if not overridden
- **budget/limit**: Caps LLM cost and file count
- **output**: Prints per-file diffs or notes fingerprint-only changes
- **exit**: Reports total cost and skipped files due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=e5cd7f2d73c04c4046b29c44387cffed3a1156f0b63e05ca1ae792ff6e7739aa body_fp=2774eaa34dbf417e88763a86d94a1af60b3a2649baf49fc5b56e9248bfacd963 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
Sync one source file's triefact, regenerating only stale symbols unless `--force` is given.

- Without `--force`: opens the graph store and passes it to `check_project` to identify stale symbols; exits early if all are fresh; passes `symbols_to_regen` to `sync_single_file` so fresh sections pass through byte-identically.
- With `--force`: skips drift check and cold-regenerates every symbol.
- Exits 1 if `file` doesn't exist, config is not found, or the file is outside the configured source root.
- Reports symbol counts distinguishing regenerated vs passed-through, plus token usage.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=181b6716a37fd19e6aa687d794cdba69cba15c48420f9c798a50e0fd1548f57c body_fp=2610850b71686d88db275fb5171fec7ed92a156e32f17703345cf491fc206ac0 source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
Refreshes triefact front matter from the live store without LLM calls, designed for post-graph-change updates.

- Rescans project to pick up new edges from resolver changes
- Updates ref counts and defines entries for each in-scope triefact
- Skips files outside source_root and no-ops when metadata already matches
- Calls `stamp_graph_fresh` after the pass so the next graph-only sync no-ops
- Reports changed count vs total processed files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_roles_only_sync fingerprint=23f7dfa386342155618233ac03b5c009c87e48a694cbeb3f741f37e4984e9fc8 body_fp=26d7522df98b95ad2bf9c30d189042024a6ff9e7f4c90ea9e0809e170ecb5c7d source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
Runs the roles-only sync mode: derives/loads role taxonomy then classifies every symbol against it without regenerating prose.

- Scans project first to ensure store reflects current source
- Uses cascade model (or override) for role classification
- Stamps graph freshness after the scan so the next graph-only sync no-ops
- Reports taxonomy derivation, symbols classified, and role changes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=a6f849b8ffac64772326ad46e9af0e7a9e00b371320dde829a37ae3c9833de0a body_fp=c3b2d6946d97926e55822892a1c40e988fda174751f5b6e287901c1e3359d45b source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
Execute an incremental sync that regenerates only stale triefacts and their cascade dependencies.

- Loads project config and opens the SQLite store with activity progress tracking
- Calls `run_incremental` to sync directly stale files and their cascade neighbors; calls `_refresh_index_quietly` when any files were synced
- Calls `stamp_graph_fresh` after the sync so the next graph-only turn hook no-ops
- Reports orphan triefact removals and sync statistics to the user
- Calls `_report_sync_errors` after syncing; exits code 1 if all files failed or any file errored
- Honors budget/limit constraints and reports any files skipped due to those caps
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=5628da5c475d18230f6a33c60d1b52e23cb950fa7d8e3503390153f058b060de body_fp=3072b3df04e1c5f26617b1554bfe15f4afadfa567a88d01f577aff011218eecd source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=api -->
Integrates trie into coding agents by installing hooks, tool overrides, documentation, and GitHub workflows.

Orchestrates multiple install steps in sequence:
- MCP server registration (optional, via `--with-mcp`)
- Turn-boundary hooks for automatic refresh after agent edits
- Tool wrapper overrides that replace agent built-in `grep`/`read` with trie equivalents
- Agent-facing documentation (TRIE.md and pointer updates)
- GitHub Actions workflow that comments the latest session digest on PRs

When no `--target`/`--all` is given and multiple agents are detected interactively, prompts the user to select which to configure; exits 0 with a message if none are chosen. Target auto-detection resolves which agents to configure. The process is idempotent — re-running safely overwrites existing configurations. Agents without automation support emit manual setup instructions. Exits with code 1 if any install step errors, including the workflow install.

- `--no-overrides`: Skip tool wrapper installation, leave agent built-ins unchanged
- `--scope`: Install in project directory or user agent configs
- `--dry-run`/`--print-only`: Preview mode without file modifications
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=9c0c752d54c3dcfa921629d39973d8145b811fdd047a21cf7002c9a974f78517 body_fp=00d3d6b6fe11ea59d9146ce4c158ed543a0cdce62c72547fc54a4a6c833a62d5 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders a combined setup plan report grouping MCP, hook, and override results by target with a separate docs section.

- Groups results by target slug, showing each target's MCP/hook/override outcomes indented under its display name
- Emits manual setup warnings and JSON previews inline where applicable
- Renders docs section separately since it's target-independent
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=1ede2878bb98b6df394615cdd58ab4ecae185270f43cadf83ab95df212d1565d body_fp=ba615a58540e306c9db7664acb2bee499d1e8cd67c59c83657c1c5497905c5a2 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders tool-override install outcomes for a single agent target within the setup command output.

- Prints summary line showing override action status
- Lists per-file outcomes indented beneath the summary  
- Handles manual setup notices for unsupported agent harnesses
- Uses Rich markup for consistent visual formatting with hook install output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=33f2a0af34ece204faf67aa6c95cef95a890aaeba6f93c9a8f92484e6ee2a603 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Formats an installation action result as a display string with optional path suffix.

- Returns `action` alone when `path` is None, otherwise `"action → path"`
- Used by setup command renderers for consistent MCP and hook line formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=21c17059efeb9d659493f91f06cd3aea63b05d387ef3446792e9d5aa97a2a34e source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Resolves project root from trie.toml and returns TrieTools instance configured for CLI telemetry.

• Returns TrieTools with event_name="cli_call" to distinguish CLI usage from MCP calls in audit logs
• Caller must close() the returned instance to release SQLite handle
• Raises typer.Exit(1) if trie.toml not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=cbf61b9c556d479acf0bd9aed32381243ee9cfdf00343a76c3dd1ad871c43a26 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints envelope as raw JSON or via provided renderer, exits with code 1 on errors.

- `as_json=True`: dumps to stdout without ANSI codes for agent parsing
- `as_json=False`: delegates to the provided renderer function
- Error envelopes always render through the renderer for human diagnostics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_patched_tag fingerprint=dc648bd9f208afe7454d79f5eebafca65d77f7014569d3999b97bf3f93928efe body_fp=9be02189078c57ce4a27212a4894416ac6166c915a7c4f9a97ad4f402d2f6f8b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Returns a yellow `[patched: N]` tag for count > 0, empty string otherwise.

Used in grep and trace output rendering to visually mark symbols with pending edit patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_grep_output_is_tty fingerprint=954ccea2a94869ba8560359233d58c8ec8285b5f8ffdb13508098fceca9bd8b5 body_fp=acad7e4bba0cd81d4e2f5b75525f95c444d86ad83b7133a7d87a2cd558dbec67 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Return `True` when `sys.stdout` is an interactive terminal, guarding Rich table rendering in `grep` output.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_grep_records fingerprint=f05dbd1300d4c47bc7b053331ccf3a8112249ac363c8b2336e857ef8a145bf93 body_fp=aec7acdcc1919edaf32ea6e8be0adeca5142ba1e65bf2dd5c060da9c08548e62 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Print grep hits as plain, full-width, one-record-per-line output for non-tty consumers.

- `qname_suffix`: optional callable appending a tag string (e.g. patch count) to each qname before printing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=e1ab9766de8658fbd35cc7a4c2034fb9b13475d687024bf152efd8b0c7c640d4 body_fp=0e2b6435f2e778ac6f253ecc30f160054251e3524f3dd03fc05e2ece444412a7 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Renders human-readable output for `trie grep` command results.

- Interactive terminals (tty) get a Rich table; piped/non-tty output gets plain untruncated records via `_print_grep_records`
- After hits, prints any `related` (prose-matched) symbols
- Falls back to candidate matches table (or plain records when not tty) when no exact hits found
- Shows pending patch counts as yellow tags on qnames
- Routes errors to `_render_error_envelope` for consistent error formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=2b10e36d759a5d0ea615a7db338822b6231723a2963b138ff8997b4262a3a179 body_fp=3db1c6f1a65ef2556ff8fb722d590775f841997ccd4986e572e2cb470af0c10d source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders human-readable output for `trie read` command responses, displaying symbol metadata, notes (before prose), prose, pending patches, caller/callee relationships, and a history block.

- **envelope**: MCP response dict containing qname, signature, source_pointer, prose, callers, callees, pending_patches, history, and notes
- **reporter**: Console output handler for styled text rendering

Formats the symbol's qualified name and signature at the top, then prints any `notes` entries early (⚠-prefixed notes in bold yellow, others in dim) before the prose block, followed by pending patches with their origins and notes, then caller and callee lists with one-liners, then a `history` block (date · change lines with optional title), and finally notes again as yellow-banged lines. Error responses are delegated to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=1af973f434ca837af6bd3bf7f5f4a14871b62746089ef1d6845c6f30cd474b15 body_fp=08321fb0893b819f18aa414844c848fb130b915d9321331e40e4d9e000bc7bc8 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders human-readable output for `trie trace` command responses.

- Displays root symbol with its one-liner description if present
- Lists all nodes in the trace with qnames, one-liners, and pending patch indicators
- Shows edges with directional arrows (→ for outbound, ← for inbound)
- Reports truncated hubs and any diagnostic notes from the trace operation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=29e06ccfb00bd8f211685d85fb3a46d9de82717423194f02d0f6dea1b11b353f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders standardized error envelope from MCP tools into human-readable form via Reporter.

- **err**: error envelope dict containing `code`, `message`, and optional `suggestion`
- **reporter**: Reporter instance for formatted console output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=7f410b69de496539d7948c4e8a86a399d45babc4ab7286234153ca799a704dc5 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Assembles a search predicate dictionary from CLI flags for the `trie grep` command.

- `predicate_json`: Base JSON predicate; individual flags override matching fields
- Constructs nested `inbound_count`/`outbound_count` objects when min/max bounds provided
- Exits with code 2 on invalid JSON to distinguish from other error types
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=8c43a494fcb2e3b2468d86052eaee440d5a34a0ab7bad2281fbdf8a0f1dbeb87 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
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
<!-- trie:section symbol=trie/cli:read_cmd fingerprint=658656804167b1ab001b1fae44c199006876251ce97e55828ca5821527066a70 body_fp=2a35bd35ab6d0ab332683838e820dc2e69799093a40ec2279e8192f1ce2fd81e source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
CLI command that reads source code or trie's synthesised description — dispatches via a single `tools.read()` call.

- Accepts a symbol qname **or** a file path as the positional argument
- `--full`: for file paths, returns every section's full prose instead of the compact triefact view
- `--source` / `--offset` / `--limit`: force raw line-numbered source with optional windowing
- `--history` (`-H`): also retrieves the symbol's or file's intent trail from the session-digest archive
- Delegates rendering to `_render_read_dispatch`, which fans out to `_render_read_source`, plain output, or `_render_read` based on envelope shape
- `--json` emits the raw MCP envelope verbatim; mirrors the MCP `read` tool wire response
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_dispatch fingerprint=2259360f989712d808ec20d13c4379463c02d8176fc94e720e458dbbb7a384d9 body_fp=93d96bba49f5483e3faf0566d24c684b1c11e8e933601bf7aa130bac37f4d8f7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Dispatch a `tools.read` response envelope to the correct human-readable renderer based on its shape.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_source fingerprint=fddcf9841287b22b0ffbf1e488f06c1ae46eacc63bd5bc0397b58066053c792b body_fp=2c21247aa600ab31b580d3ba509b35df8cbe2e05f7a97108985455e7adf1c980 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Human-readable renderer for `read_source` tool envelope responses.

- **err**: renders error details via `_render_error_envelope` and exits early
- **lines**: prints the source content directly to console
- **more**: shows paging hint when result was truncated by offset/limit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=4163cf535b50888684695017b4ba5cf75abd1a6767961b77d6fca069e7504675 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Trace call graph from a symbol outward up to specified depth, mirroring MCP `trace` tool.

- `qname`: fully-qualified symbol name to start tracing from
- `direction`: "callers", "callees", or "both" (default: "callers")
- `depth`: maximum BFS depth, clamped by config trace_max_depth (default: 2)
- `as_json`: emit raw MCP envelope as JSON instead of human-readable summary
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:blast_radius_cmd fingerprint=894cae88c8d009e068480f6da6493330bd52972377fa29f98bafe7539b4018b8 body_fp=25631381b6dd206cf283cede3d0f81a3263ac20b190c1e5d4cf16cadecde0b60 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
CLI command that computes the cascade blast radius of editing a symbol using free graph traversal.

• `qname`: fully-qualified symbol name to analyze for edit impact
• `as_json`: when True, emits raw MCP envelope instead of human-readable output

Reports every symbol whose triefact/source would be regenerated if the target symbol changed, with BFS hop distances from the seed. Makes no LLM calls—pure graph mathematics for impact assessment before risky modifications.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_blast_radius fingerprint=beec4a79525cc1ed8a249725a02cdf21768f500a1f84520ed235826beb32b13e body_fp=4cfb51b9b368d85273371bdad8292123fc3a5450ff05480da297b345d0fef286 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders blast_radius tool results in human-readable format for the CLI.

- First checks for error envelope and delegates to `_render_error_envelope`
- Prints the target symbol name and file location in bold
- Shows summary line with cascade count and direct caller count
- If cascade data exists, renders a Rich table with hop distance, symbol names, and file paths
- Falls back to "nothing else depends" message when cascade is empty
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plain fingerprint=4e5a2ebce1788aca6bfb58561caace523dda494204fee5186aadb85ddf260e0e body_fp=41da52e6393b120069b4da2c4cc69db918db307e8b02fea5d759de05870326c8 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=util -->
Renders MCP tool response envelopes as human-readable text. Checks for error envelopes first and delegates to `_render_error_envelope`, otherwise formats via `render_envelope` (not raw JSON).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_str_cmd fingerprint=ccf204ad8e903d6d88f247f32e32194d53194c152bec93aa846d64889fc83b01 body_fp=0491d2244fbab8743e51898e46c4addc4864e802a9c5dd66593b6d9c85e81106 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
CLI command that searches source file bodies with a regex pattern and attributes hits to their enclosing symbols.

- Supports `--all-files` flag to search the entire repo instead of just indexed source files
- Calls TrieTools.grep_str_all() when --all-files is enabled, otherwise TrieTools.grep_str()
- Supports `--json` flag to emit the raw JSON envelope instead of human-readable text
- Closes the tools connection in a finally block to ensure cleanup
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:find_cmd fingerprint=d5f94e0ba784d4e22c80f0ccc4a2021ae81fd1c1c78d7f75fe60c6a9f6a08405 body_fp=9fc74dac3e1ccdd081c3169a39ae9d3f8d01feabf377e50b1b5e38aa7f05fe79 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Searches project files by glob pattern, returning paths sorted by modification time.

• `pattern` — glob pattern like '**/*.ts' or 'Dockerfile'
• `indexed_only` — restrict to files in trie's scope (default searches whole tree)
• `limit` — maximum paths to return (default 100)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:write_cmd fingerprint=cf4b365e8c07b479bc6f52e78297ba187d19175ffac9258ec50a745b18964006 body_fp=e789613e78ddb1111405d8638189cee4355a1dfcf1fd834185e895e8d258c4e0 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
Implements the `trie write` CLI command to create or overwrite arbitrary files under the project root.

• **path**: File path relative to project root
• **content**: File content (reads from stdin if omitted)  
• **overwrite**: Allow replacing existing files
• Uses `TrieTools.write_file` method and renders output via `_render_write`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_write fingerprint=d176d38c585431d5800d9b9a754b58989d01a18652091e502d06dc267fbfca11 body_fp=536304b144fdebc367a52dfefc2970f15a3e05408a42530d8e0486df9d4c4daf source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
Renders a write_file envelope in human-readable form for the write command.

- Delegates error envelopes to `_render_error_envelope`
- Reports "created" or "overwrote" based on the `created` field
- Shows file path and byte count from the envelope
- Advises running sync/refresh if the file needs indexing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_find fingerprint=33aeb9572d75fb7b54cc8ba23acd8213c8a6c087e002c5264d9d8b344a2825cb body_fp=a2c9e3a8a61ed32625159ebc89cdec25d3f64e2f6be0bf23f0413be8700c877d source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders human-readable output for the `find_files` MCP tool envelope.

- Prints error details if the envelope contains an error
- Lists each matched file path on a separate line
- Shows file count with truncation notice when applicable
- Reports "no files match" for empty result sets
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_entry_points_cmd fingerprint=cecda4c2cf1f3c3187effab443ead8ed4956f23ee38328f1bbe8627486f20793 body_fp=ac4243053e2187be3fd71aefc263a7ada7b4635ad53c2752bf7a2117d21c7494 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
Provides the `trie grep-entry-points` CLI command that searches for architectural entry points by topic.

- `query`: Topic or concept to match against symbol prose in entry points
- `as_json`: When true, emits the raw JSON envelope instead of formatted text
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_cmd fingerprint=be4d9c029580187b7e0b58a499d8cef731e4860c213f9c0169599d734e837f91 body_fp=18ebb54d954567498e1bca586f5c7621287b7f256c0f81ecc6f898d270437206 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
Executes fuzzy symbol name lookup via `TrieTools.grep_symbol` and renders results as plain text or raw JSON.

- Adds `--json` flag; when set, emits the raw MCP envelope instead of rendering via `_print_plain`
- Uses `_open_tools` to create a `TrieTools` session from the nearest `trie.toml`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_neighbours_cmd fingerprint=6d966f04c194ea93b0e3894a320c59bfd0c1b1e3bef514f6715ec6e53d383fbe body_fp=443aef593b9f3197bd5eb858e5d0e472066bb70542bdbb66154d3d3312ae0138 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
Implements `trie grep-symbol-neighbours` CLI command that performs fuzzy symbol lookup and returns immediate caller/callee metadata.

- Takes a symbol name fragment to fuzzy-match against the graph
- Calls `TrieTools.grep_symbol_and_neighbours()` to get the symbol plus trimmed neighbor data
- `--json` emits the raw envelope; default renders via `_print_plain`
- Example: `trie grep-symbol-neighbours sync_single_file`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_cmd fingerprint=84e816d28b56e2962473b0f5b1b461c92580d49cf54ba185fa1c84b34bc3603a body_fp=f4ba39dca4ae1ab1c3fc363bec3815c359dea0bf4f22e60db6f8e14f93bbcf67 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
Provide detailed explanation of a symbol including its prose and reference narrative via CLI.

CLI command that wraps the MCP `explain_symbol` tool for terminal use. Takes a symbol qname or name fragment, opens a TrieTools session, calls the explain method, and renders the result. Output is human-readable by default or raw JSON with `--json`.

- `history`: when `True`, passes the flag to `tools.explain_symbol` to include the symbol's intent trail from the digest archive.
- `as_json`: when `True`, emits the raw MCP envelope as JSON instead of formatted text.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_refs_cmd fingerprint=44a32192277efccf17b36b7444cde06e692e8e2ffd663ce1e313e2bc16b4ad8e body_fp=64c8e30c82d1364cb81ea13e78aca863e2edc5774e86d7a908b3ec140f526b98 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
Typer command that explains how a symbol is used by its callers with their prose.

- Accepts `--history`/`-H` to also include the symbol's intent trail from the digest archive
- Accepts `--json` to emit the raw JSON envelope instead of human-readable output
- Calls `TrieTools.explain_symbol_references()` with the symbol name/fragment and `history` flag
- Uses generic `_print_plain` renderer for human-readable output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_flow_cmd fingerprint=30878fb0764545ed3b2c4e41e5bef393d2649e1443fcbe7c3c19581bf4336c6f body_fp=92ee820a5d360705229f3c68f6da61b0f58493bd528a333c06790a5c4f515079 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
CLI command that finds call chains between two symbols via `TrieTools.trace_flow`.

- **symbol1**: starting symbol qualified name or name fragment
- **symbol2**: target symbol qualified name or name fragment
- **as_json**: when true, emits the raw JSON envelope instead of formatted text
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_flow_cmd fingerprint=b936810b259a14ce3067b76bd914d11c5d86110d9bdc6f06614e850340d0f38e body_fp=c805b67712f8fcdb11fc5618303d3c0c9255aa5fd4519bc3deb2eebbc99c6ed3 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
CLI command that traces call chains between two symbols and narrates each step.

- `symbol1`: starting symbol qualified name or name fragment
- `symbol2`: target symbol qualified name or name fragment
- `as_json`: emit the raw JSON envelope to stdout instead of plain-text rendering

Calls `TrieTools.explain_flow` and renders output using the generic plain-text renderer, or raw JSON when `--json` is passed.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_app fingerprint=a01ba84281db5613dd9598b44b9572c2f52e7bf4a145def4e8140840006383da body_fp=0297250842674ecd94a570ce93159fdff3eade05ffef0210ab52062e894e45f4 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Typer CLI application for managing edit patches against symbols.

- Provides subcommands: create (post patch), preview (show apply plan), apply (execute patches with cascade), list (show pending), drop (remove patches)
- Configured with `no_args_is_help=True` to show help when invoked without subcommands
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress fingerprint=88a444531b547feca55d4fda3ad1c55db173b88633bd149775faf38391c33b66 body_fp=fb6070f71b83ae157c59be4141d94e3edd3701f121e2b744d694cb24c26495bc source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Rich-formatted progress reporter for apply_patches operations. Prints structured, thread-safe progress output with visual indicators for each stage.

- Methods called from worker threads, so output naturally interleaves
- verbose flag controls symbol-level detail display
- Uses Rich markup for colored icons and indented hierarchy
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.__init__ fingerprint=1c6ad7264d460fcc4f36e9524e2f5bc1f7ee6bc638d01590eca5e0f665ce4ae7 body_fp=a0f71d7355dc8f9d45ff40d01c4795e5e7c2dee41ec64dd2187f8e2ecf0b3a8e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Initializes _RichApplyProgress with a Rich console and optional verbose flag for detailed patch application reporting.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.stage fingerprint=00a0e5b25af2600c917827df1316312556da14518c19c948a17c6b4f8105174f body_fp=c1f5d9c07788f968d33182a77f2fbc33f519f9ba6937ea7b51665f4d886ed1a9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a stage header message with rich formatting to the console.

- Formats the message with bold cyan styling and a vertical bar prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_start fingerprint=1c9e2af52741b8ee459d4101628f36bc16552d1d167b3afdfa1cb25db55ae2d3 body_fp=8d280285ae0ba5941fbf5ddad5830d282b0415f9f869ef4d7b1963b0cc946fa7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a file processing start message with file path and symbol count.

- `fp`: relative file path being processed
- `symbols`: number of symbols in the file that will be patched
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_symbol fingerprint=1fc9ef71af9d3e0f90361d13907c1059d449a1913c2acbac2a945251d0e7c24d body_fp=af56c37705685b73b7b01c3a996620bda3a9787bc1bb91fc6cfe71495f652a1d source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints per-symbol progress during patch application when verbose mode is enabled.

- `qn`: qualified name displayed in cyan with indented bullet point
- `notes`: patch notes truncated to 100 chars and printed with "note:" prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_generate fingerprint=132b41245a185b2af3aacb3c8c3a18c12c5b09ff296437cde359f630862c6105 body_fp=e46e1034cc995556ab2ad34cc7aba5e7826c44445b1217c55696f5edc8e6b7c2 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints generation progress for `_RichApplyProgress` when verbose mode is enabled.

- Only executes when `self.verbose` is `True`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_fixup fingerprint=26be5de5ef710ac328e60f9b6eea26539ebdc8ecf0c1fd70a4eb97604c07d115 body_fp=354f09f9566eeae08907a9a556595c9a875c735e1f8e767ee2d747ff96371cf9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a yellow gear icon with LSP fixup iteration number and diagnostic count.

- **iteration**: Zero-based fixup pass number
- **count**: Number of diagnostics found in this iteration
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_prose fingerprint=12b3c9eda87bd14def97bc9c6c65327a7d23a45803d936cae5ab3330703ecb93 body_fp=b0639bc61593899e87e2d508c8526ec8c715256200e4a5c909ebacb3cbdf35df source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a verbose prose generation indicator for the given symbol qname.

- Only prints when `verbose=True` was set during `_RichApplyProgress` construction
- Displays an indented line with a pen icon and the qname being processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_done fingerprint=be1e14003b12fc05817ca35f7302feae8c628647d0b7cffb7cef9fef388f8c11 body_fp=e83badb76dd48eb5f9f74567e452bf20d0c6fb5799a937051c55f5132cd99bcc source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a completion status line for a file in `_RichApplyProgress` patch application progress.

- `ok`: determines green checkmark (success) vs red X (failure) icon
- `error`: failure message displayed in red when `ok` is False
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.refresh fingerprint=fa057109cbf67e48f2ca72e4736ffb716951fd64ecb1ac03f8c0afce10bfb4e2 body_fp=91777d45c485266abd077f253512020c315913a09ada1f89e811c761171e90d4 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a refresh indicator for the given file path during patch apply progress reporting.

- `fp`: File path being refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.verify fingerprint=9bb6073c0083b530e9d8a61ec3fe90bde21961bdcbb397e39268aa6d65db357c body_fp=88843d1669232469dd7a92f0b73d40fc967e947a1c92e8d576021241cb8f1664 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Prints a green checkmark indicating the project is consistent after patch application. Called by `apply_patches` at the end of its verification phase.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_close_qname_suggestions fingerprint=43648b44ebab8b775cf26778257e39e5a8f42ddf9248eeca7bce65d59d125f23 body_fp=fbf7b54c143630a9e45425a2b88f9878a75dc1ac2301d559ed80168d0c658013 source_ref=f803cb599a03936d496cac84820bfd4e78a600a2 role=util -->
Fuzzy-match `qname` against all graph-known qualified names via `_close_qname_matches` (same-module symbols ranked first) and return up to `n` suggestions; returns `[]` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_cmd fingerprint=6ef2bbed6b313b75ffe7e40afe0e61a93b665e1c52a71dab6e77f1bc14adcfc7 body_fp=788bef2d2c2f748d1a88158a7062e82e5b41c120c199521dcbe3c0569a3ee636 source_ref=1d35cd8f3622458a5b735a6b27aed37679e0201a role=api -->
Creates a fire-and-forget edit patch against a symbol in the trie graph store.

- `--gone`: records the note via `store.add_patch(..., kind="delete", require_symbol=False)` instead of an FK-constrained insert — routes through the store (not the pending-intent file)
- On `KeyError`, calls `_close_qname_suggestions` for fuzzy did-you-mean hints; suggestions and the follow-up hint are printed to `reporter.err_console` (stderr) so subprocess wrappers see them on failure
- Validates that the symbol exists in the graph database before creating the patch (non-`--gone` path)
- Uses a stable CLI session ID for tracking related patches together
- Returns the patch ID after successful creation on both paths
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_batch_cmd fingerprint=bd311badd034a507c09be8adb49b1401c0ff08b46f8799aa9cb6eeb37f768ab8 body_fp=7948b9ac29a7708441fdf34ced8db90c0f7ebfee1a02641c29a3ea2de60adc73 source_ref=1d35cd8f3622458a5b735a6b27aed37679e0201a role=api -->
Stage multiple `patch` or `create` operations in one call, reading a JSON array from `--json-file` or stdin.

- `op`: `"patch"` (default) modifies an existing symbol; `"create"` stages a new symbol — if the symbol already exists, silently falls back to `"patch"` and sets `"fell_back": true` in the result entry.
- On `KeyError` (symbol not found), the failure result row includes a `"did_you_mean"` list of close qname matches when any are found.
- Items are processed independently; failures are reported without aborting remaining items.
- Emits `{"staged": N, "failed": N, "results": [...]}` as JSON to stdout.
- Exits 1 if zero items were staged successfully.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_symbol_cmd fingerprint=e0385e93e61bcffe98beb1c7409c19582424e8afc7a4de84d89f1b2a742806c2 body_fp=c9d5741ce00c01e0e5ec8e7d2bbea5c9b71e7e50fa4944490c6e67360081bc56 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Stage creation of a new symbol to be applied by `trie patch apply`.

- **qname**: intended qualified name like `pkg/mod:new_fn`
- **note**: what the new symbol should do (required)
- **file**: target source file; when omitted, resolved via `registry.resolve_create_target` (existing module wins, else language-inferred suffix)
- **anchor**: place the symbol after this existing qname
- **reason**: why the symbol is needed
- If qname already exists in the graph, falls back to `Store.add_patch` instead of erroring
- Stores create patch via `Store.add_create_patch` with session tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_delete_symbol_cmd fingerprint=d42b44a08aab95225aa29d2ef76a46ff4a907a793fda7b7ba45a30e5335c6d39 body_fp=b394a6512f0db2a67095c269a1a8cd3bfd16923d6c1f435524aab68ae659b289 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Command handler for `trie patch delete-symbol` that stages deletion of an existing symbol.

- Creates a delete patch against the symbol via `Store.add_delete_patch`
- Warns when the symbol has dependents that will reference a deleted symbol
- Raises `typer.Exit(1)` if the symbol is not found in the graph store
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_rename_symbol_cmd fingerprint=a2a8cc1e28f4751332966ccd372069f40de13ebbcbc3d5294d7e2cb0d4939183 body_fp=2712e95a2e06591d507d60547dcf06e7531337016d14b747db51f5f830cec1ee source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Stage a rename of an existing symbol for later application by `trie patch apply`.

- Validates the new name is a valid Python identifier
- Creates a rename patch in the graph database with optional reason
- Reports the number of existing references that will need updating
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_apply_cmd fingerprint=5f4eda920305e3f49d4bdc0ce8cabd318f66cefe003c63997bc88e66d9ae1e84 body_fp=3cd7f7b8dbcf67288f85b6162c06058accd9c3bad1e38bd85554b91a300fac70 source_ref=a926c793af5e1f338acdc176a5faae767217b646 role=api -->
Archive pending patch notes as intent via `record_intent` — always the `record` path, no code generation.

- `--note`: session-level unifying intent for the apply run.
- `--json`: dumps raw envelope to stdout and exits 1 if `ok` is falsy; non-JSON path exits 1 on failure or prints a per-symbol success list.
- After success, reads `envelope["uncovered"]`: warns with up to 5 symbols still lacking notes (would fail the commit gate), or reports full coverage when the key is present but empty.
- Removed: `--model`, `--backend`, `--commit-mode` options and all `agent`/`llm` backend dispatch paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_preview_cmd fingerprint=bb43bb71a6141343c63226fcf7e8bf42a7bb400eedccecc762509629daa934f7 body_fp=e03e8a69221f0c07d9d3b8e4b3642f5e8c1ab04e8e8c08bd1c7333d523df64a7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Previews what `trie patch apply` would execute without running it.

- Displays a Rich table with separate rows for patched symbols, create-symbol patches, and cascade neighbours
- Shows an "Origin" column distinguishing patch types rather than cascade indicators
- Reports zero patches with an info message if no patches or creates are pending
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_list_cmd fingerprint=8d8b6d21fbaecc39a83d4d22192f73d2d93ceb086194fcebedc17a8f0943f357 body_fp=80a151338dd9913e69e7c6b1df21c7fc758d2dbcadf93738a1defbc817295b13 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
List all pending patches and create-symbol patches in separate tables.

Opens the graph store, retrieves symbols with pending modification patches and staged symbol creations, then displays them in two Rich tables: "Pending Patches" shows qualified names with patch counts, and "Pending Creates" shows new symbol names with target files. Exits with no output if neither patch type exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_drop_cmd fingerprint=b456b5f77094c686bfb31765795cabfab769c5ad30c8de1e19416ea722b8f2be body_fp=878dc813f49b76f20fe7673a572c395ba89428564119edac46f0824e51b0cd50 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Drop pending patches from both modify/structural and create patch tables by qname, session ID, or all patches.

- Exactly one of the three selection criteria must be provided
- Clears from both patch tables so create-symbol patches don't linger after `drop --all`
- Exits with code 1 if no selection criteria specified or config not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_app fingerprint=0c83c10dbd09994c30dee74986deefeee9e7fbcba6d0fe9f936c328a8b332275 body_fp=58e6c3b276840293bcf335b4fd33dfabda523fafd5261b08491b0cb0134c417e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=entrypoint -->
Typer sub-application for MCP (Model Context Protocol) server management commands.

- Provides `install`, `uninstall`, and `serve` subcommands for agent integration
- Shows help when invoked without arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=70fc24d5899708cd24382a7202d5b17748a63d20953b59c486d5f62a5ccc2d1d source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Run the trie MCP server over stdio as a Typer command.

Delegates to `_run_mcp_serve()` for the actual server implementation.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=73c11dc03b04976bf9a2fc8e80637299abc238437977e34a37ba8ed763f61b6e source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=io -->
Starts the MCP server over stdio after validating the project configuration.

- Locates trie.toml and validates config structure without using its contents
- Prints config errors to stderr to avoid corrupting the MCP protocol stream
- Delegates to run_mcp_stdio for actual server implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=56b8a3b5140b45725192474cf54754a68433b6176f397804f637922c8ff8f7e2 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Registers trie MCP server with one or more coding agents through their config files.

- `target`: specific agent names to install for (can be repeated)
- `install_all`: install for all known agents, skipping detection
- `scope`: "project" writes to current repo, "user" writes to ~/.<agent>/
- `print_only`: shows config snippet without writing files
- `dry_run`: shows file paths and changes without writing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=c59c0e62f61e8a6cbca9c3bc43e2245f6354f57fcf5c071f544b259056b7a493 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders human-readable output for MCP installation results, displaying per-target status and details.

- Formats each result with the target's display name and appropriate colored status indicators
- Shows JSON snippets for preview actions and error messages for failed operations
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_uninstall_cmd fingerprint=e0cbf3e2e0174b8f33dbe0589e2c6908d67e5f5c49961500186aab26268bab2a body_fp=0419c682c13f9af03e4f29b59768509b1970615524ec8ec4da9a6953dd9c1540 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
Unregisters the trie MCP server from agent configuration files.

• Validates mutually exclusive flags and scope options
• Delegates uninstall execution to `mcp_run_uninstall` with validated parameters
• Renders the uninstall plan showing removed entries per target
• Exits with code 1 if any uninstall operation encounters errors
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_uninstall_plan fingerprint=982bba634aca721cfd1aaf145aba973af33cbd7f5cb22ab4f82d6c4f8ba7a692 body_fp=2191ea5bf60f2c3f0b81ff5998d0d99449fd63a3c5851c65644d3559c8e5b85f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
Renders the output for `trie mcp uninstall` by iterating through uninstall plan results and printing status messages for each target using the Reporter console interface.

- Mirrors the install renderer with `removed` status replacing `created`/`updated`
- Prints JSON preview for dry-run mode, success/error messages for actual operations
- Shows skipped targets with explanatory detail when no action was needed
<!-- trie:end -->