---
trie_version: 0.3.0
source: trie/cli.py
file_fingerprint: e958c03676c10913cb855a80243675c074571565842973bce8ec26efe7c1bb4c
last_synced_at: '2026-08-02T21:19:37Z'
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
  signature: 'def _get_reporter(ctx: typer.Context) -> Reporter'
- kind: function
  qualified_name: trie/cli:_cli_session_id
  lines: 103-123
  signature: 'def _cli_session_id(project_root: Path) -> str'
- kind: class
  qualified_name: trie/cli:_ProgressAdapter
  lines: 126-198
  signature: class _ProgressAdapter
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.__init__
  lines: 134-139
  signature: 'def __init__(self, reporter: Reporter, label: str)'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter._ensure
  lines: 141-146
  signature: 'def _ensure(self, total: int) -> ProgressHandle'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.close
  lines: 148-151
  signature: def close(self) -> None
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_plan
  lines: 153-165
  signature: 'def on_plan(self, *, direct: int, cascade: int) -> None: # Printed once before any file starts. Summarises the worklist split so # the operator understands why N files sync when only a few drifted.'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_section
  lines: 167-176
  signature: 'def on_section(self, *, label: str, count: int) -> None: # A separator + heading printed above the live region before each group # of files (directly stale, then cascade) begins.'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_start
  lines: 178-179
  signature: 'def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_done
  lines: 181-194
  signature: 'def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None'
- kind: method
  qualified_name: trie/cli:_ProgressAdapter.on_skip
  lines: 196-198
  signature: 'def on_skip(self, rel_path: str, reason: str) -> None'
- kind: function
  qualified_name: trie/cli:_progress_callback
  lines: 202-207
  signature: 'def _progress_callback(reporter: Reporter, label: str) -> Iterator[ProgressCallback]'
- kind: function
  qualified_name: trie/cli:_activity_progress
  lines: 211-228
  signature: 'def _activity_progress( reporter: Reporter, label: str, *, op: str, project_root: Path ) -> Iterator[ProgressCallback]'
- kind: class
  qualified_name: trie/cli:_JsonlProgress
  lines: 231-277
  signature: class _JsonlProgress
- kind: method
  qualified_name: trie/cli:_JsonlProgress.__init__
  lines: 252-253
  signature: 'def __init__(self, stream: Any = None)'
- kind: method
  qualified_name: trie/cli:_JsonlProgress._emit
  lines: 255-259
  signature: 'def _emit(self, payload: dict[str, Any]) -> None'
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_start
  lines: 261-264
  signature: 'def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None'
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_done
  lines: 266-274
  signature: 'def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None'
- kind: method
  qualified_name: trie/cli:_JsonlProgress.on_skip
  lines: 276-277
  signature: 'def on_skip(self, rel_path: str, reason: str) -> None'
- kind: function
  qualified_name: trie/cli:emit_jsonl_event
  lines: 280-290
  signature: 'def emit_jsonl_event(payload: dict[str, Any], stream: Any = None) -> None'
- kind: function
  qualified_name: trie/cli:_acquire_write_lock_or_exit
  lines: 294-325
  signature: 'def _acquire_write_lock_or_exit( project_root: Path, reporter: Reporter, command_name: str ) -> Iterator[None]'
- kind: function
  qualified_name: trie/cli:_root
  lines: 329-367
  signature: 'def _root( ctx: typer.Context, version: bool = typer.Option(False, "--version", help="Show trie version and exit."), quiet: bool = typer.Option( False, "--quiet", "-q", help="Mute mode: print errors only.", ), verbose: bool = typer.Option( False, "--verbose", "-v", help="Verbose mode: include per-symbol detail and token breakdowns.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_telemetry_bootstrap
  lines: 370-382
  signature: 'def _telemetry_bootstrap(subcommand: str | None, argv_tail: list[str]) -> None'
- kind: function
  qualified_name: trie/cli:init_cmd
  lines: 386-507
  signature: 'def init_cmd( ctx: typer.Context, root: Path = typer.Argument( Path.cwd(), help="Project root to initialise. Defaults to the current directory.", show_default=False, ), force: bool = typer.Option( False, "--force", "-f", help="Overwrite trie.toml if it exists, and skip Python-project detection.", ), install_hooks: bool | None = typer.Option( None, "--install-hooks/--no-install-hooks", help="Install a pre-commit hook that runs `trie verify`. Prompts when omitted in a tty.", ), run_scan: bool = typer.Option( True, "--scan/--no-scan", help="Build the symbol graph immediately after writing trie.toml.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_is_interactive
  lines: 510-517
  signature: def _is_interactive() -> bool
- kind: function
  qualified_name: trie/cli:_prompt_select_targets
  lines: 520-578
  signature: 'def _prompt_select_targets(reporter: Reporter, detected: list[str]) -> list[str]'
- kind: class
  qualified_name: trie/cli:_NoOpStatus
  lines: 581-586
  signature: class _NoOpStatus
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__enter__
  lines: 582-583
  signature: def __enter__(self) -> _NoOpStatus
- kind: method
  qualified_name: trie/cli:_NoOpStatus.__exit__
  lines: 585-586
  signature: 'def __exit__(self, *exc: object) -> None'
- kind: function
  qualified_name: trie/cli:plan_cmd
  lines: 590-707
  signature: 'def plan_cmd( ctx: typer.Context, model: str | None = typer.Option( None, "--model", help="Override the configured model for cost estimation." ), all_: bool = typer.Option( False, "--all", help=( "Show the cost of regenerating every in-scope file (full re-bootstrap), " "not just the incremental worklist. Default on a fresh project; opt-in on " "an established one." ), ), offline: bool = typer.Option( False, "--offline", help=( "Skip the count_tokens cost preview (the only network calls plan makes). " "Shows the worklist with symbol counts; estimates read $0." ), ), ) -> None'
- kind: function
  qualified_name: trie/cli:verify_cmd
  lines: 711-723
  signature: 'def verify_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:status_cmd
  lines: 727-849
  signature: 'def status_cmd( ctx: typer.Context, as_json: bool = typer.Option( False, "--json", help="Emit the status as a single JSON object instead of prose." ), ) -> None'
- kind: function
  qualified_name: trie/cli:lock_check_cmd
  lines: 853-903
  signature: 'def lock_check_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:_run_graph_only_sync
  lines: 906-1011
  signature: 'def _run_graph_only_sync(reporter: Reporter, *, as_json: bool, before_turn: bool) -> None'
- kind: function
  qualified_name: trie/cli:_graph_sync_progress
  lines: 1015-1036
  signature: 'def _graph_sync_progress( reporter: Reporter, as_json: bool, *, project_root: Path ) -> Iterator[ProgressCallback]'
- kind: function
  qualified_name: trie/cli:_emit_freshness_json
  lines: 1039-1053
  signature: 'def _emit_freshness_json(result: FreshnessResult, *, mode: str) -> None'
- kind: function
  qualified_name: trie/cli:_report_freshness
  lines: 1056-1070
  signature: 'def _report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None'
- kind: constant
  qualified_name: trie/cli:_AUDIT_TAIL_BYTES
  lines: 1073-1073
- kind: function
  qualified_name: trie/cli:audit_cmd
  lines: 1080-1154
  signature: 'def audit_cmd( ctx: typer.Context, log: Path | None = typer.Option( None, "--log", "-l", help="Path to the debug.jsonl to read. Defaults to the configured debug.log_path.", ), compare: Path | None = typer.Option( None, "--compare", "-c", help="Render a side-by-side comparison: this log is the candidate, --log is the baseline.", ), as_json: bool = typer.Option( False, "--json", help="Print the summary as JSON. Mutually exclusive with --compare.", ), all_history: bool = typer.Option( False, "--all", help=( "Parse the entire log instead of the recent tail. The default reads " "the last ~4MB (roughly the recent sessions) so the command stays " "fast on long-lived projects whose logs run to tens of MB." ), ), ) -> None'
- kind: function
  qualified_name: trie/cli:_resolve_audit_log_path
  lines: 1157-1173
  signature: 'def _resolve_audit_log_path(log: Path | None, reporter: Reporter) -> Path'
- kind: function
  qualified_name: trie/cli:_run_intent_gate
  lines: 1176-1218
  signature: 'def _run_intent_gate(reporter: Reporter, config: Config, project_root: Path) -> bool'
- kind: function
  qualified_name: trie/cli:_warn_on_version_skew
  lines: 1221-1251
  signature: 'def _warn_on_version_skew(reporter: Reporter, project_root: Path) -> None'
- kind: function
  qualified_name: trie/cli:gate_cmd
  lines: 1255-1312
  signature: 'def gate_cmd( ctx: typer.Context, no_digest: bool = typer.Option( False, "--no-digest", help="Skip the digest write (gates only: lock + verify + intent).", ), ) -> None'
- kind: function
  qualified_name: trie/cli:intent_cmd
  lines: 1316-1334
  signature: 'def intent_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:index_cmd
  lines: 1338-1362
  signature: 'def index_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:diff_cmd
  lines: 1366-1498
  signature: 'def diff_cmd( ctx: typer.Context, base: str = typer.Option("HEAD", "--base", help="Git ref to diff the triefact tree against."), raw: bool = typer.Option( False, "--raw", help="Skip LLM synthesis; print patch notes and the raw triefact diff.", ), as_json: bool = typer.Option( False, "--json", help="Emit the collected evidence as JSON (no LLM call). Mutually exclusive with --raw.", ), model: str | None = typer.Option( None, "--model", help="Override the model used for narrative synthesis." ), write: bool = typer.Option( False, "--write", help="Prepend a digest entry to the TRIE_DIFF file (config diff.write_path) and exit; used by the pre-commit hook.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_run_digest_write
  lines: 1501-1638
  signature: 'def _run_digest_write( reporter: Reporter, config: Config, project_root: Path, *, base: str = "HEAD", raw: bool = False, model: str | None = None, stage: bool = False, ) -> bool'
- kind: function
  qualified_name: trie/cli:_print_scan_breakdown
  lines: 1641-1658
  signature: 'def _print_scan_breakdown( reporter: Reporter, scan_result, db_path: Path, project_root: Path ) -> None'
- kind: function
  qualified_name: trie/cli:_print_plan
  lines: 1661-1672
  signature: 'def _print_plan(reporter: Reporter, plan: BootstrapPlan, model_id: str) -> None'
- kind: function
  qualified_name: trie/cli:_print_incremental_plan
  lines: 1675-1741
  signature: 'def _print_incremental_plan( reporter: Reporter, plan: BootstrapPlan, worklist: IncrementalWorklist, model_id: str, ) -> None'
- kind: constant
  qualified_name: trie/cli:_REASON_LABELS
  lines: 1744-1751
- kind: function
  qualified_name: trie/cli:_print_drift_detail
  lines: 1754-1765
  signature: 'def _print_drift_detail(reporter: Reporter, items: list) -> None'
- kind: function
  qualified_name: trie/cli:_verify_drift
  lines: 1768-1802
  signature: 'def _verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool'
- kind: function
  qualified_name: trie/cli:sync_cmd
  lines: 1806-2033
  signature: "def sync_cmd( ctx: typer.Context, graph_only: bool = typer.Option( False, \"--graph-only\", help=( \"Rebuild the symbol graph and freshness stamp from source without \" \"calling the LLM. Free and fast; drifted prose is marked stale for \" \"a later full `trie sync`. This is what turn hooks run.\" ), ), before_turn: bool = typer.Option( False, \"--before-turn\", help=( \"Hook mode (implies --graph-only): cheap pre-turn freshness gate \u2014 \" \"no-op when nothing changed since the last graph sync.\" ), ), after_turn: bool = typer.Option( False, \"--after-turn\", help=( \"Hook mode (implies --graph-only): post-turn sweep that picks up the \" \"agent's own edits. Default turn mode for --graph-only.\" ), ), as_json: bool = typer.Option( False, \"--json\", help=( \"With --graph-only: emit machine-readable JSON-Lines progress to \" 'stdout instead of Rich output. Each line is one event ({\"kind\": ...}).' ), ), file: Path | None = typer.Option( None, \"--file\", \"-f\", help=( \"Sync exactly one source file. Regenerates only its stale symbols by \" \"default; combine with --force for a full fresh rewrite.\" ), ), all_: bool = typer.Option( False, \"--all\", help=\"Force a full re-pass (every file in scope), even if triefacts already exist.\", ), budget: float | None = typer.Option( None, \"--budget\", help=\"USD budget cap. Stops once cumulative actual cost reaches this.\", ), limit: int | None = typer.Option( None, \"--limit\", help=\"Cap the number of files synced.\", ), dry_run: bool = typer.Option( False, \"--dry-run\", help=( \"Preview what `trie sync` would change. Regenerates stale triefacts into \" \"`.trie/preview/` and prints unified diffs (makes API calls \u2014 cap with \" \"--budget / --limit).\" ), ), metadata_only: bool = typer.Option( False, \"--metadata-only\", help=( \"Refresh triefact front matter from the live store without calling the LLM. \" \"Useful after a graph-only change (e.g. an improved reference resolver) \" \"where edge counts moved but source did not.\" ), ), roles_only: bool = typer.Option( False, \"--roles-only\", help=( \"(Re)infer only the architectural role tag for every symbol against a \" \"project-specific role vocabulary, without regenerating prose. Derives \" \"the vocabulary first if none exists. Cheap relative to a full sync.\" ), ), rederive_taxonomy: bool = typer.Option( False, \"--rederive-taxonomy\", help=( \"With --roles-only, re-derive the role vocabulary from scratch even if one \" \"is already saved. Use after large architectural change.\" ), ), model: str | None = typer.Option( None, \"--model\", help=\"Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.\", ), force: bool = typer.Option( False, \"--force\", help=( \"Force cold regeneration for every symbol in the file, bypassing the \" \"diff-aware path. Only valid with --file. Use when existing prose is \" \"known to be wrong and a full fresh LLM pass is needed.\" ), ), ) -> None"
- kind: function
  qualified_name: trie/cli:_has_existing_triefacts
  lines: 2036-2042
  signature: 'def _has_existing_triefacts(triefacts_root: Path) -> bool'
- kind: function
  qualified_name: trie/cli:_run_full_pass
  lines: 2045-2121
  signature: 'def _run_full_pass( *, reporter: Reporter, project_root: Path, config: Config, model: str | None, budget: float | None, limit: int | None, ) -> None'
- kind: function
  qualified_name: trie/cli:_refresh_index_quietly
  lines: 2124-2131
  signature: 'def _refresh_index_quietly(config: Config, project_root: Path, store: Store) -> None'
- kind: function
  qualified_name: trie/cli:_report_sync_errors
  lines: 2134-2155
  signature: 'def _report_sync_errors(reporter: Reporter, file_errors: list[tuple[str, str]]) -> bool'
- kind: function
  qualified_name: trie/cli:_run_dry_run_diff
  lines: 2158-2203
  signature: 'def _run_dry_run_diff( *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None ) -> None'
