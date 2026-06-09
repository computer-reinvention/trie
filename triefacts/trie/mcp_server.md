---
trie_version: 0.1.5
source: trie/mcp_server.py
file_fingerprint: c3dc78f573cb95fcec191adc71835e76848e99296d1b957309a360b1cf2c87ea
last_synced_at: '2026-06-09T09:59:03Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-2797
- kind: class
  qualified_name: trie/mcp_server:RipgrepNotFoundError
  lines: 75-87
- kind: function
  qualified_name: trie/mcp_server:_require_ripgrep
  lines: 90-105
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 108-127
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 130-134
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 137-143
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 146-149
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 152-154
- kind: function
  qualified_name: trie/mcp_server:_fuzzy_score
  lines: 157-168
- kind: function
  qualified_name: trie/mcp_server:_score_sym
  lines: 171-196
- kind: function
  qualified_name: trie/mcp_server:_predicate_is_empty
  lines: 199-222
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 225-244
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 247-2732
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 261-290
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 292-293
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch
  lines: 297-337
- kind: method
  qualified_name: trie/mcp_server:TrieTools._blast_radius_brief
  lines: 339-352
- kind: method
  qualified_name: trie/mcp_server:TrieTools.create_symbol
  lines: 354-387
- kind: method
  qualified_name: trie/mcp_server:TrieTools.delete_symbol
  lines: 389-409
- kind: method
  qualified_name: trie/mcp_server:TrieTools.rename_symbol
  lines: 411-433
- kind: method
  qualified_name: trie/mcp_server:TrieTools.blast_radius
  lines: 435-482
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_drop
  lines: 484-497
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_list
  lines: 499-539
- kind: method
  qualified_name: trie/mcp_server:TrieTools.preview
  lines: 541-565
- kind: method
  qualified_name: trie/mcp_server:TrieTools.commit
  lines: 567-607
- kind: method
  qualified_name: trie/mcp_server:TrieTools.patch_apply
  lines: 610-612
- kind: method
  qualified_name: trie/mcp_server:TrieTools.all_symbols
  lines: 616-646
- kind: method
  qualified_name: trie/mcp_server:TrieTools.all_edges
  lines: 648-665
- kind: method
  qualified_name: trie/mcp_server:TrieTools.system_model
  lines: 667-690
- kind: method
  qualified_name: trie/mcp_server:TrieTools.summary
  lines: 692-718
- kind: method
  qualified_name: trie/mcp_server:TrieTools.activity
  lines: 720-774
- kind: method
  qualified_name: trie/mcp_server:TrieTools.symbols_by_file
  lines: 776-815
- kind: method
  qualified_name: trie/mcp_server:TrieTools.file_triefact
  lines: 817-878
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 882-1014
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 1016-1161
- kind: method
  qualified_name: trie/mcp_server:TrieTools._fuzzy_prose_fallback
  lines: 1163-1239
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 1241-1340
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 1342-1365
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 1367-1393
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 1395-1473
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 1477-1547
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 1549-1586
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 1588-1613
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 1617-1771
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str
  lines: 1775-1934
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str_all
  lines: 1936-2049
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read_source
  lines: 2051-2109
- kind: method
  qualified_name: trie/mcp_server:TrieTools.write_file
  lines: 2111-2171
- kind: method
  qualified_name: trie/mcp_server:TrieTools.find_files
  lines: 2173-2244
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_entry_points
  lines: 2246-2329
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol
  lines: 2331-2432
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol_and_neighbours
  lines: 2434-2460
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol
  lines: 2462-2543
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol_references
  lines: 2545-2606
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace_flow
  lines: 2608-2666
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_flow
  lines: 2668-2712
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 2716-2732
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 2738-2786
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 2789-2796
incoming_refs: 9
outgoing_refs: 64
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
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=c1ea1ab6029a7d7dbb80adad7ff36e10f0d10d98702c71fefe4b0a8343d7aad3 body_fp=a1c66dfdd5550b3044790c319651ce89a0670c4512761077c0031efd8d8b567d source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
Core interface for MCP tools as plain methods, testable without transport.

Owns the Store and project config for process lifetime. Implements patch tools (patch, create_symbol, delete_symbol, rename_symbol, blast_radius, patch_drop, patch_list, preview, commit), desktop app helpers (all_symbols, activity, file_triefact), three core operations (`grep`, `read`, `trace`), and extended wrappers (grep_str, grep_str_all, read_source, write_file, find_files, grep_entry_points, grep_symbol, grep_symbol_and_neighbours, explain_symbol, explain_symbol_references, trace_flow, explain_flow). All methods return structured dicts with error envelopes; telemetry is captured on each call with configurable event names to distinguish MCP vs CLI usage.

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
<!-- trie:section symbol=trie/mcp_server:TrieTools.all_symbols fingerprint=bb0b42695a8bce79f82c9092f0b0178fa8334fa9151e99bc957fbcfc689079b7 body_fp=8254523de55170bacbf9cc92c78fd6480c8b242ddff53b6b1811f4a16463aa0a source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=api -->
TrieTools.all_symbols returns all project symbols sorted by rank_by, bypassing grep's empty predicate guard.

