"""TypeScript reference (edge) extraction via tree-sitter.

Mirrors `trie/parse/references.py` for TypeScript. Imports are resolved to
project module keys via `TsResolver` (relative / tsconfig alias / workspace
package), then bound names used in a symbol's body produce edges. The extractor
is permissive — it emits candidate edges for every plausible target qname; the
store's `replace_all_edges` drops candidates the project doesn't define, so
`node_modules` imports vanish without special-casing.

Edge kinds match the Python resolver: `calls` (call position) outranks
`references` (bare use); `inherits` / `implements` come from `extends` /
`implements` heritage. See docs/core/multi-language-backend-prd.md §6.
"""

from __future__ import annotations

from pathlib import Path

from tree_sitter import Node

from trie.parse.ts_resolve import TsResolver
from trie.parse.types import FileData, Reference, Symbol
from trie.parse.typescript import _make_parser, _node_text, extract_symbols

_KIND_RANK = {
    "imports": 0,
    "references": 1,
    "calls": 2,
    "inherits": 3,
    "implements": 3,
    "contains": 3,
}


class _Bindings:
    """Local-name -> target module key/qname tables built from a file's imports.

    `symbols` maps a name bound by `import { x }` / `import Def` to a target
    qname (`key:x`). `namespaces` maps a name bound by `import * as ns` to a
    target module key, so `ns.run()` resolves to `key:run`.
    """

    def __init__(self) -> None:
        self.symbols: dict[str, str] = {}
        self.namespaces: dict[str, str] = {}


def _collect_imports(
    root: Node, source: bytes, *, from_file: Path, resolver: TsResolver
) -> _Bindings:
    b = _Bindings()
    for stmt in root.named_children:
        if stmt.type == "import_statement":
            _absorb_import(stmt, source, b, from_file=from_file, resolver=resolver)
        elif stmt.type == "export_statement":
            _absorb_reexport(stmt, source, b, from_file=from_file, resolver=resolver)
    return b


def _specifier_string(stmt: Node, source: bytes) -> str | None:
    src_node = stmt.child_by_field_name("source")
    if src_node is None:
        for c in stmt.named_children:
            if c.type == "string":
                src_node = c
                break
    if src_node is None:
        return None
    frag = src_node.named_children[0] if src_node.named_children else None
    return _node_text(frag, source) if frag is not None else None


def _absorb_import(
    stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver
) -> None:
    spec = _specifier_string(stmt, source)
    if spec is None:
        return
    key = resolver.resolve(spec, from_file)
    if key is None:
        # A bare (non-relative) specifier that didn't resolve to a project file
        # may still name an ambient module declared in a first-party `.d.ts`
        # (`declare module "lang-map"`), whose symbols are keyed by that literal
        # name. Bind against it; the store drops the edge if no such symbol
        # exists (e.g. a real node_modules import).
        if spec.startswith("."):
            return
        key = spec
    clause = next((c for c in stmt.named_children if c.type == "import_clause"), None)
    if clause is None:
        return
    for c in clause.named_children:
        if c.type == "identifier":
            # default import: `import Def from "..."`
            b.symbols[_node_text(c, source)] = f"{key}:default"
        elif c.type == "named_imports":
            for spec_node in c.named_children:
                if spec_node.type != "import_specifier":
                    continue
                ids = [g for g in spec_node.named_children if g.type == "identifier"]
                if not ids:
                    continue
                imported = _node_text(ids[0], source)
                local = _node_text(ids[-1], source)  # `x as y` -> local is y
                b.symbols[local] = f"{key}:{imported}"
        elif c.type == "namespace_import":
            ids = [g for g in c.named_children if g.type == "identifier"]
            if ids:
                b.namespaces[_node_text(ids[0], source)] = key


def _absorb_reexport(
    stmt: Node, source: bytes, b: _Bindings, *, from_file: Path, resolver: TsResolver
) -> None:
    # `export { x, y } from "./foo"` — bind the names so a body using them links
    # through the barrel. Only when there is a source specifier.
    spec = _specifier_string(stmt, source)
    if spec is None:
        return
    key = resolver.resolve(spec, from_file)
    if key is None:
        return
    clause = next((c for c in stmt.named_children if c.type == "export_clause"), None)
    if clause is None:
        return
    for spec_node in clause.named_children:
        if spec_node.type != "export_specifier":
            continue
        ids = [g for g in spec_node.named_children if g.type == "identifier"]
        if not ids:
            continue
        imported = _node_text(ids[0], source)
        local = _node_text(ids[-1], source)
        b.symbols[local] = f"{key}:{imported}"


def _find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None:
    """Locate the AST node whose line span matches a top-level symbol."""
    target_line = symbol.start_line

    def search(n: Node) -> Node | None:
        for c in n.named_children:
            if c.start_point[0] + 1 == target_line and c.type not in ("comment",):
                return c
            if c.start_point[0] + 1 <= target_line <= c.end_point[0] + 1:
                deeper = search(c)
                if deeper is not None:
                    return deeper
        return None

    return search(root)


