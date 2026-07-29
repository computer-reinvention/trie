"""Rust language backend — tree-sitter symbols + references, paired with rust-analyzer.

Rust shapes handled:
  - `function`: top-level `fn name(...)`.
  - `class`:    `struct Name { ... }` (and tuple structs) → `class`.
  - `enum`:     `enum Name { ... }`.
  - `interface`: `trait Name { ... }` (a contract, like an interface).
  - `type`:     `type Name = ...` alias.
  - `method`:   `fn name(...)` inside an `impl Type { ... }` block, attributed
                to the impl's type → qname `mod:Type.name`. Trait-default methods
                inside `trait Name { ... }` are attributed to the trait.
  - `constant`: top-level `const`/`static` item.
  - `module`:   synthetic `__module__` is NOT emitted for Rust in v1 (use/mod
                lines are cheap and rarely worth a symbol); can be added later.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_rust
from tree_sitter import Language, Node, Parser

from trie.parse.types import FileData, Reference, Symbol

RUST_LANGUAGE = Language(tree_sitter_rust.language())


def _make_parser() -> Parser:
    parser = Parser()
    parser.language = RUST_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _module_key(file_path: Path, source_root: Path) -> str:
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _signature_text(node: Node, source: bytes) -> str:
    body = node.child_by_field_name("body")
    end = body.start_byte if body is not None else node.end_byte
    return source[node.start_byte : end].decode("utf-8", errors="replace").strip()


def _has_pub(node: Node, source: bytes) -> bool:
    return any(c.type == "visibility_modifier" for c in node.named_children)


def _make_symbol(
    node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    name: str,
    kind: str,
    parent: str | None = None,
    parent_is_private: bool = False,
) -> Symbol:
    body = node.child_by_field_name("body")
    signature = _signature_text(node, source)
    body_text = _node_text(body, source) if body is not None else _node_text(node, source)
    dotted = f"{parent}.{name}" if parent else name
    is_public = _has_pub(node, source) and not parent_is_private
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


def _type_name(node: Node, source: bytes) -> str | None:
    """The `type_identifier` name of a struct/enum/trait/impl target."""
    for c in node.named_children:
        if c.type == "type_identifier":
            return _node_text(c, source)
    return None


def _impl_target(impl_node: Node, source: bytes) -> str | None:
    """The type an `impl` block is for: `impl Counter` or `impl Trait for Counter`.

    Returns the concrete type (the last type_identifier before the body), so
    `impl Display for Counter` attributes methods to `Counter`.
    """
    target: str | None = None
    for c in impl_node.named_children:
        if c.type == "type_identifier":
            target = _node_text(c, source)
        elif c.type == "declaration_list":
            break
    return target


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

    def emit(node, name, kind, parent=None, parent_is_private=False):
        if name:
            symbols.append(
                _make_symbol(
                    node,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    name=name,
                    kind=kind,
                    parent=parent,
                    parent_is_private=parent_is_private,
                )
            )

    for child in tree.root_node.named_children:
        t = child.type
        if t == "function_item":
            name_node = child.child_by_field_name("name")
            emit(child, _node_text(name_node, source) if name_node else None, "function")
        elif t == "struct_item":
            emit(child, _type_name(child, source), "class")
        elif t == "enum_item":
            emit(child, _type_name(child, source), "enum")
        elif t == "trait_item":
            trait_name = _type_name(child, source)
            emit(child, trait_name, "interface")
            body = child.child_by_field_name("body")
            if body is not None and trait_name is not None:
                trait_private = not _has_pub(child, source)
                for m in body.named_children:
                    if m.type == "function_item":
                        mn = m.child_by_field_name("name")
                        emit(
                            m,
                            _node_text(mn, source) if mn else None,
                            "method",
                            parent=trait_name,
                            parent_is_private=trait_private,
                        )
        elif t == "type_item":
            name_node = child.child_by_field_name("name")
            emit(child, _node_text(name_node, source) if name_node else None, "type")
        elif t in ("const_item", "static_item"):
            name_node = child.child_by_field_name("name")
            emit(child, _node_text(name_node, source) if name_node else None, "constant")
        elif t == "impl_item":
            target = _impl_target(child, source)
            body = child.child_by_field_name("body")
            if body is not None and target is not None:
                target_private = target.startswith("_")
                for m in body.named_children:
                    if m.type == "function_item":
                        mn = m.child_by_field_name("name")
                        emit(
                            m,
                            _node_text(mn, source) if mn else None,
                            "method",
                            parent=target,
                            parent_is_private=target_private,
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
            "function_item",
            "struct_item",
            "enum_item",
            "trait_item",
            "type_item",
            "const_item",
            "static_item",
        ):
            match = n
        for c in n.children:
            walk(c)

    walk(root)
    return match


def _collect_call_names(node: Node, source: bytes) -> set[str]:
    """Names in call position: `foo()` adds `foo`; `x.m()` adds `m`; `Type::new()` adds `new`."""
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("line_comment", "block_comment", "string_literal", "raw_string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None:
                if fn.type == "identifier":
                    names.add(_node_text(fn, source))
                elif fn.type == "field_expression":
                    field = fn.child_by_field_name("field")
                    if field is not None:
                        names.add(_node_text(field, source))
                elif fn.type == "scoped_identifier":
                    nm = fn.child_by_field_name("name")
                    if nm is not None:
                        names.add(_node_text(nm, source))
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


RUST_SYSTEM_PROMPT = """\
You are documenting a Rust source symbol for a code-navigation graph. Write a
concise, factual description of what the symbol does and why it exists.

- For a `fn`, state what it computes/returns and notable side effects or
  ownership/borrowing behaviour.
- For a `struct`/`enum`, describe the data it models; for a `trait`, the
  contract it defines.
- For a `method` (in an `impl`), name its type and the behaviour it adds.
- Prefer intent over restating the signature.
"""


class RustBackend:
    """`LanguageBackend` for Rust, paired with rust-analyzer."""

    name = "rust"
    extensions = (".rs",)

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
        return ".rs"

    def system_prompt(self) -> str:
        return RUST_SYSTEM_PROMPT

    def resolver(self):
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import rust_spec

                spec = rust_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver


__all__ = ["RUST_SYSTEM_PROMPT", "RustBackend", "extract_file_data", "extract_symbols"]
