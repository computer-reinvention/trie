"""The hand-off contract: the staged change-set and the ApplyReport.

`StagedChangeSet` is the ephemeral, one-cycle, in-memory object `stage` produces
and `commit` consumes (it is NOT persisted across turns). `ApplyReport` is what
the agent reads back — it must let the agent act on residue (`unresolved`) without
re-querying: every unresolved item carries a ready-to-send `repatch` call.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

_SESSION_NOTE_STOPLIST = {"update", "fix", "fixes", "changes", "change", "wip", ".", "edit"}
_SESSION_NOTE_MIN_CHARS = 12


def session_note_ok(note: str) -> bool:
    """A multi-symbol apply requires a real unifying intent, not boilerplate.

    Rejects empty / too-short / single-stoplist-word notes so the agent can't
    satisfy the gate with junk like "." or "fix".
    """
    n = (note or "").strip()
    if len(n) < _SESSION_NOTE_MIN_CHARS:
        return False
    return n.lower() not in _SESSION_NOTE_STOPLIST


# Stages a symbol can fail at, surfaced in UnresolvedItem.stage.
STAGE_GENERATE = "generate"
STAGE_COMPILE = "compile"
STAGE_FIXUP = "fixup"
STAGE_REFRESH = "refresh"
STAGE_CASCADE = "cascade"

# Enum codes (never joined strings) for UnresolvedItem.code.
CODE_BACKEND_FAILED = "backend_failed"
CODE_SYNTAX_AFTER_CAP = "syntax_error_after_retry_cap"
CODE_LSP_UNCLEAN = "lsp_unclean"
CODE_SECOND_ORDER = "second_order_cascade"
CODE_ORPHAN_CREATE = "orphan_create"
CODE_FILE_NOT_FOUND = "file_not_found"


@dataclass(frozen=True)
class StagedChange:
    """One symbol's proposed edit, fully generated and gated, awaiting commit.

    Carries the before-image (original full file bytes) so commit can restore on
    failure without a persistent journal.
    """

    qname: str
    op: str  # modify | create | delete | rename
    file_path: str  # source-root-relative
    old_source: str  # the symbol's prior span ("" for create)
    new_source: str  # the symbol's new span ("" for delete)
    new_prose: str
    before_file_bytes: str  # full original file content, for rollback
    after_file_bytes: str  # full proposed file content
    lsp_iterations: int = 0


@dataclass(frozen=True)
class UnresolvedItem:
    """A symbol needing the agent's attention. One-call recoverable via `repatch`.

    `blocking=True` means the pipeline could not produce a valid edit (generation
    or compile failure) — it blocks an all_or_nothing commit and makes the run not
    ok. `blocking=False` is advisory (e.g. a second-order cascade caller the agent
    may want to review) — it never blocks a commit or flips ok.
    """

    qname: str
    stage: str
    code: str
    message: str
    source_pointer: str = ""
    repatch: dict[str, Any] | None = None  # {"tool": ..., "args": {...}}
    blocking: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "qname": self.qname,
            "stage": self.stage,
            "code": self.code,
            "message": self.message,
            "source_pointer": self.source_pointer,
            "repatch": self.repatch,
            "blocking": self.blocking,
        }


@dataclass(frozen=True)
class AppliedItem:
    qname: str
    op: str
    file_path: str
    prose_written: bool = False
    lsp_iterations: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "qname": self.qname,
            "op": self.op,
            "file_path": self.file_path,
            "prose_written": self.prose_written,
            "lsp_iterations": self.lsp_iterations,
        }


@dataclass(frozen=True)
class CascadeAppliedItem:
    qname: str
    note: str
    origin: str = "cascade"

    def to_dict(self) -> dict[str, Any]:
        return {"qname": self.qname, "note": self.note, "origin": self.origin}


@dataclass
class ApplyReport:
    """The read-only feedback artifact returned by commit (and stage, dry)."""

    ok: bool = True
    session_note: str = ""
    committed: bool = False
    applied: list[AppliedItem] = field(default_factory=list)
    cascade_applied: list[CascadeAppliedItem] = field(default_factory=list)
    unresolved: list[UnresolvedItem] = field(default_factory=list)
    requested: int = 0
    error: str | None = None

    @property
    def blocking_unresolved(self) -> list[UnresolvedItem]:
        return [u for u in self.unresolved if u.blocking]

    def to_dict(self) -> dict[str, Any]:
        files = sorted({a.file_path for a in self.applied})
        return {
            "ok": self.ok,
            "session_note": self.session_note,
            "committed": self.committed,
            "applied": {
                "symbols": len(self.applied),
                "files": len(files),
                "files_detail": [a.to_dict() for a in self.applied],
            },
            "cascade_applied": [c.to_dict() for c in self.cascade_applied],
            "unresolved": [u.to_dict() for u in self.unresolved],
            "totals": {
                "requested": self.requested,
                "applied": len(self.applied),
                "unresolved": len(self.unresolved),
            },
            "error": self.error,
        }
