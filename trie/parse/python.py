from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_python
from tree_sitter import Language, Node, Parser

# Symbol now lives in the language-neutral types module. Re-exported here so the
# many existing `from trie.parse.python import Symbol` call sites keep working.
from trie.parse.types import KINDS, Symbol

__all__ = ["KINDS", "Symbol"]

PY_LANGUAGE = Language(tree_sitter_python.language())


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
    decorators: tuple[str, ...] = (),
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
        parent_class=parent,
        decorators=decorators,
    )


def _extract_decorators(node: Node, source: bytes) -> tuple[str, ...]:
    """Return decorator lines from a `decorated_definition` node, e.g. `("@classmethod",)`.

    Returns an empty tuple when `node` is not a `decorated_definition` or carries no
    decorator children. Each entry is the verbatim decorator text with leading whitespace
    stripped — enough for the LLM prompt to see `@property` or `@dataclass(frozen=True)`.
    """
    if node.type != "decorated_definition":
        return ()
    decorators: list[str] = []
    for child in node.named_children:
        if child.type == "decorator":
            decorators.append(_node_text(child, source).strip())
    return tuple(decorators)


def _undecorate(node: Node) -> Node:
    """If `node` is a decorated_definition, return the inner def/class. Otherwise return as-is."""
    if node.type == "decorated_definition":
        inner = node.child_by_field_name("definition")
        if inner is not None:
            return inner
    return node


def _walk_class(
    class_node: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    class_decorators: tuple[str, ...] = (),
) -> list[Symbol]:
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
            decorators=class_decorators,
        )
    ]
    body = class_node.child_by_field_name("body")
    if body is None:
        return syms
    for child in body.named_children:
        method_decorators = _extract_decorators(child, source)
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
                    decorators=method_decorators,
                )
            )
    return syms


def extract_module_docstring(file_path: Path) -> str | None:
    """Return the module-level docstring (raw, as it appears in source), or None.

    Tree-sitter exposes module-level statements as direct children of the root node;
    a leading expression-statement whose first named child is a `string` is the
    PEP 257 module docstring. The literal text (including quote marks) is returned —
    callers strip surrounding quotes when surfacing it as plain text.
    """
    file_path = file_path.resolve()
    source = file_path.read_bytes()
    tree = _make_parser().parse(source)
    for child in tree.root_node.named_children:
        if child.type == "expression_statement" and child.named_child_count > 0:
            first = child.named_children[0]
            if first.type == "string":
                return _node_text(first, source)
        # Only the very first statement is the module docstring per PEP 257.
        return None
    return None


def strip_string_literal(raw: str) -> str:
    """Strip Python string-literal delimiters and a leading f/r/b prefix.

    Used to convert a tree-sitter `string` node text into the docstring content.
    Handles triple-quoted, single-quoted, and prefixed strings. Returns the raw
    contents with surrounding whitespace stripped.
    """
    s = raw.lstrip()
    # Strip a leading prefix like r, R, b, B, u, U, rb, Rb, etc.
    i = 0
    while i < len(s) and s[i] in "rRbBuUfF" and i < 2:
        i += 1
    s = s[i:]
    for triple in ('"""', "'''"):
        if s.startswith(triple) and s.endswith(triple):
            return s[len(triple) : -len(triple)].strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1].strip()
    return s.strip()


def _build_constant_symbol(
    node: Node,
    assignment_node: Node,
    target_name: str,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
) -> Symbol:
    """Build a `kind='constant'` Symbol for a module-level `NAME = value` assignment.

    `node` is the wrapping `expression_statement` (so the line range covers the
    full statement including any trailing comment); `assignment_node` is the
    inner `assignment` that holds the right-hand side.

    The `signature` is the assignment statement itself, truncated if very long —
    enough for the agent to see what was assigned without reading the body.
    Constants don't have a meaningful "body" separate from their signature, so
    `body_text` is also the assignment text; the body-fingerprint is computed
    over a token-normalised copy so whitespace tweaks don't churn the
    fingerprint.
    """
    statement_text = _node_text(node, source)
    # Trim the signature line at the first newline if any (multi-line
    # assignments stay readable in the file view; the signature card stays
    # one line). The full statement still lives in `body_text`.
    first_line = statement_text.split("\n", 1)[0].rstrip()
    docstring = None
    body_text = statement_text
    normalized = _normalize_body_tokens(assignment_node, source)
    is_public = not target_name.startswith("_") or _is_dunder(target_name)
    return Symbol(
        qualified_name=f"{module_key}:{target_name}",
        kind="constant",
        name=target_name,
        file_path=rel_file,
        signature=first_line,
        docstring=docstring,
        body_text=body_text,
        body_normalized_hash=_hash(normalized),
        signature_hash=_hash(first_line),
        start_line=node.start_point[0] + 1,
        end_line=node.end_point[0] + 1,
        is_public=is_public,
    )


