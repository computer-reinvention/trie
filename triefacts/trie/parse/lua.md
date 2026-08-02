---
trie_version: 0.3.0
source: trie/parse/lua.py
file_fingerprint: 9a999370667cbb231e429691045ba7a000238964ca05ef572ce405fd3cdf77f0
last_synced_at: '2026-08-02T21:19:38Z'
description: "Lua language backend \u2014 tree-sitter symbols + references, paired with lua-language-server."
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
  signature: def _make_parser() -> Parser
- kind: function
  qualified_name: trie/parse/lua:_node_text
  lines: 37-38
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/lua:_hash
  lines: 41-42
  signature: 'def _hash(s: str) -> str'
- kind: function
  qualified_name: trie/parse/lua:_module_key
  lines: 45-47
  signature: 'def _module_key(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/lua:_func_name
  lines: 50-72
  signature: 'def _func_name(fn_node: Node, source: bytes) -> tuple[str | None, str | None]'
- kind: function
  qualified_name: trie/parse/lua:_is_local
  lines: 75-81
  signature: 'def _is_local(node: Node, source: bytes) -> bool'
- kind: function
  qualified_name: trie/parse/lua:_make_symbol
  lines: 84-117
  signature: 'def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, is_public: bool = True, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/lua:_assignment_names
  lines: 120-132
  signature: 'def _assignment_names(node: Node, source: bytes) -> list[str]'
- kind: function
  qualified_name: trie/parse/lua:extract_symbols
  lines: 135-185
  signature: 'def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/lua:_find_node_for_symbol
  lines: 188-206
  signature: 'def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None'
- kind: function
  qualified_name: trie/parse/lua:_collect_call_names
  lines: 209-233
  signature: 'def _collect_call_names(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/lua:extract_file_data
  lines: 236-267
  signature: 'def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData'
- kind: constant
  qualified_name: trie/parse/lua:LUA_SYSTEM_PROMPT
  lines: 270-279
