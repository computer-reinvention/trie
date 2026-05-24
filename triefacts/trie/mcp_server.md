---
trie_version: 0.1.2
source: trie/mcp_server.py
file_fingerprint: ae9721249457040b322c6eeac8a1c9c0aa53d92f52cbe10a3f3214e3cf48f591
last_synced_at: '2026-05-23T23:20:18Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: module
  qualified_name: trie/mcp_server:__module__
  lines: 1-1840
- kind: class
  qualified_name: trie/mcp_server:RipgrepNotFoundError
  lines: 75-87
- kind: function
  qualified_name: trie/mcp_server:_require_ripgrep
  lines: 90-105
- kind: function
  qualified_name: trie/mcp_server:_error
  lines: 108-121
- kind: function
  qualified_name: trie/mcp_server:_truncate
  lines: 124-128
- kind: function
  qualified_name: trie/mcp_server:_symbol_summary
  lines: 131-137
- kind: function
  qualified_name: trie/mcp_server:_close_qname_matches
  lines: 140-143
- kind: function
  qualified_name: trie/mcp_server:_close_name_matches
  lines: 146-148
- kind: function
  qualified_name: trie/mcp_server:_fuzzy_score
  lines: 151-162
- kind: function
  qualified_name: trie/mcp_server:_score_sym
  lines: 165-190
- kind: function
  qualified_name: trie/mcp_server:_predicate_is_empty
  lines: 193-216
- kind: function
  qualified_name: trie/mcp_server:_smallest_enclosing
  lines: 219-238
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 241-1802
- kind: method
  qualified_name: trie/mcp_server:TrieTools.__init__
  lines: 255-277
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 279-280
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep
  lines: 284-414
- kind: method
  qualified_name: trie/mcp_server:TrieTools._maybe_text_match_fallback
  lines: 416-560
- kind: method
  qualified_name: trie/mcp_server:TrieTools._fuzzy_prose_fallback
  lines: 562-638
- kind: method
  qualified_name: trie/mcp_server:TrieTools._text_match_in_scope
  lines: 640-739
- kind: method
  qualified_name: trie/mcp_server:TrieTools._attribute_text_matches_to_symbols
  lines: 741-764
- kind: method
  qualified_name: trie/mcp_server:TrieTools._candidate_matches_predicate
  lines: 766-792
- kind: method
  qualified_name: trie/mcp_server:TrieTools._parse_predicate
  lines: 794-872
- kind: method
  qualified_name: trie/mcp_server:TrieTools.read
  lines: 876-934
- kind: method
  qualified_name: trie/mcp_server:TrieTools._prose_for
  lines: 936-973
- kind: method
  qualified_name: trie/mcp_server:TrieTools._neighbour_summaries
  lines: 975-1000
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace
  lines: 1004-1151
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_str
  lines: 1155-1314
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_entry_points
  lines: 1316-1399
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol
  lines: 1401-1502
- kind: method
  qualified_name: trie/mcp_server:TrieTools.grep_symbol_and_neighbours
  lines: 1504-1530
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol
  lines: 1532-1613
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_symbol_references
  lines: 1615-1676
- kind: method
  qualified_name: trie/mcp_server:TrieTools.trace_flow
  lines: 1678-1736
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain_flow
  lines: 1738-1782
- kind: method
  qualified_name: trie/mcp_server:TrieTools._suggest_for_qname
  lines: 1786-1802
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 1808-1833
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 1836-1839
incoming_refs: 6
outgoing_refs: 53
---
<!-- trie:section symbol=trie/mcp_server:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=bd7fd38d006d3e2be13e6fbe69c10dab76510d9f1eaaf30c8cc1ed71d5d10420 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `trie/mcp_server`

MCP server exposing the trie triefact tree and symbol graph to coding agents over stdio.

