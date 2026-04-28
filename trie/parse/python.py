from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import tree_sitter_python
from tree_sitter import Language, Node, Parser

PY_LANGUAGE = Language(tree_sitter_python.language())


@dataclass(frozen=True)
class Symbol:
    qualified_name: str
    kind: str  # "function" | "class" | "method"
    name: str
    file_path: str  # source-root-relative, e.g. "src/foo.py"
    signature: str
    docstring: str | None
    body_text: str
    body_normalized_hash: str
    signature_hash: str
    start_line: int  # 1-indexed
    end_line: int  # 1-indexed inclusive
    is_public: bool


def _make_parser() -> Parser:
    parser = Parser()
    parser.language = PY_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _module_key(file_path: Path, source_root: Path) -> str:
    """Return the module key used in qualified names — file path minus extension, e.g. src/foo."""
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _signature_text(node: Node, source: bytes) -> str:
    """For a function_definition or class_definition, the header text (def/class ... — no trailing colon)."""
    body_node = node.child_by_field_name("body")
    end = body_node.start_byte if body_node else node.end_byte
    raw = source[node.start_byte : end].decode("utf-8", errors="replace")
    return raw.rstrip().rstrip(":").rstrip()


def _extract_docstring(body_node: Node | None, source: bytes) -> str | None:
    if body_node is None:
        return None
    for child in body_node.named_children:
        if child.type == "expression_statement" and child.named_child_count > 0:
            first = child.named_children[0]
            if first.type == "string":
                return _node_text(first, source)
        # Only the very first statement counts as the docstring.
        return None
    return None


def _normalize_body_tokens(node: Node | None, source: bytes) -> str:
    """Concatenate leaf-token text from `node`, skipping comments. Used for change detection."""
    if node is None:
        return ""
    parts: list[str] = []

    def walk(n: Node) -> None:
        if n.type == "comment":
            return
        if n.child_count == 0:
            text = source[n.start_byte : n.end_byte].decode("utf-8", errors="replace").strip()
            if text:
                parts.append(text)
            return
        for c in n.children:
            walk(c)

    walk(node)
    return " ".join(parts)


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _build_symbol(
    node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    parent: str | None,
    kind: str,
    parent_is_private: bool = False,
) -> Symbol:
    name_node = node.child_by_field_name("name")
    name = _node_text(name_node, source) if name_node else "<anon>"
    body_node = node.child_by_field_name("body")
    signature = _signature_text(node, source)
    docstring = _extract_docstring(body_node, source)
    body_text = _node_text(body_node, source) if body_node else ""
    normalized = _normalize_body_tokens(body_node, source)
    dotted = f"{parent}.{name}" if parent else name
    is_public = not name.startswith("_") and not parent_is_private
    return Symbol(
        qualified_name=f"{module_key}:{dotted}",
        kind=kind,
        name=name,
        file_path=rel_file,
        signature=signature,
        docstring=docstring,
        body_text=body_text,
        body_normalized_hash=_hash(normalized),
        signature_hash=_hash(signature),
        start_line=node.start_point[0] + 1,
        end_line=node.end_point[0] + 1,
        is_public=is_public,
    )


def _undecorate(node: Node) -> Node:
    """If `node` is a decorated_definition, return the inner def/class. Otherwise return as-is."""
    if node.type == "decorated_definition":
        inner = node.child_by_field_name("definition")
        if inner is not None:
            return inner
    return node


def _walk_class(class_node: Node, source: bytes, *, module_key: str, rel_file: str) -> list[Symbol]:
    """Emit the class symbol plus method symbols (one level deep).

    Methods of a private class (`_Foo`) inherit the private flag — they are implementation
    detail of an internal type and should not be documented in v0.1.
    """
    name_node = class_node.child_by_field_name("name")
    class_name = _node_text(name_node, source) if name_node else "?"
    class_is_private = class_name.startswith("_")
    syms = [
        _build_symbol(
            class_node,
            source,
            module_key=module_key,
            rel_file=rel_file,
            parent=None,
            kind="class",
        )
    ]
    body = class_node.child_by_field_name("body")
    if body is None:
        return syms
    for child in body.named_children:
        target = _undecorate(child)
        if target.type == "function_definition":
            syms.append(
                _build_symbol(
                    target,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    parent=class_name,
                    kind="method",
                    parent_is_private=class_is_private,
                )
            )
    return syms


def extract_symbols(file_path: Path, source_root: Path | None = None) -> list[Symbol]:
    """Parse a Python file and return its top-level functions, classes, and class methods.

    `source_root` controls the qualified_name prefix and the stored file_path. If None,
    defaults to the file's parent directory.
    """
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = file_path.read_bytes()
    tree = _make_parser().parse(source)
    module_key = _module_key(file_path, source_root)
    rel_file = str(file_path.relative_to(source_root))

    symbols: list[Symbol] = []
    for child in tree.root_node.named_children:
        target = _undecorate(child)
        if target.type == "function_definition":
            symbols.append(
                _build_symbol(
                    target,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    parent=None,
                    kind="function",
                )
            )
        elif target.type == "class_definition":
            symbols.extend(_walk_class(target, source, module_key=module_key, rel_file=rel_file))
    return symbols
