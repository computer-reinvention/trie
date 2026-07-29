"""The reference-resolver contract — tree-sitter's type-aware supplement.

Tree-sitter resolves references by *syntactic name-binding*: it matches used
names against import tables and file-local top-level symbols. That resolves
module-level calls (`foo()`, `pkg.foo()`) but has no type information, so it
drops every method call through a value — `obj.method()`, `self.helper()`. A
benchmark on trie itself showed tree-sitter resolves **zero** method-target
call edges; a type-aware resolver (jedi) recovered ~500 real edges it missed.

A `ReferenceResolver` is the pluggable type-aware pass that fills that gap. It
runs *after* tree-sitter's structural extraction, sees the symbols tree-sitter
found, and returns the extra call edges it can prove — typically instance /
`self` / inherited method dispatch. The two passes are complementary: the
benchmark measured **zero overlap** between tree-sitter's edges and the
resolver's, so merging is pure gain.

Design contract for a new language = pair a tree-sitter backend with a
resolver (or `None`):

  - The resolver is *supplemental*: it never has to reproduce tree-sitter's
    edges, only add the ones tree-sitter can't resolve. If a language has no
    resolver, the backend returns `None` and behaviour is exactly today's
    tree-sitter-only extraction.
  - The resolver over-approximates freely. It emits candidate `Reference`s
    whose `target_qname` may or may not be a real project symbol; the store's
    existence filter (`Store.replace_all_edges`) drops any edge whose target
    isn't in the symbols table, so stdlib / third-party / dynamic misfires
    vanish downstream. The resolver must NOT invent qnames in a format the
    backend wouldn't emit for a real symbol.
  - The resolver must be robust: on a parse/analysis error for one file it
    returns `[]` rather than raising, so a single bad file never fails a scan.
"""

from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from trie.parse.types import Reference, Symbol

# Edge-kind precedence (strongest wins) — shared by tree-sitter extraction and
# resolver merging so a resolver-supplied `calls` never gets clobbered by a
# weaker `references`, and vice-versa. Kept in sync with the ranking documented
# in trie/parse/references.py.
KIND_RANK: dict[str, int] = {
    "imports": 0,
    "references": 1,
    "calls": 2,
    "inherits": 3,
    "implements": 3,
    "contains": 3,
}


@runtime_checkable
class ReferenceResolver(Protocol):
    """Type-aware reference resolver paired with a tree-sitter backend.

    Stateless from the engine's point of view; a resolver may cache a language
    server / analysis project keyed by `source_root` internally, but the engine
    treats each `resolve_file` call as independent.
    """

    #: Human/config name, e.g. "jedi", "pyright-lsp". Used in telemetry.
    name: str

    def resolve_file(
        self,
        file_path: Path,
        source_root: Path,
        symbols: list[Symbol],
    ) -> list[Reference]:
        """Return the extra call/reference edges tree-sitter could not resolve.

        - `file_path`: absolute path to the source file being resolved.
        - `source_root`: project source root; target qnames are computed
          relative to this, matching the backend's `extract_symbols` output.
        - `symbols`: the symbols tree-sitter already extracted for this file,
          so the resolver can attribute each edge to its enclosing symbol
          (`src_qname`) without re-parsing structure.

        Returns candidate `Reference`s. May over-approximate; must never raise
        for a single-file failure (return `[]` instead).
        """
        ...


def merge_references(
    base: list[Reference],
    extra: list[Reference],
) -> list[Reference]:
    """Merge resolver-supplied edges into tree-sitter's, deduping by (src, dst).

    Preserves the strongest edge kind per (src, target) pair using `KIND_RANK`,
    drops self-edges, and keeps `base` ordering with `extra` appended for any
    genuinely new pairs. This is the same dedup/upgrade policy tree-sitter uses
    internally, lifted here so the resolver pass composes identically.
    """
    edge_index: dict[tuple[str, str], int] = {}
    merged: list[Reference] = []

    def add(ref: Reference) -> None:
        if ref.target_qname == ref.src_qname:
            return
        key = (ref.src_qname, ref.target_qname)
        existing = edge_index.get(key)
        if existing is None:
            edge_index[key] = len(merged)
            merged.append(ref)
            return
        cur = merged[existing]
        if KIND_RANK.get(ref.kind, 0) > KIND_RANK.get(cur.kind, 0):
            merged[existing] = ref

    for ref in base:
        add(ref)
    for ref in extra:
        add(ref)
    return merged


__all__ = ["KIND_RANK", "ReferenceResolver", "merge_references"]
