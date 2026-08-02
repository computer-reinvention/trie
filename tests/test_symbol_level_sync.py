"""Symbol-level sync: regenerate only the symbols actually asked for.

The contract under test:
  - `sync_single_file(symbols_to_regen=None)` regenerates every parser-surfaced
    symbol — the explicit-force path used by `trie sync --file` and bootstrap.
  - `sync_single_file(symbols_to_regen={X, Y})` regenerates only X and Y; every
    other section in the file passes through byte-identically.
  - `sync_single_file(symbols_to_regen=set())` runs zero LLM calls and rewrites
    no sections, but still updates file-level front matter (last_synced_at).
  - `compute_incremental_worklist` populates `regen_qnames_by_file` correctly
    from a mix of directly-stale items and cascade-pulled qnames.
  - `run_incremental` end-to-end: a single-symbol edit in a multi-symbol file
    regenerates exactly that one symbol; every other section is byte-identical.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from tests.fake_client import FakeTrieClient
from trie.config import Config
from trie.graph.store import Store
from trie.scan import scan_project
from trie.sync.incremental import compute_incremental_worklist, run_incremental
from trie.sync.single_file import sync_single_file
from trie.sync.writer import TriefactFile

FIXTURE_DIR = Path(__file__).parent / "fixtures" / "tiny_repo"


def _make_project(tmp_path: Path) -> Path:
    root = tmp_path / "demo"
    shutil.copytree(FIXTURE_DIR, root)
    (root / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    return root


@pytest.fixture
def project(tmp_path: Path) -> Path:
    return _make_project(tmp_path)


# ---------------------------------------------------------------------------
# Direct sync_single_file contract
# ---------------------------------------------------------------------------


def test_symbols_to_regen_none_regens_every_symbol(project: Path):
    """The legacy / --file path: passing None regenerates everything (6 symbols)."""
    config, _ = Config.find_and_load(project)
    client = FakeTrieClient()

    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
        symbols_to_regen=None,
    )

    assert result.symbols_generated == 6
    assert result.symbols_skipped == 0
    assert client.calls == 6


def test_symbols_to_regen_subset_only_regenerates_listed_symbols(project: Path):
    """The symbol-level path: only listed qnames are sent to the LLM."""
    config, _ = Config.find_and_load(project)

    # First sync: cold-write the whole file so we have a complete triefact to skip
    # past on the next call.
    sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        # Markers must live in the prose, not the heading — the `## ...` heading
        # is mechanically replaced with the parser-derived signature at upsert.
        client=FakeTrieClient(output_body="## first run\n\nFirst-run prose."),
    )

    # Capture pre-state bytes for every section.
    triefact_path = project / "triefacts" / "calculator.md"
    pre = TriefactFile.parse(triefact_path.read_text())
    pre_sections = {s.qualified_name: s for s in pre.chunks if hasattr(s, "qualified_name")}

    # Second sync: ask to regen only `add`. Every other symbol must pass through.
    client = FakeTrieClient(output_body="## second run\n\nSecond-run prose.")
    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
        symbols_to_regen={"calculator:add"},
    )

    assert client.calls == 1  # only `add` hit the LLM
    assert result.symbols_generated == 1
    assert result.symbols_skipped == 5

    post = TriefactFile.parse(triefact_path.read_text())
    post_sections = {s.qualified_name: s for s in post.chunks if hasattr(s, "qualified_name")}

    # Untouched symbols: byte-identical body + body_fingerprint + fingerprint.
    untouched = set(pre_sections) - {"calculator:add"}
    for qname in untouched:
        assert post_sections[qname].body == pre_sections[qname].body, qname
        assert post_sections[qname].body_fingerprint == pre_sections[qname].body_fingerprint, qname
        assert post_sections[qname].fingerprint == pre_sections[qname].fingerprint, qname

    # The targeted symbol got a fresh body.
    assert post_sections["calculator:add"].body != pre_sections["calculator:add"].body


def test_symbols_to_regen_empty_set_runs_no_llm_calls(project: Path):
    """An empty set is the degenerate symbol-level case: nothing to regen, but the
    file's front matter still updates (we visited it)."""
    config, _ = Config.find_and_load(project)

    # Establish baseline.
    sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(),
    )
    triefact_path = project / "triefacts" / "calculator.md"
    pre_text = triefact_path.read_text()

    # Sync again with an empty regen set.
    client = FakeTrieClient()
    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
        symbols_to_regen=set(),
    )

    assert client.calls == 0
    assert result.symbols_generated == 0
    assert result.symbols_skipped == 6

    # All section bytes preserved; only front-matter timestamp (and equivalents) move.
    pre = TriefactFile.parse(pre_text)
    post = TriefactFile.parse(triefact_path.read_text())
    pre_secs = {s.qualified_name: s for s in pre.chunks if hasattr(s, "qualified_name")}
    post_secs = {s.qualified_name: s for s in post.chunks if hasattr(s, "qualified_name")}
    assert pre_secs.keys() == post_secs.keys()
    for q in pre_secs:
        assert post_secs[q].body == pre_secs[q].body


