"""MCP server exposing the trie triefact tree + symbol graph to coding agents.

Read-only. Speaks MCP over stdio so an agent harness (Claude Code, Codex, etc.) can spawn
it as a subprocess and consult the triefact tree as context separate from its own
conversation memory.

## Core tools (basis-vector set)

Three verbs match the cognitive moves an agent makes when navigating an unfamiliar
codebase:

- `grep(predicate, rank_by?, limit=10)` — find symbols matching a predicate.
- `read(qname)` — read one symbol's prose plus the one-liners of its immediate
  neighbours (callers + callees).
- `trace(from_qname, direction, depth=2)` — trace the graph topology beyond one hop.

## Extended toolset (agent-ergonomic wrappers)

Eight additional tools wrap the core in shapes that match how agents already think:

- `grep_str(regexp)` — regex search across source bodies; hits attributed to symbols.
- `grep_entry_points(regexp)` — find architectural hubs whose prose matches a topic.
- `grep_symbol(sym)` — fuzzy symbol name lookup: best match + similar symbols.
- `grep_symbol_and_neighbours(sym)` — like grep_symbol but includes trimmed neighbour
  metadata for immediate callers + callees.
- `explain_symbol(sym)` — full prose + joined narrative story across references.
- `explain_symbol_references(sym)` — only explain how the symbol is *used* (callers side).
- `trace_flow(symbol1, symbol2)` — find call chain(s) between two symbols.
- `explain_flow(symbol1, symbol2)` — trace_flow + prose of each node joined as a story.

The same three core operations are also exposed as CLI subcommands (`trie grep`,
`trie read`, `trie trace`) so an agent that prefers shelling out can do
everything the MCP can without changing protocols. Both surfaces share
the same `TrieTools` methods underneath, so behaviour, knobs, and error
shapes are identical regardless of how the agent calls in.

Every response carries a `one_liner` on each symbol it mentions, pulled from the
section body at sync time and cached in `triefact_sections`. Errors return a
structured `{code, message, suggestion}` shape so an agent can recover with one
fewer round trip.

The agent never sees the underlying knobs: `Config.mcp` carries every default and
threshold the server enforces. See `docs/agent_interface.md` for the full contract.

Example agent wiring (Claude Code's mcp_servers config):

    {
      "trie": {
        "command": "trie",
        "args": ["mcp", "serve"],
        "cwd": "/path/to/project"
      }
    }
"""

from __future__ import annotations

import functools
import json
import re
import shutil
import subprocess
from collections import deque
from collections.abc import Callable
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from rapidfuzz import fuzz as _fuzz
from rapidfuzz import process as _process

from trie import telemetry
from trie.config import Config, Mcp
from trie.graph.store import GrepPredicate, Store, SymbolDetail
from trie.parse.types import KINDS
from trie.scope import discover_files


class RipgrepNotFoundError(RuntimeError):
    """Raised at MCP server startup when `rg` (ripgrep) is not on PATH.

    `grep`'s text-match fallback shells out to ripgrep for in-source-body
    searches. ripgrep gives us .gitignore-aware traversal, binary skip,
    smart-case, encoding detection, and parallel scanning for free — all
    of which a hand-rolled Python loop would have to re-implement badly.

    We fail at startup rather than at the first fallback call: a half-
    functional server (symbol-name `grep` works, fallback doesn't) would
    surprise agents at unpredictable moments. One clear failure surface
    is easier to debug.
    """


def _require_ripgrep() -> str:
    """Return the absolute path to `rg`, or raise `RipgrepNotFoundError`.

    Resolves via `shutil.which`, which honours PATH the same way the
    shell does. The result is what we pass to `subprocess.run` so the
    server doesn't have to re-resolve on every fallback call.
    """
    path = shutil.which("rg")
    if path is None:
        raise RipgrepNotFoundError(
            "trie's MCP server requires `rg` (ripgrep) on PATH. "
            "Install with `brew install ripgrep` on macOS, "
            "`apt install ripgrep` on Debian/Ubuntu, or see "
            "https://github.com/BurntSushi/ripgrep#installation."
        )
    return path


