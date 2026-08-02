---
trie_version: 0.3.0
source: trie/mcp_server.py
file_fingerprint: e124d12c3c4b9b79492321e1d6f811750d2be2f68a05e951e06ba4978becf176
last_synced_at: '2026-08-02T21:20:02Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-3388
- kind: class
  qualified_name: trie/mcp_server:RipgrepNotFoundError
  lines: 80-92
  signature: class RipgrepNotFoundError(RuntimeError)
- kind: function
  qualified_name: trie/mcp_server:_require_ripgrep
  lines: 95-110
  signature: def _require_ripgrep() -> str
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 113-132
  signature: 'def _error( code: str, message: str, suggestion: str | None = None, *, fix: dict[str, Any] | None = None, ) -> dict[str, Any]'
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 135-139
  signature: 'def _truncate(text: str, max_chars: int) -> str'
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 142-148
  signature: 'def _symbol_summary(detail: SymbolDetail, *, one_liner_max: int) -> dict[str, Any]'
- kind: constant
  qualified_name: trie/mcp_server:_URL_SCHEME_RE
  lines: 151-151
- kind: constant
  qualified_name: trie/mcp_server:_WIN_DRIVE_RE
  lines: 152-152
- kind: function
  qualified_name: trie/mcp_server:_looks_like_qname
  lines: 155-168
  signature: 'def _looks_like_qname(s: str) -> bool'
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 171-196
  signature: 'def _close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]'
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 199-201
  signature: 'def _close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]'
- kind: function
  qualified_name: trie/mcp_server:_fuzzy_score
  lines: 204-232
  signature: 'def _fuzzy_score(query: str, text: str) -> float'
- kind: function
  qualified_name: trie/mcp_server:_is_test_symbol
  lines: 235-248
  signature: 'def _is_test_symbol(sym: SymbolDetail) -> bool'
- kind: constant
  qualified_name: trie/mcp_server:_TEST_SCORE_FACTOR
  lines: 251-251
- kind: function
  qualified_name: trie/mcp_server:_score_sym
  lines: 259-291
  signature: 'def _score_sym( query: str, sym: SymbolDetail, *, prose: str = "", prose_weight: float = 0.6, ) -> float'
- kind: function
  qualified_name: trie/mcp_server:_predicate_is_empty
  lines: 294-317
  signature: 'def _predicate_is_empty(pred: GrepPredicate) -> bool'
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 320-339
  signature: 'def _smallest_enclosing(symbols: list[tuple[str, int, int]], lineno: int) -> str | None'
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 342-3268
  signature: class TrieTools
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 356-385
  signature: 'def __init__(self, project_root: Path, *, event_name: str = "mcp_call") -> None'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 387-388
  signature: def close(self) -> None
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch
  lines: 392-447
  signature: 'def patch( self, qname: str, note: str = "", source: str = "", reason: str = "", ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.batch_patch
  lines: 449-548
  signature: 'def batch_patch(self, items: list[dict[str, Any]]) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._blast_radius_brief
  lines: 550-563
  signature: 'def _blast_radius_brief(self, qname: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.create_symbol
  lines: 565-614
  signature: 'def create_symbol( self, qname: str, note: str, file_path: str = "", anchor_qname: str = "", reason: str = "", ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._resolve_create_target
  lines: 616-620
  signature: 'def _resolve_create_target(self, qname: str) -> str'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.delete_symbol
  lines: 622-644
  signature: 'def delete_symbol(self, qname: str, reason: str = "") -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.rename_symbol
  lines: 646-668
  signature: 'def rename_symbol(self, qname: str, new_name: str, reason: str = "") -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.blast_radius
  lines: 670-717
  signature: 'def blast_radius(self, qname: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_drop
  lines: 719-732
  signature: 'def patch_drop( self, qname: str | None = None, ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_list
  lines: 734-774
  signature: def patch_list(self) -> dict[str, Any]
- kind: method
  qualified_name: trie/mcp_server:TrieTools.preview
  lines: 776-801
  signature: def preview(self) -> dict[str, Any]
- kind: method
  qualified_name: trie/mcp_server:TrieTools.commit
  lines: 803-827
  signature: 'def commit(self, session_note: str = "") -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_apply
  lines: 830-832
  signature: 'def patch_apply(self, session_note: str = "") -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.summary
  lines: 834-860
  signature: def summary(self) -> dict[str, Any]
- kind: method
  qualified_name: trie/mcp_server:TrieTools.activity
  lines: 862-915
  signature: def activity(self) -> dict[str, Any]
- kind: method
  qualified_name: trie/mcp_server:TrieTools.symbols_by_file
  lines: 917-956
  signature: 'def symbols_by_file(self, file_path: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.file_triefact
  lines: 958-1019
  signature: 'def file_triefact(self, file_path: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 1023-1182
  signature: 'def grep( self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10, ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 1184-1339
  signature: 'def _maybe_text_match_fallback( self, pred: GrepPredicate, *, max_matches: int | None = None ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._fuzzy_prose_fallback
  lines: 1341-1421
  signature: 'def _fuzzy_prose_fallback( self, query: str, pred: GrepPredicate, *, max_matches: int | None = None ) -> dict[str, Any] | None'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 1423-1522
  signature: 'def _text_match_in_scope(self, query: str) -> dict[str, list[int]]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 1524-1547
  signature: 'def _attribute_text_matches_to_symbols(self, rg_hits: dict[str, list[int]]) -> dict[str, int]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 1549-1575
  signature: 'def _candidate_matches_predicate(self, detail: SymbolDetail, pred: GrepPredicate) -> bool'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 1577-1649
  signature: 'def _parse_predicate( self, predicate: dict[str, Any] | None ) -> tuple[GrepPredicate, dict[str, Any] | None]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 1653-1716
  signature: 'def read( self, path: str, *, full: bool = False, show_source: bool = False, offset: int | None = None, limit: int | None = None, history: bool = False, ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._strip_line_ref
  lines: 1719-1730
  signature: 'def _strip_line_ref(path: str) -> tuple[str, int | None, int | None]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._resolve_in_root
  lines: 1732-1742
  signature: 'def _resolve_in_root(self, path: str) -> Path | None'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._triefact_view
  lines: 1744-1832
  signature: 'def _triefact_view( self, file_path: str, *, full: bool, history: bool = False ) -> dict[str, Any] | None'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._pending_patches_for_file
  lines: 1834-1875
  signature: 'def _pending_patches_for_file(self, rel_path: str) -> list[dict[str, Any]]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._read_symbol
  lines: 1877-1950
  signature: 'def _read_symbol(self, qname: str, *, history: bool = False) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._digest_history
  lines: 1952-1973
  signature: 'def _digest_history( self, *, qname: str | None = None, module_prefix: str | None = None ) -> list[dict]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._stale_qnames_for_file
  lines: 1975-1997
  signature: 'def _stale_qnames_for_file(self, rel: str, triefact_text: str) -> set[str]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._section_fingerprint
  lines: 1999-2017
  signature: 'def _section_fingerprint(self, detail: SymbolDetail) -> str | None'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._staleness_notes
  lines: 2019-2058
  signature: 'def _staleness_notes(self, detail: SymbolDetail) -> list[str]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 2060-2097
  signature: 'def _prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 2099-2124
  signature: 'def _neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 2128-2282
  signature: 'def trace( self, from_qname: str, direction: str = "callers", depth: int = 2, ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str
  lines: 2286-2445
  signature: 'def grep_str(self, regexp: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str_all
  lines: 2447-2560
  signature: 'def grep_str_all(self, regexp: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read_source
  lines: 2562-2620
  signature: 'def read_source( self, path: str, offset: int | None = None, limit: int | None = None ) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.write_file
  lines: 2622-2682
  signature: 'def write_file(self, path: str, content: str, overwrite: bool = False) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.find_files
  lines: 2684-2755
  signature: 'def find_files(self, pattern: str, all_files: bool = True, limit: int = 100) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_entry_points
  lines: 2757-2848
  signature: 'def grep_entry_points(self, query: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol
  lines: 2850-2963
  signature: 'def grep_symbol(self, sym: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol_and_neighbours
  lines: 2965-2991
  signature: 'def grep_symbol_and_neighbours(self, sym: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol
  lines: 2993-3077
  signature: 'def explain_symbol(self, sym: str, history: bool = False) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol_references
  lines: 3079-3142
  signature: 'def explain_symbol_references(self, sym: str, history: bool = False) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace_flow
  lines: 3144-3202
  signature: 'def trace_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_flow
  lines: 3204-3248
  signature: 'def explain_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]'
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 3252-3268
  signature: 'def _suggest_for_qname(self, qname: str) -> str | None'