def test_symbols_to_regen_ignores_unknown_qnames(project: Path):
    """Qnames in the set that don't appear in current source are silently ignored —
    they're orphans handled by the file-level sweep, not regen targets."""
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(),
    )

    client = FakeTrieClient()
    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
        symbols_to_regen={"calculator:does_not_exist"},
    )

    assert client.calls == 0
    assert result.symbols_generated == 0
    assert result.symbols_skipped == 6


# ---------------------------------------------------------------------------
# Worklist projection
# ---------------------------------------------------------------------------


def _scanned_store(project: Path) -> Store:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    scan_project(project_root=project, config=config, store=store)
    return store


def test_worklist_collects_qnames_for_directly_stale_symbols(project: Path):
    """A symbol whose body changed should appear in `regen_qnames_by_file` under
    its file, scoped to exactly that qname (not the whole file)."""
    config, _ = Config.find_and_load(project)

    # Establish baseline triefacts so check has something to compare against.
    sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(),
    )
    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(),
    )

    # Edit one symbol's body in calculator.py.
    src = project / "calculator.py"
    text = src.read_text()
    edited = text.replace(
        'def add(a: float, b: float) -> float:\n    """Return the sum of two numbers."""\n    return a + b',
        'def add(a: float, b: float) -> float:\n    """Return the sum of two numbers."""\n    total = a + b\n    return total',
    )
    assert edited != text
    src.write_text(edited)

    with _scanned_store(project) as store:
        worklist = compute_incremental_worklist(project_root=project, config=config, store=store)

    assert "calculator.py" in worklist.directly_stale
    assert "calculator.py" in worklist.regen_qnames_by_file
    # Exactly the edited qname, nothing else from the file.
    assert worklist.regen_qnames_by_file["calculator.py"] == {"calculator:add"}


def test_worklist_omits_files_marked_missing_triefact(project: Path):
    """A file with no triefact at all gets the cold-write path
    (`symbols_to_regen=None`); the worklist signals this by NOT entering it
    into `regen_qnames_by_file`."""
    config, _ = Config.find_and_load(project)
    # Don't sync first — calculator.py and strings.py both have no triefact yet.

    with _scanned_store(project) as store:
        worklist = compute_incremental_worklist(project_root=project, config=config, store=store)

    # Both files are stale (MISSING_TRIEFACT) but neither should appear in the
    # per-symbol map. The runner will then pass None and regen everything in each.
    assert "calculator.py" in worklist.directly_stale
    assert "strings.py" in worklist.directly_stale
    assert "calculator.py" not in worklist.regen_qnames_by_file
    assert "strings.py" not in worklist.regen_qnames_by_file


# ---------------------------------------------------------------------------
# End-to-end via run_incremental
# ---------------------------------------------------------------------------


def test_run_incremental_regenerates_only_changed_symbol(project: Path):
    """The big one: a single-symbol edit propagates to a single-symbol regen.
    Every other section in the file is byte-identical to its pre-edit state."""
    config, _ = Config.find_and_load(project)

    # Cold-bootstrap both fixture files.
    for f in ("calculator.py", "strings.py"):
        sync_single_file(
            project / f,
            project_root=project,
            config=config,
            client=FakeTrieClient(),
        )

    triefact_path = project / "triefacts" / "calculator.md"
    pre = TriefactFile.parse(triefact_path.read_text())
    pre_secs = {s.qualified_name: s for s in pre.chunks if hasattr(s, "qualified_name")}

    # Edit `add` — same content edit as the worklist test above.
    src = project / "calculator.py"
    src.write_text(
        src.read_text().replace(
            'def add(a: float, b: float) -> float:\n    """Return the sum of two numbers."""\n    return a + b',
            'def add(a: float, b: float) -> float:\n    """Return the sum of two numbers."""\n    total = a + b\n    return total',
        )
    )

    client = FakeTrieClient()
    with Store(project / ".trie" / "graph.db") as store:
        result = run_incremental(
            project_root=project,
            config=config,
            store=store,
            client=client,
        )

    # Exactly one symbol regenerated across the whole run (no cascade hits in this fixture).
    assert client.calls == 1
    total_generated = sum(r.symbols_generated for r in result.sync_results)
    total_skipped = sum(r.symbols_skipped for r in result.sync_results)
    assert total_generated == 1
    assert total_skipped >= 5  # the other 5 symbols in calculator.py are pass-through

    # Per-section byte equality for the untouched ones.
    post = TriefactFile.parse(triefact_path.read_text())
    post_secs = {s.qualified_name: s for s in post.chunks if hasattr(s, "qualified_name")}
    for qname, pre_sec in pre_secs.items():
        if qname == "calculator:add":
            continue
        assert post_secs[qname].body == pre_sec.body, qname
        assert post_secs[qname].body_fingerprint == pre_sec.body_fingerprint, qname


