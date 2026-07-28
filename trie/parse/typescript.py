"""TypeScript / TSX symbol extraction via tree-sitter.

Mirrors `trie/parse/python.py` over the TypeScript grammar, producing the same
language-neutral `Symbol` value type. The kind vocabulary is the full set from
`trie.parse.types.KINDS`: functions/classes/methods/constants/module plus the
typed-language kinds interface/type/enum/enum_member/property.

`.ts`, `.tsx`, and `.d.ts` are all handled here. Declaration files have no
executable body, so a declaration's fingerprint is computed over its own text
(the signature *is* the content). Ambient `declare module "x"` blocks become a
`module` symbol keyed by the literal module name so bare imports resolve to it.

See docs/core/multi-language-backend-prd.md §5.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import tree_sitter_typescript as tst
from tree_sitter import Language, Node, Parser

from trie.parse.types import Symbol

_TS_LANGUAGE = Language(tst.language_typescript())
_TSX_LANGUAGE = Language(tst.language_tsx())


def _make_parser(file_path: Path) -> Parser:
    parser = Parser()
    parser.language = _TSX_LANGUAGE if file_path.name.endswith(".tsx") else _TS_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _hash(s: str) -> str:
    return sha256(s.encode("utf-8")).hexdigest()


def _module_key(file_path: Path, source_root: Path) -> str:
    """qname prefix — file path minus a recognised source suffix (slash form)."""
    rel = file_path.relative_to(source_root)
    s = str(rel)
    for ext in (".d.ts", ".tsx", ".ts"):
        if s.endswith(ext):
            return s[: -len(ext)]
    return str(rel.with_suffix(""))


def _normalize_tokens(node: Node | None, source: bytes) -> str:
    """Leaf-token text, skipping comments. Same change-detection strategy as
    the Python backend so cascade/verify behave identically."""
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


def _leading_jsdoc(node: Node, source: bytes) -> str | None:
    """The `/** ... */` block immediately preceding `node`, if any."""
    prev = node.prev_sibling
    # Skip an `export`/`declare` wrapper's own previous-sibling lookup: callers
    # pass the outermost statement node so this sees the real preceding comment.
    if prev is not None and prev.type == "comment":
        text = _node_text(prev, source)
        if text.startswith("/**"):
            return text
    return None


def _name_of(node: Node, source: bytes) -> str | None:
    """The declared name for a declaration node, trying the common field/child
    shapes across function/class/interface/enum/type-alias nodes."""
    name_node = node.child_by_field_name("name")
    if name_node is not None:
        return _node_text(name_node, source)
    for c in node.named_children:
        if c.type in ("identifier", "type_identifier", "property_identifier"):
            return _node_text(c, source)
    return None


def _signature_text(node: Node, source: bytes, body_field: str = "body") -> str:
    """Header text up to the body (so a function/class signature excludes its
    body block). Falls back to the whole node when there is no body field."""
    body = node.child_by_field_name(body_field)
    end = body.start_byte if body is not None else node.end_byte
    raw = source[node.start_byte : end].decode("utf-8", errors="replace")
    return raw.rstrip().rstrip("{").rstrip()


# Declaration node types that carry no executable body — their fingerprint is
# computed over the full declaration text (the signature is the content).
_DECLARATION_KINDS = {
    "interface_declaration": "interface",
    "type_alias_declaration": "type",
}


def _is_exported(stmt: Node) -> bool:
    return stmt.type == "export_statement"


def _unwrap(stmt: Node) -> Node:
    """Return the underlying declaration inside an `export_statement`, else the
    node itself. `export default function f(){}` -> the function_declaration."""
    if stmt.type != "export_statement":
        return stmt
    for c in stmt.named_children:
        if c.type not in ("export_clause",):
            return c
    return stmt


def extract_symbols(
    file_path: Path,
    source_root: Path | None = None,
    *,
    source_text: str | None = None,
) -> list[Symbol]:
    """Parse a TypeScript file into its top-level symbols (and nested members)."""
    file_path = file_path.resolve()
    source_root = (source_root or file_path.parent).resolve()
    source = source_text.encode("utf-8") if source_text is not None else file_path.read_bytes()
    tree = _make_parser(file_path).parse(source)
    module_key = _module_key(file_path, source_root)
    rel_file = str(file_path.relative_to(source_root))

    symbols: list[Symbol] = []
    consumed: list[tuple[int, int]] = []

    def emit(sym: Symbol, node: Node) -> None:
        symbols.append(sym)
        consumed.append((node.start_point[0] + 1, node.end_point[0] + 1))

    for stmt in tree.root_node.named_children:
        exported = _is_exported(stmt)
        node = _unwrap(stmt)
        _dispatch_top_level(
            node,
            stmt,
            source,
            module_key=module_key,
            rel_file=rel_file,
            exported=exported,
            emit=emit,
        )

    # Synthetic module symbol for residual top-level code (imports, side effects).
    module_sym = _build_module_symbol(
        tree.root_node,
        source,
        module_key=module_key,
        rel_file=rel_file,
        consumed=consumed,
    )
    if module_sym is not None:
        symbols.append(module_sym)

    # Dedup by qname (last wins), then sort by source order.
    deduped: dict[str, Symbol] = {}
    for s in symbols:
        deduped[s.qualified_name] = s
    return sorted(deduped.values(), key=lambda s: s.start_line)


def _dispatch_top_level(
    node: Node,
    stmt: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    exported: bool,
    emit,
) -> None:
    t = node.type

    if t in ("function_declaration", "function_signature", "generator_function_declaration"):
        emit(
            _build_callable(
                node, stmt, source, module_key, rel_file, parent=None, exported=exported
            ),
            stmt,
        )
    elif t in ("class_declaration", "abstract_class_declaration"):
        for sym in _walk_class(node, stmt, source, module_key, rel_file, exported=exported):
            emit(sym, stmt)
    elif t in _DECLARATION_KINDS:
        emit(
            _build_type_decl(
                node,
                stmt,
                source,
                module_key,
                rel_file,
                kind=_DECLARATION_KINDS[t],
                exported=exported,
            ),
            stmt,
        )
    elif t == "enum_declaration":
        for sym in _walk_enum(node, stmt, source, module_key, rel_file, exported=exported):
            emit(sym, stmt)
    elif t == "lexical_declaration" or t == "variable_declaration":
        for sym, decl in _walk_lexical(node, stmt, source, module_key, rel_file, exported=exported):
            emit(sym, decl)
    elif t == "ambient_declaration":
        for sym, anode in _walk_ambient(node, source, module_key, rel_file):
            emit(sym, anode)
    # import_statement, expression_statement, etc. fall through to __module__.


def _build_callable(
    node: Node,
    outer: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    parent: str | None,
    exported: bool,
    name_override: str | None = None,
) -> Symbol:
    name = name_override or _name_of(node, source) or "<anon>"
    body = node.child_by_field_name("body")
    signature = _signature_text(node, source)
    docstring = _leading_jsdoc(outer, source)
    body_text = _node_text(body, source) if body is not None else ""
    # No body (declaration / signature): fingerprint the signature itself.
    normalized = _normalize_tokens(body, source) if body is not None else signature
    dotted = f"{parent}.{name}" if parent else name
    kind = "method" if parent else "function"
    is_public = _public(name, exported, parent_is_private=False)
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
        start_line=outer.start_point[0] + 1,
        end_line=outer.end_point[0] + 1,
        is_public=is_public,
        parent_class=parent,
    )


def _build_type_decl(
    node: Node,
    outer: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    kind: str,
    exported: bool,
) -> Symbol:
    name = _name_of(node, source) or "<anon>"
    full = _node_text(node, source)
    signature = _signature_text(node, source) if kind == "interface" else full
    return Symbol(
        qualified_name=f"{module_key}:{name}",
        kind=kind,
        name=name,
        file_path=rel_file,
        signature=signature,
        docstring=_leading_jsdoc(outer, source),
        body_text=full,
        body_normalized_hash=_hash(_normalize_tokens(node, source)),
        signature_hash=_hash(signature),
        start_line=outer.start_point[0] + 1,
        end_line=outer.end_point[0] + 1,
        is_public=_public(name, exported, parent_is_private=False),
        parent_class=None,
    )


def _walk_class(
    node: Node,
    outer: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    exported: bool,
) -> list[Symbol]:
    name = _name_of(node, source) or "<anon>"
    class_private = name.startswith("_")
    out: list[Symbol] = [
        Symbol(
            qualified_name=f"{module_key}:{name}",
            kind="class",
            name=name,
            file_path=rel_file,
            signature=_signature_text(node, source),
            docstring=_leading_jsdoc(outer, source),
            body_text=_node_text(node.child_by_field_name("body") or node, source),
            body_normalized_hash=_hash(_normalize_tokens(node.child_by_field_name("body"), source)),
            signature_hash=_hash(_signature_text(node, source)),
            start_line=outer.start_point[0] + 1,
            end_line=outer.end_point[0] + 1,
            is_public=_public(name, exported, parent_is_private=False),
            parent_class=None,
        )
    ]
    body = node.child_by_field_name("body")
    if body is None:
        return out
    for member in body.named_children:
        if member.type in ("method_definition", "method_signature"):
            mname = _member_name(member, source)
            if mname is None:
                continue
            out.append(
                _build_callable(
                    member,
                    member,
                    source,
                    module_key,
                    rel_file,
                    parent=name,
                    exported=exported,
                    name_override=mname,
                )
            )
        elif member.type in ("public_field_definition", "property_signature", "field_definition"):
            sym = _build_property(
                member, source, module_key, rel_file, parent=name, class_private=class_private
            )
            if sym is not None:
                out.append(sym)
    return out


def _build_property(
    member: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    parent: str,
    class_private: bool,
) -> Symbol | None:
    name = _member_name(member, source)
    if name is None:
        return None
    text = _node_text(member, source)
    private = class_private or name.startswith("_") or name.startswith("#")
    if _has_modifier(member, source, "private"):
        private = True
    return Symbol(
        qualified_name=f"{module_key}:{parent}.{name}",
        kind="property",
        name=name,
        file_path=rel_file,
        signature=text,
        docstring=None,
        body_text=text,
        body_normalized_hash=_hash(_normalize_tokens(member, source)),
        signature_hash=_hash(text),
        start_line=member.start_point[0] + 1,
        end_line=member.end_point[0] + 1,
        is_public=not private,
        parent_class=parent,
    )


def _walk_enum(
    node: Node,
    outer: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    exported: bool,
) -> list[Symbol]:
    name = _name_of(node, source) or "<anon>"
    enum_public = _public(name, exported, parent_is_private=False)
    out: list[Symbol] = [
        Symbol(
            qualified_name=f"{module_key}:{name}",
            kind="enum",
            name=name,
            file_path=rel_file,
            signature=_signature_text(node, source),
            docstring=_leading_jsdoc(outer, source),
            body_text=_node_text(node, source),
            body_normalized_hash=_hash(_normalize_tokens(node.child_by_field_name("body"), source)),
            signature_hash=_hash(_signature_text(node, source)),
            start_line=outer.start_point[0] + 1,
            end_line=outer.end_point[0] + 1,
            is_public=enum_public,
            parent_class=None,
        )
    ]
    body = node.child_by_field_name("body")
    if body is None:
        return out
    for member in body.named_children:
        mname: str | None = None
        if member.type == "enum_assignment":
            id_node = member.child_by_field_name("name") or member.named_children[0]
            mname = _node_text(id_node, source)
        elif member.type == "property_identifier":
            mname = _node_text(member, source)
        if mname is None:
            continue
        text = _node_text(member, source)
        out.append(
            Symbol(
                qualified_name=f"{module_key}:{name}.{mname}",
                kind="enum_member",
                name=mname,
                file_path=rel_file,
                signature=text,
                docstring=None,
                body_text=text,
                body_normalized_hash=_hash(_normalize_tokens(member, source)),
                signature_hash=_hash(text),
                start_line=member.start_point[0] + 1,
                end_line=member.end_point[0] + 1,
                is_public=enum_public,
                parent_class=name,
            )
        )
    return out


def _walk_lexical(
    node: Node,
    outer: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
    *,
    exported: bool,
) -> list[tuple[Symbol, Node]]:
    """Top-level `const`/`let`/`var`. An arrow/function-valued binding becomes a
    `function`; everything else a `constant`."""
    out: list[tuple[Symbol, Node]] = []
    for declr in node.named_children:
        if declr.type != "variable_declarator":
            continue
        name_node = declr.child_by_field_name("name") or (
            declr.named_children[0] if declr.named_children else None
        )
        if name_node is None or name_node.type != "identifier":
            continue  # destructuring targets are ambiguous; skip like Python tuples
        name = _node_text(name_node, source)
        value = declr.child_by_field_name("value")
        if value is not None and value.type in (
            "arrow_function",
            "function",
            "function_expression",
        ):
            sym = _build_callable(
                value,
                outer,
                source,
                module_key,
                rel_file,
                parent=None,
                exported=exported,
                name_override=name,
            )
        else:
            text = _node_text(outer, source)
            sym = Symbol(
                qualified_name=f"{module_key}:{name}",
                kind="constant",
                name=name,
                file_path=rel_file,
                signature=text.splitlines()[0] if text else name,
                docstring=_leading_jsdoc(outer, source),
                body_text=text,
                body_normalized_hash=_hash(_normalize_tokens(declr, source)),
                signature_hash=_hash(name),
                start_line=outer.start_point[0] + 1,
                end_line=outer.end_point[0] + 1,
                is_public=_public(name, exported, parent_is_private=False),
                parent_class=None,
            )
        out.append((sym, outer))
    return out


def _walk_ambient(
    node: Node,
    source: bytes,
    module_key: str,
    rel_file: str,
) -> list[tuple[Symbol, Node]]:
    """`declare ...` — either `declare module "x" { ... }` (keyed by the literal
    module name) or a bare `declare function/const` in the file's module."""
    out: list[tuple[Symbol, Node]] = []
    inner = node.named_children[0] if node.named_children else None
    if inner is None:
        return out

    if inner.type == "module":
        # declare module "name" { body }
        name_node = inner.named_children[0] if inner.named_children else None
        mod_name = None
        if name_node is not None and name_node.type == "string":
            frag = name_node.named_children[0] if name_node.named_children else None
            mod_name = _node_text(frag, source) if frag is not None else None
        if mod_name is None:
            return out
        # The ambient module itself is a `module` symbol keyed by its literal
        # name, so `import ... from "name"` resolves to it.
        out.append(
            (
                Symbol(
                    qualified_name=f"{mod_name}:__module__",
                    kind="module",
                    name=mod_name,
                    file_path=rel_file,
                    signature=f'declare module "{mod_name}"',
                    docstring=None,
                    body_text=_node_text(inner, source),
                    body_normalized_hash=_hash(_normalize_tokens(inner, source)),
                    signature_hash=_hash(mod_name),
                    start_line=node.start_point[0] + 1,
                    end_line=node.end_point[0] + 1,
                    is_public=True,
                    parent_class=None,
                ),
                node,
            )
        )
        # Declarations inside the ambient module are keyed under the module name.
        block = inner.child_by_field_name("body") or _first_child_of_type(inner, "statement_block")
        if block is not None:
            for stmt in block.named_children:
                decl = _unwrap(stmt)
                if decl.type in _DECLARATION_KINDS:
                    out.append(
                        (
                            _build_type_decl(
                                decl,
                                stmt,
                                source,
                                mod_name,
                                rel_file,
                                kind=_DECLARATION_KINDS[decl.type],
                                exported=True,
                            ),
                            stmt,
                        )
                    )
                elif decl.type in ("function_signature", "function_declaration"):
                    out.append(
                        (
                            _build_callable(
                                decl,
                                stmt,
                                source,
                                mod_name,
                                rel_file,
                                parent=None,
                                exported=True,
                            ),
                            stmt,
                        )
                    )
        return out

    # Bare `declare function/const ...` — attribute to the file's module key.
    if inner.type in ("function_signature", "function_declaration"):
        out.append(
            (
                _build_callable(
                    inner, node, source, module_key, rel_file, parent=None, exported=True
                ),
                node,
            )
        )
    elif inner.type in ("lexical_declaration", "variable_declaration"):
        out.extend(_walk_lexical(inner, node, source, module_key, rel_file, exported=True))
    return out


