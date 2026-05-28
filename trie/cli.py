from __future__ import annotations

import sys
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from pathlib import Path

import typer
from rich.console import Console

from trie import __version__, telemetry
from trie.audit import AuditSummary
from trie.audit import render as render_audit
from trie.audit import render_comparison as render_audit_comparison
from trie.check import StaleReason, check_project
from trie.config import Config, ConfigNotFoundError
from trie.cost import get_pricing
from trie.diff_cmd import diff_project
from trie.docs_install import (
    DocsInstallError,
    DocsInstallPlan,
)
from trie.docs_install import (
    install as docs_run_install,
)
from trie.edits.apply import apply_patches, preview_patches
from trie.freshness import (
    FreshnessResult,
    NotAGitRepoError,
    ensure_fresh_after_turn,
    ensure_fresh_before_turn,
)
from trie.graph.store import Store
from trie.hook_install import (
    HookInstallError,
    HookInstallPlan,
)
from trie.hook_install import (
    install as hook_run_install,
)
from trie.init import InitError, init_project
from trie.mcp_install import TARGETS as MCP_TARGETS
from trie.mcp_install import InstallPlan, MCPInstallError, UninstallPlan
from trie.mcp_install import install as mcp_run_install
from trie.mcp_install import uninstall as mcp_run_uninstall
from trie.mcp_server import TrieTools
from trie.mcp_server import run_stdio as run_mcp_stdio
from trie.models import make_client
from trie.refresh_lock import try_acquire as try_acquire_refresh_lock
from trie.reporter import ProgressHandle, Reporter, Verbosity
from trie.scan import scan_project
from trie.scope import discover_files
from trie.sync.bootstrap import BootstrapPlan, build_plan, run_bootstrap
from trie.sync.incremental import (
    IncrementalWorklist,
    compute_incremental_worklist,
    run_incremental,
)
from trie.sync.progress import ProgressCallback
from trie.sync.single_file import (
    FileSyncResult,
    refresh_triefact_metadata,
    sync_single_file,
)
from trie.tool_override_install import (
    ToolOverrideInstallError,
    ToolOverrideInstallPlan,
)
from trie.tool_override_install import (
    install as tool_override_run_install,
)

app = typer.Typer(
    name="trie",
    help="Artefact tree that mirrors your source tree, kept coherent by an LSP-aware cascade.",
)
console = Console()


def _get_reporter(ctx: typer.Context) -> Reporter:
    """Resolve the Reporter set up by the root callback. Subcommands invoked outside
    the normal Typer dispatch (e.g. some tests) get a default MEDIUM reporter."""
    obj = getattr(ctx, "obj", None)
    if isinstance(obj, Reporter):
        return obj
    return Reporter()


class _ProgressAdapter:
    """Bridge from sync's ProgressCallback Protocol to a Reporter ProgressHandle.

    Lazily creates the underlying ProgressHandle on the first `on_start` call so
    callers don't need to know the total upfront — the sync internals report it
    along with the per-file index.
    """

    def __init__(self, reporter: Reporter, label: str):
        self.reporter = reporter
        self.label = label
        self.handle: ProgressHandle | None = None
        self._prev_running_cost = 0.0

    def _ensure(self, total: int) -> ProgressHandle:
        if self.handle is None:
            self.handle = self.reporter.start_progress(total=total, label=self.label)
            self.handle.__enter__()
        return self.handle

    def close(self) -> None:
        if self.handle is not None:
            self.handle.__exit__(None, None, None)
            self.handle = None

    def on_start(self, rel_path: str, idx: int, total: int) -> None:
        self._ensure(total).start_file(rel_path)

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None:
        per_file_cost = running_cost_usd - self._prev_running_cost
        self._prev_running_cost = running_cost_usd
        if self.handle is None:
            return
        self.handle.finish_file(
            rel_path,
            cost_usd=per_file_cost if per_file_cost > 0 else None,
            symbols=result.symbols_generated,
            tokens_in=result.input_tokens,
            tokens_out=result.output_tokens,
            cache_read=result.cache_read_input_tokens,
            cache_write=result.cache_creation_input_tokens,
        )

    def on_skip(self, rel_path: str, reason: str) -> None:
        if self.handle is not None:
            self.handle.skip_file(rel_path, reason)


@contextmanager
def _progress_callback(reporter: Reporter, label: str) -> Iterator[ProgressCallback]:
    adapter = _ProgressAdapter(reporter, label)
    try:
        yield adapter
    finally:
        adapter.close()


@contextmanager
def _acquire_write_lock_or_exit(
    project_root: Path, reporter: Reporter, command_name: str
) -> Iterator[None]:
    """Hold the refresh lock for the duration of a write-side command, or exit
    with a clear message if another process already holds it.

    The lock is shared with the hook-driven `trie refresh` and with any other
    write-side trie command in the same checkout. The hook's refresh path
    quietly queues itself when contended because the agent harness wants
    no-op-on-conflict semantics; operator-typed commands deserve the opposite
    — a loud failure with a non-zero exit so the operator knows their work
    didn't happen and can retry once the contending process finishes.

    Exit code 2 is reserved for this case so scripts can distinguish "you
    raced another trie process" (transient, retry) from exit 1 ("your config
    is broken" — non-transient, fix-the-input).
    """
    with try_acquire_refresh_lock(project_root) as holder:
        if not holder.acquired:
            telemetry.emit(
                "refresh_lock_contended",
                project_root=str(project_root),
                command=command_name,
                action="rejected",
            )
            reporter.error(
                f"another trie process is writing to this project "
                f"({project_root}); `trie {command_name}` would race the graph "
                "store. Wait for it to finish and retry."
            )
            raise typer.Exit(code=2)
        yield


