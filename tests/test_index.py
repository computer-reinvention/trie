from __future__ import annotations

from pathlib import Path

from trie.config import Config
from trie.graph.store import Store
from trie.index import INDEX_MARKER, build_index, write_index
from trie.parse.python import extract_symbols
from trie.sync.writer import TriefactFile


def _project(tmp_path: Path) -> tuple[Config, Store]:
    (tmp_path / "trie.toml").write_text("[trie]\nversion = '0.0.0'\n")
    src = tmp_path / "pkg"
    src.mkdir()
    (src / "lib.py").write_text(
        "def slugify(text):\n    return text\n\n\ndef _private(x):\n    return x\n"
    )
    (tmp_path / "app.py").write_text(
        "from pkg.lib import slugify\n\ndef go():\n    return slugify('t')\n"
    )

    config = Config.from_dict({})
    store = Store(tmp_path / ".trie" / "graph.db")
    for rel in ("pkg/lib.py", "app.py"):
        store.upsert_file(path=rel, fingerprint="fp")
        store.replace_file_symbols(rel, extract_symbols(tmp_path / rel, tmp_path))
    store.replace_all_edges(
        {"app.py": []}  # edges built via references normally; inject one manually below
    )
    # Manually add an edge app:go -> pkg/lib:slugify for inbound ranking.
    ids = {
        row[0]: row[1]
        for row in store._conn.execute("SELECT qualified_name, id FROM symbols").fetchall()
    }
    store._conn.execute(
        "INSERT INTO edges (src_symbol_id, dst_symbol_id, kind) VALUES (?, ?, 'call')",
        (ids["app:go"], ids["pkg/lib:slugify"]),
    )
    # One-liner for the entry point (index only lists symbols that have one).
    store._conn.execute(
        "INSERT INTO triefact_sections "
        "(triefact_path, symbol_id, section_fingerprint, one_liner, role, last_generated_at) "
        "VALUES (?, ?, ?, ?, ?, 0)",
        (
            "triefacts/pkg/lib.md",
            ids["pkg/lib:slugify"],
            "fp1",
            "Return text unchanged (placeholder slug).",
            "util",
        ),
    )
    store._conn.commit()

    # Triefact tree with front-matter descriptions + a digest archive to skip.
    tf_root = tmp_path / "triefacts"
    (tf_root / "pkg").mkdir(parents=True)
    tf = TriefactFile.empty()
    tf.front_matter["description"] = "String helpers."
    tf.upsert_section(qualified_name="pkg/lib:slugify", fingerprint="fp1", body="Slug.")
    (tf_root / "pkg" / "lib.md").write_text(tf.render())
    tf2 = TriefactFile.empty()
    tf2.front_matter["description"] = "App wiring."
    tf2.upsert_section(qualified_name="app:go", fingerprint="fp2", body="Go.")
    (tf_root / "app.md").write_text(tf2.render())
    (tf_root / "triediffs").mkdir()
    (tf_root / "triediffs" / "x.md").write_text("## digest entry — (parent abc)\n")
    return config, store


def test_build_index_shape(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    try:
        text = build_index(store=store, config=config, project_root=tmp_path)
    finally:
        store.close()

    assert INDEX_MARKER in text
    # Entry points: linked, ranked, one-liner shown; private symbols absent.
    assert "[`pkg/lib:slugify`](pkg/lib.md)" in text
    assert "Return text unchanged" in text
    assert "_private" not in text
    # Files section: per-directory grouping with descriptions.
    assert "### pkg" in text
    assert "[lib.md](pkg/lib.md) — String helpers." in text
    assert "[app.md](app.md) — App wiring." in text
    # Digest archive and the index itself never appear in the TOC.
    assert "triediffs" not in text
    assert "[README.md]" not in text


def test_write_index_and_idempotence(tmp_path: Path) -> None:
    config, store = _project(tmp_path)
    try:
        path = write_index(store=store, config=config, project_root=tmp_path)
        assert path is not None and path.name == "README.md"
        first = path.read_text()
        path2 = write_index(store=store, config=config, project_root=tmp_path)
        assert path2 == path
        assert path.read_text() == first, "index generation must be deterministic"
    finally:
        store.close()


def test_write_index_without_tree_is_noop(tmp_path: Path) -> None:
    (tmp_path / "trie.toml").write_text("[trie]\nversion = '0.0.0'\n")
    config = Config.from_dict({})
    store = Store(tmp_path / ".trie" / "graph.db")
    try:
        assert write_index(store=store, config=config, project_root=tmp_path) is None
    finally:
        store.close()
