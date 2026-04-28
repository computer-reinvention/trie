from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from trie import __version__
from trie.check import StaleReason, check_project
from trie.config import Config, ConfigNotFoundError
from trie.cost import get_pricing
from trie.diff_cmd import diff_project
from trie.graph.store import Store
from trie.init import InitError, init_project
from trie.mcp_server import run_stdio as run_mcp_stdio
from trie.models import make_client
from trie.scan import scan_project
from trie.sync.bootstrap import build_plan, run_bootstrap
from trie.sync.incremental import run_incremental
from trie.sync.single_file import sync_single_file

app = typer.Typer(
    name="trie",
    help="Documentation tree that mirrors your source tree, kept coherent by an LSP-aware cascade.",
)
console = Console()


@app.callback(invoke_without_command=True)
def _root(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", help="Show trie version and exit."),
) -> None:
    if version:
        typer.echo(f"trie {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()


@app.command("init")
def init_cmd(
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
) -> None:
    """Create trie.toml and update .gitignore in a Python project."""
    try:
        result = init_project(root, force=force)
    except InitError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    console.print(f"[green]✓[/green] wrote {result.project_root / 'trie.toml'}")
    detected = ", ".join(result.detected_markers)
    console.print(f"  detected: {detected}")
    if result.gitignore_updated:
        console.print(
            f"[green]✓[/green] updated {result.project_root / '.gitignore'} (added .trie/)"
        )
    else:
        console.print("  .gitignore already had .trie/ — skipped")
    console.print()
    console.print("Next: try [cyan]trie sync --file <path/to/some.py>[/cyan]")


@app.command("scan")
def scan_cmd() -> None:
    """Walk the project, parse changed files, refresh the symbol graph."""
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    db_path = project_root / ".trie" / "graph.db"
    with console.status("scanning project…"), Store(db_path) as store:
        result = scan_project(project_root=project_root, config=config, store=store)

    parts = []
    if result.files_new:
        parts.append(f"[green]{result.files_new} new[/green]")
    if result.files_updated:
        parts.append(f"[yellow]{result.files_updated} updated[/yellow]")
    if result.files_unchanged:
        parts.append(f"{result.files_unchanged} unchanged")
    if result.files_removed:
        parts.append(f"[red]{result.files_removed} removed[/red]")
    breakdown = ", ".join(parts) if parts else "no files in scope"
    console.print(f"[green]✓[/green] scanned {result.files_total} files: {breakdown}")
    console.print(
        f"  {result.symbols_total} symbols, {result.edges_total} edges in "
        f"{db_path.relative_to(project_root)}"
    )


@app.command("plan")
def plan_cmd(
    model: str | None = typer.Option(
        None, "--model", help="Override the configured model for cost estimation."
    ),
) -> None:
    """Show the bootstrap worklist + estimated cost without making API calls.

    Equivalent to `trie sync --bootstrap --dry-run`, but as a top-level command since
    "preview the work and the bill" is a distinct mental step from "run a sync."
    """
    _run_bootstrap_sync(model=model, budget=None, limit=None, dry_run=True)


@app.command("check")
def check_cmd(
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help="Print only a summary line.",
    ),
) -> None:
    """Verify the doc tree is coherent with the source. Exits non-zero if stale.

    Designed for pre-commit: fast, no API calls, no DB writes. Compares each in-scope
    source file's symbol fingerprints against the fingerprints embedded in the matching
    doc file's section sentinels.
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    result = check_project(project_root=project_root, config=config)

    if result.is_clean:
        console.print("[green]✓[/green] doc tree is coherent")
        return

    grouped: dict[str, list] = {}
    for it in result.items:
        grouped.setdefault(it.doc_path, []).append(it)

    if not quiet:
        for doc_path, items in sorted(grouped.items()):
            console.print(f"[red]✗[/red] {doc_path}")
            for it in items:
                if it.reason == StaleReason.MISSING_DOC:
                    console.print(f"    [yellow]missing doc[/yellow] for {it.source_path}")
                elif it.reason == StaleReason.MISSING_SECTION:
                    console.print(f"    [yellow]missing section[/yellow] for {it.qualified_name}")
                elif it.reason == StaleReason.STALE_SECTION:
                    console.print(f"    [yellow]stale[/yellow] {it.qualified_name}")
                elif it.reason == StaleReason.ORPHAN_SECTION:
                    console.print(f"    [yellow]orphan[/yellow] {it.qualified_name}")
        console.print()

    console.print(
        f"[red]✗ {len(result.items)} issue(s) across {len(grouped)} doc file(s)[/red] — "
        f"run [cyan]trie sync[/cyan] to refresh"
    )
    raise typer.Exit(code=1)


@app.command("sync")
def sync_cmd(
    file: Path | None = typer.Option(
        None,
        "--file",
        "-f",
        help="Sync a single source file (M1 mode).",
    ),
    bootstrap: bool = typer.Option(
        False,
        "--bootstrap",
        help="Run bootstrap mode: rank scope files and generate docs up to --budget or --limit.",
    ),
    budget: float | None = typer.Option(
        None,
        "--budget",
        help="USD budget for bootstrap mode. Stops once cumulative actual cost reaches this.",
    ),
    limit: int | None = typer.Option(
        None,
        "--limit",
        help="Maximum files to sync in bootstrap mode.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="In bootstrap mode, print the plan and estimated cost without making API calls.",
    ),
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.",
    ),
) -> None:
    """Generate or refresh trie documentation."""
    if file is not None and bootstrap:
        console.print("[red]error:[/red] --file and --bootstrap are mutually exclusive")
        raise typer.Exit(code=1)

    if file is not None:
        _run_single_file_sync(file, model)
        return

    if bootstrap:
        _run_bootstrap_sync(model=model, budget=budget, limit=limit, dry_run=dry_run)
        return

    # Default: incremental cascade mode.
    _run_incremental_sync(model=model, budget=budget, limit=limit)


def _run_single_file_sync(file: Path, model: str | None) -> None:
    if not file.exists():
        console.print(f"[red]error:[/red] {file} does not exist")
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(file.parent)
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    client = make_client(model_id)

    with console.status(f"generating docs for [cyan]{file}[/cyan]…"):
        result = sync_single_file(file, project_root=project_root, config=config, client=client)

    console.print(f"[green]✓[/green] wrote {result.doc_path}")
    console.print(
        f"  {result.symbols_generated} symbols generated"
        + (f", {result.sections_removed} stale sections removed" if result.sections_removed else "")
    )
    console.print(
        f"  tokens: {result.input_tokens} in / {result.output_tokens} out · "
        f"cache: {result.cache_creation_input_tokens} write / {result.cache_read_input_tokens} read"
    )


def _run_bootstrap_sync(
    *, model: str | None, budget: float | None, limit: int | None, dry_run: bool
) -> None:
    if not dry_run and budget is None and limit is None:
        console.print(
            "[red]error:[/red] --bootstrap requires at least one of --budget USD or --limit N "
            "(or pass --dry-run to preview without API calls)"
        )
        raise typer.Exit(code=1)

    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    pricing = get_pricing(model_id)

    db_path = project_root / ".trie" / "graph.db"
    with Store(db_path) as store:
        with console.status("scanning project…"):
            scan_project(project_root=project_root, config=config, store=store)
        plan = build_plan(project_root=project_root, store=store, model_id=model_id)

        if not plan.items:
            console.print("[yellow]no files in scope to bootstrap[/yellow]")
            return

        console.print(
            f"plan for [cyan]{model_id}[/cyan] — {len(plan.items)} files, "
            f"~${plan.total_estimated_cost:.4f} estimated"
        )
        for it in plan.items[:10]:
            console.print(
                f"  • [bold]{it.file_path}[/bold] "
                f"({it.public_symbols} symbols, score {it.score:.0f}, ~${it.estimated.cost_usd:.4f})"
            )
        if len(plan.items) > 10:
            console.print(f"  … and {len(plan.items) - 10} more")

        if dry_run:
            console.print("\n[yellow]dry-run: no API calls made[/yellow]")
            return

        client = make_client(model_id)
        with console.status("generating docs…"):
            result = run_bootstrap(
                plan=plan,
                project_root=project_root,
                config=config,
                client=client,
                pricing=pricing,
                budget_usd=budget,
                limit=limit,
            )

    console.print(
        f"[green]✓[/green] synced {result.files_synced} files "
        f"(skipped {result.files_skipped_no_budget} due to budget/limit)"
    )
    console.print(
        f"  estimated ${result.estimated_cost_usd:.4f} · actual ${result.actual_cost_usd:.4f}"
    )


def _run_incremental_sync(*, model: str | None, budget: float | None, limit: int | None) -> None:
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.cascade
    pricing = get_pricing(model_id)
    client = make_client(model_id)

    db_path = project_root / ".trie" / "graph.db"
    with Store(db_path) as store, console.status("running cascade…"):
        result = run_incremental(
            project_root=project_root,
            config=config,
            store=store,
            client=client,
            pricing=pricing,
            budget_usd=budget,
            limit=limit,
        )

    if result.orphan_docs_removed:
        for doc in result.orphan_docs_removed:
            console.print(f"[red]✗[/red] removed orphan doc {doc.relative_to(project_root)}")

    if result.files_synced == 0 and result.directly_stale_count == 0:
        if result.orphan_docs_removed:
            console.print(
                f"[green]✓[/green] cleaned up {len(result.orphan_docs_removed)} orphan(s); "
                "doc tree is otherwise coherent"
            )
        else:
            console.print("[green]✓[/green] doc tree is coherent — nothing to sync")
        return

    console.print(
        f"[green]✓[/green] synced {result.files_synced} file(s) "
        f"({result.directly_stale_count} directly stale, "
        f"{result.cascaded_count} pulled in by the cascade)"
    )
    if result.files_skipped_no_budget:
        console.print(f"  skipped {result.files_skipped_no_budget} due to budget/limit")
    console.print(f"  actual cost: ${result.actual_cost_usd:.4f}")


@app.command("diff")
def diff_cmd(
    budget: float | None = typer.Option(
        None,
        "--budget",
        help="USD budget cap. Stops once cumulative actual cost reaches this.",
    ),
    limit: int | None = typer.Option(
        None,
        "--limit",
        help="Maximum stale files to preview.",
    ),
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model.",
    ),
) -> None:
    """Preview what `trie sync` would change. Writes regenerated docs to .trie/preview/.

    Identifies stale source files via the same logic as `trie check`, regenerates their
    docs to `.trie/preview/<path>.md`, and prints a unified diff against the live tree.
    Makes API calls — pass --budget USD or --limit N to cap.
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        console.print(f"[red]error:[/red] {exc}")
        raise typer.Exit(code=1) from exc

    model_id = model or config.models.bootstrap
    pricing = get_pricing(model_id)
    client = make_client(model_id)

    with console.status("computing diffs…"):
        result = diff_project(
            project_root=project_root,
            config=config,
            client=client,
            pricing=pricing,
            budget_usd=budget,
            limit=limit,
        )

    if not result.diffs:
        console.print("[green]✓[/green] no stale docs — nothing to preview")
        return

    for fd in result.diffs:
        console.print(f"\n[bold cyan]{fd.canonical_doc_path.relative_to(project_root)}[/bold cyan]")
        if fd.unified_diff:
            console.print(fd.unified_diff, end="")
        else:
            console.print("  (no textual diff — possibly only fingerprint changes)")

    console.print(
        f"\n[green]✓[/green] previewed {len(result.diffs)} file(s); "
        f"actual cost ${result.actual_cost_usd:.4f} · "
        f"skipped {result.files_skipped_no_budget} due to budget/limit"
    )


@app.command("mcp")
def mcp_cmd() -> None:
    """Start the trie MCP server over stdio.

    Designed to be spawned by an agent harness (Claude Code, Codex, etc.) as a subprocess.
    The server is read-only — it queries the existing graph DB and doc tree but never
    modifies them. Run `trie scan && trie sync` first to populate state worth querying.
    """
    try:
        config, project_root = Config.find_and_load(Path.cwd())
    except ConfigNotFoundError as exc:
        # Don't print to stdout — that would corrupt the MCP protocol.
        import sys

        print(f"trie mcp: {exc}", file=sys.stderr)
        raise typer.Exit(code=1) from exc
    _ = config  # Config validated; the actual loading happens inside run_mcp_stdio.
    run_mcp_stdio(project_root)


if __name__ == "__main__":
    app()
