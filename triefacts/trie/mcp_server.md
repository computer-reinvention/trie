---
trie_version: 0.1.9
source: trie/mcp_server.py
file_fingerprint: 8bce031f323556b2c59573fa4e9f17d380c559add91564f910b357391b2a2347
last_synced_at: '2026-06-17T16:41:59Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-3060
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
  lines: 269-2991
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 283-312
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 314-315
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch
  lines: 319-359
- kind: method
  qualified_name: trie/mcp_server:TrieTools._blast_radius_brief
  lines: 361-374
- kind: method
  qualified_name: trie/mcp_server:TrieTools.create_symbol
  lines: 376-412
- kind: method
  qualified_name: trie/mcp_server:TrieTools.delete_symbol
  lines: 414-434
- kind: method
  qualified_name: trie/mcp_server:TrieTools.rename_symbol
  lines: 436-458
- kind: method
  qualified_name: trie/mcp_server:TrieTools.blast_radius
  lines: 460-507
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_drop
  lines: 509-522
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_list
  lines: 524-564
- kind: method
  qualified_name: trie/mcp_server:TrieTools.preview
  lines: 566-590
- kind: method
  qualified_name: trie/mcp_server:TrieTools.commit
  lines: 592-632
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_apply
  lines: 635-637
- kind: method
  qualified_name: trie/mcp_server:TrieTools.all_symbols
  lines: 641-673
- kind: method
  qualified_name: trie/mcp_server:TrieTools.all_edges
  lines: 675-692
- kind: method
  qualified_name: trie/mcp_server:TrieTools.system_model
  lines: 694-724
- kind: method
  qualified_name: trie/mcp_server:TrieTools.summary
  lines: 726-752
- kind: method
  qualified_name: trie/mcp_server:TrieTools.record_attention_event
  lines: 754-781
- kind: method
  qualified_name: trie/mcp_server:TrieTools.attention
  lines: 783-824
- kind: method
  qualified_name: trie/mcp_server:TrieTools.set_investigation
  lines: 826-852
- kind: method
  qualified_name: trie/mcp_server:TrieTools.activity
  lines: 854-908
- kind: method
  qualified_name: trie/mcp_server:TrieTools.symbols_by_file
  lines: 910-949
- kind: method
  qualified_name: trie/mcp_server:TrieTools.file_triefact
  lines: 951-1012
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 1016-1148
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 1150-1295
- kind: method
  qualified_name: trie/mcp_server:TrieTools._fuzzy_prose_fallback
  lines: 1297-1373
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 1375-1474
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 1476-1499
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 1501-1527
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 1529-1601
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 1605-1663
- kind: method
  qualified_name: trie/mcp_server:TrieTools._strip_line_ref
  lines: 1666-1677
- kind: method
  qualified_name: trie/mcp_server:TrieTools._resolve_in_root
  lines: 1679-1689
- kind: method
  qualified_name: trie/mcp_server:TrieTools._triefact_view
  lines: 1691-1734
- kind: method
  qualified_name: trie/mcp_server:TrieTools._read_symbol
  lines: 1736-1806
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 1808-1845
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 1847-1872
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 1876-2030
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str
  lines: 2034-2193
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str_all
  lines: 2195-2308
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read_source
  lines: 2310-2368
- kind: method
  qualified_name: trie/mcp_server:TrieTools.write_file
  lines: 2370-2430
- kind: method
  qualified_name: trie/mcp_server:TrieTools.find_files
  lines: 2432-2503
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_entry_points
  lines: 2505-2588
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol
  lines: 2590-2691
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol_and_neighbours
  lines: 2693-2719
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol
  lines: 2721-2802
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol_references
  lines: 2804-2865
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace_flow
  lines: 2867-2925
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_flow
  lines: 2927-2971
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 2975-2991
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 2997-3049
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 3052-3059
incoming_refs: 9
outgoing_refs: 68
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
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=f2cf2a72f457f2c2afe768ff2d1e868acb8146d7ccd0c05add9498d704a6505f body_fp=7fe01d75d9c7758f6dbd3583d8f563829c39014826594240be0c558c359b2177 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=orchestration -->
Core interface for MCP tools as plain methods, testable without transport.

