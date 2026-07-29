---
trie_version: 0.1.9
source: trie/parse/lua.py
file_fingerprint: 9a999370667cbb231e429691045ba7a000238964ca05ef572ce405fd3cdf77f0
last_synced_at: '2026-07-29T00:06:20Z'
description: "Lua language backend \u2014 tree-sitter symbols + references, paired\
  \ with lua-language-server."
defines:
- kind: module
  qualified_name: trie/parse/lua:__module__
  lines: 1-340
- kind: constant
  qualified_name: trie/parse/lua:LUA_LANGUAGE
  lines: 28-28
- kind: function
  qualified_name: trie/parse/lua:_make_parser
  lines: 31-34
- kind: function
  qualified_name: trie/parse/lua:_node_text
  lines: 37-38
- kind: function
  qualified_name: trie/parse/lua:_hash
  lines: 41-42
- kind: function
  qualified_name: trie/parse/lua:_module_key
  lines: 45-47
- kind: function
  qualified_name: trie/parse/lua:_func_name
  lines: 50-72
- kind: function
  qualified_name: trie/parse/lua:_is_local
  lines: 75-81
- kind: function
  qualified_name: trie/parse/lua:_make_symbol
  lines: 84-117
- kind: function
  qualified_name: trie/parse/lua:_assignment_names
  lines: 120-132
- kind: function
  qualified_name: trie/parse/lua:extract_symbols
  lines: 135-185
- kind: function
  qualified_name: trie/parse/lua:_find_node_for_symbol
  lines: 188-206
- kind: function
  qualified_name: trie/parse/lua:_collect_call_names
  lines: 209-233
- kind: function
  qualified_name: trie/parse/lua:extract_file_data
  lines: 236-267
- kind: constant
  qualified_name: trie/parse/lua:LUA_SYSTEM_PROMPT
  lines: 270-279
- kind: class
  qualified_name: trie/parse/lua:LuaBackend
  lines: 282-336
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.__init__
  lines: 288-290
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.extract_file_data
  lines: 292-312
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.extract_symbols
  lines: 314-315
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.source_suffix
  lines: 317-318
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.system_prompt
  lines: 320-321
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.resolver
  lines: 323-336
- kind: constant
  qualified_name: trie/parse/lua:__all__
  lines: 339-339
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/lua:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1a4d1f32db0b78db1601e82b5f67baba1dc9d3d0c8217bf5322a00be127e64c9 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Lua language backend: parses `.lua` files with tree-sitter, extracts `function`, `method`, and `constant` symbols, and resolves intra-file call references optionally augmented by lua-language-server via `LspResolver`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LUA_LANGUAGE fingerprint=0b24a9b8d99133cfa39f3ec24c95bd2340db5fdd4b81578b10bb10023315270d body_fp=3df5de2b4afa1731d2e05630dde1b05eaea63448b2f722d8230509cc452feae9 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=config -->
Module-level `tree_sitter.Language` instance initialised from the bundled `tree_sitter_lua` grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_make_parser fingerprint=b4cacde80f994b493c9875c0866c417d7d2d4f6f2730b2b4d0823250cacbbf10 body_fp=9cda107cbbd0020b98a6b4952b6639355608ae0e99f7db8eec2a64fd123869c7 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
Construct and return a `Parser` instance configured with `LUA_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=4456e126d229197868b923da30c01984a6c98aa3a6236a84aa4e74c57880b918 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
Decode the byte slice of `source` spanned by `node` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=4d6c535ddd567d3e1fea8feeb45a70dc232492d2f3105352d59a2cda51262480 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=b08ed32839d7dbb1e0e61faaeb407dfef8096642c1da41c35cf59291d8eaf0a8 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
Return the module key string for a file by stripping its suffix from its path relative to `source_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_func_name fingerprint=9c1ae5c91682a35b83ba28c0fb7f0ff3e94b9849b07b60ad665af9610d2933f9 body_fp=3eeb45ea2701efcbd30d563f568394f0161890b86ec48ff6ae75c98833a55a80 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Extract `(parent, name)` from a tree-sitter `function_declaration` node's name expression.

- Returns `(None, name)` for plain `function foo()` forms.
- Returns `("Table", "name")` for dot- or colon-indexed forms; nested tables like `A.B` become the parent string.
- Returns `(None, None)` if no recognisable name node is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_is_local fingerprint=6798b0371fa5b42ba5ba3df3eb4a6c94acf8416c9e4938b163fff29a2e464940 body_fp=b5e7aabbf0989175946a398c85c73f5b1e6877c1b426e543aa3d78016f1cddb0 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Return `True` if the tree-sitter `node` begins with a `local` keyword, checking child type then raw token text as fallback.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_make_symbol fingerprint=4110f9a2c33def602275e4da1c1158152072ce5044ca6be96f8ca4d9ac4746eb body_fp=526fe847a7f380fc66a2d41a4c73c15ce557460c6fdfc533039bc89324c90769 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Construct a `Symbol` from a tree-sitter `Node`, extracting signature, body text, hashes, and line numbers.