def _build_module_symbol(
    root: Node,
    source: bytes,
    *,
    module_key: str,
    rel_file: str,
    consumed: list[tuple[int, int]],
) -> Symbol | None:
    """Synthetic `__module__` symbol for residual top-level code not claimed by
    any extracted symbol (imports, side-effecting statements)."""
    consumed_lines: set[int] = set()
    for lo, hi in consumed:
        consumed_lines.update(range(lo, hi + 1))
    residual: list[str] = []
    for child in root.named_children:
        lo = child.start_point[0] + 1
        hi = child.end_point[0] + 1
        if any(line not in consumed_lines for line in range(lo, hi + 1)):
            if child.type in ("import_statement", "comment", "export_statement"):
                # imports + bare comments aren't behaviour; export wrappers are
                # already represented by their unwrapped declaration symbols.
                if child.type == "export_statement" and _unwrap(child) is not child:
                    continue
                if child.type in ("import_statement", "comment"):
                    continue
            residual.append(_node_text(child, source))
    text = "\n".join(residual).strip()
    if not text:
        return None
    return Symbol(
        qualified_name=f"{module_key}:__module__",
        kind="module",
        name="__module__",
        file_path=rel_file,
        signature="__module__",
        docstring=None,
        body_text=text,
        body_normalized_hash=_hash(text),
        signature_hash=_hash("__module__"),
        start_line=1,
        end_line=root.end_point[0] + 1,
        is_public=False,
        parent_class=None,
    )