def test_underscored_symbols_are_documented_and_can_go_stale(project: Path):
    """Sanity: with `is_public` no longer a filter, an underscored symbol gets
    a section and is checked for staleness the same as any other symbol."""
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(),
    )

    triefact_path = project / "triefacts" / "calculator.md"
    triefact = TriefactFile.parse(triefact_path.read_text())
    qnames = triefact.section_qnames()
    assert "calculator:_internal_helper" in qnames

    # Edit the underscored helper's body and confirm check flags it stale.
    src = project / "calculator.py"
    src.write_text(
        src.read_text().replace("return x * 2", "return x * 3"),
    )

    from trie.check import StaleReason, check_project

    result = check_project(project_root=project, config=config)
    stale_qnames = {
        it.qualified_name for it in result.items if it.reason == StaleReason.STALE_SECTION
    }
    assert "calculator:_internal_helper" in stale_qnames


# ---------------------------------------------------------------------------
# CLI `trie sync --file`: stale-only by default, --force for a full rewrite.
# ---------------------------------------------------------------------------


def _cli_file_sync(project: Path, monkeypatch: pytest.MonkeyPatch, *args: str):
    """Invoke `trie sync --file calculator.py [...args]` with a captured fake client."""
    from typer.testing import CliRunner

    from trie.cli import app

    clients: list[FakeTrieClient] = []

    def _fake_make_client(*_a, **_kw):
        client = FakeTrieClient(output_body="## regenerated")
        clients.append(client)
        return client

    monkeypatch.setattr("trie.cli.make_client", _fake_make_client)
    monkeypatch.chdir(project)
    result = CliRunner().invoke(app, ["sync", "--file", "calculator.py", *args])
    return result, clients


def test_cli_file_sync_fresh_file_is_a_free_noop(project: Path, monkeypatch: pytest.MonkeyPatch):
    """A fully-fresh file must not construct a client or call the LLM at all."""
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "calculator.py", project_root=project, config=config, client=FakeTrieClient()
    )

    result, clients = _cli_file_sync(project, monkeypatch)
    assert result.exit_code == 0, result.output
    assert "all symbols fresh" in result.output
    assert "--force" in result.output
    assert clients == [], "fresh file must not even construct an LLM client"


def test_cli_file_sync_regenerates_only_stale_symbols(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """Regression: `--file` used to re-bill every symbol in the file when only
    one had changed (123 regens for a 2-symbol edit). Default is now the same
    stale-subset the incremental path uses."""
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "calculator.py", project_root=project, config=config, client=FakeTrieClient()
    )

    src = project / "calculator.py"
    src.write_text(src.read_text().replace("return a + b", "return b + a"))

    result, clients = _cli_file_sync(project, monkeypatch)
    assert result.exit_code == 0, result.output
    assert len(clients) == 1
    assert clients[0].calls == 1, "only the edited symbol may hit the LLM"
    assert "1 symbols regenerated" in result.output
    assert "5 fresh passed through" in result.output


def test_cli_file_sync_force_rewrites_everything(project: Path, monkeypatch: pytest.MonkeyPatch):
    """--force keeps the old full-rewrite semantics (smoke-test path)."""
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "calculator.py", project_root=project, config=config, client=FakeTrieClient()
    )

    result, clients = _cli_file_sync(project, monkeypatch, "--force")
    assert result.exit_code == 0, result.output
    assert len(clients) == 1
    assert clients[0].calls == 6, "--force regenerates every symbol"


def test_cli_file_sync_never_synced_file_gets_full_cold_write(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """A file with no triefact yet regenerates everything (cold write)."""
    result, clients = _cli_file_sync(project, monkeypatch)
    assert result.exit_code == 0, result.output
    assert len(clients) == 1
    assert clients[0].calls == 6