- kind: function
  qualified_name: trie/mcp_server:_textified
  lines: 3274-3299
  signature: 'def _textified(fn: Callable[..., dict[str, Any]]) -> Callable[..., str]'
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 3302-3357
  signature: 'def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]'
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 3360-3367
  signature: 'def run_stdio(project_root: Path) -> None'
- kind: function
  qualified_name: trie/mcp_server:main
  lines: 3370-3387
  signature: def main() -> None
incoming_refs: 146
outgoing_refs: 111
---
<!-- trie:section symbol=trie/mcp_server:__module__ fingerprint=17ffdc54657e0bfdb3e4a2487d2cd07a1b53f49c2208d36a374e30e7d4aa395a body_fp=7fe3b54f1ffb2c5cf0bf8fb619733212b2701ce59504815e5ef75a07ada4e768 source_ref=93fb27518b5e02d3c31c00ece47a938ac3545182 role=mcp-server -->
MCP server exposing trie's triefact tree and symbol graph to coding agents over stdio.

- Implements 11 tools split across core operations (grep/read/trace) and agent-ergonomic wrappers
- Uses ripgrep for text search fallbacks when symbol name matching fails
- Provides patch tools for implementation notes and apply operations
- Includes desktop app helpers for project summaries and graph visualization
- Emits telemetry events for usage tracking and performance monitoring
- Shares implementation with CLI subcommands via `TrieTools` class
- Requires ripgrep binary on PATH for text search functionality
- Supports fuzzy matching with rapidfuzz for typo tolerance and conceptual queries
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:RipgrepNotFoundError fingerprint=b95338f0dbd8392f5ddf76b76cd62399af964a45ad4a5b099397463519753605 body_fp=9dd89c53236a428cb88f7e2ebfd279fbb91e549b1bf50ac1b9914fd181d3b70f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `class RipgrepNotFoundError(RuntimeError)`

Raised at MCP server startup when `rg` (ripgrep) is not found on PATH.

- Prevents a half-functional server where symbol-name grep works but text-match fallback fails
- Ensures consistent failure surface rather than runtime surprises during fallback calls
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_require_ripgrep fingerprint=056d3a41463d61526764214f6af30dce4f4833065b63def386f418891f20c4b6 body_fp=dde2bfc0f1faf1b18e9323d53a0eec370d2ad8f20a5156d20342c9827e17ec1a source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _require_ripgrep() -> str`

Returns absolute path to ripgrep binary or raises `RipgrepNotFoundError` on missing dependency.

- Raises `RipgrepNotFoundError`: when `rg` not found on PATH with installation instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_error fingerprint=f03273e5e2d0dd83dacec2ddd314e79331d5cd4f8a08b62b90016be59d9d9fdf body_fp=4bd25aa5e5d971b38931bde34bfd9acc5a39c7887db0ecd869a6ce270f2d537f source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
## `def _error( code: str, message: str, suggestion: str | None = None, *, fix: dict[str, Any] | None = None, ) -> dict[str, Any]`

Constructs standardized error response envelope with code, message, and optional suggestion or executable fix.

- Returns dict with nested `error` object containing the error fields
- `suggestion` field included when a concrete next step can be recommended
- `fix` field provides executable tool call with corrected arguments for one-step recovery
- Agents treat these envelopes as authoritative error responses
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_truncate fingerprint=fc4edfb1b25a174070610aef0283c1a28160f8d6cf1ad2b088deff400629bfbf body_fp=d047fa5abf214e702b632f0eece8be405604cff0e1d7b89dceb204f43db0a7ab source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _truncate(text: str, max_chars: int) -> str`

Truncates text to maximum length, appending ellipsis when clipped.

- max_chars: zero or negative disables truncation
- Returns original text unchanged when under limit
- Strips trailing whitespace before adding ellipsis character
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_symbol_summary fingerprint=2824255ca5be1745ada9b9e40660155f9a55afe2d80dc77fe97f7ace09fc95f8 body_fp=01fd54909c56f58bf46aefcebf6a1548888425951034aa5ebc48a44a6725bb0f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _symbol_summary(detail: SymbolDetail, *, one_liner_max: int) -> dict[str, Any]`

Builds a compact symbol record for inclusion in neighbour and trace-node lists.

- `one_liner_max`: maximum character length for the truncated one-liner field
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_URL_SCHEME_RE fingerprint=18f18a27e6e0184eb570ef37febc856a275228fb6b6a7bc530961aa6306e1e5e body_fp=bbfdffe8ea32ceadaddc6e10f6f8afb708f91df72d3f88b36cdbe3d8e532993a source_ref=387016dec2af121a411a78de8ef480a933c24894 role=model -->
Compiled regex matching RFC-3986 URI schemes (e.g. `http://`, `file://`) used by `_looks_like_qname` to exclude URLs from qname detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_WIN_DRIVE_RE fingerprint=60bdcf932521ff76041df9c5bcb8a4e313f4c356e60861665f160e1218273e50 body_fp=ec5d8536d2145fee8c7c92d25126d249d73644301ea771b1cd7212d65c3cdcb4 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Compiled regex matching a Windows drive prefix (`C:\` or `C:/`) used by `_looks_like_qname` to exclude drive-letter paths from qname detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_looks_like_qname fingerprint=6da576af0ddab05d03937b9de10852bc51154417e5abc1d1d982bf444165810a body_fp=6e7292f96a55afe192ac19d399311346f6a86c6a33bba4c3de088fca4e5065f5 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
## `def _looks_like_qname(s: str) -> bool`

Return `True` when `s` contains `:` but is neither a URL scheme nor a Windows drive prefix, indicating a trie qname shape.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_qname_matches fingerprint=8d18f836065bef2debe8d6c37a2c31524aeaad12ee9bb24aaab8930378225206 body_fp=c7d84dfc0af4761ff5ead056e1a1a7562f4fd34ac41c7832effc278d34b5809c source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=util -->
## `def _close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]`

Fuzzy-match `qname` against candidates using rapidfuzz WRatio, returning up to `n` close matches for "did you mean" suggestions.

