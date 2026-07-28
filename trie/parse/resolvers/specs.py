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


__all__ = [
    "BASEDPYRIGHT_SPEC",
    "PYRIGHT_SPEC",
    "TYPESCRIPT_SPEC",
    "python_spec",
    "typescript_spec",
]
