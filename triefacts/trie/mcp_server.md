---
trie_version: 0.1.9
source: trie/mcp_server.py
file_fingerprint: 5c2e0367220f5d603f53cc3efc1a52cca83489eb4edddde10a25638debc225ac
last_synced_at: '2026-07-26T20:28:18Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-3175
- kind: class
  qualified_name: trie/mcp_server:RipgrepNotFoundError
  lines: 77-89
- kind: function
  qualified_name: trie/mcp_server:_require_ripgrep
  lines: 92-107
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 110-129
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 132-136
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 139-145
- kind: constant
  qualified_name: trie/mcp_server:_URL_SCHEME_RE
  lines: 148-148
- kind: constant
  qualified_name: trie/mcp_server:_WIN_DRIVE_RE
  lines: 149-149
- kind: function
  qualified_name: trie/mcp_server:_looks_like_qname
  lines: 152-165
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 168-171
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 174-176
- kind: function
  qualified_name: trie/mcp_server:_fuzzy_score
  lines: 179-190
- kind: function
  qualified_name: trie/mcp_server:_score_sym
  lines: 193-218
- kind: function
  qualified_name: trie/mcp_server:_predicate_is_empty
  lines: 221-244
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 247-266
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 269-3092
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 283-312
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 314-315
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch
  lines: 319-362
- kind: method
  qualified_name: trie/mcp_server:TrieTools.batch_patch
  lines: 364-443
- kind: method
  qualified_name: trie/mcp_server:TrieTools._blast_radius_brief
  lines: 445-458
- kind: method
  qualified_name: trie/mcp_server:TrieTools.create_symbol
  lines: 460-504
- kind: method
  qualified_name: trie/mcp_server:TrieTools._resolve_create_target
  lines: 506-510
- kind: method
  qualified_name: trie/mcp_server:TrieTools.delete_symbol
  lines: 512-534
- kind: method
  qualified_name: trie/mcp_server:TrieTools.rename_symbol
  lines: 536-558
- kind: method
  qualified_name: trie/mcp_server:TrieTools.blast_radius
  lines: 560-607
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_drop
  lines: 609-622
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_list
  lines: 624-664
- kind: method
  qualified_name: trie/mcp_server:TrieTools.preview
  lines: 666-691
- kind: method
  qualified_name: trie/mcp_server:TrieTools.commit
  lines: 693-712
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_apply
  lines: 715-717
- kind: method
  qualified_name: trie/mcp_server:TrieTools.summary
  lines: 719-745
- kind: method
  qualified_name: trie/mcp_server:TrieTools.activity
  lines: 747-800
- kind: method
  qualified_name: trie/mcp_server:TrieTools.symbols_by_file
  lines: 802-841
- kind: method
  qualified_name: trie/mcp_server:TrieTools.file_triefact
  lines: 843-904
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 908-1040
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 1042-1187
- kind: method
  qualified_name: trie/mcp_server:TrieTools._fuzzy_prose_fallback
  lines: 1189-1265
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 1267-1366
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 1368-1391
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 1393-1419
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 1421-1493
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 1497-1560
- kind: method
  qualified_name: trie/mcp_server:TrieTools._strip_line_ref
  lines: 1563-1574
- kind: method
  qualified_name: trie/mcp_server:TrieTools._resolve_in_root
  lines: 1576-1586
- kind: method
  qualified_name: trie/mcp_server:TrieTools._triefact_view
  lines: 1588-1676
- kind: method
  qualified_name: trie/mcp_server:TrieTools._pending_patches_for_file
  lines: 1678-1719
- kind: method
  qualified_name: trie/mcp_server:TrieTools._read_symbol
  lines: 1721-1794
- kind: method
  qualified_name: trie/mcp_server:TrieTools._digest_history
  lines: 1796-1817
- kind: method
  qualified_name: trie/mcp_server:TrieTools._stale_qnames_for_file
  lines: 1819-1841
- kind: method
  qualified_name: trie/mcp_server:TrieTools._section_fingerprint
  lines: 1843-1861
- kind: method
  qualified_name: trie/mcp_server:TrieTools._staleness_notes
  lines: 1863-1902
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 1904-1941
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 1943-1968
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 1972-2126
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str
  lines: 2130-2289
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str_all
  lines: 2291-2404
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read_source
  lines: 2406-2464
- kind: method
  qualified_name: trie/mcp_server:TrieTools.write_file
  lines: 2466-2526
- kind: method
  qualified_name: trie/mcp_server:TrieTools.find_files
  lines: 2528-2599
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_entry_points
  lines: 2601-2684
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol
  lines: 2686-2787
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol_and_neighbours
  lines: 2789-2815
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol
  lines: 2817-2901
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol_references
  lines: 2903-2966
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace_flow
  lines: 2968-3026
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_flow
  lines: 3028-3072
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 3076-3092
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 3098-3144
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 3147-3154
- kind: function
  qualified_name: trie/mcp_server:main
  lines: 3157-3174
incoming_refs: 13
outgoing_refs: 67
---
<!-- trie:section symbol=trie/mcp_server:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=7fe3b54f1ffb2c5cf0bf8fb619733212b2701ce59504815e5ef75a07ada4e768 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
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
<!-- trie:section symbol=trie/mcp_server:RipgrepNotFoundError fingerprint=b95338f0dbd8392f5ddf76b76cd62399af964a45ad4a5b099397463519753605 body_fp=c82ea042863f0dcd469c37c161ecb8ef3bf13ac828ab66aa205856723e0568b0 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Raised at MCP server startup when `rg` (ripgrep) is not found on PATH.

- Prevents a half-functional server where symbol-name grep works but text-match fallback fails
- Ensures consistent failure surface rather than runtime surprises during fallback calls
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_require_ripgrep fingerprint=056d3a41463d61526764214f6af30dce4f4833065b63def386f418891f20c4b6 body_fp=09676b6e74821419b61116ce4674c7a7de74e7e48c889301710963697f14e9cf source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Returns absolute path to ripgrep binary or raises `RipgrepNotFoundError` on missing dependency.

