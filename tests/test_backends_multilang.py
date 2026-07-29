"""Symbol + tree-sitter reference extraction for the Go/Rust/C/Lua backends.

These assert the structural pass only (no language server needed), plus registry
wiring. Resolver-driven method-dispatch is covered by test_resolver.py for the
servers that are installed.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse import registry
from trie.parse.base import LanguageBackend


def _kinds(symbols) -> dict[str, str]:
    return {s.name: s.kind for s in symbols}


def _edges(fd) -> set[tuple[str, str, str]]:
    return {(r.src_qname, r.target_qname, r.kind) for r in fd.references}


# --- registry wiring ----------------------------------------------------------


@pytest.mark.parametrize(
    "ext",
    [".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs", ".c", ".h", ".lua"],
)
def test_extension_is_indexable(ext):
    assert registry.is_indexable(f"foo{ext}")


def test_all_backends_satisfy_protocol():
    for b in registry.all_backends():
        assert isinstance(b, LanguageBackend)


# --- Go -----------------------------------------------------------------------


def test_go_symbols_and_calls(tmp_path: Path):
    from trie.parse.go import extract_file_data, extract_symbols

    f = tmp_path / "m.go"
    f.write_text(
        "package main\n\n"
        "func Add(a int) int { return a }\n\n"
        "type Counter struct { n int }\n\n"
        "func (c *Counter) Inc() { c.n = Add(c.n) }\n\n"
        "const Max = 10\n"
    )
    kinds = _kinds(extract_symbols(f, source_root=tmp_path))
    assert kinds["Add"] == "function"
    assert kinds["Counter"] == "class"
    assert kinds["Inc"] == "method"
    assert kinds["Max"] == "constant"
    edges = _edges(extract_file_data(f, source_root=tmp_path))
    assert ("m:Counter.Inc", "m:Add", "calls") in edges


# --- Rust ---------------------------------------------------------------------


def test_rust_symbols_and_calls(tmp_path: Path):
    from trie.parse.rust import extract_file_data, extract_symbols

    f = tmp_path / "m.rs"
    f.write_text(
        "pub fn add(a: i32) -> i32 { a }\n"
        "pub struct Counter { n: i32 }\n"
        "impl Counter { pub fn inc(&mut self) { self.n = add(self.n); } }\n"
        "pub trait Runnable { fn run(&self); }\n"
        "pub enum State { On, Off }\n"
    )
    kinds = _kinds(extract_symbols(f, source_root=tmp_path))
    assert kinds["add"] == "function"
    assert kinds["Counter"] == "class"
    assert kinds["inc"] == "method"
    assert kinds["Runnable"] == "interface"
    assert kinds["State"] == "enum"
    edges = _edges(extract_file_data(f, source_root=tmp_path))
    assert ("m:Counter.inc", "m:add", "calls") in edges


# --- C ------------------------------------------------------------------------


def test_c_symbols_and_calls(tmp_path: Path):
    from trie.parse.c import extract_file_data, extract_symbols

    f = tmp_path / "m.c"
    f.write_text(
        "int add(int a) { return a; }\n"
        "struct Point { int x; };\n"
        "enum Color { RED, GREEN };\n"
        "void run(void) { add(1); }\n"
        "#define MAX 10\n"
        "static int helper(void) { return 0; }\n"
    )
    syms = extract_symbols(f, source_root=tmp_path)
    kinds = _kinds(syms)
    assert kinds["add"] == "function"
    assert kinds["Point"] == "class"
    assert kinds["Color"] == "enum"
    assert kinds["MAX"] == "constant"
    # static linkage → non-public
    assert next(s for s in syms if s.name == "helper").is_public is False
    edges = _edges(extract_file_data(f, source_root=tmp_path))
    assert ("m:run", "m:add", "calls") in edges


# --- Lua ----------------------------------------------------------------------


def test_lua_symbols_and_calls(tmp_path: Path):
    from trie.parse.lua import extract_file_data, extract_symbols

    f = tmp_path / "m.lua"
    f.write_text(
        "local function add(a) return a end\n"
        "function global_fn() return add(1) end\n"
        "local M = {}\n"
        "function M.helper() return add(2) end\n"
        "Config = { max = 10 }\n"
    )
    syms = extract_symbols(f, source_root=tmp_path)
    kinds = _kinds(syms)
    assert kinds["add"] == "function"
    assert kinds["global_fn"] == "function"
    assert kinds["helper"] == "method"
    # local function → private; global → public
    assert next(s for s in syms if s.name == "add").is_public is False
    assert next(s for s in syms if s.name == "global_fn").is_public is True
    edges = _edges(extract_file_data(f, source_root=tmp_path))
    assert ("m:global_fn", "m:add", "calls") in edges
    assert ("m:M.helper", "m:add", "calls") in edges


# --- JavaScript via the TypeScript backend -----------------------------------


def test_javascript_uses_typescript_backend(tmp_path: Path):
    from trie.parse.typescript import TypeScriptBackend

    assert registry.get_backend_for_file("app.js").name == "typescript"
    f = tmp_path / "app.js"
    f.write_text("export function greet(name) {\n  return 'hi ' + name;\n}\n")
    syms = TypeScriptBackend().extract_symbols(f, source_root=tmp_path)
    assert any(s.name == "greet" and s.kind == "function" for s in syms)
    # module key strips the .js suffix
    assert any(s.qualified_name == "app:greet" for s in syms)