- Same-module symbols are ranked first, scored against the local name alone with cutoff 30, ordered by fuzzy score (best first)
- Global qname matches use cutoff 45 and fill remaining slots after same-module hits
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_name_matches fingerprint=78c86c0dfb91a0fc6a7a7cda37db88b68e1caad670ce91e6769b951b0ba033f1 body_fp=5a99924e7cfed4d86fe443c4100ba4857574275351526facb4f4a73004d7b264 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]`

Return top N fuzzy matches for `name` against a candidate set using rapidfuzz WRatio scoring.

- Uses score_cutoff=45 to filter weak matches
- Returns match strings only, not scores or indices
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_fuzzy_score fingerprint=f496bcbab8ac42cd4cdb8ef8b68b4a1214542307bc8330dbcfa37cb9edbed80c body_fp=488c48d19ba8e83065a60fef21301752e9b73aa9bc3513deeed6afb3278e9b93 source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=util -->
## `def _fuzzy_score(query: str, text: str) -> float`

Return a graded 0-100 relevance score for `query` against `text` using four ordered tiers.

- Returns 0.0 when `text` is empty
- Returns 100.0 on case-insensitive exact match
- Returns 92.0 when `text` starts with `query` (prefix match)
- Returns 70.0 + up to 20.0 scaled by `len(query)/len(text)` on substring match
- Otherwise returns rapidfuzz WRatio score
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_is_test_symbol fingerprint=9cbe01b6f47ab812032be5b30ed6aa25e01a34423a3fa3f37997645117b7e20a body_fp=68bb9edc76a96520af6d03c216258a5ae91deb1003528cff686102dcd8102967 source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=util -->
## `def _is_test_symbol(sym: SymbolDetail) -> bool`

Return `True` when `sym`'s file path matches test-code heuristics (`tests/` root, nested `/tests/` dirs, `test_*.py`, or `conftest.py`).

- Used only to deprioritise tests in fuzzy ranking and exclude them from `grep_entry_points`; does not affect predicate-based searches.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_TEST_SCORE_FACTOR fingerprint=8a9a5d6f5d3f92d4522e6a9273714e656aa9d7d452f3ce9077295eb5c68cae76 body_fp=39d4649ccf745697ab6f945f99a1fddf297b31584c67726956d034bef3ed6eaf source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=config -->
Multiplicative penalty applied to test symbols' fuzzy scores so production symbols always outrank equally-scored tests.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_score_sym fingerprint=d700ead428178fb329e8e2a68a3dfc940e5a126bdf51719aabe83ad35beb345a body_fp=8c15e83e87812177f9d1f9c95fc9ee06470e344c716e52ba74981730f211732a source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=util -->
## `def _score_sym( query: str, sym: SymbolDetail, *, prose: str = "", prose_weight: float = 0.6, ) -> float`

Compute composite relevance score (0-100) for a symbol against a query string.

- Takes the max across three weighted fuzzy scores: local name (1.0), one_liner (0.8), and prose body (configurable weight)
- `prose_weight`: controls prose scoring weight, defaults to 0.6 to discount prose-only matches
- Truncates prose to first 2000 chars to avoid scoring on overly long triefact bodies
- Multiplies the score by `_TEST_SCORE_FACTOR` for test symbols so production code wins ties
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_predicate_is_empty fingerprint=0f46c4ac2fd44729683e473ace14c19cacdab7b4def3185826c7c004b4f8aefe body_fp=e1235bd39e3780a55a27f6972f65d6d0cd41e10f9320154aefba0104a83e7328 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _predicate_is_empty(pred: GrepPredicate) -> bool`

Check if a GrepPredicate has no filters that would narrow the result set.

- Returns `True` when all predicate fields are unset or falsy
- Prevents queries that would return alphabetically-first symbols instead of relevant matches
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_smallest_enclosing fingerprint=4839c335a6d869c0fcaaaeb5126b1db1ddeac056279037b8a98dc142a759a02f body_fp=1c3be3bf3748cce21be7967d4e905915b41aa01a94f1d70fd28af1cf433f2c82 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _smallest_enclosing(symbols: list[tuple[str, int, int]], lineno: int) -> str | None`

Find the qname of the symbol whose line range contains `lineno`, preferring nested symbols.

- `symbols`: list of `(qname, start_line, end_line)` tuples ordered by `start_line`
- Returns `None` when `lineno` falls outside all symbol ranges (module-level code)

Iterates through the ordered list, updating `enclosing` with each symbol that brackets `lineno`. Since symbols are start-ordered, the last matching symbol is the most deeply nested one.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=ca4a103644fc4d88e3d32b9247998e76866dff4560d8db29b1023f7408bf0d16 body_fp=5f8b28dd5d236dab4bd8ec50b2c77070a9390e02d07d3d3073cc762820886d9e source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=orchestration -->
## `class TrieTools`

Core interface for MCP tools as plain methods, testable without transport.

Owns the Store and project config for process lifetime. Implements patch tools (patch, batch_patch, create_symbol, delete_symbol, rename_symbol, blast_radius, patch_drop, patch_list, preview, commit), project-level queries (summary, activity, symbols_by_file, file_triefact), three core operations (`grep`, `read`, `trace`), and extended wrappers (grep_str, grep_str_all, read_source, write_file, find_files, grep_entry_points, grep_symbol, grep_symbol_and_neighbours, explain_symbol, explain_symbol_references, trace_flow, explain_flow). All methods return structured dicts with error envelopes; telemetry is captured on each call with configurable event names to distinguish MCP vs CLI usage. `commit` always routes through `record_intent` (no code generation) and its response includes an `uncovered` key listing symbols that still lack a note and would fail the pre-commit gate. `patch_apply` is an alias for `commit(session_note=...)`. `preview` imports from `trie.edits.pipeline`. `_triefact_view` prepends a staleness banner when any section's fingerprint predates the current source; `_read_symbol` prepends staleness notes via `_staleness_notes`; `explain_symbol` likewise folds staleness notes into the response. `read`, `_triefact_view`, `_read_symbol`, `explain_symbol`, and `explain_symbol_references` accept a `history=True` flag to append the symbol's or file's intent trail from the session-digest archive. `batch_patch` applies a graceful create→patch fallback: if a `create` item targets a symbol already in the graph, it is recorded as a `patch` and the result includes `fell_back: True` plus a `created_as_patch` summary list; failed items also include a `did_you_mean` list of close qname matches. `patch` error on unknown qname now leads with fuzzy did-you-mean candidates derived from `_close_qname_matches`. `create_symbol` likewise falls back to `patch` (returning `op: "patch", fell_back: True`) instead of returning an `already_exists` error. `grep` also appends a `related` list when hits are fewer than the limit and `name_contains` is set, filling up with prose/body candidates the name scan missed; the fallback and fuzzy-prose paths accept a `max_matches` cap so result size never exceeds the caller's requested limit. `_staleness_notes` file-level warning advises `trie sync --graph-only`. `grep_entry_points` now fetches `grep_max_limit * 3` raw candidates and post-filters out test symbols before scoring, preventing test fixtures from dominating results on test-heavy repos. `grep_symbol` sort key was extended with `_is_test_symbol` and local-name length tie-breaks so production symbols beat same-scored test symbols deterministically.

- `event_name`: controls telemetry event name emitted on each call ("mcp_call" for MCP server, "cli_call" for CLI)
- `store`: SQLite store containing symbol graph and triefact metadata
- `rg_path`: resolved ripgrep binary path for text search fallbacks
- `_session_id`: unique session identifier for patch operations (injectable via TRIE_SESSION_ID env var, falls back to 12-char hex UUID)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=da31ea5a8dabd217b86c7e6ed605fc3a1d2dbb26bb93f24bc8988024d73a4223 body_fp=031c33365947de2c97b4ef1758a9965448e21caddedf9103186bfbea0baa1486 source_ref=9f9aed9b3a6d7ac7607fb0fc1c4098b064b480a4 role=domain -->
## `def __init__(self, project_root: Path, *, event_name: str = "mcp_call") -> None`

Initialize `TrieTools` with project configuration, telemetry, store, and session state.

- Loads config from project root and validates ripgrep availability at startup
- Configures telemetry from debug settings and emits server start event for MCP path only
- Creates Store connection to graph database and generates session ID from `TRIE_SESSION_ID` env var or UUID
- `event_name`: defaults to `"mcp_call"` for MCP server, `"cli_call"` for CLI usage
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=855daa5089f06200c72619283edee039924ca697931f12e5d1316d4222053338 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def close(self) -> None`

Closes the underlying SQLite store connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch fingerprint=3f3bb06ea78399eba6c952323b7d2b6e1c32b8af23bfb9883095c64bd2f1c306 body_fp=decc33528327cb11c8de131e949694b93145211956475ae69b81883135d9b2cb source_ref=cb4cac77832773abbe5002c3712d8b350d74b5a7 role=domain -->
## `def patch( self, qname: str, note: str = "", source: str = "", reason: str = "", ) -> dict[str, Any]`

TrieTools.patch stages a change to an existing symbol's body, accepting either a generation note or exact source.