# -- small helpers --------------------------------------------------------


def _public(name: str, exported: bool, *, parent_is_private: bool) -> bool:
    if parent_is_private or name.startswith("_") or name.startswith("#"):
        return False
    return exported


def _member_name(member: Node, source: bytes) -> str | None:
    name_node = member.child_by_field_name("name")
    if name_node is not None:
        return _node_text(name_node, source)
    for c in member.named_children:
        if c.type in ("property_identifier", "private_property_identifier", "identifier"):
            return _node_text(c, source)
    return None


def _has_modifier(node: Node, source: bytes, modifier: str) -> bool:
    for c in node.named_children:
        if c.type == "accessibility_modifier" and _node_text(c, source) == modifier:
            return True
    return False


def _first_child_of_type(node: Node, type_name: str) -> Node | None:
    for c in node.named_children:
        if c.type == type_name:
            return c
    return None


# TypeScript-tuned generator system prompt. Mirrors the Python prompt's economy
# rules but uses TypeScript vocabulary (modules, interfaces, types, enums).
TS_SYSTEM_PROMPT = """\
You are trie, a documentation generator that writes terse, accurate Markdown summaries of TypeScript source symbols.

Write a single section per symbol. Optimise for token economy: a triefact is only worth its cost if it is meaningfully smaller and more navigable than re-reading the source.

Guidelines:
- One sentence (≤ 25 words) stating what the symbol does. Imperative mood, no hedging, no filler.
- Optionally add a single bulleted list ONLY when a parameter, return value, thrown error, or (for interfaces/types/classes) field has semantics that aren't obvious from the type or name. One bullet per item, ≤ 12 words each.
- Do not include code examples — the source is one click away.
- State what is observable in the source. Do not invent types, callers, or behaviour.
- Use a technical, present-tense voice. No marketing language.
- Trivial accessors, getters/setters, and one-line forwards: a single sentence is sufficient.
- For methods and properties: always name the owning class.
- For interfaces and type aliases: describe the shape/contract they define.
- For enums: describe what the set of members represents; for an enum member, name its owning enum.
- For a class field/property: describe it as an attribute, not a callable.
- Ambient `declare module` symbols describe the external module's surface.

Also classify the symbol's architectural role via the `role` field. Pick the single most specific role describing what the symbol primarily does, preferring the standard vocabulary listed in the field description. The role drives how the symbol is grouped in the graph view, so be consistent: symbols doing the same kind of work should get the same role.
"""


