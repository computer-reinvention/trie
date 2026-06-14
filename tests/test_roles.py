"""Tests for role tagging: durable persistence, derived taxonomy, and the
two-pass roles-only classification.

Roles are a project-specific vocabulary trie derives once and classifies every
symbol against. The vocabulary and the per-symbol tags must survive a graph.db
wipe (the DB is a regenerable cache; the triefact files are the source of truth),
and the user must never need to run the roles flow by hand.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from tests.fake_client import FakeTrieClient
from trie.config import Config
from trie.graph.store import Store
from trie.scan import scan_project
from trie.sync.bootstrap import build_plan, run_bootstrap
from trie.sync.roles import run_roles_only
from trie.sync.single_file import backfill_section_records
from trie.sync.taxonomy import Role, Taxonomy, derive_taxonomy, load_taxonomy, save_taxonomy
from trie.sync.writer import TriefactFile

# ---------------------------------------------------------------------------
# Writer: role survives the parse → render round-trip.
# ---------------------------------------------------------------------------


def test_section_role_round_trips_through_render_and_parse():
    tf = TriefactFile()
    tf.upsert_section(
        qualified_name="mod:fn",
        fingerprint="abc",
        body="## `fn`\n\nDoes a thing.",
        role="persistence",
    )
    rendered = tf.render()
    assert "role=persistence" in rendered

    reparsed = TriefactFile.parse(rendered)
    section = reparsed.get_section("mod:fn")
    assert section is not None
    assert section.role == "persistence"


def test_section_without_role_omits_the_field():
    tf = TriefactFile()
    tf.upsert_section(qualified_name="mod:fn", fingerprint="abc", body="## `fn`\n\nThing.")
    rendered = tf.render()
    assert "role=" not in rendered
    assert TriefactFile.parse(rendered).get_section("mod:fn").role == ""


def test_set_section_role_only_changes_the_role():
    tf = TriefactFile()
    tf.upsert_section(
        qualified_name="mod:fn", fingerprint="abc", body="## `fn`\n\nThing.", role="domain"
    )
    before = tf.get_section("mod:fn")
    assert tf.set_section_role("mod:fn", "api") is True
    after = tf.get_section("mod:fn")
    assert after.role == "api"
    # Body and fingerprints untouched — a roles pass is a minimal diff.
    assert after.body == before.body
    assert after.fingerprint == before.fingerprint
    assert after.body_fingerprint == before.body_fingerprint


def test_set_section_role_missing_symbol_returns_false():
    tf = TriefactFile()
    assert tf.set_section_role("mod:absent", "api") is False


# ---------------------------------------------------------------------------
# Taxonomy persistence.
# ---------------------------------------------------------------------------


def test_taxonomy_save_load_round_trip(tmp_path: Path):
    config = _write_config(tmp_path)
    tax = Taxonomy(
        roles=(Role("domain", "core logic"), Role("persistence", "storage")),
    )
    path = save_taxonomy(tmp_path, config, tax)
    assert path.exists()

    loaded = load_taxonomy(tmp_path, config)
    assert loaded is not None
    assert loaded.names() == ["domain", "persistence"]


def test_load_taxonomy_absent_returns_none(tmp_path: Path):
    config = _write_config(tmp_path)
    assert load_taxonomy(tmp_path, config) is None


def test_load_taxonomy_malformed_returns_none(tmp_path: Path):
    config = _write_config(tmp_path)
    path = tmp_path / config.triefacts.root / "role_taxonomy.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("{ not json")
    assert load_taxonomy(tmp_path, config) is None


# ---------------------------------------------------------------------------
# derive_taxonomy: surveys the store, returns the model's proposed vocab.
# ---------------------------------------------------------------------------


def test_derive_taxonomy_returns_proposed_roles(project: Path):
    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        client = FakeTrieClient(
            output_taxonomy=[("entrypoint", "cli"), ("domain", "logic"), ("util", "helpers")]
        )
        result = derive_taxonomy(store=store, client=client)
    assert result.taxonomy.names() == ["entrypoint", "domain", "util"]
    assert client.last_output_type.__name__ == "RoleTaxonomy"


# ---------------------------------------------------------------------------
# run_roles_only: end-to-end. Derives a taxonomy, classifies every symbol,
# persists roles to both the sentinel (disk) and the store (DB).
# ---------------------------------------------------------------------------


def test_run_roles_only_persists_to_disk_and_db(project: Path):
    config, _ = Config.find_and_load(project)
    _bootstrap(project, config)

    with Store(project / ".trie" / "graph.db") as store:
        client = FakeTrieClient(
            output_role="domain",
            output_taxonomy=[("domain", "logic"), ("util", "helpers")],
        )
        result = run_roles_only(project_root=project, config=config, store=store, client=client)
        assert result.taxonomy_derived is True
        assert result.symbols_classified > 0
        # DB now has roles.
        assert store.count_symbols_missing_role() == 0

    # Disk now carries role= in the sentinels.
    triefact = (project / "triefacts" / "src" / "alpha.md").read_text()
    assert "role=domain" in triefact

    # And the taxonomy file is committed alongside the tree.
    assert load_taxonomy(project, config) is not None


def test_roles_survive_db_wipe_via_disk_restore(project: Path):
    """The whole point: roles persisted on disk are recovered for free on a
    graph rebuild, no LLM call required."""
    config, _ = Config.find_and_load(project)
    _bootstrap(project, config)
    with Store(project / ".trie" / "graph.db") as store:
        run_roles_only(
            project_root=project,
            config=config,
            store=store,
            client=FakeTrieClient(output_role="domain"),
        )

    # Wipe the DB.
    (project / ".trie" / "graph.db").unlink()

    # Rebuild from scratch: scan + backfill from disk. No client needed.
    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        backfill_section_records(project, config, store)
        assert store.count_symbols_missing_role() == 0


def test_run_roles_only_only_missing_short_circuits(project: Path):
    """When every symbol already has a role, only_missing makes zero LLM calls
    and derives no taxonomy."""
    config, _ = Config.find_and_load(project)
    _bootstrap(project, config)
    with Store(project / ".trie" / "graph.db") as store:
        run_roles_only(
            project_root=project,
            config=config,
            store=store,
            client=FakeTrieClient(output_role="domain"),
        )
        assert store.count_symbols_missing_role() == 0

        probe = FakeTrieClient(output_role="domain")
        result = run_roles_only(
            project_root=project,
            config=config,
            store=store,
            client=probe,
            only_missing=True,
        )
    assert probe.calls == 0
    assert result.taxonomy_derived is False
    assert result.symbols_classified == 0


def test_infer_role_clamps_to_vocabulary(project: Path):
    """A role outside the taxonomy is dropped to '' rather than polluting the axis."""
    config, _ = Config.find_and_load(project)
    _bootstrap(project, config)
    with Store(project / ".trie" / "graph.db") as store:
        # Client returns 'made-up-role', not in the taxonomy → clamped to ''.
        client = FakeTrieClient(
            output_role="made-up-role",
            output_taxonomy=[("domain", "logic"), ("util", "helpers")],
        )
        result = run_roles_only(project_root=project, config=config, store=store, client=client)
    # Nothing valid was assigned, so every symbol is still missing a role.
    assert result.roles_changed == 0


# ---------------------------------------------------------------------------
# Scaffolding.
# ---------------------------------------------------------------------------


def _write_config(root: Path) -> Config:
    (root / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["src/**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    config, _ = Config.find_and_load(root)
    return config


def _git(args: list[str], cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    _write_config(tmp_path)
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "alpha.py").write_text('"""Alpha."""\n\n\ndef alpha_fn():\n    return 1\n')
    (src / "beta.py").write_text(
        '"""Beta."""\n\nfrom src.alpha import alpha_fn\n\n\ndef beta_fn():\n    return alpha_fn() + 1\n'
    )
    _git(["init", "-q", "-b", "main"], tmp_path)
    _git(["config", "user.email", "t@e.com"], tmp_path)
    _git(["config", "user.name", "t"], tmp_path)
    _git(["add", "."], tmp_path)
    _git(["commit", "-q", "-m", "initial"], tmp_path)
    return tmp_path


def _bootstrap(project: Path, config: Config) -> None:
    """Generate triefacts for the fixture so role passes have sections to tag.

    Bootstrap with empty roles so the roles-only tests start from an untagged tree
    (mirrors a legacy/wiped tree that needs role backfill).
    """
    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        client = FakeTrieClient(output_role="", output_boundary="internal")
        plan = build_plan(project_root=project, store=store, model_id="fake/test", client=client)
        run_bootstrap(
            plan=plan,
            project_root=project,
            config=config,
            store=store,
            client=client,
            pricing=None,
            budget_usd=None,
            limit=None,
        )