- kind: function
  qualified_name: trie/cli:_run_single_file_sync
  lines: 2206-2280
  signature: 'def _run_single_file_sync( reporter: Reporter, file: Path, model: str | None, force: bool = False ) -> None'
- kind: function
  qualified_name: trie/cli:_run_metadata_only_refresh
  lines: 2283-2343
  signature: 'def _run_metadata_only_refresh(reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_run_roles_only_sync
  lines: 2346-2388
  signature: 'def _run_roles_only_sync(reporter: Reporter, *, model: str | None, rederive_taxonomy: bool) -> None'
- kind: function
  qualified_name: trie/cli:_run_incremental_sync
  lines: 2391-2460
  signature: 'def _run_incremental_sync( *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None ) -> None'
- kind: function
  qualified_name: trie/cli:setup_cmd
  lines: 2464-2674
  signature: "def setup_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, \"--target\", \"-t\", help=( \"Set up for a specific agent. Repeat the flag for multiple targets. \" f\"Known: {', '.join(MCP_TARGETS)}.\" ), ), install_all: bool = typer.Option( False, \"--all\", help=\"Set up for every known agent. Skips per-target detection.\", ), scope: str = typer.Option( \"project\", \"--scope\", help=\"MCP install scope: 'project' (writes into this repo) or 'user' (~/.<agent>/...).\", case_sensitive=False, ), print_only: bool = typer.Option( False, \"--print-only\", help=\"Print what would be written for both MCP and hooks; don't touch any files.\", ), dry_run: bool = typer.Option( False, \"--dry-run\", help=\"Resolve target paths and show what would change, but don't write.\", ), no_overrides: bool = typer.Option( False, \"--no-overrides\", help=( \"Skip the tool-override step. By default, `setup` replaces the \" \"agent's built-in `grep` and `read` with wrappers that route \" \"through trie (and adds `trace`). Pass --no-overrides to \" \"install hook + docs only and leave the agent's built-ins alone.\" ), ), with_mcp: bool = typer.Option( False, \"--with-mcp\", help=( \"Also register the trie MCP server for each target \" \"(same as `trie mcp install`). Off by default \u2014 the hook and \" \"tool overrides are sufficient for most setups.\" ), ), ) -> None"
- kind: function
  qualified_name: trie/cli:_render_setup_plan
  lines: 2677-2747
  signature: 'def _render_setup_plan( reporter: Reporter, mcp_plan: InstallPlan | None, hook_plan: HookInstallPlan, docs_plan: DocsInstallPlan, override_plan: ToolOverrideInstallPlan | None = None, ) -> None'
- kind: function
  qualified_name: trie/cli:_render_override_target_block
  lines: 2750-2776
  signature: 'def _render_override_target_block(reporter: Reporter, result: object) -> None'
- kind: function
  qualified_name: trie/cli:_format_action
  lines: 2779-2783
  signature: 'def _format_action(action: str, path: Path | None) -> str'
- kind: function
  qualified_name: trie/cli:_open_tools
  lines: 2798-2816
  signature: 'def _open_tools(reporter: Reporter) -> TrieTools'
- kind: function
  qualified_name: trie/cli:_emit_envelope
  lines: 2819-2843
  signature: 'def _emit_envelope( envelope: dict[str, object], *, as_json: bool, reporter: Reporter, render: Callable[[dict[str, object], Reporter], None], ) -> None'
- kind: function
  qualified_name: trie/cli:_patched_tag
  lines: 2846-2850
  signature: 'def _patched_tag(count: int) -> str'
- kind: function
  qualified_name: trie/cli:_grep_output_is_tty
  lines: 2853-2866
  signature: def _grep_output_is_tty() -> bool
- kind: function
  qualified_name: trie/cli:_print_grep_records
  lines: 2869-2890
  signature: 'def _print_grep_records( reporter: Reporter, rows: list, *, qname_suffix: Callable[[dict], str] | None = None ) -> None'
- kind: function
  qualified_name: trie/cli:_render_grep
  lines: 2893-2984
  signature: 'def _render_grep(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_render_read
  lines: 2987-3074
  signature: 'def _render_read(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_render_trace
  lines: 3077-3129
  signature: 'def _render_trace(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_render_error_envelope
  lines: 3132-3144
  signature: 'def _render_error_envelope(err: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_build_grep_predicate
  lines: 3147-3209
  signature: 'def _build_grep_predicate( name: str | None, kind: str | None, scope_prefix: str | None, scope_exclude: list[str] | None, public_only: bool, inbound_min: int | None, inbound_max: int | None, outbound_min: int | None, outbound_max: int | None, predicate_json: str | None, reporter: Reporter, ) -> dict[str, object]'
- kind: function
  qualified_name: trie/cli:grep_cmd
  lines: 3213-3316
  signature: 'def grep_cmd( ctx: typer.Context, name: str | None = typer.Option( None, "--name", "-n", help="Substring match against the symbol''s local name (case-insensitive).", ), kind: str | None = typer.Option( None, "--kind", "-k", help="Restrict to one of: function, class, method, constant, module, any.", ), scope_prefix: str | None = typer.Option( None, "--scope-prefix", help="Restrict to symbols whose file path starts with this prefix (e.g. ''trie/'').", ), scope_exclude: list[str] | None = typer.Option( None, "--scope-exclude", help="File-path prefixes to skip. Repeat the flag for multiple exclusions.", ), public_only: bool = typer.Option( False, "--public-only", help="Restrict to symbols whose name doesn''t start with an underscore.", ), inbound_min: int | None = typer.Option( None, "--inbound-min", help="Minimum inbound edge count (find hubs).", ), inbound_max: int | None = typer.Option( None, "--inbound-max", help="Maximum inbound edge count.", ), outbound_min: int | None = typer.Option( None, "--outbound-min", help="Minimum outbound edge count.", ), outbound_max: int | None = typer.Option( None, "--outbound-max", help="Maximum outbound edge count (find leaves with --outbound-max 0).", ), predicate_json: str | None = typer.Option( None, "--predicate", help="Full predicate as JSON; identical shape to the MCP `grep` predicate.", ), rank_by: str | None = typer.Option( None, "--rank-by", help="public_first (default) | inbound_count | alphabetical.", ), limit: int = typer.Option( 10, "--limit", "-l", help="Maximum number of hits to return.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:read_cmd
  lines: 3320-3387
  signature: 'def read_cmd( ctx: typer.Context, path: str = typer.Argument( ..., help="Symbol qname (e.g. ''trie/sync/cascade:compute_cascade'') OR a file path.", ), full: bool = typer.Option( False, "--full", help="For a file path: return every section''s full prose instead of the compact view.", ), source: bool = typer.Option( False, "--source", help="Force raw line-numbered source for a FILE PATH (any file, indexed or not).", ), offset: int | None = typer.Option( None, "--offset", help="With a file path: 1-indexed first line to include (implies --source).", ), limit: int | None = typer.Option( None, "--limit", help="With a file path: maximum number of lines to return from offset (implies --source).", ), history: bool = typer.Option( False, "--history", "-H", help=( "Also show the symbol''s (or file''s) intent trail from the session-digest " "archive: the chronological ''why it changed'' lines recorded at each commit." ), ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_render_read_dispatch
  lines: 3390-3403
  signature: 'def _render_read_dispatch(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_render_read_source
  lines: 3406-3415
  signature: 'def _render_read_source(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:trace_cmd
  lines: 3419-3461
  signature: 'def trace_cmd( ctx: typer.Context, qname: str = typer.Argument( ..., help="Fully-qualified symbol name to start tracing from.", ), direction: str = typer.Option( "callers", "--direction", "-d", help="callers | callees | both.", ), depth: int = typer.Option( 2, "--depth", help="Maximum BFS depth (clamped by trace_max_depth in config).", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:blast_radius_cmd
  lines: 3465-3495
  signature: 'def blast_radius_cmd( ctx: typer.Context, qname: str = typer.Argument( ..., help="Fully-qualified symbol name to compute the edit blast radius for.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_render_blast_radius
  lines: 3498-3528
  signature: 'def _render_blast_radius(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_print_plain
  lines: 3538-3547
  signature: 'def _print_plain(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:grep_str_cmd
  lines: 3551-3580
  signature: 'def grep_str_cmd( ctx: typer.Context, regexp: str = typer.Argument(..., help="Regex pattern to search source bodies with."), all_files: bool = typer.Option( False, "--all-files", help="Search the WHOLE repo (incl. non-indexed files), not just indexed source bodies.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:find_cmd
  lines: 3584-3613
  signature: 'def find_cmd( ctx: typer.Context, pattern: str = typer.Argument( ..., help="Glob pattern, e.g. ''**/*.ts'', ''Dockerfile'', ''src/**/*.tsx''." ), indexed_only: bool = typer.Option( False, "--indexed-only", help="Restrict to indexed files only (default searches the whole tree).", ), limit: int = typer.Option(100, "--limit", "-l", help="Maximum number of paths to return."), ) -> None'
- kind: function
  qualified_name: trie/cli:write_cmd
  lines: 3617-3657
  signature: 'def write_cmd( ctx: typer.Context, path: str = typer.Argument( ..., help="File path to create/overwrite, relative to the project root." ), content: str | None = typer.Option( None, "--content", "-c", help="File content. If omitted, content is read from stdin.", ), overwrite: bool = typer.Option( False, "--overwrite", help="Allow replacing an existing file.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_render_write
  lines: 3660-3669
  signature: 'def _render_write(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:_render_find
  lines: 3672-3687
  signature: 'def _render_find(envelope: dict[str, object], reporter: Reporter) -> None'
- kind: function
  qualified_name: trie/cli:grep_entry_points_cmd
  lines: 3691-3709
  signature: 'def grep_entry_points_cmd( ctx: typer.Context, query: str = typer.Argument(..., help="Topic or concept to match against symbol prose."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:grep_symbol_cmd
  lines: 3713-3731
  signature: 'def grep_symbol_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:grep_symbol_neighbours_cmd
  lines: 3735-3753
  signature: 'def grep_symbol_neighbours_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:explain_symbol_cmd
  lines: 3757-3781
  signature: 'def explain_symbol_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol qname or name fragment to explain."), history: bool = typer.Option( False, "--history", "-H", help="Also show the symbol''s intent trail from the digest archive.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:explain_symbol_refs_cmd
  lines: 3785-3809
  signature: 'def explain_symbol_refs_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol qname or name fragment."), history: bool = typer.Option( False, "--history", "-H", help="Also show the symbol''s intent trail from the digest archive.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:trace_flow_cmd
  lines: 3813-3832
  signature: 'def trace_flow_cmd( ctx: typer.Context, symbol1: str = typer.Argument(..., help="Starting symbol qname or name."), symbol2: str = typer.Argument(..., help="Target symbol qname or name."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: function
  qualified_name: trie/cli:explain_flow_cmd
  lines: 3836-3855
  signature: 'def explain_flow_cmd( ctx: typer.Context, symbol1: str = typer.Argument(..., help="Starting symbol qname or name."), symbol2: str = typer.Argument(..., help="Target symbol qname or name."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None'
- kind: constant
  qualified_name: trie/cli:patch_app
  lines: 3863-3867
- kind: class
  qualified_name: trie/cli:_RichApplyProgress
  lines: 3871-3923
  signature: class _RichApplyProgress
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.__init__
  lines: 3881-3883
  signature: 'def __init__(self, console: Console, *, verbose: bool = False)'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.stage
  lines: 3885-3886
  signature: 'def stage(self, msg: str) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_start
  lines: 3888-3889
  signature: 'def file_start(self, fp: str, symbols: int) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_symbol
  lines: 3891-3897
  signature: 'def file_symbol(self, qn: str, notes: list[str]) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_generate
  lines: 3899-3901
  signature: def file_generate(self) -> None
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_fixup
  lines: 3903-3906
  signature: 'def file_fixup(self, iteration: int, count: int) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_prose
  lines: 3908-3911
  signature: 'def file_prose(self, qn: str) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.file_done
  lines: 3913-3917
  signature: 'def file_done(self, fp: str, ok: bool, error: str | None = None) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.refresh
  lines: 3919-3920
  signature: 'def refresh(self, fp: str) -> None'
- kind: method
  qualified_name: trie/cli:_RichApplyProgress.verify
  lines: 3922-3923
  signature: def verify(self) -> None
- kind: function
  qualified_name: trie/cli:_close_qname_suggestions
  lines: 3926-3940
  signature: 'def _close_qname_suggestions(store: Store, qname: str, *, n: int = 3) -> list[str]'
- kind: function
  qualified_name: trie/cli:patch_create_cmd
  lines: 3944-4000
  signature: 'def patch_create_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to patch."), note: str = typer.Option(..., "--note", "-n", help="Implementation change note."), reason: str = typer.Option( "", "--reason", "-r", help="Why the cascade needs to know about this change." ), gone: bool = typer.Option( False, "--gone", help=( "The symbol was REMOVED (no longer in the graph): record the note " "straight to the session log as a delete instead of queueing a patch. " "This is how removals satisfy the `trie intent` gate." ), ), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_create_batch_cmd
  lines: 4004-4128
  signature: 'def patch_create_batch_cmd( ctx: typer.Context, json_file: str = typer.Option( "", "--json-file", help="Path to a JSON file with the patch array (else read stdin)." ), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_create_symbol_cmd
  lines: 4132-4180
  signature: 'def patch_create_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Intended qualified name, e.g. ''pkg/mod:new_fn''."), note: str = typer.Option(..., "--note", "-n", help="What the new symbol should do."), file: str = typer.Option( "", "--file", "-f", help="Target source file (derived from qname when omitted)." ), anchor: str = typer.Option( "", "--anchor", "-a", help="Place the new symbol after this existing qname." ), reason: str = typer.Option("", "--reason", "-r", help="Why this symbol is needed."), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_delete_symbol_cmd
  lines: 4184-4211
  signature: 'def patch_delete_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to delete."), reason: str = typer.Option("", "--reason", "-r", help="Why it''s being removed."), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_rename_symbol_cmd
  lines: 4215-4244
  signature: 'def patch_rename_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to rename."), new_name: str = typer.Argument(..., help="New local name (not a qualified name)."), reason: str = typer.Option("", "--reason", "-r", help="Why it''s being renamed."), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_apply_cmd
  lines: 4248-4310
  signature: 'def patch_apply_cmd( ctx: typer.Context, note: str = typer.Option( "", "--note", "-N", help="Session note: the unifying intent (required for multi-symbol applies).", ), json_output: bool = typer.Option( False, "--json", help="Emit raw JSON output (useful for agent consumers).", ), ) -> None'
- kind: function
  qualified_name: trie/cli:patch_preview_cmd
  lines: 4314-4357
  signature: 'def patch_preview_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:patch_list_cmd
  lines: 4361-4403
  signature: 'def patch_list_cmd(ctx: typer.Context) -> None'