- Implements three core tools: `grep`, `read`, `trace`.
- Adds eight agent-ergonomic wrappers: `grep_str`, `grep_entry_points`, `grep_symbol`, `grep_symbol_and_neighbours`, `explain_symbol`, `explain_symbol_references`, `trace_flow`, `explain_flow`.
- All tools share `TrieTools` methods; CLI subcommands and MCP wire calls produce identical responses.
- Requires `rg` (ripgrep) on PATH; fails at startup if absent.
- Errors return `{code, message, suggestion}` for single-round-trip agent recovery.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:RipgrepNotFoundError fingerprint=b95338f0dbd8392f5ddf76b76cd62399af964a45ad4a5b099397463519753605 body_fp=c3474cef6fd32d0b749af408f0014d32ce1304ab2353ed6f1a4a9fdd9cbc6e78 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `RipgrepNotFoundError`

Raised at `TrieTools` startup when `rg` (ripgrep) is not on PATH.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_require_ripgrep fingerprint=056d3a41463d61526764214f6af30dce4f4833065b63def386f418891f20c4b6 body_fp=0254468ceab79deaedf96b80a3301428877f70ac4dd9aa114d7e770f54d50b2d source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_require_ripgrep() -> str`

Return the absolute path to `rg` via `shutil.which`, or raise `RipgrepNotFoundError` if not on PATH.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_error fingerprint=597d455ff4a9e49ecd772c061e825ab45cae7724ee3d569343b9cfa871474702 body_fp=4c726e3ad83926567a094a0a28cb2edea399542ed784d5a5522a1af4bc2b9fff source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_error(code: str, message: str, suggestion: str | None = None) -> dict[str, Any]`

Build the canonical error envelope `{error: {code, message, suggestion?}}`.

- `suggestion`: included only when a concrete recovery step exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_truncate fingerprint=fc4edfb1b25a174070610aef0283c1a28160f8d6cf1ad2b088deff400629bfbf body_fp=c34ebb31bffd7ebd338140cf67b908ab3ae02c09a3d5fd74604bfbd3aa2f678b source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_truncate(text: str, max_chars: int) -> str`

Truncate `text` to `max_chars`, appending `…` when clipped; `0` disables the cap.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_symbol_summary fingerprint=2824255ca5be1745ada9b9e40660155f9a55afe2d80dc77fe97f7ace09fc95f8 body_fp=ba6bfe2e359926408c83e4b4a37e0b43fa8022b0a5f9be55754996c0ba8625d8 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_symbol_summary(detail: SymbolDetail, *, one_liner_max: int) -> dict[str, Any]`

Build a compact `{qname, signature, one_liner}` record from a `SymbolDetail` for neighbour and trace-node lists.

- `one_liner_max`: character cap passed to `_truncate`; `0` means no cap.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_qname_matches fingerprint=501f57c95b68de44bbc214d45d865ab70c8460555e35a1a55da2d4271bee3666 body_fp=211aac50e883d56f08fd72131516e3e6b04cd8204f8dfb454783fc5e66f756fd source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_close_qname_matches(qname: str, candidates: list[str], *, n: int = 3) -> list[str]`

Return up to `n` fuzzy-matched qualified names from `candidates` for `not_found` suggestions.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_close_name_matches fingerprint=78c86c0dfb91a0fc6a7a7cda37db88b68e1caad670ce91e6769b951b0ba033f1 body_fp=1aed031b56505dac2fbaacca1896dd688f4cc7615ce059b4794713f3a2e74bbe source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_close_name_matches(name: str, candidates: list[str], *, n: int = 3) -> list[str]`

Return up to `n` fuzzy-matched strings from `candidates` using WRatio scoring with a cutoff of 45.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_fuzzy_score fingerprint=df1930a7033c1b75555083d67164a88ea342c7c428aef37d59a7a7a604a6f23b body_fp=11f1f2ad4ac0d95f0654481afeb3fcd3bdc748a7d4a5cb23494a76fb9993ff92 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_fuzzy_score(query: str, text: str) -> float`

Return a 0–100 rapidfuzz WRatio score, returning 100.0 immediately on exact case-insensitive substring match.

- Returns `0.0` when `text` is empty.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_score_sym fingerprint=7e3bbbed40177fcdb72361bc232f83c84a1484192b11a66452b2d23aee321f0f body_fp=d33a4b447278aaeedba93854eb8d338e82ee85c7725963fe88d7f22cfb2f72e6 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_score_sym(query: str, sym: SymbolDetail, *, prose: str = "", prose_weight: float = 0.6) -> float`

