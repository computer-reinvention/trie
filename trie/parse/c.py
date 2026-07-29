"""C language backend — tree-sitter symbols + references, paired with clangd.

C has no classes/methods; the symbol set is flat:
  - `function`: `ret name(params) { ... }` (name nested in function_declarator).
  - `class`:    `struct Name { ... }` → `class` (the closest kind for an
                aggregate type).
  - `type`:     `typedef ...` → `type`, named by the typedef's alias.
  - `enum`:     `enum Name { ... }`.
  - `constant`: `#define NAME ...` macros and top-level `const`/global
                declarations with a single named declarator.

Everything at file scope is treated as public (C has no export markers; linkage
is via `static`, which we surface by marking `static` symbols non-public).
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_c
from tree_sitter import Language, Node, Parser

from trie.parse.types import FileData, Reference, Symbol

C_LANGUAGE = Language(tree_sitter_c.language())


def _make_parser() -> Parser:
    parser = Parser()
    parser.language = C_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _module_key(file_path: Path, source_root: Path) -> str:
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _declarator_name(node: Node, source: bytes) -> str | None:
    """Dig through pointer/array/function declarators to the leaf identifier."""
    if node.type == "identifier":
        return _node_text(node, source)
    if node.type in ("field_identifier", "type_identifier"):
        return _node_text(node, source)
    decl = node.child_by_field_name("declarator")
    if decl is not None:
        return _declarator_name(decl, source)
    for c in node.named_children:
        found = _declarator_name(c, source)
        if found:
            return found
    return None


def _is_static(node: Node, source: bytes) -> bool:
    for c in node.named_children:
        if c.type == "storage_class_specifier" and _node_text(c, source) == "static":
            return True
    return False


def _make_symbol(
    node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    name: str,
    kind: str,
    is_public: bool = True,
) -> Symbol:
    body = node.child_by_field_name("body")
    if body is not None:
        signature = source[node.start_byte : body.start_byte].decode("utf-8", "replace").strip()
        body_text = _node_text(body, source)
    else:
        signature = _node_text(node, source).strip()
        body_text = signature
    return Symbol(
        qualified_name=f"{module_key}:{name}",
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
    seen_names: set[str] = set()

    def emit(node, name, kind, is_public=True):
        if name and name not in seen_names:
            seen_names.add(name)
            symbols.append(
                _make_symbol(
                    node,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    name=name,
                    kind=kind,
                    is_public=is_public,
                )
            )

    for child in tree.root_node.named_children:
        t = child.type
        if t == "function_definition":
            decl = child.child_by_field_name("declarator")
            name = _declarator_name(decl, source) if decl else None
            emit(child, name, "function", is_public=not _is_static(child, source))
        elif t == "struct_specifier":
            nm = child.child_by_field_name("name")
            emit(child, _node_text(nm, source) if nm else None, "class")
        elif t == "enum_specifier":
            nm = child.child_by_field_name("name")
            emit(child, _node_text(nm, source) if nm else None, "enum")
        elif t == "type_definition":
            # typedef: the alias is the last declarator
            alias = None
            for c in reversed(child.named_children):
                if c.type in ("type_identifier", "primitive_type"):
                    alias = _node_text(c, source)
                    break
            emit(child, alias, "type")
        elif t == "preproc_def":
            nm = child.child_by_field_name("name")
            emit(child, _node_text(nm, source) if nm else None, "constant")
        elif t == "preproc_function_def":
            nm = child.child_by_field_name("name")
            emit(child, _node_text(nm, source) if nm else None, "function")
        elif t == "declaration":
            # top-level global / const with a single named declarator
            name = _declarator_name(child, source)
            emit(child, name, "constant", is_public=not _is_static(child, source))

    return symbols


def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None:
    target_line = sym.start_line
    match: Node | None = None

    def walk(n: Node) -> None:
        nonlocal match
        if match is not None:
            return
        if n.start_point[0] + 1 == target_line and n.type in (
            "function_definition",
            "struct_specifier",
            "enum_specifier",
            "type_definition",
            "preproc_def",
            "preproc_function_def",
            "declaration",
        ):
            match = n
        for c in n.children:
            walk(c)

    walk(root)
    return match


def _collect_call_names(node: Node, source: bytes) -> set[str]:
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type in ("comment", "string_literal"):
            return
        if n.type == "call_expression":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "identifier":
                names.add(_node_text(fn, source))
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
    own_top_level: dict[str, str] = {s.name: s.qualified_name for s in symbols}

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


C_SYSTEM_PROMPT = """\
You are documenting a C source symbol for a code-navigation graph. Write a
concise, factual description of what the symbol does and why it exists.

- For a function, state what it computes/returns and notable side effects
  (memory ownership, globals touched, I/O).
- For a `struct`/`enum`/typedef, describe the data it models.
- For a macro, state what it expands to or guards.
- Prefer intent over restating the signature.
"""


class CBackend:
    """`LanguageBackend` for C, paired with clangd."""

    name = "c"
    extensions = (".c", ".h")

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
        return ".c"

    def system_prompt(self) -> str:
        return C_SYSTEM_PROMPT

    def resolver(self):
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import c_spec

                spec = c_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver


__all__ = ["C_SYSTEM_PROMPT", "CBackend", "extract_file_data", "extract_symbols"]