- kind: function
  qualified_name: trie/cli:patch_drop_cmd
  lines: 4407-4445
  signature: 'def patch_drop_cmd( ctx: typer.Context, qname: str | None = typer.Option( None, "--qname", "-q", help="Drop patches for a specific symbol." ), session_id: str | None = typer.Option( None, "--session", "-s", help="Drop patches for a specific session." ), all: bool = typer.Option(False, "--all", "-a", help="Drop all patches."), ) -> None'
- kind: constant
  qualified_name: trie/cli:mcp_app
  lines: 4453-4460
- kind: function
  qualified_name: trie/cli:mcp_serve
  lines: 4465-4467
  signature: def mcp_serve() -> None
- kind: function
  qualified_name: trie/cli:_run_mcp_serve
  lines: 4470-4480
  signature: def _run_mcp_serve() -> None
- kind: function
  qualified_name: trie/cli:mcp_install_cmd
  lines: 4484-4553
  signature: 'def mcp_install_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, "--target", "-t", help=( "Install for a specific agent. Repeat the flag for multiple targets. " f"Known: {'', ''.join(MCP_TARGETS)}." ), ), install_all: bool = typer.Option( False, "--all", help="Install for every known target. Skips per-target detection.", ), scope: str = typer.Option( "project", "--scope", help="Install scope: ''project'' (writes into the current project) or ''user'' (~/.<agent>/...).", case_sensitive=False, ), print_only: bool = typer.Option( False, "--print-only", help="Print the snippet that would be merged, don''t write any files.", ), dry_run: bool = typer.Option( False, "--dry-run", help="Show what would change without writing. Implies the file path resolution but no edit.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_render_install_plan
  lines: 4556-4571
  signature: 'def _render_install_plan(reporter: Reporter, plan: InstallPlan) -> None'
- kind: function
  qualified_name: trie/cli:mcp_uninstall_cmd
  lines: 4575-4650
  signature: 'def mcp_uninstall_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, "--target", "-t", help=( "Uninstall from a specific agent. Repeat the flag for multiple targets. " f"Known: {'', ''.join(MCP_TARGETS)}." ), ), uninstall_all: bool = typer.Option( False, "--all", help="Uninstall from every known target. Skips per-target detection.", ), scope: str = typer.Option( "project", "--scope", help="Uninstall scope: ''project'' (the current project''s config files) or ''user'' (~/.<agent>/...).", case_sensitive=False, ), print_only: bool = typer.Option( False, "--print-only", help="Print what would be removed without writing any files.", ), dry_run: bool = typer.Option( False, "--dry-run", help="Show what would change without writing.", ), ) -> None'
- kind: function
  qualified_name: trie/cli:_render_uninstall_plan
  lines: 4653-4673
  signature: 'def _render_uninstall_plan(reporter: Reporter, plan: UninstallPlan) -> None'
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
<!-- trie:section symbol=trie/cli:_get_reporter fingerprint=cf94ab09cbdb7bfbbbc6f18b1aef37b7bc59939b02d3ec4ba5d2b3408cd3d2a4 body_fp=d74aaac26f37e9b3cde9b7a2de9d2243414aacd7a2d3376d4bf3cd0eb8d1baeb source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _get_reporter(ctx: typer.Context) -> Reporter`

Resolve the `Reporter` stored on `ctx.obj` by the root callback, falling back to a default `MEDIUM` reporter when none is set.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_cli_session_id fingerprint=dcf3fe8c7e922ef3d9466b25f8ca9207e6ab499a2182dd92a3538dbda5f6aa23 body_fp=eb5db535f9e76692642452051b501f6f0c4a2d800f638db8fb08f3e878eba36f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _cli_session_id(project_root: Path) -> str`

Generates a stable session ID for CLI patch operations, reused across multiple invocations.

- Returns `TRIE_SESSION_ID` environment variable if set
- Otherwise persists a 12-character UUID in activity database for project-wide reuse
- Ensures `trie patch --session drop` works by maintaining consistent session identity
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter fingerprint=461508833971d6960227589e60e8d0554cca8d9567c3036ade7cdbf2512b7a95 body_fp=35c48f9e427520eae20a047e1cb15593d81668437047b1db6cffcd8977c0054e source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=util -->
## `class _ProgressAdapter`

Bridges sync's ProgressCallback Protocol to a Reporter ProgressHandle with lazy initialization.

- Creates underlying ProgressHandle on first `on_start` call to avoid requiring total upfront
- Tracks per-file cost delta by comparing running costs across files
- Thread-safe via internal lock protecting handle initialization
- Prints worklist summary and section separators at MEDIUM+ verbosity
- Delegates file progress events (start, done, skip) to the underlying handle when present
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.__init__ fingerprint=62d7f3387263067099a16c5c411db665b3dabb0d0c2701008d99dd22a9a9d982 body_fp=8a3db1d9da485ff2f247dae6d3cdedb1a4aec5c95db6999efb5753b3e1553561 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def __init__(self, reporter: Reporter, label: str)`

Initialise `_ProgressAdapter` with a `Reporter`, a display label, a null `ProgressHandle`, a running-cost accumulator, and a threading lock.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter._ensure fingerprint=67aef789d4a34e8f4c519362a59b70a41784bc0e2039ff8ee536353e1ab334ac body_fp=9ab9ad169fef31984a9842f753518afc72b0ef1372c9ca9486728e5e6361c7f6 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _ensure(self, total: int) -> ProgressHandle`

Lazily initialise and return `_ProgressAdapter.handle`, creating it via `reporter.start_progress` on the first call.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.close fingerprint=552546e1b2d21366675a09a46cbbc358ec539413ed6caaf33c5fad30458ea235 body_fp=088874d80ee972d5861b24e4a04cdb2d5286406fb4fce1141c3a8027269c0c8a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def close(self) -> None`

Tears down the _ProgressAdapter by exiting the underlying ProgressHandle context manager and clearing the handle reference.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_plan fingerprint=3566ccad9e5759fea947fdc6b8c297970c97a7799fcbb38f5da54fb81da4c43b body_fp=b0c92242d61c660f4915dcdf9ac80e14bfcbdd4a281258173772ae754737f34a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def on_plan(self, *, direct: int, cascade: int) -> None: # Printed once before any file starts. Summarises the worklist split so # the operator understands why N files sync when only a few drifted.`

Prints a sync worklist summary before any file processing begins in `_ProgressAdapter`.

- `direct`: count of directly stale files
- `cascade`: count of files pulled in by the cascade
- Skips output when verbosity is below MEDIUM or total is zero
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_section fingerprint=ae4688be43ab22bbc7b9daf029a1af7eb1c021910f566633cf30240275e849f8 body_fp=028291ca7c607e3c0aace4c5640f2f62d1cf6d042c5d66eba1ed9621762bcc4f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def on_section(self, *, label: str, count: int) -> None: # A separator + heading printed above the live region before each group # of files (directly stale, then cascade) begins.`

Prints a section separator line with label and count before each file group.

- Skips output when verbosity is below MEDIUM or count is zero
- Routes through progress handle when available, otherwise directly to reporter console
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_start fingerprint=34f538a7492b05dc2bf2f4087401ea296cd9a705571e3b4bf4aa7d16635d9a6b body_fp=95edcb6f90b54684827befb462842bd2ce1e33d6d3167d59e7dbcded54e9f758 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None`

Ensure the `_ProgressAdapter` progress handle exists for `total` files, then delegate to `ProgressHandle.start_file`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_done fingerprint=9b87ba62bf07734e56621131e19c8514a12a9963da3bd96eaa114fcb7657e9eb body_fp=06586c793ef0098011806b9d0d90bb02909bc801931a6f0fb9eb36c20f0e3c1b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Reports file completion to the progress bar with cost and token metrics from FileSyncResult.

• per_file_cost: computed as the delta between running_cost_usd and the previous total
• cost_usd: only passed if positive, otherwise None to avoid showing zero costs
• tokens: includes input/output counts plus cache read/write statistics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_ProgressAdapter.on_skip fingerprint=548315c2f414ff6db873c1a24a155b96cd48271bacb44311fcefb75ded30f566 body_fp=846cc5aab1a4abe75667faf70ccae1c7e674dc148ed9d61da9a5082cfdb1878c source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def on_skip(self, rel_path: str, reason: str) -> None`

Records a skipped file by forwarding to the underlying ProgressHandle if it exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_progress_callback fingerprint=68451724830ab0d2ebc43db558803015968f6d9726d300a1cfe96be720ca1409 body_fp=e264b80986eb3909ef7d3e9f093b2132b01cfb06ea479434b9b6e14eaf4f2fa4 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _progress_callback(reporter: Reporter, label: str) -> Iterator[ProgressCallback]`

Creates a context-managed _ProgressAdapter that bridges Reporter progress bars with sync ProgressCallback protocol.

- **adapter**: _ProgressAdapter instance that converts ProgressCallback calls to Reporter.start_progress operations
- **cleanup**: ensures adapter.close() is called to properly tear down the progress bar on context exit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_activity_progress fingerprint=18bb44ffa9a5e83286e0aafd8a4ba6edafdce5d003c59f5560efa39703f3c523 body_fp=1ead1cc520df5af7b860380a27f4885240948976e30d00955008049848344820 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _activity_progress( reporter: Reporter, label: str, *, op: str, project_root: Path ) -> Iterator[ProgressCallback]`

Context manager that provides progress reporting mirrored to both Rich console and shared activity state.

- Yields a `ProgressCallback` that routes to both the Rich progress bar and `.trie/status.json` + `activity.jsonl`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress fingerprint=fd935dfc306344a1ab7e8d1965eef70da05594cf71cadac05dafdb542c05825f body_fp=d4fdd3ddebca703f360fd342e6b55d8f46bbe889add38dc20fa6e06a99da4c64 source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=io -->
## `class _JsonlProgress`

Implement `ProgressCallback` by serialising each sync event as a newline-delimited JSON object to a stream, enabling subprocess hosts to parse progress without scraping Rich output.

- `stream`: defaults to `sys.stdout`; each line is flushed immediately
- Emits `{"kind": "start", ...}`, `{"kind": "done", ...}`, `{"kind": "skip", ...}`; `phase`/`summary` envelope events are emitted by the calling command, not here
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.__init__ fingerprint=4ed2aa9e0869d49d8e23949ed8110d89b7a871df3e40583ca4a3255f3e640612 body_fp=17a6e7673afc0f3de054898a0cf315eaa89fe14a2e2255d99af637948e469002 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=model -->
## `def __init__(self, stream: Any = None)`

Initialise `_JsonlProgress`, storing the output stream and defaulting to `sys.stdout`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress._emit fingerprint=ef26c79f59223ced602854e80b0eb04c17df7245ec17fdecd03c03779caa872a body_fp=e5922b8f55cf1413a25cf0d2850ad6a32171ba4739a9b59b50f7691654516563 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
## `def _emit(self, payload: dict[str, Any]) -> None`

Serialize `payload` to a JSON line and flush it to `_JsonlProgress._stream` immediately.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_start fingerprint=74eaca981cfa70b628b1cc1cc5426cc694fcfebb59fbf12062bea307de95476f body_fp=588ee819cbb9cd048b5691043857f55daf076a2d1652f45fd4b70f48b17874ae source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
## `def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None`

Emit a `{"kind": "start", ...}` JSONL event when a file sync begins.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_done fingerprint=3d84dfc675811299240d4290075310a4604fadec0ae7979b800b7a010db19e3d body_fp=1777e226a99b9363f61a2b3255de8eb6c6d81a9243fbbbad89696b48338914ac source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
## `def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None`

Emit a `{"kind": "done"}` JSONL event when a file finishes syncing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_JsonlProgress.on_skip fingerprint=2bbfaf11160d7d62cb1a5ed009bfba8e930785a96ecae21c175c3c2296531599 body_fp=78966db2b911a8b0f49332129b747e870a7678228c06223b3a24195480d5f85f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
## `def on_skip(self, rel_path: str, reason: str) -> None`

Emit a `{"kind": "skip"}` JSONL event on `_JsonlProgress`'s stream when a file is skipped during sync.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:emit_jsonl_event fingerprint=376721b7cfba875cf18dba24b9a39760deddb6042f3ef16032fa0f771876b330 body_fp=16883f876eee530645bf26a8efd860488fc08c70cd5a025a806d08b77cc31241 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=io -->
## `def emit_jsonl_event(payload: dict[str, Any], stream: Any = None) -> None`

Serialize `payload` as a JSON line and flush it to `stream` (defaults to stdout).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_acquire_write_lock_or_exit fingerprint=a5d28922bc774eedf46b515668c61a5a97ca0ba9ba85c53cf9973ad7a6638fbc body_fp=8181e4e62dc730d38caf3bcbc83ddac8a45bd9ee6af74b26573f79263feedf8a source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _acquire_write_lock_or_exit( project_root: Path, reporter: Reporter, command_name: str ) -> Iterator[None]`

Context manager that acquires a write lock for the duration of a command or exits with code 2 if contended.

- Operator-typed commands get loud failures with exit code 2 when lock is held
- Hook-driven refresh commands get queuing semantics instead
- Exit code 2 is transient (retry), exit code 1 is non-transient (fix input)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_root fingerprint=cb38f4f23c7d70341f3303813bbf16946ba34f8eb595e29d5976b6172f7ec356 body_fp=5507dbc1926d34f5162d657b637b106f19b5ffc7db7d981cb91e283011e2e4f4 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=entrypoint -->
## `def _root( ctx: typer.Context, version: bool = typer.Option(False, "--version", help="Show trie version and exit."), quiet: bool = typer.Option( False, "--quiet", "-q", help="Mute mode: print errors only.", ), verbose: bool = typer.Option( False, "--verbose", "-v", help="Verbose mode: include per-symbol detail and token breakdowns.", ), ) -> None`

Typer root callback that initialises the shared `Reporter`, enforces mutual exclusivity of `--quiet`/`--verbose`, prints the version, and bootstraps telemetry before any subcommand runs.

- `--quiet` / `-q`: sets `Verbosity.MUTE`; mutually exclusive with `--verbose`, exits 2 if both given.
- `--verbose` / `-v`: sets `Verbosity.VERBOSE`.
- Stores the configured `Reporter` on `ctx.obj` so subcommands retrieve it via `_get_reporter`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_telemetry_bootstrap fingerprint=f6f6f0318c080e04dbad6edbf345f40a4e69fcc84f49dc4d7d452fe5aa73c0cb body_fp=c7e04022014726e3623e498039d2ec9c60a2448b80a28411407f1db181ea6b32 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _telemetry_bootstrap(subcommand: str | None, argv_tail: list[str]) -> None`

Configures telemetry from trie.toml debug settings and emits a CLI invocation event.

