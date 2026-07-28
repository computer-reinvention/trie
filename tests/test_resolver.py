"""Tests for the tree-sitter + resolver seam.

Covers the language-neutral contract (`merge_references`, `ReferenceResolver`
protocol), the jedi Python resolver's method-dispatch recovery, and the
backend's two-pass extraction with graceful fallback when the resolver is
disabled or absent.
"""

from __future__ import annotations

from pathlib import Path

from trie.parse.base import LanguageBackend
from trie.parse.python import PythonBackend
from trie.parse.resolver import KIND_RANK, ReferenceResolver, merge_references
from trie.parse.resolvers.jedi_resolver import JediResolver
from trie.parse.types import Reference


def _pairs(refs) -> set[tuple[str, str, str]]:
    return {(r.src_qname, r.target_qname, r.kind) for r in refs}


# --- merge_references ---------------------------------------------------------


def test_merge_appends_new_pairs():
    base = [Reference("a:f", "a:g", "calls")]
    extra = [Reference("a:f", "a:h", "calls")]
    merged = merge_references(base, extra)
    assert _pairs(merged) == {("a:f", "a:g", "calls"), ("a:f", "a:h", "calls")}


def test_merge_dedupes_identical_pairs():
    base = [Reference("a:f", "a:g", "calls")]
    extra = [Reference("a:f", "a:g", "calls")]
    merged = merge_references(base, extra)
    assert len(merged) == 1


def test_merge_upgrades_to_stronger_kind():
    # A resolver 'calls' must win over a tree-sitter 'references' for same pair.
    base = [Reference("a:f", "a:g", "references")]
    extra = [Reference("a:f", "a:g", "calls")]
    merged = merge_references(base, extra)
    assert merged[0].kind == "calls"
    assert KIND_RANK["calls"] > KIND_RANK["references"]


def test_merge_does_not_downgrade_kind():
    base = [Reference("a:f", "a:g", "calls")]
    extra = [Reference("a:f", "a:g", "references")]
    merged = merge_references(base, extra)
    assert merged[0].kind == "calls"


def test_merge_drops_self_edges():
    merged = merge_references([], [Reference("a:f", "a:f", "calls")])
    assert merged == []


# --- protocol conformance -----------------------------------------------------


def test_jedi_resolver_satisfies_protocol():
    assert isinstance(JediResolver(), ReferenceResolver)


def test_python_backend_satisfies_language_backend():
    assert isinstance(PythonBackend(), LanguageBackend)


def test_python_backend_exposes_resolver():
    assert PythonBackend().resolver() is not None


# --- jedi method-dispatch recovery -------------------------------------------


def test_resolver_recovers_self_method_call(tmp_path: Path):
    f = tmp_path / "svc.py"
    f.write_text(
        "class Service:\n"
        "    def run(self):\n"
        "        return self.helper()\n"
        "    def helper(self):\n"
        "        return 1\n"
    )
    resolver = JediResolver()
    from trie.parse.registry import extract_symbols

    syms = extract_symbols(f, source_root=tmp_path)
    refs = resolver.resolve_file(f.resolve(), tmp_path.resolve(), syms)
    assert ("svc:Service.run", "svc:Service.helper", "calls") in _pairs(refs)


def test_backend_merges_resolver_edges(tmp_path: Path):
    f = tmp_path / "svc.py"
    f.write_text(
        "class Service:\n"
        "    def run(self):\n"
        "        return self.helper()\n"
        "    def helper(self):\n"
        "        return 1\n"
    )
    fd = PythonBackend().extract_file_data(f, source_root=tmp_path)
    method_edges = {
        (r.src_qname, r.target_qname)
        for r in fd.references
        if r.kind == "calls" and "." in r.target_qname.split(":", 1)[1]
    }
    assert ("svc:Service.run", "svc:Service.helper") in method_edges


def test_resolver_ignores_stdlib_targets(tmp_path: Path):
    f = tmp_path / "svc.py"
    f.write_text("import os\n\n\ndef run():\n    return os.getpid()\n")
    resolver = JediResolver()
    from trie.parse.registry import extract_symbols

    syms = extract_symbols(f, source_root=tmp_path)
    refs = resolver.resolve_file(f.resolve(), tmp_path.resolve(), syms)
    # os.getpid resolves outside the source root — no project edge.
    assert all("os" not in r.target_qname.split(":", 1)[0] for r in refs)


def test_resolver_disabled_env(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("TRIE_DISABLE_RESOLVER", "1")
    f = tmp_path / "svc.py"
    f.write_text(
        "class Service:\n"
        "    def run(self):\n"
        "        return self.helper()\n"
        "    def helper(self):\n"
        "        return 1\n"
    )
    backend = PythonBackend()
    assert backend.resolver() is None
    fd = backend.extract_file_data(f, source_root=tmp_path)
    method_edges = [
        r for r in fd.references if r.kind == "calls" and "." in r.target_qname.split(":", 1)[1]
    ]
    assert method_edges == []


def test_resolver_never_raises_on_bad_file(tmp_path: Path):
    f = tmp_path / "broken.py"
    f.write_text("def f(:\n    this is not valid python (((\n")
    resolver = JediResolver()
    # Must return [] rather than raising for an unparseable file.
    assert resolver.resolve_file(f.resolve(), tmp_path.resolve(), []) == []