- Requires exactly one of `note` (describes change for model generation) or `source` (provides exact new body)
- Returns `{patch_id, qname, mode, pending_patch_count, blast_radius}` on success or error envelope on failure
- `mode`: indicates whether change uses "note" (generative) or "source" (deterministic) approach
- `blast_radius`: compact blast radius metadata showing affected symbols
- Fire-and-forget staging operation; actual change is applied later by `commit()`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.batch_patch fingerprint=7f5f58c861363727cd30f3b962241464c1f1785383421210b0e21a9ee753729c body_fp=f5cb63fd33e7571252cf41d4c89e8238bce2ae03f2b7c59e5a2ef23723e5e5db source_ref=cb4cac77832773abbe5002c3712d8b350d74b5a7 role=domain -->
## `def batch_patch(self, items: list[dict[str, Any]]) -> dict[str, Any]`

Stage multiple patch and create operations in a single `TrieTools` call, collapsing N agent turns into one.

- `items`: list of `{op, qname, note, reason, file_path?, anchor_qname?}` objects; `op` defaults to `"patch"`.
- A `create` item whose qname already exists in the graph is silently downgraded to a `patch`; the result entry carries `fell_back: True`.
- Each item is processed independently; a failed item (including unknown qname) is recorded in `results` with a `did_you_mean` field when close matches exist, but does not abort remaining items.
- Returns `{staged, failed, results, pending_patch_count}`; when any fallbacks occurred, also includes `created_as_patch` and a top-level `note`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._blast_radius_brief fingerprint=b3e0abb2450c94f0f942717710c448d109338c0d7b7e66b81d8bd4b1e99a53c3 body_fp=790ee0434a04829e8835ae484701c165ca0aea0c43ec6391998eefcf8fe626ab source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
## `def _blast_radius_brief(self, qname: str) -> dict[str, Any]`

Computes a compact blast radius summary for patch operations by calling TrieTools.blast_radius and extracting key fields.

- Returns flattened qname list instead of full cascade objects for brevity
- Falls back to empty result on any error to ensure patch operations don't fail
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.create_symbol fingerprint=a1da7556ed0b0bb7f0c823aacb6bffa44aa278b4739b11c65e212b1ed9377093 body_fp=6e2a35d5b0b52b98d78c597728215f737794a64aa1afb1f42b5794db8014cb7d source_ref=9f9aed9b3a6d7ac7607fb0fc1c4098b064b480a4 role=domain -->
## `def create_symbol( self, qname: str, note: str, file_path: str = "", anchor_qname: str = "", reason: str = "", ) -> dict[str, Any]`

Stages creation of a new symbol that doesn't yet exist in the graph; if the symbol already exists, falls back silently to a patch instead of erroring.

- `qname`: intended qualified name (e.g. 'src/foo:helper')
- `note`: description of what the symbol should do (required)
- `file_path`: target source file; when omitted, resolved via registry by probing registered language suffixes for an existing file before falling back to a default suffix
- `anchor_qname`: optionally places it after an existing symbol
- Returns: `{create_patch_id, qname, target_file}` on create, or `{patch_id, qname, op, fell_back, note}` when the symbol already existed
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._resolve_create_target fingerprint=4d6043bb68b9c4df86ae56bc0d46b20a537052e4b80b390437a728cfec5bda69 body_fp=dfedff4dccda02ebd6a7681a0eb10bb940d85a2e5be3908188721bc555639a66 source_ref=c8b279d53ea4a7a3c856c698ff3b034c835ca920 role=util -->
## `def _resolve_create_target(self, qname: str) -> str`

