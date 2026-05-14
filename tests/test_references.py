from __future__ import annotations

from pathlib import Path

from trie.parse.references import extract_file_data


def _refs_by_src(file_data) -> dict[str, list[str]]:
    """Return src_qname -> sorted list of target_qnames."""
    out: dict[str, list[str]] = {}
    for r in file_data.references:
        out.setdefault(r.src_qname, []).append(r.target_qname)
    return {k: sorted(v) for k, v in out.items()}


def test_intra_file_function_calls_create_edges(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "def helper(x):\n    return x + 1\n\n\ndef wrapper(x):\n    return helper(x) + helper(x)\n"
    )
    fd = extract_file_data(f)
    refs = _refs_by_src(fd)
    assert "mod:wrapper" in refs
    assert "mod:helper" in refs["mod:wrapper"]
    # Edges should be deduplicated even if helper appears twice in the body.
    assert refs["mod:wrapper"].count("mod:helper") == 1


def test_intra_file_class_to_function_edge(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "def util():\n    return 1\n\n\nclass Service:\n    def run(self):\n        return util()\n"
    )
    fd = extract_file_data(f)
    refs = _refs_by_src(fd)
    assert "mod:util" in refs.get("mod:Service.run", [])


def test_imports_create_cross_file_edges(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text("from helpers import helper\n\n\ndef run():\n    return helper(1)\n")
    fd = extract_file_data(f)
    refs = _refs_by_src(fd)
    assert "helpers:helper" in refs.get("mod:run", [])


def test_aliased_import_resolves_to_original(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text("from helpers import helper as h\n\n\ndef run():\n    return h(1)\n")
    fd = extract_file_data(f)
    refs = _refs_by_src(fd)
    assert "helpers:helper" in refs.get("mod:run", [])


def test_dotted_module_import(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text("from foo.bar import baz\n\n\ndef run():\n    return baz()\n")
    fd = extract_file_data(f)
    refs = _refs_by_src(fd)
    assert "foo/bar:baz" in refs.get("mod:run", [])


def test_relative_imports_skipped(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "from . import sibling\nfrom .util import helper\n\n\ndef run():\n    return helper()\n"
    )
    fd = extract_file_data(f)
    # No edges from `mod:run` to anything — relative imports skipped in v0.1.
    refs = _refs_by_src(fd)
    assert refs.get("mod:run", []) == []


def test_no_self_references(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "def recursive(n):\n    if n == 0:\n        return 0\n    return recursive(n - 1)\n"
    )
    fd = extract_file_data(f)
    # Self-recursion should not produce a self-edge.
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:recursive"}
    assert "mod:recursive" not in targets


def test_unresolved_names_silently_dropped(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text("def run():\n    return some_global() + len([1, 2])\n")
    fd = extract_file_data(f)
    # `some_global` and `len` aren't imported and aren't local symbols; they shouldn't
    # produce edges (we'd rather miss than fabricate).
    assert fd.references == []


def test_class_methods_inherit_class_qname_in_src(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "def helper():\n    return 1\n\n\n"
        "class Service:\n    def run(self):\n        return helper()\n"
    )
    fd = extract_file_data(f)
    sources = {r.src_qname for r in fd.references}
    assert "mod:Service.run" in sources


def test_extract_file_data_includes_symbols(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text("def alpha():\n    return 1\n\n\ndef beta():\n    return alpha()\n")
    fd = extract_file_data(f)
    qnames = {s.qualified_name for s in fd.symbols}
    assert qnames == {"mod:alpha", "mod:beta"}


def test_both_import_and_intra_file_edges_resolve(tmp_path: Path):
    f = tmp_path / "mod.py"
    f.write_text(
        "from helpers import imp_fn\n\n\n"
        "def local_fn():\n    return 1\n\n\n"
        "def caller():\n    return imp_fn() + local_fn()\n"
    )
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:caller"}
    assert "helpers:imp_fn" in targets  # cross-file via import
    assert "mod:local_fn" in targets  # intra-file via name match