@app.callback(invoke_without_command=True)
def _root(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", help="Show trie version and exit."),
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help="Mute mode: print errors only.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Verbose mode: include per-symbol detail and token breakdowns.",
    ),
) -> None:
    if quiet and verbose:
        typer.echo("error: --quiet and --verbose are mutually exclusive", err=True)
        raise typer.Exit(code=2)

    if quiet:
        level = Verbosity.MUTE
    elif verbose:
        level = Verbosity.VERBOSE
    else:
        level = Verbosity.MEDIUM
    ctx.obj = Reporter(verbosity=level, console=console)

    if version:
        typer.echo(f"trie {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    # Telemetry: record the command invocation. Config-driven enable lives
    # behind a successful Config.find_and_load below; the env var TRIE_DEBUG
    # works without a config thanks to the lazy resolver in trie.telemetry.
    _telemetry_bootstrap(ctx.invoked_subcommand, sys.argv[1:])


def _telemetry_bootstrap(subcommand: str | None, argv_tail: list[str]) -> None:
    """Apply [debug] config (if a trie.toml exists) and emit the `cli` event.

    Failure to find a config is fine — `trie init` runs before there is one,
    and the env var is enough to enable telemetry in that case. We swallow
    every error quietly; telemetry is best-effort and never blocks a command.
    """
    try:
        cfg, root = Config.find_and_load(Path.cwd())
        telemetry.configure(cfg.debug, root)
    except (ConfigNotFoundError, Exception):
        pass
    telemetry.emit("cli", subcommand=subcommand or "(none)", argv=argv_tail)


@app.command("init")
def init_cmd(
    ctx: typer.Context,
    root: Path = typer.Argument(
        Path.cwd(),
        help="Project root to initialise. Defaults to the current directory.",
        show_default=False,
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite trie.toml if it exists, and skip Python-project detection.",
    ),
    install_hooks: bool | None = typer.Option(
        None,
        "--install-hooks/--no-install-hooks",
        help="Install a pre-commit hook that runs `trie verify`. Prompts when omitted in a tty.",
    ),
    run_scan: bool = typer.Option(
        True,
        "--scan/--no-scan",
        help="Build the symbol graph immediately after writing trie.toml.",
    ),
) -> None:
    """Create trie.toml, update .gitignore, build the symbol graph, and (optionally)
    install a pre-commit hook."""
    reporter = _get_reporter(ctx)

    if install_hooks is None:
        # Tri-state default: prompt in a tty, else skip (so CI runs are non-interactive).
        if _is_interactive():
            install_hooks = typer.confirm(
                "Install a pre-commit hook to refuse commits when triefacts drift?",
                default=True,
            )
        else:
            install_hooks = False

    # `init` materialises `.trie/graph.db` when `--scan` is set. Guard with
    # the lock so two concurrent inits (rare, but possible if a setup script
    # races a hook on an already-set-up checkout) don't corrupt the store.
    # `try_acquire` creates `.trie/` if it doesn't exist yet.
    with _acquire_write_lock_or_exit(root, reporter, "init"):
        try:
            with reporter.status("scanning project…") if run_scan else _NoOpStatus():
                result = init_project(
                    root,
                    force=force,
                    install_hooks=install_hooks,
                    run_scan=run_scan,
                )
        except InitError as exc:
            reporter.error(str(exc))
            raise typer.Exit(code=1) from exc

    reporter.success(f"wrote {result.project_root / 'trie.toml'}")
    detected = ", ".join(result.detected_markers)
    reporter.info(f"  detected: {detected}")
    if result.gitignore_updated:
        reporter.success(f"updated {result.project_root / '.gitignore'} (added .trie/)")
    else:
        reporter.info("  .gitignore already had .trie/ — skipped")

    if result.scan_ran:
        reporter.success(
            f"scanned {result.scan_files_total} files · {result.scan_symbols_total} symbols"
        )

    if install_hooks:
        if result.pre_commit_strategy == "git_hook" and result.pre_commit_installed:
            reporter.success(f"installed pre-commit hook at {result.pre_commit_path}")
        elif result.pre_commit_strategy == "git_hook":
            reporter.info("  pre-commit hook already present — skipped")
        elif result.pre_commit_strategy == "framework":
            reporter.info(
                "  detected .pre-commit-config.yaml — add this hook entry yourself:\n"
                "    - repo: https://github.com/pankajgarkoti/trie\n"
                "      rev: main\n"
                "      hooks:\n"
                "        - id: trie-verify"
            )
        elif result.pre_commit_strategy == "none":
            reporter.warn("not a git repository — skipped pre-commit hook install")

    reporter.info("")
    reporter.info("Next steps:")
    reporter.info(
        "  [cyan]trie setup[/cyan]    wire trie into your coding agent "
        "(MCP server, turn-boundary hook, agent docs)"
    )
    reporter.info("  [cyan]trie plan[/cyan]     preview the worklist + estimated cost (free)")
    reporter.info("  [cyan]trie sync[/cyan]     generate triefacts")
    reporter.info("  [cyan]trie verify[/cyan]   check drift (also runs as pre-commit hook)")

    # Offer to run `trie setup` right now so the user doesn't have to know
    # the next-step incantation. Skip the prompt in non-TTY environments
    # (CI, scripted init) so unattended invocations stay deterministic —
    # users in CI explicitly run `trie setup` themselves. The setup default
    # is "yes" since the only reason to run `trie init` in an interactive
    # session is usually to set up the project end-to-end; making the user
    # type Enter to continue down the happy path is friction we can spare.
    if _is_interactive() and typer.confirm(
        "Run `trie setup` now to wire trie into your coding agent?",
        default=True,
    ):
        reporter.info("")
        reporter.info("[bold cyan]Running `trie setup`…[/bold cyan]")
        # Defer target selection and every other knob to setup itself —
        # init's job is just to trigger it. setup uses its own defaults
        # (auto-detect target via MCPTarget.detect, project scope, tool
        # overrides on). If setup raises typer.Exit, the error already
        # reached the user; we let it propagate so init's exit code
        # reflects the actual outcome.
        setup_cmd(
            ctx,
            target=None,
            install_all=False,
            scope="project",
            print_only=False,
            dry_run=False,
            no_overrides=False,
        )


def _is_interactive() -> bool:
    """True when stdin is a tty (so we can safely prompt)."""
    import sys

    try:
        return sys.stdin.isatty()
    except (AttributeError, ValueError):
        return False


class _NoOpStatus:
    def __enter__(self) -> _NoOpStatus:
        return self

    def __exit__(self, *exc: object) -> None:
        return None


@app.command("plan")
def plan_cmd(
    ctx: typer.Context,
    model: str | None = typer.Option(
        None, "--model", help="Override the configured model for cost estimation."
    ),
    all_: bool = typer.Option(
        False,
        "--all",
        help=(
            "Show the cost of regenerating every in-scope file (full re-bootstrap), "
            "not just the incremental worklist. Default on a fresh project; opt-in on "
            "an established one."
        ),
    ),
) -> None:
    """Scan the project, surface drift, and show the worklist + estimated cost.

    Networked but cheap: uses Anthropic's free `count_tokens` endpoint per file, never
    `messages.create`. Run before `trie sync` if you want to see the bill before paying it.

    Auto-detects the right mode:
      • No triefacts yet → full bootstrap plan (every in-scope file).
      • Triefacts exist  → incremental plan: only what `trie sync` would actually touch
                           (directly stale files + their cascade), plus any orphan triefacts
                           that would be removed.
      • --all            → force the full re-bootstrap view on an established project.

    Step 1 is an offline drift check (same as `trie verify`). Drift is reported as a
    warning but does not abort — `plan` is informational, not a gate.
    """
    reporter = _get_reporter(ctx)
    _verify_drift(reporter, exit_on_drift=False)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"
    triefacts_root = project_root / config.triefacts.root
    use_incremental = not all_ and _has_existing_triefacts(triefacts_root)

    # `plan` runs `scan_project` on the full-bootstrap branch, which writes
    # to the graph store. Even on the incremental branch it locks reads to a
    # consistent snapshot of the SQLite database. Guard the whole command.
    with (
        _acquire_write_lock_or_exit(project_root, reporter, "plan"),
        Store(db_path) as store,
    ):
        if use_incremental:
            with reporter.status("computing incremental worklist…"):
                worklist = compute_incremental_worklist(
                    project_root=project_root, config=config, store=store
                )
            if not worklist.affected_files:
                if worklist.orphan_triefacts:
                    reporter.success(
                        f"no LLM work needed — {len(worklist.orphan_triefacts)} orphan "
                        "triefact(s) would be removed by `trie sync`"
                    )
                else:
                    reporter.success("triefact tree is coherent — `trie sync` would be a no-op")
                return
            # Per-file regen counts let the cost estimate reflect symbol-level
            # reality. A file present in `regen_qnames_by_file` will only regen the
            # listed qnames; a file absent (e.g. MISSING_TRIEFACT cold-write) regens
            # everything. `build_plan` interprets the map the same way.
            regen_counts = {f: len(qns) for f, qns in worklist.regen_qnames_by_file.items()}
            with reporter.status("counting tokens…"):
                plan = build_plan(
                    project_root=project_root,
                    store=store,
                    model_id=model_id,
                    client=client,
                    only_files=worklist.affected_files,
                    regen_count_by_file=regen_counts,
                )
            _print_incremental_plan(reporter, plan, worklist, model_id)
            return

        # Full-bootstrap path: fresh project, or `--all` on an established one.
        with reporter.status("scanning project…"):
            scan_result = scan_project(project_root=project_root, config=config, store=store)
        _print_scan_breakdown(reporter, scan_result, db_path, project_root)
        with reporter.status("counting tokens…"):
            plan = build_plan(
                project_root=project_root, store=store, model_id=model_id, client=client
            )

        if not plan.items:
            reporter.warn("no files in scope")
            return
        if all_ and _has_existing_triefacts(triefacts_root):
            reporter.info(
                "  [dim](showing full re-bootstrap cost; drop --all for incremental)[/dim]"
            )
        _print_plan(reporter, plan, model_id)


@app.command("verify")
def verify_cmd(ctx: typer.Context) -> None:
    """Offline drift check. Exits 1 if any triefact has drifted from its source.

    Bidirectional: catches both Code → Triefact drift (source changed but section
    wasn't regenerated, or a public symbol has no section) and Triefact → Code drift
    (section body was tampered with, or section refers to a deleted symbol).

    No LLM, no scan, no DB writes — designed for pre-commit hooks. The same drift
    detection runs as the first step of `trie plan` and `trie sync`; `verify` exists
    so CI / hooks can fail loudly when the tree drifts.
    """
    reporter = _get_reporter(ctx)
    _verify_drift(reporter, exit_on_drift=True)


@app.command("lock-check")
def lock_check_cmd(ctx: typer.Context) -> None:
    """Probe whether another trie process holds the project's write lock.

    Designed for the pre-commit hook: if a `trie refresh` or `trie sync` is
    mid-flight, committing would race the triefact tree the commit is trying
    to capture. We refuse the commit in that case so the user retries once
    the writer finishes.

    Exit codes mirror the rest of the lock-aware CLI surface:

      0 — lock is free (or this project isn't configured for trie at all,
          which means there is no trie state to race).
      2 — lock is held by another process; the caller (typically a git
          pre-commit hook) should refuse to proceed and prompt a retry.

    The probe is acquire-then-immediately-release; it never queues, blocks,
    or interferes with the holder's work. No `.trie/` files are created if
    the project isn't yet initialised — a fresh checkout simply reports free.
    """
    reporter = _get_reporter(ctx)

    # If trie isn't configured here, there's no shared state to race; report
    # free and exit 0. The pre-commit hook stays a no-op rather than throwing
    # confusing errors at users who haven't set trie up in this repo.
    try:
        _, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError:
        reporter.success("lock-check: no trie.toml — nothing to lock")
        return

    # `.trie/` may not exist yet on a fresh checkout. In that case the lock
    # file path is materialisable but unmaterialised; acquire creates `.trie/`
    # transparently and immediately releases — a stray `refresh.lock` anchor
    # file is the only artefact left behind, which is harmless and avoids
    # special-casing the not-yet-initialised state.
    with try_acquire_refresh_lock(project_root) as holder:
        if holder.acquired:
            reporter.success("lock-check: free")
            return

        telemetry.emit(
            "refresh_lock_contended",
            project_root=str(project_root),
            command="lock-check",
            action="rejected",
        )
        reporter.error(
            f"lock-check: another trie process is writing to {project_root}. "
            "Wait for it to finish and retry."
        )
        raise typer.Exit(code=2)


@app.command("refresh")
def refresh_cmd(
    ctx: typer.Context,
    before_turn: bool = typer.Option(
        False,
        "--before-turn",
        help=(
            "Run the cheap pre-turn freshness gate: full refresh if HEAD or mtimes "
            "moved, no-op otherwise. Intended as an agent harness's pre-turn hook."
        ),
    ),
    after_turn: bool = typer.Option(
        False,
        "--after-turn",
        help=(
            "Run the post-turn freshness sweep: detect filesystem changes since "
            "the last refresh and sync affected files. Intended as an agent "
            "harness's post-turn hook. Default mode when neither flag is given."
        ),
    ),
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model (only used when refresh fires a sync).",
    ),
) -> None:
    """Bring the graph + triefacts up to date with the working tree.

    The freshness gate. Agent harnesses register this as a hook:

      • `trie refresh --before-turn`: run at the start of an agent turn.
        Cheap when nothing changed since last refresh, full sync when HEAD or
        files have moved.
      • `trie refresh --after-turn`: run at the end of a turn. Picks up the
        agent's own edits and folds them into the graph + triefact tree before
        anyone (this agent next turn, another tool, a human) reads them.

    With neither flag, defaults to --after-turn behaviour.

    Both modes fail loudly outside a git repo: the gate's correctness depends
    on `git rev-parse HEAD` succeeding.
    """
    reporter = _get_reporter(ctx)
    if before_turn and after_turn:
        reporter.error("--before-turn and --after-turn are mutually exclusive")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.cascade
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    runner = ensure_fresh_before_turn if before_turn else ensure_fresh_after_turn
    mode_label = "before-turn" if before_turn else "after-turn"

    # `trie refresh` runs as a per-turn hook, so two agent turns in quick
    # succession can fire two refresh processes that race the SQLite store
    # and the triefact tree. The lock serialises them; the queued sentinel
    # coalesces N rapid contests down to "one current run + at most one
    # tail run" so we don't fan out an unbounded chain.
    with try_acquire_refresh_lock(project_root) as holder:
        if not holder.acquired:
            holder.mark_queued()
            telemetry.emit(
                "refresh_lock_contended",
                project_root=str(project_root),
                mode=mode_label,
                action="queued",
            )
            reporter.success(f"{mode_label}: another refresh is running; queued for tail pass.")
            return

        with (
            Store(db_path) as store,
            _progress_callback(reporter, label="refreshing") as cb,
        ):
            try:
                result = runner(
                    project_root=project_root,
                    config=config,
                    store=store,
                    client=client,
                    progress=cb,
                )
            except NotAGitRepoError as exc:
                reporter.error(str(exc))
                raise typer.Exit(code=1) from exc
            _report_freshness(reporter, result, mode=mode_label)

            # Tail pass: at most one extra run, coalescing every refresh
            # request that arrived while we held the lock. We deliberately
            # don't loop further — if more refreshes pile up during the
            # tail itself, the next hook invocation handles them.
            if holder.consume_queued():
                telemetry.emit(
                    "refresh_lock_tail_pass",
                    project_root=str(project_root),
                    mode=mode_label,
                )
                tail = runner(
                    project_root=project_root,
                    config=config,
                    store=store,
                    client=client,
                    progress=cb,
                )
                _report_freshness(reporter, tail, mode=f"{mode_label} (tail)")