Delegate `TrieTools` new-symbol file resolution to `registry.resolve_create_target`, rooted at `src_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.delete_symbol fingerprint=d6f45a284627050644a0d395eac17c1401e56087cb81088e07700f1daf5f03a4 body_fp=744cf4c26ec80391454c438a7065e4264b0c9d7ad0eb80cf9caee5f9ef550656 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
## `def delete_symbol(self, qname: str, reason: str = "") -> dict[str, Any]`

TrieTools stages symbol deletion, returning the patch ID and list of dependent symbols that reference the target.

- `dependents`: symbols referencing the deleted symbol; agents should decide whether to patch them
- Returns error if symbol not found in graph
- Deletion proceeds at commit regardless of dependents
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.rename_symbol fingerprint=2b959603bd3fce0b8a103483c88ab97358397181cfa841e4140ac6034ed62add body_fp=6242d931c2e401f28a4e9cbde60aaafc912b2e7cd4904438c0aa2e84b7b16d73 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
## `def rename_symbol(self, qname: str, new_name: str, reason: str = "") -> dict[str, Any]`

Stages a rename patch for an existing symbol to `new_name` (the local identifier).

- `new_name`: must be a valid Python identifier
- Returns: patch_id, qname, new_name, and list of reference qnames
- Commit fails if the symbol definition cannot be rewritten unambiguously
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.blast_radius fingerprint=3b543f280fc04f6a21787caa478637a7f569d71115bd6809c7e1b52c26a1dc68 body_fp=251a6d770d58e50230641cb3f87ca0076ec8e5db886b9d86986e84adc746c44a source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=domain -->
## `def blast_radius(self, qname: str) -> dict[str, Any]`

Computes the cascade blast radius of editing a symbol using graph traversal.

- Returns dict with qname, file path, direct hop count, cascade list with hop distances, and total cascade count
- Uses `compute_cascade` with BFS to find all symbols requiring triefact regeneration if the target symbol changes
- Sorts cascade results by hop distance then qname for predictable ordering
- Direct count includes symbols reachable within 1 hop (immediate callers in the same file)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_drop fingerprint=9f462a528298494979bd062e4ee6df1047dbefbe100cb454e031c1e60b0fb54c body_fp=5242ca656168ea06e5ab0b4456fb7a095216a5221879b96cd440df542f87c21d source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=code-editing -->
## `def patch_drop( self, qname: str | None = None, ) -> dict[str, Any]`

TrieTools.patch_drop removes pending patches for a symbol or all patches from the current session.

- `qname`: if provided, removes patches only for that symbol; if omitted, removes all patches created in this session
- Returns `{"removed": int}` indicating count of patches deleted
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_list fingerprint=10fafc96c86486937b1f8eb1844e0bd51c3d1be730fbe1c8bd9eecf21afd4ee7 body_fp=f2abefa1fe03227ffcb70ff04b71720cd63b4a4583c42a69d9a823cbeef776cc source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
## `def patch_list(self) -> dict[str, Any]`

List all pending patches grouped by symbol with count, origin classification, and structural operations.

- **origin**: "cascade" (all patches from cascade), "agent" (all from current session), or "mixed" (multiple sources)
- **kind**: "modify" (default), "delete", or "rename" based on structural patch operations on the symbol
- **creates**: pending create operations with target qname, file, and descriptive note
- **apply_in_progress**: true when another process is currently applying patches
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.preview fingerprint=bf727d0e654de7ec29f76ead945aeabf204f988998e0b3f3949bb751e6f1f32a body_fp=24ca65f3e6183fa9ca19f63397ce2f8976667af13468ae89f3ccc680d9d06bec source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
## `def preview(self) -> dict[str, Any]`

TrieTools.preview shows what commit would do without writing files or paying for generation.

- Returns patch counts, creates list, cascade symbols, and readiness flags
- Sets `needs_session_note` to true when total symbols exceed one
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.commit fingerprint=0420cbbed0b31a4c2ffb1f12705e7aeacaa4e531d68207cda5a19b05d2fb5145 body_fp=9c1205fef83a02a6211ca85adcad7e9ef01d8c045e36d9e81540a0c3130e13aa source_ref=9d1d9295fe9ade9665a214e0a25da2e1a8f04c87 role=domain -->
## `def commit(self, session_note: str = "") -> dict[str, Any]`

Archive all pending patch notes as intent via `record_intent`; no code is generated.

- `session_note`: required when more than one symbol is pending; records unifying intent.
- Always uses the `record_intent` path — the `backend` override and apply lock are removed.
- Returns `{code: "internal"}` error envelope on exception.
- Response includes an `uncovered` key listing touched symbols with no note (would fail the pre-commit gate).
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_apply fingerprint=024a0904ecda7d9180f99812c988ecdbacfd6a753be4dfca14b95fdde5164453 body_fp=266ae59fee44004ff867efa4bc10145b4e1f615e50c1b7c4d72c679af007ee79 source_ref=c921b380767d3408daed50f993e502b6ddb15ca3 role=api -->
## `def patch_apply(self, session_note: str = "") -> dict[str, Any]`

Back-compat alias for `TrieTools.commit()`; now accepts and forwards an optional `session_note` instead of always passing an empty string.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.summary fingerprint=f324310250bed2399715e1f298b6e9f05079ff8db11dff383e0cf9f9a439648b body_fp=00acf98601572d754d180c011c8860542105243684cbcce68a04adac20e88e08 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=domain -->
## `def summary(self) -> dict[str, Any]`

TrieTools returns project-level aggregate statistics by executing SQL count queries against the graph database.

- `project_name`: directory name of the project root
- `project_root`: absolute path to the project root
- `total_symbols`: count of all indexed symbols
- `public_symbols`: count of symbols whose names don't start with underscore
- `total_files`: count of distinct source files containing symbols
- `total_edges`: count of call-graph edges between symbols
- `trie_version`: package version string or "unknown"
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.activity fingerprint=97a479f532fa896bd8ea704a8a54caafc97e86e2693c6730dc8ff29ba51ac13e body_fp=e9bf91219ece316e2240cd17725c20c08e9385abf6e8b94c560780e8a9abf273 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=api -->
## `def activity(self) -> dict[str, Any]`

TrieTools.activity returns live writer status, stale file set, and patch summary for editor polling.

- Reads ephemeral `.trie/activity.db` for sync process state
- Returns dict with `status` object (state, op, pid, current_file, etc), `pending` object (count, stale files, head) or null, `patches` summary (counts by origin), and `apply` object when patch application is active
- Enables editor to show sync progress, stale file badges, and patch status regardless of which process is syncing
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.symbols_by_file fingerprint=d7a64c13443f0221d0ad7fd1df8ac09b24489a77317402484899b99181d047bd body_fp=e3cfd39855f250e984bfd2bbb9ddf22cc9bf51afaea155ee09d0dae087d7e46f source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=persistence -->
## `def symbols_by_file(self, file_path: str) -> dict[str, Any]`

TrieTools.symbols_by_file returns all symbols in a given source file with their metadata.

- Returns dict with `file_path` and `symbols` list containing symbol details
- Symbols ordered by start line ascending within the file
- Used by desktop app sidebar to highlight corresponding graph nodes on file click
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.file_triefact fingerprint=9d0df0145723d2004e0426877e7774869efafb56b45201fdcfdd231014878dec body_fp=f80ddd42037b14ccabfbaffad3de40d0a2f7b74a9e494bc1f98612613be77598 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=api -->
## `def file_triefact(self, file_path: str) -> dict[str, Any]`

TrieTools.file_triefact returns the complete triefact for a source file with front matter and symbol sections.

- `file_path`: source-root relative path like `trie/sync/writer.py`
- Returns dict with `{file_path, triefact_path, exists, front_matter, sections}`
- `exists` is False with empty sections when no triefact file exists yet
- Each section includes qname, kind, role, prose body, fingerprints, and line ranges from store
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep fingerprint=1661aace262a70b21d944c2e5d4ceff9920bcf330df165850d739e4ef4f06ac3 body_fp=6060ff982895ecfa7a3e374fe43e6fbef70ee0e60e203fcfb5ff7983f99110c3 source_ref=9d1d9295fe9ade9665a214e0a25da2e1a8f04c87 role=api -->
## `def grep( self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10, ) -> dict[str, Any]`

Searches the symbol database using a structured predicate with optional text-match fallback.

- `predicate` dict with optional filters: `name_contains` (substring), `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`/`outbound_count` ranges
- `rank_by` controls ordering: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`
- Returns `{hits: [...], fallback?: {...}, related?: [...]}` where hits contain qname, signature, file_pointer, one_liner, counts
- Empty predicates rejected with `invalid_argument` error to prevent unfiltered dumps
- Fallback (capped to `limit`) attempts text search via ripgrep when SQL finds nothing, then fuzzy scoring against names/prose
- SQL hits re-ranked by fuzzy relevance when `name_contains` present to surface closest matches first
- When hits are fewer than `limit` and `name_contains` is set, appends a `related` list of prose/body candidates the name scan missed
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_text_match_fallback fingerprint=91cb80e1935402db28118a16a239f3a2edefa53b0a45dc36f03766378c54ee49 body_fp=c81efee940d90362dad2a75ca951b966a0b0aec66493f344aeac992fdb00325e source_ref=aeff539588cd433cb93b2972de6827c12e81ee83 role=domain -->
## `def _maybe_text_match_fallback( self, pred: GrepPredicate, *, max_matches: int | None = None ) -> dict[str, Any]`

Build fallback response envelope when grep predicate matches no symbols.

Returns a dict with `kind` field indicating why the search failed:

- `"none"` — predicate has no `name_contains` to text-search for
- `"text_match_empty"` — query appears in no source body or only outside symbols  
- `"text_match"` — candidate symbols whose bodies contain the query, ranked by inbound count
- `"fuzzy_prose"` — fuzzy matches against names/one-liners when ripgrep finds nothing
- `max_matches` — additionally caps candidate list below configured limit; callers pass their request's own row budget
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._fuzzy_prose_fallback fingerprint=c39022156b0e966d7a8a314c4ac679456a368b9d2d52ff15cc3f4eae4cc96e5e body_fp=947eb899fbeb09dbd5b22c61558e98491ba192309a073b2c141f604135e01f0c source_ref=aeff539588cd433cb93b2972de6827c12e81ee83 role=domain -->
## `def _fuzzy_prose_fallback( self, query: str, pred: GrepPredicate, *, max_matches: int | None = None ) -> dict[str, Any] | None`

Fuzzy-score all symbols against `query` using name, one_liner, and prose when exact searches fail.

Returns a `fuzzy_prose` fallback envelope or `None` when no candidates clear `fuzzy_cutoff`. Applies predicate filters before scoring for efficiency. Uses lazy prose loading — only reads triefact bodies for symbols passing the `pre_filter` threshold.

- `max_matches`: when provided, further caps the result count below `grep_fallback_match_limit`
- Returns `None`: no candidates above cutoff, caller falls through to `text_match_empty`
- Returns dict with `kind: "fuzzy_prose"`: scored matches sorted by relevance descending
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._text_match_in_scope fingerprint=8b12aa6c5e0bbbbb784c06f111dcb4ced090618f377f50282e2795b08bcf9114 body_fp=ff2c3deb1cb39591cec0f698cfadaeaf10b3b78579735ed8b381612dd7d56c56 source_ref=92d722c79d9b74d00c925144ac0a7b0dcc37fb0d role=io -->
## `def _text_match_in_scope(self, query: str) -> dict[str, list[int]]`

Shell out to ripgrep to find query string in in-scope source files, returning file paths with line numbers.

- Returns `{relative_path: [line_numbers]}` keyed by paths relative to `src_root`
- Runs `rg --json --line-number --fixed-strings --ignore-case` and parses streaming JSON output
- Post-filters results against `discover_files` scope set rather than translating config to rg globs
- Caps accumulation at `grep_fallback_max_files` distinct files to guard against very common substrings
- Raises `RuntimeError` if ripgrep fails with exit code ≥ 2
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._attribute_text_matches_to_symbols fingerprint=638877abde73528dff2831fc527d43a63e2c5f7ea11680e7c835749eab28f9ca body_fp=f184fe4f4896eb91cd954e74d027ebceaac3e7e518b8615d6863ddc7955f156c source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _attribute_text_matches_to_symbols(self, rg_hits: dict[str, list[int]]) -> dict[str, int]`

Attributes ripgrep text matches to their smallest enclosing symbols by line range.

- Returns `{qname: hit_count}` mapping each symbol to its match count
- Drops matches outside any symbol (module-level code, imports, whitespace)
- For nested symbols, picks the innermost one (method over class)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._candidate_matches_predicate fingerprint=67f81def759871cd0f3e53436f8010818ba7ae33393fd206cd91da97251ffc74 body_fp=abea634d62e9b845b55de0a5e7ddcd1d2f893e7133d80f84f0001772c90be208 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _candidate_matches_predicate(self, detail: SymbolDetail, pred: GrepPredicate) -> bool`

