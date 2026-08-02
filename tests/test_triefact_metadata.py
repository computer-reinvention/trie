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


def test_defines_carry_exact_parser_signatures(project: Path):
    """Every function/method/class entry in `defines` records the exact one-line
    signature — keyword-only `*` and positional-only `/` markers included."""
    (project / "src" / "alpha.py").write_text(
        "def alpha(a, /, b, *, c: int = 1) -> str:\n"
        "    return 'x'\n\n\n"
        "class A:\n"
        "    def m(self, *, flag: bool = False) -> None:\n"
        "        pass\n"
    )
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    by_qname = {d["qualified_name"]: d for d in fm["defines"]}
    assert by_qname["src/alpha:alpha"]["signature"] == "def alpha(a, /, b, *, c: int = 1) -> str"
    assert by_qname["src/alpha:A"]["signature"] == "class A"
    assert by_qname["src/alpha:A.m"]["signature"] == "def m(self, *, flag: bool = False) -> None"


def test_defines_squeeze_multiline_signatures_to_one_line(project: Path):
    (project / "src" / "alpha.py").write_text(
        "def alpha(\n    a: int,\n    *,\n    b: str = 'x',\n) -> int:\n    return a\n"
    )
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    sig = {d["qualified_name"]: d for d in fm["defines"]}["src/alpha:alpha"]["signature"]
    assert "\n" not in sig
    assert sig == "def alpha( a: int, *, b: str = 'x', ) -> int"


def test_defines_omit_signature_for_constants_and_modules(project: Path):
    """Signatureless kinds (constants, the synthetic `__module__` symbol) omit
    the `signature` key entirely rather than emitting a fake/null value."""
    (project / "src" / "alpha.py").write_text(
        "CONSTANT = 42\n\nprint('module-level side effect')\n"
    )
    triefact = _sync(project, with_store=False)
    fm = _front_matter(triefact)
    by_qname = {d["qualified_name"]: d for d in fm["defines"]}
    assert by_qname["src/alpha:CONSTANT"]["kind"] == "constant"
    assert "signature" not in by_qname["src/alpha:CONSTANT"]
    assert by_qname["src/alpha:__module__"]["kind"] == "module"
    assert "signature" not in by_qname["src/alpha:__module__"]


def test_section_bodies_start_with_parser_derived_heading(project: Path):
    """The `## `signature`` heading is injected mechanically at upsert time —
    an LLM that omits the heading entirely cannot cause signature loss."""
    from trie.sync.writer import TriefactFile

    (project / "src" / "alpha.py").write_text(
        "def alpha(a, *, b: int = 1) -> str:\n    return 'x'\n"
    )
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "src" / "alpha.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(output_body="Prose with no heading at all."),
    )
    tf = TriefactFile.parse((project / "triefacts" / "src" / "alpha.md").read_text())
    section = tf.get_section("src/alpha:alpha")
    assert section is not None
    assert section.body.startswith("## `def alpha(a, *, b: int = 1) -> str`\n\n")
    assert "Prose with no heading at all." in section.body


def test_stale_llm_heading_is_replaced_with_parser_signature(project: Path):
    """An LLM that emits a mangled `## ...` heading (dropped `*`, elided params)
    gets it replaced with the parser-derived one."""
    from trie.sync.writer import TriefactFile

    (project / "src" / "alpha.py").write_text(
        "def alpha(a, *, b: int = 1) -> str:\n    return 'x'\n"
    )
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "src" / "alpha.py",
        project_root=project,
        config=config,
        client=FakeTrieClient(output_body="## `alpha(a, b)`\n\nDoes the thing."),
    )
    tf = TriefactFile.parse((project / "triefacts" / "src" / "alpha.md").read_text())
    section = tf.get_section("src/alpha:alpha")
    assert section is not None
    assert section.body == "## `def alpha(a, *, b: int = 1) -> str`\n\nDoes the thing."
    assert "alpha(a, b)" not in section.body


def test_metadata_refresh_migrates_pre_signature_tree_without_llm(project: Path):
    """`trie sync --metadata-only` on a pre-fix tree adds frontmatter signatures
    AND normalizes section-body headings — signatures come from re-parsing the
    source, so no LLM call and no regeneration is needed."""
    from trie.sync.single_file import refresh_triefact_metadata
    from trie.sync.writer import TriefactFile, hash_body

    (project / "src" / "alpha.py").write_text(
        "def alpha(a, *, b: int = 1) -> str:\n    return 'x'\n"
    )
    triefact_path = _sync(project, with_store=False)

    # Doctor the triefact into its pre-fix shape: strip the `signature` keys from
    # `defines` and replace the injected body heading with a stale LLM-style one.
    tf = TriefactFile.parse(triefact_path.read_text())
    for entry in tf.front_matter["defines"]:
        entry.pop("signature", None)
    old = tf.get_section("src/alpha:alpha")
    assert old is not None
    tf.upsert_section(
        qualified_name=old.qualified_name,
        fingerprint=old.fingerprint,
        body="## `alpha(a, b)`\n\nGenerated.",
        source_ref=old.source_ref,
        role=old.role,
    )
    triefact_path.write_text(tf.render())

    config, _ = Config.find_and_load(project)
    result = refresh_triefact_metadata(
        project / "src" / "alpha.py", project_root=project, config=config
    )
    assert result.changed is True

    migrated = TriefactFile.parse(triefact_path.read_text())
    fm_sig = {d["qualified_name"]: d for d in migrated.front_matter["defines"]}[
        "src/alpha:alpha"
    ].get("signature")
    assert fm_sig == "def alpha(a, *, b: int = 1) -> str"
    section = migrated.get_section("src/alpha:alpha")
    assert section is not None
    assert section.body == "## `def alpha(a, *, b: int = 1) -> str`\n\nGenerated."
    # Source fingerprint untouched; body_fp recomputed for the new body.
    assert section.fingerprint == old.fingerprint
    assert section.body_fingerprint == hash_body(section.body)

    # Idempotent: a second refresh is a byte-level no-op.
    again = refresh_triefact_metadata(
        project / "src" / "alpha.py", project_root=project, config=config
    )
    assert again.changed is False


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