def _report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None:
    """Render a single line per refresh outcome, plus token totals when a sync ran."""
    if not result.refreshed:
        reporter.success(f"{mode}: already fresh ({result.reason})")
        return
    inc = result.incremental
    if inc is None:
        # Defensive: ensure_fresh_* never returns refreshed=True with incremental=None,
        # but typed code shouldn't assume invariants the caller's eye can't see.
        reporter.success(f"{mode}: refreshed ({result.reason})")
        return
    reporter.success(
        f"{mode}: refreshed ({result.reason}); "
        f"synced {inc.files_synced} file(s), cost ${inc.actual_cost_usd:.4f}"
    )


@app.command("audit")
def audit_cmd(
    ctx: typer.Context,
    log: Path | None = typer.Option(
        None,
        "--log",
        "-l",
        help="Path to the debug.jsonl to read. Defaults to the configured debug.log_path.",
    ),
    compare: Path | None = typer.Option(
        None,
        "--compare",
        "-c",
        help="Render a side-by-side comparison: this log is the candidate, --log is the baseline.",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Print the summary as JSON. Mutually exclusive with --compare.",
    ),
) -> None:
    """Summarise a telemetry log: MCP usage, sync activity, retries, CLI invocations.

    Reads the `debug.jsonl` produced by trie's telemetry layer (see `[debug]` in
    `trie.toml`) and prints a compressed view of what happened during the run.
    With `--compare`, two logs are rendered side-by-side with deltas — the
    primary use case is comparing `with_trie` vs `without_trie` eval runs of an
    agent on the same task.

    No state is read or written beyond the log file(s); safe to run after the
    fact on archived logs.
    """
    reporter = _get_reporter(ctx)

    if compare is not None and as_json:
        reporter.error("--compare and --json are mutually exclusive")
        raise typer.Exit(code=1)

    log_path = _resolve_audit_log_path(log, reporter)
    try:
        baseline = AuditSummary.from_log(log_path)
    except FileNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    if compare is not None:
        try:
            candidate = AuditSummary.from_log(compare)
        except FileNotFoundError as exc:
            reporter.error(str(exc))
            raise typer.Exit(code=1) from exc
        render_audit_comparison(baseline, candidate, reporter.console)
        return

    if as_json:
        # Use plain print rather than the reporter so the output is pipeable.
        import json as _json

        typer.echo(_json.dumps(baseline.to_dict(), indent=2, default=str))
        return

    render_audit(baseline, reporter.console)


def _resolve_audit_log_path(log: Path | None, reporter: Reporter) -> Path:
    """Pick the debug.jsonl to read.

    Resolution order: explicit `--log` argument, then the `[debug].log_path` from
    the nearest `trie.toml`, then `./debug.jsonl` in the cwd. We don't *require*
    a trie.toml — running `trie audit` against a log from a different project is
    a normal eval workflow."""
    if log is not None:
        return log
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError:
        return Path.cwd() / "debug.jsonl"
    cfg_path = Path(config.debug.log_path)
    if not cfg_path.is_absolute():
        cfg_path = (project_root / cfg_path).resolve()
    return cfg_path


def _print_scan_breakdown(
    reporter: Reporter, scan_result, db_path: Path, project_root: Path
) -> None:
    parts: list[str] = []
    if scan_result.files_new:
        parts.append(f"[green]{scan_result.files_new} new[/green]")
    if scan_result.files_updated:
        parts.append(f"[yellow]{scan_result.files_updated} updated[/yellow]")
    if scan_result.files_unchanged:
        parts.append(f"{scan_result.files_unchanged} unchanged")
    if scan_result.files_removed:
        parts.append(f"[red]{scan_result.files_removed} removed[/red]")
    breakdown = ", ".join(parts) if parts else "no files in scope"
    reporter.success(f"scanned {scan_result.files_total} files: {breakdown}")
    reporter.detail(
        f"  {scan_result.symbols_total} symbols, {scan_result.edges_total} edges in "
        f"{db_path.relative_to(project_root)}"
    )


def _print_plan(reporter: Reporter, plan: BootstrapPlan, model_id: str) -> None:
    reporter.info(
        f"plan for [cyan]{model_id}[/cyan] — {len(plan.items)} files, "
        f"~${plan.total_estimated_cost:.4f} estimated"
    )
    for it in plan.items[:10]:
        reporter.info(
            f"  • [bold]{it.file_path}[/bold] "
            f"({it.public_symbols} symbols, score {it.score:.0f}, ~${it.estimated.cost_usd:.4f})"
        )
    if len(plan.items) > 10:
        reporter.info(f"  … and {len(plan.items) - 10} more")


def _print_incremental_plan(
    reporter: Reporter,
    plan: BootstrapPlan,
    worklist: IncrementalWorklist,
    model_id: str,
) -> None:
    """Plan output tailored to incremental sync — emphasises 'what `trie sync` would
    actually do' rather than full re-bootstrap cost."""
    direct_n = len(worklist.directly_stale)
    cascade_n = len(worklist.cascaded_files)
    orphan_n = len(worklist.orphan_triefacts)

    parts = [f"{direct_n} directly stale"]
    if cascade_n:
        parts.append(f"{cascade_n} cascaded")
    if orphan_n:
        parts.append(f"{orphan_n} orphan to remove")
    breakdown = ", ".join(parts)
    reporter.info(
        f"incremental plan for [cyan]{model_id}[/cyan] — {len(plan.items)} file(s) "
        f"({breakdown}), ~${plan.total_estimated_cost:.4f} estimated"
    )

    # Display in execution order: stale files first (sync touches them first so
    # diff-aware regen can feed their fresh prose into cascade-pulled prompts),
    # then cascade-pulled files ranked by hop distance from the seed change.
    # Within stale, preserve `plan.items` order (bootstrap rank). Within each
    # cascade hop level, also preserve `plan.items` order so the most expensive
    # work is visible at the top of each tier.
    direct_set = set(worklist.directly_stale)
    stale_items = [it for it in plan.items if it.file_path in direct_set]
    cascade_items = sorted(
        (it for it in plan.items if it.file_path not in direct_set),
        key=lambda it: worklist.hop_by_file.get(it.file_path, 0),
    )
    ordered = stale_items + cascade_items
    for it in ordered[:10]:
        if it.file_path in direct_set:
            tag = "stale"
        else:
            hop = worklist.hop_by_file.get(it.file_path, 0)
            tag = f"cascade · hop {hop}" if hop else "cascade"
        # Symbol-level breakdown: how many of the file's documented symbols will
        # actually hit the LLM. Absence from the map means full-file regen (cold-
        # write, MISSING_TRIEFACT) so all `public_symbols` will be touched.
        regen_set = worklist.regen_qnames_by_file.get(it.file_path)
        if regen_set is None:
            sym_label = f"{it.public_symbols} symbols"
        else:
            sym_label = f"{len(regen_set)}/{it.public_symbols} symbols"
        reporter.info(
            f"  • [bold]{it.file_path}[/bold] [dim]({tag})[/dim] "
            f"({sym_label}, ~${it.estimated.cost_usd:.4f})"
        )
    if len(ordered) > 10:
        reporter.info(f"  … and {len(ordered) - 10} more")

    if worklist.orphan_triefacts:
        reporter.detail("orphan triefacts (would be deleted by `trie sync`):")
        for path in worklist.orphan_triefacts[:10]:
            try:
                rel = path.relative_to(Path.cwd())
            except ValueError:
                rel = path
            reporter.detail(f"  [red]✗[/red] {rel}")
        if len(worklist.orphan_triefacts) > 10:
            reporter.detail(f"  … and {len(worklist.orphan_triefacts) - 10} more")


_REASON_LABELS: dict[StaleReason, str] = {
    StaleReason.MISSING_TRIEFACT: "missing triefact",
    StaleReason.MISSING_SECTION: "missing section",
    StaleReason.STALE_SECTION: "stale (source changed)",
    StaleReason.ORPHAN_SECTION: "orphan (symbol gone)",
    StaleReason.TAMPERED_BODY: "tampered body",
    StaleReason.LEGACY_SECTION: "legacy (no body fingerprint)",
}


def _print_drift_detail(reporter: Reporter, items: list) -> None:
    """Render per-file drift items in MEDIUM+ verbosity. Caller emits the summary line."""
    grouped: dict[str, list] = {}
    for it in items:
        grouped.setdefault(it.triefact_path, []).append(it)
    for triefact_path, group in sorted(grouped.items()):
        reporter.console.print(f"[red]✗[/red] {triefact_path}")
        for it in group:
            label = _REASON_LABELS.get(it.reason, str(it.reason))
            target = it.qualified_name or it.source_path
            reporter.console.print(f"    [yellow]{label}[/yellow] {target}")
    reporter.console.print()


