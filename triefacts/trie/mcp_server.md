---
trie_version: 0.1.0
source: trie/mcp_server.py
file_fingerprint: 4374c97fff705c75d8267b33847ec3eaf6bcdb08d5f5e4269643bee0ba1bd59f
last_synced_at: '2026-05-12T18:31:26Z'
description: MCP server exposing the trie triefact tree + symbol graph to coding agents.
defines:
- kind: class
  qualified_name: trie/mcp_server:TrieTools
  lines: 37-88
- kind: method
  qualified_name: trie/mcp_server:TrieTools.close
  lines: 49-50
- kind: method
  qualified_name: trie/mcp_server:TrieTools.get_triefact
  lines: 52-64
- kind: method
  qualified_name: trie/mcp_server:TrieTools.find_symbol
  lines: 66-73
- kind: method
  qualified_name: trie/mcp_server:TrieTools.references_to
  lines: 75-83
- kind: method
  qualified_name: trie/mcp_server:TrieTools.references_from
  lines: 85-88
- kind: function
  qualified_name: trie/mcp_server:build_server
  lines: 91-103
- kind: function
  qualified_name: trie/mcp_server:run_stdio
  lines: 106-109
incoming_refs: 2
outgoing_refs: 4
---
<!-- trie:section symbol=trie/mcp_server:TrieTools fingerprint=82ad089b92777a54080520235c2168707d9275ffb240d796d4f83f6ed50556e2 body_fp=405405e76dfa599a38848cb22c6f2f455b08ba1625712f2255e0469c03b3b4ae -->
## `TrieTools`

Encapsulates the four MCP tool methods and owns a `Store` for the server process lifetime.

- `project_root`: resolved against config to locate triefacts and the graph DB.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.close fingerprint=51581d83ec8f7571f9518e69587e72415b3fd4ca4abd2172e2a9129bfe37b523 body_fp=a09365eb54cb718df8c934890f15332adf67243945d0df859bc1212c55086868 -->
## `close() -> None`

Release the underlying database connection held by the Store.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.get_triefact fingerprint=b1ebefec54122caafbd40a4213e1ab568e7c869e832ae179e94f961ad30b1091 body_fp=142eac04dca0c4f23bca3b840b38fe65027d29b6d736ecc1eac276ef502d3854 -->
## `get_triefact(self, source_path: str) -> str`

Return the Markdown triefact for a source file, reading from the configured triefacts root.

- `source_path`: source-root-relative path (e.g. `src/foo.py`); `.md` paths used as-is.
- Returns a fallback notice string if no triefact file exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.find_symbol fingerprint=7c99546d8134592e8739c6c0d0ea4b5efc62e52daea8e1d1cbc1054c7928ee8c body_fp=950e1b1cc3117a984a0cbd52b388d00addb70684047abfd9eed93ddb04fb6f6f -->
## `find_symbol(self, name: str, limit: int = 50) -> list[dict[str, Any]]`

Substring-search symbol names, returning up to `limit` results with public symbols first.

- `name`: matched against the local (non-qualified) symbol name.
- Returns dicts equivalent to the `SymbolHit` dataclass fields.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.references_to fingerprint=b8b6cb10e64b87755a6fcf823b86f1d5a5b22cf8b4f14fbd7920f68daca64c69 body_fp=5b1ca13c57186652155581f5dbc96baa90de02f56cbccb0790dca95cecf23e54 -->
## `references_to(self, qualified_name: str) -> list[dict[str, Any]]`

Return symbols that reference `qualified_name` (inbound callers).

- Each result dict contains `src_qname`, `file_path`, and `confidence`.
- `tree_sitter_import`: precise, from an explicit import statement.
- `name_match`: heuristic, may over-match within a module.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:TrieTools.references_from fingerprint=0a2b9cad5c49c9ef3645daa571fbf659b8775f9a16571cbb8840b88b0e34f27d body_fp=67d1330a88e2eb8592364116e44822ae932bb90cd2a4d0aaee0dfdd3f7fec2e0 -->
## `references_from(self, qualified_name: str) -> list[dict[str, Any]]`

Return outbound references from `qualified_name` as a list of `{target_qname, confidence}` dicts.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:build_server fingerprint=5e5f0be4c38fc9f110dab2765fd20ce2ec2f1133cfd85d518d2a8dc5f861964d body_fp=e8606178b4e9c3368191f11b2c479173fdc0d19cf93377f82fb5473a16f8946a -->
## `build_server(project_root: Path) -> tuple[FastMCP, TrieTools]`

Construct and return an MCP server with all four trie tools registered, plus the underlying `TrieTools` instance.

- `project_root`: root directory used to locate config and the graph database.
- Returns `TrieTools` separately so tests can invoke tool methods without MCP transport.
<!-- trie:end -->

<!-- trie:section symbol=trie/mcp_server:run_stdio fingerprint=8cde71e2ff11fda4cfbc2261e1213e79ff338b8961e2ab7b957cf8c864ef91a9 body_fp=1873f72dc22eb05e0d99b565fc9f6296c757e6e459bb0616caa40255b512232c -->
## `run_stdio(project_root: Path) -> None`

Build and run the MCP server over stdio, blocking until the parent closes the pipe.
<!-- trie:end -->