Owns the Store and project config for process lifetime. Implements patch tools (patch, create_symbol, delete_symbol, rename_symbol, blast_radius, patch_drop, patch_list, preview, commit), desktop app helpers (all_symbols, all_edges, system_model, summary, record_attention_event, attention, set_investigation, activity, symbols_by_file, file_triefact), three core operations (`grep`, `read`, `trace`), and extended wrappers (grep_str, grep_str_all, read_source, write_file, find_files, grep_entry_points, grep_symbol, grep_symbol_and_neighbours, explain_symbol, explain_symbol_references, trace_flow, explain_flow). All methods return structured dicts with error envelopes; telemetry is captured on each call with configurable event names to distinguish MCP vs CLI usage.

- `event_name`: controls telemetry event name emitted on each call ("mcp_call" for MCP server, "cli_call" for CLI)
- `store`: SQLite store containing symbol graph and triefact metadata
- `rg_path`: resolved ripgrep binary path for text search fallbacks
- `_session_id`: unique session identifier for patch operations (injectable via TRIE_SESSION_ID env var, falls back to 12-char hex UUID)
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=da31ea5a8dabd217b86c7e6ed605fc3a1d2dbb26bb93f24bc8988024d73a4223 body_fp=1af7361563281662e6bb24529f529f5b296a49d4483c09673b0d6924f865a0ee source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=model -->
Initialize TrieTools with project configuration, telemetry, store, and session state.

- Loads config from project root and validates ripgrep availability at startup
- Configures telemetry from debug settings and emits server start event for MCP path only
- Creates Store connection to graph database and generates session ID from TRIE_SESSION_ID env var or UUID
- `event_name`: defaults to "mcp_call" for MCP server, "cli_call" for CLI usage
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=9967aa9f46cd1703a5cfd1ae72d466503e42628bc1c5d81769b7301acc822ebf source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Closes the underlying SQLite store connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch fingerprint=f45afbcbb524714fefa8bb5ff7b2a0dea656b126d274b590e0fd1e747a26f377 body_fp=79f3b11786499e39963078d829e7c2a106c4f735f85f328b236d9a9e30018260 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
TrieTools.patch stages a change to an existing symbol's body, accepting either a generation note or exact source.

- Requires exactly one of `note` (describes change for model generation) or `source` (provides exact new body)
- Returns `{patch_id, qname, mode, pending_patch_count, blast_radius}` on success or error envelope on failure
- `mode`: indicates whether change uses "note" (generative) or "source" (deterministic) approach
- `blast_radius`: compact blast radius metadata showing affected symbols
- Fire-and-forget staging operation; actual change is applied later by `commit()`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._blast_radius_brief fingerprint=b3e0abb2450c94f0f942717710c448d109338c0d7b7e66b81d8bd4b1e99a53c3 body_fp=035a0df8c5bccdfb1898ca4a38b4afe434273df9a4fb0810bc70d198b11e54ed source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
Computes a compact blast radius summary for patch operations by calling TrieTools.blast_radius and extracting key fields.

- Returns flattened qname list instead of full cascade objects for brevity
- Falls back to empty result on any error to ensure patch operations don't fail
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.create_symbol fingerprint=5ee5dc7be77c241123423bacd811ad0cd4b24b67254c49437479f695f48330ed body_fp=b7d902f7e0c69d3aa646b69b8537e86f77720401b93510a9d710cd3c96c30095 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
Stages creation of a new symbol that doesn't yet exist in the graph.