Checks whether TrieTools fallback candidate symbol passes all non-name predicate filters.

- Ignores `name_contains` since fallback exists because name didn't match
- Applies scope, visibility, kind, and edge count constraints from original predicate
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=932563e4410469cd038ad9bb8ad1223403b3250aaf122efb34a712cc2be608d9 body_fp=16a2e074ac7eddb9eaa6c53583cab771aea52e750a86820ec481deeeee39ea86 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=parsing -->
## `def _parse_predicate( self, predicate: dict[str, Any] | None ) -> tuple[GrepPredicate, dict[str, Any] | None]`

Parses TrieTools agent predicate dict into GrepPredicate object or returns error envelope.

- Validates field types and value ranges for all grep filter parameters
- `kind` is now validated against the imported `KINDS` constant (expanded set) plus `"any"`, not a hardcoded list
- `_count_range` nested helper validates min/max objects for edge count filters  
- Returns tuple of (GrepPredicate, error_dict_or_None) for uniform error handling
- `scope_exclude` accepts string or list, normalizes to tuple of path prefixes
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=46e507f1cac35bf18c92419134d5f23313010014b37aa774d59db9e257961084 body_fp=c89feee201c2e6c4d3356a0e9f2878c6d5ed8655c0ede5f23d7e0f6427759da1 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=api -->
## `def read( self, path: str, *, full: bool = False, show_source: bool = False, offset: int | None = None, limit: int | None = None, history: bool = False, ) -> dict[str, Any]`

Dispatch reads to the appropriate source based on `path`: symbol qname → `_read_symbol`; file path with triefact → compact or full triefact view; `path:LINE` cursor / `show_source` / `offset`/`limit` → raw numbered source via `read_source`.

- `path`: qname (`pkg/module:Name`), file path, or `file:LINE`/`file:START-END` cursor ref
- `full`: when True, returns every triefact section's full prose instead of the compact per-symbol summary
- `show_source`: forces raw source output regardless of triefact availability
- `offset`/`limit`: 1-indexed line window; implies `show_source` mode
- `history`: when True, appends the symbol's or file's intent trail from the session-digest archive; ignored for raw source reads
- File beats qname when a real on-disk file exists at the colon-bearing path
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._strip_line_ref fingerprint=16fca16e06b72f6ba9d4126a2b3420d235a51949dbfa9b246749caf424caa99b body_fp=d8c4b5c4a6a8232f755b6c041bbc65dabd0b469e9e8ad67abab6f2fdde0cf6f9 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
## `def _strip_line_ref(path: str) -> tuple[str, int | None, int | None]`

Split a trailing `:LINE` or `:START-END` suffix from `path`, returning `(clean_path, offset, limit)` on `TrieTools`.

- `limit`: number of lines in the range; `1` when only a single line number is given; `None` when no suffix is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._resolve_in_root fingerprint=dca3c2c5e29cf37b50351dee85a6ee8e72b17db89e42fe0dbce78c0de166a371 body_fp=adeee5b231daa0befe4affa7f0c76f822fc8f259a781cfa7c7d3c2483ab60a59 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
## `def _resolve_in_root(self, path: str) -> Path | None`

Resolve `path` to an absolute `Path` under the project root, returning `None` if the resolved path escapes it.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._triefact_view fingerprint=caba932f18796ee54530ff2e8577e9584ebc5528b8d9be6268c7822bcfec8074 body_fp=2347a0589aaba853cee10f7a848d0dfefdda2b452e70447196816506be4a8a67 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=domain -->
## `def _triefact_view( self, file_path: str, *, full: bool, history: bool = False ) -> dict[str, Any] | None`

Render `TrieTools`'s triefact for `file_path` as compact summary or full prose; returns `None` when no triefact exists so the caller falls back to raw source.

- `full`: `True` emits every section's full prose via `render_for_agent`; `False` emits a compact per-symbol summary via `compact_triefact_view`.
- `history`: when `True`, appends the file's intent trail from the session-digest archive to `output`.
- Both modes prepend a staleness banner when any section's sentinel fingerprint predates the last-scan fingerprint.
- Returns `{path, mode, output, has_pending_patches, pending_patches?, notes?}` on success; `pending_patches` and `notes` are present only when staged-but-unapplied patches exist for symbols in the file.
- Returns `None` when the triefact file is absent or the path escapes the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._pending_patches_for_file fingerprint=504fcbb6721ec5f593ae24dc44dd1f655d4af26c7e6b95c36ae2766dc265eeaa body_fp=7a7df3586d6eb3365152d6173a91ed03f007a4e66a5c3f79112006c87c0b3435 source_ref=c8b279d53ea4a7a3c856c698ff3b034c835ca920 role=persistence -->
## `def _pending_patches_for_file(self, rel_path: str) -> list[dict[str, Any]]`

Return all pending patch and create records for every symbol whose `file_path` matches `rel_path` in `TrieTools`.

- Returns `[]` silently on any store exception (best-effort).
- Each record: `{qname, op, count, notes}` where `op` is `"patch"` or `"create"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._read_symbol fingerprint=cf34658964c5a0847262855b596adb902404ef09541b702578510f92d5af642f body_fp=57cdb481259d5363502d201678f4f2744d66c455e22418a6e5420bda357c196d source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=domain -->
## `def _read_symbol(self, qname: str, *, history: bool = False) -> dict[str, Any]`

Fetch a single symbol's triefact prose plus compact caller/callee summaries from `TrieTools`, emitting a telemetry span.

- `history` — when `True`, adds a `history` key to the result via `_digest_history`
- `notes` — appended when prose is missing/stale, neighbours are truncated, or the symbol exceeds the hub threshold
- `pending_patches` — included only when patches exist; each entry gains an `origin` tag (`"cascade"` or `"agent"`)
- Returns `not_found` error envelope when `qname` is absent from the store
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._digest_history fingerprint=2ef6fa57a5fc313a8964bb32b428dbe4c123273a4d7ba3a173f00a656f7a41bc body_fp=7c42f1c92f2ca6065458de33c570fcd7d1327ba6011051324447474f74fa40e7 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=persistence -->
## `def _digest_history( self, *, qname: str | None = None, module_prefix: str | None = None ) -> list[dict]`

Return the chronological intent trail for a symbol or module from the session-digest archive, newest first and capped.

- `qname`: returns up to 5 entries via `symbol_history`; takes priority over `module_prefix`.
- `module_prefix`: returns up to 8 entries via `file_history` when `qname` is `None`.
- Returns `[]` on any exception or when neither argument is supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._stale_qnames_for_file fingerprint=c615dbb260e882bfb765581e8fe295f9a491cd7e2322c33da920d89cf8881da2 body_fp=68e4744d4e55d1f4cbfe9b24579dbf4340506ddf6ec83a629ea1ce4cd41d036e source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=domain -->
## `def _stale_qnames_for_file(self, rel: str, triefact_text: str) -> set[str]`

Return the set of qnames in `rel` whose triefact section fingerprint differs from the current symbols-table hash, indicating stale prose.

- `rel`: source-root-relative file path used to query the symbols table.
- `triefact_text`: raw triefact markdown content scanned for section sentinels.
- Symbols the graph no longer tracks are silently skipped (orphan detection is elsewhere).
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._section_fingerprint fingerprint=e52110bed32682aa529d093d56274a31cbcc4fd8f7047075d34b613a8d6d50b7 body_fp=6f32f1b5491a97da4ab5b77034124637889273260b42df4a18a41f2351367114 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=io -->
## `def _section_fingerprint(self, detail: SymbolDetail) -> str | None`

Return the source fingerprint stamped in `detail`'s triefact section sentinel, or `None` when the triefact or section is absent.

- Returns `""` (empty string) when the section exists but carries no fingerprint field.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._staleness_notes fingerprint=ff9c984f504565ed5e4cae13cbed1f0b76e26f6f61e4d8e45112827b413bcac4 body_fp=6152a723e1929b687ddf725763ba4f7eed3a475c601f54fd33dae3ddc44a4601 source_ref=aeff539588cd433cb93b2972de6827c12e81ee83 role=domain -->
## `def _staleness_notes(self, detail: SymbolDetail) -> list[str]`

Return warning strings when `TrieTools` detects that prose being served no longer reflects the current source.

- Checks section-level staleness first: sentinel fingerprint vs last-scan fingerprint; returns early if stale.
- Falls back to file-level staleness: current file content hash vs stored file fingerprint.
- Returns `[]` when both checks pass or on `OSError` reading the source file.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._prose_for fingerprint=7a45e1b328dea006c2f4a127330932dcfd60881d0d728880577bad7bda39f136 body_fp=70dd8348060e277d005d3243b59178092d6307f1b929507629b6edfd711f830f source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=mcp-server -->
## `def _prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]`

Extracts TrieTools prose text for a symbol from its triefact markdown file.

- Returns tuple of (prose_content, diagnostic_notes)
- Searches for symbol's section using regex sentinels rather than YAML parsing
- Truncates prose to configured max length via `read_prose_max_chars`
- Returns empty prose with explanatory notes when triefact file missing or section not found
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._neighbour_summaries fingerprint=f3c2279bac29ff83aa239609a037abaa507bf0e9a1473c10b54bda79be3009ac body_fp=1be802658236edd08cfa8bd721fba2cadd2c16195a9ff50ba04af4d554eb3c4f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]`