- kind: class
  qualified_name: trie/parse/lua:LuaBackend
  lines: 282-336
  signature: class LuaBackend
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.__init__
  lines: 288-290
  signature: def __init__(self) -> None
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.extract_file_data
  lines: 292-312
  signature: def extract_file_data(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.extract_symbols
  lines: 314-315
  signature: def extract_symbols(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.source_suffix
  lines: 317-318
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.system_prompt
  lines: 320-321
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/lua:LuaBackend.resolver
  lines: 323-336
  signature: def resolver(self)
- kind: constant
  qualified_name: trie/parse/lua:__all__
  lines: 339-339
incoming_refs: 15
outgoing_refs: 13
---
<!-- trie:section symbol=trie/parse/lua:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=1a4d1f32db0b78db1601e82b5f67baba1dc9d3d0c8217bf5322a00be127e64c9 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
Lua language backend: parses `.lua` files with tree-sitter, extracts `function`, `method`, and `constant` symbols, and resolves intra-file call references optionally augmented by lua-language-server via `LspResolver`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LUA_LANGUAGE fingerprint=0b24a9b8d99133cfa39f3ec24c95bd2340db5fdd4b81578b10bb10023315270d body_fp=3df5de2b4afa1731d2e05630dde1b05eaea63448b2f722d8230509cc452feae9 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=config -->
Module-level `tree_sitter.Language` instance initialised from the bundled `tree_sitter_lua` grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_make_parser fingerprint=b4cacde80f994b493c9875c0866c417d7d2d4f6f2730b2b4d0823250cacbbf10 body_fp=fe97f591b885fcec949d79f0b441af5b0218208869cf8b6e307c4aec10e36754 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
## `def _make_parser() -> Parser`

Construct and return a `Parser` instance configured with `LUA_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=4faa7e80c6ae3aa156c18b4b9b9947dce11f95c41d271b6b752b3dd6d23059ae source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the byte slice of `source` spanned by `node` into a UTF-8 string, replacing invalid bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=6669477292c01bece7ef1f4345e604d994c8aba94e5f3aa365f05018167230e1 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
## `def _hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=931bbae914de0801b68e243aad6c3aec285082dffe3c74e53dcc250aef26ff16 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
## `def _module_key(file_path: Path, source_root: Path) -> str`

Return the module key string for a file by stripping its suffix from its path relative to `source_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_func_name fingerprint=9c1ae5c91682a35b83ba28c0fb7f0ff3e94b9849b07b60ad665af9610d2933f9 body_fp=dad5fe68e167bb32ccef75939221bcab4346770b331b49cd115d9c894f3ac17f source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _func_name(fn_node: Node, source: bytes) -> tuple[str | None, str | None]`

Extract `(parent, name)` from a tree-sitter `function_declaration` node's name expression.

- Returns `(None, name)` for plain `function foo()` forms.
- Returns `("Table", "name")` for dot- or colon-indexed forms; nested tables like `A.B` become the parent string.
- Returns `(None, None)` if no recognisable name node is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_is_local fingerprint=6798b0371fa5b42ba5ba3df3eb4a6c94acf8416c9e4938b163fff29a2e464940 body_fp=ef64f05e232f5fc63ff33dd17e8325ff9fb582e08bad056edf9ce2c02009adcb source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _is_local(node: Node, source: bytes) -> bool`

Return `True` if the tree-sitter `node` begins with a `local` keyword, checking child type then raw token text as fallback.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_make_symbol fingerprint=4110f9a2c33def602275e4da1c1158152072ce5044ca6be96f8ca4d9ac4746eb body_fp=4910cd13f88c75ccbad4a3d888e95f861980bf7a6f009f750b2cd50e1bada3b7 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, is_public: bool = True, ) -> Symbol`

Construct a `Symbol` from a tree-sitter `Node`, extracting signature, body text, hashes, and line numbers.

- `module_key`: module-relative path string used as the qualified-name prefix.
- `parent`: dotted table name; combined with `name` as `parent.name` in `qualified_name`.
- `docstring`: always `None` (Lua has no docstring convention surfaced here).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_assignment_names fingerprint=a4d19e9a5014b6b9548a0512c281626448992cbf683b4685c8843830048d61a6 body_fp=7b2bb1a9532792b7cbc1a067af675eeb58f4216b26fa0a335f0fa696a267ad28 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _assignment_names(node: Node, source: bytes) -> list[str]`

Extract plain identifier names from the left-hand side of a top-level assignment node, ignoring non-identifier targets.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:extract_symbols fingerprint=b211ed75667a5a2912c9c8f0a5b10d8cc301f692536a8b15c3a4e78a133d7b57 body_fp=2f05f4118e488bb2b24d1c060eb6107856c82c69f99178890a54390d5dd44586 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse a Lua file and return top-level `Symbol` objects for functions, methods, and constants.

- `source_text`: if provided, used instead of reading `file_path` from disk.
- `source_root`: defaults to `file_path.parent`; used to compute module key and relative path.
- Local bindings (`local function` / `local var`) are emitted with `is_public=False`.
- Only top-level nodes are visited; nested declarations are ignored.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_find_node_for_symbol fingerprint=4d7b031231592a6c0678c6a0b659aee94aff2f7d59bca837c43ca7abb2327de9 body_fp=9149b087baff1da563001b342592a3ea174d8a421ca86a8ba98a965387dc4815 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None`

Walk `root` depth-first and return the first declaration node whose start line matches `sym.start_line`, or `None` if not found.

- `root`: tree-sitter root node to search within.
- Matches node types `function_declaration`, `variable_declaration`, `assignment_statement` only.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:_collect_call_names fingerprint=b84359637873df036d2668d5b8e6595399e9cbba744f76e495e8435d879cce8d body_fp=63c50294452dbd1c0c6d0a6f1d79598ab43a76df705d06ea00730ccf568543af source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def _collect_call_names(node: Node, source: bytes) -> set[str]`

Walk a tree-sitter `Node` subtree and collect all callee names found in call expressions.

- For `foo()`, adds `"foo"`; for `t.m()` or `t:m()`, adds only the field/method name `"m"`.
- Skips `comment` and `string` nodes to avoid false positives.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:extract_file_data fingerprint=9d46e838d84e0b3bec09e1c0d4ec9a474a40bf95ba79e310f9a8934029a7e46d body_fp=1d332e425384e5c2eee7a53c953dc92470ea4be195bc1902ca56daa542d46939 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=parsing -->
## `def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Lua file and return all top-level symbols plus intra-file `"calls"` references between them.

- `source_root`: used to compute module keys and relative paths; defaults to `file_path.parent`.
- References are only emitted between top-level, non-dotted symbols within the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LUA_SYSTEM_PROMPT fingerprint=1002df489a859eb1c6305de618592432057133dfcacdd1939a1afc251a7c49f9 body_fp=986e875fa5ba2ca959916877b661dc6e0ae993a121e20d220565aece57a9e629 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=config -->
System prompt string passed to the LLM when generating documentation for Lua symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend fingerprint=583324e1e2b983709cf589a7a9c552ee47860463be301bb2f90dfc48f1809dd0 body_fp=2741dbf720b68c8bbcd25903bdecffd55311015daaaa1093333552e2cecf12ab source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
## `class LuaBackend`

Implements the `LanguageBackend` interface for Lua, using tree-sitter for symbol/reference extraction and an optional `LspResolver` (lua-language-server) for cross-file reference enrichment.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is passed; merges LSP references when a resolver is available.
- `resolver()`: lazily constructs an `LspResolver` on first call; returns `None` if `TRIE_DISABLE_RESOLVER=1` or no `lua_spec`.
- `extensions`: only `.lua` files are matched.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=273fdcdbe99f64f0ad6ad4a78375a3519cf3a369581dc60ba1cbbbbe03cf8979 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
## `def __init__(self) -> None`

Initialize `LuaBackend` with a null, unbuilt resolver cache.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=ae7974f80b45d50c8285b2b59822bd737d1442bf2bd2358c6d9131ecf9c83135 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
## `def extract_file_data(self, file_path, source_root=None, *, source_text=None)`

Extract `FileData` for a Lua file, merging LSP-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if provided.
- Returns base `FileData` unchanged when no resolver is configured or resolver yields no extra references.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=fa2a6cece02e6c1400c916c80a4678ef8f098e5e619c7656070f3207a53fddbe source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
## `def extract_symbols(self, file_path, source_root=None, *, source_text=None)`

Delegates `LuaBackend` symbol extraction to the module-level `extract_symbols` function unchanged.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.source_suffix fingerprint=9247e5ed349c5986d033adf17ff9406b815485298768507d5b9267e97548e400 body_fp=7a802bce54808c4f645aa4940855ee24841a2afa1227eb79c09de3d559eb4856 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=util -->
## `def source_suffix(self) -> str`

Returns the `LuaBackend` file extension string `".lua"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.system_prompt fingerprint=10f4648668162b8a0b25280f32e0c9c94a05fe2012b039dcf3f79d2399273b29 body_fp=03ffd49e7f9eb52709665a358e4c303370e19b16506a8e0cab7bb1dce91ce3b8 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=api -->
## `def system_prompt(self) -> str`

Returns the `LUA_SYSTEM_PROMPT` string used to guide LLM documentation of Lua symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:LuaBackend.resolver fingerprint=4bbb0c9e1a63cf18afe56839967d6c5974076deab2dc7fc20ef7b4c0efb23bd7 body_fp=7c4c6b689f06d729473a318441f190697194ea6d674d1b7886354e7a12bb6c86 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=domain -->
## `def resolver(self)`

Return the lazily-initialised `LspResolver` for `LuaBackend`, constructing it once from `lua_spec()` or setting it to `None` if unavailable or `TRIE_DISABLE_RESOLVER=1`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/lua:__all__ fingerprint=275163d2fd179a0f2e0c1ac2f499ba137dfffb1f6cfaa68e4f2aec265a9f2c77 body_fp=a4b20fffa943a8984da8f2299c9d31c26098b081875c8ccb7d3fcc25e5052033 source_ref=d872162b61842d066e75af0b1502017e7df4041d role=model -->
Declares the public API surface of the `trie.parse.lua` module.
<!-- trie:end -->