- `qname`: intended qualified name (e.g. 'src/foo:helper')
- `note`: description of what the symbol should do (required)
- `file_path`: target source file (derived from qname module if omitted)
- `anchor_qname`: optionally places it after an existing symbol
- Returns: `{create_patch_id, qname, target_file}`
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.delete_symbol fingerprint=414b50dc9d4f359c8cabd21bd7557b4145cb4b4e1cd4fd23b2c54d95ef71f706 body_fp=3aca70cd1bbb8e1c5e8fbb746940565d5f2d8c6bf645797fca7ad35b6587726e source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
TrieTools stages symbol deletion, returning the patch ID and list of dependent symbols that reference the target.

- `dependents`: symbols referencing the deleted symbol; agents should decide whether to patch them
- Returns error if symbol not found in graph
- Deletion proceeds at commit regardless of dependents
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.rename_symbol fingerprint=fd1062eb60d81692343ee725d864825a79a2b69477d0fb1279f0fdd1cfdef4ac body_fp=e0b2e53f5bd66983579b84eb34933abbd5eb786ab245b579d2e6e49415619e1c source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
Stages a rename patch for an existing symbol to `new_name` (the local identifier).

- `new_name`: must be a valid Python identifier
- Returns: patch_id, qname, new_name, and list of reference qnames
- Commit fails if the symbol definition cannot be rewritten unambiguously
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.blast_radius fingerprint=e00d5ec65a2ed5125dafaab8333322a45b0bbf7309d98d76cfff8491f0262b9d body_fp=aa112e9ab438f72b61a977ee93f17830df1514634f4fa71d1a72f6bdb6052f94 source_ref=f2057a3fdb019667d44454cdddf8000d6523bfa7 role=domain -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools.preview fingerprint=01fe22fe1d3a82374aa893d86eac75cc58792e00f821e99b6ec136db231bcccb body_fp=872e67048b726b58cc7c76fed68ef704d867b1efdd68ff81a9d9e0948fcd487c source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
TrieTools.preview shows what commit would do without writing files or paying for generation.

- Returns patch counts, creates list, cascade symbols, and readiness flags
- Sets `needs_session_note` to true when total symbols exceed one
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.commit fingerprint=9d814a7b8d2407cb26c2478ef8f57bb0b09598a69571db03a32b9cd30a64a777 body_fp=eead4e9e72bda7b78b871ee15d0e8d42381673e0bcf34edb9871e9a305be2721 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=orchestration -->
Stage and apply all pending patches and creates, returning the ApplyReport.

- `session_note`: required for multi-symbol applies (the unifying intent)
- `backend`: overrides configured edit backend ('llm' default)

Uses exclusive lock to prevent concurrent applies. Runs generation off event-loop thread via ThreadPoolExecutor.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.patch_apply fingerprint=5231bb6b1868849393a8d96eade7fbaed3b10e8e1d76ad81897e1f14713b196a body_fp=cdf86101d9d922eafa9bd8ba612b356cd74482627253d1dd0b13f10bad3f2225 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=util -->
Deprecated alias for TrieTools.commit() with empty session note for single-symbol patch applications.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.all_symbols fingerprint=acced3bb257297d000ce63a4915aebd229274ba022dc35993e41f4906e0673ec body_fp=55d00a3a67706f204e48c5585f9a383cfc1a19e7acce6a4178bf7f6d3baa5daf source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
TrieTools.all_symbols returns all project symbols sorted by rank_by, bypassing grep's empty predicate guard.

- `rank_by`: sorting criterion, defaults to "inbound_count"
- `limit`: maximum symbols to return, defaults to 5000
- Returns: dict with "hits" list containing full SymbolDetail records plus historical_mass field
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.all_edges fingerprint=c10de1ac433089bf91a5cf68f746777bec3ef4cef890bac76788f14f86c3bfc6 body_fp=89de7974f52a1b1afccffed13aa2ff45ac08d35db23cda9a023cc245b133503b source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
Return all call-graph edges for the desktop app's initial graph population.