def _verify_drift(reporter: Reporter, *, exit_on_drift: bool) -> bool:
    """Offline drift check. Returns True if clean, False if drift was reported.

    When `exit_on_drift` is True, a non-empty result aborts via `typer.Exit(1)` —
    that's the path `trie verify` and the pre-commit hook take. Plan and sync use
    `exit_on_drift=False` so the check just surfaces drift before the main work.
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    result = check_project(project_root=project_root, config=config)

    if result.is_clean:
        reporter.success("triefact tree is coherent")
        return True

    if reporter.verbosity >= Verbosity.MEDIUM:
        _print_drift_detail(reporter, result.items)

    grouped_count = len({it.triefact_path for it in result.items})
    summary = (
        f"{len(result.items)} issue(s) across {grouped_count} triefact file(s) — "
        "run `trie sync` to refresh"
    )
    if exit_on_drift:
        reporter.error(summary)
        raise typer.Exit(code=1)
    reporter.warn(summary)
    return False


@app.command("sync")
def sync_cmd(
    ctx: typer.Context,
    file: Path | None = typer.Option(
        None,
        "--file",
        "-f",
        help="Sync exactly one source file. Useful as a smoke test of the LLM path.",
    ),
    all_: bool = typer.Option(
        False,
        "--all",
        help="Force a full re-pass (every file in scope), even if triefacts already exist.",
    ),
    budget: float | None = typer.Option(
        None,
        "--budget",
        help="USD budget cap. Stops once cumulative actual cost reaches this.",
    ),
    limit: int | None = typer.Option(
        None,
        "--limit",
        help="Cap the number of files synced.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help=(
            "Preview what `trie sync` would change. Regenerates stale triefacts into "
            "`.trie/preview/` and prints unified diffs (makes API calls — cap with "
            "--budget / --limit)."
        ),
    ),
    metadata_only: bool = typer.Option(
        False,
        "--metadata-only",
        help=(
            "Refresh triefact front matter from the live store without calling the LLM. "
            "Useful after a graph-only change (e.g. an improved reference resolver) "
            "where edge counts moved but source did not."
        ),
    ),
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        help=(
            "Force cold regeneration for every symbol in the file, bypassing the "
            "diff-aware path. Only valid with --file. Use when existing prose is "
            "known to be wrong and a full fresh LLM pass is needed."
        ),
    ),
) -> None:
    """Generate or refresh trie triefacts.

    Modes (auto-detected):
      • --file          : sync one file.
      • --dry-run       : preview unified diff against the live tree.
      • --metadata-only : refresh front matter only; no LLM, no section changes.
      • --all           : force full re-pass.
      • default         : if no triefacts exist yet → first-run bootstrap;
                          otherwise → incremental cascade.

    Drift detection runs as the first step regardless. For an LLM-free, exit-coded
    drift gate suitable for pre-commit hooks, use `trie verify`.
    """
    reporter = _get_reporter(ctx)
    if file is not None and all_:
        reporter.error("--file and --all are mutually exclusive")
        raise typer.Exit(code=1)
    if force and file is None:
        reporter.error("--force requires --file")
        raise typer.Exit(code=1)
    if metadata_only and (
        file is not None or all_ or dry_run or budget is not None or limit is not None
    ):
        reporter.error(
            "--metadata-only cannot be combined with --file / --all / --dry-run / --budget / --limit"
        )
        raise typer.Exit(code=1)

    # Resolve project root up front so we can guard every sync sub-mode with
    # the same write lock. Config errors stay exit-1; the lock guard is the
    # only thing that raises exit-2 (transient contention).
    try:
        _, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    with _acquire_write_lock_or_exit(project_root, reporter, "sync"):
        if metadata_only:
            _run_metadata_only_refresh(reporter)
            return

        if file is not None:
            _run_single_file_sync(reporter, file, model, force=force)
            return

        if dry_run:
            _run_dry_run_diff(reporter=reporter, model=model, budget=budget, limit=limit)
            return

        # Auto-detect first-run vs incremental. Re-load config here so the
        # helpers see exactly the dataclass they were built around; the
        # earlier load above was only to get a path for the lock.
        try:
            config, project_root = Config.find_and_load(Path.cwd())
        except ConfigNotFoundError as exc:
            reporter.error(str(exc))
            raise typer.Exit(code=1) from exc

        triefacts_root = project_root / config.triefacts.root
        needs_full_pass = all_ or not _has_existing_triefacts(triefacts_root)

        if needs_full_pass:
            _run_full_pass(
                reporter=reporter,
                project_root=project_root,
                config=config,
                model=model,
                budget=budget,
                limit=limit,
            )
        else:
            _run_incremental_sync(reporter=reporter, model=model, budget=budget, limit=limit)


def _has_existing_triefacts(triefacts_root: Path) -> bool:
    """True if the triefacts dir exists and contains at least one .md file."""
    if not triefacts_root.is_dir():
        return False
    for _ in triefacts_root.rglob("*.md"):
        return True
    return False


def _run_full_pass(
    *,
    reporter: Reporter,
    project_root: Path,
    config: Config,
    model: str | None,
    budget: float | None,
    limit: int | None,
) -> None:
    """First-run / forced full re-pass. Builds the plan, asks for confirmation if no
    cap is set, then runs bootstrap with streaming per-file progress."""
    model_id = model or config.models.bootstrap
    pricing = get_pricing(model_id)
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    with Store(db_path) as store:
        with reporter.status("scanning project…"):
            scan_project(project_root=project_root, config=config, store=store)
        with reporter.status("counting tokens…"):
            plan = build_plan(
                project_root=project_root, store=store, model_id=model_id, client=client
            )

        if not plan.items:
            reporter.warn("no files in scope")
            return

        _print_plan(reporter, plan, model_id)

        if budget is None and limit is None:
            if _is_interactive():
                if not typer.confirm(
                    f"Proceed with full bootstrap? (~${plan.total_estimated_cost:.4f})",
                    default=False,
                ):
                    reporter.info("aborted")
                    return
            else:
                reporter.error(
                    "first-run bootstrap requires --budget USD or --limit N "
                    "(or run interactively to confirm)."
                )
                raise typer.Exit(code=1)

        with _progress_callback(reporter, label="syncing") as cb:
            result = run_bootstrap(
                plan=plan,
                project_root=project_root,
                config=config,
                client=client,
                pricing=pricing,
                budget_usd=budget,
                limit=limit,
                progress=cb,
                store=store,
            )

    reporter.success(
        f"synced {result.files_synced} files "
        f"(skipped {result.files_skipped_no_budget} due to budget/limit)"
    )
    reporter.info(
        f"  estimated ${result.estimated_cost_usd:.4f} · actual ${result.actual_cost_usd:.4f}"
    )


def _run_dry_run_diff(
    *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None
) -> None:
    """`trie sync --dry-run`: regenerate stale triefacts into .trie/preview/ and
    print unified diffs against the live tree. Replaces the old `trie diff`."""
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    pricing = get_pricing(model_id)
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    with Store(db_path) as store, _progress_callback(reporter, label="diffing") as cb:
        result = diff_project(
            project_root=project_root,
            config=config,
            client=client,
            pricing=pricing,
            budget_usd=budget,
            limit=limit,
            progress=cb,
            store=store,
        )

    if not result.diffs:
        reporter.success("no stale triefacts — nothing to preview")
        return

    for fd in result.diffs:
        reporter.info(
            f"\n[bold cyan]{fd.canonical_triefact_path.relative_to(project_root)}[/bold cyan]"
        )
        if fd.unified_diff:
            reporter.console.print(fd.unified_diff, end="")
        else:
            reporter.info("  (no textual diff — possibly only fingerprint changes)")

    reporter.success(
        f"previewed {len(result.diffs)} file(s); "
        f"actual cost ${result.actual_cost_usd:.4f} · "
        f"skipped {result.files_skipped_no_budget} due to budget/limit"
    )


def _run_single_file_sync(
    reporter: Reporter, file: Path, model: str | None, force: bool = False
) -> None:
    if not file.exists():
        reporter.error(f"{file} does not exist")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(file.parent)
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    with (
        Store(db_path) as store,
        reporter.status(f"generating triefact for [cyan]{file}[/cyan]…"),
    ):
        result = sync_single_file(
            file, project_root=project_root, config=config, client=client, store=store, force=force
        )

    reporter.success(f"wrote {result.triefact_path}")
    reporter.info(
        f"  {result.symbols_generated} symbols generated"
        + (f", {result.sections_removed} stale sections removed" if result.sections_removed else "")
    )
    reporter.detail(
        f"  tokens: {result.input_tokens} in / {result.output_tokens} out · "
        f"cache: {result.cache_creation_input_tokens} write / {result.cache_read_input_tokens} read"
    )


def _run_metadata_only_refresh(reporter: Reporter) -> None:
    """Refresh every triefact's front matter from the live store without any LLM calls.

    The flow:
      1. Load config + open the store.
      2. Re-scan the project to make sure the graph reflects current source — this
         picks up new edges introduced by a resolver change automatically.
      3. For each in-scope source file with a triefact, recompute its front matter
         from the just-scanned store and rewrite only if the bytes changed.

    Designed for the post-graph-change case: nothing prose moved, but ref counts
    and `defines` entries are stale. Free (no API), idempotent (re-runs are
    no-ops once everything matches).
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    db_path = project_root / ".trie" / "graph.db"
    src_root = (project_root / config.triefacts.source_root).resolve()

    with Store(db_path) as store:
        with reporter.status("scanning project…"):
            scan_result = scan_project(project_root=project_root, config=config, store=store)
        reporter.detail(
            f"  scanned {scan_result.files_total} files · {scan_result.symbols_total} symbols "
            f"· {scan_result.edges_total} edges"
        )

        files = discover_files(project_root, config.scope)
        total = len(files)
        changed_count = 0
        skipped_count = 0
        with reporter.start_progress(total, label="refreshing metadata") as bar:
            for f in files:
                # `discover_files` returns absolute paths beneath the scope; ensure they
                # also live under `source_root` (the refresh function requires this).
                if not f.is_relative_to(src_root):
                    bar.skip_file(str(f), "outside source_root")
                    skipped_count += 1
                    continue
                rel = str(f.relative_to(src_root))
                bar.start_file(rel)
                result = refresh_triefact_metadata(
                    f, project_root=project_root, config=config, store=store
                )
                if result.changed:
                    changed_count += 1
                # Use `finish_file` to advance the bar; metadata refreshes have no
                # cost or token telemetry to report.
                bar.finish_file(rel)

    reporter.success(
        f"refreshed metadata on {changed_count} of {total - skipped_count} triefact(s) "
        f"({total - changed_count - skipped_count} already current)"
    )


def _run_incremental_sync(
    *, reporter: Reporter, model: str | None, budget: float | None, limit: int | None
) -> None:
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.cascade
    pricing = get_pricing(model_id)
    client = make_client(model_id, sync_cfg=config.sync)

    db_path = project_root / ".trie" / "graph.db"
    with Store(db_path) as store, _progress_callback(reporter, label="syncing") as cb:
        result = run_incremental(
            project_root=project_root,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
            budget_usd=budget,
            limit=limit,
            progress=cb,
        )

    if result.orphan_triefacts_removed:
        for triefact in result.orphan_triefacts_removed:
            reporter.info(
                f"[red]✗[/red] removed orphan triefact {triefact.relative_to(project_root)}"
            )

    if result.files_synced == 0 and result.directly_stale_count == 0:
        if result.orphan_triefacts_removed:
            reporter.success(
                f"cleaned up {len(result.orphan_triefacts_removed)} orphan(s); "
                "triefact tree is otherwise coherent"
            )
        else:
            reporter.success("triefact tree is coherent — nothing to sync")
        return

    reporter.success(
        f"synced {result.files_synced} file(s) "
        f"({result.directly_stale_count} directly stale, "
        f"{result.cascaded_count} pulled in by the cascade)"
    )
    if result.files_skipped_no_budget:
        reporter.info(f"  skipped {result.files_skipped_no_budget} due to budget/limit")
    reporter.info(f"  actual cost: ${result.actual_cost_usd:.4f}")


