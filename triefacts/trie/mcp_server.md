---
trie_version: 0.1.0
source: trie/mcp_server.py
file_fingerprint: 41ba7d9044f2110117216ff7acbbac1eb4aa8922eb50c58c51aa16482958e9f7
last_synced_at: '2026-05-16T13:27:54Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 50-63
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 66-70
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 73-79
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 82-84
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 87-88
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 91-110
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 113-817
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 119-130
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 132-133
- kind: method
  qualified_name: trie/mcp_server:TrieTools.locate
  lines: 137-226
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_grep_fallback
  lines: 228-361
- kind: method
  qualified_name: trie/mcp_server:TrieTools._grep_in_scope
  lines: 363-392
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_grep_to_symbols
  lines: 394-417
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 419-445
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 447-518
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain
  lines: 522-580
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 582-619
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 621-646
- kind: method
  qualified_name: trie/mcp_server:TrieTools.walk
  lines: 650-797
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 801-817
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 823-834
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 837-840
incoming_refs: 2
outgoing_refs: 29
---
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=4a66fb673052300464014a636feb488a8fbf617547e2a15c2c60350a3d41689a body_fp=1896c8f1ff3cbc085a8570a7d7b569fbbc5b4a4a0de5b58e9942e4954f76970c source_ref=22e6fb3ec57eaecf27caa58799ec1da39b8b81d7 -->
## `TrieTools`

Encapsulate the three MCP tool methods (`locate`, `explain`, `walk`) against a persistent `Store`, testable without MCP transport.

- `project_root`: resolved via `Config.find_and_load`; determines DB path and triefact tree location.
- Call `close()` to release the underlying store connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=442e119f95b99008035d6247dddce6fe6e965d30dfa4d278b5b93ce14b135e9f source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `close(self) -> None`

Release the underlying `Store` database connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.locate fingerprint=100f610893315abfa81397bf685b187fb4ff5a8ee3cb4cbf8a18b4ec3ca20bcd body_fp=08627125cb813722c0ceac7d590ceb59ac3012e7ba6d7b32511ba9d9b43525bd source_ref=22e6fb3ec57eaecf27caa58799ec1da39b8b81d7 -->
## `locate(self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10) -> dict[str, Any]`

Find symbols in the store matching a structured predicate, returning ranked, capped results.

- `predicate`: dict with optional keys `name_contains`, `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`, `outbound_count`.
- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`.
- `limit`: capped server-side at `mcp_cfg.locate_max_limit`; values below 1 are raised to 1.
- Returns `{"hits": [...]}` on success; adds `"fallback"` key when hits is empty; returns `{"error": ...}` on bad input.
- `fallback.kind`: one of `"none"`, `"grep"`, `"grep_empty"` (`"grep_too_noisy"` no longer exists; `"grep"` always returns top-ranked candidates instead of refusing).
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.explain fingerprint=b6b7c0bc63a3e0879a5888ead9fce642aa5c3f94e8f2540a3de2f32b70e23bca body_fp=275b10af2a169586a33fd4c8bba145ecf9e2fed7394993dde28ceb3860bc3249 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `explain(self, qname: str) -> dict[str, Any]`

Return a symbol's full prose and compact one-liners for every immediate caller and callee.

- `qname`: fully-qualified symbol name as stored in the graph DB.
- Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
- Returns `{error: {code, message, suggestion}}` if `qname` is not found.
- `notes`: list of warnings about missing triefacts, hub symbols, or truncated neighbours.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.walk fingerprint=a47a925d92469a18a79aa4f13ef64e4a34cc19c41cc83e2d0d0fc29ae0104183 body_fp=0c6c7c2f0b331a9c4a6fba9f1c96a024197c484f3b7386d52e70811fe61c67ee source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `walk(self, from_qname: str, direction: str = "callers", depth: int = 2) -> dict[str, Any]`

Trace the call graph from `from_qname` outward up to `depth` hops via BFS.

- `direction`: `"callers"`, `"callees"`, or `"both"`; controls which edges are followed.
- `depth`: clamped to `Config.mcp.walk_max_depth`; a note is added if clamped.
- Returns `{root, nodes, edges, truncated_at?, notes?}`; hub symbols (inbound count above threshold) halt expansion and appear in `truncated_at`.
- Expansion halts early and adds a note when `walk_max_nodes` is reached.
- Edge records carry `direction`: `"in"` (neighbour calls node) or `"out"` (node calls neighbour).
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=bd4ab2471102d2f7359a1496e476e579ec96cbe8b5577db0c3232e034acb8208 body_fp=465a6923a499ff236b872cd60d4956e2fe4fb4f5a8838254749fbcf7f9ee949f source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct an MCP server bound to the trie state under `project_root`, registering all three tools.

- Returns `(FastMCP, TrieTools)`; `TrieTools` is exposed for direct testing without the MCP transport.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=8cde71e2ff11fda4cfbc2261e1213e79ff338b8961e2ab7b957cf8c864ef91a9 body_fp=67b250d9427021896d3cc51336addbd6b9578fbbf05a05b75bb8fc586530b87c source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `run_stdio(project_root: Path) -> None`

Build and run the MCP server over stdio, blocking until the parent process closes the pipe.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_error fingerprint=597d455ff4a9e49ecd772c061e825ab45cae7724ee3d569343b9cfa871474702 body_fp=7bba45c38ab7e67983a82fab608d28e26992b38dc3a8fa5dddfaf6a084c6940c source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_error(code: str, message: str, suggestion: str | None = None) -> dict[str, Any]`