- `limit`: maximum number of edges to return (default 50000)
- Returns `{edges: [{from, to, kind}, ...]}` — flat list of directed edges from SQLite with edge type
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.system_model fingerprint=fe36511f156259aef3c557ed945db2d58f19c14ada29b8d2a465f45e7340abb3 body_fp=71862974933431ff42fd6266048672915dd4a8b6aed7f06ee2d70c2e9de8353c source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
Returns a high-level system model for desktop graph visualization with classified nodes, axis summaries, and landmarks.

- `landmark_limit`: maximum number of landmark symbols to include in the L1 view (default 160)
- `include_tests`: whether to include test symbols flagged as `is_test` (default False)
- returns: dict with `{nodes, axes: {role, subsystem}, landmarks, stats}` containing graph topology and metadata
- nodes are classified as door/hub/bedrock/exit/internal/orphan with salience scores and layout positions
- includes aggregated component groups and thresholded flow edges for architectural overview
- results cached on disk by graph fingerprint for instant repeat calls
- injects live AGM historical mass per node after cache read (decays continuously)
- pure graph analysis with no LLM calls required
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.summary fingerprint=ed9f6804bf456d31b6628a2ffc2d73eb903a7c3040160f5b6347896061dec46b body_fp=b1de55753ce5e944089a958c45d4a2f6c8f163328e8984a93635a45f5946f2d3 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools returns project-level aggregate statistics by executing SQL count queries against the graph database.

- `project_name`: directory name of the project root
- `project_root`: absolute path to the project root
- `total_symbols`: count of all indexed symbols
- `public_symbols`: count of symbols whose names don't start with underscore
- `total_files`: count of distinct source files containing symbols
- `total_edges`: count of call-graph edges between symbols
- `trie_version`: package version string or "unknown"
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.record_attention_event fingerprint=5bf0dd0087c2575839e9d87bf24d3ae86a2c9cf1fb352ada11db485b654ff230 body_fp=d8238d19b91315568bd3f4c10de7b77653e3d98ee3172d1fef0fdfc81d890bac source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=persistence -->
TrieTools.record_attention_event records one AGM attention event to persistent storage for replay and historical mass calculation.

- `type`: must be one of grep, read, trace, or write
- Returns weight value from EVENT_WEIGHTS for the event type
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.attention fingerprint=5ab5ec0e0188c77d3f593de541cea84ed2a185871e7a1334dd67c3795f14bbc4 body_fp=15d149a55f8379c77f034ece299949c0a499da45f4ab1c47143994dcf4afa0ae source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
TrieTools.attention returns recent AGM attention events and constant configuration tables for the desktop's live attention model.

- `since`: unix timestamp cutoff for event retrieval (default 0.0 for all events)
- Returns events list with timestamps, types, targets, and session metadata plus configuration constants
- Desktop uses this to hydrate/replay its live attention simulation without hard-coding weights or parameters
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.set_investigation fingerprint=991af81dcc0e286701e6fa41be10d8801f2907aa3e152d267fc7569957fbe1c9 body_fp=ca1c3686c63281961c2e8d812d3be098e4ddb6d75e8d0e478d4c8f8dbde0ba17 source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
Declare or update the current AGM investigation (explicit task boundary).

The TrieTools method persists investigation metadata (id, label, status) to runtime storage so the attention capture path can key events to it. Investigations represent meaningful units of continuity beyond individual turns.

- **label**: human-readable description of the investigation/task
- **status**: must be one of the valid investigation statuses from `trie.attention` 
- **investigation_id**: auto-generated when omitted (12-char UUID hex prefix)
- **Returns**: dict with investigation_id, label, and status
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.activity fingerprint=9fe4f42c234d76aa74b4596b31236ff937284e79fc9501ae3e1a191782486338 body_fp=130f441ba10806d9c22863021b38b028d23a9c9efef22f6278e1c8116d9c8bd4 source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
TrieTools.activity returns live writer status, stale file set, and patch summary for editor polling.