@app.command("setup")
def setup_cmd(
    ctx: typer.Context,
    target: list[str] | None = typer.Option(
        None,
        "--target",
        "-t",
        help=(
            "Set up for a specific agent. Repeat the flag for multiple targets. "
            f"Known: {', '.join(MCP_TARGETS)}."
        ),
    ),
    install_all: bool = typer.Option(
        False,
        "--all",
        help="Set up for every known agent. Skips per-target detection.",
    ),
    scope: str = typer.Option(
        "project",
        "--scope",
        help="MCP install scope: 'project' (writes into this repo) or 'user' (~/.<agent>/...).",
        case_sensitive=False,
    ),
    print_only: bool = typer.Option(
        False,
        "--print-only",
        help="Print what would be written for both MCP and hooks; don't touch any files.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Resolve target paths and show what would change, but don't write.",
    ),
    no_overrides: bool = typer.Option(
        False,
        "--no-overrides",
        help=(
            "Skip the tool-override step. By default, `setup` replaces the "
            "agent's built-in `grep` and `read` with wrappers that route "
            "through trie (and adds `trace`). Pass --no-overrides to "
            "install hook + docs only and leave the agent's built-ins alone."
        ),
    ),
    with_mcp: bool = typer.Option(
        False,
        "--with-mcp",
        help=(
            "Also register the trie MCP server for each target "
            "(same as `trie mcp install`). Off by default — the hook and "
            "tool overrides are sufficient for most setups."
        ),
    ),
) -> None:
    """Wire trie into an agent: hook + tool overrides + docs (MCP optional).

    For each detected (or specified) target, this runs three installs by
    default:

      1. A turn-boundary hook that calls `trie refresh --after-turn` so the
         graph and triefact tree stay current with the agent's edits.
      2. Custom tool wrappers that replace the agent's built-in `grep` and
         `read` with calls to `trie grep` / `trie read`, plus `trace` and
         the explain/grep-str family as new tools. Pass `--no-overrides` to
         skip this step and leave the agent's built-ins alone.
      3. The agent-facing docs (TRIE.md + AGENTS.md pointer).

    Pass `--with-mcp` to also register the MCP server (same as
    `trie mcp install`). This is off by default because the tool overrides
    already give the agent full access to trie without the MCP layer.

    Re-running `setup` is safe: every step is idempotent (existing files
    that match what we'd write are reported as `skipped`; drift is
    overwritten). Agents without an automatable hook or override surface
    emit a clear `needs_manual_setup` notice explaining what to wire by hand.
    """
    reporter = _get_reporter(ctx)

    if target and install_all:
        reporter.error("--target and --all are mutually exclusive")
        raise typer.Exit(code=1)

    scope_norm = scope.lower()
    if scope_norm not in ("project", "user"):
        reporter.error("--scope must be 'project' or 'user'")
        raise typer.Exit(code=1)

    try:
        _, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    # MCP install — opt-in only via --with-mcp.
    mcp_plan: InstallPlan | None = None
    if with_mcp:
        try:
            mcp_plan = mcp_run_install(
                target_names=target,
                scope=scope_norm,  # type: ignore[arg-type]
                install_all=install_all,
                print_only=print_only,
                dry_run=dry_run,
                project_root=project_root,
            )
        except MCPInstallError as exc:
            reporter.error(str(exc))
            raise typer.Exit(code=1) from exc

    # Hook install. When MCP ran we reuse its resolved target names so
    # auto-detection stays consistent across both steps. When MCP is
    # skipped the hook installer does its own detection (or honours
    # --target / --all directly).
    try:
        hook_plan = hook_run_install(
            target_names=mcp_plan.target_names if mcp_plan else target,
            install_all=install_all if not mcp_plan else False,
            print_only=print_only,
            dry_run=dry_run,
            project_root=project_root,
        )
    except HookInstallError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    # Resolved target names for all subsequent steps come from whichever
    # installer ran first (MCP if --with-mcp, otherwise hook).
    resolved_targets = mcp_plan.target_names if mcp_plan else hook_plan.target_names

    # Docs install: write TRIE.md and refresh the pointer block in any
    # existing AGENTS.md / CLAUDE.md so agents discover the navigation
    # tools without the user having to author docs by hand. We pass the
    # resolved target slugs through so the doc can bake in harness-specific
    # tool names. The first target wins for the body; the rest land in a
    # footer that names tool aliases under the other harnesses.
    try:
        docs_plan = docs_run_install(
            project_root=project_root,
            print_only=print_only,
            dry_run=dry_run,
            target_names=resolved_targets,
        )
    except DocsInstallError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    # Tool-override install: replaces the agent's built-in `grep`/`read`
    # with wrappers that call trie (opencode), or installs an advisory
    # PreToolUse hook (Claude Code). Other harnesses have no automated
    # path and emit a `needs_manual_setup` notice. Default on; the user
    # opts out with `--no-overrides`. Re-running `setup` is idempotent,
    # so an accidental install is one `--no-overrides` rerun away from a
    # clean state.
    override_plan: ToolOverrideInstallPlan | None = None
    if resolved_targets and not no_overrides:
        try:
            override_plan = tool_override_run_install(
                target_names=resolved_targets,
                print_only=print_only,
                dry_run=dry_run,
                project_root=project_root,
            )
        except ToolOverrideInstallError as exc:
            reporter.error(str(exc))
            raise typer.Exit(code=1) from exc

    _render_setup_plan(reporter, mcp_plan, hook_plan, docs_plan, override_plan)

    # Surface a non-zero exit if any step hit an error so CI/scripts react.
    mcp_errors = any(r.action == "error" for r in mcp_plan.results) if mcp_plan else False
    hook_errors = any(r.action == "error" for r in hook_plan.results)
    docs_errors = any(r.action == "error" for r in docs_plan.results)
    override_errors = (
        any(r.action == "error" for r in override_plan.results) if override_plan else False
    )
    if mcp_errors or hook_errors or docs_errors or override_errors:
        raise typer.Exit(code=1)


def _render_setup_plan(
    reporter: Reporter,
    mcp_plan: InstallPlan | None,
    hook_plan: HookInstallPlan,
    docs_plan: DocsInstallPlan,
    override_plan: ToolOverrideInstallPlan | None = None,
) -> None:
    """Print one merged report: per-target hook + override lines (+ MCP if run), plus a docs section.

    Each target gets a header with its hook, optional MCP, and optional
    tool-override install outcomes grouped beneath. Manual-setup notes are
    emitted under the relevant line so the user can copy them out of their
    terminal directly. Docs install is target-independent (one TRIE.md per
    project), so it gets its own section at the end.
    """
    import json

    mcp_by_target = {r.target: r for r in mcp_plan.results} if mcp_plan else {}
    hook_by_target = {r.target: r for r in hook_plan.results}
    override_by_target = {r.target: r for r in override_plan.results} if override_plan else {}
    targets = sorted(
        {
            *mcp_by_target.keys(),
            *hook_by_target.keys(),
            *override_by_target.keys(),
        }
    )

    for slug in targets:
        display = MCP_TARGETS[slug].display_name if slug in MCP_TARGETS else slug
        reporter.info(f"\n[bold cyan]{display}[/bold cyan]")

        mcp_result = mcp_by_target.get(slug)
        if mcp_result is not None:
            line = f"  mcp:       {_format_action(mcp_result.action, mcp_result.path)}"
            if mcp_result.detail:
                line += f" — {mcp_result.detail}"
            reporter.info(line)
            if mcp_result.action == "preview" and mcp_result.path is not None:
                snippet = {mcp_result.target: mcp_result.snippet}
                reporter.console.print(json.dumps(snippet, indent=2))

        hook_result = hook_by_target.get(slug)
        if hook_result is not None:
            line = f"  hook:      {_format_action(hook_result.action, hook_result.path)}"
            if hook_result.detail and hook_result.action != "needs_manual_setup":
                line += f" — {hook_result.detail}"
            reporter.info(line)
            if hook_result.action == "needs_manual_setup":
                reporter.warn(f"    manual setup required: {hook_result.detail}")
            elif hook_result.action == "preview" and hook_result.path is not None:
                reporter.console.print(hook_result.contents)

        override_result = override_by_target.get(slug)
        if override_result is not None:
            _render_override_target_block(reporter, override_result)

    # Docs section. Empty `results` would only happen if TRIE.md write
    # failed before any result was appended — defensive guard, shouldn't
    # be reachable in practice.
    if docs_plan.results:
        reporter.info("\n[bold cyan]docs[/bold cyan]")
        for result in docs_plan.results:
            line = f"  {result.target}: {_format_action(result.action, result.path)}"
            # `detail` carries either a status message ("already up to date")
            # or, for preview/error, the full would-be contents / error text.
            # Truncate the preview body so the renderer doesn't dump 14KB of
            # markdown into the terminal; the user can read the file directly.
            if result.detail and result.action not in ("preview",):
                line += f" — {result.detail}"
            reporter.info(line)


def _render_override_target_block(reporter: Reporter, result: object) -> None:
    """Render a single target's tool-override install outcome.

    Tool overrides can write multiple files per target (e.g. opencode writes
    `grep.ts` plus `read.ts` plus `trace.ts`), so we render a summary line
    then list each file's outcome indented underneath. Manual-
    setup notices for unsupported harnesses get the same treatment as the
    hook line so users have one consistent visual style.
    """
    line = f"  override:  {result.action}"
    if result.action == "needs_manual_setup":
        line += " — see manual instructions below"
    elif not result.files:
        line += " — nothing to do"
    reporter.info(line)

    if result.action == "needs_manual_setup" and result.detail:
        reporter.warn(f"    {result.detail}")
        return

    for f in result.files:
        sub = f"    {f.action} {f.relative_path}"
        if f.description:
            sub += f" [dim]({f.description})[/dim]"
        if f.action in ("skipped", "error") and f.detail:
            sub += f" — {f.detail}"
        reporter.info(sub)


