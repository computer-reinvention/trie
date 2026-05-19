---
trie_version: 0.1.1
source: trie/mcp_server.py
file_fingerprint: 1f3fc0d338f68c38148ecdadfa48f35db534ec727fc4d51adab6091b3acfb6e3
last_synced_at: '2026-05-19T10:41:17Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-1040
- kind: class
  qualified_name: trie/mcp_server:RipgrepNotFoundError
  lines: 58-70
- kind: function
  qualified_name: trie/mcp_server:_require_ripgrep
  lines: 73-88
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 91-104
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 107-111
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 114-120
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 123-125
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 128-129
- kind: function
  qualified_name: trie/mcp_server:_predicate_is_empty
  lines: 132-155
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 158-177
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 180-1010
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 194-216
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 218-219
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 223-338
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 340-477
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 479-578
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 580-603
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 605-631
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 633-711
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 715-773
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 775-812
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 814-839
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 843-990
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 994-1010
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 1016-1033
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 1036-1039
incoming_refs: 4
outgoing_refs: 29
---
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=7ee5dc607bb499394690a4b0485e255d6dd93b3328da3b8f98c5d2a04cd02296 body_fp=646da77eba50dd60498b67525315354b086abf60d422279c42e4c7acda551c4d source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `TrieTools`

Owns the Store and exposes `grep`, `read`, and `trace` as directly callable methods, decoupled from MCP transport.

- Accepts `event_name` kwarg (`"mcp_call"` default); CLI passes `"cli_call"` to separate telemetry.
- Emits `mcp_server_start` only when `event_name == "mcp_call"`; CLI construction is silent.
- Initialises `Config`, `Store`, ripgrep path, and telemetry from `project_root` at construction time.
- `close()` must be called to release the Store's database connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=442e119f95b99008035d6247dddce6fe6e965d30dfa4d278b5b93ce14b135e9f source_ref=7e9bcac1d9e11809a5a2f2cc565ded53aa1ea42b -->
## `close(self) -> None`

Release the underlying `Store` database connection.
<!-- trie:end -->







<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=9a66abda1c347da89b6316b6480760d01a9888829373bd13f361dd18378c1251 body_fp=4da1ceef0d377b1b81393c4a168bb8ac7609339d083f690a2df1b93390741336 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct a `FastMCP` server wired to trie's store under `project_root`, registering `grep`, `read`, and `trace` tools.

- Returns `(server, tools)` so tests and CLI subcommands can call `TrieTools` methods without driving the MCP transport.
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

<!-- trie:section symbol=trie/mcp_server:_symbol_summary fingerprint=2824255ca5be1745ada9b9e40660155f9a55afe2d80dc77fe97f7ace09fc95f8 body_fp=d14056c7c85e4ca05a23cd29f368b1e329f84d356594129366b55181d237f483 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
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

<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=74d86f992b0979150b25f2b106fe77651c32e445d36de5f044024d20949c62c9 body_fp=db79ca36a3b2a6c0c245c71ab29c3e4a560c4ea8ae4dc190c08a361979c76f19 source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `TrieTools.__init__(self, project_root: Path, *, event_name: str = "mcp_call") -> None`

Initialise the tool host: load config, resolve ripgrep, configure telemetry, and open the graph store.

- `project_root`: searches upward for `trie.toml`; resolved root may differ.
- `event_name`: controls telemetry event name; `mcp_server_start` is only emitted when it equals `"mcp_call"`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=39fb950cf30d8db1c53c19d70c183dac0a5026d690b104a4193debc0feb75ab9 body_fp=b41a8a30a553459309eece0878091eb2c28b0732ab182c84df88da25c801294a source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `_parse_predicate(self, predicate: dict[str, Any] | None) -> tuple[GrepPredicate, dict[str, Any] | None]`

Convert the raw predicate dict from an agent call into a `GrepPredicate`, returning a structured error on invalid input.

- Returns `(GrepPredicate(), error_dict)` on validation failure; `None` as second element on success.
- `kind` now accepts `"constant"` and `"module"` in addition to `"function"`, `"class"`, `"method"`, `"any"`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._prose_for fingerprint=7a45e1b328dea006c2f4a127330932dcfd60881d0d728880577bad7bda39f136 body_fp=5ad1a422bfc5d60aa359b8372a0c76705148e4576fe0bfb838c7159cf650ffc3 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `_prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]`

Read the triefact section body for a symbol, returning `(prose, notes)`.