- Silently handles missing config files since `trie init` runs before trie.toml exists
- Emits "cli" event with subcommand name and argv tail for usage tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:init_cmd fingerprint=1d3815663e939a183a3615fa14bce2303216da8109575c962b16755709c45c26 body_fp=bdb520c7bfd396a9a9b23ab5edd91ef41a3f279a401fb0c9ebae68649bb0294e source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def init_cmd( ctx: typer.Context, root: Path = typer.Argument( Path.cwd(), help="Project root to initialise. Defaults to the current directory.", show_default=False, ), force: bool = typer.Option( False, "--force", "-f", help="Overwrite trie.toml if it exists, and skip Python-project detection.", ), install_hooks: bool | None = typer.Option( None, "--install-hooks/--no-install-hooks", help="Install a pre-commit hook that runs `trie verify`. Prompts when omitted in a tty.", ), run_scan: bool = typer.Option( True, "--scan/--no-scan", help="Build the symbol graph immediately after writing trie.toml.", ), ) -> None`

Create trie.toml config, update .gitignore, build symbol graph, optionally install pre-commit hook, and offer to run setup.

- `root`: Project directory to initialize (defaults to current directory)
- `force`: Skip Python project detection and overwrite existing config
- `install_hooks`: Install pre-commit hook (prompts in interactive mode if None)
- `run_scan`: Build symbol graph after config creation (default True)

Materializes `.trie/graph.db` when scanning, acquires write lock to prevent concurrent initialization, reports success/failure for each step, displays next-step recommendations, and offers to run `trie setup` interactively.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_is_interactive fingerprint=9af26a11d8892e9deb8f6d1cb71c159a940ccc2f1590f37251b1723c50a54b4e body_fp=e4059acfa0f5816db458b757f8f428208e3c35d484f16151ef6beccbdbc4d4a1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _is_interactive() -> bool`

Checks if stdin is a tty to determine if interactive prompts are safe.

• Returns `True` when stdin is connected to a terminal
• Returns `False` for non-interactive environments (CI, pipes, redirected input)
• Gracefully handles environments where `sys.stdin.isatty()` is unavailable
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_prompt_select_targets fingerprint=e20665fd0430702ade14c0dda97ce30b4012c0f6588df62c8b92b2f894e9b5b6 body_fp=3246b72e95d0ab6e94e5e9445fa897229201c8e2959aacb267cbc25e4688df43 source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=util -->
## `def _prompt_select_targets(reporter: Reporter, detected: list[str]) -> list[str]`

Prompt the user to select which detected agent harnesses `trie setup` should wire in, returning their slugs in detection order.

- `detected`: slugs of all auto-detected agents; caller guarantees len > 1 and tty
- Returns slugs in the order they appear in `detected`; re-prompts on unrecognised input
- Default selection is the single override-capable harness when exactly one exists, otherwise all detected
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus fingerprint=10b9fa24a55c3f94395395f64e759210655c5ed35e1ff88efc7374642065e94f body_fp=5fb4413cbfbe2cd552b3bfbdf451a965178958586660b1d6ae69f50db0e7b764 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `class _NoOpStatus`

Context manager that does nothing; used to conditionally skip status indicators.

Implements the context manager protocol with no-op enter/exit methods, allowing code to use `with _NoOpStatus():` when a status indicator should be skipped while maintaining the same control flow structure as when a real status manager is used.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=ae4ada410a0b20158e9da7189bb632120534c0025cca1c44aeda259c7769a653 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def __enter__(self) -> _NoOpStatus`

_NoOpStatus.__enter__ returns self to implement the context manager protocol as a no-op.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_NoOpStatus.__exit__ fingerprint=9f730a1a70a6144b0dc8da4942d9093cd268d625eafac5188775d0d6b8b25f08 body_fp=b8fc5c0c19b967a8c91adf7c0f36fd800670f26d54c2a1c05469649e2e939fb2 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def __exit__(self, *exc: object) -> None`

`_NoOpStatus.__exit__` implements the context manager exit protocol, taking exception parameters and returning None.

- Always returns None regardless of exception arguments
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:plan_cmd fingerprint=392a35fcab27024390840bdc07a64b1d2275bc23f49e4982eb90baf4d9a5d597 body_fp=4ae16c3dd49454776ba7b88cf0d629082430626d0b066579ff81c96399ff93b4 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def plan_cmd( ctx: typer.Context, model: str | None = typer.Option( None, "--model", help="Override the configured model for cost estimation." ), all_: bool = typer.Option( False, "--all", help=( "Show the cost of regenerating every in-scope file (full re-bootstrap), " "not just the incremental worklist. Default on a fresh project; opt-in on " "an established one." ), ), offline: bool = typer.Option( False, "--offline", help=( "Skip the count_tokens cost preview (the only network calls plan makes). " "Shows the worklist with symbol counts; estimates read $0." ), ), ) -> None`

Scans project for drift, computes either incremental or full-bootstrap worklist, and displays estimated cost before any LLM work begins.

- Auto-detects incremental mode (stale files + cascade) vs full re-bootstrap based on existing triefacts unless `--all` forces full mode
- `--offline` skips the `count_tokens` network call by substituting a zero-token stub, printing the worklist with all cost estimates as $0
- Performs drift check first but continues on drift (informational, not a gate)
- Acquires write lock to ensure consistent store snapshot during planning
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:verify_cmd fingerprint=3182dc32d5135484a723e7e1259b7fa50871036159d113c4aa82c3257476827a body_fp=ff749a590ada0db1371141175d1953611f7d74fc5676dec46884038aeb0de686 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def verify_cmd(ctx: typer.Context) -> None`

Runs bidirectional drift check and exits with code 1 if triefacts have diverged from source code.

- Detects both code→triefact drift (source changed without regeneration) and triefact→code drift (tampered sections or deleted symbols)
- Designed for pre-commit hooks and CI environments - no LLM calls, no database writes
- Same drift detection logic used by `plan` and `sync` commands, exposed as standalone verification gate
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:status_cmd fingerprint=e069c10392687d5c5efd6e5e66ab595767b99099008bcbf0388eab0623ce4462 body_fp=f2e0afeb73c2e543c606a21a37bf283ef4bc4b59e464acec86769c28ba6736ac source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
## `def status_cmd( ctx: typer.Context, as_json: bool = typer.Option( False, "--json", help="Emit the status as a single JSON object instead of prose." ), ) -> None`

Reports trie's working state including active writer status, stale triefacts, and pending edit patches.

- Performs offline content-drift scan using same checks as `trie verify`; passes an open `Store` as a fingerprint cache to `check_project`
- Unions drift results with refresh-computed pending set for complete stale file list
- Queries graph store for patch summary including modify/create patch counts
- Outputs either JSON object (with patches field) or formatted prose based on `--as-json` flag
- Safe to run during active sync operations as it only reads status files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:lock_check_cmd fingerprint=9ad893426718b3f4d7092ec0d27c95d453461a354f84ee952bc3592cc2ba64fc body_fp=e23d4502b2934542a381f6c9564f21c2d2987af4e8eac427799933c642d4e1fb source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def lock_check_cmd(ctx: typer.Context) -> None`

Probe whether another trie process holds the project's write lock, exiting 2 if contended.

- Designed for pre-commit hooks to detect racing `trie sync` operations
- Exit code 0: lock is free or project has no trie.toml
- Exit code 2: lock held by another process, caller should retry
- Uses acquire-then-immediately-release pattern that never blocks or interferes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_graph_only_sync fingerprint=4c5d863696f5ba2c929eb80cd8963d0843e467495348527317636c8cf3608a64 body_fp=d7c5db7ab920566ff1175c68a4b993c9ff0ad10b526c26615217ef4790b83f3d source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=orchestration -->
## `def _run_graph_only_sync(reporter: Reporter, *, as_json: bool, before_turn: bool) -> None`

Rebuild the symbol graph and stamp freshness for `trie sync --graph-only`, without any LLM call.

- `before_turn` — selects `ensure_fresh_before_turn` (pre-turn gate) vs `ensure_fresh_after_turn` (post-turn sweep)
- `as_json` — mutes the Rich reporter and emits JSONL events to stdout instead
- Contention is handled by coalescing: on lock conflict, marks a queued tail pass rather than exiting 2 (hook semantics, not operator semantics)
- Raises `typer.Exit(1)` outside a git repo (`NotAGitRepoError`) or when config is missing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_graph_sync_progress fingerprint=ad4958aee008ab0926b0f9f63526e80c1a36229c413fc075ab443e29a18ae23a body_fp=16c715618808322d118f62161823cb34dfa441514f18dad5613711a283638eed source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=orchestration -->
## `def _graph_sync_progress( reporter: Reporter, as_json: bool, *, project_root: Path ) -> Iterator[ProgressCallback]`

Context manager that selects and yields the correct `ProgressCallback` for a graph-only sync, always mirroring into `.trie/` activity state.

- `as_json=True` yields `ActivityProgress` wrapping `_JsonlProgress`; `False` yields one wrapping `_ProgressAdapter` with a Rich live bar.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_freshness_json fingerprint=4597cfd483b0bdde0922cb779487e1ac288f00781eaef91d788b545437eace61 body_fp=a30d5eae88342517bd5fd67039a8c75205186f307a73363ff796968cd7b35647 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=io -->
## `def _emit_freshness_json(result: FreshnessResult, *, mode: str) -> None`

Emit a `{"kind": "summary"}` JSONL event encoding a `FreshnessResult` graph-sync outcome; drops the `files_synced` and `cost_usd` fields present in the previous version.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_freshness fingerprint=5989cc5b45cbe487d1776d94c865e2201e4600c6aad044808cf51713be95ce49 body_fp=3e630f62246c197f52d3911bcccd0c4b3b35ce545f22575b5561b7ff63a00f25 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None`

Render one line per graph-sync outcome with two clauses: graph state and prose freshness.

- Always emits both clauses regardless of `result.refreshed`; stale prose triggers `reporter.warn` instead of `reporter.success`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_AUDIT_TAIL_BYTES fingerprint=988e06fd434d4fb62e32a6167721980312ced4e8b1a3ff48967660d9677b18aa body_fp=cd2eb539e069c103b37acaf0996b1b8e6e274409a1411a7978b0b73635b43778 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=config -->
Default read window for `audit_cmd`: limits JSONL parsing to the trailing ~4 MB of the log file for speed; pass `--all` to override.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:audit_cmd fingerprint=67fc1fe9613a92bd595bf468ba64ed9927f1c36f87d5093efb78b9cc20b19767 body_fp=b665638024f3f59c81b1d61bb123eaaa87ad5e68b5b8d290e656f208c734df60 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
## `def audit_cmd( ctx: typer.Context, log: Path | None = typer.Option( None, "--log", "-l", help="Path to the debug.jsonl to read. Defaults to the configured debug.log_path.", ), compare: Path | None = typer.Option( None, "--compare", "-c", help="Render a side-by-side comparison: this log is the candidate, --log is the baseline.", ), as_json: bool = typer.Option( False, "--json", help="Print the summary as JSON. Mutually exclusive with --compare.", ), all_history: bool = typer.Option( False, "--all", help=( "Parse the entire log instead of the recent tail. The default reads " "the last ~4MB (roughly the recent sessions) so the command stays " "fast on long-lived projects whose logs run to tens of MB." ), ), ) -> None`

Summarise telemetry logs with MCP usage, sync activity, retries, and CLI invocations.

- `--log`: Path to debug.jsonl file (defaults to configured debug.log_path)
- `--compare`: Render side-by-side comparison with deltas (candidate vs baseline); always reads fully
- `--json`: Output as JSON instead of human-readable format
- `--all`: Parse the entire log; default reads only the last ~4MB tail
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_resolve_audit_log_path fingerprint=bad827442bead53f02cef4cde6dbfbf24222786901e57c0aee3d03c19918abf5 body_fp=638bd9b468f10a3bb02fcaec808a3e791c863ba932d07410ab65dc7618c1f040 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _resolve_audit_log_path(log: Path | None, reporter: Reporter) -> Path`

Resolves the audit log path for `trie audit` command.

• Falls back through: explicit `--log` flag → config's `debug.log_path` → `./debug.jsonl`
• Returns absolute paths, resolving relative config paths against project root
• Allows cross-project audit by not requiring trie.toml when explicit path given
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_intent_gate fingerprint=124bbd271ea315303b54d48261532e35a866ad2e7d7913d204a3fa478a2d6042 body_fp=c4d4385eaaf8150c2249c0b24c19712b2536152c87ec0cf8bfda1c5b51630b81 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=domain -->
## `def _run_intent_gate(reporter: Reporter, config: Config, project_root: Path) -> bool`

Evaluate the intent gate via `trie.intent_gate.evaluate`, render the outcome, and return `True` when all touched symbols have patch notes on record.

- Returns `False` and prints a copy-pasteable worklist when any touched symbol lacks a note.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_warn_on_version_skew fingerprint=8e948cb365beaa2acd7d3e27d9578d3316ddec7ba633ac2f3ee6bc6caff3422b body_fp=4cb68c3859166007854ee0d50a18668a1ecd7b1e5768eb17f21fa9aa6d5594f1 source_ref=f803cb599a03936d496cac84820bfd4e78a600a2 role=util -->
## `def _warn_on_version_skew(reporter: Reporter, project_root: Path) -> None`

Warn via `reporter` when the installed `trie` binary version differs from the version declared in the project root's `pyproject.toml`.

- Only fires when `pyproject.toml` exists and names `"trie"` as the project; silently no-ops otherwise.
- Advisory only — never raises or blocks the caller.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:gate_cmd fingerprint=0ca676558220b3e074f863daff5fa45ab48c8c376936521d5dffeec3dac3e140 body_fp=c08128edd610170169307769f46e5a315c74bed2ec0e6eb71943457639aff0bc source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def gate_cmd( ctx: typer.Context, no_digest: bool = typer.Option( False, "--no-digest", help="Skip the digest write (gates only: lock + verify + intent).", ), ) -> None`

Run the full pre-commit guard sequence: version-skew check → lock-check → verify drift → intent gate → digest write.

- `--no-digest`: skip the digest write; runs only lock + verify + intent.
- Exit 0: all gates pass; exit 1: verify or intent failed; exit 2: write lock contended.
- No-ops cleanly when no `trie.toml` is found in the current directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:intent_cmd fingerprint=42b1f6bdceb860f506eafa96f140cd0d81b726b5c8f152de881e9094d76a99a0 body_fp=329c2284fa0bd5f07bdae387fc38fefa29365d3ac3503fc89b05c55ff559dd9f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def intent_cmd(ctx: typer.Context) -> None`

Enforce that every symbol changed vs HEAD has a patch note on record; exits 1 with a copy-pasteable worklist when coverage is missing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:index_cmd fingerprint=03be3ee88a8f66b5d0fcb774638b5784f0ff798428a46ca21c6d844027dd6ab2 body_fp=66d9a58bebb45244391a822c5b6a010b9c58765ffb58326f7ef6188e30986525 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def index_cmd(ctx: typer.Context) -> None`