def _format_action(action: str, path: Path | None) -> str:
    """Render an action label with a path suffix. Used for both MCP and hook lines."""
    if path is None:
        return action
    return f"{action} → {path}"


# ---------------------------------------------------------------------------
# grep / read / trace — agent-facing CLI mirror of the MCP tools
# ---------------------------------------------------------------------------
#
# Every operation the MCP server exposes is also available as a `trie` CLI
# subcommand, so an agent that prefers shelling out to making MCP calls can
# still do the full set of trie operations. The CLI commands call the same
# `TrieTools` methods the MCP server registers, so the JSON output under
# `--json` is byte-equivalent to the MCP wire response. Default output is
# human-readable for terminal use; pass `--json` for the raw envelope.


def _open_tools(reporter: Reporter) -> TrieTools:
    """Resolve project root and open a TrieTools session.

    Centralised so all three subcommands handle "no trie.toml found" the
    same way. The returned TrieTools holds an open SQLite handle; callers
    must `.close()` it when done.

    Constructs `TrieTools` with `event_name="cli_call"` so per-call
    telemetry emitted from `grep`/`read`/`trace` lands as `cli_call`
    events rather than `mcp_call`. The audit module distinguishes the
    two streams so an operator can tell how the agent (or human) is
    reaching trie: shelled-out CLI vs persistent MCP server.
    """
    try:
        _, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc
    return TrieTools(project_root, event_name="cli_call")


def _emit_envelope(
    envelope: dict[str, object],
    *,
    as_json: bool,
    reporter: Reporter,
    render: Callable[[dict[str, object], Reporter], None],
) -> None:
    """Print the envelope either as raw JSON or via the provided renderer.

    Error envelopes (`{"error": {...}}`) always render through the renderer
    so the human path produces a useful diagnostic, and exit code 1 is set
    so scripts can react. JSON mode dumps to stdout verbatim so an agent
    parsing the output gets exactly what the MCP wire would return.
    """
    if as_json:
        import json as _json

        # Print to the underlying console so Rich doesn't add ANSI codes;
        # JSON consumers want a clean stream.
        typer.echo(_json.dumps(envelope, indent=2, default=str))
    else:
        render(envelope, reporter)

    if "error" in envelope:
        raise typer.Exit(code=1)


def _patched_tag(count: int) -> str:
    """Return a yellow `[patched: N]` tag when count > 0."""
    if count <= 0:
        return ""
    return f" [yellow][patched: {count}][/yellow]"


def _render_grep(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable rendering for `trie grep` output.

    Shows hits as a compact table (qname, kind, file pointer, one-liner)
    when present. When hits is empty, falls through to the fallback
    envelope: prints the fallback kind, query, note, and the ranked
    candidate matches if any. Error envelopes show the code, message,
    and suggestion on separate lines.
    """
    from rich.table import Table

    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return

    hits = envelope.get("hits") or []
    if isinstance(hits, list) and hits:
        table = Table(title=f"{len(hits)} hit(s)", show_header=True, header_style="bold")
        table.add_column("qname", style="cyan")
        table.add_column("kind", style="dim")
        table.add_column("location", style="dim")
        table.add_column("one-liner")
        for h in hits:
            if not isinstance(h, dict):
                continue
            qname = str(h.get("qname", ""))
            patch_count = int(h.get("pending_patch_count", 0))
            qname_display = qname + _patched_tag(patch_count)
            table.add_row(
                qname_display,
                str(h.get("kind", "")),
                str(h.get("file_pointer", "")),
                str(h.get("one_liner", "")),
            )
        reporter.console.print(table)
        return

    # No hits. Show the fallback envelope.
    fallback = envelope.get("fallback")
    if not isinstance(fallback, dict):
        reporter.info("[dim]no hits, no fallback envelope[/dim]")
        return

    kind = fallback.get("kind", "?")
    note = fallback.get("note", "")
    reporter.info(f"[yellow]no symbol-name hits[/yellow] (fallback: {kind})")
    if note:
        reporter.info(f"  [dim]{note}[/dim]")

    matches = fallback.get("matches") or []
    if isinstance(matches, list) and matches:
        table = Table(
            title=f"{len(matches)} candidate(s) by text match",
            show_header=True,
            header_style="bold",
        )
        table.add_column("qname", style="cyan")
        table.add_column("inbound", justify="right", style="dim")
        table.add_column("location", style="dim")
        table.add_column("one-liner")
        for m in matches:
            if not isinstance(m, dict):
                continue
            table.add_row(
                str(m.get("qname", "")),
                str(m.get("inbound_count", "")),
                str(m.get("file_pointer", "")),
                str(m.get("one_liner", "")),
            )
        reporter.console.print(table)


def _render_read(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable rendering for `trie read` output.

    Prints signature, source pointer, prose, and the caller / callee
    neighbour lists with their one-liners.
    """
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return

    qname = envelope.get("qname", "")
    signature = envelope.get("signature", "")
    source_pointer = envelope.get("source_pointer", "")
    reporter.console.print(f"[bold cyan]{qname}[/bold cyan]")
    if signature:
        reporter.console.print(f"  [dim]{signature}[/dim]")
    if source_pointer:
        reporter.console.print(f"  [dim]→ {source_pointer}[/dim]")

    prose = envelope.get("prose") or ""
    if isinstance(prose, str) and prose.strip():
        reporter.console.print()
        reporter.console.print(prose)
    else:
        reporter.console.print()
        reporter.console.print("[dim](no prose; run `trie sync` for this file)[/dim]")

    def _print_neighbours(label: str, items: object) -> None:
        if not isinstance(items, list) or not items:
            return
        reporter.console.print()
        reporter.console.print(f"[bold]{label}[/bold] ({len(items)})")
        for entry in items:
            if not isinstance(entry, dict):
                continue
            ql = entry.get("qname", "")
            ol = entry.get("one_liner", "")
            reporter.console.print(f"  [cyan]{ql}[/cyan] — {ol}")

    pending = envelope.get("pending_patches") or []
    if isinstance(pending, list) and pending:
        reporter.console.print()
        reporter.console.print(f"[yellow]pending patches[/yellow] ({len(pending)})")
        for p in pending:
            if not isinstance(p, dict):
                continue
            origin = str(p.get("origin", "?"))
            note = str(p.get("note", ""))
            reason = str(p.get("reason", ""))
            line = f"  [{origin}] {note}"
            if reason:
                line += f" [dim]({reason})[/dim]"
            reporter.console.print(line)

    _print_neighbours("callers", envelope.get("callers"))
    _print_neighbours("callees", envelope.get("callees"))

    notes = envelope.get("notes") or []
    if isinstance(notes, list) and notes:
        reporter.console.print()
        for n in notes:
            reporter.console.print(f"[yellow]![/yellow] {n}")


def _render_trace(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable rendering for `trie trace` output.

    Shows the root, then nodes by qname with their one-liners, then a
    compact edge list. For larger graphs the JSON output is more useful
    — `--json` exists for that path.
    """
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return

    root = envelope.get("root")
    if isinstance(root, dict):
        reporter.console.print(f"[bold cyan]{root.get('qname', '')}[/bold cyan]")
        ol = root.get("one_liner", "")
        if ol:
            reporter.console.print(f"  [dim]{ol}[/dim]")

    nodes = envelope.get("nodes") or {}
    if isinstance(nodes, dict) and nodes:
        reporter.console.print()
        reporter.console.print(f"[bold]nodes[/bold] ({len(nodes)})")
        for qname, data in nodes.items():
            if not isinstance(data, dict):
                continue
            ol = data.get("one_liner", "")
            patched = data.get("has_pending_patches", False)
            tag = _patched_tag(1) if patched else ""
            reporter.console.print(f"  [cyan]{qname}{tag}[/cyan] — {ol}")

    edges = envelope.get("edges") or []
    if isinstance(edges, list) and edges:
        reporter.console.print()
        reporter.console.print(f"[bold]edges[/bold] ({len(edges)})")
        for e in edges:
            if not isinstance(e, dict):
                continue
            arrow = "→" if e.get("direction") == "out" else "←"
            reporter.console.print(f"  {e.get('from', '')} {arrow} {e.get('to', '')}")

    truncated = envelope.get("truncated_at") or []
    if isinstance(truncated, list) and truncated:
        reporter.console.print()
        reporter.console.print(
            f"[yellow]truncated at hub(s):[/yellow] {', '.join(str(q) for q in truncated)}"
        )

    notes = envelope.get("notes") or []
    if isinstance(notes, list) and notes:
        reporter.console.print()
        for n in notes:
            reporter.console.print(f"[yellow]![/yellow] {n}")


def _render_error_envelope(err: dict[str, object], reporter: Reporter) -> None:
    """Render a `{code, message, suggestion?}` error block in human-readable form.

    Used by all three render functions because all three tools return the
    same error envelope shape on failure. Keeps the error UX consistent
    regardless of which subcommand the agent invoked.
    """
    code = err.get("code", "?")
    message = err.get("message", "")
    reporter.error(f"{code}: {message}")
    suggestion = err.get("suggestion")
    if suggestion:
        reporter.info(f"  [dim]suggestion: {suggestion}[/dim]")


def _build_grep_predicate(
    name: str | None,
    kind: str | None,
    scope_prefix: str | None,
    scope_exclude: list[str] | None,
    public_only: bool,
    inbound_min: int | None,
    inbound_max: int | None,
    outbound_min: int | None,
    outbound_max: int | None,
    predicate_json: str | None,
    reporter: Reporter,
) -> dict[str, object]:
    """Assemble the predicate dict from the CLI's separate flags.

    `--predicate JSON` lets the agent pass the full envelope verbatim (the
    same shape it would send via MCP); the other flags are ergonomic
    shortcuts for the common single-field queries. Flags override JSON
    fields when both are given, which matches how an agent would expect
    "more specific wins" — pass the JSON for the base shape, tighten with
    flags.
    """
    pred: dict[str, object] = {}
    if predicate_json:
        import json as _json

        try:
            parsed = _json.loads(predicate_json)
        except _json.JSONDecodeError as exc:
            reporter.error(f"--predicate is not valid JSON: {exc}")
            raise typer.Exit(code=2) from exc
        if not isinstance(parsed, dict):
            reporter.error("--predicate JSON must be an object")
            raise typer.Exit(code=2)
        pred.update(parsed)

    if name is not None:
        pred["name_contains"] = name
    if kind is not None:
        pred["kind"] = kind
    if scope_prefix is not None:
        pred["scope_prefix"] = scope_prefix
    if scope_exclude:
        pred["scope_exclude"] = list(scope_exclude)
    if public_only:
        pred["public_only"] = True

    if inbound_min is not None or inbound_max is not None:
        ic: dict[str, int] = {}
        if inbound_min is not None:
            ic["min"] = inbound_min
        if inbound_max is not None:
            ic["max"] = inbound_max
        pred["inbound_count"] = ic
    if outbound_min is not None or outbound_max is not None:
        oc: dict[str, int] = {}
        if outbound_min is not None:
            oc["min"] = outbound_min
        if outbound_max is not None:
            oc["max"] = outbound_max
        pred["outbound_count"] = oc

    return pred


@app.command("grep")
def grep_cmd(
    ctx: typer.Context,
    name: str | None = typer.Option(
        None,
        "--name",
        "-n",
        help="Substring match against the symbol's local name (case-insensitive).",
    ),
    kind: str | None = typer.Option(
        None,
        "--kind",
        "-k",
        help="Restrict to one of: function, class, method, constant, module, any.",
    ),
    scope_prefix: str | None = typer.Option(
        None,
        "--scope-prefix",
        help="Restrict to symbols whose file path starts with this prefix (e.g. 'trie/').",
    ),
    scope_exclude: list[str] | None = typer.Option(
        None,
        "--scope-exclude",
        help="File-path prefixes to skip. Repeat the flag for multiple exclusions.",
    ),
    public_only: bool = typer.Option(
        False,
        "--public-only",
        help="Restrict to symbols whose name doesn't start with an underscore.",
    ),
    inbound_min: int | None = typer.Option(
        None,
        "--inbound-min",
        help="Minimum inbound edge count (find hubs).",
    ),
    inbound_max: int | None = typer.Option(
        None,
        "--inbound-max",
        help="Maximum inbound edge count.",
    ),
    outbound_min: int | None = typer.Option(
        None,
        "--outbound-min",
        help="Minimum outbound edge count.",
    ),
    outbound_max: int | None = typer.Option(
        None,
        "--outbound-max",
        help="Maximum outbound edge count (find leaves with --outbound-max 0).",
    ),
    predicate_json: str | None = typer.Option(
        None,
        "--predicate",
        help="Full predicate as JSON; identical shape to the MCP `grep` predicate.",
    ),
    rank_by: str | None = typer.Option(
        None,
        "--rank-by",
        help="public_first (default) | inbound_count | alphabetical.",
    ),
    limit: int = typer.Option(
        10,
        "--limit",
        "-l",
        help="Maximum number of hits to return.",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the raw MCP envelope as JSON instead of a human-readable summary.",
    ),
) -> None:
    """Find symbols matching a predicate. Mirror of the MCP `grep` tool.

    Uses the same TrieTools.grep method that the MCP server registers, so the
    `--json` output is byte-equivalent to the MCP wire response. Common
    queries can be expressed with the named flags; for the full predicate
    envelope pass `--predicate '<json>'`.

    Examples:

      trie grep --name compute_cascade --scope-prefix trie/
      trie grep --public-only --rank-by inbound_count --limit 10
      trie grep --predicate '{"name_contains": "store", "kind": "class"}'
    """
    reporter = _get_reporter(ctx)
    pred = _build_grep_predicate(
        name,
        kind,
        scope_prefix,
        scope_exclude,
        public_only,
        inbound_min,
        inbound_max,
        outbound_min,
        outbound_max,
        predicate_json,
        reporter,
    )
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep(pred or None, rank_by=rank_by, limit=limit)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_render_grep)


@app.command("read")
def read_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(
        ...,
        help="Fully-qualified symbol name (e.g. 'trie/sync/cascade:compute_cascade').",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the raw MCP envelope as JSON instead of a human-readable summary.",
    ),
) -> None:
    """Read a symbol's prose plus its immediate callers and callees.

    Mirror of the MCP `read` tool. Use after `trie grep` once you know
    the qname you want to understand. Returns the symbol's signature,
    triefact prose, source pointer, and one-liner descriptions of every
    caller and callee — one round trip for the entire one-hop
    neighbourhood.

    Examples:

      trie read trie/sync/cascade:compute_cascade
      trie read --json trie/graph/store:Store.replace_all_edges
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.read(qname)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_render_read)


@app.command("trace")
def trace_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(
        ...,
        help="Fully-qualified symbol name to start tracing from.",
    ),
    direction: str = typer.Option(
        "callers",
        "--direction",
        "-d",
        help="callers | callees | both.",
    ),
    depth: int = typer.Option(
        2,
        "--depth",
        help="Maximum BFS depth (clamped by trace_max_depth in config).",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the raw MCP envelope as JSON instead of a human-readable summary.",
    ),
) -> None:
    """Trace the call graph from a symbol outward up to `depth` hops.

    Mirror of the MCP `trace` tool. When one hop (which `trie read`
    already gives you) isn't enough, use this to walk farther.
    Expansion stops at hub symbols; their qnames appear in
    `truncated_at`.

    Examples:

      trie trace trie/sync/cascade:compute_cascade --direction callers --depth 2
      trie trace trie/graph/store:Store.replace_all_edges --direction both
      trie trace --json some_qname --direction callees --depth 3
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.trace(qname, direction=direction, depth=depth)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_render_trace)


# ---------------------------------------------------------------------------
# Extended agent tools: grep_str, grep_entry_points, grep_symbol,
# grep_symbol_and_neighbours, explain_symbol, explain_symbol_references,
# trace_flow, explain_flow
# ---------------------------------------------------------------------------


def _print_plain(envelope: dict[str, object], reporter: Reporter) -> None:
    """Generic plain-text renderer for the extended tools.

    Walks the envelope recursively and prints it in a readable form.
    Lists render as bullet items; nested dicts render indented. This keeps
    the CLI output human-readable without requiring a custom renderer per
    tool.
    """
    import json as _json

    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    reporter.console.print(_json.dumps(envelope, indent=2, default=str))


@app.command("grep-str")
def grep_str_cmd(
    ctx: typer.Context,
    regexp: str = typer.Argument(..., help="Regex pattern to search source bodies with."),
) -> None:
    """Search source bodies with a regex; attribute hits to enclosing symbols.

    Example:
      trie grep-str 'raise.*Error'
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep_str(regexp)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("grep-entry-points")
def grep_entry_points_cmd(
    ctx: typer.Context,
    query: str = typer.Argument(..., help="Topic or concept to match against symbol prose."),
) -> None:
    """Find architectural entry points whose triefact prose matches a topic.

    Example:
      trie grep-entry-points 'authentication'
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep_entry_points(query)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("grep-symbol")
def grep_symbol_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."),
) -> None:
    """Fuzzy symbol name lookup: best match + similar symbols.

    Example:
      trie grep-symbol compute_casc
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep_symbol(sym)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("grep-symbol-neighbours")
def grep_symbol_neighbours_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."),
) -> None:
    """Fuzzy symbol lookup + trimmed metadata for immediate callers/callees.

    Example:
      trie grep-symbol-neighbours sync_single_file
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep_symbol_and_neighbours(sym)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("explain-symbol")
def explain_symbol_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol qname or name fragment to explain."),
) -> None:
    """Full prose + joined narrative story of a symbol's references.

    Example:
      trie explain-symbol compute_cascade
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.explain_symbol(sym)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("explain-symbol-refs")
def explain_symbol_refs_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol qname or name fragment."),
) -> None:
    """Explain how a symbol is used — callers only, with their prose.

    Example:
      trie explain-symbol-refs slugify
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.explain_symbol_references(sym)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("trace-flow")
def trace_flow_cmd(
    ctx: typer.Context,
    symbol1: str = typer.Argument(..., help="Starting symbol qname or name."),
    symbol2: str = typer.Argument(..., help="Target symbol qname or name."),
) -> None:
    """Find call chain(s) between two symbols.

    Example:
      trie trace-flow sync_single_file Store.upsert_section_record
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.trace_flow(symbol1, symbol2)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


