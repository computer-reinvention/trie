"""Go language backend — tree-sitter symbols + references, paired with gopls.

Mirrors the Python/TypeScript backends: a fast structural pass extracts symbols
and the edges tree-sitter can resolve syntactically (imports, containment,
same-package calls), and the paired `LspResolver` (gopls) fills the
method-dispatch gap.

Go shapes handled:
  - `function`: top-level `func Name(...)`.
  - `method`:   `func (r Recv) Name(...)` — attributed to its receiver type,
                so the qname is `pkg/mod:Recv.Name` (matching how the resolver
                maps `x.Name()` back once gopls resolves the receiver type).
  - `type` / `class`: `type Name struct { ... }` becomes a `class`; other
                `type Name = ...` / interface / alias declarations become
                `type`. Struct fields and interface methods are not emitted as
                separate symbols in v1 (kept flat like the Python constant view).
  - `constant`: top-level `const`/`var` single-name declarations.
  - `module`:   synthetic `__module__` holding package clause + imports.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_go
from tree_sitter import Language, Node, Parser

from trie.parse.types import FileData, Reference, Symbol

GO_LANGUAGE = Language(tree_sitter_go.language())


def _make_parser() -> Parser:
    parser = Parser()
    parser.language = GO_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _module_key(file_path: Path, source_root: Path) -> str:
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _signature_text(node: Node, source: bytes) -> str:
    """Header text up to the body block (no trailing brace)."""
    body = node.child_by_field_name("body")
    end = body.start_byte if body is not None else node.end_byte
    return source[node.start_byte : end].decode("utf-8", errors="replace").strip()


def _is_public_go(name: str) -> bool:
    """Go exports identifiers that start with an uppercase letter."""
    return bool(name) and name[0].isupper()


def _receiver_type(method_node: Node, source: bytes) -> str | None:
    """Return the receiver type name of a `method_declaration`, e.g. `T` from `(t *T)`."""
    receiver = method_node.child_by_field_name("receiver")
    if receiver is None:
        return None
    for decl in receiver.named_children:
        # parameter_declaration -> type may be pointer_type(type_identifier) or type_identifier
        tnode = decl.child_by_field_name("type") or decl
        return _rightmost_type_identifier(tnode, source)
    return None


def _rightmost_type_identifier(node: Node, source: bytes) -> str | None:
    if node.type == "type_identifier":
        return _node_text(node, source)
    for c in reversed(node.named_children):
        found = _rightmost_type_identifier(c, source)
        if found:
            return found
    return None


def _make_symbol(
    node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    name: str,
    kind: str,
    parent: str | None = None,
) -> Symbol:
    body = node.child_by_field_name("body")
    signature = _signature_text(node, source)
    body_text = _node_text(body, source) if body is not None else _node_text(node, source)
    dotted = f"{parent}.{name}" if parent else name
    is_public = _is_public_go(name) and (parent is None or _is_public_go(parent))
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
    root = tree.root_node

    for child in root.named_children:
        if child.type == "function_declaration":
            name_node = child.child_by_field_name("name")
            if name_node is not None:
                symbols.append(
                    _make_symbol(
                        child,
                        source,
                        module_key=module_key,
                        rel_file=rel_file,
                        name=_node_text(name_node, source),
                        kind="function",
                    )
                )
        elif child.type == "method_declaration":
            name_node = child.child_by_field_name("name")
            recv = _receiver_type(child, source)
            if name_node is not None:
                symbols.append(
                    _make_symbol(
                        child,
                        source,
                        module_key=module_key,
                        rel_file=rel_file,
                        name=_node_text(name_node, source),
                        kind="method",
                        parent=recv,
                    )
                )
        elif child.type == "type_declaration":
            for spec in child.named_children:
                if spec.type != "type_spec":
                    continue
                name_node = spec.child_by_field_name("name")
                type_node = spec.child_by_field_name("type")
                if name_node is None:
                    continue
                name = _node_text(name_node, source)
                kind = "class" if (type_node and type_node.type == "struct_type") else "type"
                if type_node is not None and type_node.type == "interface_type":
                    kind = "interface"
                symbols.append(
                    _make_symbol(
                        spec,
                        source,
                        module_key=module_key,
                        rel_file=rel_file,
                        name=name,
                        kind=kind,
                    )
                )
        elif child.type in ("const_declaration", "var_declaration"):
            for spec in child.named_children:
                if spec.type not in ("const_spec", "var_spec"):
                    continue
                name_node = spec.child_by_field_name("name")
                if name_node is None:
                    # const_spec name is a plain identifier child
                    for c in spec.named_children:
                        if c.type == "identifier":
                            name_node = c
                            break
                if name_node is not None:
                    symbols.append(
                        _make_symbol(
                            spec,
                            source,
                            module_key=module_key,
                            rel_file=rel_file,
                            name=_node_text(name_node, source),
                            kind="constant",
                        )
                    )

    return symbols


def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None:
    """Locate the definition node whose start line matches the symbol."""
    target_line = sym.start_line
    match: Node | None = None

    def walk(n: Node) -> None:
        nonlocal match
        if match is not None:
            return
        if n.start_point[0] + 1 == target_line and n.type in (
            "function_declaration",
            "method_declaration",
            "type_spec",
            "const_spec",
            "var_spec",
        ):
            match = n
        for c in n.children:
            walk(c)

    walk(root)
    return match


def _collect_call_names(node: Node, source: bytes) -> set[str]:
    """Identifiers in call position: `Foo()` adds `Foo`; `x.M()` adds `M`."""
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "interpreted_string_literal", "raw_string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None:
                if fn.type == "identifier":
                    names.add(_node_text(fn, source))
                elif fn.type == "selector_expression":
                    field = fn.child_by_field_name("field")
                    if field is not None:
                        names.add(_node_text(field, source))
        for c in n.children:
            walk(c)

    walk(node)
    return names


def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData:
    """Symbols + same-file/same-package reference edges (tree-sitter only)."""
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
        called = _collect_call_names(node, source)
        for name in called:
            if name in own_top_level:
                add(sym.qualified_name, own_top_level[name], "calls")

    return FileData(symbols=symbols, references=references)


GO_SYSTEM_PROMPT = """\
You are documenting a Go source symbol for a code-navigation graph. Write a
concise, factual description of what the symbol does and why it exists.

- For a `func`, state what it computes/returns and any important side effects.
- For a `method`, name its receiver type and the behaviour it adds.
- For a `type` (struct/interface), describe the data it models or the contract
  it defines; do not enumerate every field.
- Prefer behaviour and intent over restating the signature.
"""


class GoBackend:
    """`LanguageBackend` for Go, paired with gopls for method resolution."""

    name = "go"
    extensions = (".go",)

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
        return ".go"

    def system_prompt(self) -> str:
        return GO_SYSTEM_PROMPT

    def resolver(self):
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import go_spec

                spec = go_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver


__all__ = ["GO_SYSTEM_PROMPT", "GoBackend", "extract_file_data", "extract_symbols"]