Build the canonical error envelope `{error: {code, message, suggestion?}}`.

- `suggestion`: include only when a concrete recovery step exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_truncate fingerprint=fc4edfb1b25a174070610aef0283c1a28160f8d6cf1ad2b088deff400629bfbf body_fp=c34ebb31bffd7ebd338140cf67b908ab3ae02c09a3d5fd74604bfbd3aa2f678b source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_truncate(text: str, max_chars: int) -> str`

Truncate `text` to `max_chars`, appending `…` when clipped; `0` disables the cap.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_symbol_summary fingerprint=06295dc08f2502dc1fb570cb09f2a0861eadf86820532f2c2b709d0b488a1d80 body_fp=d14056c7c85e4ca05a23cd29f368b1e329f84d356594129366b55181d237f483 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_symbol_summary(detail: SymbolDetail, *, one_liner_max: int) -> dict[str, Any]`

Build a compact symbol record containing `qname`, `signature`, and truncated `one_liner`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_close_qname_matches fingerprint=5c016d120d3f322918ecc9e21a389a0cc6103e27b1fa4363817aeb1ec01ad11d body_fp=211aac50e883d56f08fd72131516e3e6b04cd8204f8dfb454783fc5e66f756fd source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]`

Return up to `n` fuzzy-matched qualified names from `candidates` for `not_found` suggestions.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_close_name_matches fingerprint=c8c6ecd43dc9d7b0e584c6b83507b407d0a401c416d3f65832ccc0b38da908e9 body_fp=f831d7d0c4ec2a7f3204b7a9497a6e89456e663c157dead19b9ab909954bd166 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]`

Return up to `n` fuzzy matches for `name` against `candidates` using a 0.6 cutoff.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=27c0c1c0d5b5263b7d7e99a4d7f81c9c6c28f801c827e0d46ef58bafc491e61e body_fp=8b5c828e90eb7911e3941054c5a5892b482289c4320a093928eca5fe07d2fed1 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `TrieTools.__init__(self, project_root: Path) -> None`

Initialise `TrieTools` by loading config, wiring telemetry, and opening the SQLite symbol store.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=f67ca2b1749bd025582b3376f0c4fa839fefa9deed29e02309ce8ef5f01b3e57 body_fp=6fffcb3b1546b219462ef79686cb5ac899f661d6a3aac2a9411191f23c9a9e49 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_parse_predicate(self, predicate: dict[str, Any] | None) -> tuple[LocatePredicate, dict[str, Any] | None]`

Convert the raw predicate dict from an agent call into a `LocatePredicate`, returning a structured error on invalid input.

- Returns `(LocatePredicate(), error_dict)` on validation failure; `None` as second element on success.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._prose_for fingerprint=722b45e60db921b88d227e74da903a8762da1c8449c5dd8ee53fbbfbaf99bc5b body_fp=6079628b2a7be38f2be57c06c1aa35198ef800c81eae4f053d2b1130833ebf61 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]`

Read the triefact section body for a symbol, returning `(prose, notes)`.