def _is_dunder(name: str) -> bool:
    """True for `__name__`-shape identifiers (dunder, double-underscore wrapped).

    Used to keep `__all__`, `__version__`, `__author__`, etc. as `is_public=True`
    even though they start with an underscore. Dunders are part of a module's
    documented surface, not implementation detail.
    """
    return name.startswith("__") and name.endswith("__") and len(name) > 4


def _module_level_constant(node: Node, source: bytes) -> tuple[Node, str] | None:
    """If `node` is a top-level `NAME = value` (or `NAME: T = value`) assignment,
    return (assignment_node, name). Otherwise None.

    Skips tuple unpacking (`X, Y = 1, 2`) and attribute targets (`obj.attr = ...`).
    Those have ambiguous "symbol names" and indexing them would clutter the
    symbol table; we only capture single-identifier targets, which covers the
    overwhelmingly common case (module constants, dunder declarations, simple
    framework instantiations like `app = FastAPI()`).
    """
    if node.type != "expression_statement":
        return None
    if node.named_child_count == 0:
        return None
    inner = node.named_children[0]
    if inner.type != "assignment":
        return None
    left = inner.child_by_field_name("left")
    if left is None or left.type != "identifier":
        return None
    name = _node_text(left, source)
    if not name:
        return None
    return inner, name


def _build_module_body_symbol(
    tree_root: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    consumed_ranges: list[tuple[int, int]],
    noise_ranges: list[tuple[int, int]] | None = None,
) -> Symbol | None:
    """Build a single synthetic `kind='module'` symbol carrying the residual
    module-level code that isn't captured by any other symbol.

    `consumed_ranges` is the list of `(start_line, end_line)` for symbols
    already extracted (functions, classes, constants). `noise_ranges` covers
    lines that are real module-level syntax but carry no behaviour worth
    surfacing as a symbol (imports, the module docstring). Both are
    subtracted from the residual; the symbol is only emitted when something
    *interesting* remains — a top-level call like `setup(...)`, an
    `if __name__ == "__main__":` block, or some other top-level expression.

    Files that are pure-defs-plus-imports get no `__module__` symbol; their
    behaviour is captured entirely by the per-symbol sections, and the
    overhead of generating a module-body description for "two imports and
    nothing else" isn't worth the LLM cost.
    """
    total_lines = tree_root.end_point[0] + 1
    if total_lines <= 0:
        return None

    consumed: set[int] = set()
    for start, end in consumed_ranges:
        consumed.update(range(start, end + 1))
    noise: set[int] = set()
    for start, end in noise_ranges or ():
        noise.update(range(start, end + 1))

    lines = source.decode("utf-8", errors="replace").splitlines()
    residual_lines: list[str] = []
    # Track which line numbers landed in `residual_lines` so we can also
    # include adjacent imports/docstring lines back in if there's real
    # residual content nearby (for context). Currently we drop them
    # unconditionally — the agent gets the docstring via the file
    # `description:` field and doesn't need to re-see imports.
    for lineno in range(1, total_lines + 1):
        if lineno in consumed or lineno in noise:
            continue
        idx = lineno - 1
        if idx >= len(lines):
            continue
        line = lines[idx]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        residual_lines.append(line)

    if not residual_lines:
        return None

    body_text = "\n".join(residual_lines)
    # `signature` is a one-line summary: how many residual lines, what kinds
    # of statement they start with. Cheap to compute and gives the agent a
    # one-glance view of what's in there.
    first_real = residual_lines[0].strip()
    signature = (
        f"module-level code ({len(residual_lines)} statements): "
        + first_real[:100]
        + ("…" if len(first_real) > 100 else "")
    )
    return Symbol(
        qualified_name=f"{module_key}:__module__",
        kind="module",
        name="__module__",
        file_path=rel_file,
        signature=signature,
        docstring=None,
        body_text=body_text,
        body_normalized_hash=_hash(body_text),
        signature_hash=_hash(signature),
        start_line=1,
        end_line=total_lines,
        is_public=True,
    )


