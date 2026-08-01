from __future__ import annotations

import os
import sys
import threading
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import replace
from pathlib import Path
from typing import Any

# Before ANY pydantic import in this process: pydantic auto-loads every
# installed plugin (logfire ships one) at `import pydantic` time via entry
# points — ~250ms of telemetry SDK for a CLI that never uses it. setdefault
# so an operator who genuinely wants pydantic plugins can re-enable them.
os.environ.setdefault("PYDANTIC_DISABLE_PLUGINS", "__all__")

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
from trie.edits.pipeline import preview_patches
from trie.freshness import (
    FreshnessResult,
    NotAGitRepoError,
    ensure_fresh_after_turn,
    ensure_fresh_before_turn,
    stamp_graph_fresh,
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
from trie.render import render_envelope
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
from trie.sync.roles import run_roles_only
from trie.sync.single_file import (
    FileSyncResult,
    refresh_triefact_metadata,
    sync_single_file,
)
from trie.sync.taxonomy import taxonomy_path
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


def _cli_session_id(project_root: Path) -> str:
    """Stable patch session id for CLI invocations.

    Reads TRIE_SESSION_ID if set; else a value persisted in activity.db so repeated
    `trie patch ...` calls in one project share a session and `--session` drop works
    (fixes the prior per-invocation-UUID bug). Minted once, then reused.
    """
    import os
    import uuid

    from trie import activity

    env = os.environ.get("TRIE_SESSION_ID")
    if env:
        return env
    existing = activity.get_meta(project_root, "cli_session_id")
    if existing:
        return existing
    sid = uuid.uuid4().hex[:12]
    activity.set_meta(project_root, "cli_session_id", sid)
    return sid


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
        self._lock = threading.Lock()

    def _ensure(self, total: int) -> ProgressHandle:
        with self._lock:
            if self.handle is None:
                self.handle = self.reporter.start_progress(total=total, label=self.label)
                self.handle.__enter__()
            return self.handle

    def close(self) -> None:
        if self.handle is not None:
            self.handle.__exit__(None, None, None)
            self.handle = None

    def on_plan(self, *, direct: int, cascade: int) -> None:
        # Printed once before any file starts. Summarises the worklist split so
        # the operator understands why N files sync when only a few drifted.
        if self.reporter.verbosity < Verbosity.MEDIUM:
            return
        total = direct + cascade
        if total == 0:
            return
        self.reporter.console.print(
            f"[bold]syncing {total} file(s)[/bold]: "
            f"[cyan]{direct} directly stale[/cyan] · "
            f"[magenta]{cascade} pulled in by the cascade[/magenta]"
        )

    def on_section(self, *, label: str, count: int) -> None:
        # A separator + heading printed above the live region before each group
        # of files (directly stale, then cascade) begins.
        if self.reporter.verbosity < Verbosity.MEDIUM or count == 0:
            return
        line = f"\n[dim]── {label} ({count}) ──[/dim]"
        if self.handle is not None:
            self.handle._print(line)
        else:
            self.reporter.console.print(line)

    def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None:
        self._ensure(total).start_file(rel_path, cascade=cascade)

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
def _activity_progress(
    reporter: Reporter, label: str, *, op: str, project_root: Path
) -> Iterator[ProgressCallback]:
    """Like `_progress_callback`, but also mirrors progress into the shared
    `.trie/` activity state (`status.json` + `activity.jsonl`) so any process —
    a terminal sync or the hook — has a live, readable view of
    what this run is doing. The Rich/JSONL reporter and the activity feed both
    fire.
    """
    from trie.activity import ActivityProgress, ActivityWriter

    adapter = _ProgressAdapter(reporter, label)
    writer = ActivityWriter(project_root, op)
    try:
        with writer:
            yield ActivityProgress(writer, inner=adapter)
    finally:
        adapter.close()


class _JsonlProgress:
    """ProgressCallback that emits one JSON object per line to a stream.

    This is the machine-readable counterpart to `_ProgressAdapter`. Hosts that
    drive trie as a subprocess (CI, editor plugins) parse
    these lines to render their own progress UI instead of scraping Rich output.

    Event schema (every line is a complete JSON object with a `kind` field):

      {"kind": "start",   "rel_path": str, "idx": int, "total": int}
      {"kind": "done",    "rel_path": str, "symbols": int, "cost_usd": float,
                          "running_cost_usd": float}
      {"kind": "skip",    "rel_path": str, "reason": str}

    The `phase`/`summary` envelope events are emitted by the command itself
    (see `refresh_cmd`), not here, so the host sees a single ordered stream.

    Lines are flushed immediately so a host reading the pipe sees progress in
    real time rather than at process exit.
    """

    def __init__(self, stream: Any = None):
        self._stream = stream if stream is not None else sys.stdout

    def _emit(self, payload: dict[str, Any]) -> None:
        import json as _json

        self._stream.write(_json.dumps(payload) + "\n")
        self._stream.flush()

    def on_start(self, rel_path: str, idx: int, total: int, *, cascade: bool = False) -> None:
        self._emit(
            {"kind": "start", "rel_path": rel_path, "idx": idx, "total": total, "cascade": cascade}
        )

    def on_done(self, rel_path: str, result: FileSyncResult, running_cost_usd: float) -> None:
        self._emit(
            {
                "kind": "done",
                "rel_path": rel_path,
                "symbols": result.symbols_generated,
                "running_cost_usd": running_cost_usd,
            }
        )

    def on_skip(self, rel_path: str, reason: str) -> None:
        self._emit({"kind": "skip", "rel_path": rel_path, "reason": reason})


def emit_jsonl_event(payload: dict[str, Any], stream: Any = None) -> None:
    """Emit a single envelope JSONL event (phase markers, summaries, errors).

    Used by commands running in `--json` mode to bracket the per-file events
    from `_JsonlProgress` with lifecycle markers the host can key on.
    """
    import json as _json

    out = stream if stream is not None else sys.stdout
    out.write(_json.dumps(payload) + "\n")
    out.flush()


@contextmanager
def _acquire_write_lock_or_exit(
    project_root: Path, reporter: Reporter, command_name: str
) -> Iterator[None]:
    """Hold the refresh lock for the duration of a write-side command, or exit
    with a clear message if another process already holds it.

    The lock is shared with the hook-driven `trie sync --graph-only` and with any
    other write-side trie command in the same checkout. The hook's graph-sync path
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
    offline: bool = typer.Option(
        False,
        "--offline",
        help=(
            "Skip the count_tokens cost preview (the only network calls plan makes). "
            "Shows the worklist with symbol counts; estimates read $0."
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
    if offline:
        # count_tokens is plan's only network dependency; a zero-token stub
        # keeps the worklist available with no key and no connectivity.
        class _OfflineTokenStub:
            def count_tokens(self, *args: object, **kwargs: object) -> int:
                return 0

        client = _OfflineTokenStub()  # type: ignore[assignment]
        reporter.info("[dim]--offline: cost estimates skipped (worklist only)[/dim]")
    else:
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
    (section body was hand-edited between sentinels, or section refers to a deleted symbol).

    No LLM, no scan, no DB writes — designed for pre-commit hooks. The same drift
    detection runs as the first step of `trie plan` and `trie sync`; `verify` exists
    so CI / hooks can fail loudly when the tree drifts.
    """
    reporter = _get_reporter(ctx)
    _verify_drift(reporter, exit_on_drift=True)


@app.command("status")
def status_cmd(
    ctx: typer.Context,
    as_json: bool = typer.Option(
        False, "--json", help="Emit the status as a single JSON object instead of prose."
    ),
) -> None:
    """Show trie's working state — like `git status` for the triefact tree.

    Reports:
      • the active writer (idle, or a running sync with live progress),
      • the stale triefacts a `trie sync` would regenerate — computed from the
        same offline content-drift check `trie verify` uses (source body
        fingerprints vs. triefact sentinels), so it's authoritative, not a cached
        guess. The pending set recorded by graph-only syncs is unioned in.

    Read-only and fast: a content-drift scan (no LLM, no DB writes). Safe to run
    while a sync is in flight — it reflects that sync's live progress.
    """
    import json as _json

    from trie.activity import read_pending, read_status
    from trie.check import check_project

    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    status = read_status(project_root)

    # Authoritative drift via the same `check_project` call `trie verify` uses —
    # status reports exactly what verify would, never an independent computation.
    # The store is a content-addressed cache here (fingerprint-gated), not an
    # authority — it spares the tree-sitter+LSP parse for unchanged files.
    with Store(project_root / ".trie" / "graph.db") as _check_store:
        check = check_project(project_root=project_root, config=config, store=_check_store)
    drift_by_file: dict[str, int] = {}
    for it in check.items:
        drift_by_file[it.source_path] = drift_by_file.get(it.source_path, 0) + 1

    # Union with the recorded pending set (a graph-only sync may have
    # flagged cascade files whose own bodies didn't change but whose neighbours did).
    pending = read_pending(project_root)
    stale_set = set(drift_by_file) | set(pending.stale if pending else ())
    stale = sorted(stale_set)

    # Pending edit patches (durable, from graph.db) — the shared patch_summary reader.
    patch_summary: dict[str, object] = {
        "total_patches": 0,
        "symbol_count": 0,
        "create_count": 0,
        "by_origin": {},
    }
    try:
        _pstore = Store(project_root / ".trie" / "graph.db")
        try:
            patch_summary = _pstore.patch_summary()
        finally:
            _pstore.close()
    except Exception:
        pass

    if as_json:
        typer.echo(
            _json.dumps(
                {
                    "state": status.state,
                    "op": status.op,
                    "pid": status.pid,
                    "current_file": status.current_file,
                    "done": status.done,
                    "total": status.total,
                    "stale_count": len(stale),
                    "stale": stale,
                    "drift_items": len(check.items),
                    "patches": patch_summary,
                },
                default=str,
            )
        )
        return

    # Writer line.
    if status.is_active:
        prog = f" {status.done}/{status.total}" if status.total else ""
        cur = f" · {status.current_file}" if status.current_file else ""
        reporter.console.print(f"[cyan]●[/cyan] {status.op or status.state}{prog}{cur}")
    elif status.state == "error":
        reporter.console.print(f"[red]✗[/red] last run errored: {status.error or 'unknown'}")
    else:
        reporter.console.print("[green]●[/green] idle")

    # Stale set.
    if stale:
        reporter.console.print(
            f"\n[yellow]{len(stale)} triefact(s) stale[/yellow] "
            f"({len(check.items)} drifted section(s)) — run `trie sync` to regenerate:"
        )
        for f in stale[:20]:
            n = drift_by_file.get(f)
            suffix = f" [dim]({n} section{'s' if n != 1 else ''})[/dim]" if n else ""
            reporter.console.print(f"  [yellow]~[/yellow] {f}{suffix}")
        if len(stale) > 20:
            reporter.console.print(f"  … and {len(stale) - 20} more")

    # Pending edit patches.
    def _as_int(v: object) -> int:
        return int(v) if isinstance(v, int) else 0

    total_patches = _as_int(patch_summary.get("total_patches", 0))
    create_count = _as_int(patch_summary.get("create_count", 0))
    sym_count = _as_int(patch_summary.get("symbol_count", 0))
    if total_patches or create_count:
        bits = []
        if total_patches:
            bits.append(f"{total_patches} patch(es) across {sym_count} symbol(s)")
        if create_count:
            bits.append(f"{create_count} pending create(s)")
        reporter.console.print(
            f"\n[magenta]◐ {' · '.join(bits)}[/magenta] — run `trie patch apply` to commit"
        )


@app.command("lock-check")
def lock_check_cmd(ctx: typer.Context) -> None:
    """Probe whether another trie process holds the project's write lock.

    Designed for the pre-commit hook: if a `trie sync` is
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


def _run_graph_only_sync(reporter: Reporter, *, as_json: bool, before_turn: bool) -> None:
    """`trie sync --graph-only`: rebuild the graph + stamp freshness, never the LLM.

    This is the hook-facing half of sync (formerly the `trie refresh` command).
    Agent harnesses register it as a turn hook:

      • `trie sync --graph-only --before-turn`: cheap pre-turn freshness gate.
      • `trie sync --graph-only --after-turn`: post-turn sweep picking up the
        agent's own edits (the default turn mode).

    Guaranteed free: no LLM call, no API key needed. Prose drift is recorded
    in the pending set and reported; a plain `trie sync` regenerates it.
    Fails loudly outside a git repo: the gate's correctness depends on
    `git rev-parse HEAD` succeeding.
    """
    # In --json mode the Rich progress bar and success lines would interleave
    # with the JSONL stream and corrupt it. Mute the reporter so stdout carries
    # only well-formed JSON events; errors still emit as {"kind": "error"}.
    if as_json:
        reporter.verbosity = Verbosity.MUTE

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        if as_json:
            emit_jsonl_event({"kind": "error", "message": str(exc)})
        else:
            reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    db_path = project_root / ".trie" / "graph.db"

    runner = ensure_fresh_before_turn if before_turn else ensure_fresh_after_turn
    mode_label = "before-turn" if before_turn else "after-turn"

    if as_json:
        emit_jsonl_event({"kind": "phase", "phase": "graph-sync", "mode": mode_label})

    # Graph-only sync runs as a per-turn hook, so two agent turns in quick
    # succession can fire two processes that race the SQLite store and the
    # triefact tree. The lock serialises them; the queued sentinel coalesces
    # N rapid contests down to "one current run + at most one tail run" so we
    # don't fan out an unbounded chain. (Full sync uses the same lock but
    # exits 2 on contention instead — operators deserve a loud failure,
    # hooks deserve quiet coalescing.)
    with try_acquire_refresh_lock(project_root) as holder:
        if not holder.acquired:
            holder.mark_queued()
            telemetry.emit(
                "refresh_lock_contended",
                project_root=str(project_root),
                mode=mode_label,
                action="queued",
            )
            if as_json:
                emit_jsonl_event(
                    {"kind": "summary", "refreshed": False, "reason": "queued", "mode": mode_label}
                )
            else:
                reporter.success(
                    f"{mode_label}: another graph sync is running; queued for tail pass."
                )
            return

        with (
            Store(db_path) as store,
            _graph_sync_progress(reporter, as_json, project_root=project_root) as cb,
        ):
            try:
                result = runner(
                    project_root=project_root,
                    config=config,
                    store=store,
                    progress=cb,
                )
            except NotAGitRepoError as exc:
                if as_json:
                    emit_jsonl_event({"kind": "error", "message": str(exc)})
                else:
                    reporter.error(str(exc))
                raise typer.Exit(code=1) from exc
            if as_json:
                _emit_freshness_json(result, mode=mode_label)
            else:
                _report_freshness(reporter, result, mode=mode_label)

            # Tail pass: at most one extra run, coalescing every request
            # that arrived while we held the lock. We deliberately don't
            # loop further — if more requests pile up during the tail
            # itself, the next hook invocation handles them.
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
                    progress=cb,
                )
                if as_json:
                    _emit_freshness_json(tail, mode=f"{mode_label} (tail)")
                else:
                    _report_freshness(reporter, tail, mode=f"{mode_label} (tail)")


@contextmanager
def _graph_sync_progress(
    reporter: Reporter, as_json: bool, *, project_root: Path
) -> Iterator[ProgressCallback]:
    """Pick the progress sink for a graph-only sync run, mirroring into the shared
    `.trie/` activity state either way.

    `--json` routes per-file events through `_JsonlProgress` (one JSON object
    per line on stdout); otherwise the Rich-backed `_ProgressAdapter` renders a
    live bar. Both are wrapped so `status.json` + `activity.jsonl` reflect the
    run for `trie status` and the editor.
    """
    from trie.activity import ActivityProgress, ActivityWriter

    writer = ActivityWriter(project_root, "refresh")
    inner: ProgressCallback
    with writer:
        if as_json:
            yield ActivityProgress(writer, inner=_JsonlProgress())
        else:
            with _progress_callback(reporter, label="refreshing") as cb:
                inner = cb
                yield ActivityProgress(writer, inner=inner)


def _emit_freshness_json(result: FreshnessResult, *, mode: str) -> None:
    """Emit the terminal `summary` JSONL event for a graph-sync outcome.

    Mirrors `_report_freshness` but as a structured event subprocess hosts key
    on to close out its status display.
    """
    emit_jsonl_event(
        {
            "kind": "summary",
            "mode": mode,
            "refreshed": result.refreshed,
            "reason": result.reason,
            "stale_files": list(result.stale_files),
        }
    )


def _report_freshness(reporter: Reporter, result: FreshnessResult, *, mode: str) -> None:
    """Render one line per graph-sync outcome, always in two clauses: graph and prose.

    A fresh graph must never be reported as plain "fresh" while prose lags —
    that phrasing shipped commit failures where the hook said "already fresh"
    and the pre-commit gate immediately found stale triefacts. The prose clause
    is sourced from `FreshnessResult.stale_files` (the pending set), which is
    populated on every outcome including `unchanged`.
    """
    graph = f"graph synced ({result.reason})" if result.refreshed else "graph fresh"
    n = len(result.stale_files)
    if n:
        reporter.warn(f"{mode}: {graph}; prose stale in {n} file(s) — run `trie sync`")
    else:
        reporter.success(f"{mode}: {graph}; prose fresh")


_AUDIT_TAIL_BYTES = 4 * 1024 * 1024
"""Default read window for `trie audit`: ~4MB of trailing JSONL ≈ the recent
sessions. Full-history parsing of a months-old log (28MB+) made audit the
slowest read command; `--all` restores it."""


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
    all_history: bool = typer.Option(
        False,
        "--all",
        help=(
            "Parse the entire log instead of the recent tail. The default reads "
            "the last ~4MB (roughly the recent sessions) so the command stays "
            "fast on long-lived projects whose logs run to tens of MB."
        ),
    ),
) -> None:
    """Summarise a telemetry log: MCP usage, sync activity, retries, CLI invocations.

    Reads the `debug.jsonl` produced by trie's telemetry layer (see `[debug]` in
    `trie.toml`) and prints a compressed view of what happened during the run.
    By default only the recent tail of the log is parsed (pass --all for the
    full history). With `--compare`, two logs are rendered side-by-side with
    deltas — the primary use case is comparing `with_trie` vs `without_trie`
    eval runs of an agent on the same task; comparisons always read fully.

    No state is read or written beyond the log file(s); safe to run after the
    fact on archived logs.
    """
    reporter = _get_reporter(ctx)

    if compare is not None and as_json:
        reporter.error("--compare and --json are mutually exclusive")
        raise typer.Exit(code=1)

    # Comparisons summarise whole runs; the tail default is for the
    # interactive "what just happened?" case.
    tail = None if (all_history or compare is not None) else _AUDIT_TAIL_BYTES

    log_path = _resolve_audit_log_path(log, reporter)
    try:
        baseline = AuditSummary.from_log(log_path, tail_bytes=tail)
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


def _run_intent_gate(reporter: Reporter, config: Config, project_root: Path) -> bool:
    """Run the intent gate and render the outcome. Returns True when covered.

    Shared by `trie intent` and `trie gate` so hook-driven and hook-less (CI)
    environments enforce the identical contract.
    """
    from trie.intent_gate import evaluate

    store = Store(project_root / ".trie" / "graph.db")
    try:
        report = evaluate(project_root, config, store)
    finally:
        store.close()

    if not report.touched:
        reporter.success("intent gate: no symbol-level changes vs HEAD")
        return True
    if report.ok:
        reporter.success(
            f"intent gate: all {len(report.touched)} touched symbol(s) have notes on record"
        )
        return True

    reporter.error(
        f"intent gate: {len(report.uncovered)} of {len(report.touched)} touched "
        "symbol(s) have no patch note — every change must record its intent"
    )
    for t in report.uncovered:
        reporter.console.print(f"  [yellow]{t.status:<8}[/yellow] {t.qname}")
    reporter.console.print()
    reporter.console.print("stage a note per symbol, then re-run:")
    for t in report.uncovered[:3]:
        suffix = " --gone" if t.status == "removed" else ""
        reporter.console.print(f'  trie patch create {t.qname} -n "<why this changed>"{suffix}')
    if len(report.uncovered) > 3:
        reporter.console.print(f"  … and {len(report.uncovered) - 3} more")
    reporter.console.print(
        'then: trie patch apply -N "<session intent>"   (records notes; no code generation)'
    )
    reporter.console.print(
        "(agent harnesses: stage via the patch / batch_patch tools, then patch_apply)"
    )
    return False


def _warn_on_version_skew(reporter: Reporter, project_root: Path) -> None:
    """Warn when the running trie binary is a different version than this checkout's
    trie source package (the self-hosting case).

    Hooks and generated tools resolve `trie` from PATH; after editing trie's own
    interface the globally installed tool lags the checkout until reinstalled,
    which once shipped a whole commit whose digest was written by the previous
    release. Cheap probe: only fires when `pyproject.toml` at the project root
    names the `trie` package itself. Advisory — never blocks.
    """
    from trie import __version__

    pyproject = project_root / "pyproject.toml"
    if not pyproject.exists():
        return
    try:
        import tomllib

        data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    except Exception:
        return
    project = data.get("project") or {}
    if project.get("name") != "trie":
        return
    repo_version = str(project.get("version", ""))
    if repo_version and repo_version != __version__:
        reporter.warn(
            f"running trie {__version__} but this checkout is {repo_version} — "
            "reinstall with `uv tool install --force --reinstall .` so hooks "
            "and tools run the code you just changed"
        )


@app.command("gate")
def gate_cmd(
    ctx: typer.Context,
    no_digest: bool = typer.Option(
        False,
        "--no-digest",
        help="Skip the digest write (gates only: lock + verify + intent).",
    ),
) -> None:
    """The commit guard, as one command: lock-check + verify + intent + digest.

    This is exactly what the pre-commit hook runs. Call it explicitly in
    environments where git hooks don't exist or don't fire — CI runners,
    agents committing from GitHub Actions, bare automation:

        trie sync --graph-only   # cold runner: rebuild the graph first (no LLM)
        ...work...
        trie gate                # before git commit

    Exit codes: 0 all gates pass (digest is advisory and never blocks),
    1 verify or intent failed (output says exactly what to fix),
    2 another trie writer holds the lock (retry when it finishes).
    A repo without trie.toml exits 0 — nothing to guard.
    """
    reporter = _get_reporter(ctx)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError:
        reporter.info("no trie.toml here — nothing to gate")
        return

    # 0. Version visibility: hooks resolve `trie` from PATH, so a stale global
    # install can silently run old gate logic against a newer checkout. Print
    # the running version, and when this project *is* the trie source repo at
    # a different version, warn loudly — that skew shipped confusing gate
    # behaviour before it was made visible.
    _warn_on_version_skew(reporter, project_root)

    # 1. Lock: never commit while a writer is mid-flight.
    from trie.refresh_lock import try_acquire

    with try_acquire(project_root, name="gate") as holder:
        if not holder.acquired:
            reporter.error("another trie process is writing (a sync is in flight) — retry shortly")
            raise typer.Exit(code=2)

    # 2. Verify: prose must match source, both directions.
    if not _verify_drift(reporter, exit_on_drift=False):
        reporter.info("fix: run `trie sync`, then retry")
        raise typer.Exit(code=1)

    # 3. Intent: every changed symbol carries a note.
    if not _run_intent_gate(reporter, config, project_root):
        raise typer.Exit(code=1)

    # 4. Digest: advisory — record the commit's story and stage it.
    if not no_digest:
        _run_digest_write(reporter, config, project_root, stage=True)


@app.command("intent")
def intent_cmd(ctx: typer.Context) -> None:
    """Gate: every changed symbol must carry a patch note (its intent).

    Compares the working tree against HEAD at the normalized-body level (so
    formatting and line shifts never gate), then checks each touched symbol
    has intent on record — a pending patch note or an applied session-log row
    from this commit window. Exits 1 with a copy-pasteable worklist when
    coverage is missing. Runs in the pre-commit hook between `verify` and the
    digest write; agents clear it with `trie patch create <qname> -n "<why>"`.
    """
    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    if not _run_intent_gate(reporter, config, project_root):
        raise typer.Exit(code=1)


@app.command("index")
def index_cmd(ctx: typer.Context) -> None:
    """Regenerate the triefact-tree index (<triefacts.root>/README.md).

    Deterministic and LLM-free: entry points ranked by inbound references plus
    a per-directory table of contents with file descriptions. Runs automatically
    at the end of every sync; this command exists for manual refreshes.
    """
    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    from trie.index import write_index

    store = Store(project_root / ".trie" / "graph.db")
    try:
        path = write_index(store=store, config=config, project_root=project_root)
    finally:
        store.close()
    if path is None:
        reporter.info("no triefact tree yet — run `trie sync` first")
        return
    reporter.success(f"index written to {path.relative_to(project_root)}")


@app.command("diff")
def diff_cmd(
    ctx: typer.Context,
    base: str = typer.Option("HEAD", "--base", help="Git ref to diff the triefact tree against."),
    raw: bool = typer.Option(
        False,
        "--raw",
        help="Skip LLM synthesis; print patch notes and the raw triefact diff.",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the collected evidence as JSON (no LLM call). Mutually exclusive with --raw.",
    ),
    model: str | None = typer.Option(
        None, "--model", help="Override the model used for narrative synthesis."
    ),
    write: bool = typer.Option(
        False,
        "--write",
        help="Prepend a digest entry to the TRIE_DIFF file (config diff.write_path) and exit; used by the pre-commit hook.",
    ),
) -> None:
    """Describe what changed in a session at the intent level.

    Combines the raw git diff of the triefact tree with the patch notes recorded
    when edits were staged (applied notes from the session log, pending notes from
    the patch queue) and synthesises a coherent narrative via the LLM.  Use --raw
    or --json to inspect the underlying evidence without paying for synthesis.
    Pass --write to prepend a digest entry to the configured TRIE_DIFF file instead
    of rendering to the terminal; this is the mode used by the pre-commit hook.
    """
    reporter = _get_reporter(ctx)

    if raw and as_json:
        reporter.error("--raw and --json are mutually exclusive")
        raise typer.Exit(code=1)

    if write and as_json:
        reporter.error("--write and --json are mutually exclusive")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    from trie.session_diff import (
        collect_session_diff,
        synthesize_narrative,
    )

    if write:
        _run_digest_write(
            reporter,
            config,
            project_root,
            base=base,
            raw=raw,
            model=model,
        )
        return

    # ------------------------------------------------------------------ #
    # Terminal rendering modes                                             #
    # ------------------------------------------------------------------ #

    store = Store(project_root / ".trie" / "graph.db")
    try:
        data = collect_session_diff(project_root, config, store, base=base)
    finally:
        store.close()

    if data.is_empty():
        reporter.info("no session changes detected (no triefact diff, no patch notes)")
        return

    console = reporter.console

    if as_json:
        import json as _json

        typer.echo(
            _json.dumps(
                {
                    "base": data.base,
                    "session_ids": data.session_ids(),
                    "triefact_diff": data.triefact_diff,
                    "applied": data.applied,
                    "pending": data.pending,
                },
                indent=2,
                default=str,
            )
        )
        return

    if raw:
        console.print("[bold]Applied patch notes[/bold]")
        for entry in data.applied:
            notes_text = (
                "; ".join(entry.get("notes") or []) if entry.get("notes") else "[dim](none)[/dim]"
            )
            op = entry.get("op", "?")
            qname = entry.get("qname", "?")
            console.print(f"  [green]✓[/green] [{op}] {qname} — {notes_text}")

        console.print("[bold]Pending patch notes[/bold]")
        for entry in data.pending:
            note_val = entry.get("note", "")
            notes_text = note_val if note_val else "[dim](none)[/dim]"
            op = entry.get("op", "?")
            qname = entry.get("qname", "?")
            console.print(f"  [yellow]○[/yellow] [{op}] {qname} — {notes_text}")

        if data.triefact_diff.strip():
            console.print("[bold]Raw triefact diff[/bold]")
            console.print(data.triefact_diff, highlight=False, markup=False)

        return

    # Default path: LLM narrative synthesis
    client = make_client(model or config.models.cascade, sync_cfg=config.sync)
    with console.status("synthesising session narrative..."):
        narrative = synthesize_narrative(data, client)

    from rich.markdown import Markdown

    console.print(Markdown(narrative.as_markdown()))
    console.print(
        f"[dim]{len(data.applied)} applied, {len(data.pending)} pending patch note(s);"
        f" diff vs {data.base}[/dim]"
    )


def _run_digest_write(
    reporter: Reporter,
    config: Config,
    project_root: Path,
    *,
    base: str = "HEAD",
    raw: bool = False,
    model: str | None = None,
    stage: bool = False,
) -> bool:
    """Write this session's digest entry (the `trie diff --write` body).

    Shared by `diff_cmd` and `trie gate` so hook-driven and hook-less (CI)
    environments run identical logic. Evidence is consumption-based — the
    pending-intent file plus the staging queue — so there are no timestamp
    windows and no cursor state. On success the pending-intent file is
    consumed (its rows now live in the digest entry, which is committed).

    Amend/retry: if a digest file for the same parent commit already exists,
    its recorded rows are folded back into the evidence and the file is
    rewritten in place rather than duplicated.

    Advisory by design: returns True when a digest was written or there was
    nothing to record, False only on hard failure. `stage=True` additionally
    `git add`s the archive dir and the latest-symlink so an in-flight commit
    picks up both the new digest and the consumed pending file.
    """
    from datetime import datetime

    from trie.git_helpers import current_head
    from trie.session_diff import (
        _one_line,
        collect_session_diff,
        collect_symbol_deltas,
        iter_digest_entries,
        render_digest_section,
        rows_from_digest_entry,
        synthesize_narrative,
        write_digest,
    )

    # 1. Resolve parent commit identity
    parent_sha = current_head(project_root)
    if parent_sha is None:
        parent_sha = base
    parent_short = parent_sha[:12]

    # 2. Amend/retry detection: an existing digest entry for the same parent
    #    is rewritten in place, with its rows folded back into the evidence.
    reuse_file: str | None = None
    prior_rows: list[dict] = []
    for entry in iter_digest_entries(project_root, diffs_dir=config.diff.diffs_dir):
        if entry.get("parent", "").startswith(parent_short):
            reuse_file = f"{config.diff.diffs_dir}/{entry['name']}"
            prior_rows = rows_from_digest_entry(entry)
            break

    # 3. Collect session evidence
    store = Store(project_root / ".trie" / "graph.db")
    try:
        data = collect_session_diff(project_root, config, store, base=base)
    finally:
        store.close()

    if prior_rows:
        data = replace(data, applied=prior_rows + data.applied)

    if data.is_empty():
        reporter.info("no session changes; digest not updated")
        return True

    # 4. Collect semantic symbol deltas
    deltas = collect_symbol_deltas(project_root, config, base=base)

    # 5. Derive a human title from the first non-empty session note
    # (the per-apply unifying intent — NOT the per-symbol patch notes)
    title: str | None = None
    for entry in data.applied:
        candidate = _one_line(entry.get("session_note", ""), max_chars=80)
        if candidate:
            title = candidate
            break
    if not title:
        title = "Session changes"

    # 6. Optionally synthesize an LLM narrative
    narrative = ""
    if getattr(config.diff, "narrative", True) and not raw:
        try:
            client = make_client(model or config.models.cascade, sync_cfg=config.sync)
            narrative = synthesize_narrative(data, client).as_markdown()
        except Exception:
            narrative = ""

    # 7. Render and write the digest section
    date_str = datetime.now().strftime("%Y-%m-%d")
    section = render_digest_section(
        data,
        title=title,
        date_str=date_str,
        parent_short=parent_short,
        narrative=narrative,
        deltas=deltas,
    )

    try:
        written_file = write_digest(
            project_root,
            section,
            diffs_dir=config.diff.diffs_dir,
            symlink_path=config.diff.write_path,
            max_entries=config.diff.max_entries,
            reuse_file=reuse_file,
        )
    except OSError as exc:
        reporter.error(f"digest write failed: {exc}")
        return False

    # 8. The sealed rows now live in a digest entry — consume them.
    store = Store(project_root / ".trie" / "graph.db")
    try:
        store.delete_applied_patches()
    finally:
        store.close()

    backed_by = "narrative" if narrative else "raw evidence"
    reporter.info(
        f"digest written to {written_file} ({backed_by}); {config.diff.write_path} -> latest"
    )

    if stage:
        from trie.git_helpers import _run_git

        _run_git(
            ["add", "-A", "--", config.diff.write_path, config.diff.diffs_dir],
            cwd=project_root,
        )
    return True


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
    StaleReason.TAMPERED_BODY: "hand-edited inside a generated section — move your prose OUTSIDE the sentinels (trie preserves it there), then run `trie sync`",
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

    # Store as content-addressed parse cache (fingerprint-gated; see
    # check_project docstring) — keeps verify/gate under the 300ms budget.
    with Store(project_root / ".trie" / "graph.db") as _check_store:
        result = check_project(project_root=project_root, config=config, store=_check_store)

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
    graph_only: bool = typer.Option(
        False,
        "--graph-only",
        help=(
            "Rebuild the symbol graph and freshness stamp from source without "
            "calling the LLM. Free and fast; drifted prose is marked stale for "
            "a later full `trie sync`. This is what turn hooks run."
        ),
    ),
    before_turn: bool = typer.Option(
        False,
        "--before-turn",
        help=(
            "Hook mode (implies --graph-only): cheap pre-turn freshness gate — "
            "no-op when nothing changed since the last graph sync."
        ),
    ),
    after_turn: bool = typer.Option(
        False,
        "--after-turn",
        help=(
            "Hook mode (implies --graph-only): post-turn sweep that picks up the "
            "agent's own edits. Default turn mode for --graph-only."
        ),
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help=(
            "With --graph-only: emit machine-readable JSON-Lines progress to "
            'stdout instead of Rich output. Each line is one event ({"kind": ...}).'
        ),
    ),
    file: Path | None = typer.Option(
        None,
        "--file",
        "-f",
        help=(
            "Sync exactly one source file. Regenerates only its stale symbols by "
            "default; combine with --force for a full fresh rewrite."
        ),
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
    roles_only: bool = typer.Option(
        False,
        "--roles-only",
        help=(
            "(Re)infer only the architectural role tag for every symbol against a "
            "project-specific role vocabulary, without regenerating prose. Derives "
            "the vocabulary first if none exists. Cheap relative to a full sync."
        ),
    ),
    rederive_taxonomy: bool = typer.Option(
        False,
        "--rederive-taxonomy",
        help=(
            "With --roles-only, re-derive the role vocabulary from scratch even if one "
            "is already saved. Use after large architectural change."
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
    """Bring the graph and triefacts up to date with the working tree.

    Modes (auto-detected):
      • --graph-only    : rebuild graph + freshness stamp; never the LLM. Turn
                          hooks run `trie sync --graph-only --after-turn`.
      • --file          : sync one file (stale symbols only; --force for all).
      • --dry-run       : preview unified diff against the live tree.
      • --metadata-only : refresh front matter only; no LLM, no section changes.
      • --all           : force full re-pass.
      • default         : if no triefacts exist yet → first-run bootstrap;
                          otherwise → incremental cascade.

    Drift detection runs as the first step regardless. For an LLM-free, exit-coded
    drift gate suitable for pre-commit hooks, use `trie verify`.
    """
    reporter = _get_reporter(ctx)

    # Turn flags imply --graph-only: a turn hook must never spend.
    if before_turn and after_turn:
        reporter.error("--before-turn and --after-turn are mutually exclusive")
        raise typer.Exit(code=1)
    graph_only = graph_only or before_turn or after_turn
    if graph_only:
        incompatible = {
            "--file": file is not None,
            "--all": all_,
            "--budget": budget is not None,
            "--limit": limit is not None,
            "--dry-run": dry_run,
            "--metadata-only": metadata_only,
            "--roles-only": roles_only,
            "--rederive-taxonomy": rederive_taxonomy,
            "--force": force,
            "--model": model is not None,
        }
        offending = [flag for flag, given in incompatible.items() if given]
        if offending:
            reporter.error(
                f"--graph-only never calls the LLM and cannot be combined with "
                f"{', '.join(offending)}"
            )
            raise typer.Exit(code=1)
        _run_graph_only_sync(reporter, as_json=as_json, before_turn=before_turn)
        return
    if as_json:
        reporter.error("--json requires --graph-only")
        raise typer.Exit(code=1)

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
    if roles_only and (file is not None or all_ or dry_run or metadata_only):
        reporter.error(
            "--roles-only cannot be combined with --file / --all / --dry-run / --metadata-only"
        )
        raise typer.Exit(code=1)
    if rederive_taxonomy and not roles_only:
        reporter.error("--rederive-taxonomy requires --roles-only")
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

        if roles_only:
            _run_roles_only_sync(reporter, model=model, rederive_taxonomy=rederive_taxonomy)
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

        with _activity_progress(
            reporter, label="syncing", op="bootstrap", project_root=project_root
        ) as cb:
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
        if result.files_synced:
            _refresh_index_quietly(config, project_root, store)

    # Bootstrap began with a whole-project scan: the graph is current with
    # disk regardless of how much prose the budget allowed. Stamp it so the
    # next graph-only sync no-ops.
    stamp_graph_fresh(project_root, config)

    had_errors = _report_sync_errors(reporter, result.file_errors)
    reporter.success(
        f"synced {result.files_synced} files "
        f"(skipped {result.files_skipped_no_budget} due to budget/limit)"
    )
    reporter.info(
        f"  estimated ${result.estimated_cost_usd:.4f} · actual ${result.actual_cost_usd:.4f}"
    )
    if had_errors:
        raise typer.Exit(code=1)


def _refresh_index_quietly(config: Config, project_root: Path, store: Store) -> None:
    """Regenerate the triefact index after a sync; advisory, never fails the run."""
    try:
        from trie.index import write_index

        write_index(store=store, config=config, project_root=project_root)
    except Exception:
        pass


def _report_sync_errors(reporter: Reporter, file_errors: list[tuple[str, str]]) -> bool:
    """Report per-file generation failures. Returns True when any occurred.

    Sync must never green-lie: a run where files errored (missing API key,
    network failure, provider errors) is not a success even though the wave
    scheduler correctly kept going. Shows up to 5 errors plus a count, and a
    targeted hint when the failure smells like missing credentials.
    """
    if not file_errors:
        return False
    shown = file_errors[:5]
    for rel, err in shown:
        reporter.error(f"✗ {rel}: {err}")
    if len(file_errors) > len(shown):
        reporter.error(f"  … and {len(file_errors) - len(shown)} more file(s) failed")
    blob = " ".join(err.lower() for _, err in file_errors)
    if "api_key" in blob or "api key" in blob or "authentication" in blob or "x-api-key" in blob:
        reporter.info(
            "hint: no usable model credentials — set ANTHROPIC_API_KEY (or the key for "
            "your configured provider) and re-run `trie sync`"
        )
    return True


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
    """`trie sync --file X`: regenerate one file's triefact, stale symbols only.

    By default the LLM is called only for symbols whose section fingerprints
    lag their source (per `check_project`, the same classifier the pre-commit
    gate uses); fresh sections pass through byte-identically. A file that has
    never been synced (missing triefact) gets a full cold write. `--force`
    regenerates every symbol from scratch — the smoke-test / known-bad-prose
    path. Nothing stale and no --force → report and exit without an LLM call.
    """
    if not file.exists():
        reporter.error(f"{file} does not exist")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(file.parent)
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    symbols_to_regen: set[str] | None = None
    if not force:
        src_root = (project_root / config.triefacts.source_root).resolve()
        try:
            rel_source = str(file.resolve().relative_to(src_root))
        except ValueError:
            reporter.error(f"{file} is outside the configured source root ({src_root})")
            raise typer.Exit(code=1) from None
        with Store(project_root / ".trie" / "graph.db") as _check_store:
            check = check_project(project_root=project_root, config=config, store=_check_store)
        file_items = [it for it in check.items if it.source_path == rel_source]
        if not file_items:
            reporter.success(f"{rel_source}: all symbols fresh — nothing to do")
            reporter.info("  use --force to rewrite every symbol from scratch")
            return
        if not any(it.qualified_name is None for it in file_items):
            # Symbol-level staleness only: regenerate exactly those, pass the
            # rest through byte-identically. A missing-triefact item (qname
            # None) keeps symbols_to_regen=None for a full cold write.
            symbols_to_regen = {
                it.qualified_name for it in file_items if it.qualified_name is not None
            }

    model_id = model or config.models.bootstrap
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    with (
        Store(db_path) as store,
        reporter.status(f"generating triefact for [cyan]{file}[/cyan]…"),
    ):
        result = sync_single_file(
            file,
            project_root=project_root,
            config=config,
            client=client,
            store=store,
            symbols_to_regen=symbols_to_regen,
            force=force,
        )

    reporter.success(f"wrote {result.triefact_path}")
    passed_through = (
        f", {result.symbols_skipped} fresh passed through" if result.symbols_skipped else ""
    )
    reporter.info(
        f"  {result.symbols_generated} symbols regenerated{passed_through}"
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

    # The metadata pass began with a whole-project scan: stamp graph freshness.
    stamp_graph_fresh(config=config, project_root=project_root)

    reporter.success(
        f"refreshed metadata on {changed_count} of {total - skipped_count} triefact(s) "
        f"({total - changed_count - skipped_count} already current)"
    )


def _run_roles_only_sync(reporter: Reporter, *, model: str | None, rederive_taxonomy: bool) -> None:
    """(Re)infer the architectural role tag for every symbol against a derived vocab.

    Scans first so the store reflects current source (the survey + classification
    both read it), then runs the two-pass roles flow: derive/load the taxonomy, then
    classify every symbol against it, persisting roles into both the triefact
    sentinels and the store. No prose is regenerated.
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.cascade
    client = make_client(model_id, sync_cfg=config.sync)
    db_path = project_root / ".trie" / "graph.db"

    with Store(db_path) as store:
        with reporter.status("scanning project…"):
            scan_project(project_root=project_root, config=config, store=store)
        with _progress_callback(reporter, label="classifying roles") as cb:
            result = run_roles_only(
                project_root=project_root,
                config=config,
                store=store,
                client=client,
                progress=cb,
                rederive_taxonomy=rederive_taxonomy,
            )

    # The roles pass began with a whole-project scan: stamp graph freshness.
    stamp_graph_fresh(config=config, project_root=project_root)

    if result.taxonomy_derived:
        reporter.success(
            f"derived role taxonomy ({result.taxonomy_size} roles) → "
            f"{taxonomy_path(project_root, config).relative_to(project_root)}"
        )
    reporter.success(
        f"classified {result.symbols_classified} symbol(s) across "
        f"{result.files_processed} file(s); {result.roles_changed} role(s) changed"
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
    with (
        Store(db_path) as store,
        _activity_progress(reporter, label="syncing", op="sync", project_root=project_root) as cb,
    ):
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
        if result.files_synced:
            _refresh_index_quietly(config, project_root, store)

    # run_incremental began with a whole-project scan, so the graph is now
    # current with disk: stamp it so the next graph-only sync (the turn hook)
    # no-ops instead of redundantly rebuilding.
    stamp_graph_fresh(project_root, config)

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

    had_errors = _report_sync_errors(reporter, result.file_errors)
    if had_errors and result.files_synced == 0:
        reporter.error(
            f"synced 0 of {len(result.file_errors)} file(s) — every file failed; "
            "the triefact tree was NOT refreshed"
        )
        raise typer.Exit(code=1)

    reporter.success(
        f"synced {result.files_synced} file(s) "
        f"({result.directly_stale_count} directly stale, "
        f"{result.cascaded_count} pulled in by the cascade)"
    )
    if result.files_skipped_no_budget:
        reporter.info(f"  skipped {result.files_skipped_no_budget} due to budget/limit")
    reporter.info(f"  actual cost: ${result.actual_cost_usd:.4f}")
    if had_errors:
        raise typer.Exit(code=1)


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

      1. A turn-boundary hook that calls `trie sync --graph-only --after-turn`
         so the graph and triefact tree stay current with the agent's edits.
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
        setup_config, project_root = Config.find_and_load(Path.cwd())
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

    # GitHub workflow install: comments the latest session digest on PRs.
    # Skipped for non-git dirs; user-owned files (no managed-by marker) are
    # never touched. Inert off GitHub, so no remote detection is needed.
    from trie.workflow_install import install_triediff_workflow

    workflow_result = install_triediff_workflow(
        project_root,
        diffs_dir=setup_config.diff.diffs_dir,
        dry_run=dry_run or print_only,
    )

    _render_setup_plan(reporter, mcp_plan, hook_plan, docs_plan, override_plan)
    wf_path = workflow_result.path or Path(".github/workflows/triediff-comment.yml")
    wf_note = f" ({workflow_result.note})" if workflow_result.note else ""
    reporter.info(f"pr digest workflow: {workflow_result.action} {wf_path}{wf_note}")
    # Surface a non-zero exit if any step hit an error so CI/scripts react.
    mcp_errors = any(r.action == "error" for r in mcp_plan.results) if mcp_plan else False
    hook_errors = any(r.action == "error" for r in hook_plan.results)
    docs_errors = any(r.action == "error" for r in docs_plan.results)
    override_errors = (
        any(r.action == "error" for r in override_plan.results) if override_plan else False
    )
    if (
        mcp_errors
        or hook_errors
        or docs_errors
        or override_errors
        or (workflow_result.action == "error")
    ):
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


def _grep_output_is_tty() -> bool:
    """True when grep output goes to an interactive terminal.

    Piped/captured output (agent tool wrappers, scripts) gets plain records
    instead of Rich tables: box-drawn tables render at width 80 when piped
    and truncate qnames with `…` — destroying exactly the datum the caller
    needs to copy into the next tool call.
    """
    import sys as _sys

    try:
        return _sys.stdout.isatty()
    except Exception:
        return False


def _print_grep_records(
    reporter: Reporter, rows: list, *, qname_suffix: Callable[[dict], str] | None = None
) -> None:
    """Plain, full-width, one-record-per-hit rendering for non-tty consumers.

    Format (stable — agent wrappers parse this visually, keep it grep-able):

        <qname>  <kind>  <file:line>
            <one-liner>
    """
    for r in rows:
        if not isinstance(r, dict):
            continue
        qname = str(r.get("qname", ""))
        if qname_suffix is not None:
            qname += qname_suffix(r)
        kind = str(r.get("kind", "") or r.get("inbound_count", ""))
        pointer = str(r.get("file_pointer", ""))
        reporter.console.print(f"{qname}  {kind}  {pointer}", markup=False, highlight=False)
        one_liner = str(r.get("one_liner", "")).strip()
        if one_liner:
            reporter.console.print(f"    {one_liner}", markup=False, highlight=False)


def _render_grep(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable rendering for `trie grep` output.

    Interactive terminals get a compact Rich table (qname, kind, file
    pointer, one-liner). Piped output — the agent-wrapper case — gets plain
    untruncated records instead, one per hit. When hits is empty, falls
    through to the fallback envelope: prints the fallback kind, query, note,
    and the ranked candidate matches if any. Error envelopes show the code,
    message, and suggestion on separate lines.
    """
    from rich.table import Table

    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return

    is_tty = _grep_output_is_tty()

    hits = envelope.get("hits") or []
    if isinstance(hits, list) and hits:
        if not is_tty:
            reporter.console.print(f"{len(hits)} hit(s)", markup=False)
            _print_grep_records(
                reporter,
                hits,
                qname_suffix=lambda h: _patched_tag(int(h.get("pending_patch_count", 0))),
            )
        else:
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
        related = envelope.get("related") or []
        if isinstance(related, list) and related:
            reporter.info(
                f"[dim]related by prose ({len(related)} — name didn't match, prose did):[/dim]"
            )
            _print_grep_records(reporter, related)
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
        if not is_tty:
            reporter.console.print(f"{len(matches)} candidate(s) by text match", markup=False)
            _print_grep_records(reporter, matches)
            return
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

    # Notes carry the honesty layer (stale-prose warnings, missing-triefact
    # hints, hub truncation). Stale warnings especially must never be dropped:
    # a read that serves outdated prose silently is a lying wiki.
    notes = envelope.get("notes")
    if isinstance(notes, list) and notes:
        reporter.console.print()
        for note in notes:
            text = str(note)
            style = "bold yellow" if text.startswith("⚠") else "dim"
            reporter.console.print(f"[{style}]{text}[/{style}]")

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

    hist = envelope.get("history")
    if isinstance(hist, list):
        reporter.console.print()
        reporter.console.print(f"[bold]history[/bold] ({len(hist)})")
        if not hist:
            reporter.console.print("  [dim](no digest entries mention this symbol)[/dim]")
        for h in hist:
            if not isinstance(h, dict):
                continue
            reporter.console.print(f"  {h.get('date', '?')} · {h.get('change', '')}")
            title = h.get("title", "")
            if title:
                reporter.console.print(f"    [dim]{title}[/dim]")

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
    path: str = typer.Argument(
        ...,
        help="Symbol qname (e.g. 'trie/sync/cascade:compute_cascade') OR a file path.",
    ),
    full: bool = typer.Option(
        False,
        "--full",
        help="For a file path: return every section's full prose instead of the compact view.",
    ),
    source: bool = typer.Option(
        False,
        "--source",
        help="Force raw line-numbered source for a FILE PATH (any file, indexed or not).",
    ),
    offset: int | None = typer.Option(
        None,
        "--offset",
        help="With a file path: 1-indexed first line to include (implies --source).",
    ),
    limit: int | None = typer.Option(
        None,
        "--limit",
        help="With a file path: maximum number of lines to return from offset (implies --source).",
    ),
    history: bool = typer.Option(
        False,
        "--history",
        "-H",
        help=(
            "Also show the symbol's (or file's) intent trail from the session-digest "
            "archive: the chronological 'why it changed' lines recorded at each commit."
        ),
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the raw MCP envelope as JSON instead of a human-readable summary.",
    ),
) -> None:
    """Read source code or trie's synthesised description of it — triefact-first.

    Mirror of the MCP `read` tool. Dispatch on the argument:

    - A symbol qname → its signature, triefact prose, source pointer, and
      one-liner descriptions of every caller and callee in one round trip.
    - A file path → a COMPACT triefact view by default (one entry per symbol:
      qname, kind, lines, signature, intro). Pass `--full` for every section's
      full prose, or `--source` (or `--offset`/`--limit`) for raw source.

    Examples:

      trie read trie/sync/cascade:compute_cascade
      trie read trie/sync/cascade.py            # compact triefact view
      trie read trie/sync/cascade.py --full     # full prose bundle
      trie read package.json --source
      trie read src/app.ts --offset 1 --limit 40
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.read(
            path, full=full, show_source=source, offset=offset, limit=limit, history=history
        )
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_render_read_dispatch)


def _render_read_dispatch(envelope: dict[str, object], reporter: Reporter) -> None:
    """Render whichever shape `tools.read` returned: symbol / triefact view / source."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    # read_source envelope carries `lines`; the triefact view carries `output`;
    # a symbol read carries `prose`/`callers`/`callees`.
    if "lines" in envelope:
        _render_read_source(envelope, reporter)
    elif "output" in envelope:
        reporter.console.print(str(envelope.get("output", "")))
    else:
        _render_read(envelope, reporter)


def _render_read_source(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable render of a read_source envelope."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    lines = envelope.get("lines", "")
    reporter.console.print(str(lines))
    if envelope.get("more"):
        reporter.info("(more lines available; pass --offset/--limit to page)")


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


@app.command("blast-radius")
def blast_radius_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(
        ...,
        help="Fully-qualified symbol name to compute the edit blast radius for.",
    ),
    as_json: bool = typer.Option(
        False,
        "--json",
        help="Emit the raw MCP envelope as JSON instead of a human-readable summary.",
    ),
) -> None:
    """Compute the cascade blast radius of editing a symbol — free graph math.

    Mirror of the MCP `blast_radius` tool. Reports every symbol whose
    triefact/source would be regenerated if `qname` changed, with each
    one's BFS hop distance from the seed. No LLM calls. Use before a risky
    delete/rename/modify to gauge impact.

    Examples:

      trie blast-radius trie/graph/store:Store.replace_all_edges
      trie blast-radius --json some_qname
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.blast_radius(qname)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_render_blast_radius)


