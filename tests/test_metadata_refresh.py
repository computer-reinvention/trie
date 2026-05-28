"""Metadata-only triefact refresh.

The contract under test:

  - `refresh_triefact_metadata` rewrites a triefact's front matter from the live
    store and **does not** call the LLM.
  - Section bodies and section fingerprints stay byte-identical: prose is a
    function of source, not of edge counts.
  - `last_synced_at` is preserved from the previous triefact; the refresh path
    must not bump it (semantically reserved for "the LLM ran").
  - When `incoming_refs` or `outgoing_refs` change because the graph changed,
    those are the deltas that show up.
  - `trie verify` stays green after a refresh: the same source / same fingerprint
    pair on the section body is what verify checks.
  - Idempotent: re-running a refresh after the first one is a no-op.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

from tests.fake_client import FakeTrieClient
from trie.check import check_project
from trie.config import Config
from trie.graph.store import Store
from trie.scan import scan_project
from trie.sync.single_file import (
    MetadataRefreshResult,
    refresh_triefact_metadata,
    sync_single_file,
)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Two-module project with a cross-file edge. Used to exercise refs counts."""
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "alpha.py").write_text('"""Alpha module."""\n\n\ndef alpha_fn():\n    return 1\n')
    (src / "beta.py").write_text(
        '"""Beta module."""\n\n'
        "from src.alpha import alpha_fn\n\n\n"
        "def beta_fn():\n"
        "    return alpha_fn() + 1\n"
    )
    return tmp_path


def _sync_both(project: Path) -> Store:
    """Scan + sync both modules so we have real triefacts on disk to refresh.

    Returns the open Store for the caller to use (and close)."""
    config, _ = Config.find_and_load(project)
    db = project / ".trie" / "graph.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    store = Store(db)
    scan_project(project_root=project, config=config, store=store)
    for name in ("alpha.py", "beta.py"):
        sync_single_file(
            project / "src" / name,
            project_root=project,
            config=config,
            client=FakeTrieClient(output_body="## `body`\n\nDeterministic prose."),
            store=store,
        )
    return store


def _read_yaml_front(triefact_path: Path) -> dict:
    """Parse the YAML front matter from a triefact file."""
    text = triefact_path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    assert match is not None, f"no YAML front matter in {triefact_path}"
    return yaml.safe_load(match.group(1))