@app.command("explain-flow")
def explain_flow_cmd(
    ctx: typer.Context,
    symbol1: str = typer.Argument(..., help="Starting symbol qname or name."),
    symbol2: str = typer.Argument(..., help="Target symbol qname or name."),
) -> None:
    """Trace the call chain between two symbols and narrate each step.

    Example:
      trie explain-flow sync_single_file Store.upsert_section_record
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.explain_flow(symbol1, symbol2)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_print_plain)


# ---------------------------------------------------------------------------
# trie patch — fire-and-forget edit notes
# ---------------------------------------------------------------------------


patch_app = typer.Typer(
    name="patch",
    help="Post, preview, apply, list, or drop edit patches against symbols.",
    no_args_is_help=True,
)
app.add_typer(patch_app, name="patch")


class _RichApplyProgress:
    """Rich progress reporter passed as ``progress`` to ``apply_patches``.

    Prints structured lines to the console.  Each stage gets a section
    header; per-file output is indented under that header.  Because
    ``apply_patches`` calls these methods from worker threads, lines from
    different files interleave naturally — the user sees parallelism in
    real time.
    """

    def __init__(self, console: Console, *, verbose: bool = False):
        self.console = console
        self.verbose = verbose

    def stage(self, msg: str) -> None:
        self.console.print(f"[bold cyan]┃ {msg}[/]")

    def file_start(self, fp: str, symbols: int) -> None:
        self.console.print(f"  [dim]→[/dim] [bold]{fp}[/] [dim]({symbols} symbol(s))[/dim]")

    def file_symbol(self, qn: str, notes: list[str]) -> None:
        if not self.verbose:
            return
        self.console.print(f"    [dim]·[/dim] [cyan]{qn}[/]")
        for n in notes:
            short = n[:100].replace("\n", " ")
            self.console.print(f"      [dim]note:[/dim] {short}")

    def file_generate(self) -> None:
        if not self.verbose:
            return

    def file_fixup(self, iteration: int, count: int) -> None:
        self.console.print(
            f"    [yellow]⚙[/yellow] lsp fixup #{iteration} ([dim]{count} diagnostic(s)[/dim])"
        )

    def file_prose(self, qn: str) -> None:
        if not self.verbose:
            return
        self.console.print(f"    [dim]✎[/dim] prose: {qn}")

    def file_done(self, fp: str, ok: bool, error: str | None = None) -> None:
        if ok:
            self.console.print(f"  [green]✓[/green] {fp}")
        else:
            self.console.print(f"  [red]✗[/red] {fp} [red]{error or ''}[/red]")

    def refresh(self, fp: str) -> None:
        self.console.print(f"  [dim]↻[/dim] {fp}")

    def verify(self) -> None:
        self.console.print("  [green]✓[/green] project consistent")


@patch_app.command("create")
def patch_create_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(..., help="Qualified name of the symbol to patch."),
    note: str = typer.Option(..., "--note", "-n", help="Implementation change note."),
    reason: str = typer.Option(
        "", "--reason", "-r", help="Why the cascade needs to know about this change."
    ),
) -> None:
    """Post a fire-and-forget edit patch against a symbol."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    import uuid

    store = Store(project_root / ".trie" / "graph.db")
    try:
        session_id = uuid.uuid4().hex[:12]
        patch_id = store.add_patch(qname, note, reason, session_id)
    except KeyError:
        reporter.error(f"symbol {qname!r} not found in the graph")
        raise typer.Exit(code=1) from None
    finally:
        store.close()

    reporter.success(f"patch #{patch_id} posted for {qname}")