Return a 0–100 composite relevance score for `sym` against `query`, taking the max across three weighted layers.

- `prose`: caller supplies this lazily; omit to skip disk reads on hot paths.
- `prose_weight`: scales the prose layer; lower than name (1.0) and one_liner (0.8) by default.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_predicate_is_empty fingerprint=0f46c4ac2fd44729683e473ace14c19cacdab7b4def3185826c7c004b4f8aefe body_fp=5aac7852e726a81b0d9f06536e2b155b02c7dd5b8b11659399746c755a5eab45 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_predicate_is_empty(pred: GrepPredicate) -> bool`

Return `True` when `pred` has no filter that would narrow the symbol result set.

- Returns `True` only when all fields are unset: falsy `name_contains`, `kind` is `None` or `"any"`, no `scope_prefix`/`scope_exclude`, `public_only` is `False`, and all edge-count bounds are `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:_smallest_enclosing fingerprint=4839c335a6d869c0fcaaaeb5126b1db1ddeac056279037b8a98dc142a759a02f body_fp=05b050b4c2eb2c8b1639ec0508b67bb3c8ba1c2b91889d639c3001f2247d395c source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `_smallest_enclosing(symbols: list[tuple[str, int, int]], lineno: int) -> str | None`

Return the qname of the innermost symbol whose line range contains `lineno`.

- `symbols`: start-line-ordered `(qname, start_line, end_line)` triples.
- Returns `None` when `lineno` falls outside all symbol ranges (module-level code, imports).
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=ccdef9669595a4a398d28af3a7ad263c7e69a1f17309d45f02050e0156de2cde body_fp=1890892b3dc4fc48abb98b313da52ab3f8fa23c84d9ad225db6ab832a4e9f2b0 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools(project_root: Path, *, event_name: str = "mcp_call")`

Implement all MCP and CLI tool methods as plain Python, owning the `Store` for the process lifetime.

- `event_name`: distinguishes MCP (`"mcp_call"`) from CLI (`"cli_call"`) in telemetry.
- `store`: opened against `.trie/graph.db` under the resolved project root.
- `rg_path`: resolved at construction; raises `RipgrepNotFoundError` if `rg` is absent.
- `grep`: symbol-name predicate search with ripgrep + fuzzy fallbacks on empty hits.
- `read`: returns full prose + neighbour one-liners for one exact qname.
- `trace`: BFS over the call graph up to `depth` hops; stops at hub symbols.
- `grep_str`: regex search over raw source bodies, results attributed to enclosing symbols.
- `grep_entry_points`: fuzzy-prose search restricted to high-inbound public symbols.
- `grep_symbol`: fuzzy name lookup returning best match + similar list.
- `grep_symbol_and_neighbours`: `grep_symbol` plus immediate caller/callee summaries.
- `explain_symbol`: prose + joined narrative weaving callee and caller prose snippets.
- `explain_symbol_references`: caller-side usage story only, no symbol's own prose.
- `trace_flow`: shortest call chain(s) between two symbols via `Store.find_paths`.
- `explain_flow`: `trace_flow` + per-node prose joined as an execution narrative.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.__init__ fingerprint=74d86f992b0979150b25f2b106fe77651c32e445d36de5f044024d20949c62c9 body_fp=f55bf426e5a01672ebf045ba328f8c7753550120e266c898e06b2e094f08ef96 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.__init__(self, project_root: Path, *, event_name: str = "mcp_call") -> None`

Initialize a `TrieTools` instance, loading config, resolving ripgrep, configuring telemetry, and opening the graph store.

