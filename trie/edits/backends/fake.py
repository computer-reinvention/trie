"""Deterministic edit backend for tests.

`FakeBackend` is the canonical way to exercise the apply pipeline without LLM or
opencode calls — and it proves the plug-and-play seam holds: if the full apply
passes against `FakeBackend`, nothing below the seam branches on the concrete
backend.

Modes let a test pick the per-symbol outcome deterministically:
  - "passthrough": echo old_source unchanged (no-op edit, always compiles if input did)
  - "append": append a marker comment line (a real, compiling change)
  - "broken": emit deliberately non-compiling source (exercises the compile gate)
  - "fail": return ok=False (exercises backend-level failure handling)
A per-qname override map takes precedence over the default mode.
"""

from __future__ import annotations

from .base import EditRequest, EditResult

_MARKER = "    # trie-fake-edit\n"


class FakeBackend:
    def __init__(
        self,
        mode: str = "passthrough",
        *,
        per_qname: dict[str, str] | None = None,
    ) -> None:
        self._mode = mode
        self._per_qname = per_qname or {}

    def generate(self, req: EditRequest) -> EditResult:
        mode = self._per_qname.get(req.qname, self._mode)

        if mode == "fail":
            return EditResult(req.qname, "", "", ok=False, error="fake backend failure")

        if mode == "broken":
            return EditResult(req.qname, "def (((broken", f"prose for {req.qname}", ok=True)

        # Create always synthesizes a valid def for the new symbol, regardless of
        # mode — there is no old_source to append to / pass through.
        if req.op == "create":
            name = req.qname.rsplit(":", 1)[-1]
            src = f"def {name}():\n    return None\n"
            return EditResult(req.qname, src, f"prose for {req.qname}", ok=True)

        if mode == "append":
            src = req.old_source
            if not src.endswith("\n"):
                src += "\n"
            src += _MARKER
            return EditResult(req.qname, src, f"prose for {req.qname}", ok=True)

        # passthrough
        return EditResult(req.qname, req.old_source, f"prose for {req.qname}", ok=True)