TrieTools._neighbour_summaries resolves qnames to compact symbol records with optional truncation.

- Returns tuple of (records, optional_note) where records are compact symbol dictionaries  
- Truncates to `read_max_neighbours_per_direction` limit and returns explanatory note if exceeded
- Skips deleted symbols that no longer exist in the store
- Each record includes qname, signature, and truncated one-liner via `_symbol_summary`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace fingerprint=73eb9bec13d74bd5ae45e72a5b691b87e3520de766924c3208b26e7bdcf3ed26 body_fp=4a11cdb9650216119388360c416c33d4852236b2043b59048d52bae927ecc71d source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
## `def trace( self, from_qname: str, direction: str = "callers", depth: int = 2, ) -> dict[str, Any]`

TrieTools.trace traverses the call graph from a starting symbol using breadth-first search.

- `direction`: "callers", "callees", or "both" to control expansion direction
- `depth`: maximum hops from root (clamped to server limit)
- Returns nodes dict, edges list with direction tags, and root metadata
- Stops expansion through hub symbols (high inbound count) to prevent explosion
- Applies node count limit with BFS ordering from root
- Edges tagged "in" (caller-side) or "out" (callee-side) relative to starting symbol
- `truncated_at` lists hub symbols where expansion was blocked
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str fingerprint=7c92736236e6ccc5c8d906b78b97bcf545f2f54c2e218635cb1851d8a07888ab body_fp=d3de5829f914080ae400a78cef1003fdbd5f157b41520fb2cce869ec81d020e1 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
## `def grep_str(self, regexp: str) -> dict[str, Any]`

TrieTools.grep_str searches source bodies with regex using ripgrep and maps matched lines to enclosing symbols.

- `regexp`: regex pattern to search for in source files
- Returns `{hits: [{qname, signature, file_pointer, one_liner, match_count}]}` or `{hits: [], fallback: {...}}` on no matches
- Falls back to fuzzy symbol name matching when no regex matches found
- Uses ripgrep with `--json`, `--line-number`, `--ignore-case` flags for structured output
- Filters results to project scope and attributes matches to smallest enclosing symbols
- Ranks results by inbound_count descending when multiple symbols match
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str_all fingerprint=8d17cf58b624639da66f21877977a85d3719bd9e1fec2b3f54d7c057d796deaa body_fp=a9a90335a5fd54a8819edf1a6ae27e7094ec286cab788f530ef9d89b9a55e508 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
## `def grep_str_all(self, regexp: str) -> dict[str, Any]`

Searches entire project with regex, returning both symbol hits and plain text matches.

TrieTools method expands beyond indexed files to include all project content (configs, docs, dependencies). Uses ripgrep with gitignore awareness. In-scope matches are attributed to enclosing symbols; out-of-scope matches return as file:line:text records.

- **regexp**: Regular expression pattern to search for
- **Returns**: Dict with `hits` (symbol matches), `text_hits` (plain file matches), and `text_match_count`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read_source fingerprint=ae0368848e00281a549c07164f18c011b572f42df7f66fec538181e603c96965 body_fp=e785b0eee52cbb718953c5ccf8b620e85ccdc193b9bca048f62c5df832f48d95 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
## `def read_source( self, path: str, offset: int | None = None, limit: int | None = None ) -> dict[str, Any]`

TrieTools.read_source reads raw file content with optional windowed line numbering.

Accepts any file path under project root (indexed or not), applies 1-based `offset` and `limit` windowing, returns line-numbered text with each line prefixed by its number. Long lines are clipped at 2000 characters to prevent output bloat.

- `offset`: 1-based starting line (defaults to 1)
- `limit`: maximum lines to return (defaults to whole file)
- Returns: `{path, lines, line_count, offset, more}` where `more` indicates truncation
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.write_file fingerprint=89d7a8ddb06571d55ba21ef12eb5a34ae380f5e8050d79339f31fd0ab313a898 body_fp=173072474c84e1b1e65a18572443583a5a28d04f004d3c39c36c18341f0e4f45 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
## `def write_file(self, path: str, content: str, overwrite: bool = False) -> dict[str, Any]`

TrieTools creates or overwrites arbitrary files under the project root with UTF-8 content.

- Creates parent directories as needed; refuses to overwrite existing files unless `overwrite=True`
- Returns path, bytes written, creation flag, and whether sync is needed for in-scope files
- Validates path is within project root and not a directory before writing
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.find_files fingerprint=439c27ce866653ef6bf9c43e790155269b0cb9b504b5ebc0fc61da634f204277 body_fp=6f17e5b05ef967825bcc03f2f377c127f065f04c9e99ca6d56884dced238e475 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
## `def find_files(self, pattern: str, all_files: bool = True, limit: int = 100) -> dict[str, Any]`

TrieTools.find_files searches for files matching a glob pattern with optional scope restrictions.

- `pattern`: glob pattern (e.g. `**/*.ts`, bare names like `config.json`)  
- `all_files=True`: searches entire project tree; `False` restricts to indexed files
- `limit=100`: maximum results returned, mtime-sorted newest first
- Returns dict with `matches` (relative paths), `match_count`, and `truncated` flag
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_entry_points fingerprint=48736ea5343ad7609b0cd97ce6c9565a5e6387736c9769c278876e1b2ba5f953 body_fp=f15dab28e8a0f734ef859504246562abeb46d5290b7b9b1565cd90722fd396d0 source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=api -->
## `def grep_entry_points(self, query: str) -> dict[str, Any]`

Finds high-traffic public symbols whose triefact prose fuzzy-matches the query string.

