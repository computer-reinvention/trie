"""Lua language backend — tree-sitter symbols + references, paired with lua-language-server.

Lua has no classes; the idiomatic OO pattern is a table with function fields
(`function M.helper()` / `function Obj:method()`). We surface those as:
  - `function`: `function name(...)` / `local function name(...)` with a plain
                identifier name.
  - `method`:   `function Table.name(...)` or `function Table:name(...)` — the
                dotted/colon index is split into `parent=Table`, name=`name`, so
                the qname is `mod:Table.name` and the resolver can map
                `obj.name()` once the server resolves the table type.
  - `constant`: top-level `Name = { ... }` / `Name = value` assignments and
                `local Name = ...` bindings with a single name.

`local` bindings are treated as non-public (module-private), matching Lua's
scoping convention; globals are public.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_lua
from tree_sitter import Language, Node, Parser

from trie.parse.types import FileData, Reference, Symbol

LUA_LANGUAGE = Language(tree_sitter_lua.language())


def _make_parser() -> Parser:
    parser = Parser()
    parser.language = LUA_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _module_key(file_path: Path, source_root: Path) -> str:
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _func_name(fn_node: Node, source: bytes) -> tuple[str | None, str | None]:
    """Return (parent, name) for a function_declaration.

    - plain `function foo()`            -> (None, "foo")
    - `function Obj.foo()`              -> ("Obj", "foo")
    - `function Obj:foo()`              -> ("Obj", "foo")  (method-colon form)
    - nested `function A.B.foo()`       -> ("A.B", "foo")
    """
    for c in fn_node.named_children:
        if c.type == "identifier":
            return (None, _node_text(c, source))
        if c.type in ("dot_index_expression", "method_index_expression"):
            # object field/method: table + key
            obj = c.child_by_field_name("table") or (
                c.named_children[0] if c.named_children else None
            )
            key = c.child_by_field_name("field") or c.child_by_field_name("method")
            if key is None and c.named_children:
                key = c.named_children[-1]
            parent = _node_text(obj, source) if obj is not None else None
            name = _node_text(key, source) if key is not None else None
            return (parent, name)
    return (None, None)


def _is_local(node: Node, source: bytes) -> bool:
    for c in node.children:
        if c.type == "local":
            return True
    # token text fallback
    first = node.children[0] if node.children else None
    return first is not None and _node_text(first, source) == "local"


def _make_symbol(
    node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    name: str,
    kind: str,
    parent: str | None = None,
    is_public: bool = True,
) -> Symbol:
    body = node.child_by_field_name("body")
    if body is not None:
        signature = source[node.start_byte : body.start_byte].decode("utf-8", "replace").strip()
        body_text = _node_text(body, source)
    else:
        signature = _node_text(node, source).strip().splitlines()[0]
        body_text = _node_text(node, source)
    dotted = f"{parent}.{name}" if parent else name
    return Symbol(
        qualified_name=f"{module_key}:{dotted}",
        kind=kind,
        name=name,
        file_path=rel_file,
        signature=signature,
        docstring=None,
        body_text=body_text,
        body_normalized_hash=_hash(body_text),
        signature_hash=_hash(signature),
        start_line=node.start_point[0] + 1,
        end_line=node.end_point[0] + 1,
        is_public=is_public,
        parent_class=parent,
    )


def _assignment_names(node: Node, source: bytes) -> list[str]:
    """Names on the LHS of a top-level assignment (`A, B = ...`), plain identifiers only."""
    names: list[str] = []
    var_list = None
    for c in node.named_children:
        if c.type == "variable_list":
            var_list = c
            break
    target = var_list or node
    for c in target.named_children:
        if c.type == "identifier":
            names.append(_node_text(c, source))
    return names


def extract_symbols(
    file_path: Path,
    source_root: Path | None = None,
    *,
    source_text: str | None = None,
) -> list[Symbol]:
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = source_text.encode("utf-8") if source_text is not None else file_path.read_bytes()
    tree = _make_parser().parse(source)
    module_key = _module_key(file_path, source_root)
    rel_file = str(file_path.relative_to(source_root))

    symbols: list[Symbol] = []

    for child in tree.root_node.named_children:
        t = child.type
        if t == "function_declaration":
            parent, name = _func_name(child, source)
            if name is None:
                continue
            is_local = _is_local(child, source)
            kind = "method" if parent else "function"
            symbols.append(
                _make_symbol(
                    child,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    name=name,
                    kind=kind,
                    parent=parent,
                    is_public=not is_local,
                )
            )
        elif t in ("variable_declaration", "assignment_statement"):
            is_local = t == "variable_declaration" and _is_local(child, source)
            for name in _assignment_names(child, source):
                symbols.append(
                    _make_symbol(
                        child,
                        source,
                        module_key=module_key,
                        rel_file=rel_file,
                        name=name,
                        kind="constant",
                        is_public=not is_local,
                    )
                )

    return symbols


def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None:
    target_line = sym.start_line
    match: Node | None = None

    def walk(n: Node) -> None:
        nonlocal match
        if match is not None:
            return
        if n.start_point[0] + 1 == target_line and n.type in (
            "function_declaration",
            "variable_declaration",
            "assignment_statement",
        ):
            match = n
        for c in n.children:
            walk(c)

    walk(root)
    return match


def _collect_call_names(node: Node, source: bytes) -> set[str]:
    """Names in call position: `foo()` adds `foo`; `t.m()` / `t:m()` adds `m`."""
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "function_call":
            fn = n.child_by_field_name("name") or (
                n.named_children[0] if n.named_children else None
            )
            if fn is not None:
                if fn.type == "identifier":
                    names.add(_node_text(fn, source))
                elif fn.type in ("dot_index_expression", "method_index_expression"):
                    key = fn.child_by_field_name("field") or fn.child_by_field_name("method")
                    if key is None and fn.named_children:
                        key = fn.named_children[-1]
                    if key is not None:
                        names.add(_node_text(key, source))
        for c in n.children:
            walk(c)

    walk(node)
    return names


def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData:
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = file_path.read_bytes()
    tree = _make_parser().parse(source)
    root = tree.root_node

    symbols = extract_symbols(file_path, source_root=source_root)
    own_top_level: dict[str, str] = {}
    for s in symbols:
        local = s.qualified_name.split(":", 1)[1]
        if "." not in local:
            own_top_level[s.name] = s.qualified_name

    references: list[Reference] = []
    seen: set[tuple[str, str]] = set()

    def add(src: str, tgt: str, kind: str) -> None:
        if src == tgt or (src, tgt) in seen:
            return
        seen.add((src, tgt))
        references.append(Reference(src_qname=src, target_qname=tgt, kind=kind))

    for sym in symbols:
        node = _find_node_for_symbol(root, sym)
        if node is None:
            continue
        for name in _collect_call_names(node, source):
            if name in own_top_level:
                add(sym.qualified_name, own_top_level[name], "calls")

    return FileData(symbols=symbols, references=references)


LUA_SYSTEM_PROMPT = """\
You are documenting a Lua source symbol for a code-navigation graph. Write a
concise, factual description of what the symbol does and why it exists.

