---
trie_version: 0.1.0
source: trie/mcp_server.py
file_fingerprint: dd6150114ab5b7c73dd5bd3f7920f782cebda2dfbb67b13afab1fbefe725ca6d
last_synced_at: '2026-05-14T18:31:50Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 90-544
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 109-110
- kind: method
  qualified_name: trie/mcp_server:TrieTools.locate
  lines: 114-172
- kind: method
  qualified_name: trie/mcp_server:TrieTools.explain
  lines: 249-307
- kind: method
  qualified_name: trie/mcp_server:TrieTools.walk
  lines: 377-524
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 550-561
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 564-567
incoming_refs: 2
outgoing_refs: 10
---
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=a9276102fa3197d721d6aeea11f59f308aa262003a5bfdbdd933bdab4b98f35d body_fp=1896c8f1ff3cbc085a8570a7d7b569fbbc5b4a4a0de5b58e9942e4954f76970c -->
## `TrieTools`

Encapsulate the three MCP tool methods (`locate`, `explain`, `walk`) against a persistent `Store`, testable without MCP transport.

- `project_root`: resolved via `Config.find_and_load`; determines DB path and triefact tree location.
- Call `close()` to release the underlying store connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=442e119f95b99008035d6247dddce6fe6e965d30dfa4d278b5b93ce14b135e9f -->
## `close(self) -> None`

Release the underlying `Store` database connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.locate fingerprint=153edba47e914290ef15c96bc9115c1ad61b23c296b28968be5602c151f6cba8 body_fp=66b21097a42278633e30412ff580679c88a9b39f242d8ec108a3dda3a482a1a1 -->
## `locate(self, predicate: dict[str, Any] | None = None, rank_by: str | None = None, limit: int = 10) -> list[dict[str, Any]] | dict[str, Any]`

Find symbols in the store matching a structured predicate, returning ranked, capped results.

- `predicate`: dict with optional keys `name_contains`, `kind`, `scope_prefix`, `scope_exclude`, `public_only`, `inbound_count`, `outbound_count`.
- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`.
- `limit`: capped server-side at `mcp_cfg.locate_max_limit`; values below 1 are raised to 1.
- Returns a list of symbol dicts or an `{error: ...}` envelope on bad input.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.explain fingerprint=b6b7c0bc63a3e0879a5888ead9fce642aa5c3f94e8f2540a3de2f32b70e23bca body_fp=275b10af2a169586a33fd4c8bba145ecf9e2fed7394993dde28ceb3860bc3249 -->
## `explain(self, qname: str) -> dict[str, Any]`

Return a symbol's full prose and compact one-liners for every immediate caller and callee.

- `qname`: fully-qualified symbol name as stored in the graph DB.
- Returns `{qname, signature, prose, source_pointer, callers, callees, notes?}`.
- Returns `{error: {code, message, suggestion}}` if `qname` is not found.
- `notes`: list of warnings about missing triefacts, hub symbols, or truncated neighbours.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.walk fingerprint=a47a925d92469a18a79aa4f13ef64e4a34cc19c41cc83e2d0d0fc29ae0104183 body_fp=0c6c7c2f0b331a9c4a6fba9f1c96a024197c484f3b7386d52e70811fe61c67ee -->
## `walk(self, from_qname: str, direction: str = "callers", depth: int = 2) -> dict[str, Any]`

Trace the call graph from `from_qname` outward up to `depth` hops via BFS.

- `direction`: `"callers"`, `"callees"`, or `"both"`; controls which edges are followed.
- `depth`: clamped to `Config.mcp.walk_max_depth`; a note is added if clamped.
- Returns `{root, nodes, edges, truncated_at?, notes?}`; hub symbols (inbound count above threshold) halt expansion and appear in `truncated_at`.
- Expansion halts early and adds a note when `walk_max_nodes` is reached.
- Edge records carry `direction`: `"in"` (neighbour calls node) or `"out"` (node calls neighbour).
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=bd4ab2471102d2f7359a1496e476e579ec96cbe8b5577db0c3232e034acb8208 body_fp=465a6923a499ff236b872cd60d4956e2fe4fb4f5a8838254749fbcf7f9ee949f -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct an MCP server bound to the trie state under `project_root`, registering all three tools.

- Returns `(FastMCP, TrieTools)`; `TrieTools` is exposed for direct testing without the MCP transport.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=8cde71e2ff11fda4cfbc2261e1213e79ff338b8961e2ab7b957cf8c864ef91a9 body_fp=67b250d9427021896d3cc51336addbd6b9578fbbf05a05b75bb8fc586530b87c -->
## `run_stdio(project_root: Path) -> None`

Build and run the MCP server over stdio, blocking until the parent process closes the pipe.
<!-- trie:end -->