Regenerate the triefact-tree index (`<triefacts.root>/README.md`) from the live graph store without calling the LLM.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:diff_cmd fingerprint=d688004861efa2c07fa47c916179ab285fa34e31c648c7201c1f7b2ab1eb4550 body_fp=9dfe18a751b25c2266a0f01edde371caec6386b241e153bb089af3dbb588e4a1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def diff_cmd( ctx: typer.Context, base: str = typer.Option("HEAD", "--base", help="Git ref to diff the triefact tree against."), raw: bool = typer.Option( False, "--raw", help="Skip LLM synthesis; print patch notes and the raw triefact diff.", ), as_json: bool = typer.Option( False, "--json", help="Emit the collected evidence as JSON (no LLM call). Mutually exclusive with --raw.", ), model: str | None = typer.Option( None, "--model", help="Override the model used for narrative synthesis." ), write: bool = typer.Option( False, "--write", help="Prepend a digest entry to the TRIE_DIFF file (config diff.write_path) and exit; used by the pre-commit hook.", ), ) -> None`

Typer `diff` command that collects session evidence (triefact git diff + patch notes) and either synthesises an LLM narrative, dumps raw evidence, emits JSON, or writes a digest entry to the configured `diff.write_path`.

- `--base`: git ref used as the diff baseline; defaults to `HEAD`
- `--raw` / `--json`: mutually exclusive; skip LLM and print raw notes or JSON envelope
- `--write`: pre-commit hook mode — delegates to `_run_digest_write`; mutually exclusive with `--json`
- `--model`: overrides `config.models.cascade` for narrative synthesis only
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_digest_write fingerprint=0443c9cee11db826180b5a19cfe6e8377ec46a8cc8a7f88a5ba10069a5015774 body_fp=714fd8f1fd1f43e44ef9443fb790413f0fa7bdaefd37a8160809db873c99cb9a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=orchestration -->
## `def _run_digest_write( reporter: Reporter, config: Config, project_root: Path, *, base: str = "HEAD", raw: bool = False, model: str | None = None, stage: bool = False, ) -> bool`

Collect session evidence, render a digest section, write it to the configured diffs directory, and clear applied patches from the store via `store.delete_applied_patches()`; shared by `diff_cmd` and `gate_cmd`.

- `stage`: when `True`, also `git add -A`s the digest archive dir and symlink for an in-flight commit.
- Returns `False` only on hard `OSError`; returns `True` when a digest was written or there was nothing to record.
- `raw`: when `True`, skips LLM narrative synthesis regardless of config.
- Amend/retry: if a digest entry for the same parent commit already exists, its rows are folded into the evidence and the file is rewritten in place.
- No `session` parameter or digest cursor; evidence is consumption-based (pending-intent file + staging queue).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_scan_breakdown fingerprint=2e73f73d6b381e6f0d1a30836e44644e8628a03f8aeee95872bda7faa8fcc1d3 body_fp=2a304908b0d95d7c71e2bebab5ead440b56560bdfaf088d8ff624db7470ab442 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _print_scan_breakdown( reporter: Reporter, scan_result, db_path: Path, project_root: Path ) -> None`

Prints a colored breakdown of files scanned by status and symbols/edges count.

- Renders new/updated/unchanged/removed file counts with color coding
- Falls back to "no files in scope" when no categorizable files exist
- Shows total symbols and edges written to the database file
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plan fingerprint=5f2da078a99fec69dbdcddca27d22838e07d134148b753b09c8d4edd1404e8a8 body_fp=f5518d3b96a02037d1522b24dc752b9980139a249cde932bd942f211e5f10949 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _print_plan(reporter: Reporter, plan: BootstrapPlan, model_id: str) -> None`

Prints a bootstrap plan summary showing model, file count, total cost, and top 10 files with their symbol counts and estimates.

- Displays total estimated cost formatted to 4 decimal places
- Shows first 10 plan items with file path, symbol count, score, and per-file cost
- Adds "… and N more" footer when plan exceeds 10 files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_incremental_plan fingerprint=61b8ccd749271c4ceb104b106904e7bd1a38bf9df7685a5ce31f56af665c73f2 body_fp=45ca376d453adfb6b72e8d2bea7cd6b5fa4be89390a7f898631feb8327284717 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _print_incremental_plan( reporter: Reporter, plan: BootstrapPlan, worklist: IncrementalWorklist, model_id: str, ) -> None`

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
<!-- trie:section symbol=trie/cli:_print_drift_detail fingerprint=8a63edb41f6619840b29e3b7633ab94852d56e8b2a79b89dcf180f9c1b8a6367 body_fp=2f038db123d5fc1ac6175080c0fd238200fc137c1e21b270429c28d0acf327bb source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _print_drift_detail(reporter: Reporter, items: list) -> None`

Renders drift check items grouped by triefact file with colored status indicators and indented issue details.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_verify_drift fingerprint=e1756d124c46c591211c8188a85a2319d1a72a9fdbabfbf20bad7e49e0c2ca75 body_fp=814889e75d69a444d0e791c719d9e37d0bcb235bf4ba33c08d90baf5a1bb3af7 source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=domain -->
## `def _verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool`

Checks triefact tree coherence and reports drift, returning True if clean.

- `exit_on_drift`: When True, raises `typer.Exit(1)` on drift (for `verify` command); when False, warns and continues (for `plan`/`sync`)
- Opens `graph.db` as a content-addressed parse cache to keep the check under budget
- Returns False if drift detected, True if tree is coherent
- Reports detailed drift items when verbosity is MEDIUM or higher
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:sync_cmd fingerprint=bd60267768471ecf35dc486645dbf74508e6972988b7daa520fe467f6bb3815b body_fp=b2dca4f2ea3a0e4f345f23ac0f958009c03878d7658e6cf2391a64333a6c9493 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def sync_cmd( ctx: typer.Context, graph_only: bool = typer.Option( False, "--graph-only", help=( "Rebuild the symbol graph and freshness stamp from source without " "calling the LLM. Free and fast; drifted prose is marked stale for " "a later full `trie sync`. This is what turn hooks run." ), ), before_turn: bool = typer.Option( False, "--before-turn", help=( "Hook mode (implies --graph-only): cheap pre-turn freshness gate — " "no-op when nothing changed since the last graph sync." ), ), after_turn: bool = typer.Option( False, "--after-turn", help=( "Hook mode (implies --graph-only): post-turn sweep that picks up the " "agent's own edits. Default turn mode for --graph-only." ), ), as_json: bool = typer.Option( False, "--json", help=( "With --graph-only: emit machine-readable JSON-Lines progress to " 'stdout instead of Rich output. Each line is one event ({"kind": ...}).' ), ), file: Path | None = typer.Option( None, "--file", "-f", help=( "Sync exactly one source file. Regenerates only its stale symbols by " "default; combine with --force for a full fresh rewrite." ), ), all_: bool = typer.Option( False, "--all", help="Force a full re-pass (every file in scope), even if triefacts already exist.", ), budget: float | None = typer.Option( None, "--budget", help="USD budget cap. Stops once cumulative actual cost reaches this.", ), limit: int | None = typer.Option( None, "--limit", help="Cap the number of files synced.", ), dry_run: bool = typer.Option( False, "--dry-run", help=( "Preview what `trie sync` would change. Regenerates stale triefacts into " "`.trie/preview/` and prints unified diffs (makes API calls — cap with " "--budget / --limit)." ), ), metadata_only: bool = typer.Option( False, "--metadata-only", help=( "Refresh triefact front matter from the live store without calling the LLM. " "Useful after a graph-only change (e.g. an improved reference resolver) " "where edge counts moved but source did not." ), ), roles_only: bool = typer.Option( False, "--roles-only", help=( "(Re)infer only the architectural role tag for every symbol against a " "project-specific role vocabulary, without regenerating prose. Derives " "the vocabulary first if none exists. Cheap relative to a full sync." ), ), rederive_taxonomy: bool = typer.Option( False, "--rederive-taxonomy", help=( "With --roles-only, re-derive the role vocabulary from scratch even if one " "is already saved. Use after large architectural change." ), ), model: str | None = typer.Option( None, "--model", help="Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.", ), force: bool = typer.Option( False, "--force", help=( "Force cold regeneration for every symbol in the file, bypassing the " "diff-aware path. Only valid with --file. Use when existing prose is " "known to be wrong and a full fresh LLM pass is needed." ), ), ) -> None`

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
<!-- trie:section symbol=trie/cli:_has_existing_triefacts fingerprint=e3127b5904f703ca364034223353af7b38d3aa9ec4c1fa155e0f4f69852c6b1c body_fp=091d2f07a9c0199c9a4821cbd283d5a9cacdf1b22c7379aa30d53eadf43d3e05 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _has_existing_triefacts(triefacts_root: Path) -> bool`

Returns True if the triefacts directory exists and contains at least one markdown file.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_full_pass fingerprint=e525efbf503ab98d85cc1594568ac0286bf2411e58b398b0043ec23c32dfb9b8 body_fp=19960490acc4c0b8287f1b314a6b7ea56d7dd152af5ac6a77e246622d3e34e09 source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
## `def _run_full_pass( *, reporter: Reporter, project_root: Path, config: Config, model: str | None, budget: float | None, limit: int | None, ) -> None`

Executes first-run bootstrap sync: scans project, builds plan, prompts for confirmation, then generates triefacts and refreshes the index.

- Requires budget/limit or interactive confirmation when no cap is set
- Scans project and builds token estimation plan before proceeding
- Calls `_refresh_index_quietly` after a successful sync if any files were synced
- Calls `stamp_graph_fresh` after the store closes to mark the graph current for subsequent graph-only syncs
- Reports per-file errors via `_report_sync_errors`; exits with code 1 if any occurred
- Reports final cost comparison (estimated vs actual) and files processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_refresh_index_quietly fingerprint=d529f7105e01e70c95ec0edde7ecd5d69d83d6a4b700b9586c39ec54c6ad83d6 body_fp=9d0d8322e3989f17140475cea9d78214d0278d2a9ea2c5113134d490fab25686 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _refresh_index_quietly(config: Config, project_root: Path, store: Store) -> None`

Regenerate the triefact index after a sync, silently swallowing all exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_report_sync_errors fingerprint=728c6f436fd1675b4a5e8b61b79f8776946aa9129a1e2634405f94b84d5323ba body_fp=2a2d7617dd1472cca467f4aff11f29a78fa82fbca27b6e41b7e22d80ba7cde79 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _report_sync_errors(reporter: Reporter, file_errors: list[tuple[str, str]]) -> bool`

Report per-file sync failures to `reporter`, printing up to 5 errors plus a credential hint when error text suggests a missing API key.

- Returns `True` if any errors occurred, `False` if `file_errors` is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_dry_run_diff fingerprint=ea340e6fb3ae76699d84d7c95cb3dbffd3a8307777a7fada12178a997f8133c5 body_fp=3f29d8baea40400bbb4f35e8600ac966146f2584a6fdb1c3b9648305995e14e5 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=domain -->
## `def _run_dry_run_diff( *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None ) -> None`

Implements `trie sync --dry-run` by regenerating stale triefacts into `.trie/preview/` and printing unified diffs.

- **model**: Uses `models.bootstrap` if not overridden
- **budget/limit**: Caps LLM cost and file count
- **output**: Prints per-file diffs or notes fingerprint-only changes
- **exit**: Reports total cost and skipped files due to budget constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_single_file_sync fingerprint=e5cd7f2d73c04c4046b29c44387cffed3a1156f0b63e05ca1ae792ff6e7739aa body_fp=00a2988d2657d1bdad6608b1d96c0dd6be5fa159f73fb412d94e1ad1adf482bf source_ref=8d72848bbe76bcdd20773c451d84afe6200dbb22 role=api -->
## `def _run_single_file_sync( reporter: Reporter, file: Path, model: str | None, force: bool = False ) -> None`

Sync one source file's triefact, regenerating only stale symbols unless `--force` is given.

- Without `--force`: opens the graph store and passes it to `check_project` to identify stale symbols; exits early if all are fresh; passes `symbols_to_regen` to `sync_single_file` so fresh sections pass through byte-identically.
- With `--force`: skips drift check and cold-regenerates every symbol.
- Exits 1 if `file` doesn't exist, config is not found, or the file is outside the configured source root.
- Reports symbol counts distinguishing regenerated vs passed-through, plus token usage.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_metadata_only_refresh fingerprint=181b6716a37fd19e6aa687d794cdba69cba15c48420f9c798a50e0fd1548f57c body_fp=f22cf54be5f1cc4f7a39339014c61295c589a9e0fffa31db249d5aa1612f3dd5 source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=orchestration -->
## `def _run_metadata_only_refresh(reporter: Reporter) -> None`

Refreshes triefact front matter from the live store without LLM calls, designed for post-graph-change updates.

- Rescans project to pick up new edges from resolver changes
- Updates ref counts and defines entries for each in-scope triefact
- Skips files outside source_root and no-ops when metadata already matches
- Calls `stamp_graph_fresh` after the pass so the next graph-only sync no-ops
- Reports changed count vs total processed files
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_roles_only_sync fingerprint=23f7dfa386342155618233ac03b5c009c87e48a694cbeb3f741f37e4984e9fc8 body_fp=f6464f16e16b5a0317fd8318e1ddbbb43ce681a4f5d49b593d81a2ae29acb3ab source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
## `def _run_roles_only_sync(reporter: Reporter, *, model: str | None, rederive_taxonomy: bool) -> None`

Runs the roles-only sync mode: derives/loads role taxonomy then classifies every symbol against it without regenerating prose.

- Scans project first to ensure store reflects current source
- Uses cascade model (or override) for role classification
- Stamps graph freshness after the scan so the next graph-only sync no-ops
- Reports taxonomy derivation, symbols classified, and role changes
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_incremental_sync fingerprint=a6f849b8ffac64772326ad46e9af0e7a9e00b371320dde829a37ae3c9833de0a body_fp=fdc5d639dbe4ebcb4e0065660e41acd389662115329b43e55628b8b2f287a7d5 source_ref=732563097108f24f0d4cf893599e09db87469090 role=orchestration -->
## `def _run_incremental_sync( *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None ) -> None`

Execute an incremental sync that regenerates only stale triefacts and their cascade dependencies.

- Loads project config and opens the SQLite store with activity progress tracking
- Calls `run_incremental` to sync directly stale files and their cascade neighbors; calls `_refresh_index_quietly` when any files were synced
- Calls `stamp_graph_fresh` after the sync so the next graph-only turn hook no-ops
- Reports orphan triefact removals and sync statistics to the user
- Calls `_report_sync_errors` after syncing; exits code 1 if all files failed or any file errored
- Honors budget/limit constraints and reports any files skipped due to those caps
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:setup_cmd fingerprint=5628da5c475d18230f6a33c60d1b52e23cb950fa7d8e3503390153f058b060de body_fp=03ad17bf3fc52ff5749e1a9ed58d4ec49ad852e9318b1e47fff7f54862b96bf5 source_ref=bf098bf66789b2b6073a47dbbde26a79e893ecd2 role=api -->
## `def setup_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, "--target", "-t", help=( "Set up for a specific agent. Repeat the flag for multiple targets. " f"Known: {', '.join(MCP_TARGETS)}." ), ), install_all: bool = typer.Option( False, "--all", help="Set up for every known agent. Skips per-target detection.", ), scope: str = typer.Option( "project", "--scope", help="MCP install scope: 'project' (writes into this repo) or 'user' (~/.<agent>/...).", case_sensitive=False, ), print_only: bool = typer.Option( False, "--print-only", help="Print what would be written for both MCP and hooks; don't touch any files.", ), dry_run: bool = typer.Option( False, "--dry-run", help="Resolve target paths and show what would change, but don't write.", ), no_overrides: bool = typer.Option( False, "--no-overrides", help=( "Skip the tool-override step. By default, `setup` replaces the " "agent's built-in `grep` and `read` with wrappers that route " "through trie (and adds `trace`). Pass --no-overrides to " "install hook + docs only and leave the agent's built-ins alone." ), ), with_mcp: bool = typer.Option( False, "--with-mcp", help=( "Also register the trie MCP server for each target " "(same as `trie mcp install`). Off by default — the hook and " "tool overrides are sufficient for most setups." ), ), ) -> None`

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
<!-- trie:section symbol=trie/cli:_render_setup_plan fingerprint=9c0c752d54c3dcfa921629d39973d8145b811fdd047a21cf7002c9a974f78517 body_fp=3c0abcbe71684e03703b06a0eb20e8d9a09e9c382990c7963b61a68ed23b5890 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_setup_plan( reporter: Reporter, mcp_plan: InstallPlan | None, hook_plan: HookInstallPlan, docs_plan: DocsInstallPlan, override_plan: ToolOverrideInstallPlan | None = None, ) -> None`