- `event_name`: `"mcp_call"` emits `mcp_server_start` telemetry; `"cli_call"` skips it.
- Raises `RipgrepNotFoundError` immediately if `rg` is not on PATH.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=82c9b284e567ebd2a20c301c5898b1c58437adab16052bb9c89eb02071c12e6e source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.close() -> None`

Close the `TrieTools` store connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep fingerprint=90ba90cba54b502de62199bbe77d945223ddf87f05a28f3e5c82bf682d9a1ec4 body_fp=66bee2159bf22046dad6ed5f3bd4e058cec9db971bc2355dfe6933ab84dd585d source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.grep(predicate, rank_by=None, limit=10) -> dict`

Query the symbol graph by predicate, returning ranked hits with fallback when empty.

- `predicate`: dict with optional fields `name_contains`, `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`, `outbound_count`; at least one field required.
- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`.
- `limit`: capped at `mcp_cfg.grep_max_limit`.
- `hits`: list of `{qname, signature, file_pointer, one_liner, is_public, kind, inbound_count, outbound_count}`.
- `fallback`: present when `hits` is empty; `kind` is `"none"`, `"text_match_empty"`, `"text_match"`, or `"fuzzy_prose"`.
- Empty predicate returns `invalid_argument` error rather than an unfiltered result.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._maybe_text_match_fallback fingerprint=82fbd1dbe26ec388045f10fe0ceeb2470f1d4d7a6ae9a4f4c506d51ff6e1cc38 body_fp=67df84b5f809a0c9cc92a0caadc02a471bfc3784bbc13be1271198d456795de6 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._maybe_text_match_fallback(self, pred: GrepPredicate) -> dict[str, Any]`

Build the `fallback` envelope returned alongside an empty `hits` list in `TrieTools.grep`.

- Returns a dict with `kind` always present: `"none"` (no `name_contains`), `"text_match_empty"` (query absent from all in-scope bodies), or `"text_match"` (ranked symbol hits).
- Falls through to `_fuzzy_prose_fallback` before emitting `text_match_empty` when ripgrep finds nothing or no candidates survive predicate filters.
- Non-name predicate fields (`scope_prefix`, `scope_exclude`, `public_only`, `kind`, edge-count bounds) are enforced on candidates even on this fallback path.
- Results ranked by `inbound_count` descending, capped at `grep_fallback_match_limit`; truncation noted in `note` field.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._fuzzy_prose_fallback fingerprint=0c1e0782658f14fba532c4353851b382fdd0e24428fd65598839f72fbc87215c body_fp=27daa5b47fd9f812e8d0acc63eb74eddda34907f4f8dc94e2bf0b6817bd61fc3 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._fuzzy_prose_fallback(self, query: str, pred: GrepPredicate) -> dict[str, Any] | None`

Score all in-scope symbols against `query` via name, one_liner, and prose, returning a `fuzzy_prose` envelope or `None`.

- Called only after both SQL name-match and ripgrep body-match return nothing.
- Applies predicate's scope/kind/public filters before scoring to limit the sweep.
- Prose read is lazy: only fetched when name+one_liner pre-score clears `fuzzy_prose_pre_filter`.
- Returns `None` when no candidate clears `fuzzy_cutoff`; caller falls through to `text_match_empty`.
- Results sorted by score descending, then `inbound_count`; capped at `grep_fallback_match_limit`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._text_match_in_scope fingerprint=d3b53cf1edec68c4065271cb469ec003b74e7141cf154025945db6ef0029f216 body_fp=16a00d1c3a102689e4d876632baff9b41c55b70620bb39cdf91bc5b1547bb9d0 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._text_match_in_scope(self, query: str) -> dict[str, list[int]]`

Shell out to ripgrep to find `query` as a literal string in in-scope source files, returning matched line numbers keyed by relative path.

