"""Reference extraction via tree-sitter.

This is an implementation detail of trie's graph. Today it's a tree-sitter heuristic;
tomorrow it'll be SCIP/Pyright. The downstream contract — the `Reference` dataclass and
the store's `replace_all_edges` — does not change when the resolver changes. There is no
edge-level confidence field exposed to the rest of the system: an edge either exists
(precise enough to act on) or it doesn't.

Today's coverage:

- `from foo import bar` → bind `bar` to qualified target `foo:bar`
- `from foo.baz import qux` → bind `qux` to `foo/baz:qux`
- `import foo` followed by `foo.bar()` → edge to `foo:bar`
- `import foo.baz` followed by `foo.baz.qux()` → edge to `foo/baz:qux`
- `import foo as f` followed by `f.bar()` → edge to `foo:bar`
- intra-file usage: a top-level symbol's body referencing another top-level symbol's name
  in the same module produces an edge to that symbol

The extractor is permissive: it emits candidate edges for every plausible target qname.
The store's `replace_all_edges` resolves those candidates against the known symbols
table and silently drops edges to qnames the project doesn't define. That means
`import os; os.path.join(...)` produces a candidate edge to `os/path:join` which the
store then drops — no special-casing of stdlib or third-party imports needed here.

Today's misses (closed when the resolver gets replaced):

- relative imports (`from . import sib`)
- method calls / dynamic dispatch on instances (`obj.method()` where `obj` is a parameter)
- shadowed names (local rebinding of an imported name)
- `import foo.bar.baz` with three-level attribute access
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


@dataclass(frozen=True)
class FileData:
    """Symbols + outbound references extracted from one file in a single tree-sitter parse."""

    symbols: list[Symbol]
    references: list[Reference]


@dataclass(frozen=True)
class _ImportBindings:
    """Two binding tables produced by walking a module's import statements once.

    `symbols` maps a local name introduced by `from X import Y` to a fully-qualified
    target qname (e.g. `{"emit": "trie/telemetry:emit"}`). Hits here become edges
    directly when the local name appears as a bare identifier in a function body.

    `modules` maps a local name introduced by `import X` (or `import X.Y`, or
    `import X as Y`) to a *module path* in the slash-separated form trie uses for
    qnames (e.g. `{"telemetry": "trie/telemetry"}`). Hits here become edges only
    when the local name appears as the leftmost part of an attribute access, with
    the attribute providing the symbol name (`telemetry.emit` → `trie/telemetry:emit`).

    Keeping the two kinds separate makes resolution rule-by-rule explicit instead
    of overloading a single dict's values with a sentinel.
    """

    symbols: dict[str, str]
    modules: dict[str, str]


def _collect_imports(root: Node, source: bytes) -> _ImportBindings:
    """Build the symbol and module binding tables for one module.

    Handled syntactic forms:

      - `from foo import bar`        → symbols["bar"] = "foo:bar"
      - `from foo.baz import qux`    → symbols["qux"] = "foo/baz:qux"
      - `from foo import bar as b`   → symbols["b"]   = "foo:bar"
      - `import foo`                 → modules["foo"] = "foo"
      - `import foo.bar`             → modules["foo.bar"] = "foo/bar"
                                       AND modules["foo"] = "foo"   (so plain `foo.X(...)` resolves too)
      - `import foo as f`            → modules["f"]   = "foo"
      - `import foo.bar as fb`       → modules["fb"]  = "foo/bar"

    Relative imports (leading `.`) are skipped — v0.1 has no project root context
    inside the parser to resolve them against.
    """
    symbols: dict[str, str] = {}
    modules: dict[str, str] = {}

    for child in root.named_children:
        if child.type == "import_from_statement":
            _absorb_from_import(child, source, symbols, modules)
        elif child.type == "import_statement":
            _absorb_plain_import(child, source, modules)

    return _ImportBindings(symbols=symbols, modules=modules)


def _absorb_from_import(
    child: Node,
    source: bytes,
    symbols: dict[str, str],
    modules: dict[str, str] | None = None,
) -> None:
    """Populate `symbols` (and optionally `modules`) from one `from X import Y` statement.

    When `modules` is provided, every imported name also gets registered as a
    candidate module binding `parent_module/name`. This covers the common
    "import a submodule via from-import" pattern: `from trie import scan;
    scan.scan_project(...)` should resolve to `trie/scan:scan_project`. Without
    runtime info we can't tell whether `scan` is a module or a value; we register
    both interpretations and rely on the store dropping candidates whose target
    qname doesn't actually exist in the symbols table.
    """
    module_node = child.child_by_field_name("module_name")
    if module_node is None:
        return
    module_name = _node_text(module_node, source).strip()
    if not module_name or module_name.startswith("."):
        return  # relative imports: skipped
    module_key = module_name.replace(".", "/")
    for n in child.named_children:
        if n is module_node:
            continue
        if n.type == "dotted_name":
            name = _node_text(n, source).strip()
            if name and "." not in name:
                symbols[name] = f"{module_key}:{name}"
                if modules is not None:
                    modules.setdefault(name, f"{module_key}/{name}")
        elif n.type == "aliased_import":
            inner_name_node = n.child_by_field_name("name")
            alias_node = n.child_by_field_name("alias")
            if inner_name_node and alias_node:
                original = _node_text(inner_name_node, source).strip()
                alias = _node_text(alias_node, source).strip()
                if original and alias and "." not in original:
                    symbols[alias] = f"{module_key}:{original}"
                    if modules is not None:
                        modules.setdefault(alias, f"{module_key}/{original}")


def _absorb_plain_import(child: Node, source: bytes, modules: dict[str, str]) -> None:
    """Populate `modules` from one `import X[, Y as alias, ...]` statement.

    For `import foo.bar` we register both `"foo.bar"` and `"foo"` as bindings. The
    former lets `foo.bar.baz(...)` resolve to `foo/bar:baz`; the latter is a
    pragmatic concession to the common pattern `import package.module` followed by
    bare `package.thing(...)` in the body (where `thing` is actually exposed by
    `package/__init__.py`). The store's existence filter drops misfires.
    """
    for n in child.named_children:
        if n.type == "dotted_name":
            dotted = _node_text(n, source).strip()
            if not dotted or dotted.startswith("."):
                continue
            module_key = dotted.replace(".", "/")
            modules[dotted] = module_key
            # Also register the leftmost component so `import foo.bar` followed by
            # `foo.something(...)` resolves (something defined in foo/__init__).
            head = dotted.split(".", 1)[0]
            modules.setdefault(head, head)
        elif n.type == "aliased_import":
            inner_name_node = n.child_by_field_name("name")
            alias_node = n.child_by_field_name("alias")
            if inner_name_node and alias_node:
                original = _node_text(inner_name_node, source).strip()
                alias = _node_text(alias_node, source).strip()
                if original and alias and not original.startswith("."):
                    modules[alias] = original.replace(".", "/")


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


def _collect_attribute_accesses(node: Node, source: bytes) -> set[tuple[str, str]]:
    """Return `(base, attr)` pairs for every `<base>.<attr>` access in the subtree,
    including chained accesses like `a.b.c` which yield `("a.b", "c")` *and*
    `("a", "b")`.

    Tree-sitter parses `a.b.c` as nested attribute nodes: `(attribute (attribute a b) c)`.
    For each `attribute` node we emit a pair where `base` is the dotted source slice
    of its `object` field (so `("a", "b")` or `("a.b", "c")`) and `attr` is the
    attribute name. The resolver checks both forms against the module bindings —
    `import foo.bar` registers `"foo.bar"` *and* `"foo"`, so `foo.bar.baz` can
    resolve via the longer path while `foo.bar` (used as `foo/bar:bar`-like) still
    works when the dotted base matches.

    Comments and string nodes are skipped to keep the result focused on real
    name references.
    """
    pairs: set[tuple[str, str]] = set()

    def walk(n: Node) -> None:
        if n.type == "comment" or n.type == "string":
            return
        if n.type == "attribute":
            object_node = n.child_by_field_name("object")
            attr_node = n.child_by_field_name("attribute")
            if (
                object_node is not None
                and attr_node is not None
                and attr_node.type == "identifier"
                and object_node.type in ("identifier", "attribute")
            ):
                base = _dotted_text(object_node, source)
                attr = _node_text(attr_node, source)
                if base and attr:
                    pairs.add((base, attr))
        for c in n.children:
            walk(c)

    walk(node)
    return pairs


def _dotted_text(node: Node, source: bytes) -> str:
    """Render an attribute-or-identifier subtree back as a dotted name like `"a.b.c"`.

    Returns the empty string for any node shape we don't recognise (e.g. when an
    attribute's object is a call or a subscript). That keeps the resolver from
    inventing module bindings for arbitrary expressions.
    """
    if node.type == "identifier":
        return _node_text(node, source)
    if node.type == "attribute":
        object_node = node.child_by_field_name("object")
        attr_node = node.child_by_field_name("attribute")
        if object_node is None or attr_node is None or attr_node.type != "identifier":
            return ""
        base = _dotted_text(object_node, source)
        if not base:
            return ""
        return f"{base}.{_node_text(attr_node, source)}"
    return ""


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

    bindings = _collect_imports(root, source)
    own_top_level: dict[str, str] = {}
    for s in symbols:
        # Only top-level symbols (no `.` in the local part of qname after the colon)
        local = s.qualified_name.split(":", 1)[1]
        if "." not in local:
            own_top_level[s.name] = s.qualified_name

    references: list[Reference] = []
    seen: set[tuple[str, str]] = set()  # (src_qname, target_qname) dedup

    def _maybe_add_edge(src: str, target: str) -> None:
        """Add an outbound edge, deduping and dropping self-edges.

        The store has the authoritative "does this target exist in the project"
        filter, so we don't gate on resolution accuracy here — we just dedupe.
        """
        if target == src:
            return
        key = (src, target)
        if key in seen:
            return
        seen.add(key)
        references.append(Reference(src_qname=src, target_qname=target))

    for sym in symbols:
        node = _find_node_for_symbol(root, sym)
        if node is None:
            continue
        body = node.child_by_field_name("body")
        if body is None:
            continue

        # Bare-identifier edges (existing path): `from X import Y; Y(...)` or a local
        # top-level name. Self-references (recursion) are dropped.
        names = _collect_identifier_names(body, source)
        for name in names:
            if name == sym.name:
                continue
            if name in bindings.symbols:
                _maybe_add_edge(sym.qualified_name, bindings.symbols[name])
            elif name in own_top_level:
                _maybe_add_edge(sym.qualified_name, own_top_level[name])

        # Module-attribute edges: `import X; X.Y(...)` resolves to `X:Y`, where the
        # base of the attribute access matches a module binding. Each attribute
        # access yields one candidate edge; the store drops candidates whose target
        # isn't a project symbol (so stdlib / third-party attribute accesses are
        # automatically filtered).
        attr_pairs = _collect_attribute_accesses(body, source)
        for base, attr in attr_pairs:
            if base in bindings.modules:
                module_path = bindings.modules[base]
                _maybe_add_edge(sym.qualified_name, f"{module_path}:{attr}")

    return FileData(symbols=symbols, references=references)


__all__ = ["FileData", "Reference", "extract_file_data"]
