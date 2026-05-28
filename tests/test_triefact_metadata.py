"""Front-matter enrichment in `sync_single_file`.

Covers the metadata block trie writes alongside each triefact: timestamps, file
description (from the module docstring), the public-symbol roster, and cross-file
reference counts when a Store is provided.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from tests.fake_client import FakeTrieClient
from trie.config import Config
from trie.graph.store import Store
from trie.parse.python import extract_module_docstring, strip_string_literal
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file


@pytest.fixture
def project(tmp_path: Path) -> Path:
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
    (src / "alpha.py").write_text(
        '"""Alpha module: utilities for the alpha workflow.\n\n'
        "Multi-line detail that should not appear in description.\n"
        '"""\n\n'
        "from src.beta import beta\n\n\n"
        "def alpha():\n    return beta() + 1\n\n\n"
        "class A:\n    def m(self):\n        return alpha()\n"
    )
    (src / "beta.py").write_text("def beta():\n    return 2\n")
    return tmp_path


def _front_matter(path: Path) -> dict:
    """Parse YAML front matter directly so we can assert structured fields."""
    text = path.read_text()
    assert text.startswith("---\n")
    end = text.index("\n---\n", 4)
    return yaml.safe_load(text[4:end])


def _sync(project: Path, *, with_store: bool) -> Path:
    config, _ = Config.find_and_load(project)
    if with_store:
        with Store(project / ".trie" / "graph.db") as store:
            scan_project(project_root=project, config=config, store=store)
            sync_single_file(
                project / "src" / "alpha.py",
                project_root=project,
                config=config,
                client=FakeTrieClient(output_body="## `body`\n\nGenerated."),
                store=store,
            )
    else:
        sync_single_file(
            project / "src" / "alpha.py",
            project_root=project,
            config=config,
            client=FakeTrieClient(output_body="## `body`\n\nGenerated."),
        )
    return project / "triefacts" / "src" / "alpha.md"


def test_front_matter_carries_description_from_module_docstring(project: Path):
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    assert fm["description"] == "Alpha module: utilities for the alpha workflow."


def test_front_matter_omits_description_when_no_module_docstring(project: Path):
    (project / "src" / "alpha.py").write_text("def alpha():\n    return 1\n")
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    assert "description" not in fm


def test_front_matter_lists_public_symbols_in_source_order(project: Path):
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    qnames = [d["qualified_name"] for d in fm["defines"]]
    assert qnames == ["src/alpha:alpha", "src/alpha:A", "src/alpha:A.m"]
    kinds = [d["kind"] for d in fm["defines"]]
    assert kinds == ["function", "class", "method"]


def test_front_matter_carries_iso8601_timestamp(project: Path):
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    ts = fm["last_synced_at"]
    assert isinstance(ts, str)
    assert ts.endswith("Z")
    # Parse as ISO 8601 to validate the format.
    from datetime import datetime

    datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")


def test_front_matter_includes_ref_counts_when_store_provided(project: Path):
    triefact = _sync(project, with_store=True)
    fm = _front_matter(triefact)
    assert fm["incoming_refs"] == 0  # nothing in alpha is called from elsewhere
    # alpha.py imports from beta.py — exactly one cross-file outbound edge.
    assert fm["outgoing_refs"] == 1


def test_front_matter_omits_ref_counts_when_store_omitted(project: Path):
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    assert "incoming_refs" not in fm
    assert "outgoing_refs" not in fm


def test_extract_module_docstring_handles_triple_and_single(tmp_path: Path):
    f = tmp_path / "a.py"
    f.write_text('"""triple double."""\n\ndef x(): ...\n')
    raw = extract_module_docstring(f)
    assert raw is not None and strip_string_literal(raw) == "triple double."

    f.write_text("'single triple.'\n\ndef x(): ...\n")
    raw = extract_module_docstring(f)
    assert raw is not None and strip_string_literal(raw) == "single triple."


def test_extract_module_docstring_returns_none_when_first_stmt_is_code(tmp_path: Path):
    f = tmp_path / "a.py"
    f.write_text("import os\n\ndef x(): ...\n")
    assert extract_module_docstring(f) is None


def test_strip_string_literal_handles_prefixes():
    assert strip_string_literal('r"""raw triple."""') == "raw triple."
    assert strip_string_literal("rb'raw bytes'") == "raw bytes"
    assert strip_string_literal('f"f-string."') == "f-string."


def test_store_file_ref_counts_excludes_intra_file_edges(project: Path):
    """Intra-file references must not show up in incoming/outgoing — those counts
    surface external coupling, not within-file internal calls."""
    config, _ = Config.find_and_load(project)
    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        # alpha.py: alpha() and A.m() reference each other intra-file. Outbound is the
        # single cross-file ref to beta. Inbound is zero.
        inbound, outbound = store.file_ref_counts("src/alpha.py")
        assert (inbound, outbound) == (0, 1)
        inbound, outbound = store.file_ref_counts("src/beta.py")
        # beta is called from alpha — exactly one inbound, no outbound.
        assert (inbound, outbound) == (1, 0)