- Reads ephemeral `.trie/activity.db` for sync process state
- Returns dict with `status` object (state, op, pid, current_file, etc), `pending` object (count, stale files, head) or null, `patches` summary (counts by origin), and `apply` object when patch application is active
- Enables editor to show sync progress, stale file badges, and patch status regardless of which process is syncing
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.symbols_by_file fingerprint=7327f1e7efcb1aa7fac79a7727cf492e4e245e2c515b9a12885e1bc6f275c1eb body_fp=c8ad00c51cc8cb0f9ba66d2dad0a4e7325165c931755b1888857def48c88f307 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools.symbols_by_file returns all symbols in a given source file with their metadata.

- Returns dict with `file_path` and `symbols` list containing symbol details
- Symbols ordered by start line ascending within the file
- Used by desktop app sidebar to highlight corresponding graph nodes on file click
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.file_triefact fingerprint=3c41b032bf487c41094e3b5f9fa082c10a3e49fb37af694dea6fb92da57dd2d7 body_fp=ed47071f8ef4d957aa8e62c01f0c75928e3cf695b48192f01df7f9649e5b7be0 source_ref=f2057a3fdb019667d44454cdddf8000d6523bfa7 role=api -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_text_match_fallback fingerprint=d061850ff6487e0fde601e72500b697bd58b06916a488948f0a25a680f2e9e67 body_fp=74e61a3470a6a1434f35ad665bb7c372ed2a55c2c69619823afb363e29b16b16 source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
Build fallback response envelope when grep predicate matches no symbols.

Returns a dict with `kind` field indicating why the search failed:

- `"none"` — predicate has no `name_contains` to text-search for
- `"text_match_empty"` — query appears in no source body or only outside symbols  
- `"text_match"` — candidate symbols whose bodies contain the query, ranked by inbound count
- `"fuzzy_prose"` — fuzzy matches against names/one-liners when ripgrep finds nothing

When text matches are found, applies predicate filters (scope_prefix, public_only, etc.) and caps results at configured limit. Always returns something actionable rather than "too noisy" refusal.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._fuzzy_prose_fallback fingerprint=0c1e0782658f14fba532c4353851b382fdd0e24428fd65598839f72fbc87215c body_fp=ba5d77ddc0c42666f70b6e3efe40ec3a4df4dd3f445be6cf48c7b12f63835bf1 source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=util -->
Fuzzy-score all symbols against `query` using name, one_liner, and prose when exact searches fail.

Returns a `fuzzy_prose` fallback envelope or `None` when no candidates clear `fuzzy_cutoff`. Applies predicate filters before scoring for efficiency. Uses lazy prose loading — only reads triefact bodies for symbols passing the `pre_filter` threshold.

- Returns `None`: no candidates above cutoff, caller falls through to `text_match_empty`
- Returns dict with `kind: "fuzzy_prose"`: scored matches sorted by relevance descending
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._text_match_in_scope fingerprint=d3b53cf1edec68c4065271cb469ec003b74e7141cf154025945db6ef0029f216 body_fp=fbb45bfbc942fc7c84ce3e2be56d1d7ed862beab065e617124bc066576a6fa6f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=932563e4410469cd038ad9bb8ad1223403b3250aaf122efb34a712cc2be608d9 body_fp=97df960141315f3662c693ed7cc98d19a7302fbbc49bff518607eb8e83dd629c source_ref=387016dec2af121a411a78de8ef480a933c24894 role=domain -->
Parses TrieTools agent predicate dict into GrepPredicate object or returns error envelope.

