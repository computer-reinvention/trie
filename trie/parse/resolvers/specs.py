"""Per-language LSP server specs — the one place a new language is registered.

Each `LspServerSpec` binds a language server command + LSP languageId to a
tree-sitter callback that yields member-call sites for that grammar. Adding a
language's type-aware resolution is a spec here plus a `backend.resolver()` that
returns `LspResolver(spec)`; the resolver machinery itself is language-agnostic.

Server commands are the stdio invocations; discovery is by PATH lookup
(`LspServerSpec.is_available`), so a backend only offers the resolver when the
server is installed and otherwise degrades to tree-sitter-only.
"""

from __future__ import annotations

from trie.parse.resolvers.lsp_resolver import CallSite, LspServerSpec


def _python_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line, col) of each `<expr>.<attr>(...)` attribute call in Python."""
    from trie.parse.python import _make_parser

    tree = _make_parser().parse(source)
    return _walk_attribute_calls(tree.root_node)


def _typescript_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line, col) of each `<expr>.<member>(...)` call in TS/TSX.

    Uses the `.ts` grammar; `.tsx` files parse acceptably for locating call
    positions since member-expression shape is identical.
    """
    from pathlib import Path

    from trie.parse.typescript import _make_parser

    tree = _make_parser(Path("x.ts")).parse(source)
    return _walk_member_calls(tree.root_node)


def _walk_attribute_calls(root) -> list[CallSite]:
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "call":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "attribute":
                attr = fn.child_by_field_name("attribute")
                if attr is not None and attr.type == "identifier":
                    out.append((attr.start_point[0], attr.start_point[1]))
        for c in n.children:
            walk(c)

    walk(root)
    return out


def _walk_member_calls(root) -> list[CallSite]:
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "member_expression":
                prop = fn.child_by_field_name("property")
                if prop is not None and prop.type in ("property_identifier", "identifier"):
                    out.append((prop.start_point[0], prop.start_point[1]))
        for c in n.children:
            walk(c)

    walk(root)
    return out


def _go_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line,col) of each `x.Method(...)` selector call in Go."""
    from trie.parse.go import _make_parser

    tree = _make_parser().parse(source)
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("comment", "interpreted_string_literal", "raw_string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "selector_expression":
                field = fn.child_by_field_name("field")
                if field is not None:
                    out.append((field.start_point[0], field.start_point[1]))
        for c in n.children:
            walk(c)

    walk(tree.root_node)
    return out


def _rust_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line,col) of each `x.method(...)` field-expression call in Rust."""
    from trie.parse.rust import _make_parser

    tree = _make_parser().parse(source)
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("line_comment", "block_comment", "string_literal", "raw_string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "field_expression":
                field = fn.child_by_field_name("field")
                if field is not None:
                    out.append((field.start_point[0], field.start_point[1]))
        for c in n.children:
            walk(c)

    walk(tree.root_node)
    return out


def _c_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line,col) of each `p->field(...)` / `s.field(...)` call in C.

    C member calls are rare (function pointers in structs); this catches them
    so clangd can resolve the pointer target. Plain `foo()` calls are already
    handled by tree-sitter's same-file resolution.
    """
    from trie.parse.c import _make_parser

    tree = _make_parser().parse(source)
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("comment", "string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "field_expression":
                field = fn.child_by_field_name("field")
                if field is not None:
                    out.append((field.start_point[0], field.start_point[1]))
        for c in n.children:
            walk(c)

    walk(tree.root_node)
    return out


def _lua_call_sites(source: bytes) -> list[CallSite]:
    """0-based (line,col) of each `t.m(...)` / `t:m(...)` call in Lua."""
    from trie.parse.lua import _make_parser

    tree = _make_parser().parse(source)
    out: list[CallSite] = []

    def walk(n) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "function_call":
            fn = n.child_by_field_name("name") or (
                n.named_children[0] if n.named_children else None
            )
            if fn is not None and fn.type in ("dot_index_expression", "method_index_expression"):
                key = fn.child_by_field_name("field") or fn.child_by_field_name("method")
                if key is None and fn.named_children:
                    key = fn.named_children[-1]
                if key is not None:
                    out.append((key.start_point[0], key.start_point[1]))
        for c in n.children:
            walk(c)

    walk(tree.root_node)
    return out


PYRIGHT_SPEC = LspServerSpec(
    name="pyright",
    command=["pyright-langserver", "--stdio"],
    language_id="python",
    call_sites=_python_call_sites,
)

BASEDPYRIGHT_SPEC = LspServerSpec(
    name="basedpyright",
    command=["basedpyright-langserver", "--stdio"],
    language_id="python",
    call_sites=_python_call_sites,
)

TYPESCRIPT_SPEC = LspServerSpec(
    name="typescript-language-server",
    command=["typescript-language-server", "--stdio"],
    language_id="typescript",
    call_sites=_typescript_call_sites,
)


def python_spec() -> LspServerSpec | None:
    """The first available Python LSP spec, or None.

    Prefers basedpyright (faster) and falls back to pyright.
    """
    for spec in (BASEDPYRIGHT_SPEC, PYRIGHT_SPEC):
        if spec.is_available():
            return spec
    return None


def typescript_spec() -> LspServerSpec | None:
    """The TypeScript LSP spec if its server is installed, else None."""
    return TYPESCRIPT_SPEC if TYPESCRIPT_SPEC.is_available() else None


# Heavier servers index the whole workspace before answering; give the
# initialize handshake room and let them settle after didOpen. Too-low values
# just degrade that language to tree-sitter-only rather than crashing.
GO_SPEC = LspServerSpec(
    name="gopls",
    command=["gopls"],  # bare gopls speaks LSP over stdio
    language_id="go",
    call_sites=_go_call_sites,
    init_timeout=30.0,
    warmup=2.0,
)

RUST_SPEC = LspServerSpec(
    name="rust-analyzer",
    command=["rust-analyzer"],
    language_id="rust",
    call_sites=_rust_call_sites,
    init_timeout=60.0,
    warmup=3.0,
)

C_SPEC = LspServerSpec(
    name="clangd",
    command=["clangd"],
    language_id="c",
    call_sites=_c_call_sites,
    init_timeout=30.0,
    warmup=1.5,
)

LUA_SPEC = LspServerSpec(
    name="lua-language-server",
    command=["lua-language-server"],
    language_id="lua",
    call_sites=_lua_call_sites,
    init_timeout=30.0,
    warmup=1.5,
)


def go_spec() -> LspServerSpec | None:
    """The Go LSP spec (gopls) if installed, else None."""
    return GO_SPEC if GO_SPEC.is_available() else None


def rust_spec() -> LspServerSpec | None:
    """The Rust LSP spec (rust-analyzer) if installed, else None."""
    return RUST_SPEC if RUST_SPEC.is_available() else None


def c_spec() -> LspServerSpec | None:
    """The C LSP spec (clangd) if installed, else None."""
    return C_SPEC if C_SPEC.is_available() else None


def lua_spec() -> LspServerSpec | None:
    """The Lua LSP spec (lua-language-server) if installed, else None."""
    return LUA_SPEC if LUA_SPEC.is_available() else None


__all__ = [
    "BASEDPYRIGHT_SPEC",
    "C_SPEC",
    "GO_SPEC",
    "LUA_SPEC",
    "PYRIGHT_SPEC",
    "RUST_SPEC",
    "TYPESCRIPT_SPEC",
    "c_spec",
    "go_spec",
    "lua_spec",
    "python_spec",
    "rust_spec",
    "typescript_spec",
]
