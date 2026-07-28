"""Jedi-backed reference resolver for Python — tree-sitter's type-aware pair.

Fills the gap tree-sitter leaves: method dispatch through a value. For every
attribute call `<expr>.<attr>(...)` in a file, jedi's static type inference is
asked where `<attr>` is defined (`goto`). When the definition lands inside the
project, the edge is attributed to the enclosing symbol and emitted as a
`calls` edge to the target symbol's qname.

Why jedi and not a language server (yet): jedi is in-process, already a project
dependency, needs no subprocess lifecycle or workspace warmup, and is
deterministic per file set. It is the concrete first implementation of the
`ReferenceResolver` seam; a generic LSP-client resolver can replace it per
language later without touching the extraction pipeline.

Robustness contract: any per-file analysis error yields `[]`, never an
exception — one unparseable file must not fail a scan.
"""

from __future__ import annotations

from pathlib import Path

from trie.parse.python import _make_parser, _node_text
from trie.parse.types import Reference, Symbol


class JediResolver:
    """`ReferenceResolver` using jedi static analysis for Python method calls."""

    name = "jedi"

    def __init__(self) -> None:
        # jedi is imported lazily so importing this module never hard-requires
        # jedi at definition time; a missing dep degrades to no resolver.
        self._parser = _make_parser()
        self._project = None  # jedi.Project, built per source_root on first use
        self._project_root: Path | None = None

    def _jedi(self):
        import jedi

        return jedi

    def _get_project(self, source_root: Path):
        jedi = self._jedi()
        root = source_root.resolve()
        if self._project is None or self._project_root != root:
            # Project root is the source root's parent so the top package
            # (e.g. `trie/`) is importable and cross-file goto resolves.
            self._project = jedi.Project(str(root.parent))
            self._project_root = root
        return self._project

    def resolve_file(
        self,
        file_path: Path,
        source_root: Path,
        symbols: list[Symbol],
    ) -> list[Reference]:
        try:
            return self._resolve_file_inner(file_path, source_root, symbols)
        except Exception:
            # Never fail a scan for one file. Telemetry can hook here later.
            return []

    def _resolve_file_inner(
        self,
        file_path: Path,
        source_root: Path,
        symbols: list[Symbol],
    ) -> list[Reference]:
        jedi = self._jedi()
        source = file_path.read_bytes()
        tree = self._parser.parse(source)

        # Line -> enclosing symbol qname (innermost def/class/method containing it),
        # for both the source file (attribute call site) and target resolution.
        own_by_line = _symbols_by_line(symbols)

        # A per-file index of target files' symbols is built lazily as jedi points
        # us at definitions; cache to avoid re-parsing a target file per hit.
        target_index: dict[Path, dict[int, str]] = {}

        def target_qname_for(def_path: Path, def_line: int) -> str | None:
            resolved = def_path.resolve()
            src_root = source_root.resolve()
            if not resolved.is_relative_to(src_root):
                return None  # stdlib / third-party — not a project edge
            idx = target_index.get(resolved)
            if idx is None:
                idx = _file_symbols_by_line(resolved, src_root)
                target_index[resolved] = idx
            return idx.get(def_line)

        project = self._get_project(source_root)
        script = jedi.Script(path=str(file_path), project=project)

        references: list[Reference] = []
        seen: set[tuple[str, str]] = set()

        for line, col, _attr in _attribute_call_sites(tree.root_node, source):
            src_qname = own_by_line.get(line)
            if src_qname is None:
                continue
            try:
                defs = script.goto(line, col + 1, follow_imports=True)
            except Exception:
                continue
            for d in defs:
                if d.module_path is None or d.line is None:
                    continue
                tgt = target_qname_for(Path(d.module_path), d.line)
                if tgt is None or tgt == src_qname:
                    continue
                key = (src_qname, tgt)
                if key in seen:
                    continue
                seen.add(key)
                references.append(Reference(src_qname=src_qname, target_qname=tgt, kind="calls"))
                break

        return references


def _symbols_by_line(symbols: list[Symbol]) -> dict[int, str]:
    """Map each line to the innermost def/class/method symbol covering it."""
    by_line: dict[int, str] = {}
    ordered = sorted(
        (s for s in symbols if s.kind in ("function", "method", "class")),
        key=lambda s: s.end_line - s.start_line,  # widest first, narrow overwrites
        reverse=True,
    )
    for s in ordered:
        for ln in range(s.start_line, s.end_line + 1):
            by_line[ln] = s.qualified_name
    return by_line


def _file_symbols_by_line(abs_path: Path, source_root: Path) -> dict[int, str]:
    """Parse a target file and map its symbols' start lines to their qnames.

    Keyed by *start line* because jedi's `goto` reports the definition's own
    line (the `def`/`class` line), which is a symbol's `start_line`.
    """
    from trie.parse import registry

    try:
        syms = registry.extract_symbols(abs_path, source_root=source_root)
    except Exception:
        return {}
    out: dict[int, str] = {}
    for s in syms:
        out[s.start_line] = s.qualified_name
    return out


def _attribute_call_sites(root, source: bytes):
    """Yield (line, col, attr_name) for every `<expr>.<attr>(...)` call.

    `line`/`col` are 1-indexed line, 0-indexed col of the attribute identifier —
    the position jedi's `goto` needs to resolve the called member.
    """
    out: list[tuple[int, int, str]] = []

    def walk(n) -> None:
        if n.type in ("comment", "string"):
            return
        if n.type == "call":
            fn = n.child_by_field_name("function")
            if fn is not None and fn.type == "attribute":
                attr_node = fn.child_by_field_name("attribute")
                if attr_node is not None and attr_node.type == "identifier":
                    out.append(
                        (
                            attr_node.start_point[0] + 1,
                            attr_node.start_point[1],
                            _node_text(attr_node, source),
                        )
                    )
        for c in n.children:
            walk(c)

    walk(root)
    return out


__all__ = ["JediResolver"]
