"""Heuristic reference extraction via tree-sitter.

v0.1 covers the cases that catch the most cascade signal with the least machinery:

- `from foo import bar` → bind name `bar` to qualified target `foo:bar`
- `from foo.baz import qux` → bind `qux` to `foo/baz:qux`
- intra-file usage: a top-level symbol's body referencing another top-level symbol's name
  in the same module produces an edge to that symbol

Misses (deferred to v0.2 with proper SCIP):
- `import foo` followed by `foo.bar()` (attribute access on imported module)
- relative imports (`from . import sib`)
- method calls / dynamic dispatch
- shadowed names

The point is to give the cascade enough edges to demonstrate value, not to be sound. Edges
are labelled with `confidence` so downstream consumers (`trie check`) can apply coarser
fallback rules when precision is low.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tree_sitter import Node

from trie.parse.python import (
    Symbol,
    _make_parser,
    _node_text,
    _undecorate,
    extract_symbols,
)


@dataclass(frozen=True)
class Reference:
    """An outbound reference from a symbol within a file.

    `target_qname` is the resolved target's qualified name (e.g. `src/foo:bar`). It's a string
    so it can be persisted before the target's symbol_id is looked up in the DB.
    """

    src_qname: str
    target_qname: str
    confidence: str  # "tree_sitter_import" | "name_match"


@dataclass(frozen=True)
class FileData:
    """Symbols + outbound references extracted from one file in a single tree-sitter parse."""

    symbols: list[Symbol]
    references: list[Reference]


def _collect_imports(root: Node, source: bytes) -> dict[str, str]:
    """Return name → target_qname mapping for `from X import Y` style imports.

    Each binding maps a local name to the qualified name it resolves to. e.g.
    `from foo.bar import baz` → {"baz": "foo/bar:baz"}.
    """
    bindings: dict[str, str] = {}
    for child in root.named_children:
        if child.type == "import_from_statement":
            module_node = child.child_by_field_name("module_name")
            if module_node is None:
                continue
            module_name = _node_text(module_node, source).strip()
            if not module_name or module_name.startswith("."):
                continue  # skip relative imports for v0.1
            module_key = module_name.replace(".", "/")
            for n in child.named_children:
                if n is module_node:
                    continue
                if n.type == "dotted_name":
                    name = _node_text(n, source).strip()
                    if name and "." not in name:
                        bindings[name] = f"{module_key}:{name}"
                elif n.type == "aliased_import":
                    inner_name_node = n.child_by_field_name("name")
                    alias_node = n.child_by_field_name("alias")
                    if inner_name_node and alias_node:
                        original = _node_text(inner_name_node, source).strip()
                        alias = _node_text(alias_node, source).strip()
                        if original and alias and "." not in original:
                            bindings[alias] = f"{module_key}:{original}"
    return bindings


def _collect_identifier_names(node: Node, source: bytes) -> set[str]:
    """Return all identifier-looking names mentioned within `node`'s subtree.

    Includes plain identifiers, the leftmost name of attribute expressions, and call targets.
    Excludes type annotations parsed as identifiers (acceptable noise for v0.1 — they tend
    to refer to in-scope names anyway).
    """
    names: set[str] = set()

    def walk(n: Node) -> None:
        if n.type == "identifier":
            names.add(_node_text(n, source))
        elif n.type == "comment":
            return
        for c in n.children:
            walk(c)

    walk(node)
    return names


def _find_node_for_symbol(root: Node, symbol: Symbol) -> Node | None:
    """Locate the def/class node corresponding to `symbol` so we can scan its body.

    Symbols carry start_line, so we walk top-level + one-deep candidates and match.
    """
    target_line = symbol.start_line
    for child in root.named_children:
        target = _undecorate(child)
        if target.type in ("function_definition", "class_definition"):
            if target.start_point[0] + 1 == target_line:
                return target
            if target.type == "class_definition":
                body = target.child_by_field_name("body")
                if body is None:
                    continue
                for grandchild in body.named_children:
                    inner = _undecorate(grandchild)
                    if (
                        inner.type == "function_definition"
                        and inner.start_point[0] + 1 == target_line
                    ):
                        return inner
    return None


def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData:
    """Parse a Python file once and return both its symbols and outbound references."""
    file_path = file_path.resolve()
    source_root_resolved = (source_root or file_path.parent).resolve()
    source = file_path.read_bytes()
    tree = _make_parser().parse(source)
    root = tree.root_node

    symbols = extract_symbols(file_path, source_root=source_root_resolved)

    imports = _collect_imports(root, source)
    own_top_level: dict[str, str] = {}
    for s in symbols:
        # Only top-level symbols (no `.` in the local part of qname after the colon)
        local = s.qualified_name.split(":", 1)[1]
        if "." not in local:
            own_top_level[s.name] = s.qualified_name

    references: list[Reference] = []
    seen: set[tuple[str, str]] = set()  # (src_qname, target_qname) dedup

    for sym in symbols:
        node = _find_node_for_symbol(root, sym)
        if node is None:
            continue
        body = node.child_by_field_name("body")
        if body is None:
            continue
        names = _collect_identifier_names(body, source)
        for name in names:
            if name == sym.name:
                continue  # skip self-references (recursion is fine, just not edge-useful)
            if name in imports:
                target = imports[name]
                key = (sym.qualified_name, target)
                if key not in seen:
                    seen.add(key)
                    references.append(
                        Reference(
                            src_qname=sym.qualified_name,
                            target_qname=target,
                            confidence="tree_sitter_import",
                        )
                    )
            elif name in own_top_level:
                target = own_top_level[name]
                if target == sym.qualified_name:
                    continue
                key = (sym.qualified_name, target)
                if key not in seen:
                    seen.add(key)
                    references.append(
                        Reference(
                            src_qname=sym.qualified_name,
                            target_qname=target,
                            confidence="name_match",
                        )
                    )

    return FileData(symbols=symbols, references=references)


__all__ = ["FileData", "Reference", "extract_file_data"]