Renders a combined setup plan report grouping MCP, hook, and override results by target with a separate docs section.

- Groups results by target slug, showing each target's MCP/hook/override outcomes indented under its display name
- Emits manual setup warnings and JSON previews inline where applicable
- Renders docs section separately since it's target-independent
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_override_target_block fingerprint=1ede2878bb98b6df394615cdd58ab4ecae185270f43cadf83ab95df212d1565d body_fp=07fd8631beca813b8398de61739db5a33f7ccce6a7aefe9c946cc29f69c53955 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_override_target_block(reporter: Reporter, result: object) -> None`

Renders tool-override install outcomes for a single agent target within the setup command output.

- Prints summary line showing override action status
- Lists per-file outcomes indented beneath the summary  
- Handles manual setup notices for unsupported agent harnesses
- Uses Rich markup for consistent visual formatting with hook install output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_format_action fingerprint=8dac93a50edff702bbc2e173939a50d0d8f091203a3dd20675261719d0821994 body_fp=812fe044778b3d0eaf1f91e2e1cfb0ab9369b0471bc06a15608a9ec544acee35 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _format_action(action: str, path: Path | None) -> str`

Formats an installation action result as a display string with optional path suffix.

- Returns `action` alone when `path` is None, otherwise `"action → path"`
- Used by setup command renderers for consistent MCP and hook line formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_open_tools fingerprint=9ff890870c2306ffd8bde89af77920adb349e44244a0688aa15babc3e845bd9b body_fp=abbf9636caae873819a827d6211c9f2aaea6c21382022f0d84d95088381c6537 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _open_tools(reporter: Reporter) -> TrieTools`

Resolves project root from trie.toml and returns TrieTools instance configured for CLI telemetry.

• Returns TrieTools with event_name="cli_call" to distinguish CLI usage from MCP calls in audit logs
• Caller must close() the returned instance to release SQLite handle
• Raises typer.Exit(1) if trie.toml not found
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_emit_envelope fingerprint=d1726392a85988504e1f10436d84418156249e0a58208a7944a61a7736385139 body_fp=6c2e79e0abf197a9a639e6aa58c2a5fbb094afdd0fbc3a19a2cfc07a7757e05a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _emit_envelope( envelope: dict[str, object], *, as_json: bool, reporter: Reporter, render: Callable[[dict[str, object], Reporter], None], ) -> None`

Prints envelope as raw JSON or via provided renderer, exits with code 1 on errors.

- `as_json=True`: dumps to stdout without ANSI codes for agent parsing
- `as_json=False`: delegates to the provided renderer function
- Error envelopes always render through the renderer for human diagnostics
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_patched_tag fingerprint=dc648bd9f208afe7454d79f5eebafca65d77f7014569d3999b97bf3f93928efe body_fp=69d72b565aec1c0ff4ada01d232afdf1afcedde4f633935ddb037bffe24058e2 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _patched_tag(count: int) -> str`

Returns a yellow `[patched: N]` tag for count > 0, empty string otherwise.

Used in grep and trace output rendering to visually mark symbols with pending edit patches.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_grep_output_is_tty fingerprint=954ccea2a94869ba8560359233d58c8ec8285b5f8ffdb13508098fceca9bd8b5 body_fp=15a9af092f4a4838593cc8581dccba5038e1465ec90660cd7dc40a357716640e source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _grep_output_is_tty() -> bool`

Return `True` when `sys.stdout` is an interactive terminal, guarding Rich table rendering in `grep` output.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_grep_records fingerprint=f05dbd1300d4c47bc7b053331ccf3a8112249ac363c8b2336e857ef8a145bf93 body_fp=1d86c9a3945f60401ca8d729b1c36380e0b48c546f9a0d2e1ec046927b6cd4fa source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _print_grep_records( reporter: Reporter, rows: list, *, qname_suffix: Callable[[dict], str] | None = None ) -> None`

Print grep hits as plain, full-width, one-record-per-line output for non-tty consumers.

- `qname_suffix`: optional callable appending a tag string (e.g. patch count) to each qname before printing.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_grep fingerprint=e1ab9766de8658fbd35cc7a4c2034fb9b13475d687024bf152efd8b0c7c640d4 body_fp=0e9e32a73e5e27c4849264437e8fc0a71cac5148f1a1f04d88d558e111931b8a source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _render_grep(envelope: dict[str, object], reporter: Reporter) -> None`

Renders human-readable output for `trie grep` command results.

- Interactive terminals (tty) get a Rich table; piped/non-tty output gets plain untruncated records via `_print_grep_records`
- After hits, prints any `related` (prose-matched) symbols
- Falls back to candidate matches table (or plain records when not tty) when no exact hits found
- Shows pending patch counts as yellow tags on qnames
- Routes errors to `_render_error_envelope` for consistent error formatting
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read fingerprint=2b10e36d759a5d0ea615a7db338822b6231723a2963b138ff8997b4262a3a179 body_fp=503a212119fb64393989cc55537366bc0ead5dbc1a20622165e82416ab4e5be5 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_read(envelope: dict[str, object], reporter: Reporter) -> None`

Renders human-readable output for `trie read` command responses, displaying symbol metadata, notes (before prose), prose, pending patches, caller/callee relationships, and a history block.

- **envelope**: MCP response dict containing qname, signature, source_pointer, prose, callers, callees, pending_patches, history, and notes
- **reporter**: Console output handler for styled text rendering

Formats the symbol's qualified name and signature at the top, then prints any `notes` entries early (⚠-prefixed notes in bold yellow, others in dim) before the prose block, followed by pending patches with their origins and notes, then caller and callee lists with one-liners, then a `history` block (date · change lines with optional title), and finally notes again as yellow-banged lines. Error responses are delegated to `_render_error_envelope`.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_trace fingerprint=1af973f434ca837af6bd3bf7f5f4a14871b62746089ef1d6845c6f30cd474b15 body_fp=c9ae7852576f9817781d5d9a763894881b877af7db58f2380165f34acb8878f8 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_trace(envelope: dict[str, object], reporter: Reporter) -> None`

Renders human-readable output for `trie trace` command responses.

- Displays root symbol with its one-liner description if present
- Lists all nodes in the trace with qnames, one-liners, and pending patch indicators
- Shows edges with directional arrows (→ for outbound, ← for inbound)
- Reports truncated hubs and any diagnostic notes from the trace operation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_error_envelope fingerprint=eb679d10d43ad20f60079ecf971b43d76c2d34e9df56abca2edbc761852875e9 body_fp=a9d881d908ca6c569f12aec1c4c551550a8828a826c67bec2518aa7d1858bea9 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_error_envelope(err: dict[str, object], reporter: Reporter) -> None`

Renders standardized error envelope from MCP tools into human-readable form via Reporter.

- **err**: error envelope dict containing `code`, `message`, and optional `suggestion`
- **reporter**: Reporter instance for formatted console output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_build_grep_predicate fingerprint=b001ffd9b944a9b6aec077b245e5eeb62037c4b7abaa0250017e5d70f1edfbdd body_fp=145b6e89678c7ce5b7037eae686e5030a18a599a5d70bd833ddd86e0b925888b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _build_grep_predicate( name: str | None, kind: str | None, scope_prefix: str | None, scope_exclude: list[str] | None, public_only: bool, inbound_min: int | None, inbound_max: int | None, outbound_min: int | None, outbound_max: int | None, predicate_json: str | None, reporter: Reporter, ) -> dict[str, object]`

Assembles a search predicate dictionary from CLI flags for the `trie grep` command.