- Raises `RipgrepNotFoundError`: when `rg` not found on PATH with installation instructions
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_error fingerprint=f03273e5e2d0dd83dacec2ddd314e79331d5cd4f8a08b62b90016be59d9d9fdf body_fp=4c8c503b0e00ef9e0dc12e0739304519aff29bdf880b178682e2faad6ee34e26 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
Constructs standardized error response envelope with code, message, and optional suggestion or executable fix.

- Returns dict with nested `error` object containing the error fields
- `suggestion` field included when a concrete next step can be recommended
- `fix` field provides executable tool call with corrected arguments for one-step recovery
- Agents treat these envelopes as authoritative error responses
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_truncate fingerprint=fc4edfb1b25a174070610aef0283c1a28160f8d6cf1ad2b088deff400629bfbf body_fp=77d89908f6a75c7073105ad79b89dc5c84b115ad10257a68d2edbcf522d654dd source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Truncates text to maximum length, appending ellipsis when clipped.

- max_chars: zero or negative disables truncation
- Returns original text unchanged when under limit
- Strips trailing whitespace before adding ellipsis character
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_symbol_summary fingerprint=2824255ca5be1745ada9b9e40660155f9a55afe2d80dc77fe97f7ace09fc95f8 body_fp=1d857004a2942506021f71bf25ad767dd4d38b87fdd47f5066c1894a9cd40416 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Builds a compact symbol record for inclusion in neighbour and trace-node lists.