- `module_key`: module-relative path string used as the qualified-name prefix.
- `parent`: dotted table name; combined with `name` as `parent.name` in `qualified_name`.
- `docstring`: always `None` (Lua has no docstring convention surfaced here).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_assignment_names fingerprint=a4d19e9a5014b6b9548a0512c281626448992cbf683b4685c8843830048d61a6 body_fp=e5abed015998ae7fdc0480fea738a14ef46438c6e8f128ed05982be22de9a305 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Extract plain identifier names from the left-hand side of a top-level assignment node, ignoring non-identifier targets.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:extract_symbols fingerprint=b211ed75667a5a2912c9c8f0a5b10d8cc301f692536a8b15c3a4e78a133d7b57 body_fp=90e971b40aecd912502e1e19a84de18b10e7d782c3b207e2f2807d85b0dcd618 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Parse a Lua file and return top-level `Symbol` objects for functions, methods, and constants.

- `source_text`: if provided, used instead of reading `file_path` from disk.
- `source_root`: defaults to `file_path.parent`; used to compute module key and relative path.
- Local bindings (`local function` / `local var`) are emitted with `is_public=False`.
- Only top-level nodes are visited; nested declarations are ignored.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_find_node_for_symbol fingerprint=4d7b031231592a6c0678c6a0b659aee94aff2f7d59bca837c43ca7abb2327de9 body_fp=657ee9b29099d616067b27378945bd0b9f61fc2bfaf91655d904d4ebd562ed91 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Walk `root` depth-first and return the first declaration node whose start line matches `sym.start_line`, or `None` if not found.

- `root`: tree-sitter root node to search within.
- Matches node types `function_declaration`, `variable_declaration`, `assignment_statement` only.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_collect_call_names fingerprint=b84359637873df036d2668d5b8e6595399e9cbba744f76e495e8435d879cce8d body_fp=ce319600294c64ccb75742cc8d9c6b93d9ffd615c5ef68a9004f5101e2c2c8da source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Walk a tree-sitter `Node` subtree and collect all callee names found in call expressions.

- For `foo()`, adds `"foo"`; for `t.m()` or `t:m()`, adds only the field/method name `"m"`.
- Skips `comment` and `string` nodes to avoid false positives.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:extract_file_data fingerprint=9d46e838d84e0b3bec09e1c0d4ec9a474a40bf95ba79e310f9a8934029a7e46d body_fp=a2f0bae87ffc4f3b59e9d3d6ac4c2acc4315154f2e7a48fd699f9be14fe0b4f4 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Parse a Lua file and return all top-level symbols plus intra-file `"calls"` references between them.

- `source_root`: used to compute module keys and relative paths; defaults to `file_path.parent`.
- References are only emitted between top-level, non-dotted symbols within the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LUA_SYSTEM_PROMPT fingerprint=1002df489a859eb1c6305de618592432057133dfcacdd1939a1afc251a7c49f9 body_fp=986e875fa5ba2ca959916877b661dc6e0ae993a121e20d220565aece57a9e629 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=config -->
System prompt string passed to the LLM when generating documentation for Lua symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend fingerprint=583324e1e2b983709cf589a7a9c552ee47860463be301bb2f90dfc48f1809dd0 body_fp=cdcf7e9d5d2667d3acc5b6417e1db5aa97ebdf7654513fe7460c13c773e45711 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
Implements the `LanguageBackend` interface for Lua, using tree-sitter for symbol/reference extraction and an optional `LspResolver` (lua-language-server) for cross-file reference enrichment.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is passed; merges LSP references when a resolver is available.
- `resolver()`: lazily constructs an `LspResolver` on first call; returns `None` if `TRIE_DISABLE_RESOLVER=1` or no `lua_spec`.
- `extensions`: only `.lua` files are matched.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=10960a92aa6aee4c5e71ef2dac19c88f0ad236819ede1db7df5927ba05536626 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
Initialize `LuaBackend` with a null, unbuilt resolver cache.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=c61c6e689b6e0685a422b7f7be9bcbffcf3903391fc8fb4f0e8e2509463b8691 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
Extract `FileData` for a Lua file, merging LSP-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if provided.
- Returns base `FileData` unchanged when no resolver is configured or resolver yields no extra references.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=7b85843a84b226d24982f70b2c4d59df9aeb653d23075dae71a89a3f45b42308 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
Delegates `LuaBackend` symbol extraction to the module-level `extract_symbols` function unchanged.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.source_suffix fingerprint=9247e5ed349c5986d033adf17ff9406b815485298768507d5b9267e97548e400 body_fp=8bf452fa8614d1712549e84aa3387dc1f86a8ffa1ab21a351d3ea922c9a83205 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
Returns the `LuaBackend` file extension string `".lua"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.system_prompt fingerprint=10f4648668162b8a0b25280f32e0c9c94a05fe2012b039dcf3f79d2399273b29 body_fp=43b1a4970f3c26d063bdd21837e15c25ffe800278a7f97fb52d5d74ce4756714 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
Returns the `LUA_SYSTEM_PROMPT` string used to guide LLM documentation of Lua symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.resolver fingerprint=4bbb0c9e1a63cf18afe56839967d6c5974076deab2dc7fc20ef7b4c0efb23bd7 body_fp=c5216ac214394b2f4cf6e977a819bc1bc626e5f885257f55238b0b89eb0e19d7 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
Return the lazily-initialised `LspResolver` for `LuaBackend`, constructing it once from `lua_spec()` or setting it to `None` if unavailable or `TRIE_DISABLE_RESOLVER=1`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:__all__ fingerprint=275163d2fd179a0f2e0c1ac2f499ba137dfffb1f6cfaa68e4f2aec265a9f2c77 body_fp=a4b20fffa943a8984da8f2299c9d31c26098b081875c8ccb7d3fcc25e5052033 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=model -->
Declares the public API surface of the `trie.parse.lua` module.
<!-- trie:end -->