def _error(
    code: str,
    message: str,
    suggestion: str | None = None,
    *,
    fix: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build the canonical error envelope: `{error: {code, message, suggestion?, fix?}}`.

    Agents read these as authoritative — a `suggestion` is included whenever there
    is a concrete next step to recommend. `fix` is an executable, ready-to-replay
    tool call (`{tool, args}`) with the corrected argument pre-filled, so recovery
    is "resend `fix`" — one step, zero re-querying.
    """
    body: dict[str, Any] = {"code": code, "message": message}
    if suggestion is not None:
        body["suggestion"] = suggestion
    if fix is not None:
        body["fix"] = fix
    return {"error": body}


def _truncate(text: str, max_chars: int) -> str:
    """Truncate `text` to `max_chars`, suffixing an ellipsis when clipped. `0` = no cap."""
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "\u2026"


def _symbol_summary(detail: SymbolDetail, *, one_liner_max: int) -> dict[str, Any]:
    """Compact symbol record used inside neighbour / trace-node lists."""
    return {
        "qname": detail.qualified_name,
        "signature": detail.signature or "",
        "one_liner": _truncate(detail.one_liner, one_liner_max),
    }


_URL_SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*://")
_WIN_DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")


def _looks_like_qname(s: str) -> bool:
    """True when `s` has the shape of a trie qname (`path/to/file:Name`).

    A qname contains a `:` but is not a URL (`scheme://...`) and not a Windows
    drive prefix (`C:\\`). Mirrors `looksLikeQname` in the opencode fork so the
    qname-vs-file-path dispatch is identical across surfaces. Note: a `:`-bearing
    string can still resolve to a real file (e.g. a `file:LINE` cursor ref); the
    caller probes the filesystem before committing to the graph.
    """
    if ":" not in s:
        return False
    if _URL_SCHEME_RE.match(s):
        return False
    return not _WIN_DRIVE_RE.match(s)


def _close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]:
    """Fuzzy-match `qname` against the known set. Used for `not_found` suggestions.

    Same-module candidates lead: a missed qname almost always names the right
    file with the wrong local symbol (the classic `mod:__module__` guess for
    what is actually `mod:__version__`), so symbols from the same module are
    scored on local name alone and ranked ahead of global qname matches.
    """
    module, sep, local = qname.partition(":")
    ranked: list[str] = []
    if sep and local:
        same_module = [c for c in candidates if c.startswith(module + ":")]
        local_names = {c: c.split(":", 1)[1] for c in same_module}
        hits = _process.extract(
            local, list(local_names.values()), scorer=_fuzz.WRatio, limit=n, score_cutoff=30
        )
        # Preserve the fuzzy-score order (best first), not the candidate-list
        # order — the closest correction must lead the suggestion line.
        rank_of = {name: i for i, (name, _score, _idx) in enumerate(hits)}
        matched = [c for c in same_module if local_names[c] in rank_of]
        ranked = sorted(matched, key=lambda c: rank_of[local_names[c]])
    global_hits = _process.extract(qname, candidates, scorer=_fuzz.WRatio, limit=n, score_cutoff=45)
    for h in global_hits:
        if h[0] not in ranked:
            ranked.append(h[0])
    return ranked[:n]


def _close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]:
    hits = _process.extract(name, candidates, scorer=_fuzz.WRatio, limit=n, score_cutoff=45)
    return [h[0] for h in hits]


def _fuzzy_score(query: str, text: str) -> float:
    """Return a 0-100 graded relevance score for `query` against `text`.

    Grades, highest first — replacing the old unconditional substring→100.0
    shortcut, which made every symbol whose name merely *contained* the query
    tie at a perfect score (so `write_stamp` scored identically to
    `test_write_stamp_is_atomic_no_partial_files_left_behind`, and the winner
    was decided by ASCII order of qnames — tests beat production symbols):

      - exact match (case-insensitive)      → 100.0
      - prefix match (`query…`)             → 92.0
      - substring match                     → 70.0 + up to 20.0 by coverage
                                              (len(query)/len(text): tighter
                                              containers score higher)
      - otherwise                           → rapidfuzz WRatio

    A query still always beats WRatio noise when it literally appears in the
    text, but containment no longer masquerades as equality.
    """
    if not text:
        return 0.0
    q, t = query.lower(), text.lower()
    if q == t:
        return 100.0
    if t.startswith(q):
        return 92.0
    if q in t:
        return 70.0 + 20.0 * (len(q) / len(t))
    return float(_fuzz.WRatio(query, text))


def _is_test_symbol(sym: SymbolDetail) -> bool:
    """Heuristic: does this symbol live in test code?

    Path-based (`tests/` root, nested `/tests/` dirs, `test_*.py` /
    `conftest.py` files) — there is no structural is_test flag in the graph.
    Used only to *deprioritize* tests in fuzzy ranking and to exclude them
    from entry-point candidacy; explicit predicates (`scope_prefix` etc.) are
    unaffected, and tests remain fully indexed and searchable.
    """
    fp = sym.file_path or ""
    if fp.startswith("tests/") or "/tests/" in fp:
        return True
    base = fp.rsplit("/", 1)[-1]
    return base.startswith("test_") or base == "conftest.py"


_TEST_SCORE_FACTOR = 0.85
"""Multiplicative penalty applied to test symbols' fuzzy scores.

Strong enough that an equally-good production symbol always outranks a test;
weak enough that a test still surfaces when it is genuinely the best match
(e.g. the query names the test itself)."""


def _score_sym(
    query: str,
    sym: SymbolDetail,
    *,
    prose: str = "",
    prose_weight: float = 0.6,
) -> float:
    """Composite relevance score for `sym` against `query` (0-100).

    Scoring layers, highest wins:
      1. Local symbol name          — weight 1.0  (most precise signal)
      2. Cached one_liner           — weight 0.8  (free DB column)
      3. Triefact prose body        — weight `prose_weight` (default 0.6; caller controls
                                       whether to supply prose to keep disk reads lazy)

    Taking the max rather than averaging means a strong name match isn't dragged down
    by a weak prose match, and a prose-only match is always slightly discounted relative
    to an equally-strong name match.

    Test symbols (see `_is_test_symbol`) are multiplied by `_TEST_SCORE_FACTOR`
    so production code wins ties everywhere this score is used — search results
    were drowning in same-named test functions before this penalty existed.
    """
    local_name = (
        sym.qualified_name.split(":")[-1] if ":" in sym.qualified_name else sym.qualified_name
    )
    name_score = _fuzzy_score(query, local_name)
    liner_score = _fuzzy_score(query, sym.one_liner or "") * 0.8
    prose_score = _fuzzy_score(query, prose[:2000]) * prose_weight if prose else 0.0
    score = max(name_score, liner_score, prose_score)
    if _is_test_symbol(sym):
        score *= _TEST_SCORE_FACTOR
    return score


def _predicate_is_empty(pred: GrepPredicate) -> bool:
    """True when `pred` carries no filter that would narrow the result set.

    Mirrors the SQL builder's notion of "this field is unset": a falsy
    `name_contains` (None or empty string), no `kind` or `kind == "any"`,
    no `scope_prefix`, no `scope_exclude`, `public_only` False, and no
    inbound/outbound bounds. An empty predicate against a populated graph
    would otherwise hit the un-WHERE'd `SELECT ... FROM symbols ORDER BY
    is_public DESC, qualified_name LIMIT N` path, which returns the
    alphabetically-first public symbols — useful to nobody and easy to
    misread as relevance. The caller rejects with an invalid_argument
    envelope so the agent gets a clear next step instead.
    """
    return (
        not pred.name_contains
        and (pred.kind is None or pred.kind == "any")
        and not pred.scope_prefix
        and not pred.scope_exclude
        and not pred.public_only
        and pred.inbound_count_min is None
        and pred.inbound_count_max is None
        and pred.outbound_count_min is None
        and pred.outbound_count_max is None
    )


def _smallest_enclosing(symbols: list[tuple[str, int, int]], lineno: int) -> str | None:
    """Find the qname of the symbol whose `[start_line, end_line]` brackets `lineno`.

    `symbols` is the `(qname, start_line, end_line)` list returned by
    `Store.symbols_in_file_with_lines`. When symbols nest (a method inside a
    class), the smallest enclosing one wins — i.e. the symbol with the latest
    `start_line` still ≤ `lineno`, whose `end_line` is ≥ `lineno`.

    Returns `None` when `lineno` falls outside every symbol's line range — the
    grep matched something at module level (imports, top-level statements) or
    in whitespace at end-of-file. The caller drops these from the fallback to
    avoid suggesting "the whole file" as a symbol.
    """
    enclosing: str | None = None
    for qname, start, end in symbols:
        if start > lineno:
            break  # symbols are start_line-ordered; no later one starts ≤ lineno
        if start <= lineno <= end:
            enclosing = qname
    return enclosing


class TrieTools:
    """The three MCP tools as plain methods, so they can be tested without the transport.

    Owns the Store for the lifetime of the surrounding process.

    `event_name` controls the telemetry event name emitted on each call.
    Defaults to `"mcp_call"` (the value the MCP server uses); the CLI
    overrides it to `"cli_call"` so the audit can distinguish CLI-
    originated invocations from real MCP traffic. The fields populated on
    each event are identical regardless of surface — only the event name
    differs — so an aggregator that wants to merge them can; one that
    wants to split them can filter by `event`.
    """

    def __init__(self, project_root: Path, *, event_name: str = "mcp_call") -> None:
        self.config, self.root = Config.find_and_load(project_root)
        self.mcp_cfg: Mcp = self.config.mcp
        self.event_name = event_name
        # Resolve ripgrep up front so the failure mode is "server refuses
        # to start" rather than "first fallback query mysteriously errors".
        # Stored on the instance so per-call shellouts skip the PATH walk.
        self.rg_path = _require_ripgrep()
        # Telemetry: configure from the project's [debug] block. Agents spawn the
        # MCP server directly (not via `trie ...`), so this is the only place we
        # can wire it from config for the stdio path. The env var TRIE_DEBUG
        # still wins if set.
        telemetry.configure(self.config.debug, self.root)
        # Only emit the `mcp_server_start` event on the actual MCP path.
        # The CLI also constructs `TrieTools` for `trie grep`/`read`/`trace`,
        # but those are short-lived processes — flagging them as server
        # starts would pollute the audit's MCP usage stats with phantom
        # spawns. CLI usage is captured separately via `cli_call` events.
        if event_name == "mcp_call":
            telemetry.emit("mcp_server_start", project_root=str(self.root))
        self.triefacts_root = self.root / self.config.triefacts.root
        self.src_root = (self.root / self.config.triefacts.source_root).resolve()
        self.store = Store(self.root / ".trie" / "graph.db")
        # Session id for patch operations. Injectable via TRIE_SESSION_ID so a
        # host (e.g. an opencode fork) can align trie's patch session with its own
        # session boundaries; falls back to a per-server-lifetime UUID standalone.
        import os
        import uuid

        self._session_id = os.environ.get("TRIE_SESSION_ID") or uuid.uuid4().hex[:12]

    def close(self) -> None:
        self.store.close()

    # --- patch tools -------------------------------------------------------

    def patch(
        self,
        qname: str,
        note: str = "",
        source: str = "",
        reason: str = "",
    ) -> dict[str, Any]:
        """Record WHY an existing symbol changed (or is about to change).

        You make the code change yourself with your normal editing tools; this
        posts the intent note that the pre-commit `trie intent` gate requires
        for every changed symbol. Provide `note` (why, not what — one or two
        sentences written for the reviewer reading the commit digest later);
        `source` is accepted as a verbatim-payload alternative. Returns
        {patch_id, qname, pending_patch_count, blast_radius}. Notes accumulate
        until commit() archives them to the session log.
        """
        if bool(note.strip()) == bool(source.strip()):
            return _error(
                "invalid_argument",
                "provide exactly one of `note` or `source`.",
                "use `note` to describe the change, or `source` for the exact body.",
            )
        # `source=` is carried as the note payload with a sentinel reason so the
        # backend path can pass it through verbatim (a future deterministic lane).
        payload_note = note if note.strip() else source
        payload_reason = reason if note.strip() else (reason or "verbatim-source")
        try:
            patch_id = self.store.add_patch(qname, payload_note, payload_reason, self._session_id)
        except KeyError:
            # A missed qname is far more often hand-built/guessed than a
            # genuinely removed symbol — lead with did-you-mean candidates so
            # the agent recovers in zero extra round trips.
            close = _close_qname_matches(qname, self.store.all_qualified_names())
            suggestion = (
                f"Did you mean: {', '.join(close)}? "
                if close
                else "Use grep({'name_contains': '...'}) to find the exact qname. "
            )
            return _error(
                "not_found",
                f"Symbol {qname!r} not found in the graph.",
                suggestion + "For a removed symbol, use delete intent (patch create --gone).",
                fix={
                    "tool": "patch",
                    "args": {"qname": close[0] if close else qname, "note": note or ""},
                },
            )
        detail = self.store.get_symbol_detail(qname)
        return {
            "patch_id": int(patch_id),
            "qname": qname,
            "mode": "note" if note.strip() else "source",
            "pending_patch_count": detail.pending_patch_count if detail else 1,
            "blast_radius": self._blast_radius_brief(qname),
        }

    def batch_patch(self, items: list[dict[str, Any]]) -> dict[str, Any]:
        """Record intent notes for MANY symbols in ONE call.

        The usual way to clear the `trie intent` gate after a multi-symbol
        change. `items` is a list of objects, each:
          {"op": "patch",  "qname": "src/foo:bar", "note": "...", "reason": "..."}
          {"op": "create", "qname": "src/foo:baz", "note": "...",
           "file_path": "...", "anchor_qname": "...", "reason": "..."}
        `op` defaults to "patch". Recording is a cheap DB write; batching
        collapses what would be N separate tool calls into one. Items are
        independent — a bad item is reported in `results` but does not abort
        the rest. Returns {staged, failed, results, pending_patch_count}.
        """
        if not isinstance(items, list) or not items:
            return _error("invalid_argument", "items must be a non-empty list of patch objects.")

        from trie.parse import registry

        src_root = (self.root / self.config.triefacts.source_root).resolve()
        results: list[dict[str, Any]] = []
        staged = 0
        for idx, item in enumerate(items):
            if not isinstance(item, dict):
                results.append({"index": idx, "ok": False, "error": "item is not an object"})
                continue
            qname = str(item.get("qname", "")).strip()
            note = str(item.get("note", "")).strip()
            reason = str(item.get("reason", "") or "")
            op = str(item.get("op", "patch")).strip().lower() or "patch"
            if not qname or not note:
                results.append(
                    {"index": idx, "qname": qname, "ok": False, "error": "qname and note required"}
                )
                continue
            try:
                # Graceful create→patch fallback: if a `create` targets a symbol
                # that already exists in the graph, record it as a `patch`
                # instead of failing. Recording intent shouldn't force the agent
                # to re-classify create vs patch — post-sync the symbol usually
                # exists, and the note is equally valid either way. The result
                # flags `fell_back: True` so the caller can see what happened.
                if op == "create" and self.store.get_symbol_detail(qname) is not None:
                    op = "patch"
                    fell_back_from_create = True
                else:
                    fell_back_from_create = False

                if op == "create":
                    target_file = str(item.get("file_path", "")) or registry.resolve_create_target(
                        src_root, qname
                    )
                    cid = self.store.add_create_patch(
                        target_file=target_file,
                        target_qname=qname,
                        note=note,
                        reason=reason,
                        session_id=self._session_id,
                        anchor_qname=str(item.get("anchor_qname", "")) or None,
                    )
                    results.append(
                        {"index": idx, "qname": qname, "ok": True, "op": "create", "patch_id": cid}
                    )
                    staged += 1
                else:
                    pid = self.store.add_patch(qname, note, reason, self._session_id)
                    entry = {
                        "index": idx,
                        "qname": qname,
                        "ok": True,
                        "op": "patch",
                        "patch_id": pid,
                    }
                    if fell_back_from_create:
                        entry["fell_back"] = True
                        entry["note"] = "symbol already existed — recorded as patch"
                    results.append(entry)
                    staged += 1
            except KeyError:
                close = _close_qname_matches(qname, self.store.all_qualified_names())
                entry = {"index": idx, "qname": qname, "ok": False, "error": "symbol not found"}
                if close:
                    entry["did_you_mean"] = close
                results.append(entry)
        pending = len(self.store.get_patched_qnames()) + sum(
            len(v) for v in self.store.get_create_patches_grouped().values()
        )
        fell_back = [r["qname"] for r in results if r.get("fell_back")]
        summary = {
            "staged": staged,
            "failed": len(results) - staged,
            "results": results,
            "pending_patch_count": pending,
        }
        if fell_back:
            summary["created_as_patch"] = fell_back
            summary["note"] = (
                f"{len(fell_back)} symbol(s) already existed and were recorded as patches: "
                + ", ".join(fell_back)
            )
        return summary

    def _blast_radius_brief(self, qname: str) -> dict[str, Any]:
        """Compact blast-radius for patch returns (no LLM). Best-effort."""
        try:
            br = self.blast_radius(qname)
            if "error" in br:
                return {"direct": 0, "cascade": [], "cascade_count": 0, "hubs_stopped_at": []}
            return {
                "direct": br["direct"],
                "cascade": [c["qname"] for c in br["cascade"]],
                "cascade_count": br["cascade_count"],
                "hubs_stopped_at": br["hubs_stopped_at"],
            }
        except Exception:
            return {"direct": 0, "cascade": [], "cascade_count": 0, "hubs_stopped_at": []}

    def create_symbol(
        self,
        qname: str,
        note: str,
        file_path: str = "",
        anchor_qname: str = "",
        reason: str = "",
    ) -> dict[str, Any]:
        """Record the intent behind a NEW symbol (not yet in the graph).

        You write the code yourself; this stores the why so the added symbol
        passes the `trie intent` gate and its purpose lands in the commit
        digest. `qname` is the intended qualified name (e.g. 'src/foo:helper');
        `note` describes what it is for; `file_path` is the target source file
        (derived from qname's module part when omitted); `anchor_qname`
        optionally names an existing neighbour. Returns
        {create_patch_id, qname}.
        """
        if not note.strip():
            return _error("invalid_argument", "note must describe the new symbol.")
        # Graceful create→patch fallback: recording intent for a symbol that
        # already exists shouldn't be an error the agent has to recover from —
        # the note is equally valid as a patch. Record it and say so.
        if self.store.get_symbol_detail(qname) is not None:
            pid = self.store.add_patch(qname, note, reason, self._session_id)
            return {
                "patch_id": int(pid),
                "qname": qname,
                "op": "patch",
                "fell_back": True,
                "note": f"{qname!r} already existed — recorded as a patch instead of a create.",
            }
        # Resolve the target source file. An explicit `file_path` always wins.
        # Otherwise the qname's module part names the file MINUS extension — probe
        # the registered language suffixes for an existing file on disk (the
        # common "add a symbol to an existing module" case), so a `.ts`/`.tsx`
        # module isn't mis-resolved to a non-existent `.py`. Only when no file
        # exists yet (true new-file creation) do we fall back to a default suffix,
        # inferred from a sibling file in the same directory when possible, else
        # the first registered backend's source_suffix.
        target_file = file_path or self._resolve_create_target(qname)
        cid = self.store.add_create_patch(
            target_file=target_file,
            target_qname=qname,
            note=note,
            reason=reason,
            session_id=self._session_id,
            anchor_qname=anchor_qname or None,
        )
        return {"create_patch_id": int(cid), "qname": qname, "target_file": target_file}

    def _resolve_create_target(self, qname: str) -> str:
        """Map a new-symbol qname to its source file path (registry-driven)."""
        from trie.parse import registry

        return registry.resolve_create_target(self.src_root, qname)

    def delete_symbol(self, qname: str, reason: str = "") -> dict[str, Any]:
        """Record the intent behind deleting an existing symbol.

        You remove the code yourself; this notes why. Returns
        {patch_id, qname, dependents}. `dependents` lists symbols that
        reference this one — review them, and note the ones you also change.
        For symbols already gone from the graph, use the CLI form:
        `trie patch create <qname> -n "..." --gone`.
        """
        try:
            pid = self.store.add_delete_patch(qname, reason, self._session_id)
        except KeyError:
            return _error(
                "not_found",
                f"Symbol {qname!r} not found in the graph.",
                "Use grep({'name_contains': '...'}) to find the exact qname.",
            )
        dependents = []
        for src in self.store.references_in(qname):
            d = self.store.get_symbol_detail(src)
            if d is not None:
                dependents.append({"qname": src, "source_pointer": f"{d.file_path}:{d.start_line}"})
        return {"patch_id": int(pid), "qname": qname, "dependents": dependents}

    def rename_symbol(self, qname: str, new_name: str, reason: str = "") -> dict[str, Any]:
        """Record a rename of an existing symbol to `new_name` (the local name).

        You perform the rename in source yourself; this notes the intent.
        Returns {patch_id, qname, new_name, references} — references are the
        call sites trie can see, so you can verify you updated them all.
        """
        if not new_name.isidentifier():
            return _error(
                "invalid_argument",
                f"{new_name!r} is not a valid identifier.",
                "choose a valid Python identifier for new_name.",
            )
        try:
            pid = self.store.add_rename_patch(qname, new_name, reason, self._session_id)
        except KeyError:
            return _error(
                "not_found",
                f"Symbol {qname!r} not found in the graph.",
                "Use grep({'name_contains': '...'}) to find the exact qname.",
            )
        refs = list(self.store.references_in(qname))
        return {"patch_id": int(pid), "qname": qname, "new_name": new_name, "references": refs}

    def blast_radius(self, qname: str) -> dict[str, Any]:
        """Compute the cascade blast radius of editing `qname` — free graph math.

        Resolves the symbol's file and reuses the mature `compute_cascade` walk to
        find every symbol whose triefact would be regenerated if `qname` changed,
        with each one's BFS hop distance from the seed (so a caller can order
        the cascade as a staggered wavefront).

        Returns {qname, file, direct, cascade:[{qname, hop, file}], cascade_count,
        hubs_stopped_at}. LLM-free.
        """
        from trie.sync.cascade import compute_cascade

        detail = self.store.get_symbol_detail(qname)
        if detail is None:
            return _error(
                "not_found",
                f"Symbol {qname!r} not found in the graph.",
                "Use grep({'name_contains': '...'}) to find the exact qname.",
            )
        file_path = detail.file_path
        result = compute_cascade(
            changed_files=[file_path],
            store=self.store,
            depth=2,
            hub_threshold=self.config.cascade.hub_symbol_threshold,
        )
        cascade = [
            {
                "qname": qn,
                "hop": result.hop_by_qname.get(qn, 1),
                "file": result.file_by_cascaded_qname.get(qn, ""),
            }
            for qn in sorted(
                result.cascaded_qnames,
                key=lambda q: (result.hop_by_qname.get(q, 99), q),
            )
        ]
        # "direct" = symbols reached at hop 1 (immediate callers across the file).
        direct = sum(1 for c in cascade if c["hop"] <= 1)
        return {
            "qname": qname,
            "file": file_path,
            "direct": direct,
            "cascade": cascade,
            "cascade_count": len(cascade),
            "hubs_stopped_at": [],
        }

    def patch_drop(
        self,
        qname: str | None = None,
    ) -> dict[str, Any]:
        """Remove pending patches for a symbol or for this session.

        Omit qname to drop all patches created this session.
        Returns {removed: int}.
        """
        if qname is not None:
            removed = self.store.delete_patches(qname=qname)
        else:
            removed = self.store.delete_patches(session_id=self._session_id)
        return {"removed": removed}

    def patch_list(self) -> dict[str, Any]:
        """List all pending patches grouped by symbol, plus pending creates.

        Returns {patches: [{qname, count, origin, kind, notes}], creates: [...],
        apply_in_progress: bool}.
        """
        from trie import activity as activity_mod

        qnames = self.store.get_patched_qnames()
        patches: list[dict[str, Any]] = []
        for qn in qnames:
            notes = self.store.get_patches_for_qname(qn)
            origins = set(p.get("session_id", "") for p in notes)
            origin = (
                "cascade" if origins == {"cascade"} else "mixed" if len(origins) > 1 else "agent"
            )
            # Structural kind, if any patch on this symbol set one.
            kind = "modify"
            for p in notes:
                if p.get("kind") in ("delete", "rename"):
                    kind = p["kind"]
            patches.append(
                {
                    "qname": qn,
                    "count": len(notes),
                    "origin": origin,
                    "kind": kind,
                    "notes": notes,
                }
            )
        creates = [
            {"target_qname": c["target_qname"], "target_file": c["target_file"], "note": c["note"]}
            for v in self.store.get_create_patches_grouped().values()
            for c in v
        ]
        status = activity_mod.read_status(self.root)
        return {
            "patches": patches,
            "creates": creates,
            "apply_in_progress": status.op == "apply" and status.is_active,
        }

    def preview(self) -> dict[str, Any]:
        """Review pending intent notes and their call-graph blast radius.

        Free, offline, idempotent. Returns {pending, creates, cascade, totals,
        ready_to_commit}. Call before commit() to see which symbols carry
        notes, which callers a reviewer might want to look at, and any blockers
        (e.g. a missing session note for a multi-symbol apply).
        """
        from trie.edits.pipeline import preview_patches

        pv = preview_patches(self.store, self.config)
        creates = self.store.get_create_patches_grouped()
        create_list = [c["target_qname"] for v in creates.values() for c in v]
        total = pv["patched_symbols"] + len(create_list)
        return {
            "pending": pv["patched_list"],
            "creates": create_list,
            "cascade": pv["cascade_list"],
            "totals": {
                "patches": pv["total_patches"],
                "symbols": total,
                "cascade_symbols": pv["cascade_symbols"],
            },
            "ready_to_commit": total > 0,
            "needs_session_note": total > 1,
        }

    def commit(self, session_note: str = "") -> dict[str, Any]:
        """Commit pending patch notes as intent — trie generates no code.

        Archives every pending note to the session log (feeding the per-commit
        digest, `read --history`, and the `trie intent` pre-commit gate) and
        clears the queue. `session_note` (the unifying intent) is required when
        more than one symbol is pending. Source changes are yours; this records
        why they happened.

        The response's `uncovered` key lists touched symbols that still have
        no note and would fail the pre-commit gate — stage notes for those and
        commit again instead of finding out at `git commit` time. Empty list
        means full coverage.
        """
        from trie.edits.pipeline import record_intent

        try:
            return record_intent(
                self.store,
                self.config,
                self.root,
                session_note=session_note,
            )
        except Exception as exc:
            return _error("internal", f"commit failed: {exc}")

    # Back-compat alias for the older tool name.
    def patch_apply(self, session_note: str = "") -> dict[str, Any]:
        """Alias for commit(): record pending notes as intent (no code generation)."""
        return self.commit(session_note=session_note)

    def summary(self) -> dict[str, Any]:
        """Return project-level aggregate counts for the project.

        Returns {project_name, total_symbols, public_symbols, total_files,
        total_edges, trie_version}.
        """
        import trie as trie_pkg

        conn = self.store._conn
        total_symbols: int = conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]
        public_symbols: int = conn.execute(
            "SELECT COUNT(*) FROM symbols WHERE is_public = 1"
        ).fetchone()[0]
        total_files: int = conn.execute("SELECT COUNT(DISTINCT file_path) FROM symbols").fetchone()[
            0
        ]
        total_edges: int = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]

        return {
            "project_name": self.root.name,
            "project_root": str(self.root),
            "total_symbols": total_symbols,
            "public_symbols": public_symbols,
            "total_files": total_files,
            "total_edges": total_edges,
            "trie_version": getattr(trie_pkg, "__version__", "unknown"),
        }

    def activity(self) -> dict[str, Any]:
        """Return the live writer status + working-tree stale set.

        Reads the ephemeral `.trie/activity.db` (see `trie.activity`). Any process
        — a terminal `trie sync` or the end-of-turn refresh hook — updates that DB,
        so any client can poll this for live writer status and the stale count
        regardless of which process is doing the work. A crashed writer reads back as idle.

        Returns {status: {...}, pending: {count, stale, head} | null,
        patches: {total_patches, symbol_count, create_count, by_origin}, apply: {...}|null}.
        """
        from trie import activity as activity_mod

        status = activity_mod.read_status(self.root)
        pending = activity_mod.read_pending(self.root)
        summary = self.store.patch_summary()
        apply_block = None
        if status.op == "apply" and status.is_active:
            apply_block = {
                "phase": status.current_file,
                "done": status.done,
                "total": status.total,
                "session_note": activity_mod.get_meta(self.root, "apply_session_note") or "",
            }
        return {
            "status": {
                "state": status.state,
                "op": status.op,
                "pid": status.pid,
                "is_active": status.is_active,
                "current_file": status.current_file,
                "done": status.done,
                "total": status.total,
                "error": status.error,
                "updated_at": status.updated_at,
            },
            "pending": (
                None
                if pending is None
                else {
                    "count": pending.count,
                    "stale": list(pending.stale),
                    "head": pending.head,
                    "computed_at": pending.computed_at,
                }
            ),
            "patches": {
                "total_patches": summary["total_patches"],
                "symbol_count": summary["symbol_count"],
                "create_count": summary["create_count"],
                "by_origin": summary["by_origin"],
            },
            "apply": apply_block,
        }

    def symbols_by_file(self, file_path: str) -> dict[str, Any]:
        """Return all symbols in a given source file.

        Returns {file_path, symbols: [SymbolDetail, ...]}.
        A file-level view over the symbol graph.
        """
        rows = self.store._conn.execute(
            """
            SELECT
                sym.qualified_name, sym.name, sym.kind, sym.file_path,
                sym.start_line, sym.end_line, sym.signature, sym.is_public,
                (SELECT COUNT(*) FROM edges e WHERE e.dst_symbol_id = sym.id) as inbound_count,
                (SELECT COUNT(*) FROM edges e WHERE e.src_symbol_id = sym.id) as outbound_count,
                COALESCE(ts.one_liner, '') as one_liner,
                COALESCE(ts.role, '') as role
            FROM symbols sym
            LEFT JOIN triefact_sections ts ON ts.symbol_id = sym.id
            WHERE sym.file_path = ?
            ORDER BY sym.start_line
            """,
            (file_path,),
        ).fetchall()

        symbols = [
            {
                "qname": r[0],
                "name": r[1],
                "kind": r[2],
                "file_path": r[3],
                "start_line": r[4],
                "end_line": r[5],
                "is_public": bool(r[7]),
                "inbound_count": r[8],
                "outbound_count": r[9],
                "one_liner": r[10],
                "role": r[11],
            }
            for r in rows
        ]
        return {"file_path": file_path, "symbols": symbols}

    def file_triefact(self, file_path: str) -> dict[str, Any]:
        """Return the whole triefact for a source file: front matter + ordered
        per-symbol sections (prose body, role, fingerprints, source line range).

        `file_path` is source-root
        relative (e.g. `trie/sync/writer.py`). Returns
        `{file_path, triefact_path, exists, front_matter, sections: [...]}`;
        `exists` is False (with empty sections) when the file has no triefact yet.
        """
        from trie.sync.writer import TriefactFile, extract_one_liner

        rel_md = Path(file_path).with_suffix(".md")
        triefact_path = self.triefacts_root / rel_md
        triefact_rel = str(triefact_path.relative_to(self.root))
        if not triefact_path.exists():
            return {
                "file_path": file_path,
                "triefact_path": triefact_rel,
                "exists": False,
                "front_matter": {},
                "sections": [],
            }

        triefact = TriefactFile.parse(triefact_path.read_text())

        # Line ranges + kind come from the store (the sentinel doesn't carry them).
        lines_by_qname: dict[str, tuple[int, int]] = {}
        kind_by_qname: dict[str, str] = {}
        for row in self.store._conn.execute(
            "SELECT qualified_name, start_line, end_line, kind FROM symbols WHERE file_path = ?",
            (file_path,),
        ).fetchall():
            lines_by_qname[row[0]] = (row[1], row[2])
            kind_by_qname[row[0]] = row[3]

        sections = []
        for qn in triefact.section_qnames():
            sec = triefact.get_section(qn)
            if sec is None:
                continue
            start, end = lines_by_qname.get(qn, (0, 0))
            sections.append(
                {
                    "qname": qn,
                    "kind": kind_by_qname.get(qn, ""),
                    "role": sec.role,
                    "body": sec.body,
                    "one_liner": extract_one_liner(sec.body),
                    "fingerprint": sec.fingerprint,
                    "body_fingerprint": sec.body_fingerprint or "",
                    "start_line": start,
                    "end_line": end,
                }
            )

        return {
            "file_path": file_path,
            "triefact_path": triefact_rel,
            "exists": True,
            "front_matter": triefact.front_matter,
            "sections": sections,
        }

    # --- grep --------------------------------------------------------------

    def grep(
        self,
        predicate: dict[str, Any] | None = None,
        rank_by: str | None = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        """Find symbols matching `predicate`.

        Predicate fields (all optional, but at least one is required —
        an empty predicate returns an `invalid_argument` error):
        - `name_contains`: substring match against the symbol's local name (case-insensitive).
        - `kind`: one of `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`, `"interface"`, `"type"`, `"enum"`, `"enum_member"`, `"property"`, `"any"`.
        - `scope_prefix`: file-path prefix, e.g. `"trie/"` to exclude tests/vendored code.
        - `scope_exclude`: list of file-path prefixes to skip, e.g. `["tests/"]`.
        - `public_only`: bool. Restrict to symbols whose name doesn't start with `_`.
        - `inbound_count`: `{min?: int, max?: int}` — filter by inbound edge count.
        - `outbound_count`: `{min?: int, max?: int}` — filter by outbound edge count.

        `rank_by` is one of `"public_first"` (default), `"inbound_count"` (centrality
        for orientation queries), or `"alphabetical"`.

        Provide only the fields you need — most queries use just `name_contains` or
        `scope_prefix`. To list the architectural hubs of a project, pass
        `public_only: true` with `rank_by: "inbound_count"`.

        Return shape:
        ```
        {
          "hits": [ {qname, signature, file_pointer, one_liner, is_public, kind,
                     inbound_count, outbound_count}, ... ],
          "fallback"?: { ... },  # present only when hits is empty
          "related"?: [ ... ],   # body/prose-matched extras when hits < limit
          "related_kind"?: "text_match" | "fuzzy_prose"
        }
        ```
        When name hits leave room under `limit`, `related` carries candidates
        whose *bodies or prose* match the query (never repeating a hit's
        qname) — the module implementing a concept surfaces even when its
        symbol names don't contain the query string.

        On empty hits, `fallback.kind` is one of:
        - `"none"`: predicate had no `name_contains` for the fallback to search on.
        - `"text_match_empty"`: the query string appears in no in-scope source body
          and fuzzy matching also found nothing above the cutoff.
        - `"text_match"`: a string search against in-scope source bodies found
          candidate symbols; `matches` is the ranked list (by `inbound_count`
          desc) capped at `grep_fallback_match_limit` and by the request's
          own `limit`. Even when the underlying string match was very broad,
          we always return the top-ranked candidates so the agent can
          triangulate from data rather than refine blindly.
        - `"fuzzy_prose"`: no exact match anywhere, but rapidfuzz found symbols
          whose name, one_liner, or triefact prose is close enough; `matches`
          is sorted by relevance score descending.

        Errors (bad predicate shape, etc.) still return `{"error": {...}}`.
        """
        tele_args = (
            {"predicate": predicate, "rank_by": rank_by, "limit": limit}
            if telemetry.capture_args()
            else {}
        )
        with telemetry.timed(self.event_name, tool="grep", args=tele_args) as tele_ctx:
            pred_obj, err = self._parse_predicate(predicate)
            if err is not None:
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err

            # Reject no-op predicates explicitly. An empty predicate previously
            # returned the alphabetically-first N public symbols under the
            # default `public_first` ranking — useful for nobody, and easy to
            # mistake for "trie found these relevant results." We refuse and
            # tell the agent what shape of predicate to send instead. Both
            # surfaces (MCP wire + `trie grep` CLI) share this code path so
            # the behaviour is identical on either.
            if _predicate_is_empty(pred_obj):
                err = _error(
                    "invalid_argument",
                    "predicate is empty: at least one filter field is required.",
                    (
                        "Pass `name_contains` for a substring search, "
                        "`scope_prefix` for a path-restricted query, "
                        "`public_only: true` to list public symbols, or "
                        '`inbound_count: {min: N}` (with `rank_by: "inbound_count"`) '
                        "to surface architectural hubs."
                    ),
                )
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err

            rank = rank_by or self.mcp_cfg.grep_default_rank_by
            capped_limit = min(max(1, limit), self.mcp_cfg.grep_max_limit)

            hits = self.store.grep_symbols(pred_obj, rank_by=rank, limit=capped_limit)

            # When a name query is present, re-sort the SQL hits by relevance
            # so the closest fuzzy match surfaces first within the rank_by bucket.
            # Score on name + one_liner only — no disk reads on the primary path.
            if pred_obj.name_contains and hits:
                query_str = pred_obj.name_contains
                hits = sorted(
                    hits,
                    key=lambda h: -_score_sym(query_str, h),
                )

            one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
            hit_dicts = [
                {
                    "qname": h.qualified_name,
                    "signature": h.signature or "",
                    "file_pointer": f"{h.file_path}:{h.start_line}",
                    "one_liner": _truncate(h.one_liner, one_liner_cap),
                    "is_public": h.is_public,
                    "kind": h.kind,
                    "inbound_count": h.inbound_count,
                    "outbound_count": h.outbound_count,
                    "pending_patch_count": h.pending_patch_count,
                    "has_pending_patches": h.pending_patch_count > 0,
                }
                for h in hits
            ]
            result: dict[str, Any] = {"hits": hit_dicts}

            # When the predicate matched nothing, try the text-match fallback.
            # The fallback always produces SOMETHING in the response — even if
            # it's `kind="none"` — so the agent never has to guess whether
            # trie tried alternatives or not. The fallback is additionally
            # capped by the request's own `limit` so an 8-row ask never fans
            # out into a 30-row consolation table.
            if not hit_dicts:
                fallback = self._maybe_text_match_fallback(pred_obj, max_matches=capped_limit)
                result["fallback"] = fallback
                tele_ctx["fallback_kind"] = fallback["kind"]
                tele_ctx["fallback_match_count"] = len(fallback.get("matches", []))
            elif len(hit_dicts) < capped_limit and pred_obj.name_contains:
                # Fill-up: a couple of weak name hits used to suppress the
                # text/prose fallback entirely, hiding the module that actually
                # implements the concept (e.g. `triediff` name-matching only a
                # workflow installer while all the digest machinery lives in
                # `session_diff`). Append prose/body candidates the name scan
                # missed, clearly separated under `related`.
                seen = {h["qname"] for h in hit_dicts}
                fb = self._maybe_text_match_fallback(
                    pred_obj, max_matches=capped_limit - len(hit_dicts) + len(seen)
                )
                related = [m for m in fb.get("matches", []) if m.get("qname") not in seen][
                    : capped_limit - len(hit_dicts)
                ]
                if related:
                    result["related"] = related
                    result["related_kind"] = fb["kind"]
                    tele_ctx["related_count"] = len(related)

            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hit_dicts)
            tele_ctx["response_bytes"] = len(json.dumps(result, default=str))
            if telemetry.capture_responses():
                tele_ctx["response"] = result
            return result

    def _maybe_text_match_fallback(
        self, pred: GrepPredicate, *, max_matches: int | None = None
    ) -> dict[str, Any]:
        """Build the `fallback` envelope returned alongside an empty `hits` list.

        `max_matches` additionally caps the candidate list below the configured
        `grep_fallback_match_limit` — callers pass the request's own `limit`
        (or the remaining row budget on the fill-up path) so fallback output
        never exceeds what the caller asked for.

        The contract is to always return a dict with a `kind` field, so the
        agent can dispatch on three distinct empty cases:

        - `none`: no `name_contains` was supplied; nothing to text-search for.
          The agent should not try the same predicate again — its shape isn't
          string-searchable.
        - `text_match_empty`: the query appears in no in-scope source body
          (or only outside any indexed symbol). Likely a typo or a wrong
          project.
        - `text_match`: candidate symbols whose bodies contain the query,
          ranked by `inbound_count` descending and capped at
          `grep_fallback_match_limit`.

        We deliberately do not bail out when the result is "too noisy" — raw
        ripgrep would have shown the user N matches and let them eyeball
        them; we match that floor by ranking and capping. The `match_count`
        / `unique_symbols` fields convey the breadth of the underlying hit
        so the agent knows the cap was reached.

        Predicate fields beyond `name_contains` (`scope_prefix`, `scope_exclude`,
        `public_only`, etc.) are applied to the candidate list at the end, so
        the agent's scope restrictions are honoured even on the fallback path.
        """
        query = (pred.name_contains or "").strip()
        if not query:
            return {
                "kind": "none",
                "note": (
                    "Predicate matched no symbols, and it has no `name_contains` "
                    "to text-search for. Add a name substring or relax other filters."
                ),
            }

        # Walk in-scope source files and collect line-level hits. The
        # ripgrep walker has its own internal cap on files-scanned (a
        # runtime guard, not a discriminator); on hitting that cap it
        # returns whatever it accumulated so far, which we treat as
        # authoritative — the agent gets the most-relevant N files' worth
        # of matches either way.
        rg_hits = self._text_match_in_scope(query)
        if not rg_hits:
            # Exact-string search found nothing — try fuzzy scoring across
            # all symbol names and one_liners as a last resort.
            fuzzy_fallback = self._fuzzy_prose_fallback(query, pred, max_matches=max_matches)
            if fuzzy_fallback:
                return fuzzy_fallback
            return {
                "kind": "text_match_empty",
                "query": query,
                "note": (
                    f"Predicate matched no symbols, and {query!r} appears in no "
                    "in-scope source file body either. Likely a typo or a name "
                    "that doesn't exist in this project."
                ),
            }

        # Attribute each matched line to the smallest enclosing symbol.
        per_symbol = self._attribute_text_matches_to_symbols(rg_hits)
        if not per_symbol:
            # The query matched lines, but every match was outside any symbol
            # (module-level code, imports, comments at file top, etc.). This
            # is honest signal — the agent shouldn't be misled into thinking a
            # symbol was found.
            return {
                "kind": "text_match_empty",
                "query": query,
                "note": (
                    f"Query {query!r} appears in source but only outside any "
                    "documented symbol (e.g. in imports or module-level code). "
                    "No symbol-level redirect possible."
                ),
            }

        # Build candidate hits with full SymbolDetail and the per-body hit count,
        # then apply predicate filters (scope_prefix, scope_exclude, public_only,
        # kind) the user originally asked for. Rank by inbound_count desc, cap
        # at the configured match limit. We always return *something* when
        # there are candidates — even a 30-symbol fanout is more useful as a
        # ranked top-N than as a "too noisy" refusal.
        candidates: list[tuple[SymbolDetail, int]] = []
        for qname, body_hits in per_symbol.items():
            detail = self.store.get_symbol_detail(qname)
            if detail is None:
                continue
            if not self._candidate_matches_predicate(detail, pred):
                continue
            candidates.append((detail, body_hits))

        if not candidates:
            # Text-search found symbols, but none survived the predicate's
            # other filters. Try fuzzy fallback before giving up.
            fuzzy_fallback = self._fuzzy_prose_fallback(query, pred, max_matches=max_matches)
            if fuzzy_fallback:
                return fuzzy_fallback
            return {
                "kind": "text_match_empty",
                "query": query,
                "note": (
                    f"Query {query!r} matched symbols, but none satisfied the "
                    "other predicate filters (e.g. `scope_prefix`, `kind`, "
                    "`public_only`). Try a broader predicate."
                ),
            }

        candidates.sort(key=lambda c: (-c[0].inbound_count, c[0].qualified_name))
        cap = self.mcp_cfg.grep_fallback_match_limit
        if max_matches is not None:
            cap = min(cap, max(1, max_matches))
        capped = candidates[:cap]
        truncated = len(candidates) > len(capped)

        one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
        matches = [
            {
                "qname": d.qualified_name,
                "signature": d.signature or "",
                "file_pointer": f"{d.file_path}:{d.start_line}",
                "one_liner": _truncate(d.one_liner, one_liner_cap),
                "is_public": d.is_public,
                "kind": d.kind,
                "inbound_count": d.inbound_count,
                "outbound_count": d.outbound_count,
                "pending_patch_count": d.pending_patch_count,
                "text_match_hits_in_body": body_hits,
            }
            for d, body_hits in capped
        ]
        note = (
            "Predicate matched no symbols, but the query string appears in "
            "the bodies of these symbols. Ranked by `inbound_count` so the "
            "most-referenced (likely hub) candidate is first."
        )
        if truncated:
            note += (
                f" Showing top {len(capped)} of {len(candidates)} matching "
                f"symbols; refine `name_contains` or add `scope_prefix` to "
                f"see different candidates."
            )
        return {
            "kind": "text_match",
            "query": query,
            "match_count": sum(per_symbol.values()),
            "unique_symbols": len(per_symbol),
            "matches": matches,
            "note": note,
        }

    def _fuzzy_prose_fallback(
        self, query: str, pred: GrepPredicate, *, max_matches: int | None = None
    ) -> dict[str, Any] | None:
        """Fuzzy-score all in-scope symbols against `query` using name + one_liner +
        prose, returning a `fuzzy_prose` fallback envelope if any clear enough.

        Called when both SQL name-match and ripgrep body-match return nothing.
        Uses the same `_score_sym` primitive as `grep_entry_points` so scoring
        semantics are consistent across every search surface.

        Returns `None` when no candidate clears `fuzzy_cutoff`, so the caller
        can fall through to a `text_match_empty` response.
        """
        cutoff = self.mcp_cfg.fuzzy_cutoff
        pre_filter = self.mcp_cfg.fuzzy_prose_pre_filter
        prose_weight = self.mcp_cfg.fuzzy_prose_weight
        match_limit = self.mcp_cfg.grep_fallback_match_limit
        if max_matches is not None:
            match_limit = min(match_limit, max(1, max_matches))

        # Walk all symbols in the store; apply predicate filters before scoring
        # to keep the loop as tight as possible.
        all_syms = self.store.grep_symbols(
            GrepPredicate(
                scope_prefix=pred.scope_prefix,
                scope_exclude=pred.scope_exclude,
                public_only=pred.public_only,
                kind=pred.kind,
            ),
            rank_by="public_first",
            limit=self.mcp_cfg.grep_max_limit * 10,  # broad sweep
        )

        scored: list[tuple[float, SymbolDetail]] = []
        for sym in all_syms:
            local_name = (
                sym.qualified_name.split(":")[-1]
                if ":" in sym.qualified_name
                else sym.qualified_name
            )
            pre_score = max(
                _fuzzy_score(query, local_name),
                _fuzzy_score(query, sym.one_liner or "") * 0.8,
            )
            prose = ""
            if pre_score >= pre_filter:
                prose, _ = self._prose_for(sym)
            score = _score_sym(query, sym, prose=prose, prose_weight=prose_weight)
            if score >= cutoff:
                scored.append((score, sym))

        if not scored:
            return None

        scored.sort(key=lambda x: (-x[0], x[1].inbound_count))
        capped = scored[:match_limit]
        one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
        matches = [
            {
                "qname": sym.qualified_name,
                "signature": sym.signature or "",
                "file_pointer": f"{sym.file_path}:{sym.start_line}",
                "one_liner": _truncate(sym.one_liner, one_liner_cap),
                "is_public": sym.is_public,
                "kind": sym.kind,
                "inbound_count": sym.inbound_count,
                "outbound_count": sym.outbound_count,
                "score": round(score, 1),
            }
            for score, sym in capped
        ]
        return {
            "kind": "fuzzy_prose",
            "query": query,
            "matches": matches,
            "note": (
                f"No exact name or body match for {query!r}. "
                "These symbols were found by fuzzy-matching name, one_liner, "
                "and triefact prose. Ranked by relevance score descending."
            ),
        }

    def _text_match_in_scope(self, query: str) -> dict[str, list[int]]:
        """Shell out to ripgrep to find `query` in in-scope source bodies.

        Returns `{rel_path: [line_numbers]}` keyed by paths relative to
        `src_root`. The implementation runs `rg --json --line-number
        --fixed-strings --ignore-case` rooted at `src_root` and parses
        the streaming JSON output, taking the `match` events and ignoring
        framing (`begin`/`end`/`summary`).

        We post-filter results against `discover_files(...)`'s scope set
        rather than translating `config.scope` into rg's `--glob` flags.
        Single source of truth for scope (Python), and the post-filter
        is a hash-set lookup per match — negligible cost. rg's default
        `.gitignore` honouring already excludes the obvious noise.

        Cap: stops accumulating once `grep_fallback_max_files` distinct
        files have hits, matching the previous Python implementation's
        runtime guard against very-common substrings on huge projects.
        """
        # `-F`: treat the query as a literal string, not a regex. The agent
        # passed `name_contains` expecting substring semantics.
        # `-i`: case-insensitive, matching the previous Python behaviour.
        # `--json --line-number`: structured output we can parse without
        #   reinventing rg's text format.
        # `--no-messages`: drop "file not readable" warnings; we only care
        #   about matches.
        proc = subprocess.run(
            [
                self.rg_path,
                "--json",
                "--line-number",
                "--fixed-strings",
                "--ignore-case",
                "--no-messages",
                "--",
                query,
                str(self.src_root),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        # rg exits 1 when there are no matches; that's not an error from
        # our side. Exit codes ≥ 2 indicate genuine failure (invalid
        # regex, broken pipe, etc.) but we already pass `--fixed-strings`,
        # so the realistic failure is "rg disappeared between startup and
        # now" — surface it loudly rather than mask it.
        if proc.returncode not in (0, 1):
            raise RuntimeError(
                f"rg failed (exit {proc.returncode}): {proc.stderr.strip() or proc.stdout.strip() or 'no output'}"
            )

        # Build the in-scope file set once so we can do O(1) membership
        # checks per match. Stored as str relative paths to match what
        # rg emits after we strip src_root.
        scope_set: set[str] = set()
        for abs_path in discover_files(self.root, self.config.scope):
            if abs_path.is_relative_to(self.src_root):
                scope_set.add(str(abs_path.relative_to(self.src_root)))

        max_files = self.mcp_cfg.grep_fallback_max_files
        hits: dict[str, list[int]] = {}
        src_root_str = str(self.src_root)

        for raw_line in proc.stdout.splitlines():
            if not raw_line:
                continue
            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                # rg occasionally emits non-JSON noise on stderr; we
                # already filtered stderr, but defend against a torn
                # event from a buffered write under load.
                continue
            if event.get("type") != "match":
                continue
            data = event.get("data") or {}
            path_obj = data.get("path") or {}
            abs_path_str = path_obj.get("text")
            lineno = data.get("line_number")
            if not isinstance(abs_path_str, str) or not isinstance(lineno, int):
                continue

            # Convert rg's absolute path back to src_root-relative. rg
            # was rooted at src_root so every match path starts with it,
            # but defend against symlink resolution drift.
            if not abs_path_str.startswith(src_root_str):
                continue
            rel = abs_path_str[len(src_root_str) :].lstrip("/")
            if rel not in scope_set:
                continue

            if rel in hits:
                hits[rel].append(lineno)
            else:
                if len(hits) >= max_files:
                    continue
                hits[rel] = [lineno]

        return hits

    def _attribute_text_matches_to_symbols(self, rg_hits: dict[str, list[int]]) -> dict[str, int]:
        """For each `(file, line)` match, attribute it to the smallest enclosing
        symbol by line range. Returns `{qname: count_of_hits_in_body}`.

        Lines that don't fall inside any symbol (module-level code, imports,
        whitespace at the bottom of a class) are dropped — the fallback is
        about steering the agent toward symbols, not arbitrary source locations.

        "Smallest enclosing" matters when symbols nest: a hit inside a method
        attributes to the method, not the surrounding class. Implemented by
        picking the symbol with the largest `start_line` not exceeding the
        match line, then bounded by `end_line`.
        """
        per_symbol: dict[str, int] = {}
        for file_path, linenos in rg_hits.items():
            symbols = self.store.symbols_in_file_with_lines(file_path)
            if not symbols:
                continue
            for lineno in linenos:
                enclosing = _smallest_enclosing(symbols, lineno)
                if enclosing is None:
                    continue
                per_symbol[enclosing] = per_symbol.get(enclosing, 0) + 1
        return per_symbol

    def _candidate_matches_predicate(self, detail: SymbolDetail, pred: GrepPredicate) -> bool:
        """Apply the predicate's non-name filters to a fallback candidate.

        `name_contains` is intentionally NOT enforced here: the whole point of
        the fallback is that the name didn't match. The other filters
        (`scope_prefix`, `scope_exclude`, `public_only`, `kind`, edge-count
        bounds) DO still apply — the agent's scope restrictions should narrow
        the fallback the same way they narrow the primary path.
        """
        if pred.scope_prefix and not detail.file_path.startswith(pred.scope_prefix):
            return False
        for excl in pred.scope_exclude:
            if detail.file_path.startswith(excl):
                return False
        if pred.public_only and not detail.is_public:
            return False
        if pred.kind is not None and pred.kind != "any" and detail.kind != pred.kind:
            return False
        if pred.inbound_count_min is not None and detail.inbound_count < pred.inbound_count_min:
            return False
        if pred.inbound_count_max is not None and detail.inbound_count > pred.inbound_count_max:
            return False
        if pred.outbound_count_min is not None and detail.outbound_count < pred.outbound_count_min:
            return False
        return not (
            pred.outbound_count_max is not None and detail.outbound_count > pred.outbound_count_max
        )

    def _parse_predicate(
        self, predicate: dict[str, Any] | None
    ) -> tuple[GrepPredicate, dict[str, Any] | None]:
        """Turn the dict the agent passed into a GrepPredicate, or return an error."""
        if predicate is None:
            return GrepPredicate(), None
        if not isinstance(predicate, dict):
            return GrepPredicate(), _error(
                "invalid_argument",
                "`predicate` must be an object with optional filter fields.",
                "Try predicate={'name_contains': '<fragment>'}.",
            )

        def _count_range(value: Any, field: str) -> tuple[int | None, int | None, dict | None]:
            if value is None:
                return None, None, None
            if not isinstance(value, dict):
                return (
                    None,
                    None,
                    _error(
                        "invalid_argument",
                        f"`{field}` must be an object like {{'min': N}} or {{'max': N}}.",
                    ),
                )
            mn = value.get("min")
            mx = value.get("max")
            if mn is not None and not isinstance(mn, int):
                return None, None, _error("invalid_argument", f"`{field}.min` must be an int.")
            if mx is not None and not isinstance(mx, int):
                return None, None, _error("invalid_argument", f"`{field}.max` must be an int.")
            return mn, mx, None

        in_min, in_max, err = _count_range(predicate.get("inbound_count"), "inbound_count")
        if err is not None:
            return GrepPredicate(), err
        out_min, out_max, err = _count_range(predicate.get("outbound_count"), "outbound_count")
        if err is not None:
            return GrepPredicate(), err

        kind = predicate.get("kind")
        if kind is not None and kind not in (*KINDS, "any"):
            allowed = "/".join((*KINDS, "any"))
            return GrepPredicate(), _error(
                "invalid_argument",
                (f"`kind` must be one of {allowed}, got {kind!r}."),
            )

        scope_exclude_raw = predicate.get("scope_exclude") or ()
        if isinstance(scope_exclude_raw, str):
            scope_exclude_raw = (scope_exclude_raw,)
        try:
            scope_exclude = tuple(str(x) for x in scope_exclude_raw)
        except TypeError:
            return GrepPredicate(), _error(
                "invalid_argument",
                "`scope_exclude` must be a list of path prefixes.",
            )

        return (
            GrepPredicate(
                name_contains=predicate.get("name_contains"),
                kind=kind,
                scope_prefix=predicate.get("scope_prefix"),
                scope_exclude=scope_exclude,
                public_only=bool(predicate.get("public_only", False)),
                inbound_count_min=in_min,
                inbound_count_max=in_max,
                outbound_count_min=out_min,
                outbound_count_max=out_max,
            ),
            None,
        )

    # --- read --------------------------------------------------------------

    def read(
        self,
        path: str,
        *,
        full: bool = False,
        show_source: bool = False,
        offset: int | None = None,
        limit: int | None = None,
        history: bool = False,
    ) -> dict[str, Any]:
        """Read source code or trie's synthesised description of it — triefact-first.

        Dispatch on `path`:

        - A qualified symbol name ('pkg/module:Name' or 'pkg/module:Class.method')
          with no matching file on disk → that symbol's prose plus one-liners for
          every immediate caller and callee.
        - A FILE PATH with a triefact → a COMPACT view by default (file
          description, ref counts, one entry per symbol: qname, kind, lines,
          signature, intro). Pass `full=True` for every section's full prose.
        - `show_source=True`, or `offset`/`limit`, or a file with no triefact, or a
          `path:LINE` cursor reference → raw line-numbered source.

        Use `grep`/`grep_symbol` to resolve a qname rather than hand-building one;
        a guessed qname returns `not_found` even when the source contains the symbol.

        `history=True` additionally surfaces the symbol's (or file's) intent
        trail from the session-digest archive — the chronological "why it
        changed" lines recorded at each commit. Ignored for raw source reads.
        """
        force_source = show_source or offset is not None or limit is not None

        # Explicit source mode: read bytes directly.
        if force_source:
            return self.read_source(self._strip_line_ref(path)[0], offset=offset, limit=limit)

        is_qname = _looks_like_qname(path)

        # A colon-bearing string is usually a qname, but a real on-disk file can
        # carry a colon and editors pass `path/to/file:LINE` cursor refs. Prefer
        # the file whenever one exists, so a file read never 404s into the graph.
        candidate, line_offset, line_limit = self._strip_line_ref(path)
        file_target = self._resolve_in_root(candidate)
        file_exists = file_target is not None and file_target.exists() and file_target.is_file()

        if is_qname and not file_exists:
            return self._read_symbol(path, history=history)

        # A `:LINE` (or `:START-END`) suffix on a real file → source window.
        if file_exists and line_offset is not None:
            return self.read_source(candidate, offset=line_offset, limit=line_limit)

        # File path: prefer the triefact view; fall back to raw source for
        # non-indexed files (configs, markdown, freshly added files).
        if file_exists or self._resolve_in_root(path) is not None:
            rel = candidate if file_exists else path
            view = self._triefact_view(rel, full=full, history=history)
            if view is not None:
                return view
            return self.read_source(rel if file_exists else path)

        # Neither a known file nor resolvable: treat as a qname so the agent
        # gets a structured not_found with a suggestion.
        return self._read_symbol(path, history=history)

    @staticmethod
    def _strip_line_ref(path: str) -> tuple[str, int | None, int | None]:
        """Split a trailing `:LINE` or `:START-END` cursor suffix off a path.

        Returns (path_without_suffix, offset, limit). When there's no numeric
        suffix, returns (path, None, None).
        """
        m = re.match(r"^(.*):(\d+)(?:-(\d+))?$", path)
        if m is None:
            return path, None, None
        start = int(m.group(2))
        limit = int(m.group(3)) - start + 1 if m.group(3) else 1
        return m.group(1), start, limit

    def _resolve_in_root(self, path: str) -> Path | None:
        """Resolve `path` to an absolute path under the project root, or None.

        None when the path escapes the root (so callers can refuse out-of-scope
        reads consistently with `read_source`).
        """
        target = Path(path)
        target = target.resolve() if target.is_absolute() else (self.root / path).resolve()
        if target == self.root or target.is_relative_to(self.root):
            return target
        return None

    def _triefact_view(
        self, file_path: str, *, full: bool, history: bool = False
    ) -> dict[str, Any] | None:
        """Render a file's triefact as compact (default) or full prose.

        Returns None when no triefact exists for the file (caller falls back to
        raw source). `file_path` is interpreted relative to the project root.
        """
        from trie.sync.writer import compact_triefact_view, render_for_agent

        target = self._resolve_in_root(file_path)
        if target is None:
            return None
        rel = (
            target.relative_to(self.root).as_posix()
            if target.is_relative_to(self.root)
            else file_path
        )
        triefact_path = self.triefacts_root / Path(rel).with_suffix(".md")
        if not triefact_path.exists():
            return None

        text = triefact_path.read_text()

        # Staleness banner: sections whose sentinel fingerprint no longer matches
        # the symbol's last-scan fingerprint are being served from outdated prose.
        # Prefixed into the output text so every renderer surfaces it verbatim.
        stale_qnames = self._stale_qnames_for_file(rel, text)
        banner = ""
        if stale_qnames:
            listed = ", ".join(sorted(stale_qnames)[:5])
            more = f" (+{len(stale_qnames) - 5} more)" if len(stale_qnames) > 5 else ""
            banner = (
                f"⚠ STALE PROSE: {len(stale_qnames)} section(s) predate the current "
                f"source — {listed}{more}. Run `trie sync` to refresh.\n\n"
            )

        if full:
            output = banner + render_for_agent(text)
            mode = "triefact_full"
        else:
            lines_by_qname: dict[str, str] = {}
            kind_by_qname: dict[str, str] = {}
            for row in self.store._conn.execute(
                "SELECT qualified_name, start_line, end_line, kind FROM symbols WHERE file_path = ?",
                (rel,),
            ).fetchall():
                lines_by_qname[row[0]] = f"{row[1]}-{row[2]}"
                kind_by_qname[row[0]] = row[3]
            output = banner + compact_triefact_view(
                text, rel, lines_by_qname=lines_by_qname, kind_by_qname=kind_by_qname
            )
            mode = "triefact_compact"

        if history:
            module_prefix = rel.rsplit(".", 1)[0]
            rows = self._digest_history(module_prefix=module_prefix)
            if rows:
                lines = ["", "## Recent changes (intent trail from the digest archive)", ""]
                for r in rows:
                    lines.append(f"- {r['date']} · {r['change']}")
                    lines.append(f"  ({r['title']})")
                output = output + "\n".join(lines) + "\n"

        tele_args = {"path": rel} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="read", args=tele_args) as tele_ctx:
            tele_ctx["mode"] = mode
            tele_ctx["result_kind"] = "ok"
            tele_ctx["response_bytes"] = len(output)
        result: dict[str, Any] = {"path": rel, "mode": mode, "output": output}
        # Surface staged-but-unapplied patches for symbols in THIS file. Without
        # this, a file read shows only the committed triefact — so an agent that
        # has batch-staged patches (and especially one re-reading after a partial
        # apply) sees no trace of its own pending work, concludes nothing
        # happened, and falls back to hand-editing. Mirror what _read_symbol
        # already does for qname reads, so the patch pipeline is visible through
        # the agent's primary lens (file reads).
        pending = self._pending_patches_for_file(rel)
        if pending:
            result["pending_patches"] = pending
            result["has_pending_patches"] = True
            result["notes"] = [
                f"{len(pending)} symbol(s) in this file have STAGED patches awaiting "
                "trie_patch_apply. Do NOT hand-edit them — run trie_patch_apply "
                "(or trie_patch_list to review, trie_patch_drop to discard)."
            ]
        else:
            result["has_pending_patches"] = False
        return result

    def _pending_patches_for_file(self, rel_path: str) -> list[dict[str, Any]]:
        """Pending patch + create notes for every symbol in `rel_path`.

        Used by the file-read view so staged work is visible on a file read, not
        just a qname read. Best-effort; returns [] on any store hiccup.
        """
        try:
            out: list[dict[str, Any]] = []
            # Edits to existing symbols: match patched qnames that live in this file.
            file_qnames = {
                row[0]
                for row in self.store._conn.execute(
                    "SELECT qualified_name FROM symbols WHERE file_path = ?", (rel_path,)
                ).fetchall()
            }
            for qn in self.store.get_patched_qnames():
                if qn not in file_qnames:
                    continue
                notes = self.store.get_patches_for_qname(qn)
                out.append(
                    {
                        "qname": qn,
                        "op": "patch",
                        "count": len(notes),
                        "notes": [n.get("note", "") for n in notes],
                    }
                )
            # New-symbol creates targeting this file.
            for group in self.store.get_create_patches_grouped().values():
                for c in group:
                    if c.get("target_file") == rel_path:
                        out.append(
                            {
                                "qname": c.get("target_qname", ""),
                                "op": "create",
                                "count": 1,
                                "notes": [c.get("note", "")],
                            }
                        )
            return out
        except Exception:
            return []

    def _read_symbol(self, qname: str, *, history: bool = False) -> dict[str, Any]:
        """Read a symbol's prose plus one-liners for every immediate caller and callee.

        Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
        Use after `grep` once you know which symbol you want to understand. If you
        need depth > 1, use `trace` and follow up with `read` on the nodes that matter.
        """
        tele_args = {"qname": qname} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="read", args=tele_args) as tele_ctx:
            detail = self.store.get_symbol_detail(qname)
            if detail is None:
                err = _error(
                    "not_found",
                    f"No symbol with qualified name {qname!r}.",
                    self._suggest_for_qname(qname),
                )
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err

            prose, prose_notes = self._prose_for(detail)
            prose_notes = self._staleness_notes(detail) + prose_notes

            callers_raw = self.store.references_in(qname)
            callees_raw = self.store.references_out(qname)

            callers, caller_truncated_note = self._neighbour_summaries(callers_raw)
            callees, callee_truncated_note = self._neighbour_summaries(callees_raw)

            notes: list[str] = []
            notes.extend(prose_notes)
            if caller_truncated_note:
                notes.append(caller_truncated_note)
            if callee_truncated_note:
                notes.append(callee_truncated_note)
            if detail.inbound_count > self.mcp_cfg.trace_hub_threshold:
                notes.append(
                    f"this symbol has {detail.inbound_count} inbound edges and is treated "
                    "as a hub; cascade expansion stops here."
                )

            out: dict[str, Any] = {
                "qname": detail.qualified_name,
                "signature": detail.signature or "",
                "prose": prose,
                "source_pointer": f"{detail.file_path}:{detail.start_line}-{detail.end_line}",
                "callers": callers,
                "callees": callees,
            }
            if history:
                out["history"] = self._digest_history(qname=detail.qualified_name)
            if detail.pending_patches:
                # Add origin tag to each patch (derived from session_id)
                tagged_patches = []
                for p in detail.pending_patches:
                    p_copy = dict(p)
                    sid = p_copy.get("session_id", "")
                    p_copy["origin"] = "cascade" if sid == "cascade" else "agent"
                    tagged_patches.append(p_copy)
                out["pending_patches"] = tagged_patches
                out["has_pending_patches"] = True
            else:
                out["has_pending_patches"] = False
            if notes:
                out["notes"] = notes
            tele_ctx["result_kind"] = "ok"
            tele_ctx["callers_count"] = len(callers)
            tele_ctx["callees_count"] = len(callees)
            tele_ctx["prose_chars"] = len(prose)
            tele_ctx["notes_count"] = len(notes)
            tele_ctx["response_bytes"] = len(json.dumps(out, default=str))
            if telemetry.capture_responses():
                tele_ctx["response"] = out
            return out

    def _digest_history(
        self, *, qname: str | None = None, module_prefix: str | None = None
    ) -> list[dict]:
        """Intent trail from the session-digest archive (newest first, capped).

        The archive stores every commit's intent keyed by qname; this is the
        wiki's "why is it like this" dimension, opt-in via `history=True` on
        the read/explain surfaces so the default token cost is unchanged.
        """
        from trie.session_diff import file_history, symbol_history

        diffs_dir = getattr(getattr(self.config, "diff", None), "diffs_dir", "") or (
            "triefacts/triediffs"
        )
        try:
            if qname is not None:
                return symbol_history(self.root, qname, diffs_dir=diffs_dir, limit=5)
            if module_prefix is not None:
                return file_history(self.root, module_prefix, diffs_dir=diffs_dir, limit=8)
        except Exception:
            return []
        return []

    def _stale_qnames_for_file(self, rel: str, triefact_text: str) -> set[str]:
        """Qnames in `rel` whose section fingerprint predates the last scan.

        Compares each sentinel's generation-time fingerprint against the symbols
        table (kept current by scan/refresh). Sections for symbols the graph no
        longer knows are ignored here — verify reports orphans separately.
        """
        from trie.sync.writer import SECTION_OPEN_RE

        current: dict[str, str] = {
            row[0]: row[1] or ""
            for row in self.store._conn.execute(
                "SELECT qualified_name, body_normalized_hash FROM symbols WHERE file_path = ?",
                (rel,),
            ).fetchall()
        }
        stale: set[str] = set()
        for match in SECTION_OPEN_RE.finditer(triefact_text):
            qname = match.group("symbol")
            fp_now = current.get(qname)
            if fp_now and (match.group("fp") or "") != fp_now:
                stale.add(qname)
        return stale

    def _section_fingerprint(self, detail: SymbolDetail) -> str | None:
        """Sentinel fingerprint of `detail`'s triefact section, or None when absent.

        This is the source fingerprint at prose-generation time; comparing it to
        `detail.fingerprint` (the last-scan fingerprint) detects stale prose.
        """
        from trie.sync.writer import SECTION_OPEN_RE

        triefact_path = self.triefacts_root / Path(detail.file_path).with_suffix(".md")
        if not triefact_path.exists():
            return None
        try:
            text = triefact_path.read_text()
        except OSError:
            return None
        for match in SECTION_OPEN_RE.finditer(text):
            if match.group("symbol") == detail.qualified_name:
                return match.group("fp") or ""
        return None

    def _staleness_notes(self, detail: SymbolDetail) -> list[str]:
        """Warnings when the prose being served no longer reflects the source.

        Two layers, cheapest first:

        1. Section-level: the sentinel fingerprint (stamped at generation time)
           differs from the symbol's last-scan fingerprint — the graph knows the
           source moved but the prose was never regenerated.
        2. File-level: the source file's current content hash differs from the
           store's file fingerprint — the *graph itself* is stale (no scan since
           the edit), so even a matching section fingerprint proves nothing.

        A read that serves stale prose without saying so is the worst failure a
        live wiki can have; these notes are the honesty layer.
        """
        notes: list[str] = []
        sec_fp = self._section_fingerprint(detail)
        if sec_fp is not None and detail.fingerprint and sec_fp != detail.fingerprint:
            notes.append(
                f"⚠ STALE PROSE: the source of {detail.qualified_name} changed after "
                "this prose was generated — run `trie sync` to refresh it."
            )
            return notes
        try:
            from trie.scan import file_fingerprint

            src = self.root / detail.file_path
            record = self.store.get_file(detail.file_path)
            if (
                record is not None
                and src.is_file()
                and file_fingerprint(src.read_text()) != record.fingerprint
            ):
                notes.append(
                    f"⚠ {detail.file_path} changed since the last graph refresh; "
                    "this prose may be stale — run `trie sync --graph-only`."
                )
        except OSError:
            pass
        return notes

    def _prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]:
        """Pull the section body verbatim from the triefact tree.

        Returns (prose, notes). When no triefact exists, prose is "" and a note explains
        why so the agent doesn't reason over silence.
        """
        rel_md = Path(detail.file_path).with_suffix(".md")
        triefact_path = self.triefacts_root / rel_md
        if not triefact_path.exists():
            return "", [
                f"no triefact exists for {detail.file_path}; prose is empty. "
                "run `trie sync` to generate one."
            ]

        # Avoid pulling TriefactFile (and yaml) here — a regex over the sentinels is
        # cheaper and what we actually want.
        from trie.sync.writer import SECTION_CLOSE, SECTION_OPEN_RE

        text = triefact_path.read_text()
        for match in SECTION_OPEN_RE.finditer(text):
            if match.group("symbol") != detail.qualified_name:
                continue
            close_idx = text.find(SECTION_CLOSE, match.end())
            if close_idx == -1:
                return "", [
                    f"section for {detail.qualified_name} in {triefact_path.name} is "
                    "missing its close sentinel; triefact may be corrupted."
                ]
            body = text[match.end() : close_idx]
            if body.startswith("\n"):
                body = body[1:]
            if body.endswith("\n"):
                body = body[:-1]
            return _truncate(body, self.mcp_cfg.read_prose_max_chars), []
        return "", [
            f"no section for {detail.qualified_name} in {triefact_path.name}; "
            "the triefact exists but this symbol hasn't been synced into it."
        ]

    def _neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]:
        """Resolve a list of qnames to compact neighbour records, with optional truncation.

        Returns (records, note_or_None). If the configured per-direction cap is hit,
        the records are truncated and a note describes the cut.
        """
        cap = self.mcp_cfg.read_max_neighbours_per_direction
        total = len(qnames)
        truncated_note: str | None = None
        if cap > 0 and total > cap:
            qnames = qnames[:cap]
            truncated_note = (
                f"showed {cap} of {total} neighbours; use trace(direction=...) "
                "for the full topology."
            )

        records: list[dict[str, Any]] = []
        for q in qnames:
            d = self.store.get_symbol_detail(q)
            if d is None:
                # Symbol was deleted between scan and query; skip.
                continue
            records.append(
                _symbol_summary(d, one_liner_max=self.mcp_cfg.read_neighbour_one_liner_max_chars)
            )
        return records, truncated_note

    # --- trace -------------------------------------------------------------

    def trace(
        self,
        from_qname: str,
        direction: str = "callers",
        depth: int = 2,
    ) -> dict[str, Any]:
        """Trace the call graph from `from_qname` outward up to `depth` hops.

        `direction` is one of `"callers"`, `"callees"`, or `"both"`. Each edge is
        tagged with its direction relative to the starting symbol (`"in"` = caller-side,
        `"out"` = callee-side). Expansion stops at hub symbols (inbound count above the
        configured threshold); their qnames appear in `truncated_at`.

        Returns signatures and one-liners only — for prose, follow up with `read`
        on a specific node.
        """
        tele_args = (
            {"from_qname": from_qname, "direction": direction, "depth": depth}
            if telemetry.capture_args()
            else {}
        )
        tele_ctx_outer = telemetry.timed(self.event_name, tool="trace", args=tele_args)
        with tele_ctx_outer as tele_ctx:
            if direction not in ("callers", "callees", "both"):
                err = _error(
                    "invalid_argument",
                    f"`direction` must be one of callers/callees/both, got {direction!r}.",
                )
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err
            root_detail = self.store.get_symbol_detail(from_qname)
            if root_detail is None:
                err = _error(
                    "not_found",
                    f"No symbol with qualified name {from_qname!r}.",
                    self._suggest_for_qname(from_qname),
                )
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err

            notes: list[str] = []
            requested_depth = depth
            depth = max(0, min(depth, self.mcp_cfg.trace_max_depth))
            if depth != requested_depth:
                notes.append(f"depth was clamped from {requested_depth} to {depth} (server max).")

            nodes: dict[str, dict[str, Any]] = {}
            edges: list[dict[str, str]] = []
            truncated_at: list[str] = []
            max_nodes = self.mcp_cfg.trace_max_nodes
            hub_threshold = self.mcp_cfg.trace_hub_threshold
            one_liner_cap = self.mcp_cfg.read_neighbour_one_liner_max_chars

            patched_qnames: set[str] = set(self.store.get_patched_qnames())

            def add_node(detail: SymbolDetail) -> bool:
                """Register a node if it fits under max_nodes. False on capacity hit."""
                if detail.qualified_name in nodes:
                    return True
                if len(nodes) >= max_nodes:
                    return False
                qn = detail.qualified_name
                nodes[qn] = {
                    "signature": detail.signature or "",
                    "one_liner": _truncate(detail.one_liner, one_liner_cap),
                }
                if qn in patched_qnames:
                    nodes[qn]["has_pending_patches"] = True
                return True

            add_node(root_detail)

            # BFS frontier carries (qname, current_hop) so we know when to stop expanding.
            queue: deque[tuple[str, int]] = deque([(root_detail.qualified_name, 0)])
            visited: set[str] = {root_detail.qualified_name}
            capacity_hit = False

            while queue:
                qname, hop = queue.popleft()
                if hop >= depth:
                    continue
                detail = self.store.get_symbol_detail(qname)
                if detail is None:
                    continue
                # Hub guard: skip outward expansion *through* a hub. The hub itself is
                # already a node; we just don't pull its neighbours into the result.
                if qname != root_detail.qualified_name and detail.inbound_count > hub_threshold:
                    if qname not in truncated_at:
                        truncated_at.append(qname)
                    continue

                outbound_qnames: list[tuple[str, str]] = []  # (neighbour_qname, edge_direction)
                if direction in ("callers", "both"):
                    for src in self.store.references_in(qname):
                        outbound_qnames.append((src, "in"))
                if direction in ("callees", "both"):
                    for dst in self.store.references_out(qname):
                        outbound_qnames.append((dst, "out"))

                for neighbour, edge_dir in outbound_qnames:
                    # Edge: oriented relative to root. "in" = neighbour calls qname, etc.
                    edge = (
                        {"from": neighbour, "to": qname}
                        if edge_dir == "in"
                        else {
                            "from": qname,
                            "to": neighbour,
                        }
                    )
                    edge_record = {**edge, "direction": edge_dir}
                    if edge_record not in edges:
                        edges.append(edge_record)

                    if neighbour in visited:
                        continue
                    neighbour_detail = self.store.get_symbol_detail(neighbour)
                    if neighbour_detail is None:
                        continue
                    if not add_node(neighbour_detail):
                        capacity_hit = True
                        continue
                    visited.add(neighbour)
                    queue.append((neighbour, hop + 1))

            if capacity_hit:
                notes.append(
                    f"trace reached max_nodes={max_nodes}; result is BFS-ordered from root."
                )

            result: dict[str, Any] = {
                "root": {
                    "qname": root_detail.qualified_name,
                    "signature": root_detail.signature or "",
                    "one_liner": _truncate(root_detail.one_liner, one_liner_cap),
                },
                "nodes": nodes,
                "edges": edges,
            }
            if root_detail.qualified_name in patched_qnames:
                result["root"]["has_pending_patches"] = True
            if truncated_at:
                result["truncated_at"] = truncated_at
            if notes:
                result["notes"] = notes
            tele_ctx["result_kind"] = "ok"
            tele_ctx["nodes_count"] = len(nodes)
            tele_ctx["edges_count"] = len(edges)
            tele_ctx["truncated_at_count"] = len(truncated_at)
            tele_ctx["notes_count"] = len(notes)
            tele_ctx["response_bytes"] = len(json.dumps(result, default=str))
            if telemetry.capture_responses():
                tele_ctx["response"] = result
            return result

    # --- extended toolset --------------------------------------------------

    def grep_str(self, regexp: str) -> dict[str, Any]:
        """Search source bodies with a regex; attribute matched lines to their enclosing symbols.

        Unlike `grep` (which searches symbol names), this searches the raw source text using
        ripgrep with full regex support, then maps each matched line back to the smallest
        enclosing symbol. Returns a flat list of symbol hits with signature and one-liner —
        no JSON envelope, just what the agent needs to act.

        Returns `{hits: [{qname, signature, file_pointer, one_liner, match_count}]}`.
        """
        tele_args = {"regexp": regexp} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="grep_str", args=tele_args) as tele_ctx:
            if not regexp or not regexp.strip():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", "`regexp` must be a non-empty string.")

            proc = __import__("subprocess").run(
                [
                    self.rg_path,
                    "--json",
                    "--line-number",
                    "--ignore-case",
                    "--no-messages",
                    "--",
                    regexp,
                    str(self.src_root),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode not in (0, 1):
                tele_ctx["result_kind"] = "error"
                return _error(
                    "internal", f"rg failed (exit {proc.returncode}): {proc.stderr.strip()}"
                )

            import json as _json

            scope_set: set[str] = set()
            for abs_path in __import__("trie.scope", fromlist=["discover_files"]).discover_files(
                self.root, self.config.scope
            ):
                if abs_path.is_relative_to(self.src_root):
                    scope_set.add(str(abs_path.relative_to(self.src_root)))

            rg_hits: dict[str, list[int]] = {}
            src_root_str = str(self.src_root)
            for raw_line in proc.stdout.splitlines():
                if not raw_line:
                    continue
                try:
                    event = _json.loads(raw_line)
                except _json.JSONDecodeError:
                    continue
                if event.get("type") != "match":
                    continue
                data = event.get("data") or {}
                path_obj = data.get("path") or {}
                abs_path_str = path_obj.get("text")
                lineno = data.get("line_number")
                if not isinstance(abs_path_str, str) or not isinstance(lineno, int):
                    continue
                if not abs_path_str.startswith(src_root_str):
                    continue
                rel = abs_path_str[len(src_root_str) :].lstrip("/")
                if rel not in scope_set:
                    continue
                rg_hits.setdefault(rel, []).append(lineno)

            per_symbol = self._attribute_text_matches_to_symbols(rg_hits)
            if not per_symbol:
                # rg found nothing — try fuzzy scoring against symbol names and
                # one_liners using the regexp string as the query.  This handles
                # the common case where the user typed a function name slightly
                # wrong (e.g. "slugufy") or used a description rather than an
                # exact identifier.
                cutoff = self.mcp_cfg.fuzzy_cutoff
                pre_filter = self.mcp_cfg.fuzzy_prose_pre_filter
                prose_weight = self.mcp_cfg.fuzzy_prose_weight
                all_syms = self.store.grep_symbols(
                    GrepPredicate(),
                    rank_by="public_first",
                    limit=self.mcp_cfg.grep_max_limit * 10,
                )
                scored_str: list[tuple[float, SymbolDetail]] = []
                for sym in all_syms:
                    local_name = (
                        sym.qualified_name.split(":")[-1]
                        if ":" in sym.qualified_name
                        else sym.qualified_name
                    )
                    pre_score = max(
                        _fuzzy_score(regexp, local_name),
                        _fuzzy_score(regexp, sym.one_liner or "") * 0.8,
                    )
                    prose = ""
                    if pre_score >= pre_filter:
                        prose, _ = self._prose_for(sym)
                    score = _score_sym(regexp, sym, prose=prose, prose_weight=prose_weight)
                    if score >= cutoff:
                        scored_str.append((score, sym))

                tele_ctx["result_kind"] = "ok"
                tele_ctx["result_count"] = 0
                if not scored_str:
                    return {
                        "hits": [],
                        "note": f"No matches for {regexp!r} in any indexed symbol body.",
                    }
                scored_str.sort(key=lambda x: (-x[0], x[1].inbound_count))
                one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
                fuzzy_hits = [
                    {
                        "qname": sym.qualified_name,
                        "signature": sym.signature or "",
                        "file_pointer": f"{sym.file_path}:{sym.start_line}",
                        "one_liner": _truncate(sym.one_liner, one_liner_cap),
                        "score": round(score, 1),
                    }
                    for score, sym in scored_str[:10]
                ]
                return {
                    "hits": [],
                    "fallback": {
                        "kind": "fuzzy_one_liner",
                        "matches": fuzzy_hits,
                        "note": (
                            f"No regex matches for {regexp!r}. "
                            "These symbols were found by fuzzy-matching the "
                            "pattern against symbol names, one_liners, and "
                            "triefact prose. Ranked by relevance score descending."
                        ),
                    },
                }

            candidates = sorted(
                ((self.store.get_symbol_detail(q), c) for q, c in per_symbol.items()),
                key=lambda x: (
                    -(x[0].inbound_count if x[0] else 0),
                    x[0].qualified_name if x[0] else "",
                ),
            )
            one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
            hits = [
                {
                    "qname": d.qualified_name,
                    "signature": d.signature or "",
                    "file_pointer": f"{d.file_path}:{d.start_line}",
                    "one_liner": _truncate(d.one_liner, one_liner_cap),
                    "match_count": count,
                }
                for d, count in candidates
                if d is not None
            ]
            result: dict[str, Any] = {"hits": hits}
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hits)
            tele_ctx["response_bytes"] = len(_json.dumps(result, default=str))
            return result

    def grep_str_all(self, regexp: str) -> dict[str, Any]:
        """Regex search across the WHOLE repo, not just indexed source bodies.

        EXT-1: `grep_str` only sees in-scope (indexed) files; this variant runs
        gitignore-aware ripgrep over the entire project root so non-indexed
        files (TS/JS, configs, docs, lockfiles) are searchable too. In-scope
        hits are still attributed to their enclosing symbol; out-of-scope hits
        come back as plain `file:line:text` rows under `text_hits`.

        Returns `{hits: [...symbol hits...], text_hits: [{file, line, text}],
        text_match_count}`.
        """
        import json as _json
        import subprocess as _subprocess

        tele_args = {"regexp": regexp} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="grep_str_all", args=tele_args) as tele_ctx:
            if not regexp or not regexp.strip():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", "`regexp` must be a non-empty string.")

            proc = _subprocess.run(
                [
                    self.rg_path,
                    "--json",
                    "--line-number",
                    "--ignore-case",
                    "--no-messages",
                    "--",
                    regexp,
                    str(self.root),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            if proc.returncode not in (0, 1):
                tele_ctx["result_kind"] = "error"
                return _error(
                    "internal", f"rg failed (exit {proc.returncode}): {proc.stderr.strip()}"
                )

            # Build the set of in-scope relative paths (relative to src_root) so
            # we can split hits into "attributable to a symbol" vs "plain text".
            scope_set: set[str] = set()
            for abs_path in __import__("trie.scope", fromlist=["discover_files"]).discover_files(
                self.root, self.config.scope
            ):
                if abs_path.is_relative_to(self.src_root):
                    scope_set.add(str(abs_path.relative_to(self.src_root)))

            src_root_str = str(self.src_root)
            root_str = str(self.root)
            rg_hits: dict[str, list[int]] = {}
            text_hits: list[dict[str, Any]] = []
            text_cap = 100
            for raw_line in proc.stdout.splitlines():
                if not raw_line:
                    continue
                try:
                    event = _json.loads(raw_line)
                except _json.JSONDecodeError:
                    continue
                if event.get("type") != "match":
                    continue
                data = event.get("data") or {}
                abs_path_str = (data.get("path") or {}).get("text")
                lineno = data.get("line_number")
                if not isinstance(abs_path_str, str) or not isinstance(lineno, int):
                    continue
                # In-scope, indexed → attribute to a symbol.
                if abs_path_str.startswith(src_root_str):
                    rel = abs_path_str[len(src_root_str) :].lstrip("/")
                    if rel in scope_set:
                        rg_hits.setdefault(rel, []).append(lineno)
                        continue
                # Otherwise it's an out-of-scope text hit.
                if len(text_hits) < text_cap:
                    rel_repo = (
                        abs_path_str[len(root_str) :].lstrip("/")
                        if abs_path_str.startswith(root_str)
                        else abs_path_str
                    )
                    line_text = ((data.get("lines") or {}).get("text") or "").rstrip("\n")
                    text_hits.append({"file": rel_repo, "line": lineno, "text": line_text[:300]})

            per_symbol = self._attribute_text_matches_to_symbols(rg_hits)
            candidates = sorted(
                ((self.store.get_symbol_detail(q), c) for q, c in per_symbol.items()),
                key=lambda x: (
                    -(x[0].inbound_count if x[0] else 0),
                    x[0].qualified_name if x[0] else "",
                ),
            )
            one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
            hits = [
                {
                    "qname": d.qualified_name,
                    "signature": d.signature or "",
                    "file_pointer": f"{d.file_path}:{d.start_line}",
                    "one_liner": _truncate(d.one_liner, one_liner_cap),
                    "match_count": count,
                }
                for d, count in candidates
                if d is not None
            ]
            result = {
                "hits": hits,
                "text_hits": text_hits,
                "text_match_count": len(text_hits),
            }
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hits) + len(text_hits)
            return result

    def read_source(
        self, path: str, offset: int | None = None, limit: int | None = None
    ) -> dict[str, Any]:
        """Read raw source of an ARBITRARY file (EXT-3/EXT-4), indexed or not.

        `read` is qname/triefact-centric and only covers indexed files; this
        returns the raw bytes of any path under the project root with optional
        1-indexed `offset` + `limit` windowing, line-number prefixed
        (`<n>: <text>`), matching stock editor read semantics. Long lines are
        clipped at 2000 chars.

        Returns `{path, lines: "<numbered text>", line_count, offset, more}`.
        """
        tele_args = {"path": path} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="read_source", args=tele_args) as tele_ctx:
            target = Path(path)
            target = target.resolve() if target.is_absolute() else (self.root / path).resolve()
            # Keep reads inside the project root.
            if not (target == self.root or target.is_relative_to(self.root)):
                tele_ctx["result_kind"] = "error"
                return _error(
                    "out_of_scope",
                    f"{path!r} is outside the project root.",
                    "read_source only serves files under the trie project root.",
                )
            if not target.exists():
                tele_ctx["result_kind"] = "error"
                return _error("not_found", f"No file at {path!r}.")
            if target.is_dir():
                tele_ctx["result_kind"] = "error"
                return _error(
                    "invalid_argument",
                    f"{path!r} is a directory; use `find` to list its contents.",
                )
            try:
                text = target.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                tele_ctx["result_kind"] = "error"
                return _error("internal", f"could not read {path!r}: {exc}")

            all_lines = text.split("\n")
            start = max(0, (offset - 1)) if offset else 0
            end = (start + limit) if limit else len(all_lines)
            sliced = all_lines[start:end]
            numbered = "\n".join(
                f"{start + i + 1}: {(line[:2000] if len(line) > 2000 else line)}"
                for i, line in enumerate(sliced)
            )
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(sliced)
            return {
                "path": target.relative_to(self.root).as_posix()
                if target.is_relative_to(self.root)
                else str(target),
                "lines": numbered,
                "line_count": len(sliced),
                "offset": start + 1,
                "more": end < len(all_lines),
            }

    def write_file(self, path: str, content: str, overwrite: bool = False) -> dict[str, Any]:
        """Create or overwrite a file under the project root (EXT-8).

        Fills the gap where `create_symbol` only adds a Python symbol to an
        existing indexed file — this writes an ARBITRARY new file (configs,
        docs, scripts, a fresh module). Parent directories are created. Refuses
        to clobber an existing file unless `overwrite=True`.

        If the written path is in trie's scope (an indexed file type), the
        response flags `needs_sync=True` — the caller should run a sync/refresh
        so the new file enters the graph (incremental in-process indexing is
        intentionally left to the sync pipeline to keep the graph consistent).

        Returns `{path, bytes_written, created, needs_sync}`.
        """
        tele_args = {"path": path} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="write_file", args=tele_args) as tele_ctx:
            target = Path(path)
            target = target.resolve() if target.is_absolute() else (self.root / path).resolve()
            if not (target == self.root or target.is_relative_to(self.root)):
                tele_ctx["result_kind"] = "error"
                return _error(
                    "out_of_scope",
                    f"{path!r} is outside the project root.",
                    "write_file only writes under the trie project root.",
                )
            if target.is_dir():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", f"{path!r} is a directory.")
            existed = target.exists()
            if existed and not overwrite:
                tele_ctx["result_kind"] = "error"
                return _error(
                    "invalid_argument",
                    f"{path!r} already exists. Pass overwrite=true to replace it, "
                    "or use the patch pipeline to change indexed code.",
                )
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")
            except OSError as exc:
                tele_ctx["result_kind"] = "error"
                return _error("internal", f"could not write {path!r}: {exc}")

            from trie.scope import _matches

            rel = (
                target.relative_to(self.root).as_posix()
                if target.is_relative_to(self.root)
                else str(target)
            )
            in_scope = any(_matches(rel, pat) for pat in self.config.scope.include) and not any(
                _matches(rel, pat) for pat in self.config.scope.exclude
            )
            tele_ctx["result_kind"] = "ok"
            return {
                "path": rel,
                "bytes_written": len(content.encode("utf-8")),
                "created": not existed,
                "needs_sync": in_scope,
            }

    def find_files(self, pattern: str, all_files: bool = True, limit: int = 100) -> dict[str, Any]:
        """Find files by name/path glob (EXT-2). Fills the gap where trie has no
        filename search — only symbol search.

        With `all_files=True` (default) the match runs over the whole project
        tree (respecting scope excludes so vendored/`.venv`/`node_modules`
        subtrees are skipped); with `all_files=False` it restricts to indexed
        files. Results are mtime-sorted (newest first) and capped at `limit`.

        `pattern` uses glob semantics, e.g. `**/*.ts`, `Dockerfile`,
        `src/**/*.tsx`. A bare name like `config.json` matches that basename
        anywhere in the tree.

        Returns `{matches: [path, ...], match_count, truncated}`.
        """
        import os as _os

        tele_args = {"pattern": pattern} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="find_files", args=tele_args) as tele_ctx:
            if not pattern or not pattern.strip():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", "`pattern` must be a non-empty string.")

            from trie.scope import _matches, discover_files

            root = self.root
            if all_files:
                # Walk the tree, pruning excluded dirs, matching the glob against
                # each relative path (and its basename for bare-name patterns).
                bare = "/" not in pattern and "*" not in pattern
                candidates: list[Path] = []
                excludes = self.config.scope.exclude
                for dirpath, dirnames, filenames in _os.walk(root, topdown=True):
                    abs_dir = Path(dirpath)
                    rel_dir = abs_dir.relative_to(root).as_posix()
                    kept: list[str] = []
                    for d in dirnames:
                        child_rel = d if rel_dir == "." else f"{rel_dir}/{d}"
                        if any(_matches(child_rel + "/x", pat) for pat in excludes) or d in {
                            ".git",
                            ".trie",
                        }:
                            continue
                        kept.append(d)
                    dirnames[:] = kept
                    for fname in filenames:
                        rel = fname if rel_dir == "." else f"{rel_dir}/{fname}"
                        if bare:
                            if fname == pattern:
                                candidates.append(root / rel)
                        elif _matches(rel, pattern):
                            candidates.append(root / rel)
            else:
                candidates = [
                    p
                    for p in discover_files(root, self.config.scope)
                    if _matches(p.relative_to(root).as_posix(), pattern)
                ]

            # Sort by mtime descending (mirror stock glob), cap at limit.
            def _mtime(p: Path) -> float:
                try:
                    return p.stat().st_mtime
                except OSError:
                    return 0.0

            candidates.sort(key=_mtime, reverse=True)
            truncated = len(candidates) > limit
            matches = [p.relative_to(root).as_posix() for p in candidates[:limit]]
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(matches)
            return {"matches": matches, "match_count": len(matches), "truncated": truncated}

    def grep_entry_points(self, query: str) -> dict[str, Any]:
        """Find architectural entry points (high inbound-count public symbols) whose
        triefact prose fuzzy-matches `query`.

        Use this when orienting in an unfamiliar codebase or looking for the main
        path that handles a concept.

        Hits are sorted by **descending relevance score first, then ascending
        inbound-count** — so the most focused/niche entry point for the concept
        ranks above a sprawling utility hub with the same relevance. This gives
        both "closest textual match" and "lowest inbound" simultaneously: you see
        the most specific match at the top rather than the most-wired one.

        Returns `{hits: [{qname, signature, file_pointer, one_liner, inbound_count,
        prose_snippet, score}]}`.
        """
        tele_args = {"query": query} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="grep_entry_points", args=tele_args) as tele_ctx:
            if not query or not query.strip():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", "`query` must be a non-empty string.")

            # Pull public hubs as the candidate pool. Test symbols are
            # excluded outright — a fixture referenced by two tests is not an
            # architectural entry point, and with tests in the pool this tool
            # degenerated into generic prose grep over test files. Fetch a
            # deeper page than we keep so the post-filter doesn't starve the
            # pool on test-heavy repos.
            pred = GrepPredicate(public_only=True, inbound_count_min=2)
            raw_candidates = self.store.grep_symbols(
                pred, rank_by="inbound_count", limit=self.mcp_cfg.grep_max_limit * 3
            )
            candidates = [s for s in raw_candidates if not _is_test_symbol(s)][
                : self.mcp_cfg.grep_max_limit
            ]

            cutoff = self.mcp_cfg.fuzzy_cutoff
            pre_filter = self.mcp_cfg.fuzzy_prose_pre_filter
            prose_weight = self.mcp_cfg.fuzzy_prose_weight

            scored: list[tuple[float, Any, str]] = []
            for sym in candidates:
                # First pass: score on name + one_liner only (no disk I/O).
                local_name = (
                    sym.qualified_name.split(":")[-1]
                    if ":" in sym.qualified_name
                    else sym.qualified_name
                )
                name_score = _fuzzy_score(query, local_name)
                liner_score = _fuzzy_score(query, sym.one_liner or "") * 0.8
                pre_score = max(name_score, liner_score)

                # Lazy prose read: only pay disk cost if pre-filter clears.
                prose = ""
                if pre_score >= pre_filter:
                    prose, _ = self._prose_for(sym)

                score = _score_sym(query, sym, prose=prose, prose_weight=prose_weight)
                if score < cutoff:
                    continue
                scored.append((score, sym, prose))

            # Primary sort: relevance DESC; secondary: inbound_count ASC so the
            # most focused/niche entry point floats above sprawling hubs at
            # the same relevance level — achieving "closest match + lowest inbound"
            # in a single sorted list.
            scored.sort(key=lambda x: (-x[0], x[1].inbound_count))

            one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars
            hits = []
            for score, sym, prose in scored[:20]:
                prose_snippet = prose[:300].rstrip()
                if len(prose) > 300:
                    prose_snippet += "…"
                hits.append(
                    {
                        "qname": sym.qualified_name,
                        "signature": sym.signature or "",
                        "file_pointer": f"{sym.file_path}:{sym.start_line}",
                        "one_liner": _truncate(sym.one_liner, one_liner_cap),
                        "inbound_count": sym.inbound_count,
                        "prose_snippet": prose_snippet,
                        "score": round(score, 1),
                    }
                )

            result: dict[str, Any] = {"hits": hits}
            if not hits:
                result["note"] = f"No entry-point symbols found matching {query!r}."
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hits)
            return result

    def grep_symbol(self, sym: str) -> dict[str, Any]:
        """Fuzzy symbol name lookup. Returns the best-matching symbol's full metadata
        plus a `similar` list of other close matches.

        Uses rapidfuzz WRatio scoring across symbol names, one_liners, and (lazily)
        triefact prose bodies so typos, partial names, and conceptual descriptions all
        resolve correctly. Each result carries a `score` field (0-100) so callers can
        see why a symbol ranked first.

        Use when you have a rough name but aren't sure of the exact qname. Better than
        `grep` for typo-tolerance and for discovering related symbols in one call.

        Returns `{match: {qname, kind, signature, file_pointer, one_liner, inbound_count,
        outbound_count, score}, similar: [...]}`.
        """
        tele_args = {"sym": sym} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="grep_symbol", args=tele_args) as tele_ctx:
            if not sym or not sym.strip():
                tele_ctx["result_kind"] = "error"
                return _error("invalid_argument", "`sym` must be a non-empty string.")

            cutoff = self.mcp_cfg.fuzzy_cutoff
            pre_filter = self.mcp_cfg.fuzzy_prose_pre_filter
            prose_weight = self.mcp_cfg.fuzzy_prose_weight

            # --- Phase 1: substring SQL hit -----------------------------------
            # Pull up to 20 candidates via the fast SQL LIKE path, then
            # re-rank by rapidfuzz score so the closest match leads.
            sql_hits = self.store.grep_symbols(
                GrepPredicate(name_contains=sym), rank_by="public_first", limit=20
            )

            # --- Phase 2: fuzzy name fallback ---------------------------------
            # When SQL finds nothing, ask rapidfuzz to find close names from
            # the full symbol roster. Cutoff 45 (vs old difflib 0.6 ≈ 60) to
            # catch short-name typos better.
            if not sql_hits:
                all_names = self.store.all_symbol_names()
                close_hits = _process.extract(
                    sym, all_names, scorer=_fuzz.WRatio, limit=10, score_cutoff=cutoff
                )
                if not close_hits:
                    tele_ctx["result_kind"] = "error"
                    return _error(
                        "not_found",
                        f"No symbol matching {sym!r}.",
                        "Use grep_str to search source bodies instead.",
                    )
                sql_hits = []
                for name, _score, _idx in close_hits:
                    sql_hits.extend(
                        self.store.grep_symbols(
                            GrepPredicate(name_contains=name), rank_by="public_first", limit=3
                        )
                    )

            # --- Phase 3: prose augmentation + final scoring ------------------
            # Score each candidate with name + one_liner first (free).
            # Lazily read prose for those that clear the pre-filter.
            scored: list[tuple[float, SymbolDetail]] = []
            seen: set[str] = set()
            for h in sql_hits:
                if h.qualified_name in seen:
                    continue
                seen.add(h.qualified_name)
                local_name = (
                    h.qualified_name.split(":")[-1] if ":" in h.qualified_name else h.qualified_name
                )
                pre_score = max(
                    _fuzzy_score(sym, local_name),
                    _fuzzy_score(sym, h.one_liner or "") * 0.8,
                )
                prose = ""
                if pre_score >= pre_filter:
                    prose, _ = self._prose_for(h)
                score = _score_sym(sym, h, prose=prose, prose_weight=prose_weight)
                scored.append((score, h))

            # Score desc, then production before tests, then shorter local
            # names (a tie between `write_stamp` and anything longer should
            # resolve to the exact name), then qname for determinism. Before
            # these tie-breaks, ties fell through to SQL order — ASCII qname
            # sorting — which is how `tests/…` beat `trie/…` for months.
            scored.sort(
                key=lambda x: (
                    -x[0],
                    _is_test_symbol(x[1]),
                    len(x[1].qualified_name.split(":")[-1]),
                    x[1].qualified_name,
                )
            )

            one_liner_cap = self.mcp_cfg.grep_one_liner_max_chars

            def _sym_dict(d: SymbolDetail, s: float) -> dict[str, Any]:
                return {
                    "qname": d.qualified_name,
                    "kind": d.kind,
                    "signature": d.signature or "",
                    "file_pointer": f"{d.file_path}:{d.start_line}",
                    "one_liner": _truncate(d.one_liner, one_liner_cap),
                    "inbound_count": d.inbound_count,
                    "outbound_count": d.outbound_count,
                    "score": round(s, 1),
                }

            best_score, best = scored[0]
            result: dict[str, Any] = {
                "match": _sym_dict(best, best_score),
                "similar": [_sym_dict(h, s) for s, h in scored[1:10]],
            }
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(scored)
            return result

    def grep_symbol_and_neighbours(self, sym: str) -> dict[str, Any]:
        """Like `grep_symbol` but also returns trimmed triefact metadata for the
        best match's immediate callers and callees.

        Use when you want to orient around a symbol without making a separate
        `read` call — one round trip for the symbol + its neighbourhood.

        Returns `{match: {...}, similar: [...], callers: [...], callees: [...]}`.
        """
        tele_args = {"sym": sym} if telemetry.capture_args() else {}
        with telemetry.timed(
            self.event_name, tool="grep_symbol_and_neighbours", args=tele_args
        ) as tele_ctx:
            base = self.grep_symbol(sym)
            if "error" in base:
                tele_ctx["result_kind"] = "error"
                return base

            best_qname: str = base["match"]["qname"]
            callers_raw = self.store.references_in(best_qname)
            callees_raw = self.store.references_out(best_qname)
            callers, _ = self._neighbour_summaries(callers_raw)
            callees, _ = self._neighbour_summaries(callees_raw)
            result: dict[str, Any] = {**base, "callers": callers, "callees": callees}
            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = 1
            return result

    def explain_symbol(self, sym: str, history: bool = False) -> dict[str, Any]:
        """Full prose for a symbol plus a joined narrative story that weaves together
        the prose of its callers and callees into a single readable explanation.

        Use when you want to deeply understand a symbol and how it fits into the
        system — not just its own docstring but the story of what calls it and
        what it calls.

        Returns `{qname, signature, source_pointer, prose, story, callers, callees, notes?}`.
        """
        tele_args = {"sym": sym} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="explain_symbol", args=tele_args) as tele_ctx:
            # Resolve sym to a qname if needed.
            detail = self.store.get_symbol_detail(sym)
            if detail is None:
                # Try fuzzy resolution.
                base = self.grep_symbol(sym)
                if "error" in base:
                    tele_ctx["result_kind"] = "error"
                    return _error(
                        "not_found", f"No symbol matching {sym!r}.", self._suggest_for_qname(sym)
                    )
                sym = base["match"]["qname"]
                detail = self.store.get_symbol_detail(sym)
                if detail is None:
                    tele_ctx["result_kind"] = "error"
                    return _error(
                        "not_found",
                        f"No symbol with qualified name {sym!r}.",
                        self._suggest_for_qname(sym),
                    )

            prose, prose_notes = self._prose_for(detail)
            prose_notes = self._staleness_notes(detail) + prose_notes
            callers_raw = self.store.references_in(detail.qualified_name)
            callees_raw = self.store.references_out(detail.qualified_name)
            callers, _ = self._neighbour_summaries(callers_raw)
            callees, _ = self._neighbour_summaries(callees_raw)

            # Build a joined narrative story.
            story_parts: list[str] = []
            if callees_raw:
                callee_lines: list[str] = []
                for q in callees_raw[:5]:
                    d = self.store.get_symbol_detail(q)
                    if d is None:
                        continue
                    p, _ = self._prose_for(d)
                    snippet = p.split("\n\n")[0].strip() if p else d.one_liner
                    if snippet:
                        callee_lines.append(f"- **{d.qualified_name}**: {snippet}")
                if callee_lines:
                    story_parts.append("**Calls into:**\n" + "\n".join(callee_lines))
            if callers_raw:
                caller_lines: list[str] = []
                for q in callers_raw[:5]:
                    d = self.store.get_symbol_detail(q)
                    if d is None:
                        continue
                    p, _ = self._prose_for(d)
                    snippet = p.split("\n\n")[0].strip() if p else d.one_liner
                    if snippet:
                        caller_lines.append(f"- **{d.qualified_name}**: {snippet}")
                if caller_lines:
                    story_parts.append("**Called by:**\n" + "\n".join(caller_lines))

            story = "\n\n".join(story_parts) if story_parts else ""

            out: dict[str, Any] = {
                "qname": detail.qualified_name,
                "signature": detail.signature or "",
                "source_pointer": f"{detail.file_path}:{detail.start_line}-{detail.end_line}",
                "prose": prose,
                "story": story,
                "callers": callers,
                "callees": callees,
            }
            if history:
                out["history"] = self._digest_history(qname=detail.qualified_name)
            if prose_notes:
                out["notes"] = prose_notes
            tele_ctx["result_kind"] = "ok"
            tele_ctx["prose_chars"] = len(prose)
            tele_ctx["story_chars"] = len(story)
            return out

    def explain_symbol_references(self, sym: str, history: bool = False) -> dict[str, Any]:
        """Explain how a symbol is used — callers only, with their prose.

        Use when you want to understand the call sites of a symbol: who uses it,
        in what context, and with what intent. Skips the symbol's own prose and
        focuses entirely on the usage story.

        Returns `{qname, signature, source_pointer, usage_story, callers}`.
        """
        tele_args = {"sym": sym} if telemetry.capture_args() else {}
        with telemetry.timed(
            self.event_name, tool="explain_symbol_references", args=tele_args
        ) as tele_ctx:
            detail = self.store.get_symbol_detail(sym)
            if detail is None:
                base = self.grep_symbol(sym)
                if "error" in base:
                    tele_ctx["result_kind"] = "error"
                    return _error(
                        "not_found", f"No symbol matching {sym!r}.", self._suggest_for_qname(sym)
                    )
                sym = base["match"]["qname"]
                detail = self.store.get_symbol_detail(sym)
                if detail is None:
                    tele_ctx["result_kind"] = "error"
                    return _error(
                        "not_found",
                        f"No symbol with qualified name {sym!r}.",
                        self._suggest_for_qname(sym),
                    )

            callers_raw = self.store.references_in(detail.qualified_name)
            callers, _ = self._neighbour_summaries(callers_raw)

            usage_lines: list[str] = []
            for q in callers_raw[:8]:
                d = self.store.get_symbol_detail(q)
                if d is None:
                    continue
                p, _ = self._prose_for(d)
                snippet = p.split("\n\n")[0].strip() if p else d.one_liner
                if snippet:
                    usage_lines.append(
                        f"**{d.qualified_name}** ({d.file_path}:{d.start_line}): {snippet}"
                    )

            usage_story = (
                "\n\n".join(usage_lines)
                if usage_lines
                else f"No documented callers of `{detail.qualified_name}`."
            )

            result: dict[str, Any] = {
                "qname": detail.qualified_name,
                "signature": detail.signature or "",
                "source_pointer": f"{detail.file_path}:{detail.start_line}-{detail.end_line}",
                "usage_story": usage_story,
                "callers": callers,
            }
            if history:
                result["history"] = self._digest_history(qname=detail.qualified_name)
            tele_ctx["result_kind"] = "ok"
            tele_ctx["callers_count"] = len(callers)
            return result

    def trace_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]:
        """Find call chain(s) between two symbols.

        Returns the shortest path(s) from `symbol1` to `symbol2` following callee edges.
        If no path exists within the search depth, returns an empty paths list with a note.
        Hub symbols are skipped during expansion (same guard as the cascade).

        Returns `{from_qname, to_qname, paths: [[qname, ...], ...], notes?}`.
        """
        tele_args = {"symbol1": symbol1, "symbol2": symbol2} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="trace_flow", args=tele_args) as tele_ctx:
            # Resolve both symbols — accept fuzzy names.
            def _resolve(sym: str) -> tuple[str | None, dict[str, Any] | None]:
                detail = self.store.get_symbol_detail(sym)
                if detail is not None:
                    return detail.qualified_name, None
                base = self.grep_symbol(sym)
                if "error" in base:
                    return None, _error(
                        "not_found", f"No symbol matching {sym!r}.", self._suggest_for_qname(sym)
                    )
                return base["match"]["qname"], None

            qname1, err = _resolve(symbol1)
            if err:
                tele_ctx["result_kind"] = "error"
                return err
            qname2, err = _resolve(symbol2)
            if err:
                tele_ctx["result_kind"] = "error"
                return err

            paths = self.store.find_paths(
                qname1,  # type: ignore[arg-type]
                qname2,  # type: ignore[arg-type]
                max_depth=self.mcp_cfg.trace_max_depth,
                hub_threshold=self.mcp_cfg.trace_hub_threshold,
                max_paths=3,
            )

            notes: list[str] = []
            if not paths:
                notes.append(
                    f"No call chain found from {qname1!r} to {qname2!r} within "
                    f"depth {self.mcp_cfg.trace_max_depth}. The symbols may be "
                    "unrelated, or the path may route through a hub symbol that "
                    "was skipped. Try swapping the arguments to search the reverse direction."
                )

            result: dict[str, Any] = {
                "from_qname": qname1,
                "to_qname": qname2,
                "paths": paths,
            }
            if notes:
                result["notes"] = notes
            tele_ctx["result_kind"] = "ok"
            tele_ctx["paths_count"] = len(paths)
            return result

    def explain_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]:
        """Find call chain(s) between two symbols and join the prose of each node
        in the path into a readable execution narrative.

        Use when you want to understand not just that a path exists but what each
        step in the chain actually does — the story of the execution flow from
        entry to target.

        Returns `{from_qname, to_qname, paths: [{chain: [qname,...], narrative: str}], notes?}`.
        """
        tele_args = {"symbol1": symbol1, "symbol2": symbol2} if telemetry.capture_args() else {}
        with telemetry.timed(self.event_name, tool="explain_flow", args=tele_args) as tele_ctx:
            flow = self.trace_flow(symbol1, symbol2)
            if "error" in flow:
                tele_ctx["result_kind"] = "error"
                return flow

            paths_with_narrative: list[dict[str, Any]] = []
            for path in flow.get("paths", []):
                steps: list[str] = []
                for qname in path:
                    detail = self.store.get_symbol_detail(qname)
                    if detail is None:
                        steps.append(f"**{qname}** — (no symbol detail)")
                        continue
                    prose, _ = self._prose_for(detail)
                    snippet = prose.split("\n\n")[0].strip() if prose else detail.one_liner
                    loc = f"{detail.file_path}:{detail.start_line}"
                    if snippet:
                        steps.append(f"**{qname}** ({loc})\n{snippet}")
                    else:
                        steps.append(f"**{qname}** ({loc}) — no prose yet; run `trie sync`.")
                narrative = "\n\n→ ".join(steps)
                paths_with_narrative.append({"chain": path, "narrative": narrative})

            result: dict[str, Any] = {
                "from_qname": flow["from_qname"],
                "to_qname": flow["to_qname"],
                "paths": paths_with_narrative,
            }
            if "notes" in flow:
                result["notes"] = flow["notes"]
            tele_ctx["result_kind"] = "ok"
            tele_ctx["paths_count"] = len(paths_with_narrative)
            return result

    # --- helpers -----------------------------------------------------------

    def _suggest_for_qname(self, qname: str) -> str | None:
        """Suggestion text for a `not_found` qname. Pulls fuzzy matches from the symbol set."""
        matches = _close_qname_matches(qname, self.store.all_qualified_names())
        if not matches:
            # Fall back to local-name fuzzy match: agent may have given just the name
            # rather than a qname.
            short = qname.split(":")[-1].split(".")[-1]
            name_matches = _close_name_matches(short, self.store.all_symbol_names())
            if not name_matches:
                return "Use grep({'name_contains': '...'}) to find the exact qname."
            joined = ", ".join(name_matches)
            return (
                f"No exact qname match. Names that look close: {joined}. "
                "Use grep({'name_contains': '...'}) to resolve a full qname."
            )
        joined = ", ".join(repr(m) for m in matches)
        return f"Did you mean one of: {joined}?"


# --- server construction ---------------------------------------------------


def _textified(fn: Callable[..., dict[str, Any]]) -> Callable[..., str]:
    """Wrap a dict-returning TrieTools method so it returns rendered text.

    Pretty text is the default on every interaction surface: agents READ tool
    output, and JSON made them pay for braces, escaped-newline prose, and
    unicode escapes on every query. The wrapper preserves the method's name,
    docstring, and parameter signature (FastMCP builds the tool schema from
    them) and swaps only the return annotation to `str`. The underlying
    `TrieTools` methods keep returning dicts — tests and programmatic callers
    (and `trie <cmd> --json` on the CLI, which shares them) are unaffected.
    """
    import inspect

    from trie.render import render_envelope

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = fn(*args, **kwargs)
        return render_envelope(result) if isinstance(result, dict) else str(result)

    sig = inspect.signature(fn)
    wrapper.__signature__ = sig.replace(return_annotation=str)  # type: ignore[attr-defined]
    annotations = dict(getattr(fn, "__annotations__", {}))
    annotations["return"] = str
    wrapper.__annotations__ = annotations
    return wrapper


def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]:
    """Construct an MCP server bound to the trie state under `project_root`.

    Returns the server and the underlying TrieTools instance — the latter is exposed so
    tests can call tool methods directly without driving the MCP transport, and so the
    CLI subcommands (`trie grep`, `trie read`, `trie trace`) can share the same
    implementation as the MCP wire calls.

    Query tools are registered `_textified`: the wire carries rendered text,
    not JSON — same data, readable instead of parseable. Edit-pipeline tools
    stay structured: their envelopes are small and callers branch on fields
    (`ok`, `staged`, `uncovered`, `did_you_mean`).
    """
    tools = TrieTools(project_root)
    server = FastMCP("trie")
    # Query tools: text on the wire. The CLI subcommands share the same
    # underlying methods and offer `--json` for the raw envelope, so the
    # structured form is always one flag away.
    server.tool(name="grep")(_textified(tools.grep))
    server.tool(name="read")(_textified(tools.read))
    server.tool(name="trace")(_textified(tools.trace))
    server.tool(name="grep_str")(_textified(tools.grep_str))
    server.tool(name="grep_str_all")(_textified(tools.grep_str_all))
    server.tool(name="find_files")(_textified(tools.find_files))
    server.tool(name="read_source")(_textified(tools.read_source))
    server.tool(name="write_file")(tools.write_file)
    server.tool(name="grep_entry_points")(_textified(tools.grep_entry_points))
    server.tool(name="grep_symbol")(_textified(tools.grep_symbol))
    server.tool(name="grep_symbol_and_neighbours")(_textified(tools.grep_symbol_and_neighbours))
    server.tool(name="explain_symbol")(_textified(tools.explain_symbol))
    server.tool(name="explain_symbol_references")(_textified(tools.explain_symbol_references))
    server.tool(name="trace_flow")(_textified(tools.trace_flow))
    server.tool(name="explain_flow")(_textified(tools.explain_flow))
    # Edit tools — declare intent (modify/create/delete/rename) then preview/commit.
    # Structured on purpose: callers branch on envelope fields.
    server.tool(name="patch")(tools.patch)
    server.tool(name="batch_patch")(tools.batch_patch)
    server.tool(name="create_symbol")(tools.create_symbol)
    server.tool(name="delete_symbol")(tools.delete_symbol)
    server.tool(name="rename_symbol")(tools.rename_symbol)
    server.tool(name="preview")(tools.preview)
    server.tool(name="commit")(tools.commit)
    server.tool(name="patch_drop")(tools.patch_drop)
    server.tool(name="patch_list")(tools.patch_list)
    server.tool(name="patch_apply")(tools.patch_apply)
    # Project-level queries.
    server.tool(name="summary")(_textified(tools.summary))
    server.tool(name="symbols_by_file")(_textified(tools.symbols_by_file))
    server.tool(name="file_triefact")(_textified(tools.file_triefact))
    server.tool(name="activity")(_textified(tools.activity))
    server.tool(name="blast_radius")(_textified(tools.blast_radius))
    return server, tools


def run_stdio(project_root: Path) -> None:
    """Run the MCP server over stdio. Blocks until the parent closes the pipe."""
    import sys

    sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
    sys.stderr.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
    server, _tools = build_server(project_root)
    server.run()


def main() -> None:
    """Console-script entry point: ``trie-mcp <project-dir>``.

    Runs the stdio MCP server for the given project. This is the surface
    external harnesses spawn as a sidecar.
    """
    import sys

    if len(sys.argv) < 2:
        print("usage: trie-mcp <project-dir>", file=sys.stderr)
        sys.exit(1)

    project_root = Path(sys.argv[1]).resolve()
    if not project_root.exists():
        print(f"error: project directory does not exist: {project_root}", file=sys.stderr)
        sys.exit(1)

    run_stdio(project_root)