- `notes`: non-empty when no triefact file exists, the section is missing, or a close sentinel is absent.
- `prose`: empty string on any failure; truncated to `explain_prose_max_chars` on success.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._neighbour_summaries fingerprint=025c563779c8d0856457480a50eccc05435e0611d4c16e6d5436610f65469b7b body_fp=7bcaca454f4dd3c265e6d8ae42b33e9d2609de2747f0af6ff21bf673fddfc6d1 source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]`

Resolve qnames to compact neighbour records, truncating to the configured per-direction cap.

- Returns `(records, note)` where `note` is non-None when records were truncated.
- Silently skips qnames whose symbols no longer exist in the store.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._suggest_for_qname fingerprint=54654ef3af3b23025e7eddf19645e85f4e37fb29f72dd69a4cf9cbc704c9f5aa body_fp=f62353767b45a7a1f120d78f48c95866ed5637f140e7f4d0c99a620e2af8b8ca source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `_suggest_for_qname(self, qname: str) -> str | None`

Return a human-readable suggestion string for a `not_found` qname using fuzzy matching.

- Falls back to local-name matching if no full qname match is found.
- Returns `None` implicitly only if both match paths yield results; always returns a string otherwise.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_smallest_enclosing fingerprint=4839c335a6d869c0fcaaaeb5126b1db1ddeac056279037b8a98dc142a759a02f body_fp=92106c63fe26c73554bb54967a4320a95e034e7fdadf17032d8a135003208d97 source_ref=6795f2438f7cef495f72fab2ec62616550b31303 -->
## `_smallest_enclosing(symbols: list[tuple[str, int, int]], lineno: int) -> str | None`

Return the qname of the innermost symbol whose line range brackets `lineno`.

- `symbols`: `(qname, start_line, end_line)` tuples, ordered by `start_line` ascending.
- Returns `None` when `lineno` falls outside every symbol's range.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_grep_fallback fingerprint=ae6ee217c25c5bbd99ce263ae578761a1b8016fbc8a9e6725789189e783d4387 body_fp=9ae8b4ef66b4b8e824b0e8122acab7de44b96db495050cc7ac373d18cab441ca source_ref=22e6fb3ec57eaecf27caa58799ec1da39b8b81d7 -->
## `_maybe_grep_fallback(self, pred: LocatePredicate) -> dict[str, Any]`

Build the `fallback` envelope returned alongside an empty `hits` list from `locate`.

- Returns a dict with a `kind` field: `"none"`, `"grep_empty"`, or `"grep"`.
- `"none"`: predicate has no `name_contains`; no grep attempted.
- `"grep_empty"`: query appears nowhere in-scope, or only outside any symbol, or all matches excluded by predicate filters.
- `"grep"`: `matches` list of candidate symbols whose bodies contain the query, ranked by `inbound_count` desc; never refuses on "too noisy" — always ranks and caps instead; appends truncation note to `note` when candidates exceed the cap.
- Predicate filters (`scope_prefix`, `scope_exclude`, `public_only`, `kind`, edge bounds) still apply to `"grep"` candidates; `name_contains` is intentionally skipped.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._grep_in_scope fingerprint=781552aed2c14208280c88cb127b24b9538f743f2950f6f1303fd1bdee64bb25 body_fp=5f165876c66fd4bf734c2b525f4a0cbf66fa74d623a28123747070ee4c277041 source_ref=22e6fb3ec57eaecf27caa58799ec1da39b8b81d7 -->
## `_grep_in_scope(self, query: str) -> dict[str, list[int]]`

Case-insensitively search all in-scope source files for `query`, returning matched line numbers per file.

- Never returns `None`; stops walking and returns accumulated results when file count hits `mcp_cfg.locate_fallback_max_files`.
- Returns `{}` when no file contains the query.
- Keys are paths relative to `src_root`; values are 1-based line number lists.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._attribute_grep_to_symbols fingerprint=4cc8dbd8650ae67b6b138abfebf17d9b3504a74a9db2b4451e2d84f881e631c8 body_fp=0686e8b421c2f2a66c4f81de594a035172247dcb18318132c8c6e565173402f6 source_ref=6795f2438f7cef495f72fab2ec62616550b31303 -->
## `_attribute_grep_to_symbols(self, grep_hits: dict[str, list[int]]) -> dict[str, int]`

Map each `(file, line)` grep match to its smallest enclosing symbol, returning `{qname: hit_count}`.

- Lines outside any symbol (imports, module-level code) are silently dropped.
- Nested symbols resolve to the innermost enclosing one (method over class).
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._candidate_matches_predicate fingerprint=67f81def759871cd0f3e53436f8010818ba7ae33393fd206cd91da97251ffc74 body_fp=5000c3ff619dbaf5774b9769db8d18365f9d5e81ca377d3a3c69713e223e14bd source_ref=6795f2438f7cef495f72fab2ec62616550b31303 -->
## `_candidate_matches_predicate(self, detail: SymbolDetail, pred: LocatePredicate) -> bool`

Apply non-name predicate filters to a grep fallback candidate symbol.

- Skips `name_contains` check intentionally; only scope, visibility, kind, and edge-count bounds are enforced.
<!-- trie:end -->