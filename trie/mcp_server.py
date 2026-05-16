"""MCP server exposing the trie triefact tree + symbol graph to coding agents.

Read-only. Speaks MCP over stdio so an agent harness (Claude Code, Codex, etc.) can spawn
it as a subprocess and consult the triefact tree as context separate from its own
conversation memory.

Three verbs match the cognitive moves an agent makes when navigating an unfamiliar
codebase:

- `locate(predicate, rank_by?, limit=10)` — find symbols matching a predicate.
- `explain(qname)` — read one symbol's prose plus the one-liners of its immediate
  neighbours (callers + callees).
- `walk(from_qname, direction, depth=2)` — trace the graph topology beyond one hop.

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

import difflib
import json
from collections import deque
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from trie import telemetry
from trie.config import Config, Mcp
from trie.graph.store import LocatePredicate, Store, SymbolDetail
from trie.scope import discover_files


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
    """Compact symbol record used inside neighbour / walk-node lists."""
    return {
        "qname": detail.qualified_name,
        "signature": detail.signature or "",
        "one_liner": _truncate(detail.one_liner, one_liner_max),
    }


def _close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]:
    """Fuzzy-match `qname` against the known set. Used for `not_found` suggestions."""
    return difflib.get_close_matches(qname, candidates, n=n, cutoff=0.6)


def _close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]:
    return difflib.get_close_matches(name, candidates, n=n, cutoff=0.6)


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

    Owns the Store for the lifetime of the surrounding server process.
    """

    def __init__(self, project_root: Path) -> None:
        self.config, self.root = Config.find_and_load(project_root)
        self.mcp_cfg: Mcp = self.config.mcp
        # Telemetry: configure from the project's [debug] block. Agents spawn the
        # MCP server directly (not via `trie ...`), so this is the only place we
        # can wire it from config for the stdio path. The env var TRIE_DEBUG
        # still wins if set.
        telemetry.configure(self.config.debug, self.root)
        telemetry.emit("mcp_server_start", project_root=str(self.root))
        self.triefacts_root = self.root / self.config.triefacts.root
        self.src_root = (self.root / self.config.triefacts.source_root).resolve()
        self.store = Store(self.root / ".trie" / "graph.db")

    def close(self) -> None:
        self.store.close()

    # --- locate ------------------------------------------------------------

    def locate(
        self,
        predicate: dict[str, Any] | None = None,
        rank_by: str | None = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        """Find symbols matching `predicate`.

        Predicate fields (all optional):
        - `name_contains`: substring match against the symbol's local name (case-insensitive).
        - `kind`: one of `"function"`, `"class"`, `"method"`, `"any"`.
        - `scope_prefix`: file-path prefix, e.g. `"trie/"` to exclude tests/vendored code.
        - `scope_exclude`: list of file-path prefixes to skip, e.g. `["tests/"]`.
        - `public_only`: bool. Restrict to symbols whose name doesn't start with `_`.
        - `inbound_count`: `{min?: int, max?: int}` — filter by inbound edge count.
        - `outbound_count`: `{min?: int, max?: int}` — filter by outbound edge count.

        `rank_by` is one of `"public_first"` (default), `"inbound_count"` (centrality
        for orientation queries), or `"alphabetical"`.

        Provide only the fields you need — most queries use just `name_contains` or
        `scope_prefix`.

        Return shape:
        ```
        {
          "hits": [ {qname, signature, file_pointer, one_liner, is_public, kind,
                     inbound_count, outbound_count}, ... ],
          "fallback"?: { ... }   # present only when hits is empty
        }
        ```
        On empty hits, `fallback.kind` is one of:
        - `"none"`: predicate had no `name_contains` to grep on, nothing to suggest.
        - `"grep_empty"`: the query string appears in no in-scope source body.
        - `"grep"`: grep found candidate symbols whose bodies contain the query;
          `matches` is the ranked list (by `inbound_count` desc) capped at
          `locate_fallback_match_limit`. Even when the underlying grep hit was
          very broad, we always return the top-ranked candidates so the agent
          can triangulate from data rather than refine blindly.

        Errors (bad predicate shape, etc.) still return `{"error": {...}}`.
        """
        tele_args = (
            {"predicate": predicate, "rank_by": rank_by, "limit": limit}
            if telemetry.capture_args()
            else {}
        )
        with telemetry.timed("mcp_call", tool="locate", args=tele_args) as tele_ctx:
            pred_obj, err = self._parse_predicate(predicate)
            if err is not None:
                tele_ctx["result_kind"] = "error"
                tele_ctx["error_code"] = err["error"]["code"]
                return err

            rank = rank_by or self.mcp_cfg.locate_default_rank_by
            capped_limit = min(max(1, limit), self.mcp_cfg.locate_max_limit)

            hits = self.store.locate_symbols(pred_obj, rank_by=rank, limit=capped_limit)
            one_liner_cap = self.mcp_cfg.locate_one_liner_max_chars
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
                }
                for h in hits
            ]
            result: dict[str, Any] = {"hits": hit_dicts}

            # When the predicate matched nothing, try the grep fallback. The
            # fallback always produces SOMETHING in the response — even if it's
            # `kind="none"` — so the agent never has to guess whether trie
            # tried alternatives or not.
            if not hit_dicts:
                fallback = self._maybe_grep_fallback(pred_obj)
                result["fallback"] = fallback
                tele_ctx["fallback_kind"] = fallback["kind"]
                tele_ctx["fallback_match_count"] = len(fallback.get("matches", []))

            tele_ctx["result_kind"] = "ok"
            tele_ctx["result_count"] = len(hit_dicts)
            tele_ctx["response_bytes"] = len(json.dumps(result, default=str))
            if telemetry.capture_responses():
                tele_ctx["response"] = result
            return result

    def _maybe_grep_fallback(self, pred: LocatePredicate) -> dict[str, Any]:
        """Build the `fallback` envelope returned alongside an empty `hits` list.

        The contract is to always return a dict with a `kind` field, so the
        agent can dispatch on three distinct empty cases:

        - `none`: no `name_contains` was supplied; nothing to grep for. The agent
          should not try the same predicate again — its shape isn't grep-able.
        - `grep_empty`: the query appears in no in-scope source body (or only
          outside any indexed symbol). Likely a typo or a wrong project.
        - `grep`: candidate symbols whose bodies contain the query, ranked by
          `inbound_count` descending and capped at `locate_fallback_match_limit`.

        We deliberately do not bail out when the result is "too noisy" — raw
        grep would have shown the user N matches and let them eyeball it; we
        match that floor by ranking and capping. The `match_count` /
        `unique_symbols` fields convey the breadth of the underlying hit so
        the agent knows the cap was reached.

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
                    "to grep for. Add a name substring or relax other filters."
                ),
            }

        # Walk in-scope source files and collect line-level hits. The grep
        # walker has its own internal cap on files-scanned (a runtime guard,
        # not a discriminator); on hitting that cap it returns whatever it
        # accumulated so far, which we treat as authoritative — the agent
        # gets the most-relevant N files' worth of matches either way.
        grep_hits = self._grep_in_scope(query)
        if not grep_hits:
            return {
                "kind": "grep_empty",
                "query": query,
                "note": (
                    f"Predicate matched no symbols, and {query!r} appears in no "
                    "in-scope source file body either. Likely a typo or a name "
                    "that doesn't exist in this project."
                ),
            }

        # Attribute each matched line to the smallest enclosing symbol.
        per_symbol = self._attribute_grep_to_symbols(grep_hits)
        if not per_symbol:
            # The query matched lines, but every match was outside any symbol
            # (module-level code, imports, comments at file top, etc.). This
            # is honest signal — the agent shouldn't be misled into thinking a
            # symbol was found.
            return {
                "kind": "grep_empty",
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
            # Grep found symbols, but none survived the predicate's other filters.
            # That's still useful signal: the agent's scope restrictions are
            # excluding what the substring would point to.
            return {
                "kind": "grep_empty",
                "query": query,
                "note": (
                    f"Query {query!r} matched symbols, but none satisfied the "
                    "other predicate filters (e.g. `scope_prefix`, `kind`, "
                    "`public_only`). Try a broader predicate."
                ),
            }

        candidates.sort(key=lambda c: (-c[0].inbound_count, c[0].qualified_name))
        capped = candidates[: self.mcp_cfg.locate_fallback_match_limit]
        truncated = len(candidates) > len(capped)

        one_liner_cap = self.mcp_cfg.locate_one_liner_max_chars
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
                "grep_hits_in_body": body_hits,
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
            "kind": "grep",
            "query": query,
            "match_count": sum(per_symbol.values()),
            "unique_symbols": len(per_symbol),
            "matches": matches,
            "note": note,
        }

    def _grep_in_scope(self, query: str) -> dict[str, list[int]]:
        """Walk in-scope source files and return `{rel_path: [line_numbers]}`.

        Case-insensitive substring search. Stops walking once the file-count
        cap (`mcp_cfg.locate_fallback_max_files`) is reached and returns
        whatever it has accumulated — this is a runtime guard against
        scanning a huge project on a very common substring, not a signal to
        the caller. The fallback ranks and caps the symbol-level result
        regardless of how many files contributed.
        """
        src_root = self.src_root
        needle = query.lower()
        hits: dict[str, list[int]] = {}
        for abs_path in discover_files(self.root, self.config.scope):
            if not abs_path.is_relative_to(src_root):
                continue
            try:
                text = abs_path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            file_hits: list[int] = []
            for lineno, line in enumerate(text.splitlines(), start=1):
                if needle in line.lower():
                    file_hits.append(lineno)
            if file_hits:
                rel = str(abs_path.relative_to(src_root))
                hits[rel] = file_hits
                if len(hits) >= self.mcp_cfg.locate_fallback_max_files:
                    break
        return hits

    def _attribute_grep_to_symbols(self, grep_hits: dict[str, list[int]]) -> dict[str, int]:
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
        for file_path, linenos in grep_hits.items():
            symbols = self.store.symbols_in_file_with_lines(file_path)
            if not symbols:
                continue
            for lineno in linenos:
                enclosing = _smallest_enclosing(symbols, lineno)
                if enclosing is None:
                    continue
                per_symbol[enclosing] = per_symbol.get(enclosing, 0) + 1
        return per_symbol

    def _candidate_matches_predicate(self, detail: SymbolDetail, pred: LocatePredicate) -> bool:
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
    ) -> tuple[LocatePredicate, dict[str, Any] | None]:
        """Turn the dict the agent passed into a LocatePredicate, or return an error."""
        if predicate is None:
            return LocatePredicate(), None
        if not isinstance(predicate, dict):
            return LocatePredicate(), _error(
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
            return LocatePredicate(), err
        out_min, out_max, err = _count_range(predicate.get("outbound_count"), "outbound_count")
        if err is not None:
            return LocatePredicate(), err

        kind = predicate.get("kind")
        if kind is not None and kind not in ("function", "class", "method", "any"):
            return LocatePredicate(), _error(
                "invalid_argument",
                f"`kind` must be one of function/class/method/any, got {kind!r}.",
            )

        scope_exclude_raw = predicate.get("scope_exclude") or ()
        if isinstance(scope_exclude_raw, str):
            scope_exclude_raw = (scope_exclude_raw,)
        try:
            scope_exclude = tuple(str(x) for x in scope_exclude_raw)
        except TypeError:
            return LocatePredicate(), _error(
                "invalid_argument",
                "`scope_exclude` must be a list of path prefixes.",
            )

        return (
            LocatePredicate(
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

    # --- explain -----------------------------------------------------------

    def explain(self, qname: str) -> dict[str, Any]:
        """Read a symbol's prose plus one-liners for every immediate caller and callee.

        Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
        Use after `locate` once you know which symbol you want to understand. If you
        need depth > 1, use `walk` and follow up with `explain` on the nodes that matter.
        """
        tele_args = {"qname": qname} if telemetry.capture_args() else {}
        with telemetry.timed("mcp_call", tool="explain", args=tele_args) as tele_ctx:
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
            if detail.inbound_count > self.mcp_cfg.walk_hub_threshold:
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
            return _truncate(body, self.mcp_cfg.explain_prose_max_chars), []
        return "", [
            f"no section for {detail.qualified_name} in {triefact_path.name}; "
            "the triefact exists but this symbol hasn't been synced into it."
        ]

    def _neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]:
        """Resolve a list of qnames to compact neighbour records, with optional truncation.

        Returns (records, note_or_None). If the configured per-direction cap is hit,
        the records are truncated and a note describes the cut.
        """
        cap = self.mcp_cfg.explain_max_neighbours_per_direction
        total = len(qnames)
        truncated_note: str | None = None
        if cap > 0 and total > cap:
            qnames = qnames[:cap]
            truncated_note = (
                f"showed {cap} of {total} neighbours; use walk(direction=...) "
                "for the full topology."
            )

        records: list[dict[str, Any]] = []
        for q in qnames:
            d = self.store.get_symbol_detail(q)
            if d is None:
                # Symbol was deleted between scan and query; skip.
                continue
            records.append(
                _symbol_summary(d, one_liner_max=self.mcp_cfg.explain_neighbour_one_liner_max_chars)
            )
        return records, truncated_note

    # --- walk --------------------------------------------------------------

    def walk(
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

        Returns signatures and one-liners only — for prose, follow up with `explain`
        on a specific node.
        """
        tele_args = (
            {"from_qname": from_qname, "direction": direction, "depth": depth}
            if telemetry.capture_args()
            else {}
        )
        tele_ctx_outer = telemetry.timed("mcp_call", tool="walk", args=tele_args)
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
            depth = max(0, min(depth, self.mcp_cfg.walk_max_depth))
            if depth != requested_depth:
                notes.append(f"depth was clamped from {requested_depth} to {depth} (server max).")

            nodes: dict[str, dict[str, Any]] = {}
            edges: list[dict[str, str]] = []
            truncated_at: list[str] = []
            max_nodes = self.mcp_cfg.walk_max_nodes
            hub_threshold = self.mcp_cfg.walk_hub_threshold
            one_liner_cap = self.mcp_cfg.explain_neighbour_one_liner_max_chars

            def add_node(detail: SymbolDetail) -> bool:
                """Register a node if it fits under max_nodes. False on capacity hit."""
                if detail.qualified_name in nodes:
                    return True
                if len(nodes) >= max_nodes:
                    return False
                nodes[detail.qualified_name] = {
                    "signature": detail.signature or "",
                    "one_liner": _truncate(detail.one_liner, one_liner_cap),
                }
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
                    f"walk reached max_nodes={max_nodes}; result is BFS-ordered from root."
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
                return "Use locate({'name_contains': '...'}) to find the exact qname."
            joined = ", ".join(name_matches)
            return (
                f"No exact qname match. Names that look close: {joined}. "
                "Use locate({'name_contains': '...'}) to resolve a full qname."
            )
        joined = ", ".join(repr(m) for m in matches)
        return f"Did you mean one of: {joined}?"


# --- server construction ---------------------------------------------------


def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]:
    """Construct an MCP server bound to the trie state under `project_root`.

    Returns the server and the underlying TrieTools instance — the latter is exposed so
    tests can call tool methods directly without driving the MCP transport.
    """
    tools = TrieTools(project_root)
    server = FastMCP("trie")
    server.tool()(tools.locate)
    server.tool()(tools.explain)
    server.tool()(tools.walk)
    return server, tools


def run_stdio(project_root: Path) -> None:
    """Run the MCP server over stdio. Blocks until the parent closes the pipe."""
    server, _tools = build_server(project_root)
    server.run()