- `predicate_json`: Base JSON predicate; individual flags override matching fields
- Constructs nested `inbound_count`/`outbound_count` objects when min/max bounds provided
- Exits with code 2 on invalid JSON to distinguish from other error types
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_cmd fingerprint=825bfd6a4a60a6971e8d99bd056b8440fad1bb1febf4fe68c6b05add1bc774c0 body_fp=a2f30f546de9661b128c51ed89a3ff23029c15c44f7ccd466f9e064050d834e1 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def grep_cmd( ctx: typer.Context, name: str | None = typer.Option( None, "--name", "-n", help="Substring match against the symbol's local name (case-insensitive).", ), kind: str | None = typer.Option( None, "--kind", "-k", help="Restrict to one of: function, class, method, constant, module, any.", ), scope_prefix: str | None = typer.Option( None, "--scope-prefix", help="Restrict to symbols whose file path starts with this prefix (e.g. 'trie/').", ), scope_exclude: list[str] | None = typer.Option( None, "--scope-exclude", help="File-path prefixes to skip. Repeat the flag for multiple exclusions.", ), public_only: bool = typer.Option( False, "--public-only", help="Restrict to symbols whose name doesn't start with an underscore.", ), inbound_min: int | None = typer.Option( None, "--inbound-min", help="Minimum inbound edge count (find hubs).", ), inbound_max: int | None = typer.Option( None, "--inbound-max", help="Maximum inbound edge count.", ), outbound_min: int | None = typer.Option( None, "--outbound-min", help="Minimum outbound edge count.", ), outbound_max: int | None = typer.Option( None, "--outbound-max", help="Maximum outbound edge count (find leaves with --outbound-max 0).", ), predicate_json: str | None = typer.Option( None, "--predicate", help="Full predicate as JSON; identical shape to the MCP `grep` predicate.", ), rank_by: str | None = typer.Option( None, "--rank-by", help="public_first (default) | inbound_count | alphabetical.", ), limit: int = typer.Option( 10, "--limit", "-l", help="Maximum number of hits to return.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None`

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
<!-- trie:section symbol=trie/cli:read_cmd fingerprint=658656804167b1ab001b1fae44c199006876251ce97e55828ca5821527066a70 body_fp=f058f8eb7a37b73c1111754ccd3afa60551ca7eb0dd03284183f093f5c08f744 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def read_cmd( ctx: typer.Context, path: str = typer.Argument( ..., help="Symbol qname (e.g. 'trie/sync/cascade:compute_cascade') OR a file path.", ), full: bool = typer.Option( False, "--full", help="For a file path: return every section's full prose instead of the compact view.", ), source: bool = typer.Option( False, "--source", help="Force raw line-numbered source for a FILE PATH (any file, indexed or not).", ), offset: int | None = typer.Option( None, "--offset", help="With a file path: 1-indexed first line to include (implies --source).", ), limit: int | None = typer.Option( None, "--limit", help="With a file path: maximum number of lines to return from offset (implies --source).", ), history: bool = typer.Option( False, "--history", "-H", help=( "Also show the symbol's (or file's) intent trail from the session-digest " "archive: the chronological 'why it changed' lines recorded at each commit." ), ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None`

CLI command that reads source code or trie's synthesised description — dispatches via a single `tools.read()` call.

- Accepts a symbol qname **or** a file path as the positional argument
- `--full`: for file paths, returns every section's full prose instead of the compact triefact view
- `--source` / `--offset` / `--limit`: force raw line-numbered source with optional windowing
- `--history` (`-H`): also retrieves the symbol's or file's intent trail from the session-digest archive
- Delegates rendering to `_render_read_dispatch`, which fans out to `_render_read_source`, plain output, or `_render_read` based on envelope shape
- `--json` emits the raw MCP envelope verbatim; mirrors the MCP `read` tool wire response
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_dispatch fingerprint=2259360f989712d808ec20d13c4379463c02d8176fc94e720e458dbbb7a384d9 body_fp=bb9d94c612c45960e78c9e4d5ebde58b5347bed10a4d010c42f8065d76b6b24f source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_read_dispatch(envelope: dict[str, object], reporter: Reporter) -> None`

Dispatch a `tools.read` response envelope to the correct human-readable renderer based on its shape.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_read_source fingerprint=fddcf9841287b22b0ffbf1e488f06c1ae46eacc63bd5bc0397b58066053c792b body_fp=bfcb7622d24ab6cc0afed8c392f0558284c65305b93ca94197860a2f889e97a7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_read_source(envelope: dict[str, object], reporter: Reporter) -> None`

Human-readable renderer for `read_source` tool envelope responses.

- **err**: renders error details via `_render_error_envelope` and exits early
- **lines**: prints the source content directly to console
- **more**: shows paging hint when result was truncated by offset/limit
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_cmd fingerprint=9cb63d88dbea2c7cbdd90e5991c0b5134a09f990e3bbfa46efb7174d0810140b body_fp=27155141aed854eed2404118acf00fd2ecad4fffe5eedd64ab8fdd98ce302f52 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def trace_cmd( ctx: typer.Context, qname: str = typer.Argument( ..., help="Fully-qualified symbol name to start tracing from.", ), direction: str = typer.Option( "callers", "--direction", "-d", help="callers | callees | both.", ), depth: int = typer.Option( 2, "--depth", help="Maximum BFS depth (clamped by trace_max_depth in config).", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None`

Trace call graph from a symbol outward up to specified depth, mirroring MCP `trace` tool.

- `qname`: fully-qualified symbol name to start tracing from
- `direction`: "callers", "callees", or "both" (default: "callers")
- `depth`: maximum BFS depth, clamped by config trace_max_depth (default: 2)
- `as_json`: emit raw MCP envelope as JSON instead of human-readable summary
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:blast_radius_cmd fingerprint=894cae88c8d009e068480f6da6493330bd52972377fa29f98bafe7539b4018b8 body_fp=09ceb9a7b2bff5efbcc05de248a4a5f86812a1f4abf859ae78124ece28f2f475 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def blast_radius_cmd( ctx: typer.Context, qname: str = typer.Argument( ..., help="Fully-qualified symbol name to compute the edit blast radius for.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw MCP envelope as JSON instead of a human-readable summary.", ), ) -> None`

CLI command that computes the cascade blast radius of editing a symbol using free graph traversal.

• `qname`: fully-qualified symbol name to analyze for edit impact
• `as_json`: when True, emits raw MCP envelope instead of human-readable output

Reports every symbol whose triefact/source would be regenerated if the target symbol changed, with BFS hop distances from the seed. Makes no LLM calls—pure graph mathematics for impact assessment before risky modifications.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_blast_radius fingerprint=beec4a79525cc1ed8a249725a02cdf21768f500a1f84520ed235826beb32b13e body_fp=3379880697b66b0838e779000aa58118bb714ff07ad8b12d6b684a11a030264a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_blast_radius(envelope: dict[str, object], reporter: Reporter) -> None`

Renders blast_radius tool results in human-readable format for the CLI.

- First checks for error envelope and delegates to `_render_error_envelope`
- Prints the target symbol name and file location in bold
- Shows summary line with cascade count and direct caller count
- If cascade data exists, renders a Rich table with hop distance, symbol names, and file paths
- Falls back to "nothing else depends" message when cascade is empty
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_print_plain fingerprint=4e5a2ebce1788aca6bfb58561caace523dda494204fee5186aadb85ddf260e0e body_fp=2e61a805cc53feb8e7d8fef209174f2dbbe05a01071436ac3456a273798739e4 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=util -->
## `def _print_plain(envelope: dict[str, object], reporter: Reporter) -> None`

Renders MCP tool response envelopes as human-readable text. Checks for error envelopes first and delegates to `_render_error_envelope`, otherwise formats via `render_envelope` (not raw JSON).
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_str_cmd fingerprint=ccf204ad8e903d6d88f247f32e32194d53194c152bec93aa846d64889fc83b01 body_fp=98ef4604dfa1997c1cb32b3debaf3dd863f88318b2c24c92d16f3162960c7732 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def grep_str_cmd( ctx: typer.Context, regexp: str = typer.Argument(..., help="Regex pattern to search source bodies with."), all_files: bool = typer.Option( False, "--all-files", help="Search the WHOLE repo (incl. non-indexed files), not just indexed source bodies.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

CLI command that searches source file bodies with a regex pattern and attributes hits to their enclosing symbols.

- Supports `--all-files` flag to search the entire repo instead of just indexed source files
- Calls TrieTools.grep_str_all() when --all-files is enabled, otherwise TrieTools.grep_str()
- Supports `--json` flag to emit the raw JSON envelope instead of human-readable text
- Closes the tools connection in a finally block to ensure cleanup
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:find_cmd fingerprint=d5f94e0ba784d4e22c80f0ccc4a2021ae81fd1c1c78d7f75fe60c6a9f6a08405 body_fp=10e6812dc61e2c12f944c4f82ea7f8f313cb214eb52a26361fd9104b617e6928 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def find_cmd( ctx: typer.Context, pattern: str = typer.Argument( ..., help="Glob pattern, e.g. '**/*.ts', 'Dockerfile', 'src/**/*.tsx'." ), indexed_only: bool = typer.Option( False, "--indexed-only", help="Restrict to indexed files only (default searches the whole tree).", ), limit: int = typer.Option(100, "--limit", "-l", help="Maximum number of paths to return."), ) -> None`

Searches project files by glob pattern, returning paths sorted by modification time.

• `pattern` — glob pattern like '**/*.ts' or 'Dockerfile'
• `indexed_only` — restrict to files in trie's scope (default searches whole tree)
• `limit` — maximum paths to return (default 100)
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:write_cmd fingerprint=cf4b365e8c07b479bc6f52e78297ba187d19175ffac9258ec50a745b18964006 body_fp=54d868e540357297b9e1d873b996f25bbf5e145e2d3301452b47740cf3670e06 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=api -->
## `def write_cmd( ctx: typer.Context, path: str = typer.Argument( ..., help="File path to create/overwrite, relative to the project root." ), content: str | None = typer.Option( None, "--content", "-c", help="File content. If omitted, content is read from stdin.", ), overwrite: bool = typer.Option( False, "--overwrite", help="Allow replacing an existing file.", ), ) -> None`

Implements the `trie write` CLI command to create or overwrite arbitrary files under the project root.

• **path**: File path relative to project root
• **content**: File content (reads from stdin if omitted)  
• **overwrite**: Allow replacing existing files
• Uses `TrieTools.write_file` method and renders output via `_render_write`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_write fingerprint=d176d38c585431d5800d9b9a754b58989d01a18652091e502d06dc267fbfca11 body_fp=96efdab4496dc645b14d54659b83c6ef7a1f99bc9a4ddf078d08f87791837bdd source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=util -->
## `def _render_write(envelope: dict[str, object], reporter: Reporter) -> None`

Renders a write_file envelope in human-readable form for the write command.

- Delegates error envelopes to `_render_error_envelope`
- Reports "created" or "overwrote" based on the `created` field
- Shows file path and byte count from the envelope
- Advises running sync/refresh if the file needs indexing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_find fingerprint=33aeb9572d75fb7b54cc8ba23acd8213c8a6c087e002c5264d9d8b344a2825cb body_fp=8be04406cd33fb40d31c9361ccb0b4f87501337d08e1a2d9a427d8f4dfdaddc5 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_find(envelope: dict[str, object], reporter: Reporter) -> None`

Renders human-readable output for the `find_files` MCP tool envelope.

- Prints error details if the envelope contains an error
- Lists each matched file path on a separate line
- Shows file count with truncation notice when applicable
- Reports "no files match" for empty result sets
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_entry_points_cmd fingerprint=cecda4c2cf1f3c3187effab443ead8ed4956f23ee38328f1bbe8627486f20793 body_fp=210b957b4d05d4f230c8ced4d19a479b8c36233200777ad6de6908dcef67ae32 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def grep_entry_points_cmd( ctx: typer.Context, query: str = typer.Argument(..., help="Topic or concept to match against symbol prose."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

Provides the `trie grep-entry-points` CLI command that searches for architectural entry points by topic.

- `query`: Topic or concept to match against symbol prose in entry points
- `as_json`: When true, emits the raw JSON envelope instead of formatted text
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_cmd fingerprint=be4d9c029580187b7e0b58a499d8cef731e4860c213f9c0169599d734e837f91 body_fp=f7e1d2cad3da74ed7cc6b6cf8b0b7ff17ed2067e2f1c04aebf66068b618c5374 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def grep_symbol_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

Executes fuzzy symbol name lookup via `TrieTools.grep_symbol` and renders results as plain text or raw JSON.

- Adds `--json` flag; when set, emits the raw MCP envelope instead of rendering via `_print_plain`
- Uses `_open_tools` to create a `TrieTools` session from the nearest `trie.toml`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:grep_symbol_neighbours_cmd fingerprint=6d966f04c194ea93b0e3894a320c59bfd0c1b1e3bef514f6715ec6e53d383fbe body_fp=4259a7cfc81bc2548170c9d99b919266eeb3758e6e8c12edf0a1d04d745ed9d5 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def grep_symbol_neighbours_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

Implements `trie grep-symbol-neighbours` CLI command that performs fuzzy symbol lookup and returns immediate caller/callee metadata.

- Takes a symbol name fragment to fuzzy-match against the graph
- Calls `TrieTools.grep_symbol_and_neighbours()` to get the symbol plus trimmed neighbor data
- `--json` emits the raw envelope; default renders via `_print_plain`
- Example: `trie grep-symbol-neighbours sync_single_file`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_cmd fingerprint=84e816d28b56e2962473b0f5b1b461c92580d49cf54ba185fa1c84b34bc3603a body_fp=877307f84e855f61fb2525a55f151dbe18a96170ca1b1d852a3b6713634a7f38 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def explain_symbol_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol qname or name fragment to explain."), history: bool = typer.Option( False, "--history", "-H", help="Also show the symbol's intent trail from the digest archive.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

Provide detailed explanation of a symbol including its prose and reference narrative via CLI.

CLI command that wraps the MCP `explain_symbol` tool for terminal use. Takes a symbol qname or name fragment, opens a TrieTools session, calls the explain method, and renders the result. Output is human-readable by default or raw JSON with `--json`.

- `history`: when `True`, passes the flag to `tools.explain_symbol` to include the symbol's intent trail from the digest archive.
- `as_json`: when `True`, emits the raw MCP envelope as JSON instead of formatted text.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_symbol_refs_cmd fingerprint=44a32192277efccf17b36b7444cde06e692e8e2ffd663ce1e313e2bc16b4ad8e body_fp=6da8a617b237d33086ca29670ad5349385d62e1414b9a8c9259c11927a8a3cc2 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def explain_symbol_refs_cmd( ctx: typer.Context, sym: str = typer.Argument(..., help="Symbol qname or name fragment."), history: bool = typer.Option( False, "--history", "-H", help="Also show the symbol's intent trail from the digest archive.", ), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

Typer command that explains how a symbol is used by its callers with their prose.

- Accepts `--history`/`-H` to also include the symbol's intent trail from the digest archive
- Accepts `--json` to emit the raw JSON envelope instead of human-readable output
- Calls `TrieTools.explain_symbol_references()` with the symbol name/fragment and `history` flag
- Uses generic `_print_plain` renderer for human-readable output
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:trace_flow_cmd fingerprint=30878fb0764545ed3b2c4e41e5bef393d2649e1443fcbe7c3c19581bf4336c6f body_fp=36cbc3db0ba478f533ab4e82887d140e33cd7068a7c100157fe3035027e52d96 source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def trace_flow_cmd( ctx: typer.Context, symbol1: str = typer.Argument(..., help="Starting symbol qname or name."), symbol2: str = typer.Argument(..., help="Target symbol qname or name."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

CLI command that finds call chains between two symbols via `TrieTools.trace_flow`.

- **symbol1**: starting symbol qualified name or name fragment
- **symbol2**: target symbol qualified name or name fragment
- **as_json**: when true, emits the raw JSON envelope instead of formatted text
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:explain_flow_cmd fingerprint=b936810b259a14ce3067b76bd914d11c5d86110d9bdc6f06614e850340d0f38e body_fp=6f0bbf1877fd9dded7a03ac7406e9b924931f5697e12b0aa8614b0985dc2cc2b source_ref=3de8744a020137e033218bf1ca5978eb1977cfe2 role=api -->
## `def explain_flow_cmd( ctx: typer.Context, symbol1: str = typer.Argument(..., help="Starting symbol qname or name."), symbol2: str = typer.Argument(..., help="Target symbol qname or name."), as_json: bool = typer.Option( False, "--json", help="Emit the raw JSON envelope instead of formatted text." ), ) -> None`

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
<!-- trie:section symbol=trie/cli:_RichApplyProgress fingerprint=88a444531b547feca55d4fda3ad1c55db173b88633bd149775faf38391c33b66 body_fp=479a2e5b1e3c4284b00ffc3279291a5f64778849c2274b984a9f976bd0a81813 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `class _RichApplyProgress`

Rich-formatted progress reporter for apply_patches operations. Prints structured, thread-safe progress output with visual indicators for each stage.

- Methods called from worker threads, so output naturally interleaves
- verbose flag controls symbol-level detail display
- Uses Rich markup for colored icons and indented hierarchy
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.__init__ fingerprint=1c6ad7264d460fcc4f36e9524e2f5bc1f7ee6bc638d01590eca5e0f665ce4ae7 body_fp=e152dc6e3edba768a30f7d1166da2953737764c14e6838ddaab702c4119120ee source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def __init__(self, console: Console, *, verbose: bool = False)`

Initializes _RichApplyProgress with a Rich console and optional verbose flag for detailed patch application reporting.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.stage fingerprint=00a0e5b25af2600c917827df1316312556da14518c19c948a17c6b4f8105174f body_fp=ee0a33a1014fd3e79fda478f2889b29c5dbfd606da06f0f89d72edf6dfbe1883 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def stage(self, msg: str) -> None`

Prints a stage header message with rich formatting to the console.

- Formats the message with bold cyan styling and a vertical bar prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_start fingerprint=1c9e2af52741b8ee459d4101628f36bc16552d1d167b3afdfa1cb25db55ae2d3 body_fp=45b479edc3aacde9dd65f01f09a65ae9083fc04cff96afcfb547613110fd2a65 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_start(self, fp: str, symbols: int) -> None`

Prints a file processing start message with file path and symbol count.

- `fp`: relative file path being processed
- `symbols`: number of symbols in the file that will be patched
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_symbol fingerprint=1fc9ef71af9d3e0f90361d13907c1059d449a1913c2acbac2a945251d0e7c24d body_fp=812507ac4a41abab8a201c71d4ebf7bb6ab1c52170e218c33d9fa56880c2d541 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_symbol(self, qn: str, notes: list[str]) -> None`

Prints per-symbol progress during patch application when verbose mode is enabled.

- `qn`: qualified name displayed in cyan with indented bullet point
- `notes`: patch notes truncated to 100 chars and printed with "note:" prefix
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_generate fingerprint=132b41245a185b2af3aacb3c8c3a18c12c5b09ff296437cde359f630862c6105 body_fp=75aab617f78490a42dfa9ddee8beef9e19d108415185cc719c09e0c1b5cd9a70 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_generate(self) -> None`

Prints generation progress for `_RichApplyProgress` when verbose mode is enabled.

- Only executes when `self.verbose` is `True`
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_fixup fingerprint=26be5de5ef710ac328e60f9b6eea26539ebdc8ecf0c1fd70a4eb97604c07d115 body_fp=f99c218663d2dc183604aeb8d0cf2ca6996b42f6f2ef817b790d10a8e3456de7 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_fixup(self, iteration: int, count: int) -> None`

Prints a yellow gear icon with LSP fixup iteration number and diagnostic count.

- **iteration**: Zero-based fixup pass number
- **count**: Number of diagnostics found in this iteration
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_prose fingerprint=12b3c9eda87bd14def97bc9c6c65327a7d23a45803d936cae5ab3330703ecb93 body_fp=d037ead1a93e52c050841afa44cb3357089bd63c05c207e97710943c1ab723ed source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_prose(self, qn: str) -> None`

Prints a verbose prose generation indicator for the given symbol qname.

- Only prints when `verbose=True` was set during `_RichApplyProgress` construction
- Displays an indented line with a pen icon and the qname being processed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.file_done fingerprint=be1e14003b12fc05817ca35f7302feae8c628647d0b7cffb7cef9fef388f8c11 body_fp=a99726fc1011833bdb74808d64f4f165931489fbd5e8b339be19e447fb93713b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def file_done(self, fp: str, ok: bool, error: str | None = None) -> None`

Prints a completion status line for a file in `_RichApplyProgress` patch application progress.

- `ok`: determines green checkmark (success) vs red X (failure) icon
- `error`: failure message displayed in red when `ok` is False
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.refresh fingerprint=fa057109cbf67e48f2ca72e4736ffb716951fd64ecb1ac03f8c0afce10bfb4e2 body_fp=82c52deb3669a4e19b803b7a0b089291610f3a90e5bd065321af88007f83901c source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def refresh(self, fp: str) -> None`

Prints a refresh indicator for the given file path during patch apply progress reporting.

- `fp`: File path being refreshed
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_RichApplyProgress.verify fingerprint=9bb6073c0083b530e9d8a61ec3fe90bde21961bdcbb397e39268aa6d65db357c body_fp=35e854aa25061bd05a1426cc384d01078854973f9d9f3fa84cb10e7382f7d96a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def verify(self) -> None`

Prints a green checkmark indicating the project is consistent after patch application. Called by `apply_patches` at the end of its verification phase.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_close_qname_suggestions fingerprint=43648b44ebab8b775cf26778257e39e5a8f42ddf9248eeca7bce65d59d125f23 body_fp=d9056e347794c4efa484725656077d043f064a1ac317c9c653786795d3baa8cf source_ref=f803cb599a03936d496cac84820bfd4e78a600a2 role=util -->
## `def _close_qname_suggestions(store: Store, qname: str, *, n: int = 3) -> list[str]`

Fuzzy-match `qname` against all graph-known qualified names via `_close_qname_matches` (same-module symbols ranked first) and return up to `n` suggestions; returns `[]` on any failure.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_cmd fingerprint=6ef2bbed6b313b75ffe7e40afe0e61a93b665e1c52a71dab6e77f1bc14adcfc7 body_fp=51ed3b9803e7d9cbfdc38c95240bf7069b95fd93dcb976a420411551643be3ef source_ref=1d35cd8f3622458a5b735a6b27aed37679e0201a role=api -->
## `def patch_create_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to patch."), note: str = typer.Option(..., "--note", "-n", help="Implementation change note."), reason: str = typer.Option( "", "--reason", "-r", help="Why the cascade needs to know about this change." ), gone: bool = typer.Option( False, "--gone", help=( "The symbol was REMOVED (no longer in the graph): record the note " "straight to the session log as a delete instead of queueing a patch. " "This is how removals satisfy the `trie intent` gate." ), ), ) -> None`

Creates a fire-and-forget edit patch against a symbol in the trie graph store.

- `--gone`: records the note via `store.add_patch(..., kind="delete", require_symbol=False)` instead of an FK-constrained insert — routes through the store (not the pending-intent file)
- On `KeyError`, calls `_close_qname_suggestions` for fuzzy did-you-mean hints; suggestions and the follow-up hint are printed to `reporter.err_console` (stderr) so subprocess wrappers see them on failure
- Validates that the symbol exists in the graph database before creating the patch (non-`--gone` path)
- Uses a stable CLI session ID for tracking related patches together
- Returns the patch ID after successful creation on both paths
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_batch_cmd fingerprint=bd311badd034a507c09be8adb49b1401c0ff08b46f8799aa9cb6eeb37f768ab8 body_fp=1abebeec03ad8ff5dd8c5bed8dc45c17a4542ee88e24f7f258b40fa5ab0981d1 source_ref=1d35cd8f3622458a5b735a6b27aed37679e0201a role=api -->
## `def patch_create_batch_cmd( ctx: typer.Context, json_file: str = typer.Option( "", "--json-file", help="Path to a JSON file with the patch array (else read stdin)." ), ) -> None`

Stage multiple `patch` or `create` operations in one call, reading a JSON array from `--json-file` or stdin.

- `op`: `"patch"` (default) modifies an existing symbol; `"create"` stages a new symbol — if the symbol already exists, silently falls back to `"patch"` and sets `"fell_back": true` in the result entry.
- On `KeyError` (symbol not found), the failure result row includes a `"did_you_mean"` list of close qname matches when any are found.
- Items are processed independently; failures are reported without aborting remaining items.
- Emits `{"staged": N, "failed": N, "results": [...]}` as JSON to stdout.
- Exits 1 if zero items were staged successfully.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_create_symbol_cmd fingerprint=e0385e93e61bcffe98beb1c7409c19582424e8afc7a4de84d89f1b2a742806c2 body_fp=6d3464327948642a9f89dabad308325cf1f329f91459375063c8ada41a24c74b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_create_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Intended qualified name, e.g. 'pkg/mod:new_fn'."), note: str = typer.Option(..., "--note", "-n", help="What the new symbol should do."), file: str = typer.Option( "", "--file", "-f", help="Target source file (derived from qname when omitted)." ), anchor: str = typer.Option( "", "--anchor", "-a", help="Place the new symbol after this existing qname." ), reason: str = typer.Option("", "--reason", "-r", help="Why this symbol is needed."), ) -> None`

Stage creation of a new symbol to be applied by `trie patch apply`.

- **qname**: intended qualified name like `pkg/mod:new_fn`
- **note**: what the new symbol should do (required)
- **file**: target source file; when omitted, resolved via `registry.resolve_create_target` (existing module wins, else language-inferred suffix)
- **anchor**: place the symbol after this existing qname
- **reason**: why the symbol is needed
- If qname already exists in the graph, falls back to `Store.add_patch` instead of erroring
- Stores create patch via `Store.add_create_patch` with session tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_delete_symbol_cmd fingerprint=d42b44a08aab95225aa29d2ef76a46ff4a907a793fda7b7ba45a30e5335c6d39 body_fp=98320aa339bcce3e7ccbe5dc1709e4c779059fb903e2675968f154c6e09cadef source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_delete_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to delete."), reason: str = typer.Option("", "--reason", "-r", help="Why it's being removed."), ) -> None`

Command handler for `trie patch delete-symbol` that stages deletion of an existing symbol.

- Creates a delete patch against the symbol via `Store.add_delete_patch`
- Warns when the symbol has dependents that will reference a deleted symbol
- Raises `typer.Exit(1)` if the symbol is not found in the graph store
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_rename_symbol_cmd fingerprint=a2a8cc1e28f4751332966ccd372069f40de13ebbcbc3d5294d7e2cb0d4939183 body_fp=4cf1879831fc94891837dcde14ca2b7e949db213a9171f2d5f4f9ae6ccc6098b source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_rename_symbol_cmd( ctx: typer.Context, qname: str = typer.Argument(..., help="Qualified name of the symbol to rename."), new_name: str = typer.Argument(..., help="New local name (not a qualified name)."), reason: str = typer.Option("", "--reason", "-r", help="Why it's being renamed."), ) -> None`

Stage a rename of an existing symbol for later application by `trie patch apply`.

- Validates the new name is a valid Python identifier
- Creates a rename patch in the graph database with optional reason
- Reports the number of existing references that will need updating
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_apply_cmd fingerprint=5f4eda920305e3f49d4bdc0ce8cabd318f66cefe003c63997bc88e66d9ae1e84 body_fp=4e3b7c13db182a6d0dc0b0b4260ed1ee0169156a7075c4b20b2a8cca4fbfee3f source_ref=a926c793af5e1f338acdc176a5faae767217b646 role=api -->
## `def patch_apply_cmd( ctx: typer.Context, note: str = typer.Option( "", "--note", "-N", help="Session note: the unifying intent (required for multi-symbol applies).", ), json_output: bool = typer.Option( False, "--json", help="Emit raw JSON output (useful for agent consumers).", ), ) -> None`

Archive pending patch notes as intent via `record_intent` — always the `record` path, no code generation.

- `--note`: session-level unifying intent for the apply run.
- `--json`: dumps raw envelope to stdout and exits 1 if `ok` is falsy; non-JSON path exits 1 on failure or prints a per-symbol success list.
- After success, reads `envelope["uncovered"]`: warns with up to 5 symbols still lacking notes (would fail the commit gate), or reports full coverage when the key is present but empty.
- Removed: `--model`, `--backend`, `--commit-mode` options and all `agent`/`llm` backend dispatch paths.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_preview_cmd fingerprint=bb43bb71a6141343c63226fcf7e8bf42a7bb400eedccecc762509629daa934f7 body_fp=08bed3e31018952ed7bee921c0c8a25bc7759c9cdca939d35d9e1a6ac2509205 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_preview_cmd(ctx: typer.Context) -> None`

Previews what `trie patch apply` would execute without running it.

- Displays a Rich table with separate rows for patched symbols, create-symbol patches, and cascade neighbours
- Shows an "Origin" column distinguishing patch types rather than cascade indicators
- Reports zero patches with an info message if no patches or creates are pending
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_list_cmd fingerprint=8d8b6d21fbaecc39a83d4d22192f73d2d93ceb086194fcebedc17a8f0943f357 body_fp=8b0ae61aa34def2669ee09c3b88478ec10241868f04b03e8c9fe04ac69c50c7a source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_list_cmd(ctx: typer.Context) -> None`

List all pending patches and create-symbol patches in separate tables.

Opens the graph store, retrieves symbols with pending modification patches and staged symbol creations, then displays them in two Rich tables: "Pending Patches" shows qualified names with patch counts, and "Pending Creates" shows new symbol names with target files. Exits with no output if neither patch type exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:patch_drop_cmd fingerprint=b456b5f77094c686bfb31765795cabfab769c5ad30c8de1e19416ea722b8f2be body_fp=0ad5100d25a9aa1f827320b9dc977cbb80407664568e88238e56c934aa48b5b6 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def patch_drop_cmd( ctx: typer.Context, qname: str | None = typer.Option( None, "--qname", "-q", help="Drop patches for a specific symbol." ), session_id: str | None = typer.Option( None, "--session", "-s", help="Drop patches for a specific session." ), all: bool = typer.Option(False, "--all", "-a", help="Drop all patches."), ) -> None`

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
<!-- trie:section symbol=trie/cli:mcp_serve fingerprint=cd3c1e0935ce39624688d3d14d5849759c65f9d7765068ccd8ef4ca118b44211 body_fp=2ec9b162c002735c4116bf8d8748b628e31ee4b498df3e24585ea8e161fcc221 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def mcp_serve() -> None`

Run the trie MCP server over stdio as a Typer command.

Delegates to `_run_mcp_serve()` for the actual server implementation.
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_run_mcp_serve fingerprint=ae7533faa0329509290b89496e7a1965bcac67339cfb61c9d2092872d3505fb6 body_fp=e3ddb2cc9bd1b559d9215bb2adf061ee4572c69c50ff0c54956ec59d551523a7 source_ref=b1cd8673daa7f27bf82a8377747312a95d250581 role=io -->
## `def _run_mcp_serve() -> None`

Starts the MCP server over stdio after validating the project configuration.

- Locates trie.toml and validates config structure without using its contents
- Prints config errors to stderr to avoid corrupting the MCP protocol stream
- Delegates to run_mcp_stdio for actual server implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_install_cmd fingerprint=2b0ec965d048ca70c51eb306977f7e7c8fd3f2b163fb3ede828618f3a9f3921c body_fp=fe71491280ac0c68824b32a8f37a3d907278b9fbc23230135bd56bb150033ebd source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def mcp_install_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, "--target", "-t", help=( "Install for a specific agent. Repeat the flag for multiple targets. " f"Known: {', '.join(MCP_TARGETS)}." ), ), install_all: bool = typer.Option( False, "--all", help="Install for every known target. Skips per-target detection.", ), scope: str = typer.Option( "project", "--scope", help="Install scope: 'project' (writes into the current project) or 'user' (~/.<agent>/...).", case_sensitive=False, ), print_only: bool = typer.Option( False, "--print-only", help="Print the snippet that would be merged, don't write any files.", ), dry_run: bool = typer.Option( False, "--dry-run", help="Show what would change without writing. Implies the file path resolution but no edit.", ), ) -> None`

Registers trie MCP server with one or more coding agents through their config files.

- `target`: specific agent names to install for (can be repeated)
- `install_all`: install for all known agents, skipping detection
- `scope`: "project" writes to current repo, "user" writes to ~/.<agent>/
- `print_only`: shows config snippet without writing files
- `dry_run`: shows file paths and changes without writing
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_install_plan fingerprint=2d4ce0c3e41a692373e64cecba4106fb75fc68999e018cf45d367c48ad981e95 body_fp=e93049e926ed0094b687c5099b6599c2b315fa41b95f589aacc1fc5b2fd50d04 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_install_plan(reporter: Reporter, plan: InstallPlan) -> None`

Renders human-readable output for MCP installation results, displaying per-target status and details.

- Formats each result with the target's display name and appropriate colored status indicators
- Shows JSON snippets for preview actions and error messages for failed operations
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:mcp_uninstall_cmd fingerprint=e0cbf3e2e0174b8f33dbe0589e2c6908d67e5f5c49961500186aab26268bab2a body_fp=346f5d90b59603f3bb8df5685ff649c44c2988c234ea9034f47fe7617f741421 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=api -->
## `def mcp_uninstall_cmd( ctx: typer.Context, target: list[str] | None = typer.Option( None, "--target", "-t", help=( "Uninstall from a specific agent. Repeat the flag for multiple targets. " f"Known: {', '.join(MCP_TARGETS)}." ), ), uninstall_all: bool = typer.Option( False, "--all", help="Uninstall from every known target. Skips per-target detection.", ), scope: str = typer.Option( "project", "--scope", help="Uninstall scope: 'project' (the current project's config files) or 'user' (~/.<agent>/...).", case_sensitive=False, ), print_only: bool = typer.Option( False, "--print-only", help="Print what would be removed without writing any files.", ), dry_run: bool = typer.Option( False, "--dry-run", help="Show what would change without writing.", ), ) -> None`

Unregisters the trie MCP server from agent configuration files.

• Validates mutually exclusive flags and scope options
• Delegates uninstall execution to `mcp_run_uninstall` with validated parameters
• Renders the uninstall plan showing removed entries per target
• Exits with code 1 if any uninstall operation encounters errors
<!-- trie:end -->
<!-- trie:section symbol=trie/cli:_render_uninstall_plan fingerprint=982bba634aca721cfd1aaf145aba973af33cbd7f5cb22ab4f82d6c4f8ba7a692 body_fp=18d7c721652cc712efa08de06b717a3ded8dcff3575170c5095066966bd0f605 source_ref=ec65582312b341065f0f0bb2b57d76d2fbe38026 role=util -->
## `def _render_uninstall_plan(reporter: Reporter, plan: UninstallPlan) -> None`

Renders the output for `trie mcp uninstall` by iterating through uninstall plan results and printing status messages for each target using the Reporter console interface.

- Mirrors the install renderer with `removed` status replacing `created`/`updated`
- Prints JSON preview for dry-run mode, success/error messages for actual operations
- Shows skipped targets with explanatory detail when no action was needed
<!-- trie:end -->