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


# ---------------------------------------------------------------------------
# Module-attribute resolution: `import X; X.Y()` and friends
# ---------------------------------------------------------------------------


def test_plain_import_attribute_access(tmp_path: Path):
    """`import foo` followed by `foo.bar()` should resolve to `foo:bar`."""
    f = tmp_path / "mod.py"
    f.write_text("import foo\n\n\ndef run():\n    return foo.bar()\n")
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    assert "foo:bar" in targets


def test_aliased_plain_import_attribute_access(tmp_path: Path):
    """`import foo as f` followed by `f.bar()` should resolve to `foo:bar`,
    not `f:bar`."""
    f = tmp_path / "mod.py"
    f.write_text("import foo as f\n\n\ndef run():\n    return f.bar()\n")
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    assert "foo:bar" in targets


def test_dotted_import_attribute_access(tmp_path: Path):
    """`import foo.bar` followed by `foo.bar.baz()` should resolve to `foo/bar:baz`.

    This also leaves `foo` available as a bare module binding so `foo.thing(...)`
    (referring to something from `foo/__init__.py`) also resolves to `foo:thing`.
    """
    f = tmp_path / "mod.py"
    f.write_text("import foo.bar\n\n\ndef run():\n    return foo.bar.baz()\n")
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    assert "foo/bar:baz" in targets


def test_from_import_submodule_attribute_resolves(tmp_path: Path):
    """`from pkg import submod; submod.thing()` is the bootstrapping pattern (e.g.
    `from trie import telemetry; telemetry.emit(...)`). The submod binding lives
    in both the symbols table (existing behaviour) and the modules table (new),
    so both `submod` as a bare reference and `submod.thing` as attribute access
    emit candidate edges. The store filters whichever doesn't actually exist."""
    f = tmp_path / "mod.py"
    f.write_text("from pkg import submod\n\n\ndef run():\n    return submod.thing()\n")
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    # Both candidates emitted; the store's existence filter picks the real one.
    assert "pkg:submod" in targets  # the bare-name (symbol) interpretation
    assert "pkg/submod:thing" in targets  # the module-attribute interpretation


def test_module_attribute_emitted_even_for_stdlib(tmp_path: Path):
    """`import os; os.path.join(...)` emits candidate edges; the store filters them.

    We don't special-case stdlib at extraction time — the store's existence check
    against the symbols table is the gate. This test pins the extractor's
    permissive behaviour so a future "filter at extraction" refactor doesn't
    silently re-introduce the original `import X` blind spot."""
    f = tmp_path / "mod.py"
    f.write_text("import os\n\n\ndef run():\n    return os.path.join('a', 'b')\n")
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    assert "os:path" in targets


def test_mixed_from_and_plain_import(tmp_path: Path):
    """Combining `from X import Y` and `import Z; Z.W()` in the same file yields
    edges from both resolution paths."""
    f = tmp_path / "mod.py"
    f.write_text(
        "from helpers import direct\n"
        "import other\n\n\n"
        "def run():\n    return direct() + other.method()\n"
    )
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    assert "helpers:direct" in targets
    assert "other:method" in targets


def test_attribute_access_through_local_var_not_treated_as_module(tmp_path: Path):
    """An attribute access whose base is a local variable (not an imported module)
    must not emit a spurious module-attribute edge. The resolver only looks at
    the imports table for module bindings."""
    f = tmp_path / "mod.py"
    f.write_text(
        "def run():\n    obj = make()\n    return obj.method()\n\ndef make():\n    return None\n"
    )
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:run"}
    # `obj.method` doesn't resolve to anything — `obj` is a local, not an import.
    # The only edge is the intra-file `make()` call.
    assert targets == {"mod:make"}


def test_module_attribute_no_self_edge(tmp_path: Path):
    """If the resolved target qname equals the source symbol qname (the symbol
    references its own module's attribute), no self-edge is emitted."""
    f = tmp_path / "mod.py"
    f.write_text(
        "import mod\n\n\n"
        "def alpha():\n"
        "    return mod.alpha\n"  # alpha referring to itself via module access
    )
    fd = extract_file_data(f)
    targets = {r.target_qname for r in fd.references if r.src_qname == "mod:alpha"}
    assert "mod:alpha" not in targets