- Validates field types and value ranges for all grep filter parameters
- `kind` is now validated against the imported `KINDS` constant (expanded set) plus `"any"`, not a hardcoded list
- `_count_range` nested helper validates min/max objects for edge count filters  
- Returns tuple of (GrepPredicate, error_dict_or_None) for uniform error handling
- `scope_exclude` accepts string or list, normalizes to tuple of path prefixes
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=ea87a54ab9ee9b1ea91cfe7a236f9edd29e5da1ad51881430829c0b3b7a29ea3 body_fp=a7721dbfb63a86b9cb89b2457b152591c7aa590db0b46d6ae7d5c61b6a132cb0 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=api -->
Dispatch reads to the appropriate source based on `path`: symbol qname → `_read_symbol`; file path with triefact → compact or full triefact view; `path:LINE` cursor / `show_source` / `offset`/`limit` → raw numbered source via `read_source`.

- `path`: qname (`pkg/module:Name`), file path, or `file:LINE`/`file:START-END` cursor ref
- `full`: when True, returns every triefact section's full prose instead of the compact per-symbol summary
- `show_source`: forces raw source output regardless of triefact availability
- `offset`/`limit`: 1-indexed line window; implies `show_source` mode
- File beats qname when a real on-disk file exists at the colon-bearing path
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._strip_line_ref fingerprint=16fca16e06b72f6ba9d4126a2b3420d235a51949dbfa9b246749caf424caa99b body_fp=e86b072393325ecf09b6e1c02942eaa1e24301989f5da1b2b6d16d9989a8bb16 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Split a trailing `:LINE` or `:START-END` suffix from `path`, returning `(clean_path, offset, limit)` on `TrieTools`.

- `limit`: number of lines in the range; `1` when only a single line number is given; `None` when no suffix is present.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._resolve_in_root fingerprint=dca3c2c5e29cf37b50351dee85a6ee8e72b17db89e42fe0dbce78c0de166a371 body_fp=5d2fc74743076fc933c6f51030ee2ccb6e5381c7ab1f6553aa32d0b94031917a source_ref=387016dec2af121a411a78de8ef480a933c24894 role=util -->
Resolve `path` to an absolute `Path` under the project root, returning `None` if the resolved path escapes it.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._triefact_view fingerprint=e0bbf39fa64c1a8eda441b9a40c7009d43cede3191335486207868812f15686f body_fp=7edbfbcc62f32cea0a0f93a405c3406d49f9471bee6bd9b8d36cfe391a0776c2 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=domain -->
Render `TrieTools`'s triefact for `file_path` as compact summary or full prose; returns `None` when no triefact exists so the caller falls back to raw source.

- `full`: `True` emits every section's full prose via `render_for_agent`; `False` emits a compact per-symbol summary via `compact_triefact_view`.
- Returns `{path, mode, output}` on success, `None` when the triefact file is absent or the path escapes the project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._read_symbol fingerprint=972dd361d21217884a13eb6b850eeee46e6bd6a0d749a8a7b0a4df77c7b81f37 body_fp=3c6d4bd0c3d7c129b4ba9651a71e93463537b41cfc35753922f05031c49fed41 source_ref=387016dec2af121a411a78de8ef480a933c24894 role=domain -->
Fetch a single symbol's triefact prose plus compact caller/callee summaries from `TrieTools`, emitting a telemetry span.

- `notes` — appended when prose is missing, neighbours are truncated, or the symbol exceeds the hub threshold
- `pending_patches` — included only when patches exist; each entry gains an `origin` tag (`"cascade"` or `"agent"`)
- Returns `not_found` error envelope when `qname` is absent from the store
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
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace fingerprint=73eb9bec13d74bd5ae45e72a5b691b87e3520de766924c3208b26e7bdcf3ed26 body_fp=ad9fa708eb8c34825e81fdb739a1452e9e22922199ce69f7033beab26d6cc436 source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
TrieTools.trace traverses the call graph from a starting symbol using breadth-first search.

