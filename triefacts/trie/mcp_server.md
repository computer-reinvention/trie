---
trie_version: 0.1.0
source: trie/mcp_server.py
file_fingerprint: 603d01f010b2929ac6b20d18e6a44e209b7631021b71ca2e1029055ea100f0aa
last_synced_at: '2026-05-14T17:21:36Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 88-486
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 101-102
- kind: method
  qualified_name: trie/mcp_server:TrieTools.locate
  lines: 106-150
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain
  lines: 227-272
- kind: method
  qualified_name: trie/mcp_server:TrieTools.walk
  lines: 342-466
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 492-503
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 506-509
incoming_refs: 2
outgoing_refs: 10
---
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=3afac261a45c7adce610b119d56c701db4708148379bd67139606b201d9d4d2c body_fp=b4fef3d50737ccce9e82a62d62dcbfdc48ebb49d50fd4db5d2da5311b9562794 -->
## `TrieTools(project_root: Path)`

Host the three MCP tools (`locate`, `explain`, `walk`) as plain methods, owning a `Store` for the server process lifetime.

- `project_root`: resolved against `Config.find_and_load` to locate config and graph DB.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=dea1685fafbfd885cd0d5039bb88bac15fcf1910b30f092d6c55ae5445971767 -->
## `close() -> None`

Release the underlying Store's database connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.locate fingerprint=29eb69b3cefcaefb299d19c21bb3bae0701ebcc6fbf026a145486e24ec163b2f body_fp=d92e3c6ad7b476b5d742f959ec2dcfe2836552f3d7742bff7782bb17697d1e61 -->
## `locate(self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10) -> list[dict[str, Any]] | dict[str, Any]`

Find symbols in the store matching a structured predicate, returning a ranked, capped list of symbol records.

- `predicate`: optional dict with fields `name_contains`, `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`, `outbound_count`.
- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`.
- `limit`: clamped to `[1, mcp_cfg.locate_max_limit]`.
- Returns error envelope `{error: {code, message, suggestion?}}` on invalid input.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.explain fingerprint=1ae3cb9dd8160b29676fa21d3d2696c25fd9d736fce5215dac9f4191ea9f26d8 body_fp=d55a2f9866d870e58903233d0bec59cfd4e6566614af7d9b501ceb67f17ab071 -->
## `explain(self, qname: str) -> dict[str, Any]`

Return a symbol's full prose plus one-liner summaries of every immediate caller and callee.

- `qname`: fully-qualified symbol name, e.g. as returned by `locate`.
- Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
- Returns `{error: {code, message, suggestion}}` with code `not_found` if `qname` is unknown.
- `notes` lists truncation warnings, missing triefact warnings, and hub detection notices.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.walk fingerprint=2e6816ae285b1d494147432aa2d1877647aec570ba18adcd439bfa71f082d142 body_fp=98b0802773ecef2e1d9bc92328f5f126b79787a32a946f312a413e83d2f76f44 -->
## `walk(self, from_qname: str, direction: str = "callers", depth: int = 2) -> dict[str, Any]`

Trace the call graph from `from_qname` outward up to `depth` hops via BFS.

- `direction`: `"callers"`, `"callees"`, or `"both"`; invalid values return an error dict.
- `depth`: clamped to `Config.mcp.walk_max_depth`; a note records any clamping.
- Expansion halts at hub symbols (inbound count > `walk_hub_threshold`); their qnames appear in `truncated_at`.
- Returns `{root, nodes, edges, truncated_at?, notes?}`; nodes carry signature and one-liner only.
- For full prose on any node, call `explain` afterward.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=bd4ab2471102d2f7359a1496e476e579ec96cbe8b5577db0c3232e034acb8208 body_fp=3e0f55d5dda6919e5909c15aed0c620c39d8210053f126bbb4d7960f3a7b56d9 -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct an MCP server with `locate`, `explain`, and `walk` tools bound to `project_root`.

- Returns both the server and `TrieTools` to allow direct method calls in tests.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=8cde71e2ff11fda4cfbc2261e1213e79ff338b8961e2ab7b957cf8c864ef91a9 body_fp=8c2f5537c9cc2271008d996fd0e21c3a1cfdd2e2f6eb893d54b534bf302ba744 -->
## `run_stdio(project_root: Path) -> None`

Run the MCP server over stdio, blocking until the parent process closes the pipe.
<!-- trie:end -->