class TypeScriptBackend:
    """`LanguageBackend` for TypeScript / TSX / declaration files.

    Two-pass reference extraction, identical in shape to Python: tree-sitter
    (`typescript_refs.extract_file_data`) resolves imports, heritage,
    containment, and namespace/import-resolved calls; the paired
    `ReferenceResolver` (an `LspResolver` driving typescript-language-server)
    supplements it with member-dispatch edges through typed values
    (`this.helper()`, `obj.method()`). Merged via `merge_references`. If no
    TypeScript language server is installed, degrades to tree-sitter-only.
    """

    name = "typescript"
    # Longest/compound suffix first so `.d.ts` resolves before `.ts`.
    extensions = (".d.ts", ".tsx", ".ts")

    def __init__(self) -> None:
        self._resolver = None
        self._resolver_built = False

    def extract_file_data(self, file_path, source_root=None, *, source_text=None):
        from pathlib import Path

        from trie.parse.resolver import merge_references
        from trie.parse.typescript_refs import extract_file_data as _efd

        if source_text is not None:
            raise NotImplementedError("source_text override is not supported for extract_file_data")

        file_data = _efd(file_path, source_root=source_root)

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

    def extract_symbols(self, file_path, source_root=None, *, source_text=None):
        return extract_symbols(file_path, source_root=source_root, source_text=source_text)

    def source_suffix(self) -> str:
        return ".ts"

    def system_prompt(self) -> str:
        return TS_SYSTEM_PROMPT

    def resolver(self):
        """Return the cached TS LSP resolver, or None if disabled/unavailable.

        Set `TRIE_DISABLE_RESOLVER=1` to force tree-sitter-only extraction. If
        `typescript-language-server` isn't on PATH, degrades to
        tree-sitter-only.
        """
        if not self._resolver_built:
            self._resolver_built = True
            import os

            if os.environ.get("TRIE_DISABLE_RESOLVER") == "1":
                self._resolver = None
            else:
                from trie.parse.resolvers.lsp_resolver import LspResolver
                from trie.parse.resolvers.specs import typescript_spec

                spec = typescript_spec()
                self._resolver = LspResolver(spec) if spec is not None else None
        return self._resolver