def extract_symbols(
    file_path: Path,
    source_root: Path | None = None,
    *,
    source_text: str | None = None,
) -> list[Symbol]:
    """Parse a Python file and return its top-level symbols.

    Captures four shapes:

      - `function`: module-level `def` (and async def).
      - `class`: module-level `class`, plus each `method` defined directly inside.
      - `constant`: module-level `NAME = value` (or `NAME: T = value`). Includes
        dunders like `__version__` and `__all__`, and simple framework
        instantiations like `app = FastAPI()`. Tuple-target and attribute-target
        assignments are skipped — their symbol names are ambiguous.
      - `module`: a single synthetic `__module__` symbol per file holding the
        residual module-level code that isn't captured by any of the above:
        imports, top-level `if` blocks (`if TYPE_CHECKING:`, `if __name__ == ...`),
        top-level expression statements (`setup(...)` calls in setup.py), and
        decorator lines. This is the "what does the file *do* at import time"
        view that agents need but the per-symbol view drops.

    `source_root` controls the qualified_name prefix and the stored file_path. If None,
    defaults to the file's parent directory.

    `source_text`, when provided, overrides reading from disk. Used by diff-aware
    regeneration to parse a previous version of the file (retrieved from a git blob)
    while still attributing symbols to the current file path. The qualified names
    therefore match what the current symbol table would produce, which is exactly
    what we need to look up "previous body of this same symbol."
    """
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = source_text.encode("utf-8") if source_text is not None else file_path.read_bytes()
    tree = _make_parser().parse(source)
    module_key = _module_key(file_path, source_root)
    rel_file = str(file_path.relative_to(source_root))

    symbols: list[Symbol] = []
    # Two range lists:
    # - `consumed_ranges` tracks lines claimed by extracted symbols (functions,
    #   classes/methods, constants). Used as the basis for the `__module__`
    #   residual.
    # - `noise_ranges` additionally tracks lines that are real module-level
    #   syntax but carry no operational behaviour worth a separate symbol:
    #   imports and the module docstring. These are subtracted from the
    #   residual to avoid emitting a `__module__` symbol whose entire body
    #   is `from x import y` lines.
    consumed_ranges: list[tuple[int, int]] = []
    noise_ranges: list[tuple[int, int]] = []
    first_statement = True  # only the very first statement can be the module docstring
    for child in tree.root_node.named_children:
        top_decorators = _extract_decorators(child, source)
        target = _undecorate(child)
        is_doc_or_import = False
        if target.type == "function_definition":
            symbols.append(
                _build_symbol(
                    target,
                    source,
                    module_key=module_key,
                    rel_file=rel_file,
                    parent=None,
                    kind="function",
                    decorators=top_decorators,
                )
            )
            consumed_ranges.append((child.start_point[0] + 1, child.end_point[0] + 1))
        elif target.type == "class_definition":
            class_symbols = _walk_class(
                target,
                source,
                module_key=module_key,
                rel_file=rel_file,
                class_decorators=top_decorators,
            )
            symbols.extend(class_symbols)
            consumed_ranges.append((child.start_point[0] + 1, child.end_point[0] + 1))
        elif target.type in ("import_statement", "import_from_statement"):
            # Imports aren't a meaningful symbol on their own. Tag the line
            # as noise so it doesn't make the residual body look non-empty.
            is_doc_or_import = True
            noise_ranges.append((child.start_point[0] + 1, child.end_point[0] + 1))
        else:
            # Module docstring: PEP 257 says the very first statement, if it's
            # a bare string expression, is the module docstring. We tag it as
            # noise here so it doesn't end up in the `__module__` body — the
            # docstring already feeds the file-level `description:` field.
            if (
                first_statement
                and target.type == "expression_statement"
                and target.named_child_count > 0
                and target.named_children[0].type == "string"
            ):
                is_doc_or_import = True
                noise_ranges.append((child.start_point[0] + 1, child.end_point[0] + 1))
            else:
                # Try to interpret `child` as a module-level constant
                # assignment. If so, emit `kind='constant'`. If not, the line
                # range stays unclaimed and the residual goes into the
                # `__module__` symbol below.
                const_match = _module_level_constant(child, source)
                if const_match is not None:
                    assignment_node, target_name = const_match
                    symbols.append(
                        _build_constant_symbol(
                            child,
                            assignment_node,
                            target_name,
                            source,
                            module_key=module_key,
                            rel_file=rel_file,
                        )
                    )
                    consumed_ranges.append((child.start_point[0] + 1, child.end_point[0] + 1))
        if not is_doc_or_import:
            # After the first real (non-docstring, non-import) statement, the
            # "first statement could be the module docstring" window closes.
            first_statement = False

    # Deduplicate by qualified_name. typing.@overload creates multiple defs with the
    # same name, and @property + @x.setter does too. Python requires the actual
    # implementation/getter to come last in source order, so last-wins picks the
    # symbol whose body is the one users actually call.
    deduped: dict[str, Symbol] = {}
    for sym in symbols:
        deduped[sym.qualified_name] = sym
    # Sort by start_line so the result list is in source order regardless of dict
    # insertion order (which can be disrupted by the last-wins dedup above).
    result = sorted(deduped.values(), key=lambda s: s.start_line)

    # Module-body symbol: everything *not* claimed by a function/class/constant
    # extraction above AND not just imports / the module docstring (which are
    # `noise_ranges`). Computed after dedup so the consumed_ranges from
    # overload/setter dedup pairs only count once.
    module_sym = _build_module_body_symbol(
        tree.root_node,
        source,
        module_key=module_key,
        rel_file=rel_file,
        consumed_ranges=consumed_ranges,
        noise_ranges=noise_ranges,
    )
    if module_sym is not None:
        result.append(module_sym)
    return result


