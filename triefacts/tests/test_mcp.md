---
trie_version: 0.1.0
source: tests/test_mcp.py
file_fingerprint: c2dc66ce59c0927094fed1ef064a51c0f347aa330fc7690a3a6ac28265b9425b
last_synced_at: '2026-05-12T18:24:26Z'
description: Tests for the MCP tool functions.
defines:
- kind: class
  qualified_name: tests/test_mcp:FakeClient
  lines: 23-37
- kind: method
  qualified_name: tests/test_mcp:FakeClient.generate
  lines: 27-34
- kind: method
  qualified_name: tests/test_mcp:FakeClient.count_tokens
  lines: 36-37
- kind: function
  qualified_name: tests/test_mcp:project
  lines: 41-60
- kind: function
  qualified_name: tests/test_mcp:populated_project
  lines: 64-83
- kind: function
  qualified_name: tests/test_mcp:tools
  lines: 87-90
- kind: function
  qualified_name: tests/test_mcp:test_get_triefact_returns_markdown_for_source_path
  lines: 96-99
- kind: function
  qualified_name: tests/test_mcp:test_get_triefact_accepts_md_path
  lines: 102-104
- kind: function
  qualified_name: tests/test_mcp:test_get_triefact_returns_notice_when_missing
  lines: 107-110
- kind: function
  qualified_name: tests/test_mcp:test_find_symbol_substring_match
  lines: 116-119
- kind: function
  qualified_name: tests/test_mcp:test_find_symbol_returns_metadata
  lines: 122-131
- kind: function
  qualified_name: tests/test_mcp:test_find_symbol_empty_query_returns_some
  lines: 134-137
- kind: function
  qualified_name: tests/test_mcp:test_find_symbol_limit_respected
  lines: 140-142
- kind: function
  qualified_name: tests/test_mcp:test_find_symbol_unknown_returns_empty
  lines: 145-147
- kind: function
  qualified_name: tests/test_mcp:test_references_to_finds_callers
  lines: 153-158
- kind: function
  qualified_name: tests/test_mcp:test_references_from_finds_callees
  lines: 161-164
- kind: function
  qualified_name: tests/test_mcp:test_references_to_for_unreferenced_symbol
  lines: 167-170
- kind: function
  qualified_name: tests/test_mcp:test_references_to_unknown_symbol
  lines: 173-175
- kind: function
  qualified_name: tests/test_mcp:test_build_server_registers_tools
  lines: 181-192
incoming_refs: 0
outgoing_refs: 7
---
<!-- trie:section symbol=tests/test_mcp:FakeClient fingerprint=c5476e52a6a55daf0b623214d0e84b360c5efd846938481fa23201c0ec24342c body_fp=f3ef0b2f0885b0ca5ab95702300ad3d0c8ccbca0d30109f11cc8fae908d51483 -->
## `FakeClient(model_id: str = "fake/test", body: str = "## generated\n\nbody.")`

Stub LLM client returning fixed text and token counts for use in tests.

- `body`: the exact string returned as `GenerationResponse.text`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.generate fingerprint=a28c91031810d416f079e2d7a57f5ed7651bd8c3315cf78d1ec869c3b812915e body_fp=6c05839a3be9b42c773ceae30eda0723c643bae684ce39b2efdd88622b38f8df -->
## `generate(_req: GenerationRequest) -> GenerationResponse`

Return a fixed `GenerationResponse` with the configured `body` text and hardcoded token counts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:FakeClient.count_tokens fingerprint=d2e54258807160cae2cd3e384f807ff7ab8c686f8c79830c0798dd9ba6b1e027 body_fp=c1b5694654ec914ab0f207bbecb7aba3b466d7b1a264442dcc735b57672ca2f0 -->
## `count_tokens(self, _req: GenerationRequest) -> int`

Return a fixed token count of 100.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:project fingerprint=6ba28be719fa59a185e04227a44558c52564297d699fb743848ee2785d2583fc body_fp=344bb2777e61d220643bee70f46e9c06803dd0a4eebc90b117283a2c1bb5cb7c -->
## `project(tmp_path: Path) -> Path`

Pytest fixture that creates a minimal two-file Python project with a `trie.toml` config in a temporary directory.

- **returns** `tmp_path` populated with `trie.toml`, `lib.py`, and `app.py`
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:populated_project fingerprint=82473bb3733399e205e3ab32e5bcc5aa4f3de4190ac96e0f17b611053c8ecc14 body_fp=84b18d860b6386ab4760feba29cb3bd102dc5c67a7907586f647cad98e0e7ee5 -->
## `populated_project(project: Path) -> Path`

Fixture that runs scan and sync on the project so MCP tools have queryable data.

- Returns the same `project` path after populating the graph DB and writing triefacts for `lib.py` and `app.py`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:tools fingerprint=b89f3ca1611ed5226f820d82ffc6f4d3db27942f64390976744c1fbf0d5e67de body_fp=dd934eae976ba2aa8e47cc89714633329acb5ae2dcd277fd50c9ff2b733b348d -->
## `tools(populated_project: Path)`

Yield a `TrieTools` instance bound to `populated_project`, closing it after the test.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_get_triefact_returns_markdown_for_source_path fingerprint=25cf8dce0c445a84c0a566a827bc8229f03f81f512fffb6a4225af4f3cbcff43 body_fp=3a6932e85f214408d1773a71175bde6cc4e35c02f0a6629645cffbb996a60550 -->
## `test_get_triefact_returns_markdown_for_source_path(tools: TrieTools)`