@patch_app.command("apply")
def patch_apply_cmd(
    ctx: typer.Context,
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured edit model for this apply run.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show per-symbol detail during apply.",
    ),
) -> None:
    """Merge all patches, generate source+prose, cascade, and commit."""
    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.edits
    client = make_client(model_id)

    progress = _RichApplyProgress(reporter.console, verbose=verbose)

    store = Store(project_root / ".trie" / "graph.db")
    try:
        result = apply_patches(store, config, client, project_root, progress=progress)
    finally:
        store.close()

    if result["ok"]:
        n = result["total_files"]
        s = result["total_symbols"]
        reporter.success(f"applied {s} symbol(s) across {n} file(s)")
    else:
        reporter.error(
            f"apply failed: {result.get('error', 'unknown')} "
            f"(files: {result.get('total_files', 0)}, "
            f"symbols: {result.get('total_symbols', 0)})"
        )
        raise typer.Exit(code=1)

    reporter.info(reporter.elapsed())


@patch_app.command("preview")
def patch_preview_cmd(ctx: typer.Context) -> None:
    """Show what --apply would do without executing it."""
    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        result = preview_patches(store, config)
    finally:
        store.close()

    if result["total_patches"] == 0:
        reporter.info("no pending patches")
        return

    from rich.table import Table

    table = Table(title="Patch Preview")
    table.add_column("Symbol", style="cyan")
    table.add_column("Patches", style="magenta")
    table.add_column("Cascade", style="yellow")

    for qname in result["patched_list"]:
        cascade_str = "yes" if qname in result.get("cascade_list", []) else "no"
        table.add_row(qname, "1", cascade_str)

    reporter.console.print(table)
    reporter.info(
        f"{result['total_patches']} patches across {result['patched_symbols']} symbols, "
        f"{result['cascade_symbols']} cascaded neighbours"
    )


@patch_app.command("list")
def patch_list_cmd(ctx: typer.Context) -> None:
    """List all pending patches."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        qnames = store.get_patched_qnames()
        if not qnames:
            reporter.info("no pending patches")
            return

        from rich.table import Table

        table = Table(title="Pending Patches")
        table.add_column("QName", style="cyan")
        table.add_column("Patches", style="magenta")

        for qname in qnames:
            patches = store.get_patches_for_qname(qname)
            table.add_row(qname, str(len(patches)))

        reporter.console.print(table)
    finally:
        store.close()


@patch_app.command("drop")
def patch_drop_cmd(
    ctx: typer.Context,
    qname: str | None = typer.Option(
        None, "--qname", "-q", help="Drop patches for a specific symbol."
    ),
    session_id: str | None = typer.Option(
        None, "--session", "-s", help="Drop patches for a specific session."
    ),
    all: bool = typer.Option(False, "--all", "-a", help="Drop all patches."),
) -> None:
    """Drop pending patches for a symbol, session, or everything."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        if qname:
            count = store.delete_patches(qname=qname)
        elif session_id:
            count = store.delete_patches(session_id=session_id)
        elif all:
            count = store.delete_patches(all=True)
        else:
            reporter.error("specify --qname, --session, or --all")
            raise typer.Exit(code=1)
    finally:
        store.close()

    reporter.success(f"dropped {count} patch(es)")


# ---------------------------------------------------------------------------
# mcp serve / mcp install
# ---------------------------------------------------------------------------


mcp_app = typer.Typer(
    name="mcp",
    help=(
        "MCP server: install for an agent (`install`), remove from an agent "
        "(`uninstall`), or serve over stdio (`serve`)."
    ),
    no_args_is_help=True,
)
app.add_typer(mcp_app, name="mcp")


@mcp_app.command("serve")
def mcp_serve() -> None:
    """Run the trie MCP server over stdio (spawned by agents; rarely typed by hand)."""
    _run_mcp_serve()


def _run_mcp_serve() -> None:
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        # Don't print to stdout — that would corrupt the MCP protocol.
        import sys

        print(f"trie mcp: {exc}", file=sys.stderr)
        raise typer.Exit(code=1) from exc
    _ = config  # Config validated; the actual loading happens inside run_mcp_stdio.
    run_mcp_stdio(project_root)


@mcp_app.command("install")
def mcp_install_cmd(
    ctx: typer.Context,
    target: list[str] | None = typer.Option(
        None,
        "--target",
        "-t",
        help=(
            "Install for a specific agent. Repeat the flag for multiple targets. "
            f"Known: {', '.join(MCP_TARGETS)}."
        ),
    ),
    install_all: bool = typer.Option(
        False,
        "--all",
        help="Install for every known target. Skips per-target detection.",
    ),
    scope: str = typer.Option(
        "project",
        "--scope",
        help="Install scope: 'project' (writes into the current project) or 'user' (~/.<agent>/...).",
        case_sensitive=False,
    ),
    print_only: bool = typer.Option(
        False,
        "--print-only",
        help="Print the snippet that would be merged, don't write any files.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Show what would change without writing. Implies the file path resolution but no edit.",
    ),
) -> None:
    """Register `trie mcp serve` as a stdio MCP server with one or more coding agents."""
    reporter = _get_reporter(ctx)

    if target and install_all:
        reporter.error("--target and --all are mutually exclusive")
        raise typer.Exit(code=1)

    scope_norm = scope.lower()
    if scope_norm not in ("project", "user"):
        reporter.error("--scope must be 'project' or 'user'")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc
    _ = config

    try:
        plan = mcp_run_install(
            target_names=target,
            scope=scope_norm,  # type: ignore[arg-type]
            install_all=install_all,
            print_only=print_only,
            dry_run=dry_run,
            project_root=project_root,
        )
    except MCPInstallError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    _render_install_plan(reporter, plan)

    # Non-zero exit if any errors so CI / scripts can react.
    if any(r.action == "error" for r in plan.results):
        raise typer.Exit(code=1)


def _render_install_plan(reporter: Reporter, plan: InstallPlan) -> None:
    import json

    for r in plan.results:
        target_label = MCP_TARGETS[r.target].display_name
        if r.action == "preview":
            reporter.info(f"\n[bold cyan]{target_label}[/bold cyan] → {r.path}")
            reporter.console.print(json.dumps(r.snippet, indent=2))
        elif r.action == "created":
            reporter.success(f"{target_label}: created {r.path}")
        elif r.action == "updated":
            reporter.success(f"{target_label}: updated {r.path}")
        elif r.action == "skipped":
            reporter.info(f"  [dim]⊘[/dim] {target_label}: {r.detail or 'skipped'}")
        elif r.action == "error":
            reporter.error(f"{target_label}: {r.detail}")


@mcp_app.command("uninstall")
def mcp_uninstall_cmd(
    ctx: typer.Context,
    target: list[str] | None = typer.Option(
        None,
        "--target",
        "-t",
        help=(
            "Uninstall from a specific agent. Repeat the flag for multiple targets. "
            f"Known: {', '.join(MCP_TARGETS)}."
        ),
    ),
    uninstall_all: bool = typer.Option(
        False,
        "--all",
        help="Uninstall from every known target. Skips per-target detection.",
    ),
    scope: str = typer.Option(
        "project",
        "--scope",
        help="Uninstall scope: 'project' (the current project's config files) or 'user' (~/.<agent>/...).",
        case_sensitive=False,
    ),
    print_only: bool = typer.Option(
        False,
        "--print-only",
        help="Print what would be removed without writing any files.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Show what would change without writing.",
    ),
) -> None:
    """Remove the trie MCP server registration from one or more coding agents.

    The inverse of `trie mcp install`. Removes the `trie` entry from each
    target's MCP config file and drops the surrounding `mcpServers` (or
    equivalent) key if it becomes empty. Other servers under the same key
    are left untouched. The config file itself is never deleted — agents
    own that file; we only own our entry inside it.
    """
    reporter = _get_reporter(ctx)

    if target and uninstall_all:
        reporter.error("--target and --all are mutually exclusive")
        raise typer.Exit(code=1)

    scope_norm = scope.lower()
    if scope_norm not in ("project", "user"):
        reporter.error("--scope must be 'project' or 'user'")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc
    _ = config

    try:
        plan = mcp_run_uninstall(
            target_names=target,
            scope=scope_norm,  # type: ignore[arg-type]
            uninstall_all=uninstall_all,
            print_only=print_only,
            dry_run=dry_run,
            project_root=project_root,
        )
    except MCPInstallError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    _render_uninstall_plan(reporter, plan)

    if any(r.action == "error" for r in plan.results):
        raise typer.Exit(code=1)


def _render_uninstall_plan(reporter: Reporter, plan: UninstallPlan) -> None:
    """Render the uninstall plan in the same shape as the install renderer.

    Mirrors `_render_install_plan` action-for-action, with `removed`
    swapped in where install reports `created`/`updated`. Skipped cases
    carry a `detail` explaining why (no config file, no trie entry,
    scope unsupported) so the user sees which targets were no-ops.
    """
    import json

    for r in plan.results:
        target_label = MCP_TARGETS[r.target].display_name
        if r.action == "preview":
            reporter.info(f"\n[bold cyan]{target_label}[/bold cyan] → {r.path}")
            reporter.console.print(json.dumps(r.snippet, indent=2))
        elif r.action == "removed":
            reporter.success(f"{target_label}: removed trie entry from {r.path}")
        elif r.action == "skipped":
            reporter.info(f"  [dim]⊘[/dim] {target_label}: {r.detail or 'skipped'}")
        elif r.action == "error":
            reporter.error(f"{target_label}: {r.detail}")


if __name__ == "__main__":
    app()