class PythonBackend:
    """The reference `LanguageBackend` for Python.

    Two-pass reference extraction: tree-sitter (`references.extract_file_data`)
    does the fast structural pass — symbols, imports, containment, class bases,
    and module-level/import-resolved call edges — then the paired
    `ReferenceResolver` (a `LspResolver` driving pyright/basedpyright)
    supplements it with the type-dependent method dispatch edges tree-sitter
    can't derive (`obj.method()`, `self.helper()`). The two edge sets are merged
    with `merge_references` (dedup + strongest-kind wins). The resolver is
    optional and cached per backend instance; if no Python language server is
    installed the backend degrades to tree-sitter-only extraction.
    """

    name = "python"
    extensions = (".py",)

    def __init__(self) -> None:
        self._resolver = None
        self._resolver_built = False

    def extract_file_data(self, file_path, source_root=None, *, source_text=None):
        # references.py imports python.py at module load, so import lazily here
        # to avoid a circular import at definition time.
        from pathlib import Path

        from trie.parse.references import extract_file_data
        from trie.parse.resolver import merge_references

        if source_text is not None:
            raise NotImplementedError("source_text override is not supported for extract_file_data")

        file_data = extract_file_data(file_path, source_root=source_root)

        resolver = self.resolver()
        if resolver is None:
            return file_data

        abs_path = Path(file_path).resolve()
        root = (Path(source_root) if source_root is not None else abs_path.parent).resolve()
        extra = resolver.resolve_file(abs_path, root, file_data.symbols)
        if not extra:
            return file_data

        from trie.parse.types import FileData

        merged = merge_references(file_data.references, extra)
        return FileData(symbols=file_data.symbols, references=merged)

    def resolver(self):
        """Return the cached LSP resolver, or None if disabled/unavailable.

        Set `TRIE_DISABLE_RESOLVER=1` to force tree-sitter-only extraction
        (used by tests that assert on tree-sitter's edge set, and as a debug
        escape hatch). If no Python language server (pyright / basedpyright) is
        on PATH, the backend silently degrades to tree-sitter-only.
        """
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import python_spec

                spec = python_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver

    def extract_symbols(self, file_path, source_root=None, *, source_text=None):
        return extract_symbols(file_path, source_root=source_root, source_text=source_text)

    def source_suffix(self) -> str:
        return ".py"

    def system_prompt(self) -> str:
        from trie.sync.generator import SYSTEM_PROMPT

        return SYSTEM_PROMPT
