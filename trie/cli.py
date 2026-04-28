from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from trie import __version__
from trie.config import Config, ConfigNotFoundError
from trie.init import InitError, init_project
from trie.models import make_client
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


@app.command("sync")
def sync_cmd(
    file: Path | None = typer.Option(
        None,
        "--file",
        "-f",
        help="Sync a single source file. Other modes (--bootstrap, incremental cascade) are deferred to M2/M4.",
    ),
    model: str | None = typer.Option(
        None,
        "--model",
        help="Override the configured model, e.g. 'anthropic/claude-sonnet-4-6'.",
    ),
) -> None:
    """Generate or refresh trie documentation."""
    if file is None:
        console.print("[red]error:[/red] --file <path> is required in v0.1 (M1).")
        raise typer.Exit(code=1)

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


if __name__ == "__main__":
    app()