- Filters to public symbols with `inbound_count >= 2` as candidate pool; test symbols are excluded before scoring
- Fetches `grep_max_limit * 3` raw candidates then trims to `grep_max_limit` after the test-symbol filter
- Scores on symbol name, one-liner, and triefact prose using fuzzy matching
- Sorts by relevance score descending, then inbound count ascending
- Returns hits with qname, signature, inbound count, prose snippet, and relevance score
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol fingerprint=9d512dc58450425ce810cf234fc573627a3926c86817f007fcb85dcaec6235a5 body_fp=8508a391b64160cb0ab79f2d35fbe8925a502d4a564b0fc840059a71c34008d9 source_ref=f0193a6b7b7fab56bcbd2ee55d7eb86792976b97 role=domain -->
## `def grep_symbol(self, sym: str) -> dict[str, Any]`

Fuzzy symbol name lookup returning the best match plus similar symbols with relevance scores.

TrieTools.grep_symbol performs three-phase matching: SQL substring search for fast candidates, rapidfuzz fallback against all symbol names when SQL finds nothing, then name/one_liner/prose scoring with lazy prose reads. Returns the highest-scoring match with up to 9 similar alternatives, each carrying a 0-100 relevance score. Better than grep for typo tolerance and discovering related symbols in one call.

- Uses rapidfuzz WRatio scoring with configurable cutoffs and prose weight
- SQL LIKE phase pulls up to 20 candidates, re-ranked by fuzzy score
- Fallback phase searches all symbol names with score cutoff 45
- Prose augmentation only for candidates clearing the pre-filter threshold
- Tie-breaks: score desc → production before tests → shorter local name → qname (deterministic)
- Returns match object with qname/kind/signature/score plus similar list
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol_and_neighbours fingerprint=7ea37438f4dc626cbdbb108b54c36c9dc7731a3b134e51c78f5228e1295929ad body_fp=04f7806dac5ada374fc8f831781805f98fc57c263977cc8137b6f05235dd2da4 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def grep_symbol_and_neighbours(self, sym: str) -> dict[str, Any]`

TrieTools method extends grep_symbol to include immediate caller and callee metadata for the best match.

Combines fuzzy symbol lookup with neighbourhood exploration in a single round trip. Returns the same structure as grep_symbol plus trimmed summaries of direct references. Used for symbol orientation without separate read calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol fingerprint=ec6c9df2f6e2fd37c306c0ddc5a4533af8f1a333ab180ca986dd49ba6a498891 body_fp=0ef24b5cb027d037041eecb1a44541bc77ff9d2ae3461018350b21a4a42c3d31 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=api -->
## `def explain_symbol(self, sym: str, history: bool = False) -> dict[str, Any]`

TrieTools.explain_symbol returns full prose for a symbol plus a narrative story weaving together its callers and callees.

- `sym`: symbol name or qname (uses fuzzy resolution if exact match fails)
- `history`: when True, appends `_digest_history` intent trail under `out["history"]`
- Returns dict with `qname`, `signature`, `source_pointer`, `prose`, `story`, `callers`, `callees`, optional `notes`, optional `history`
- `notes` prepends staleness warnings (from `_staleness_notes`) before any prose-generation notes
- Story includes first paragraph of prose from up to 5 callers/callees under "Called by:" and "Calls into:" sections
- Telemetry tracks result kind, prose/story character counts, and response size
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol_references fingerprint=2a49b14331cbf83b57abb1d76da27ac245404ce8e48bec57af742e8491abbeeb body_fp=22a5bd57fb62ff220e191919283b0f85ef69cc610efaf20c2cfddf6122c3c159 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=domain -->
## `def explain_symbol_references(self, sym: str, history: bool = False) -> dict[str, Any]`

TrieTools.explain_symbol_references explains how a symbol is used by building a usage story from caller prose.

- Resolves the symbol name via fuzzy search if not found directly
- Builds usage narrative from the first paragraph of each caller's prose
- Limits to 8 callers for the usage story, all callers for the summary list
- `history=True` appends the symbol's intent trail from the digest archive as `result["history"]`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace_flow fingerprint=4dd9d61ff701bd2992e0aa4e9b3b5d43ff52b010a1562bc193ddaa229de437b6 body_fp=1152263488e2ce7e072e04b81695ab831576f711d24d264df7051a790a1c91d8 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def trace_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]`

TrieTools.trace_flow finds call chains between two symbols using graph pathfinding.

- `symbol1`, `symbol2`: accepts exact qnames or fuzzy symbol names via grep_symbol resolution
- Returns dict with `from_qname`, `to_qname`, `paths` (list of qname lists), optional `notes`
- Searches up to `trace_max_depth` hops, skips hub symbols above threshold, returns max 3 paths
- Empty paths list with explanatory note when no connection found within depth limit
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_flow fingerprint=47e5b35007183ceaa63f7a11cb99ebc79fbbbce4788c1bd0ecfe4c5e0a088870 body_fp=aa882bc1e27eec77de8a4f629fc6984b8fd70fe1810939dcecd8f93b78feb478 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def explain_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]`

TrieTools method that finds call chains between symbols and weaves their triefact prose into readable execution narratives.

- Uses `trace_flow` to find paths, then enriches each path step with prose snippets
- Returns `paths` as list of `{chain: [qname,...], narrative: str}` dictionaries
- Narrative joins symbol prose with "→" separators to show execution flow story
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._suggest_for_qname fingerprint=5ac22b4d30b52fa3bf0f60a18bdbf94c7855456a7fa9b25fca44752526dc1a98 body_fp=342b0450319df27d0d1fb9956e834793460ede136c31d11334b12ae082a286bb source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def _suggest_for_qname(self, qname: str) -> str | None`

Generate suggestion text for `not_found` errors by fuzzy-matching the failed qname against all symbols.

- Returns help text with close matches, or fallback instructions when no close matches exist
- Uses qualified name matching first, then falls back to local name matching if no qname matches
- Returns None only when no fuzzy matches are found (rare case)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_textified fingerprint=efb8cbe7e50b64d4210f88926ca4c7da3c63a464581af9abdd992ef4a10f2ee1 body_fp=200b8fe92db820d87fb6dfbd30c58e16f8067ed385017545f890d6112d98b0b6 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=util -->
## `def _textified(fn: Callable[..., dict[str, Any]]) -> Callable[..., str]`

Wrap a dict-returning `TrieTools` method to return rendered text instead of a raw dict, preserving the original name, docstring, and parameter signature.

- Calls `render_envelope` on dict results; falls back to `str()` for non-dicts.
- Patches `__signature__` and `__annotations__` so FastMCP sees `-> str` in the schema.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=87bef781a4ae79f4586d0a033fa7098f7240a2d79c9b3d395ae9d1ea28730a2e body_fp=1d1f142abadaf0cf1335c323a98069804e54a1415941ce58522e6c56ba7b7ef2 source_ref=06483f7e76e96388684de7b91d0c1fcc2799c663 role=orchestration -->
## `def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct an MCP server with all trie tools registered from a TrieTools instance.

- Returns tuple of (FastMCP server, TrieTools) for testing and CLI reuse
- Query tools (grep/read/trace family, extended search/explain, file tools, project-level queries) are wrapped with `_textified` so the wire carries rendered text instead of JSON; `write_file` is the sole query-side exception and stays structured
- Edit tools (patch/batch_patch/create/delete/rename/preview/commit/drop/list/apply) remain structured so callers can branch on envelope fields
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=c57b100fd07ba8bcfcaedebb2648cbe5949b2106b69128d814bb6c633382c744 body_fp=ae4a366a90b814246236fc572678a53ef3dad84591b478c5ec3ab6fe3fb0e650 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
## `def run_stdio(project_root: Path) -> None`

Run the MCP server over stdio for the project at `project_root`.

- Configures stdout and stderr for line buffering to ensure prompt output
- Blocks until the parent process closes the pipe
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:main fingerprint=cae2a0ae09ead6d8ca05631fe03f2b4e857ad2666fbccf4fd92eb04c469dd2ac body_fp=ab1a15c30322f7e836ee44709db02a83b5e7f4672584b52a6e4e364e2640f2c4 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=entrypoint -->
## `def main() -> None`

Parse `sys.argv[1]` as a project directory and delegate to `run_stdio`, exiting with an error message if the argument is missing or the path does not exist.
<!-- trie:end -->