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

import json
import shutil
import subprocess
from collections import deque
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from rapidfuzz import fuzz as _fuzz
from rapidfuzz import process as _process

from trie import telemetry
from trie.config import Config, Mcp
from trie.graph.store import GrepPredicate, Store, SymbolDetail
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
) -> dict[str, Any]:
    """Build the canonical error envelope: `{error: {code, message, suggestion?}}`.

    Agents read these as authoritative — a `suggestion` is included whenever there
    is a concrete next step to recommend.
    """
    body: dict[str, Any] = {"code": code, "message": message}
    if suggestion is not None:
        body["suggestion"] = suggestion
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


def _close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]:
    """Fuzzy-match `qname` against the known set. Used for `not_found` suggestions."""
    hits = _process.extract(qname, candidates, scorer=_fuzz.WRatio, limit=n, score_cutoff=45)
    return [h[0] for h in hits]


def _close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]:
    hits = _process.extract(name, candidates, scorer=_fuzz.WRatio, limit=n, score_cutoff=45)
    return [h[0] for h in hits]


def _fuzzy_score(query: str, text: str) -> float:
    """Return a 0-100 rapidfuzz WRatio score, short-circuiting to 100.0 on exact substring.

    Used as the single scoring primitive across all fuzzy paths. Exact substring wins
    unconditionally so that a query like "slugify" always matches a symbol named
    "slugify_strict" with a perfect score before the ratio path even runs.
    """
    if not text:
        return 0.0
    if query.lower() in text.lower():
        return 100.0
    return _fuzz.WRatio(query, text)


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
    """
    local_name = (
        sym.qualified_name.split(":")[-1] if ":" in sym.qualified_name else sym.qualified_name
    )
    name_score = _fuzzy_score(query, local_name)
    liner_score = _fuzzy_score(query, sym.one_liner or "") * 0.8
    prose_score = _fuzzy_score(query, prose[:2000]) * prose_weight if prose else 0.0
    return max(name_score, liner_score, prose_score)


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
        # Session id for patch operations — lives for the MCP server lifetime,
        # which maps 1:1 to an agent session.
        import uuid

        self._session_id = uuid.uuid4().hex[:12]

    def close(self) -> None:
        self.store.close()

    # --- patch tools -------------------------------------------------------

    def patch(
        self,
        qname: str,
        note: str,
        reason: str = "",
    ) -> dict[str, Any]:
        """Post an implementation note against a symbol.

        Fire-and-forget. Returns {patch_id, qname, pending_patch_count}.
        Use patch_list() to view all pending; patch_drop() to undo.
        """
        if not note.strip():
            return _error("invalid_argument", "note must be non-empty.")
        try:
            patch_id = self.store.add_patch(qname, note, reason, self._session_id)
        except KeyError:
            return _error(
                "not_found",
                f"Symbol {qname!r} not found in the graph.",
                "Use grep({'name_contains': '...'}) to find the exact qname.",
            )
        detail = self.store.get_symbol_detail(qname)
        return {
            "patch_id": int(patch_id),
            "qname": qname,
            "pending_patch_count": detail.pending_patch_count if detail else 1,
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
        """List all pending patches grouped by symbol.

        Returns {patches: [{qname, count, origin, notes: [...]}, ...]}.
        """
        qnames = self.store.get_patched_qnames()
        patches: list[dict[str, Any]] = []
        for qn in qnames:
            notes = self.store.get_patches_for_qname(qn)
            # Determine origin from session_id of patches
            origins = set(p.get("session_id", "") for p in notes)
            origin = (
                "cascade" if origins == {"cascade"} else "mixed" if len(origins) > 1 else "agent"
            )
            patches.append(
                {
                    "qname": qn,
                    "count": len(notes),
                    "origin": origin,
                    "notes": notes,
                }
            )
        return {"patches": patches}

    def patch_apply(self) -> dict[str, Any]:
        """Apply all pending patches: merge, generate, cascade, commit.

        Uses an exclusive lock to prevent concurrent apply runs.
        Returns {ok, applied, failed, error?}.
        """
        from trie.edits.apply import apply_patches
        from trie.models import make_client
        from trie.refresh_lock import try_acquire

        with try_acquire(self.root, name="apply") as holder:
            if not holder.acquired:
                return _error(
                    "conflict",
                    "another patch apply is already in progress",
                    "retry when the current apply finishes.",
                )
            client = make_client(self.config.models.edits)
            try:
                result = apply_patches(self.store, self.config, client, self.root)
            except Exception as exc:
                return _error("internal", f"patch apply failed: {exc}")
            return result

    # --- desktop app helpers -----------------------------------------------

    def summary(self) -> dict[str, Any]:
        """Return project-level aggregate counts for the trie desktop app.

        Returns {project_name, total_symbols, public_symbols, total_files,
        total_edges, trie_version}.
        """
        import trie as trie_pkg

        with self.store as s:
            total_symbols: int = s._conn.execute("SELECT COUNT(*) FROM symbols").fetchone()[0]
            public_symbols: int = s._conn.execute(
                "SELECT COUNT(*) FROM symbols WHERE is_public = 1"
            ).fetchone()[0]
            total_files: int = s._conn.execute(
                "SELECT COUNT(DISTINCT file_path) FROM symbols"
            ).fetchone()[0]
            total_edges: int = s._conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]

        return {
            "project_name": self.root.name,
            "project_root": str(self.root),
            "total_symbols": total_symbols,
            "public_symbols": public_symbols,
            "total_files": total_files,
            "total_edges": total_edges,
            "trie_version": getattr(trie_pkg, "__version__", "unknown"),
        }

    def symbols_by_file(self, file_path: str) -> dict[str, Any]:
        """Return all symbols in a given source file.

        Returns {file_path, symbols: [SymbolDetail, ...]}.
        Used by the desktop app sidebar file-click to highlight graph nodes.
        """
        with self.store as s:
            rows = s._conn.execute(
                """
                SELECT
                    sym.qualified_name, sym.name, sym.kind, sym.file_path,
                    sym.start_line, sym.end_line, sym.signature, sym.is_public,
                    (SELECT COUNT(*) FROM edges e WHERE e.dst_symbol_id = sym.id) as inbound_count,
                    (SELECT COUNT(*) FROM edges e WHERE e.src_symbol_id = sym.id) as outbound_count,
                    COALESCE(ts.one_liner, '') as one_liner
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
                "signature": r[6],
                "is_public": bool(r[7]),
                "inbound_count": r[8],
                "outbound_count": r[9],
                "one_liner": r[10],
            }
            for r in rows
        ]
        return {"file_path": file_path, "symbols": symbols}

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
        - `kind`: one of `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`, `"any"`.
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
          "fallback"?: { ... }   # present only when hits is empty
        }
        ```
        On empty hits, `fallback.kind` is one of:
        - `"none"`: predicate had no `name_contains` for the fallback to search on.
        - `"text_match_empty"`: the query string appears in no in-scope source body
          and fuzzy matching also found nothing above the cutoff.
        - `"text_match"`: a string search against in-scope source bodies found
          candidate symbols; `matches` is the ranked list (by `inbound_count`
          desc) capped at `grep_fallback_match_limit`. Even when the underlying
          string match was very broad, we always return the top-ranked
          candidates so the agent can triangulate from data rather than refine
          blindly.
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
            # trie tried alternatives or not.
            if not hit_dicts:
                fallback = self._maybe_text_match_fallback(pred_obj)
                result["fallback"] = fallback
                tele_ctx["fallback_kind"] = fallback["kind"]
                tele_ctx["fallback_match_count"] = len(fallback.get("matches", []))

            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hit_dicts)
            tele_ctx["response_bytes"] = len(json.dumps(result, default=str))
            if telemetry.capture_responses():
                tele_ctx["response"] = result
            return result

    def _maybe_text_match_fallback(self, pred: GrepPredicate) -> dict[str, Any]:
        """Build the `fallback` envelope returned alongside an empty `hits` list.

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
            fuzzy_fallback = self._fuzzy_prose_fallback(query, pred)
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
            fuzzy_fallback = self._fuzzy_prose_fallback(query, pred)
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
        capped = candidates[: self.mcp_cfg.grep_fallback_match_limit]
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

    def _fuzzy_prose_fallback(self, query: str, pred: GrepPredicate) -> dict[str, Any] | None:
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
                f"rg failed (exit {proc.returncode}): {proc.stderr.strip() or 'no stderr'}"
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
        if kind is not None and kind not in (
            "function",
            "class",
            "method",
            "constant",
            "module",
            "any",
        ):
            return GrepPredicate(), _error(
                "invalid_argument",
                (f"`kind` must be one of function/class/method/constant/module/any, got {kind!r}."),
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

    def read(self, qname: str) -> dict[str, Any]:
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

            # Pull public hubs as the candidate pool.
            pred = GrepPredicate(public_only=True, inbound_count_min=2)
            candidates = self.store.grep_symbols(
                pred, rank_by="inbound_count", limit=self.mcp_cfg.grep_max_limit
            )

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

            scored.sort(key=lambda x: -x[0])

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

    def explain_symbol(self, sym: str) -> dict[str, Any]:
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
            if prose_notes:
                out["notes"] = prose_notes
            tele_ctx["result_kind"] = "ok"
            tele_ctx["prose_chars"] = len(prose)
            tele_ctx["story_chars"] = len(story)
            return out

    def explain_symbol_references(self, sym: str) -> dict[str, Any]:
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


def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]:
    """Construct an MCP server bound to the trie state under `project_root`.

    Returns the server and the underlying TrieTools instance — the latter is exposed so
    tests can call tool methods directly without driving the MCP transport, and so the
    CLI subcommands (`trie grep`, `trie read`, `trie trace`) can share the same
    implementation as the MCP wire calls.
    """
    tools = TrieTools(project_root)
    server = FastMCP("trie")
    # Three operations, three wire names, three identical CLI subcommands.
    # The underlying methods on TrieTools have the same names, so an agent
    # calling `trie grep --json ...` from the shell gets a response that's
    # byte-equivalent to what it would get from the MCP `grep` tool.
    server.tool(name="grep")(tools.grep)
    server.tool(name="read")(tools.read)
    server.tool(name="trace")(tools.trace)
    server.tool(name="grep_str")(tools.grep_str)
    server.tool(name="grep_entry_points")(tools.grep_entry_points)
    server.tool(name="grep_symbol")(tools.grep_symbol)
    server.tool(name="grep_symbol_and_neighbours")(tools.grep_symbol_and_neighbours)
    server.tool(name="explain_symbol")(tools.explain_symbol)
    server.tool(name="explain_symbol_references")(tools.explain_symbol_references)
    server.tool(name="trace_flow")(tools.trace_flow)
    server.tool(name="explain_flow")(tools.explain_flow)
    # Patch tools — implementation notes + apply
    server.tool(name="patch")(tools.patch)
    server.tool(name="patch_drop")(tools.patch_drop)
    server.tool(name="patch_list")(tools.patch_list)
    server.tool(name="patch_apply")(tools.patch_apply)
    # Desktop app helpers — project summary + symbols by file
    server.tool(name="summary")(tools.summary)
    server.tool(name="symbols_by_file")(tools.symbols_by_file)
    return server, tools


def run_stdio(project_root: Path) -> None:
    """Run the MCP server over stdio. Blocks until the parent closes the pipe."""
    import sys

    sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
    sys.stderr.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
    server, _tools = build_server(project_root)
    server.run()
