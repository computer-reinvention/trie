from __future__ import annotations

import sys
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import typer
from rich.console import Console

from trie import __version__, telemetry
from trie.check import StaleReason, check_project
from trie.config import Config, ConfigNotFoundError
from trie.cost import get_pricing
from trie.diff_cmd import diff_project
from trie.graph.store import Store
from trie.init import InitError, init_project
from trie.mcp_install import TARGETS as MCP_TARGETS
from trie.mcp_install import InstallPlan, MCPInstallError
from trie.mcp_install import install as mcp_run_install
from trie.mcp_server import run_stdio as run_mcp_stdio
from trie.models import make_client
from trie.reporter import ProgressHandle, Reporter, Verbosity
from trie.scan import scan_project
from trie.sync.bootstrap import BootstrapPlan, build_plan, run_bootstrap
from trie.sync.incremental import (
    IncrementalWorklist,
    compute_incremental_worklist,
    run_incremental,
)
from trie.sync.progress import ProgressCallback
from trie.sync.single_file import FileSyncResult, sync_single_file

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
    reporter.info("  [cyan]trie plan[/cyan]     preview the worklist + estimated cost (free)")
    reporter.info("  [cyan]trie sync[/cyan]     generate triefacts")
    reporter.info("  [cyan]trie verify[/cyan]   check drift (also runs as pre-commit hook)")


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
    client = make_client(model_id)
    db_path = project_root / ".trie" / "graph.db"
    triefacts_root = project_root / config.triefacts.root
    use_incremental = not all_ and _has_existing_triefacts(triefacts_root)

    with Store(db_path) as store:
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
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.",
    ),
) -> None:
    """Generate or refresh trie triefacts.

    Modes (auto-detected):
      • --file   : sync one file.
      • --dry-run: preview unified diff against the live tree.
      • --all    : force full re-pass.
      • default  : if no triefacts exist yet → first-run bootstrap (with cost confirmation);
                   otherwise → incremental cascade.

    Drift detection runs as the first step regardless. For an LLM-free, exit-coded
    drift gate suitable for pre-commit hooks, use `trie verify`.
    """
    reporter = _get_reporter(ctx)
    if file is not None and all_:
        reporter.error("--file and --all are mutually exclusive")
        raise typer.Exit(code=1)

    if file is not None:
        _run_single_file_sync(reporter, file, model)
        return

    if dry_run:
        _run_dry_run_diff(reporter=reporter, model=model, budget=budget, limit=limit)
        return

    # Auto-detect first-run vs incremental.
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
    client = make_client(model_id)
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
    client = make_client(model_id)
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


def _run_single_file_sync(reporter: Reporter, file: Path, model: str | None) -> None:
    if not file.exists():
        reporter.error(f"{file} does not exist")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(file.parent)
    except ConfigNotFoundError as exc:
        reporter.error(str(exc))
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    client = make_client(model_id)
    db_path = project_root / ".trie" / "graph.db"

    with Store(db_path) as store, reporter.status(f"generating triefact for [cyan]{file}[/cyan]…"):
        result = sync_single_file(
            file, project_root=project_root, config=config, client=client, store=store
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
    client = make_client(model_id)

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


mcp_app = typer.Typer(
    name="mcp",
    help="MCP server: install for an agent (`install`), or serve over stdio.",
    invoke_without_command=True,
    no_args_is_help=False,
)
app.add_typer(mcp_app, name="mcp")


@mcp_app.callback()
def _mcp_root(ctx: typer.Context) -> None:
    """When invoked without a subcommand (back-compat with v0.1's `trie mcp`),
    fall through to `serve`. New installs and snippets reference `trie mcp serve`
    explicitly."""
    if ctx.invoked_subcommand is None:
        _run_mcp_serve()
        raise typer.Exit()


@mcp_app.command("serve", hidden=True)
def mcp_serve() -> None:
    """Stdio MCP server entry point. Hidden from help — agents spawn this directly
    via the snippet that `trie mcp install` writes."""
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


if __name__ == "__main__":
    app()