def _section_bodies(triefact_path: Path) -> dict[str, str]:
    """Extract a {qname: section body} map from a triefact file.

    Used to assert that the body bytes between sentinels are preserved verbatim
    across a metadata-only refresh.
    """
    text = triefact_path.read_text()
    out: dict[str, str] = {}
    pattern = re.compile(
        r"<!-- trie:section symbol=(?P<qname>[^\s]+) [^>]*-->\n(?P<body>.*?)\n<!-- trie:end -->",
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        out[m.group("qname")] = m.group("body")
    return out


# ---------------------------------------------------------------------------
# Core contract
# ---------------------------------------------------------------------------


def test_refresh_does_not_call_the_llm(project: Path):
    """The whole point: refresh is free. A FakeClient passed in would never see
    a `generate` call. Easiest assertion: refresh works without a client at all."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)
        # No client argument exists on `refresh_triefact_metadata` — that's the
        # interface guarantee. We just call it and confirm it returns cleanly.
        result = refresh_triefact_metadata(
            project / "src" / "beta.py",
            project_root=project,
            config=config,
            store=store,
        )
        assert isinstance(result, MetadataRefreshResult)
    finally:
        store.close()


def test_refresh_preserves_section_bodies_byte_for_byte(project: Path):
    """Section sentinels and bodies must be untouched. Only YAML moves."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)
        triefact_path = project / "triefacts" / "src" / "beta.md"
        bodies_before = _section_bodies(triefact_path)
        sentinels_before = re.findall(r"<!-- trie:section [^>]+ -->", triefact_path.read_text())

        refresh_triefact_metadata(
            project / "src" / "beta.py",
            project_root=project,
            config=config,
            store=store,
        )

        bodies_after = _section_bodies(triefact_path)
        sentinels_after = re.findall(r"<!-- trie:section [^>]+ -->", triefact_path.read_text())
        assert bodies_before == bodies_after
        assert sentinels_before == sentinels_after
    finally:
        store.close()


def test_refresh_preserves_last_synced_at(project: Path):
    """The timestamp documents when the LLM last ran. Refresh must not bump it."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)
        triefact_path = project / "triefacts" / "src" / "beta.md"
        before = _read_yaml_front(triefact_path)
        before_ts = before["last_synced_at"]
        assert before_ts  # should be set by the initial sync

        refresh_triefact_metadata(
            project / "src" / "beta.py",
            project_root=project,
            config=config,
            store=store,
        )

        after = _read_yaml_front(triefact_path)
        assert after["last_synced_at"] == before_ts
    finally:
        store.close()


def test_refresh_picks_up_new_edges_in_front_matter(project: Path):
    """When the store learns new edges between syncs, refresh surfaces them in
    `incoming_refs` / `outgoing_refs`. We simulate the case by adding a third
    module that references `alpha_fn` *after* the initial sync, then refreshing
    alpha's metadata."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)

        alpha_triefact = project / "triefacts" / "src" / "alpha.md"
        before = _read_yaml_front(alpha_triefact)
        before_incoming = before.get("incoming_refs", 0)

        # Add a new module that references alpha_fn — increases inbound count by 1.
        (project / "src" / "gamma.py").write_text(
            "from src.alpha import alpha_fn\n\n\ndef gamma_fn():\n    return alpha_fn()\n"
        )
        scan_project(project_root=project, config=config, store=store)

        refresh_triefact_metadata(
            project / "src" / "alpha.py",
            project_root=project,
            config=config,
            store=store,
        )

        after = _read_yaml_front(alpha_triefact)
        assert after["incoming_refs"] == before_incoming + 1
    finally:
        store.close()


def test_refresh_is_idempotent(project: Path):
    """Re-running refresh after a successful refresh is a no-op (changed=False).
    Guard against accidental serialisation churn from the YAML round-trip."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)
        path = project / "src" / "beta.py"

        first = refresh_triefact_metadata(path, project_root=project, config=config, store=store)
        # Whatever the first call did (`changed` either way), the next call
        # must observe no further change.
        _ = first
        second = refresh_triefact_metadata(path, project_root=project, config=config, store=store)
        assert second.changed is False
    finally:
        store.close()


def test_refresh_skips_missing_triefact(project: Path, tmp_path: Path):
    """A source file with no triefact yet (e.g. a brand-new file that hasn't
    been synced) is a no-op — refresh doesn't *create* triefacts, only updates
    them. The CLI flow expects to walk every source file without error."""
    config, _ = Config.find_and_load(project)
    # Add a third source file but don't sync it.
    new_src = project / "src" / "delta.py"
    new_src.write_text('"""Delta module."""\n\n\ndef delta_fn():\n    return 0\n')

    result = refresh_triefact_metadata(new_src, project_root=project, config=config, store=None)
    assert result.changed is False


def test_verify_passes_after_refresh(project: Path):
    """`trie verify` checks section fingerprints, not edge counts. A metadata
    refresh must not introduce any drift detectable by verify."""
    store = _sync_both(project)
    try:
        config, _ = Config.find_and_load(project)
        # Sanity: verify is clean *before* refresh too. (`_sync_both` does a
        # cold-write so all sections match source.)
        check_before = check_project(project_root=project, config=config)
        assert check_before.is_clean, check_before.items

        for name in ("alpha.py", "beta.py"):
            refresh_triefact_metadata(
                project / "src" / name,
                project_root=project,
                config=config,
                store=store,
            )

        check_after = check_project(project_root=project, config=config)
        assert check_after.is_clean, check_after.items
    finally:
        store.close()


# ---------------------------------------------------------------------------
# CLI integration
# ---------------------------------------------------------------------------


def test_cli_sync_metadata_only_mutex_with_other_flags(
    project: Path, monkeypatch: pytest.MonkeyPatch
):
    """--metadata-only must be exclusive with --file / --all / --dry-run /
    --budget / --limit. Mixing them is operator error and we should reject it
    loudly rather than try to be clever about precedence."""
    from typer.testing import CliRunner

    from trie.cli import app

    monkeypatch.chdir(project)
    runner = CliRunner()

    cases = [
        ["sync", "--metadata-only", "--all"],
        ["sync", "--metadata-only", "--dry-run"],
        ["sync", "--metadata-only", "--budget", "1.0"],
        ["sync", "--metadata-only", "--limit", "1"],
        ["sync", "--metadata-only", "--file", "src/beta.py"],
    ]
    for argv in cases:
        result = runner.invoke(app, argv)
        assert result.exit_code == 1, f"expected mutex rejection for {argv}: {result.output}"
        assert "cannot be combined" in result.output


def test_cli_sync_metadata_only_runs(project: Path, monkeypatch: pytest.MonkeyPatch):
    """End-to-end: after a cold sync, `trie sync --metadata-only` runs cleanly
    and reports a refresh count without invoking the LLM."""
    from typer.testing import CliRunner

    from trie.cli import app

    # Cold-sync first so triefacts exist.
    store = _sync_both(project)
    store.close()

    monkeypatch.chdir(project)
    runner = CliRunner()
    # Patch make_client so even if the path somehow tried to construct one,
    # the test would fail loudly rather than fall back to a real API call.
    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda *_a, **_kw: (_ for _ in ()).throw(
            AssertionError("metadata-only path must not construct an LLM client")
        ),
    )
    result = runner.invoke(app, ["sync", "--metadata-only"])
    assert result.exit_code == 0, result.output
    assert "refreshed metadata" in result.output