- `notes`: non-empty when no triefact file exists, the section is missing, or a close sentinel is absent.
- `prose`: empty string on any failure; truncated to `read_prose_max_chars` on success.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._neighbour_summaries fingerprint=f3c2279bac29ff83aa239609a037abaa507bf0e9a1473c10b54bda79be3009ac body_fp=7bcaca454f4dd3c265e6d8ae42b33e9d2609de2747f0af6ff21bf673fddfc6d1 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `_neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]`

Resolve qnames to compact neighbour records, truncating to the configured per-direction cap.

- Returns `(records, note)` where `note` is non-None when records were truncated.
- Silently skips qnames whose symbols no longer exist in the store.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._suggest_for_qname fingerprint=5ac22b4d30b52fa3bf0f60a18bdbf94c7855456a7fa9b25fca44752526dc1a98 body_fp=f62353767b45a7a1f120d78f48c95866ed5637f140e7f4d0c99a620e2af8b8ca source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
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







<!-- trie:section symbol=trie/mcp_server:TrieTools._candidate_matches_predicate fingerprint=67f81def759871cd0f3e53436f8010818ba7ae33393fd206cd91da97251ffc74 body_fp=5000c3ff619dbaf5774b9769db8d18365f9d5e81ca377d3a3c69713e223e14bd source_ref=6795f2438f7cef495f72fab2ec62616550b31303 -->
## `_candidate_matches_predicate(self, detail: SymbolDetail, pred: LocatePredicate) -> bool`

Apply non-name predicate filters to a grep fallback candidate symbol.

- Skips `name_contains` check intentionally; only scope, visibility, kind, and edge-count bounds are enforced.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:RipgrepNotFoundError fingerprint=b95338f0dbd8392f5ddf76b76cd62399af964a45ad4a5b099397463519753605 body_fp=c1a44365ebc0cbbf17153502e6f9a4d3b771cb34b09ab99a00b9e888658f4165 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `RipgrepNotFoundError`

Raised at MCP server startup when `rg` (ripgrep) is not found on PATH.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_require_ripgrep fingerprint=056d3a41463d61526764214f6af30dce4f4833065b63def386f418891f20c4b6 body_fp=4ad43131cf9640c0fbade1d9ccd37fa572be6cb9aa3e2f2985939a2ba428c2fe source_ref=b5595ca0056fcd22d5e1be4c1818598a1e3aab28 -->
## `_require_ripgrep() -> str`

Return the absolute path to `rg` via `shutil.which`, or raise `RipgrepNotFoundError` if not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.grep fingerprint=a86181d3aeb234fb6e45066e5edeb4073aea9859961eb9e05c614c4b640bb0a1 body_fp=8af935992c9857d94f06440458a09b6a90d0bc9c33269203a2b29fcfd9ed04eb source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `grep(self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10) -> dict[str, Any]`

Find symbols matching a predicate, with a text-match fallback when no symbols match.

