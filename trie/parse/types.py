"""Language-neutral value types for the parse layer.

`Symbol`, `Reference`, and `FileData` are the contract every language backend
produces and every downstream consumer (graph store, sync, edits, agent
surface) operates on. They live here — not in `parse/python.py` — so a
non-Python backend can emit the same types without importing the Python
parser.

`KINDS` is the single source of truth for the symbol-kind vocabulary. Every
validator and doc that enumerates kinds imports it from here rather than
hardcoding a string list, so adding a kind is a one-line change.

`EDGE_KINDS` mirrors the relationship vocabulary for `Reference.kind` (the AGM
typed edges).
"""

from __future__ import annotations

from dataclasses import dataclass

# The canonical symbol-kind vocabulary. The first five are the original
# Python-era kinds; the rest were added for strongly-typed languages where a
# type declaration is itself a referenceable construct (TypeScript and beyond):
#   - interface / type / enum : top-level type declarations
#   - enum_member             : a member of an enum (child of the enum, like a method)
#   - property                : a class field / property signature (child of the class)
# A construct earns its own kind+symbol iff it can be an independent reference
# target in the graph. See docs/core/multi-language-backend-prd.md §4.
KINDS: tuple[str, ...] = (
    "function",
    "class",
    "method",
    "constant",
    "module",
    "interface",
    "type",
    "enum",
    "enum_member",
    "property",
)

# Relationship vocabulary for `Reference.kind` (typed edges in the graph).
EDGE_KINDS: tuple[str, ...] = (
    "calls",
    "references",
    "imports",
    "contains",
    "inherits",
    "implements",
)


@dataclass(frozen=True)
class Symbol:
    qualified_name: str
    kind: str  # one of KINDS
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
    parent_class: str | None = None  # set for methods/enum_member/property; the container's name
    decorators: tuple[str, ...] = ()  # decorator lines, e.g. ("@classmethod",)


@dataclass(frozen=True)
class Reference:
    """An outbound reference from a symbol within a file.

    `target_qname` is the resolved target's qualified name (e.g. `src/foo:bar`). It's a string
    so it can be persisted before the target's symbol_id is looked up in the DB.

    `kind` is the relationship type (AGM typed edges): one of `calls`, `references`,
    `imports`, `contains`, `inherits`, `implements`. The resolver assigns the most
    specific kind it can derive from the AST; ambiguous bare-identifier uses default
    to `references` and call-position uses to `calls`. `depends_on` from the AGM PRD
    is intentionally not produced — there is no AST construct for it.
    """

    src_qname: str
    target_qname: str
    kind: str = "calls"


@dataclass(frozen=True)
class FileData:
    """Symbols + outbound references extracted from one file in a single tree-sitter parse."""

    symbols: list[Symbol]
    references: list[Reference]