- `one_liner_max`: maximum character length for the truncated one-liner field
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_URL_SCHEME_RE fingerprint=18f18a27e6e0184eb570ef37febc856a275228fb6b6a7bc530961aa6306e1e5e body_fp=bbfdffe8ea32ceadaddc6e10f6f8afb708f91df72d3f88b36cdbe3d8e532993a source_ref=387016dec2af121a411a78de8ef480a933c24894 role=model -->
Compiled regex matching RFC-3986 URI schemes (e.g. `http://`, `file://`) used by `_looks_like_qname` to exclude URLs from qname detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_WIN_DRIVE_RE fingerprint=60bdcf932521ff76041df9c5bcb8a4e313f4c356e60861665f160e1218273e50 body_fp=ec5d8536d2145fee8c7c92d25126d249d73644301ea771b1cd7212d65c3cdcb4 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Compiled regex matching a Windows drive prefix (`C:\` or `C:/`) used by `_looks_like_qname` to exclude drive-letter paths from qname detection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_looks_like_qname fingerprint=6da576af0ddab05d03937b9de10852bc51154417e5abc1d1d982bf444165810a body_fp=240f08ff0e6a02a5d6ae5d17663a6030d65c2ea289b8054be4bc7cd98776fb9a source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Return `True` when `s` contains `:` but is neither a URL scheme nor a Windows drive prefix, indicating a trie qname shape.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_qname_matches fingerprint=501f57c95b68de44bbc214d45d865ab70c8460555e35a1a55da2d4271bee3666 body_fp=f7d870e92d347c39faa4d259e4a6b7e9047aa17d797a2520dbfea03ddd663c97 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Fuzzy-match `qname` against candidates using rapidfuzz WRatio, returning up to `n` matches above score 45.

- Used for generating "did you mean" suggestions in not_found error responses
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_name_matches fingerprint=78c86c0dfb91a0fc6a7a7cda37db88b68e1caad670ce91e6769b951b0ba033f1 body_fp=495dd9332e9237d1c2befbf424cc7f55ba9bcc1f505d8d2384f5b68826c82179 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Return top N fuzzy matches for `name` against a candidate set using rapidfuzz WRatio scoring.

- Uses score_cutoff=45 to filter weak matches
- Returns match strings only, not scores or indices
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_fuzzy_score fingerprint=df1930a7033c1b75555083d67164a88ea342c7c428aef37d59a7a7a604a6f23b body_fp=3b3658d7427092aab98e20a4ddfe3524a177984e666d613ee7fa466ecfd5e580 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Returns fuzzy match score (0-100) for query against text, short-circuiting to 100.0 on exact substring.

- Returns 0.0 when text is empty
- Returns 100.0 when query is a case-insensitive substring of text
- Otherwise returns rapidfuzz WRatio score between query and text
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_score_sym fingerprint=7e3bbbed40177fcdb72361bc232f83c84a1484192b11a66452b2d23aee321f0f body_fp=ba8918934d6f21c7fb0467769278825218eb34375cfe0218f91b7e49027e7a39 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Compute composite relevance score (0-100) for a symbol against a query string.

- Takes the max across three weighted fuzzy scores: local name (1.0), one_liner (0.8), and prose body (configurable weight)
- `prose_weight`: controls prose scoring weight, defaults to 0.6 to discount prose-only matches
- Truncates prose to first 2000 chars to avoid scoring on overly long triefact bodies
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_predicate_is_empty fingerprint=0f46c4ac2fd44729683e473ace14c19cacdab7b4def3185826c7c004b4f8aefe body_fp=8a7996aa1caeca5300bdca4d43abcd01bda6b384fae6f91ecb0a07f6d408263b source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Check if a GrepPredicate has no filters that would narrow the result set.

- Returns `True` when all predicate fields are unset or falsy
- Prevents queries that would return alphabetically-first symbols instead of relevant matches
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_smallest_enclosing fingerprint=4839c335a6d869c0fcaaaeb5126b1db1ddeac056279037b8a98dc142a759a02f body_fp=24e2ccaf9e8c9ccc547f6319f50eb7444ab2396e59f526ecbbeaf932f006b64e source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Find the qname of the symbol whose line range contains `lineno`, preferring nested symbols.

- `symbols`: list of `(qname, start_line, end_line)` tuples ordered by `start_line`
- Returns `None` when `lineno` falls outside all symbol ranges (module-level code)

Iterates through the ordered list, updating `enclosing` with each symbol that brackets `lineno`. Since symbols are start-ordered, the last matching symbol is the most deeply nested one.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=3355dd5c359acbd8ca1b80332d68d3d98f2a357e00ea2c961b54da7f08f4c790 body_fp=384daf997b9c12048b7f7b493d139bcf04114db4d969fde00f01aa8c9b62c942 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=orchestration -->
Core interface for MCP tools as plain methods, testable without transport.

Owns the Store and project config for process lifetime. Implements patch tools (patch, batch_patch, create_symbol, delete_symbol, rename_symbol, blast_radius, patch_drop, patch_list, preview, commit), project-level queries (summary, activity, symbols_by_file, file_triefact), three core operations (`grep`, `read`, `trace`), and extended wrappers (grep_str, grep_str_all, read_source, write_file, find_files, grep_entry_points, grep_symbol, grep_symbol_and_neighbours, explain_symbol, explain_symbol_references, trace_flow, explain_flow). All methods return structured dicts with error envelopes; telemetry is captured on each call with configurable event names to distinguish MCP vs CLI usage. `commit` always routes through `record_intent` (no code generation). `patch_apply` is an alias for `commit(session_note=...)`. `preview` imports from `trie.edits.pipeline`. `_triefact_view` prepends a staleness banner when any section's fingerprint predates the current source; `_read_symbol` prepends staleness notes via `_staleness_notes`; `explain_symbol` likewise folds staleness notes into the response. `read`, `_triefact_view`, `_read_symbol`, `explain_symbol`, and `explain_symbol_references` accept a `history=True` flag to append the symbol's or file's intent trail from the session-digest archive.

- `event_name`: controls telemetry event name emitted on each call ("mcp_call" for MCP server, "cli_call" for CLI)
- `store`: SQLite store containing symbol graph and triefact metadata
- `rg_path`: resolved ripgrep binary path for text search fallbacks
- `_session_id`: unique session identifier for patch operations (injectable via TRIE_SESSION_ID env var, falls back to 12-char hex UUID)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=da31ea5a8dabd217b86c7e6ed605fc3a1d2dbb26bb93f24bc8988024d73a4223 body_fp=3f1442d7ffaffd877c13b2fbb819d2a8be0aafd969463aa996f25077eca51c52 source_ref=31ea5773e72df0b09ea019dcab835d5205588818 role=domain -->
Initialize `TrieTools` with project configuration, telemetry, store, and session state.

- Loads config from project root and validates ripgrep availability at startup
- Configures telemetry from debug settings and emits server start event for MCP path only
- Creates Store connection to graph database and generates session ID from `TRIE_SESSION_ID` env var or UUID
- `event_name`: defaults to `"mcp_call"` for MCP server, `"cli_call"` for CLI usage
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=9967aa9f46cd1703a5cfd1ae72d466503e42628bc1c5d81769b7301acc822ebf source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Closes the underlying SQLite store connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch fingerprint=fcf87bb6129a3ebe3f0005064f09ff20191671eaed19c5836013fb305c11676c body_fp=79f3b11786499e39963078d829e7c2a106c4f735f85f328b236d9a9e30018260 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
TrieTools.patch stages a change to an existing symbol's body, accepting either a generation note or exact source.

- Requires exactly one of `note` (describes change for model generation) or `source` (provides exact new body)
- Returns `{patch_id, qname, mode, pending_patch_count, blast_radius}` on success or error envelope on failure
- `mode`: indicates whether change uses "note" (generative) or "source" (deterministic) approach
- `blast_radius`: compact blast radius metadata showing affected symbols
- Fire-and-forget staging operation; actual change is applied later by `commit()`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.batch_patch fingerprint=88d487764445c34688c6f3a819eee86fcb3eaebc3b5263bfc90bbaf3d326a85f body_fp=799a7e5d2d0e226d1b005b4e85313fc4368cacd997f9713d567f708470990110 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
Stage multiple patch and create operations in a single `TrieTools` call, collapsing N agent turns into one.

- `items`: list of `{op, qname, note, reason, file_path?, anchor_qname?}` objects; `op` defaults to `"patch"`.
- Each item is processed independently; a failed item is recorded in `results` but does not abort remaining items.
- Returns `{staged, failed, results, pending_patch_count}`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._blast_radius_brief fingerprint=b3e0abb2450c94f0f942717710c448d109338c0d7b7e66b81d8bd4b1e99a53c3 body_fp=035a0df8c5bccdfb1898ca4a38b4afe434273df9a4fb0810bc70d198b11e54ed source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
Computes a compact blast radius summary for patch operations by calling TrieTools.blast_radius and extracting key fields.

- Returns flattened qname list instead of full cascade objects for brevity
- Falls back to empty result on any error to ensure patch operations don't fail
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.create_symbol fingerprint=f029bf408ba4161b8ad68cac54db7e13c19883791fde4a9a8df3bed5bacb517e body_fp=04db2cf65c048191eb7975184a9cfe39037b6e330a70765c223965ff3f3bc7b3 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
Stages creation of a new symbol that doesn't yet exist in the graph.

- `qname`: intended qualified name (e.g. 'src/foo:helper')
- `note`: description of what the symbol should do (required)
- `file_path`: target source file; when omitted, resolved via registry by probing registered language suffixes for an existing file before falling back to a default suffix
- `anchor_qname`: optionally places it after an existing symbol
- Returns: `{create_patch_id, qname, target_file}`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._resolve_create_target fingerprint=4d6043bb68b9c4df86ae56bc0d46b20a537052e4b80b390437a728cfec5bda69 body_fp=f046ccf387115877ce6c9ab6dc4ba432a9d5e280357e8f7f05f713140bafcd9a source_ref=c8b279d53ea4a7a3c856c698ff3b034c835ca920 role=util -->
Delegate `TrieTools` new-symbol file resolution to `registry.resolve_create_target`, rooted at `src_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.delete_symbol fingerprint=d6f45a284627050644a0d395eac17c1401e56087cb81088e07700f1daf5f03a4 body_fp=3aca70cd1bbb8e1c5e8fbb746940565d5f2d8c6bf645797fca7ad35b6587726e source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
TrieTools stages symbol deletion, returning the patch ID and list of dependent symbols that reference the target.

- `dependents`: symbols referencing the deleted symbol; agents should decide whether to patch them
- Returns error if symbol not found in graph
- Deletion proceeds at commit regardless of dependents
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.rename_symbol fingerprint=2b959603bd3fce0b8a103483c88ab97358397181cfa841e4140ac6034ed62add body_fp=e0b2e53f5bd66983579b84eb34933abbd5eb786ab245b579d2e6e49415619e1c source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
Stages a rename patch for an existing symbol to `new_name` (the local identifier).

- `new_name`: must be a valid Python identifier
- Returns: patch_id, qname, new_name, and list of reference qnames
- Commit fails if the symbol definition cannot be rewritten unambiguously
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.blast_radius fingerprint=3b543f280fc04f6a21787caa478637a7f569d71115bd6809c7e1b52c26a1dc68 body_fp=aa112e9ab438f72b61a977ee93f17830df1514634f4fa71d1a72f6bdb6052f94 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=domain -->
Computes the cascade blast radius of editing a symbol using graph traversal.

- Returns dict with qname, file path, direct hop count, cascade list with hop distances, and total cascade count
- Uses `compute_cascade` with BFS to find all symbols requiring triefact regeneration if the target symbol changes
- Sorts cascade results by hop distance then qname for predictable ordering
- Direct count includes symbols reachable within 1 hop (immediate callers in the same file)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_drop fingerprint=9f462a528298494979bd062e4ee6df1047dbefbe100cb454e031c1e60b0fb54c body_fp=bec0a605bff504767d40a57025a61da071b093d6225cc5c710d94719b1b34eb9 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=code-editing -->
TrieTools.patch_drop removes pending patches for a symbol or all patches from the current session.

- `qname`: if provided, removes patches only for that symbol; if omitted, removes all patches created in this session
- Returns `{"removed": int}` indicating count of patches deleted
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_list fingerprint=10fafc96c86486937b1f8eb1844e0bd51c3d1be730fbe1c8bd9eecf21afd4ee7 body_fp=590c68d015559341b2cb06a1a99dc0bddd0d5c08a48872ea35c188179d90b7b1 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
List all pending patches grouped by symbol with count, origin classification, and structural operations.

- **origin**: "cascade" (all patches from cascade), "agent" (all from current session), or "mixed" (multiple sources)
- **kind**: "modify" (default), "delete", or "rename" based on structural patch operations on the symbol
- **creates**: pending create operations with target qname, file, and descriptive note
- **apply_in_progress**: true when another process is currently applying patches
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.preview fingerprint=bf727d0e654de7ec29f76ead945aeabf204f988998e0b3f3949bb751e6f1f32a body_fp=872e67048b726b58cc7c76fed68ef704d867b1efdd68ff81a9d9e0948fcd487c source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
TrieTools.preview shows what commit would do without writing files or paying for generation.

- Returns patch counts, creates list, cascade symbols, and readiness flags
- Sets `needs_session_note` to true when total symbols exceed one
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.commit fingerprint=7883ea0d81c4a472962bccbaead6b0b7e52a54711306269fdab58da7a4e1eed8 body_fp=8ea1b96e01b02e5139302136b21c02142cebe4baa8413aaa67d4e96f45190f55 source_ref=c921b380767d3408daed50f993e502b6ddb15ca3 role=domain -->
Archive all pending patch notes as intent via `record_intent`; no code is generated.

- `session_note`: required when more than one symbol is pending; records unifying intent.
- Always uses the `record_intent` path — the `backend` override and apply lock are removed.
- Returns `{code: "internal"}` error envelope on exception.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_apply fingerprint=024a0904ecda7d9180f99812c988ecdbacfd6a753be4dfca14b95fdde5164453 body_fp=43930a6144854de6e6143dfb9822a12bf664a28d827de60b14b7c4c8abc77a1a source_ref=c921b380767d3408daed50f993e502b6ddb15ca3 role=api -->
Back-compat alias for `TrieTools.commit()`; now accepts and forwards an optional `session_note` instead of always passing an empty string.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.summary fingerprint=f324310250bed2399715e1f298b6e9f05079ff8db11dff383e0cf9f9a439648b body_fp=b1de55753ce5e944089a958c45d4a2f6c8f163328e8984a93635a45f5946f2d3 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=domain -->
TrieTools returns project-level aggregate statistics by executing SQL count queries against the graph database.

- `project_name`: directory name of the project root
- `project_root`: absolute path to the project root
- `total_symbols`: count of all indexed symbols
- `public_symbols`: count of symbols whose names don't start with underscore
- `total_files`: count of distinct source files containing symbols
- `total_edges`: count of call-graph edges between symbols
- `trie_version`: package version string or "unknown"
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.activity fingerprint=97a479f532fa896bd8ea704a8a54caafc97e86e2693c6730dc8ff29ba51ac13e body_fp=130f441ba10806d9c22863021b38b028d23a9c9efef22f6278e1c8116d9c8bd4 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=api -->
TrieTools.activity returns live writer status, stale file set, and patch summary for editor polling.

- Reads ephemeral `.trie/activity.db` for sync process state
- Returns dict with `status` object (state, op, pid, current_file, etc), `pending` object (count, stale files, head) or null, `patches` summary (counts by origin), and `apply` object when patch application is active
- Enables editor to show sync progress, stale file badges, and patch status regardless of which process is syncing
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.symbols_by_file fingerprint=d7a64c13443f0221d0ad7fd1df8ac09b24489a77317402484899b99181d047bd body_fp=c8ad00c51cc8cb0f9ba66d2dad0a4e7325165c931755b1888857def48c88f307 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=persistence -->
TrieTools.symbols_by_file returns all symbols in a given source file with their metadata.

- Returns dict with `file_path` and `symbols` list containing symbol details
- Symbols ordered by start line ascending within the file
- Used by desktop app sidebar to highlight corresponding graph nodes on file click
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.file_triefact fingerprint=9d0df0145723d2004e0426877e7774869efafb56b45201fdcfdd231014878dec body_fp=ed47071f8ef4d957aa8e62c01f0c75928e3cf695b48192f01df7f9649e5b7be0 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=api -->
TrieTools.file_triefact returns the complete triefact for a source file with front matter and symbol sections.

- `file_path`: source-root relative path like `trie/sync/writer.py`
- Returns dict with `{file_path, triefact_path, exists, front_matter, sections}`
- `exists` is False with empty sections when no triefact file exists yet
- Each section includes qname, kind, role, prose body, fingerprints, and line ranges from store
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep fingerprint=94368126518efcb70340ec3214ad10e9df7f0ee022d178e31ecd69182d26f906 body_fp=5598346a77057e4a7d8206868d6d578abea802846376d206fe50226c62b38895 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=api -->
Searches the symbol database using a structured predicate with optional text-match fallback.

- `predicate` dict with optional filters: `name_contains` (substring), `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`/`outbound_count` ranges
- `rank_by` controls ordering: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`  
- Returns `{hits: [...], fallback?: {...}}` where hits contain qname, signature, file_pointer, one_liner, counts
- Empty predicates rejected with `invalid_argument` error to prevent unfiltered dumps
- Fallback attempts text search via ripgrep when SQL finds nothing, then fuzzy scoring against names/prose
- SQL hits re-ranked by fuzzy relevance when `name_contains` present to surface closest matches first
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_text_match_fallback fingerprint=d061850ff6487e0fde601e72500b697bd58b06916a488948f0a25a680f2e9e67 body_fp=74e61a3470a6a1434f35ad665bb7c372ed2a55c2c69619823afb363e29b16b16 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
Build fallback response envelope when grep predicate matches no symbols.

Returns a dict with `kind` field indicating why the search failed:

- `"none"` — predicate has no `name_contains` to text-search for
- `"text_match_empty"` — query appears in no source body or only outside symbols  
- `"text_match"` — candidate symbols whose bodies contain the query, ranked by inbound count
- `"fuzzy_prose"` — fuzzy matches against names/one-liners when ripgrep finds nothing

When text matches are found, applies predicate filters (scope_prefix, public_only, etc.) and caps results at configured limit. Always returns something actionable rather than "too noisy" refusal.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._fuzzy_prose_fallback fingerprint=0c1e0782658f14fba532c4353851b382fdd0e24428fd65598839f72fbc87215c body_fp=ba5d77ddc0c42666f70b6e3efe40ec3a4df4dd3f445be6cf48c7b12f63835bf1 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=domain -->
Fuzzy-score all symbols against `query` using name, one_liner, and prose when exact searches fail.

Returns a `fuzzy_prose` fallback envelope or `None` when no candidates clear `fuzzy_cutoff`. Applies predicate filters before scoring for efficiency. Uses lazy prose loading — only reads triefact bodies for symbols passing the `pre_filter` threshold.

- Returns `None`: no candidates above cutoff, caller falls through to `text_match_empty`
- Returns dict with `kind: "fuzzy_prose"`: scored matches sorted by relevance descending
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._text_match_in_scope fingerprint=8b12aa6c5e0bbbbb784c06f111dcb4ced090618f377f50282e2795b08bcf9114 body_fp=fbb45bfbc942fc7c84ce3e2be56d1d7ed862beab065e617124bc066576a6fa6f source_ref=92d722c79d9b74d00c925144ac0a7b0dcc37fb0d role=io -->
Shell out to ripgrep to find query string in in-scope source files, returning file paths with line numbers.

- Returns `{relative_path: [line_numbers]}` keyed by paths relative to `src_root`
- Runs `rg --json --line-number --fixed-strings --ignore-case` and parses streaming JSON output
- Post-filters results against `discover_files` scope set rather than translating config to rg globs
- Caps accumulation at `grep_fallback_max_files` distinct files to guard against very common substrings
- Raises `RuntimeError` if ripgrep fails with exit code ≥ 2
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._attribute_text_matches_to_symbols fingerprint=638877abde73528dff2831fc527d43a63e2c5f7ea11680e7c835749eab28f9ca body_fp=4bc2505a93decf8e7981897952569233938324186fbb451947699f14a3d7bae1 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Attributes ripgrep text matches to their smallest enclosing symbols by line range.

- Returns `{qname: hit_count}` mapping each symbol to its match count
- Drops matches outside any symbol (module-level code, imports, whitespace)
- For nested symbols, picks the innermost one (method over class)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._candidate_matches_predicate fingerprint=67f81def759871cd0f3e53436f8010818ba7ae33393fd206cd91da97251ffc74 body_fp=90711e5ddea372609ddb2b5d5a0bdf0ec3f1dee27c8fdfb266d5753173bb756b source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Checks whether TrieTools fallback candidate symbol passes all non-name predicate filters.

- Ignores `name_contains` since fallback exists because name didn't match
- Applies scope, visibility, kind, and edge count constraints from original predicate
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=932563e4410469cd038ad9bb8ad1223403b3250aaf122efb34a712cc2be608d9 body_fp=97df960141315f3662c693ed7cc98d19a7302fbbc49bff518607eb8e83dd629c source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=parsing -->
Parses TrieTools agent predicate dict into GrepPredicate object or returns error envelope.

- Validates field types and value ranges for all grep filter parameters
- `kind` is now validated against the imported `KINDS` constant (expanded set) plus `"any"`, not a hardcoded list
- `_count_range` nested helper validates min/max objects for edge count filters  
- Returns tuple of (GrepPredicate, error_dict_or_None) for uniform error handling
- `scope_exclude` accepts string or list, normalizes to tuple of path prefixes
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=46e507f1cac35bf18c92419134d5f23313010014b37aa774d59db9e257961084 body_fp=9ad4ac221c72ca76e14272b818943d30404db32245a0eb69cf41332ee0aac802 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=api -->
Dispatch reads to the appropriate source based on `path`: symbol qname → `_read_symbol`; file path with triefact → compact or full triefact view; `path:LINE` cursor / `show_source` / `offset`/`limit` → raw numbered source via `read_source`.

- `path`: qname (`pkg/module:Name`), file path, or `file:LINE`/`file:START-END` cursor ref
- `full`: when True, returns every triefact section's full prose instead of the compact per-symbol summary
- `show_source`: forces raw source output regardless of triefact availability
- `offset`/`limit`: 1-indexed line window; implies `show_source` mode
- `history`: when True, appends the symbol's or file's intent trail from the session-digest archive; ignored for raw source reads
- File beats qname when a real on-disk file exists at the colon-bearing path
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._strip_line_ref fingerprint=16fca16e06b72f6ba9d4126a2b3420d235a51949dbfa9b246749caf424caa99b body_fp=e86b072393325ecf09b6e1c02942eaa1e24301989f5da1b2b6d16d9989a8bb16 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Split a trailing `:LINE` or `:START-END` suffix from `path`, returning `(clean_path, offset, limit)` on `TrieTools`.

- `limit`: number of lines in the range; `1` when only a single line number is given; `None` when no suffix is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._resolve_in_root fingerprint=dca3c2c5e29cf37b50351dee85a6ee8e72b17db89e42fe0dbce78c0de166a371 body_fp=5d2fc74743076fc933c6f51030ee2ccb6e5381c7ab1f6553aa32d0b94031917a source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Resolve `path` to an absolute `Path` under the project root, returning `None` if the resolved path escapes it.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._triefact_view fingerprint=caba932f18796ee54530ff2e8577e9584ebc5528b8d9be6268c7822bcfec8074 body_fp=4533c5302b9f34dbd9487e515e9439e406c754aa2e928597b5f5ed8b95500790 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=domain -->
Render `TrieTools`'s triefact for `file_path` as compact summary or full prose; returns `None` when no triefact exists so the caller falls back to raw source.

- `full`: `True` emits every section's full prose via `render_for_agent`; `False` emits a compact per-symbol summary via `compact_triefact_view`.
- `history`: when `True`, appends the file's intent trail from the session-digest archive to `output`.
- Both modes prepend a staleness banner when any section's sentinel fingerprint predates the last-scan fingerprint.
- Returns `{path, mode, output, has_pending_patches, pending_patches?, notes?}` on success; `pending_patches` and `notes` are present only when staged-but-unapplied patches exist for symbols in the file.
- Returns `None` when the triefact file is absent or the path escapes the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._pending_patches_for_file fingerprint=504fcbb6721ec5f593ae24dc44dd1f655d4af26c7e6b95c36ae2766dc265eeaa body_fp=da9f76b3f61e5c1da911add209d57688e2d32038e03ef3275e9bf5b7e114c852 source_ref=c8b279d53ea4a7a3c856c698ff3b034c835ca920 role=persistence -->
Return all pending patch and create records for every symbol whose `file_path` matches `rel_path` in `TrieTools`.

- Returns `[]` silently on any store exception (best-effort).
- Each record: `{qname, op, count, notes}` where `op` is `"patch"` or `"create"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._read_symbol fingerprint=cf34658964c5a0847262855b596adb902404ef09541b702578510f92d5af642f body_fp=4bd833c3dc62b870a6e1b05092af8329a7452298efa8ed46d5f2e2db4fc79cc9 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=domain -->
Fetch a single symbol's triefact prose plus compact caller/callee summaries from `TrieTools`, emitting a telemetry span.

- `history` — when `True`, adds a `history` key to the result via `_digest_history`
- `notes` — appended when prose is missing/stale, neighbours are truncated, or the symbol exceeds the hub threshold
- `pending_patches` — included only when patches exist; each entry gains an `origin` tag (`"cascade"` or `"agent"`)
- Returns `not_found` error envelope when `qname` is absent from the store
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._digest_history fingerprint=2ef6fa57a5fc313a8964bb32b428dbe4c123273a4d7ba3a173f00a656f7a41bc body_fp=aa94f369fbbc3307de74eed005bb9aaf8ffd26f72452abacd017e5edb5267f28 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=persistence -->
Return the chronological intent trail for a symbol or module from the session-digest archive, newest first and capped.

- `qname`: returns up to 5 entries via `symbol_history`; takes priority over `module_prefix`.
- `module_prefix`: returns up to 8 entries via `file_history` when `qname` is `None`.
- Returns `[]` on any exception or when neither argument is supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._stale_qnames_for_file fingerprint=c615dbb260e882bfb765581e8fe295f9a491cd7e2322c33da920d89cf8881da2 body_fp=be19c5beaa102afd43d857796d1bdb1f89177d77240bd0c2bc10a99ff6e06aa8 source_ref=df7c277d94a9a29198067812a2a9243331b67c81 role=domain -->
Return the set of qnames in `rel` whose triefact section fingerprint differs from the current symbols-table hash, indicating stale prose.

- `rel`: source-root-relative file path used to query the symbols table.
- `triefact_text`: raw triefact markdown content scanned for section sentinels.
- Symbols the graph no longer tracks are silently skipped (orphan detection is elsewhere).
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._section_fingerprint fingerprint=e52110bed32682aa529d093d56274a31cbcc4fd8f7047075d34b613a8d6d50b7 body_fp=f86bf3e1124e3a5b6c42c2eaa2fcc1287e30efee9c023cf429fa3294a8705d46 source_ref=df7c277d94a9a29198067812a2a9243331b67c81 role=io -->
Return the source fingerprint stamped in `detail`'s triefact section sentinel, or `None` when the triefact or section is absent.

- Returns `""` (empty string) when the section exists but carries no fingerprint field.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._staleness_notes fingerprint=5695d37af3bf4b52df506c5d654b465335054c6e03d32386fad2b1cd09f9d671 body_fp=3b0d8b4bfdd512f463ddb02a31993dd4d09144513296be193ad91b3a14f685d1 source_ref=31ea5773e72df0b09ea019dcab835d5205588818 role=domain -->
Return warning strings when `TrieTools` detects that prose being served no longer reflects the current source.

- Checks section-level staleness first: sentinel fingerprint vs last-scan fingerprint; returns early if stale.
- Falls back to file-level staleness: current file content hash vs stored file fingerprint.
- Returns `[]` when both checks pass or on `OSError` reading the source file.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._prose_for fingerprint=7a45e1b328dea006c2f4a127330932dcfd60881d0d728880577bad7bda39f136 body_fp=b5dce63360a11cad94c1276ab48d29142a4383612ecbd266a53277ae2657952f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Extracts TrieTools prose text for a symbol from its triefact markdown file.

- Returns tuple of (prose_content, diagnostic_notes)
- Searches for symbol's section using regex sentinels rather than YAML parsing
- Truncates prose to configured max length via `read_prose_max_chars`
- Returns empty prose with explanatory notes when triefact file missing or section not found
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._neighbour_summaries fingerprint=f3c2279bac29ff83aa239609a037abaa507bf0e9a1473c10b54bda79be3009ac body_fp=d5c774b7fbabd577877cbb95ae1b1410e695749ef134d406645f74302b0fa373 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools._neighbour_summaries resolves qnames to compact symbol records with optional truncation.

- Returns tuple of (records, optional_note) where records are compact symbol dictionaries  
- Truncates to `read_max_neighbours_per_direction` limit and returns explanatory note if exceeded
- Skips deleted symbols that no longer exist in the store
- Each record includes qname, signature, and truncated one-liner via `_symbol_summary`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace fingerprint=73eb9bec13d74bd5ae45e72a5b691b87e3520de766924c3208b26e7bdcf3ed26 body_fp=ad9fa708eb8c34825e81fdb739a1452e9e22922199ce69f7033beab26d6cc436 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
TrieTools.trace traverses the call graph from a starting symbol using breadth-first search.

- `direction`: "callers", "callees", or "both" to control expansion direction
- `depth`: maximum hops from root (clamped to server limit)
- Returns nodes dict, edges list with direction tags, and root metadata
- Stops expansion through hub symbols (high inbound count) to prevent explosion
- Applies node count limit with BFS ordering from root
- Edges tagged "in" (caller-side) or "out" (callee-side) relative to starting symbol
- `truncated_at` lists hub symbols where expansion was blocked
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str fingerprint=7c92736236e6ccc5c8d906b78b97bcf545f2f54c2e218635cb1851d8a07888ab body_fp=e780d2e19c5809c8f4f5d93a264d3244075db7ff30058f72fe97e6189bff3061 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
TrieTools.grep_str searches source bodies with regex using ripgrep and maps matched lines to enclosing symbols.

- `regexp`: regex pattern to search for in source files
- Returns `{hits: [{qname, signature, file_pointer, one_liner, match_count}]}` or `{hits: [], fallback: {...}}` on no matches
- Falls back to fuzzy symbol name matching when no regex matches found
- Uses ripgrep with `--json`, `--line-number`, `--ignore-case` flags for structured output
- Filters results to project scope and attributes matches to smallest enclosing symbols
- Ranks results by inbound_count descending when multiple symbols match
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str_all fingerprint=8d17cf58b624639da66f21877977a85d3719bd9e1fec2b3f54d7c057d796deaa body_fp=d47c6cf4a9e5a739ea476d6e41f30a0fe5b656391fe72e37e5224a571bf1cce5 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
Searches entire project with regex, returning both symbol hits and plain text matches.

TrieTools method expands beyond indexed files to include all project content (configs, docs, dependencies). Uses ripgrep with gitignore awareness. In-scope matches are attributed to enclosing symbols; out-of-scope matches return as file:line:text records.

- **regexp**: Regular expression pattern to search for
- **Returns**: Dict with `hits` (symbol matches), `text_hits` (plain file matches), and `text_match_count`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read_source fingerprint=ae0368848e00281a549c07164f18c011b572f42df7f66fec538181e603c96965 body_fp=8b6245aaf7a94e117babd3229cb0f0ac640da711de45977198f0a4904e739e13 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
TrieTools.read_source reads raw file content with optional windowed line numbering.

Accepts any file path under project root (indexed or not), applies 1-based `offset` and `limit` windowing, returns line-numbered text with each line prefixed by its number. Long lines are clipped at 2000 characters to prevent output bloat.

- `offset`: 1-based starting line (defaults to 1)
- `limit`: maximum lines to return (defaults to whole file)
- Returns: `{path, lines, line_count, offset, more}` where `more` indicates truncation
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.write_file fingerprint=89d7a8ddb06571d55ba21ef12eb5a34ae380f5e8050d79339f31fd0ab313a898 body_fp=8050c6af5f78bdde28d746db827fcb05916885c592eb63054420b05460f3c18d source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
TrieTools creates or overwrites arbitrary files under the project root with UTF-8 content.

- Creates parent directories as needed; refuses to overwrite existing files unless `overwrite=True`
- Returns path, bytes written, creation flag, and whether sync is needed for in-scope files
- Validates path is within project root and not a directory before writing
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.find_files fingerprint=439c27ce866653ef6bf9c43e790155269b0cb9b504b5ebc0fc61da634f204277 body_fp=a78e8d0578d55f06fa32b4de139eab5835fa2b12c3f6e8685eafa7e9aebe9982 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=io -->
TrieTools.find_files searches for files matching a glob pattern with optional scope restrictions.

- `pattern`: glob pattern (e.g. `**/*.ts`, bare names like `config.json`)  
- `all_files=True`: searches entire project tree; `False` restricts to indexed files
- `limit=100`: maximum results returned, mtime-sorted newest first
- Returns dict with `matches` (relative paths), `match_count`, and `truncated` flag
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_entry_points fingerprint=a40b453a3358e2fb289e16ffa988fa7300da361d6366c30d5b035811b7564545 body_fp=970b2c0833f34c63bdd7d323641a092da64ecf7a7a283fdb28742a7096e70f30 source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
Finds high-traffic public symbols whose triefact prose fuzzy-matches the query string.

- Filters to public symbols with `inbound_count >= 2` as candidate pool
- Scores on symbol name, one-liner, and triefact prose using fuzzy matching
- Sorts by relevance score descending, then inbound count ascending
- Returns hits with qname, signature, inbound count, prose snippet, and relevance score
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol fingerprint=8f3e4bf4c648a9d74203d23ce3e4dd811c1954895663a4a1dca66d22e49bae91 body_fp=56a42702de7918e0cdfd7ad82c112097ea73e418d33fab84ba7749a72b30aa5f source_ref=77098c0a1179a2a9ecd9ad8b5616de5b457df217 role=api -->
Fuzzy symbol name lookup returning the best match plus similar symbols with relevance scores.

TrieTools.grep_symbol performs three-phase matching: SQL substring search for fast candidates, rapidfuzz fallback against all symbol names when SQL finds nothing, then name/one_liner/prose scoring with lazy prose reads. Returns the highest-scoring match with up to 9 similar alternatives, each carrying a 0-100 relevance score. Better than grep for typo tolerance and discovering related symbols in one call.

- Uses rapidfuzz WRatio scoring with configurable cutoffs and prose weight
- SQL LIKE phase pulls up to 20 candidates, re-ranked by fuzzy score  
- Fallback phase searches all symbol names with score cutoff 45
- Prose augmentation only for candidates clearing the pre-filter threshold
- Returns match object with qname/kind/signature/score plus similar list
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol_and_neighbours fingerprint=7ea37438f4dc626cbdbb108b54c36c9dc7731a3b134e51c78f5228e1295929ad body_fp=30b0a894f33f118ef503ce8fc45cc93927f10a2851f7b344d90a326b2c2b08b0 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools method extends grep_symbol to include immediate caller and callee metadata for the best match.

Combines fuzzy symbol lookup with neighbourhood exploration in a single round trip. Returns the same structure as grep_symbol plus trimmed summaries of direct references. Used for symbol orientation without separate read calls.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol fingerprint=ec6c9df2f6e2fd37c306c0ddc5a4533af8f1a333ab180ca986dd49ba6a498891 body_fp=ed95be0b5ffc9f875af50bd7984ffaeb2e21443c881361a165b4142106505b16 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=api -->
TrieTools.explain_symbol returns full prose for a symbol plus a narrative story weaving together its callers and callees.

- `sym`: symbol name or qname (uses fuzzy resolution if exact match fails)
- `history`: when True, appends `_digest_history` intent trail under `out["history"]`
- Returns dict with `qname`, `signature`, `source_pointer`, `prose`, `story`, `callers`, `callees`, optional `notes`, optional `history`
- `notes` prepends staleness warnings (from `_staleness_notes`) before any prose-generation notes
- Story includes first paragraph of prose from up to 5 callers/callees under "Called by:" and "Calls into:" sections
- Telemetry tracks result kind, prose/story character counts, and response size
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol_references fingerprint=2a49b14331cbf83b57abb1d76da27ac245404ce8e48bec57af742e8491abbeeb body_fp=e17bb4b1c98afbad07ba07b30811827c5f515749f7e20719e2e04c215f318d84 source_ref=81a270b759f118deb5c5b87c2265bff8a79f1334 role=domain -->
TrieTools.explain_symbol_references explains how a symbol is used by building a usage story from caller prose.

- Resolves the symbol name via fuzzy search if not found directly
- Builds usage narrative from the first paragraph of each caller's prose
- Limits to 8 callers for the usage story, all callers for the summary list
- `history=True` appends the symbol's intent trail from the digest archive as `result["history"]`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace_flow fingerprint=4dd9d61ff701bd2992e0aa4e9b3b5d43ff52b010a1562bc193ddaa229de437b6 body_fp=8ba1c8e084a272174d1ae698449dafe2a13855f2fa78c5168ee6ead9f109d01f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools.trace_flow finds call chains between two symbols using graph pathfinding.

- `symbol1`, `symbol2`: accepts exact qnames or fuzzy symbol names via grep_symbol resolution
- Returns dict with `from_qname`, `to_qname`, `paths` (list of qname lists), optional `notes`
- Searches up to `trace_max_depth` hops, skips hub symbols above threshold, returns max 3 paths
- Empty paths list with explanatory note when no connection found within depth limit
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_flow fingerprint=47e5b35007183ceaa63f7a11cb99ebc79fbbbce4788c1bd0ecfe4c5e0a088870 body_fp=2bfe07dccbe60d76dffddbec36596bd7402b91171a90bc85a73d453e24d61d3e source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools method that finds call chains between symbols and weaves their triefact prose into readable execution narratives.

- Uses `trace_flow` to find paths, then enriches each path step with prose snippets
- Returns `paths` as list of `{chain: [qname,...], narrative: str}` dictionaries
- Narrative joins symbol prose with "→" separators to show execution flow story
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._suggest_for_qname fingerprint=5ac22b4d30b52fa3bf0f60a18bdbf94c7855456a7fa9b25fca44752526dc1a98 body_fp=a6024aa8a3777e4763580f5793641a04de2ec87971c195f7723a2bed246dc99b source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Generate suggestion text for `not_found` errors by fuzzy-matching the failed qname against all symbols.

- Returns help text with close matches, or fallback instructions when no close matches exist
- Uses qualified name matching first, then falls back to local name matching if no qname matches
- Returns None only when no fuzzy matches are found (rare case)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=ccada3c83ab2a413e5211220ba4e05071524543fed482f54060ec01e2e03e392 body_fp=2a1c5e4cb0c6b63ce51f4789ac9ff91aeaea4fb3e3838ead0e0885cd7334e661 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=orchestration -->
Construct an MCP server with all trie tools registered from a TrieTools instance.

- Returns tuple of (FastMCP server, TrieTools) for testing and CLI reuse
- Registers 11 core tools: grep/read/trace family plus extended search/explain functions
- Registers 4 file tools: grep_str_all, find_files, read_source, write_file
- Registers 10 edit tools: adds `batch_patch` to the create/modify/delete/rename workflow with preview/commit
- Registers 5 project-level query tools: summary, symbols_by_file, file_triefact, activity, blast_radius
- AGM tools and desktop-only helpers (all_symbols, all_edges, system_model) are no longer registered
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=c57b100fd07ba8bcfcaedebb2648cbe5949b2106b69128d814bb6c633382c744 body_fp=8a8cba0ff5e958f81c55546e70cad6b2d11b39ce9a25aa725ed997e48c4d1089 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Run the MCP server over stdio for the project at `project_root`.

- Configures stdout and stderr for line buffering to ensure prompt output
- Blocks until the parent process closes the pipe
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:main fingerprint=cae2a0ae09ead6d8ca05631fe03f2b4e857ad2666fbccf4fd92eb04c469dd2ac body_fp=87be6759d2b659a0120598ba3d2790afe461e3254accc39dd95c1e74c8d2d5d6 source_ref=df8a5cd8065a92017ff6c2705df9e5afb2e8cd8f role=entrypoint -->
Parse `sys.argv[1]` as a project directory and delegate to `run_stdio`, exiting with an error message if the argument is missing or the path does not exist.
<!-- trie:end -->