def _render_blast_radius(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable render of a blast_radius envelope."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    qname = envelope.get("qname", "")
    file = envelope.get("file", "")
    cascade = envelope.get("cascade", [])
    count = envelope.get("cascade_count", 0)
    direct = envelope.get("direct", 0)
    reporter.console.print(f"[bold]{qname}[/bold]  [dim]({file})[/dim]")
    reporter.console.print(
        f"  blast radius: {count} symbol(s) regenerated · {direct} direct caller(s)"
    )
    if isinstance(cascade, list) and cascade:
        from rich.table import Table

        table = Table(title="Cascade")
        table.add_column("hop", style="magenta", justify="right")
        table.add_column("symbol", style="cyan")
        table.add_column("file", style="dim")
        for item in cascade:
            if not isinstance(item, dict):
                continue
            table.add_row(
                str(item.get("hop", "")), str(item.get("qname", "")), str(item.get("file", ""))
            )
        reporter.console.print(table)
    else:
        reporter.info("nothing else depends on this symbol")


# ---------------------------------------------------------------------------
# Extended agent tools: grep_str, grep_entry_points, grep_symbol,
# grep_symbol_and_neighbours, explain_symbol, explain_symbol_references,
# trace_flow, explain_flow
# ---------------------------------------------------------------------------


def _print_plain(envelope: dict[str, object], reporter: Reporter) -> None:
    """Render a tool envelope as dense readable text (shared with the MCP
    surface via `trie.render.render_envelope`). Exists because the previous
    implementation was `json.dumps` in a trench coat — agents paid for
    braces, escaped newlines, and repeated keys on every query."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    reporter.console.print(render_envelope(envelope), markup=False, highlight=False)


@app.command("grep-str")
def grep_str_cmd(
    ctx: typer.Context,
    regexp: str = typer.Argument(..., help="Regex pattern to search source bodies with."),
    all_files: bool = typer.Option(
        False,
        "--all-files",
        help="Search the WHOLE repo (incl. non-indexed files), not just indexed source bodies.",
    ),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
) -> None:
    """Search source bodies with a regex; attribute hits to enclosing symbols.

    By default only indexed (in-scope) source bodies are searched. Pass
    `--all-files` to run ripgrep over the entire project (EXT-1): in-scope
    hits are still attributed to their enclosing symbol, and out-of-scope
    hits (TS/JS, configs, docs, lockfiles) come back as `file:line:text`.

    Examples:
      trie grep-str 'raise.*Error'
      trie grep-str 'TODO' --all-files
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.grep_str_all(regexp) if all_files else tools.grep_str(regexp)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("find")
def find_cmd(
    ctx: typer.Context,
    pattern: str = typer.Argument(
        ..., help="Glob pattern, e.g. '**/*.ts', 'Dockerfile', 'src/**/*.tsx'."
    ),
    indexed_only: bool = typer.Option(
        False,
        "--indexed-only",
        help="Restrict to indexed files only (default searches the whole tree).",
    ),
    limit: int = typer.Option(100, "--limit", "-l", help="Maximum number of paths to return."),
) -> None:
    """Find files by name/path glob (EXT-2) — the filename-search trie lacked.

    Walks the whole project tree by default (pruning excluded/vendored dirs),
    mtime-sorted, newest first. Pass `--indexed-only` to restrict to files in
    trie's scope.

    Examples:
      trie find '**/*.ts'
      trie find 'trie.toml'
      trie find 'src/**/*.tsx' --limit 50
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.find_files(pattern, all_files=not indexed_only, limit=limit)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_render_find)


@app.command("write")
def write_cmd(
    ctx: typer.Context,
    path: str = typer.Argument(
        ..., help="File path to create/overwrite, relative to the project root."
    ),
    content: str | None = typer.Option(
        None,
        "--content",
        "-c",
        help="File content. If omitted, content is read from stdin.",
    ),
    overwrite: bool = typer.Option(
        False,
        "--overwrite",
        help="Allow replacing an existing file.",
    ),
) -> None:
    """Create or overwrite an arbitrary file under the project root (EXT-8).

    Fills the gap where `create-symbol` only adds a Python symbol to an
    existing indexed file. Use for new config/doc/script files. If the path is
    an indexed file type, the output notes that a `trie sync`/refresh is needed
    to bring it into the graph.

    Examples:
      trie write README.md --content "# Project\n"
      cat body.txt | trie write notes.md
    """
    reporter = _get_reporter(ctx)
    if content is None:
        import sys as _sys

        body = _sys.stdin.read()
    else:
        body = content
    tools = _open_tools(reporter)
    try:
        envelope = tools.write_file(path, body, overwrite=overwrite)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=False, reporter=reporter, render=_render_write)


def _render_write(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable render of a write_file envelope."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    verb = "created" if envelope.get("created") else "overwrote"
    reporter.success(f"{verb} {envelope.get('path')} ({envelope.get('bytes_written')} bytes)")
    if envelope.get("needs_sync"):
        reporter.info("this file is in trie's scope — run `trie sync` to index it")


def _render_find(envelope: dict[str, object], reporter: Reporter) -> None:
    """Human-readable render of a find_files envelope."""
    err = envelope.get("error")
    if isinstance(err, dict):
        _render_error_envelope(err, reporter)
        return
    matches = envelope.get("matches", [])
    count = envelope.get("match_count", 0)
    truncated = envelope.get("truncated", False)
    if not isinstance(matches, list) or not matches:
        reporter.info("no files match")
        return
    for m in matches:
        reporter.console.print(str(m))
    suffix = " (truncated; raise --limit for more)" if truncated else ""
    reporter.info(f"{count} file(s){suffix}")


@app.command("grep-entry-points")
def grep_entry_points_cmd(
    ctx: typer.Context,
    query: str = typer.Argument(..., help="Topic or concept to match against symbol prose."),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
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
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("grep-symbol")
def grep_symbol_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
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
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("grep-symbol-neighbours")
def grep_symbol_neighbours_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol name or fragment to fuzzy-match."),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
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
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("explain-symbol")
def explain_symbol_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol qname or name fragment to explain."),
    history: bool = typer.Option(
        False,
        "--history",
        "-H",
        help="Also show the symbol's intent trail from the digest archive.",
    ),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
) -> None:
    """Full prose + joined narrative story of a symbol's references.

    Example:
      trie explain-symbol compute_cascade
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.explain_symbol(sym, history=history)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("explain-symbol-refs")
def explain_symbol_refs_cmd(
    ctx: typer.Context,
    sym: str = typer.Argument(..., help="Symbol qname or name fragment."),
    history: bool = typer.Option(
        False,
        "--history",
        "-H",
        help="Also show the symbol's intent trail from the digest archive.",
    ),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
) -> None:
    """Explain how a symbol is used — callers only, with their prose.

    Example:
      trie explain-symbol-refs slugify
    """
    reporter = _get_reporter(ctx)
    tools = _open_tools(reporter)
    try:
        envelope = tools.explain_symbol_references(sym, history=history)
    finally:
        tools.close()
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("trace-flow")
def trace_flow_cmd(
    ctx: typer.Context,
    symbol1: str = typer.Argument(..., help="Starting symbol qname or name."),
    symbol2: str = typer.Argument(..., help="Target symbol qname or name."),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
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
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


@app.command("explain-flow")
def explain_flow_cmd(
    ctx: typer.Context,
    symbol1: str = typer.Argument(..., help="Starting symbol qname or name."),
    symbol2: str = typer.Argument(..., help="Target symbol qname or name."),
    as_json: bool = typer.Option(
        False, "--json", help="Emit the raw JSON envelope instead of formatted text."
    ),
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
    _emit_envelope(envelope, as_json=as_json, reporter=reporter, render=_print_plain)


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


def _close_qname_suggestions(store: Store, qname: str, *, n: int = 3) -> list[str]:
    """Fuzzy-match a missed qname against the graph for did-you-mean hints.

    A `not_found` on the patch path is far more often a hand-built/guessed
    qname than a genuinely removed symbol (module-level constants and methods
    are the usual traps), so the error message leads with close matches —
    same-module symbols first (see `_close_qname_matches`). Best-effort:
    returns [] on any failure rather than masking the real error.
    """
    try:
        from trie.mcp_server import _close_qname_matches

        return _close_qname_matches(qname, store.all_qualified_names(), n=n)
    except Exception:
        return []


@patch_app.command("create")
def patch_create_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(..., help="Qualified name of the symbol to patch."),
    note: str = typer.Option(..., "--note", "-n", help="Implementation change note."),
    reason: str = typer.Option(
        "", "--reason", "-r", help="Why the cascade needs to know about this change."
    ),
    gone: bool = typer.Option(
        False,
        "--gone",
        help=(
            "The symbol was REMOVED (no longer in the graph): record the note "
            "straight to the session log as a delete instead of queueing a patch. "
            "This is how removals satisfy the `trie intent` gate."
        ),
    ),
) -> None:
    """Post a fire-and-forget edit patch against a symbol."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        session_id = _cli_session_id(project_root)
        if gone:
            # Removed symbols aren't in the graph anymore; the qname-keyed
            # patches table holds their deletion intent without an FK.
            patch_id = store.add_patch(
                qname, note, reason, session_id, kind="delete", require_symbol=False
            )
            reporter.success(f"removal note #{patch_id} recorded for {qname}")
            return
        patch_id = store.add_patch(qname, note, reason, session_id)
    except KeyError:
        # A wrong qname is far more often a guess/typo than a removed symbol:
        # suggest close matches first (hand-built qnames are the documented
        # trap), and mention --gone only as the removal escape hatch. The
        # whole block goes to STDERR: subprocess wrappers (the opencode tool
        # overrides) relay stderr on failure, and suggestions printed to
        # stdout were invisible exactly when they mattered.
        suggestions = _close_qname_suggestions(store, qname)
        reporter.error(f"symbol {qname!r} not found in the graph")
        if suggestions:
            reporter.err_console.print("  did you mean: " + "  ".join(suggestions))
        reporter.err_console.print(
            "  (wrong name? look it up with `trie grep --name <fragment>`; "
            "actually removed? re-run with --gone)"
        )
        raise typer.Exit(code=1) from None
    finally:
        store.close()

    reporter.success(f"patch #{patch_id} posted for {qname}")


@patch_app.command("create-batch")
def patch_create_batch_cmd(
    ctx: typer.Context,
    json_file: str = typer.Option(
        "", "--json-file", help="Path to a JSON file with the patch array (else read stdin)."
    ),
) -> None:
    """Stage MANY patches/creates in one call. Reads a JSON array.

    Source: `--json-file PATH` if given, otherwise stdin. Each item is an object:
      {"op": "patch",  "qname": "src/foo:bar", "note": "...", "reason": "..."}
      {"op": "create", "qname": "src/foo:baz", "note": "...", "file": "...",
       "anchor": "...", "reason": "..."}
    `op` defaults to "patch". This collapses what would be N separate
    `patch create` invocations (N agent turns) into one: the staging itself is a
    cheap DB write, so the win is removing the per-call round-trip. Items are
    processed independently — a bad item is reported but does not abort the rest.
    Emits a JSON summary on stdout: {staged, failed, results:[...]}.
    """
    import json as _json
    import sys as _sys

    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    if json_file:
        try:
            raw = Path(json_file).read_text()
        except OSError as exc:
            reporter.error(f"cannot read --json-file {json_file!r}: {exc}")
            raise typer.Exit(code=1) from exc
    else:
        raw = _sys.stdin.read()
    try:
        items = _json.loads(raw)
    except _json.JSONDecodeError as exc:
        reporter.error(f"stdin is not valid JSON: {exc}")
        raise typer.Exit(code=1) from exc
    if not isinstance(items, list) or not items:
        reporter.error("stdin must be a non-empty JSON array of patch items")
        raise typer.Exit(code=1)

    from trie.parse import registry

    src_root = (project_root / _config.triefacts.source_root).resolve()
    store = Store(project_root / ".trie" / "graph.db")
    session_id = _cli_session_id(project_root)
    results: list[dict[str, object]] = []
    staged = 0
    try:
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                results.append({"index": idx, "ok": False, "error": "item is not an object"})
                continue
            qname = str(item.get("qname", "")).strip()
            note = str(item.get("note", "")).strip()
            reason = str(item.get("reason", "") or "")
            op = str(item.get("op", "patch")).strip().lower() or "patch"
            if not qname or not note:
                results.append(
                    {"index": idx, "qname": qname, "ok": False, "error": "qname and note required"}
                )
                continue
            try:
                # Graceful create→patch fallback (mirrors TrieTools.batch_patch):
                # a `create` for an already-existing symbol is recorded as a
                # `patch` instead of failing, flagged with `fell_back`.
                fell_back_from_create = (
                    op == "create" and store.get_symbol_detail(qname) is not None
                )
                if fell_back_from_create:
                    op = "patch"

                if op == "create":
                    target_file = str(item.get("file", "")) or registry.resolve_create_target(
                        src_root, qname
                    )
                    cid = store.add_create_patch(
                        target_file=target_file,
                        target_qname=qname,
                        note=note,
                        reason=reason,
                        session_id=session_id,
                        anchor_qname=str(item.get("anchor", "")) or None,
                    )
                    results.append(
                        {"index": idx, "qname": qname, "ok": True, "op": "create", "patch_id": cid}
                    )
                    staged += 1
                else:
                    pid = store.add_patch(qname, note, reason, session_id)
                    entry: dict[str, object] = {
                        "index": idx,
                        "qname": qname,
                        "ok": True,
                        "op": "patch",
                        "patch_id": pid,
                    }
                    if fell_back_from_create:
                        entry["fell_back"] = True
                    results.append(entry)
                    staged += 1
            except KeyError:
                # Parity with TrieTools.batch_patch: a missed qname is usually
                # a guess/typo, so hand back close matches in the result row.
                entry = {
                    "index": idx,
                    "qname": qname,
                    "ok": False,
                    "error": "symbol not found in graph",
                }
                close = _close_qname_suggestions(store, qname)
                if close:
                    entry["did_you_mean"] = close
                results.append(entry)
    finally:
        store.close()

    failed = len(results) - staged
    reporter.console.print_json(data={"staged": staged, "failed": failed, "results": results})
    if staged == 0:
        raise typer.Exit(code=1)


@patch_app.command("create-symbol")
def patch_create_symbol_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(..., help="Intended qualified name, e.g. 'pkg/mod:new_fn'."),
    note: str = typer.Option(..., "--note", "-n", help="What the new symbol should do."),
    file: str = typer.Option(
        "", "--file", "-f", help="Target source file (derived from qname when omitted)."
    ),
    anchor: str = typer.Option(
        "", "--anchor", "-a", help="Place the new symbol after this existing qname."
    ),
    reason: str = typer.Option("", "--reason", "-r", help="Why this symbol is needed."),
) -> None:
    """Stage creation of a NEW symbol (applied by `trie patch apply`)."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        # Graceful create→patch fallback: if the symbol already exists, record
        # the note as a patch rather than erroring — the intent is equally valid
        # and the agent shouldn't have to re-run with a different subcommand.
        if store.get_symbol_detail(qname) is not None:
            pid = store.add_patch(qname, note, reason, _cli_session_id(project_root))
            reporter.success(
                f"{qname!r} already existed — recorded as patch #{pid} instead of a create"
            )
            return
        # Resolve target file via the registry: existing module file wins, else
        # infer the language for a new file (sibling, then default suffix). Pass
        # `--file` to override explicitly.
        from trie.parse import registry

        src_root = (project_root / _config.triefacts.source_root).resolve()
        target_file = file or registry.resolve_create_target(src_root, qname)
        cid = store.add_create_patch(
            target_file=target_file,
            target_qname=qname,
            note=note,
            reason=reason,
            session_id=_cli_session_id(project_root),
            anchor_qname=anchor or None,
        )
    finally:
        store.close()
    reporter.success(f"create patch #{cid} staged for {qname} in {target_file}")


@patch_app.command("delete-symbol")
def patch_delete_symbol_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(..., help="Qualified name of the symbol to delete."),
    reason: str = typer.Option("", "--reason", "-r", help="Why it's being removed."),
) -> None:
    """Stage deletion of an existing symbol (applied by `trie patch apply`)."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    store = Store(project_root / ".trie" / "graph.db")
    try:
        pid = store.add_delete_patch(qname, reason, _cli_session_id(project_root))
        dependents = store.references_in(qname)
    except KeyError:
        reporter.error(f"symbol {qname!r} not found in the graph")
        raise typer.Exit(code=1) from None
    finally:
        store.close()
    reporter.success(f"delete patch #{pid} staged for {qname}")
    if dependents:
        reporter.console.print(
            f"  [yellow]{len(dependents)} dependent(s)[/yellow] will reference a deleted "
            f"symbol unless patched: {', '.join(dependents[:5])}"
        )


@patch_app.command("rename-symbol")
def patch_rename_symbol_cmd(
    ctx: typer.Context,
    qname: str = typer.Argument(..., help="Qualified name of the symbol to rename."),
    new_name: str = typer.Argument(..., help="New local name (not a qualified name)."),
    reason: str = typer.Option("", "--reason", "-r", help="Why it's being renamed."),
) -> None:
    """Stage a rename of an existing symbol (applied by `trie patch apply`)."""
    reporter = _get_reporter(ctx)
    try:
        _config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    if not new_name.isidentifier():
        reporter.error(f"{new_name!r} is not a valid identifier")
        raise typer.Exit(code=1)

    store = Store(project_root / ".trie" / "graph.db")
    try:
        pid = store.add_rename_patch(qname, new_name, reason, _cli_session_id(project_root))
        refs = store.references_in(qname)
    except KeyError:
        reporter.error(f"symbol {qname!r} not found in the graph")
        raise typer.Exit(code=1) from None
    finally:
        store.close()
    reporter.success(f"rename patch #{pid} staged: {qname} → {new_name}")
    if refs:
        reporter.console.print(f"  [dim]{len(refs)} caller(s) reference it[/dim]")


@patch_app.command("apply")
def patch_apply_cmd(
    ctx: typer.Context,
    note: str = typer.Option(
        "",
        "--note",
        "-N",
        help="Session note: the unifying intent (required for multi-symbol applies).",
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Emit raw JSON output (useful for agent consumers).",
    ),
) -> None:
    """Commit pending patch notes as intent — trie generates no code.

    Archives every pending note to the session log (feeding the per-commit
    digest, `read --history`, and the `trie intent` gate) and clears the
    queue. Source changes are yours; this records why they happened.
    """
    reporter = _get_reporter(ctx)
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    from trie.edits.pipeline import record_intent

    store = Store(project_root / ".trie" / "graph.db")
    try:
        envelope = record_intent(store, config, project_root, session_note=note)
    finally:
        store.close()

    if json_output:
        import json as _json

        console.print_json(_json.dumps(envelope))
        if not envelope.get("ok"):
            raise typer.Exit(code=1)
        return
    if not envelope.get("ok"):
        reporter.error(envelope.get("message", "record failed"))
        raise typer.Exit(code=1)
    if envelope.get("recorded", 0) == 0:
        reporter.info("no pending patches to record")
    else:
        reporter.success(f"recorded intent for {envelope['recorded']} symbol(s) to the session log")
        for q in envelope.get("symbols", []):
            reporter.console.print(f"  [cyan]{q}[/cyan]")
    uncovered = envelope.get("uncovered")
    if uncovered:
        reporter.warn(
            f"intent gate: {len(uncovered)} touched symbol(s) still lack notes "
            "and would fail the commit gate:"
        )
        for q in uncovered[:5]:
            reporter.console.print(f"  [yellow]{q}[/yellow]")
        if len(uncovered) > 5:
            reporter.console.print(f"  … and {len(uncovered) - 5} more")
    elif uncovered is not None:
        reporter.info("intent gate: all touched symbols covered")


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
        # preview_patches covers modify/structural patches; staged creates live
        # in a separate table, so pull them in so the preview reflects them too.
        creates = store.get_create_patches_grouped()
    finally:
        store.close()

    create_qnames = [str(row.get("target_qname", "")) for rows in creates.values() for row in rows]

    if result["total_patches"] == 0 and not create_qnames:
        reporter.info("no pending patches")
        return

    from rich.table import Table

    table = Table(title="Patch Preview")
    table.add_column("Symbol", style="cyan")
    table.add_column("Origin", style="magenta")

    for qname in result["patched_list"]:
        table.add_row(qname, "patched")
    for qname in create_qnames:
        table.add_row(qname, "create")
    # Cascade neighbours are DISTINCT symbols (callers) reached from the patched
    # set — shown as their own rows, not a flag on the patched symbols.
    for qname in result.get("cascade_list", []):
        table.add_row(qname, "cascade")

    reporter.console.print(table)
    reporter.info(
        f"{result['total_patches']} patch(es) across {result['patched_symbols']} symbol(s); "
        f"{len(create_qnames)} create(s); {result['cascade_symbols']} cascade neighbour(s)"
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
        # Create-symbol patches live in a separate table; include them so the
        # listing reflects the full pending queue (otherwise staged creates are
        # invisible here even though `patch apply` processes them).
        creates = store.get_create_patches_grouped()
        if not qnames and not creates:
            reporter.info("no pending patches")
            return

        from rich.table import Table

        if qnames:
            table = Table(title="Pending Patches")
            table.add_column("QName", style="cyan")
            table.add_column("Patches", style="magenta")
            for qname in qnames:
                patches = store.get_patches_for_qname(qname)
                table.add_row(qname, str(len(patches)))
            reporter.console.print(table)

        if creates:
            ctable = Table(title="Pending Creates")
            ctable.add_column("New QName", style="green")
            ctable.add_column("File", style="cyan")
            for _file, rows in creates.items():
                for row in rows:
                    ctable.add_row(
                        str(row.get("target_qname", "")), str(row.get("target_file", ""))
                    )
            reporter.console.print(ctable)
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
        # Drop from BOTH the modify/structural patch table and the separate
        # create_patches table so a single drop clears the whole pending queue
        # (otherwise staged creates linger after `drop --all`).
        if qname:
            count = store.delete_patches(qname=qname)
            count += store.delete_create_patches(target_qname=qname)
        elif session_id:
            count = store.delete_patches(session_id=session_id)
            count += store.delete_create_patches(session_id=session_id)
        elif all:
            count = store.delete_patches(all=True)
            count += store.delete_create_patches(all=True)
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