- `predicate`: optional dict with fields `name_contains`, `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`, `outbound_count`; at least one field required or returns `invalid_argument`.
- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`.
- `limit`: clamped to `[1, grep_max_limit]`; defaults to 10.
- Returns `{hits: [...]}` on success; adds `fallback` key when `hits` is empty.
- `fallback.kind` is `"none"`, `"text_match_empty"`, or `"text_match"` (ranked candidates).
- Returns `{"error": {code, message, suggestion}}` on bad predicate shape or empty predicate.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_text_match_fallback fingerprint=524de26eaf4596c55ebc847a83ce241a4ff09e4c5334887f11daf161a83e0d94 body_fp=a699eb066305a4eaf289544af95a90bee017b82797dd9c2eedbb5dcbfba7d0c6 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `_maybe_text_match_fallback(self, pred: GrepPredicate) -> dict[str, Any]`

Build the `fallback` envelope returned alongside an empty `hits` list when `grep` finds no symbol-name matches.

- Returns `kind="none"` when `pred.name_contains` is absent or blank.
- Returns `kind="text_match_empty"` when ripgrep finds no in-scope hits, or every hit falls outside a documented symbol, or no candidate survives the predicate's non-name filters.
- Returns `kind="text_match"` with candidates ranked by `inbound_count` desc, capped at `grep_fallback_match_limit`.
- `name_contains` is used as the ripgrep query; all other predicate filters still apply to candidates.
- `match_count` / `unique_symbols` indicate breadth before capping; `truncated=True` cases are noted in the response.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._text_match_in_scope fingerprint=d3b53cf1edec68c4065271cb469ec003b74e7141cf154025945db6ef0029f216 body_fp=0ac4ff41416f1fde7f6932ac71f447751232256cc4b13ed45d70564512290213 source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `_text_match_in_scope(self, query: str) -> dict[str, list[int]]`

Shell out to ripgrep to find literal, case-insensitive occurrences of `query` in in-scope source files.

- Returns `{src_root-relative path: [line numbers]}` for each matched file.
- Filters results against `discover_files` scope set, not ripgrep glob flags.
- Stops accumulating files once `grep_fallback_max_files` distinct files have hits.
- Raises `RuntimeError` if ripgrep exits with code ≥ 2.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools._attribute_text_matches_to_symbols fingerprint=638877abde73528dff2831fc527d43a63e2c5f7ea11680e7c835749eab28f9ca body_fp=599a942f33c5b9a43735b8cdefc021dbf876707072478af4899767da6c1064ac source_ref=cdb7c717485168c67e602f53f176ce638ce44ee9 -->
## `_attribute_text_matches_to_symbols(self, rg_hits: dict[str, list[int]]) -> dict[str, int]`

Map each `(file, line)` ripgrep hit to its smallest enclosing symbol, returning `{qname: hit_count}`.

- Lines outside any indexed symbol are silently dropped.
- Nesting resolved by picking the deepest symbol whose `[start_line, end_line]` brackets the match line.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=4169958b776cec1f8ce456c64e8cfb3cecad6995a99df2402d9fe7ab7f660268 body_fp=21359eba7ec65d07959c8f7f60c7cbf1cdc262d77c03da929ad16d5c781b75eb source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `read(self, qname: str) -> dict[str, Any]`

Read a symbol's full prose and compact one-liners for every immediate caller and callee.

- `qname`: fully-qualified symbol name as returned by `grep`.
- Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
- `notes` present when prose is missing, neighbours are truncated, or the symbol is a hub.
- Returns `{"error": {code, message, suggestion}}` if `qname` is not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.trace fingerprint=11fb60c36dc4704ea8181354ddf832facebad431d34b396f61015e0f9139c285 body_fp=41fe85050b6da40b6011f7912d5adc510026fd7523bd0ab685393303400d03cc source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `trace(self, from_qname: str, direction: str = "callers", depth: int = 2) -> dict[str, Any]`

Traverse the call graph from `from_qname` via BFS up to `depth` hops, returning nodes, edges, and truncation metadata.

- `direction`: one of `"callers"`, `"callees"`, or `"both"`; invalid value returns an error dict.
- `depth`: clamped to `Config.mcp.trace_max_depth`; clamping is noted in `result["notes"]`.
- Hub symbols (inbound count > `trace_hub_threshold`) block further expansion; their qnames appear in `truncated_at`.
- Node capacity (`trace_max_nodes`) is enforced BFS-order; hitting it adds a note but does not error.
- Each edge record: `{from, to, direction}` where `direction` is `"in"` (caller-side) or `"out"` (callee-side).
- Returns `{root, nodes, edges, truncated_at?, notes?}`; prose is omitted — follow up with `read` for a specific node.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:_predicate_is_empty fingerprint=0f46c4ac2fd44729683e473ace14c19cacdab7b4def3185826c7c004b4f8aefe body_fp=74a71f96050c5ecbee7c7ad0bc938c8fd109928ee78c0731a02240324484d19e source_ref=208d963e8755736b64473d98f04dd5c5ac701361 -->
## `_predicate_is_empty(pred: GrepPredicate) -> bool`

Return `True` when `pred` contains no filter that would narrow the symbol result set.

- Returns `True` when `name_contains` is falsy, `kind` is `None` or `"any"`, `scope_prefix`/`scope_exclude` are absent, `public_only` is `False`, and all edge-count bounds are `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=bd0b12eff0808bf296717b6a3e5dca068ff7711c7d60fc68c213790788812d6f source_ref=1d147ec50d38a315efdd117d9e4b3a9082c6e549 -->
## `mcp_server`

Expose the trie triefact tree and symbol graph to coding agents via MCP over stdio.

- Three tools: `grep` (find symbols), `read` (prose + neighbours), `trace` (graph topology).
- Same logic served by both MCP wire protocol and `trie grep/read/trace` CLI subcommands.
- Errors return `{code, message, suggestion}` for agent-recoverable failures.
- Requires `rg` (ripgrep) on PATH; fails at startup if absent.
<!-- trie:end -->