- For a function, state what it computes/returns and notable side effects.
- For a table-field method (`M.foo` / `Obj:foo`), name the table/object and the
  behaviour it adds.
- For a top-level table/value, describe what it holds or configures.
- Prefer intent over restating the signature.
"""


class LuaBackend:
    """`LanguageBackend` for Lua, paired with lua-language-server."""

    name = "lua"
    extensions = (".lua",)

    def __init__(self) -> None:
        self._resolver = None
        self._resolver_built = False

    def extract_file_data(self, file_path, source_root=None, *, source_text=None):
        from pathlib import Path as _Path

        from trie.parse.resolver import merge_references

        if source_text is not None:
            raise NotImplementedError("source_text override is not supported for extract_file_data")

        file_data = extract_file_data(file_path, source_root=source_root)
        resolver = self.resolver()
        if resolver is None:
            return file_data
        abs_path = _Path(file_path).resolve()
        root = (_Path(source_root) if source_root is not None else abs_path.parent).resolve()
        extra = resolver.resolve_file(abs_path, root, file_data.symbols)
        if not extra:
            return file_data
        return FileData(
            symbols=file_data.symbols,
            references=merge_references(file_data.references, extra),
        )

    def extract_symbols(self, file_path, source_root=None, *, source_text=None):
        return extract_symbols(file_path, source_root=source_root, source_text=source_text)

    def source_suffix(self) -> str:
        return ".lua"

    def system_prompt(self) -> str:
        return LUA_SYSTEM_PROMPT

    def resolver(self):
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import lua_spec

                spec = lua_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver


__all__ = ["LUA_SYSTEM_PROMPT", "LuaBackend", "extract_file_data", "extract_symbols"]