- `rank_by`: sorting criterion, defaults to "inbound_count"
- `limit`: maximum symbols to return, defaults to 5000
- Returns: dict with "hits" list containing full SymbolDetail records
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.all_edges fingerprint=e20df0cb433306fcea49198faa9b933527f5b4f433c753442d6002fbeac61789 body_fp=01863d8239ea0077f7f02b427a37a184803b2400aab9f1fa5f09269cda13bfda source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Return all call-graph edges for the desktop app's initial graph population.

- `limit`: maximum number of edges to return (default 50000)
- Returns `{edges: [{from, to}, ...]}` — flat list of directed edges from SQLite
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.system_model fingerprint=172871e9e7f3321aa96d5cf81e8c08c11df7f77d7a5a2d7efe573091fbca9033 body_fp=e6cb2c4dc46624d3a9bde54016afa5ea29f3aa06a30386d5793c05c9515fb06d source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=mcp-server -->
Returns a high-level system model for desktop graph visualization with classified nodes, axis summaries, and landmarks.

- `landmark_limit`: maximum number of landmark symbols to include in the L1 view (default 160)
- `include_tests`: whether to include test symbols flagged as `is_test` (default False)
- returns: dict with `{nodes, axes: {role, subsystem}, landmarks, stats}` containing graph topology and metadata
- nodes are classified as door/hub/bedrock/exit/internal/orphan with salience scores and layout positions
- includes aggregated component groups and thresholded flow edges for architectural overview
- results cached on disk by graph fingerprint for instant repeat calls
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
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep fingerprint=7cca9c783d1f1827611377f5674891ce8d60fbb6554369a20d316ff1539e6c46 body_fp=5598346a77057e4a7d8206868d6d578abea802846376d206fe50226c62b38895 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
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
<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=39fb950cf30d8db1c53c19d70c183dac0a5026d690b104a4193debc0feb75ab9 body_fp=cd65fc43158d775e50baece7051c28207dacfcdad00abef5ecb5819505accb3b source_ref=b002a84e4f30d22b29fa6bf9f2f5d71998be7d82 role=parsing -->
Parses TrieTools agent predicate dict into GrepPredicate object or returns error envelope.

- Validates field types and value ranges for all grep filter parameters
- `_count_range` nested helper validates min/max objects for edge count filters  
- Returns tuple of (GrepPredicate, error_dict_or_None) for uniform error handling
- `scope_exclude` accepts string or list, normalizes to tuple of path prefixes
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=972dd361d21217884a13eb6b850eeee46e6bd6a0d749a8a7b0a4df77c7b81f37 body_fp=573e1cd394261764875d4b61ae90b15fd73a156e453515169627d426efaa3146 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
TrieTools.read retrieves a symbol's full prose documentation plus one-liner summaries of its immediate callers and callees.

- Returns dict with `qname`, `signature`, `prose`, `source_pointer`, `callers`, `callees`, optional `notes`
- Callers/callees truncated per config limits with notes when exceeded  
- Hub symbols (high inbound count) flagged in notes
- Pending patches included with origin tags (agent vs cascade)
- Emits telemetry with response metrics and optional capture
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
<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=166a30d30a42cc4658c0fe809d05fcd6f2535139057561cc30a211eaad225ade body_fp=4d8cda71245f2c08ff9c844ce70097cd1d0b58c47baa72a260b49bbfea4ef9df source_ref=2eb1969800e5124c94db178fe9d69fe146ad89ac role=api -->
Construct an MCP server with all trie tools registered from a TrieTools instance.

- Returns tuple of (FastMCP server, TrieTools) for testing and CLI reuse
- Registers 11 core tools: grep/read/trace family plus extended search/explain functions
- Registers 3 new file tools: grep_str_all, find_files, read_source, write_file  
- Registers 9 edit tools for full create/modify/delete/rename workflow with preview/commit
- Registers 8 desktop app helpers for graph visualization and file triefacts
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=c57b100fd07ba8bcfcaedebb2648cbe5949b2106b69128d814bb6c633382c744 body_fp=8a8cba0ff5e958f81c55546e70cad6b2d11b39ce9a25aa725ed997e48c4d1089 source_ref=88dd24eddd3b68c97efef6072f01ae2eb29d1a89 role=mcp-server -->
Run the MCP server over stdio for the project at `project_root`.

- Configures stdout and stderr for line buffering to ensure prompt output
- Blocks until the parent process closes the pipe
<!-- trie:end -->