Assert that `get_triefact` returns the generated Markdown content when given a source file path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_get_triefact_accepts_md_path fingerprint=eb40ac58066a7744a0e776d93273ff16bdafa7350d5a4e5cea2be43f24094822 body_fp=583ca35e5f2525ee29d5569de21f6f856757c6c112b8ea9942fd2622a3831369 -->
## `test_get_triefact_accepts_md_path(tools: TrieTools)`

Assert that `get_triefact` resolves a `.md` path to the same triefact as its source counterpart.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_get_triefact_returns_notice_when_missing fingerprint=aa92137147d59c38764692dacbc80927f3a3bf72daf19ea14220a7752decf962 body_fp=03ac0fa8642d11a13b5782358b03317c909f9745ab3257ddf097b5dde9fab12f -->
## `test_get_triefact_returns_notice_when_missing(tools: TrieTools)`

Assert that `get_triefact` returns a guidance message containing "No trie triefact" and "trie sync" for an unknown path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_find_symbol_substring_match fingerprint=2c94ddd3cad68d6a81b2cf391ba1a8f486385aa5d75de5373656c5b19a892027 body_fp=a0a145ca28f0ebfefb6e18cd33c5065a90f0f9897721874a12901312bce0ace8 -->
## `test_find_symbol_substring_match(tools: TrieTools)`

Assert that `find_symbol` returns results containing `"lib:slugify"` when queried with a partial name substring.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_find_symbol_returns_metadata fingerprint=0b65397a21cce2924cc3216d9cd587db2b87a3000f3041019e6f8d18abec8381 body_fp=d47dd80d6d24e8cea7f0d0c8d3c9974d21286c9ab6d98db88fcd82744b206dbf -->
## `test_find_symbol_returns_metadata(tools: TrieTools)`

Assert that `find_symbol` returns a fully-populated metadata dict for an exact symbol name match.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_find_symbol_empty_query_returns_some fingerprint=4e52d184486a16a79ee2a426bfa2556a00937c77b0a38d61454e74c84d8a6d74 body_fp=108ab41699e77b0399e202b37801b6eea2265d74688e647957adcf4be099982b -->
## `test_find_symbol_empty_query_returns_some(tools: TrieTools)`

Assert that an empty query string matches all symbols, returning at least `slugify` and `make_url`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_find_symbol_limit_respected fingerprint=15cc7517289b5919841fc7c1ad475c07bfb3651120808f2afd58267474c7d366 body_fp=6bc0517afe1e3eb55757ee8032e8be8bd7825132a2c975fcd39516866e49d33b -->
## `test_find_symbol_limit_respected(tools: TrieTools)`

Assert that `find_symbol` returns no more results than the specified `limit`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_find_symbol_unknown_returns_empty fingerprint=3c63d7cd9f50a93358c57fec4ea69552ae027808ad3a372f904baf4a26cf3d83 body_fp=4372a0f6470b9933846082a6f2955ce0e490d76fc6803d657bc7969f5a4afdff -->
## `test_find_symbol_unknown_returns_empty(tools: TrieTools)`

Assert that querying a nonexistent symbol name returns an empty list.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_references_to_finds_callers fingerprint=11d005714f7aefb14db7cce6483aec4f16820c2214384658e1410236efdf89a6 body_fp=141cdbb09b8f2a668903de8be4e0778e97093065736a6decb843390b27ea551e -->
## `test_references_to_finds_callers(tools: TrieTools)`

Assert that `references_to` identifies `app:make_url` as a caller of `lib:slugify` with correct confidence and file path.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_references_from_finds_callees fingerprint=307986cb620dced8b6bea075ce9ce38dc85d2d12b47b7cfd6223edf94de7745e body_fp=3d8cf99c3aac14cec8778d601fde4e9ea69f4b53122a725aa4bda2c3c7812ae5 -->
## `test_references_from_finds_callees(tools: TrieTools)`

Assert that `references_from` returns outbound edges, including `lib:slugify` as a callee of `app:make_url`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_references_to_for_unreferenced_symbol fingerprint=471fac06a9b271e1e6bf99721be20792d93e4551d54915768d27de57ad3b333b body_fp=c3574a8585553d6d903e450150b0ea61272ae7d547e5053d8ea686735ddf4c44 -->
## `test_references_to_for_unreferenced_symbol(tools: TrieTools)`

Assert `references_to` returns an empty list for a symbol with no callers.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_references_to_unknown_symbol fingerprint=0856fa92cd1fa60f5bb5ea2239be55affdef76d90a5c7f3899f67e761a0f5111 body_fp=718331ae026cb822300ee195458f3c7bc6e4cda2048058f5b567f636af1f3bc3 -->
## `test_references_to_unknown_symbol(tools: TrieTools)`

Assert that `references_to` returns an empty list for a non-existent qualified name.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_mcp:test_build_server_registers_tools fingerprint=acf70fe13e5f0a2e29477425879cf66e798fb804f00ef9fd5efb06bade1dcefa body_fp=c568fb44d003d31e988082f4379f59b4b0af72f17393524c4a5889a401573e56 -->
## `test_build_server_registers_tools(populated_project: Path)`

Verify `build_server` registers exactly the four expected tool names with FastMCP's tool manager.
<!-- trie:end -->