- Returns `{rel_path: [line_numbers]}` relative to `src_root`; empty dict if no matches.
- Runs `rg --fixed-strings --ignore-case --json`; raises `RuntimeError` on exit code ≥ 2.
- Post-filters results against `discover_files` scope set; not translated to `--glob` flags.
- Stops accumulating after `grep_fallback_max_files` distinct files have hits.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._attribute_text_matches_to_symbols fingerprint=638877abde73528dff2831fc527d43a63e2c5f7ea11680e7c835749eab28f9ca body_fp=4b36d9781b95222b8e0f446e4e85ae9e5040e9766ccf4de7b0e2dd88cafca333 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._attribute_text_matches_to_symbols(self, rg_hits: dict[str, list[int]]) -> dict[str, int]`

Map each `(file, line)` ripgrep hit to the smallest enclosing symbol, returning `{qname: hit_count}`.

- `rg_hits`: `{relative_file_path: [line_numbers]}` as produced by `_text_match_in_scope`.
- Lines outside any symbol boundary are silently dropped.
- Nested symbols resolve to the innermost (method, not enclosing class).
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._candidate_matches_predicate fingerprint=67f81def759871cd0f3e53436f8010818ba7ae33393fd206cd91da97251ffc74 body_fp=cfe9c4c72dd6f9d8c6d7f2008cea308bc3904c04ae1f18217ff9d299f08fd47c source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._candidate_matches_predicate(self, detail: SymbolDetail, pred: GrepPredicate) -> bool`

Apply non-name predicate filters to a fallback candidate, returning `False` if any filter rejects it.

- `name_contains` is deliberately ignored; fallback candidates already failed that filter.
- Enforces `scope_prefix`, `scope_exclude`, `public_only`, `kind`, and edge-count bounds.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._parse_predicate fingerprint=39fb950cf30d8db1c53c19d70c183dac0a5026d690b104a4193debc0feb75ab9 body_fp=eba395dfa12c797c5d518e72feeb378f1fb24b9e7453423757583c57aacaaf01 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._parse_predicate(self, predicate: dict[str, Any] | None) -> tuple[GrepPredicate, dict[str, Any] | None]`

Validate and convert an agent-supplied predicate dict into a `GrepPredicate`, returning an error envelope on invalid input.

- Returns `(GrepPredicate(), None)` when `predicate` is `None`.
- Second tuple element is a `_error(...)` dict on validation failure, `None` on success.
- Validates `kind` against the allowed literal set; validates `inbound_count`/`outbound_count` as `{min?, max?}` int objects.
- Normalises `scope_exclude`: accepts a bare string or a list; coerces elements to `str`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.read fingerprint=4169958b776cec1f8ce456c64e8cfb3cecad6995a99df2402d9fe7ab7f660268 body_fp=fd1f7921d478b5cb58be553da5e5f9eab2d45e3176d4874915f3913c7640cb80 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.read(self, qname: str) -> dict[str, Any]`

Fetch a symbol's triefact prose plus compact summaries of its immediate callers and callees.

- `qname`: exact qualified name; returns `not_found` error with fuzzy suggestions if absent.
- `notes`: populated when prose is missing, neighbours are truncated, or the symbol is a hub.
- Hub symbols (inbound count above threshold) are flagged but not expanded further.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._prose_for fingerprint=7a45e1b328dea006c2f4a127330932dcfd60881d0d728880577bad7bda39f136 body_fp=d20d13ec2624dcebd336892642954f41cfffc2d3a6a0bc6a7f9b92c8ed4dfb61 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._prose_for(self, detail: SymbolDetail) -> tuple[str, list[str]]`

Pull the section body verbatim from the triefact file for `detail`.

- Returns `("", [note])` when the triefact file is missing or the symbol's section is absent.
- Parses section sentinels via regex; avoids loading `TriefactFile`/YAML.
- Prose is truncated to `mcp_cfg.read_prose_max_chars`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._neighbour_summaries fingerprint=f3c2279bac29ff83aa239609a037abaa507bf0e9a1473c10b54bda79be3009ac body_fp=6edc97b187aa28be2b22530036031eaf1cbbba25629363b0865b54d658a1130f source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._neighbour_summaries(self, qnames: list[str]) -> tuple[list[dict[str, Any]], str | None]`

Resolve qnames to compact neighbour records, truncating to the per-direction cap if exceeded.