def _collect_call_names(node: Node, source: bytes) -> set[str]:
    """Names in call position (`f()`, `a.b.f()`, `new C()`)."""
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type in ("call_expression", "new_expression"):
            fn = n.child_by_field_name("function") or (
                n.named_children[0] if n.named_children else None
            )
            if fn is not None:
                if fn.type == "identifier":
                    names.add(_node_text(fn, source))
                elif fn.type == "member_expression":
                    prop = fn.child_by_field_name("property")
                    if prop is not None:
                        names.add(_node_text(prop, source))
        for c in n.children:
            walk(c)

    walk(node)
    return names


def _collect_identifiers(node: Node, source: bytes) -> set[str]:
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type in ("identifier", "type_identifier"):
            names.add(_node_text(n, source))
        for c in n.children:
            walk(c)

    walk(node)
    return names


def _collect_namespace_uses(node: Node, source: bytes) -> set[tuple[str, str]]:
    """`ns.member` pairs, so a namespace import resolves to `key:member`."""
    pairs: set[tuple[str, str]] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "member_expression":
            obj = n.child_by_field_name("object")
            prop = n.child_by_field_name("property")
            if obj is not None and obj.type == "identifier" and prop is not None:
                pairs.add((_node_text(obj, source), _node_text(prop, source)))
        for c in n.children:
            walk(c)

    walk(node)
    return pairs


def _class_declaration_node(node: Node) -> Node:
    """Descend through an `export_statement` wrapper to the class_declaration."""
    if node.type in ("class_declaration", "abstract_class_declaration"):
        return node
    for c in node.named_children:
        if c.type in ("class_declaration", "abstract_class_declaration"):
            return c
    return node


def _heritage(class_node: Node, source: bytes) -> tuple[list[str], list[str]]:
    """(extends_names, implements_names) from a class's heritage clause."""
    class_node = _class_declaration_node(class_node)
    extends: list[str] = []
    implements: list[str] = []
    for c in class_node.named_children:
        if c.type != "class_heritage":
            continue
        for clause in c.named_children:
            names = [
                _node_text(g, source)
                for g in clause.named_children
                if g.type in ("identifier", "type_identifier")
            ]
            text = _node_text(clause, source)
            if clause.type == "extends_clause" or text.startswith("extends"):
                extends.extend(names)
            elif clause.type == "implements_clause" or text.startswith("implements"):
                implements.extend(names)
    return extends, implements


def extract_file_data(
    file_path: Path,
    source_root: Path | None = None,
    *,
    resolver: TsResolver | None = None,
) -> FileData:
    """Parse one TS file into symbols + resolved outbound references."""
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = file_path.read_bytes()
    tree = _make_parser(file_path).parse(source)
    root = tree.root_node

    if resolver is None:
        resolver = TsResolver.build(source_root)

    symbols = extract_symbols(file_path, source_root=source_root)
    bindings = _collect_imports(root, source, from_file=file_path, resolver=resolver)

    own_top_level: dict[str, str] = {}
    for s in symbols:
        local = s.qualified_name.split(":", 1)[1]
        if "." not in local:
            own_top_level[s.name] = s.qualified_name

    references: list[Reference] = []
    edge_index: dict[tuple[str, str], int] = {}

    def add_edge(src: str, target: str, kind: str) -> None:
        if src == target:
            return
        k = (src, target)
        if k in edge_index:
            existing = references[edge_index[k]]
            if _KIND_RANK[kind] > _KIND_RANK[existing.kind]:
                references[edge_index[k]] = Reference(src, target, kind)
            return
        edge_index[k] = len(references)
        references.append(Reference(src, target, kind))

    for sym in symbols:
        node = _find_node_for_symbol(root, sym)
        if node is None:
            continue
        src = sym.qualified_name

        # Class heritage -> inherits / implements.
        if sym.kind == "class":
            extends, implements = _heritage(node, source)
            for base in extends:
                tgt = _resolve_name(base, bindings, own_top_level)
                if tgt:
                    add_edge(src, tgt, "inherits")
            for iface in implements:
                tgt = _resolve_name(iface, bindings, own_top_level)
                if tgt:
                    add_edge(src, tgt, "implements")
            # class -> its own members (contains).
            for member in symbols:
                if member.parent_class == sym.name:
                    add_edge(src, member.qualified_name, "contains")

        call_names = _collect_call_names(node, source)
        all_names = _collect_identifiers(node, source)
        ns_uses = _collect_namespace_uses(node, source)

        for name in all_names:
            tgt = _resolve_name(name, bindings, own_top_level)
            if tgt is None:
                continue
            kind = "calls" if name in call_names else "references"
            add_edge(src, tgt, kind)

        for ns, member in ns_uses:
            key = bindings.namespaces.get(ns)
            if key is None:
                continue
            tgt = f"{key}:{member}"
            kind = "calls" if member in call_names else "references"
            add_edge(src, tgt, kind)

    return FileData(symbols=symbols, references=references)


def _resolve_name(name: str, bindings: _Bindings, own_top_level: dict[str, str]) -> str | None:
    if name in bindings.symbols:
        return bindings.symbols[name]
    if name in own_top_level:
        return own_top_level[name]
    return None
