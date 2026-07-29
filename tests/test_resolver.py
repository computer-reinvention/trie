"""Tests for the tree-sitter + LSP resolver seam.

Covers the language-neutral contract (`merge_references`, `ReferenceResolver`
protocol, `LspServerSpec`), the generic `LspResolver`'s method-dispatch recovery
via a real language server (pyright for Python, typescript-language-server for
TS), and each backend's two-pass extraction with graceful fallback when the
resolver is disabled or its server is absent.

The LSP-driven tests skip when the relevant server binary isn't on PATH, so the
suite stays green on machines without pyright / typescript-language-server.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse.base import LanguageBackend
from trie.parse.python import PythonBackend
from trie.parse.resolver import KIND_RANK, ReferenceResolver, merge_references
from trie.parse.resolvers.lsp_resolver import LspResolver
from trie.parse.resolvers.specs import python_spec, typescript_spec
from trie.parse.types import Reference


def _pairs(refs) -> set[tuple[str, str, str]]:
    return {(r.src_qname, r.target_qname, r.kind) for r in refs}


def _method_edges(fd) -> set[tuple[str, str]]:
    return {
        (r.src_qname, r.target_qname)
        for r in fd.references
        if r.kind == "calls" and "." in r.target_qname.split(":", 1)[1]
    }


requires_python_lsp = pytest.mark.skipif(
    python_spec() is None, reason="no Python language server (pyright/basedpyright) on PATH"
)
requires_ts_lsp = pytest.mark.skipif(
    typescript_spec() is None, reason="typescript-language-server not on PATH"
)


# --- merge_references ---------------------------------------------------------


def test_merge_appends_new_pairs():
    base = [Reference("a:f", "a:g", "calls")]
    extra = [Reference("a:f", "a:h", "calls")]
    merged = merge_references(base, extra)
    assert _pairs(merged) == {("a:f", "a:g", "calls"), ("a:f", "a:h", "calls")}


def test_merge_dedupes_identical_pairs():
    merged = merge_references(
        [Reference("a:f", "a:g", "calls")], [Reference("a:f", "a:g", "calls")]
    )
    assert len(merged) == 1


def test_merge_upgrades_to_stronger_kind():
    merged = merge_references(
        [Reference("a:f", "a:g", "references")], [Reference("a:f", "a:g", "calls")]
    )
    assert merged[0].kind == "calls"
    assert KIND_RANK["calls"] > KIND_RANK["references"]


def test_merge_does_not_downgrade_kind():
    merged = merge_references(
        [Reference("a:f", "a:g", "calls")], [Reference("a:f", "a:g", "references")]
    )
    assert merged[0].kind == "calls"


def test_merge_drops_self_edges():
    assert merge_references([], [Reference("a:f", "a:f", "calls")]) == []


# --- protocol / spec conformance ---------------------------------------------


def test_lsp_resolver_satisfies_protocol():
    spec = python_spec() or typescript_spec()
    if spec is None:
        pytest.skip("no language server available to construct a resolver")
    assert isinstance(LspResolver(spec), ReferenceResolver)


def test_python_backend_satisfies_language_backend():
    assert isinstance(PythonBackend(), LanguageBackend)


def test_spec_availability_is_path_based():
    spec = python_spec()
    if spec is None:
        pytest.skip("no Python server on PATH")
    assert spec.is_available()
    assert spec.command and spec.language_id == "python"


# --- Python method-dispatch recovery (pyright over LSP) ----------------------


@requires_python_lsp
def test_python_backend_exposes_resolver(enable_resolver):
    assert PythonBackend().resolver() is not None


@requires_python_lsp
def test_python_resolver_recovers_self_method_call(tmp_path: Path, enable_resolver):
    f = tmp_path / "svc.py"
    f.write_text(
        "class Service:\n"
        "    def run(self):\n"
        "        return self.helper()\n"
        "    def helper(self):\n"
        "        return 1\n"
    )
    backend = PythonBackend()
    try:
        fd = backend.extract_file_data(f, source_root=tmp_path)
        assert ("svc:Service.run", "svc:Service.helper") in _method_edges(fd)
    finally:
        r = backend.resolver()
        if r is not None:
            r.close()


@requires_python_lsp
def test_python_resolver_ignores_stdlib_targets(tmp_path: Path):
    f = tmp_path / "svc.py"
    f.write_text("import os\n\n\ndef run():\n    return os.getpid()\n")
    spec = python_spec()
    resolver = LspResolver(spec)
    try:
        from trie.parse.registry import extract_symbols

        syms = extract_symbols(f, source_root=tmp_path)
        refs = resolver.resolve_file(f.resolve(), tmp_path.resolve(), syms)
        assert all("os" not in r.target_qname.split(":", 1)[0] for r in refs)
    finally:
        resolver.close()


# --- TypeScript method-dispatch recovery (tsserver over LSP) -----------------


@requires_ts_lsp
def test_typescript_backend_exposes_resolver(enable_resolver):
    from trie.parse.typescript import TypeScriptBackend

    assert TypeScriptBackend().resolver() is not None


@requires_ts_lsp
def test_typescript_resolver_recovers_this_method_call(tmp_path: Path, enable_resolver):
    from trie.parse.typescript import TypeScriptBackend

    (tmp_path / "tsconfig.json").write_text(
        '{"compilerOptions":{"strict":true},"include":["*.ts"]}'
    )
    f = tmp_path / "svc.ts"
    f.write_text(
        "export class Service {\n"
        "  run(): number {\n"
        "    return this.helper();\n"
        "  }\n"
        "  helper(): number {\n"
        "    return 1;\n"
        "  }\n"
        "}\n"
    )
    backend = TypeScriptBackend()
    try:
        fd = backend.extract_file_data(f, source_root=tmp_path)
        assert ("svc:Service.run", "svc:Service.helper") in _method_edges(fd)
    finally:
        r = backend.resolver()
        if r is not None:
            r.close()


# --- disable flag / graceful fallback ----------------------------------------


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
    assert _method_edges(fd) == set()


def test_resolver_never_raises_on_missing_server(tmp_path: Path, monkeypatch):
    # Point the spec at a non-existent binary; resolve_file must return [] and
    # the backend must fall back to tree-sitter-only extraction.
    from trie.parse.resolvers.lsp_resolver import LspServerSpec

    bad_spec = LspServerSpec(
        name="nope",
        command=["definitely-not-a-real-lsp-server-xyz", "--stdio"],
        language_id="python",
        call_sites=python_spec().call_sites if python_spec() else (lambda s: []),
    )
    resolver = LspResolver(bad_spec)
    f = tmp_path / "svc.py"
    f.write_text(
        "class S:\n    def a(self):\n        return self.b()\n    def b(self):\n        return 1\n"
    )
    from trie.parse.registry import extract_symbols

    syms = extract_symbols(f, source_root=tmp_path)
    assert resolver.resolve_file(f.resolve(), tmp_path.resolve(), syms) == []