- Returns `(records, note_or_None)`; note is non-`None` only when the cap was hit.
- Silently skips qnames whose `SymbolDetail` no longer exists in the store.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace fingerprint=11fb60c36dc4704ea8181354ddf832facebad431d34b396f61015e0f9139c285 body_fp=6450dea5bf1c128682725710d90ed624067bb0fe058ac392889778f43aca7348 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.trace(from_qname, direction="callers", depth=2) -> dict[str, Any]`

BFS-expand the call graph from `from_qname` up to `depth` hops, returning nodes, edges, and hub-truncation metadata.

- `direction`: `"callers"`, `"callees"`, or `"both"`; edges tagged `"in"`/`"out"` relative to root.
- `depth`: clamped to `Mcp.trace_max_depth`; a note is added when clamped.
- Hub symbols (inbound count > `trace_hub_threshold`) halt expansion; their qnames appear in `truncated_at`.
- Returns signatures and one-liners only; use `read` for prose on specific nodes.
- Capacity hit (`trace_max_nodes`) produces a BFS-ordered partial result with a note.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_str fingerprint=7c92736236e6ccc5c8d906b78b97bcf545f2f54c2e218635cb1851d8a07888ab body_fp=85ee0fc32b563d842815c118901c153131e5f1b04927420708ea0287e67d576c source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.grep_str(self, regexp: str) -> dict[str, Any]`

Search in-scope source bodies with a ripgrep regex and attribute matched lines to their smallest enclosing symbols.

- `regexp`: full regex pattern; matched case-insensitively against raw source text.
- On zero ripgrep hits, falls back to fuzzy scoring (name + one_liner + prose); returns `fallback.kind="fuzzy_one_liner"` with ranked matches.
- `hits[].match_count`: number of lines within that symbol's body that matched.
- Results ranked by `inbound_count` descending; filtered to in-scope files only.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_entry_points fingerprint=a40b453a3358e2fb289e16ffa988fa7300da361d6366c30d5b035811b7564545 body_fp=b4a4c7919d3219722b2469dd982dffa1a9e3a6b671e3673653053addf59db86f source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.grep_entry_points(self, query: str) -> dict[str, Any]`

Find public, high-inbound-count symbols whose triefact prose fuzzy-matches `query`, sorted by relevance descending then inbound-count ascending.

- `query`: free-text topic; matched against symbol name, one_liner, and prose body.
- Candidate pool: `public_only=True`, `inbound_count_min=2`; prose read lazily only when name/one_liner pre-score clears `fuzzy_prose_pre_filter`.
- Returns `{hits: [{qname, signature, file_pointer, one_liner, inbound_count, prose_snippet, score}]}`; empty hits include a `note`.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol fingerprint=8f3e4bf4c648a9d74203d23ce3e4dd811c1954895663a4a1dca66d22e49bae91 body_fp=7d71246f139a29dd89f9b2f01b0422a1791d42b8e86185a34f45964d49ace3e9 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.grep_symbol(self, sym: str) -> dict[str, Any]`

Resolve a fuzzy symbol name to the best-matching symbol plus up to nine similar alternatives.

- `sym`: partial name, typo, or description; resolved via SQL LIKE → rapidfuzz fallback → prose scoring.
- `match`: highest-scoring `SymbolDetail` with a `score` field (0–100) explaining its rank.
- `similar`: next nine candidates by descending score.
- Returns `{"error": {...}}` when no candidate clears the configured fuzzy cutoff.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.grep_symbol_and_neighbours fingerprint=7ea37438f4dc626cbdbb108b54c36c9dc7731a3b134e51c78f5228e1295929ad body_fp=d35c0c5d2078e9226e5296ad6976e95e703eb2ded2809505ddd7b8296ad7262d source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.grep_symbol_and_neighbours(sym: str) -> dict[str, Any]`

Extend `TrieTools.grep_symbol` with immediate caller and callee summaries in a single round trip.

- **`callers`/`callees`**: trimmed neighbour records from `_neighbour_summaries`, subject to `read_max_neighbours_per_direction` cap.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol fingerprint=27d2591b20b21c2dd2dae483931f70266fe2b2555692cf8d75905ddb48174323 body_fp=ced2a4574ec6017026f33fb343701cb3d64f9fd15733fb4f8f19705461e5caa7 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.explain_symbol(sym: str) -> dict[str, Any]`