- `direction`: "callers", "callees", or "both" to control expansion direction
- `depth`: maximum hops from root (clamped to server limit)
- Returns nodes dict, edges list with direction tags, and root metadata
- Stops expansion through hub symbols (high inbound count) to prevent explosion
- Applies node count limit with BFS ordering from root
- Edges tagged "in" (caller-side) or "out" (callee-side) relative to starting symbol
- `truncated_at` lists hub symbols where expansion was blocked
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str fingerprint=7c92736236e6ccc5c8d906b78b97bcf545f2f54c2e218635cb1851d8a07888ab body_fp=e780d2e19c5809c8f4f5d93a264d3244075db7ff30058f72fe97e6189bff3061 source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_entry_points fingerprint=a40b453a3358e2fb289e16ffa988fa7300da361d6366c30d5b035811b7564545 body_fp=970b2c0833f34c63bdd7d323641a092da64ecf7a7a283fdb28742a7096e70f30 source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
Finds high-traffic public symbols whose triefact prose fuzzy-matches the query string.

- Filters to public symbols with `inbound_count >= 2` as candidate pool
- Scores on symbol name, one-liner, and triefact prose using fuzzy matching
- Sorts by relevance score descending, then inbound count ascending
- Returns hits with qname, signature, inbound count, prose snippet, and relevance score
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol fingerprint=8f3e4bf4c648a9d74203d23ce3e4dd811c1954895663a4a1dca66d22e49bae91 body_fp=56a42702de7918e0cdfd7ad82c112097ea73e418d33fab84ba7749a72b30aa5f source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol fingerprint=27d2591b20b21c2dd2dae483931f70266fe2b2555692cf8d75905ddb48174323 body_fp=13b849da68f410d5f020593091fa2043ec0a956fb5aec05bd96909df2124e58f source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools.explain_symbol returns full prose for a symbol plus a narrative story weaving together its callers and callees.

- `sym`: symbol name or qname (uses fuzzy resolution if exact match fails)
- Returns dict with `qname`, `signature`, `source_pointer`, `prose`, `story`, `callers`, `callees`, optional `notes`
- Story includes first paragraph of prose from up to 5 callers/callees under "Called by:" and "Calls into:" sections
- Telemetry tracks result kind, prose/story character counts, and response size
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol_references fingerprint=eea4957620148f9d0248392d9f05abb2b42803af63e9fcd92c25002b5b64438a body_fp=551bca66176259a1876dedf6342c9fe2b38c0d51422076da6416a504e1443ca3 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools.explain_symbol_references explains how a symbol is used by building a usage story from caller prose.

- Resolves the symbol name via fuzzy search if not found directly
- Builds usage narrative from the first paragraph of each caller's prose
- Limits to 8 callers for the usage story, all callers for the summary list
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
<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=6511b64f8e01c6e0d4be25e3747af2532303ae231954ccbb0612f9b297b3a25b body_fp=f08454a590fe1d0b2492919169588c92377b0b98b1ee6c8aea5af641890cbd9e source_ref=31da51020b7add0a40187e2904d7841c0e4651f1 role=api -->
Construct an MCP server with all trie tools registered from a TrieTools instance.

- Returns tuple of (FastMCP server, TrieTools) for testing and CLI reuse
- Registers 11 core tools: grep/read/trace family plus extended search/explain functions
- Registers 4 file tools: grep_str_all, find_files, read_source, write_file  
- Registers 9 edit tools for full create/modify/delete/rename workflow with preview/commit
- Registers 8 desktop app helpers for graph visualization and file triefacts
- Registers 3 AGM tools for attention event capture and investigation tracking
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=c57b100fd07ba8bcfcaedebb2648cbe5949b2106b69128d814bb6c633382c744 body_fp=8a8cba0ff5e958f81c55546e70cad6b2d11b39ce9a25aa725ed997e48c4d1089 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Run the MCP server over stdio for the project at `project_root`.

- Configures stdout and stderr for line buffering to ensure prompt output
- Blocks until the parent process closes the pipe
<!-- trie:end -->