Return full triefact prose for a symbol plus a joined narrative weaving in first-paragraph prose of up to 5 callers and 5 callees.

- `sym`: exact qname or fuzzy name; resolved via `grep_symbol` if not found directly.
- `story`: Markdown sections "**Calls into:**" and "**Called by:**" joined with blank lines; empty string if no neighbours have prose.
- `notes`: present only when `_prose_for` reports a missing or corrupt triefact.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_symbol_references fingerprint=eea4957620148f9d0248392d9f05abb2b42803af63e9fcd92c25002b5b64438a body_fp=f6feda51daa8364d4efdf43527e1922a2732051221da3082fe0e4c2d4e00c3eb source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.explain_symbol_references(sym: str) -> dict[str, Any]`

Resolve `sym` (fuzzy if needed) and return a usage narrative built from the prose of its callers only.

- `usage_story`: first prose paragraph of each caller joined with `\n\n`; falls back to `one_liner`; capped at 8 callers.
- `callers`: compact neighbour records via `_neighbour_summaries`.
- Skips the symbol's own prose entirely — caller-side context only.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.trace_flow fingerprint=4dd9d61ff701bd2992e0aa4e9b3b5d43ff52b010a1562bc193ddaa229de437b6 body_fp=8c9c3d618480b3c0ccfbd59d4bdf131135fa51d1e3a79c4fc55ddb40bf165508 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.trace_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]`

Find shortest call chain(s) between two symbols, accepting fuzzy names for both.

- Both arguments are fuzzy-resolved via `grep_symbol` before path search.
- Skips hub symbols during expansion; returns up to 3 paths.
- Empty `paths` list is returned with a diagnostic `notes` entry when no chain exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools.explain_flow fingerprint=47e5b35007183ceaa63f7a11cb99ebc79fbbbce4788c1bd0ecfe4c5e0a088870 body_fp=a631aa36c618f783e9c33e7880ddae4f114c886ae477085c14fb8c78559df320 source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools.explain_flow(self, symbol1: str, symbol2: str) -> dict[str, Any]`

Call `trace_flow` between two symbols and enrich each path with a prose narrative joining each node's first triefact paragraph.

- `paths`: list of `{chain: [qname,...], narrative: str}` where narrative steps are joined by `→`.
- Falls back to `one_liner` when a node has no triefact prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:TrieTools._suggest_for_qname fingerprint=5ac22b4d30b52fa3bf0f60a18bdbf94c7855456a7fa9b25fca44752526dc1a98 body_fp=52618f4c40896eae1e53681a1df71b765d8df68ce5f5ba1aa7c2c79f5095528d source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `TrieTools._suggest_for_qname(self, qname: str) -> str | None`

Return a human-readable suggestion string for a `not_found` qname, using fuzzy qname then local-name fallback.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=7e6b1b7cd56397ea5407d43392250a4baff694a48366105321bfb3b58f69f752 body_fp=98929baa4159a70e810b58adc5ecb8a1e42fd8ce676bd141b1a40b89572dac4d source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct a `FastMCP` server with all eleven trie tools registered, bound to the trie state under `project_root`.

- Returns both the server and the `TrieTools` instance so tests and CLI subcommands can invoke tool methods without the MCP transport.
<!-- trie:end -->
<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=8cde71e2ff11fda4cfbc2261e1213e79ff338b8961e2ab7b957cf8c864ef91a9 body_fp=fdb6d169f4f6114f67c1df8a4c625282f1e12f5ce069ae0b76d581304bc689bb source_ref=a187b0cf4b9dbac53f5b1253491cdb904e3072b4 -->
## `run_stdio(project_root: Path) -> None`

Start the MCP server over stdio, blocking until the parent process closes the pipe.
<!-- trie:end -->