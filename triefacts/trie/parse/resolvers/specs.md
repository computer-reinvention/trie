---
trie_version: 0.1.9
source: trie/parse/resolvers/specs.py
file_fingerprint: 2b7232135e3f6a8040144b88b594e4b9523e4feee6a494195a8592f660e609a1
last_synced_at: '2026-07-29T00:06:11Z'
description: "Per-language LSP server specs \u2014 the one place a new language is\
  \ registered."
defines:
- kind: module
  qualified_name: trie/parse/resolvers/specs:__module__
  lines: 1-292
- kind: function
  qualified_name: trie/parse/resolvers/specs:_python_call_sites
  lines: 18-23
- kind: function
  qualified_name: trie/parse/resolvers/specs:_typescript_call_sites
  lines: 26-37
- kind: function
  qualified_name: trie/parse/resolvers/specs:_walk_attribute_calls
  lines: 40-56
- kind: function
  qualified_name: trie/parse/resolvers/specs:_walk_member_calls
  lines: 59-75
- kind: function
  qualified_name: trie/parse/resolvers/specs:_go_call_sites
  lines: 78-98
- kind: function
  qualified_name: trie/parse/resolvers/specs:_rust_call_sites
  lines: 101-121
- kind: function
  qualified_name: trie/parse/resolvers/specs:_c_call_sites
  lines: 124-149
- kind: function
  qualified_name: trie/parse/resolvers/specs:_lua_call_sites
  lines: 152-176
- kind: constant
  qualified_name: trie/parse/resolvers/specs:PYRIGHT_SPEC
  lines: 179-184
- kind: constant
  qualified_name: trie/parse/resolvers/specs:BASEDPYRIGHT_SPEC
  lines: 186-191
- kind: constant
  qualified_name: trie/parse/resolvers/specs:TYPESCRIPT_SPEC
  lines: 193-198
- kind: function
  qualified_name: trie/parse/resolvers/specs:python_spec
  lines: 201-209
- kind: function
  qualified_name: trie/parse/resolvers/specs:typescript_spec
  lines: 212-214
- kind: constant
  qualified_name: trie/parse/resolvers/specs:GO_SPEC
  lines: 220-227
- kind: constant
  qualified_name: trie/parse/resolvers/specs:RUST_SPEC
  lines: 229-236
- kind: constant
  qualified_name: trie/parse/resolvers/specs:C_SPEC
  lines: 238-245
- kind: constant
  qualified_name: trie/parse/resolvers/specs:LUA_SPEC
  lines: 247-254
- kind: function
  qualified_name: trie/parse/resolvers/specs:go_spec
  lines: 257-259
- kind: function
  qualified_name: trie/parse/resolvers/specs:rust_spec
  lines: 262-264
- kind: function
  qualified_name: trie/parse/resolvers/specs:c_spec
  lines: 267-269
- kind: function
  qualified_name: trie/parse/resolvers/specs:lua_spec
  lines: 272-274
- kind: constant
  qualified_name: trie/parse/resolvers/specs:__all__
  lines: 277-291
incoming_refs: 5
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/resolvers/specs:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9af97eb90c31e8b7bcbcaf6033061f919c64c365ddef2549f32f007b4f796153 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
Register per-language `LspServerSpec` instances binding LSP server commands, language IDs, and tree-sitter call-site extractors for Python and TypeScript.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_python_call_sites fingerprint=ed0551b2e658fd519428649b97642b6dcf0e161ec33abf9df7db6b9f7f3ce5ca body_fp=c0e9d27f14ff4876588cd02de5db59152cd73c6e87ac9a5fd020640f2c0ce342 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
Parse `source` and return 0-based `(line, col)` positions for every `<expr>.<attr>(...)` attribute call in Python source.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_typescript_call_sites fingerprint=2b489fe744dae9005bd87ea7bd0aee99dcd50b873fe6495519e2d690c66f00ad body_fp=e0d39b1fd0c9ec2921d9c8c1b9bdd80516dfa1a8fdacda1cd1681711007b85e7 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
Parse `source` bytes as TypeScript and return 0-based `(line, col)` positions for each `<expr>.<member>(...)` call site.

- `source`: raw TypeScript or TSX file bytes; TSX parses acceptably via the `.ts` grammar.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_walk_attribute_calls fingerprint=60d8023f0ddc6f3927f15eeec95a64c4e4db1bc7238dca78c80865eb79b8702f body_fp=2b1c2e2f3801cecb4957907216bae34bcee8a02861d5c65cd2210257615432cd source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
Recursively walk a Python tree-sitter AST from `root`, returning 0-based `(line, col)` positions for each attribute-call site's method name node.

- Skips `comment` and `string` nodes entirely, avoiding false positives.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_walk_member_calls fingerprint=57f338f9c603ed8a7d93ec38b409442f145684f23105ed478da8cfae626beab5 body_fp=627b658a0419d09906e08ad3e1ccecb0eec858b0297c81555e1947c4e04d5b7a source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
Walk a tree-sitter node tree and return 0-based `(line, col)` positions of each `<expr>.<member>(...)` call expression's property identifier, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_go_call_sites fingerprint=73d8f2d256e6b4e48cac53c4625a8566bdf2673047293c780071ace437bcfee9 body_fp=1462b95ec80fa887475143883c6340309b4b15c6b2d6992412fd256d1f68f65d source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
Walk a Go source file's tree-sitter AST and return the 0-based `(line, col)` position of each selector field in `x.Method(...)` call expressions, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_rust_call_sites fingerprint=3003e44cdd652a788965c1090d3dd310c26de169400d6e0131b66292c3ee66e7 body_fp=d7031f78b3d9404d7e981d4314e281ad6fcbc14bfe58991ecf4c40c68bf92a25 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
Parse `source` bytes as Rust and return 0-based `(line, col)` positions for each `x.method(...)` field-expression call site, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_c_call_sites fingerprint=19ed181f854bcd63beb168f00b3df96bbc573b348ce2c6bc07ac994e3c03d9cb body_fp=2862ed1235815d0f9d0456dc27cf021fc68ffe448b88eab5efd3bf3680141e34 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
Parse `source` and return 0-based `(line, col)` positions of each `p->field(...)` or `s.field(...)` member call expression in C, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_lua_call_sites fingerprint=8226c453d01e0a6bbb1b96dc77bf98b79321d413d73c776f9ba2380e023d9abc body_fp=b30b363597bccf334f7d4a0e87b5f69dfad0eb08492a7cc8fe599cf5ffdfb49f source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
Return 0-based `(line, col)` positions of each `t.m(...)` or `t:m(...)` member call site in Lua source bytes.

- Skips `comment` and `string` nodes during traversal.
- Resolves the key from `field` or `method` fields, falling back to the last named child.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:PYRIGHT_SPEC fingerprint=64c179d60673d1a217ee40d88c2a7cdff5aaf8c7767aeb8034ddc9cab062872a body_fp=5fb3511475536d547ff5b5c62e96a62188eb61617186af2255750dd0f99cdfb5 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
`LspServerSpec` for the `pyright` language server, invoking `pyright-langserver --stdio` with `language_id="python"` and `_python_call_sites` as the call-site extractor.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:BASEDPYRIGHT_SPEC fingerprint=3c0988052743d28e15f4f8d85b38bea2acb442664078a0444fcce008b93a2fef body_fp=71eba07d9e33cad7d8331f77fbd5e4e464978bc7991535892e137b68d28b9d3c source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
`LspServerSpec` for the `basedpyright-langserver` stdio server, bound to the `python` language ID and `_python_call_sites`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:TYPESCRIPT_SPEC fingerprint=65688ad05eeb5ac12e73421a1a2b9098ebb9adab2f5b723508651e90d07fbc7c body_fp=e8992dbb3070623c2c25e91c2ee2843812be0028c5a384ceb0c6be1d6cdf4909 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
`LspServerSpec` binding `typescript-language-server --stdio` to the `typescript` language ID with `_typescript_call_sites` as the call-site extractor.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:python_spec fingerprint=ccb481b5782c566c817aa06afefd8da59c2605e2075b80444545b9b12612a8f1 body_fp=f7978cfbcc58b3a62f37575d695a0e2b6e045504c1e5bea503b34306c4ec45ef source_ref=c7ac435e9b947e60b7f6b8e2bf0cdb6fb6ab1858 role=config -->
Return the first available Python `LspServerSpec`, preferring `BASEDPYRIGHT_SPEC` over `PYRIGHT_SPEC`, or `None` if neither is installed.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:typescript_spec fingerprint=ff137e937219d700b573d5f9e0eb6e5646e82791e53a4fe8bb6840d488796656 body_fp=d017b217b7378e420d4284c300e9aad445e5c0f57a2107cd65e48d341505ae38 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
Return `TYPESCRIPT_SPEC` if the typescript-language-server binary is on PATH, otherwise `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:GO_SPEC fingerprint=1dd64ee24dc95e0e32bb0f9143c16085b749f7148364b97d217df6f3169f3c05 body_fp=7372c75ba5f45191e9fe0a0145d3dd3750105e55923066eb1ed0bdad89cfa356 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
`LspServerSpec` for Go, binding `gopls` (stdio) to the Go call-site walker with a 30 s init timeout and 2 s warmup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:RUST_SPEC fingerprint=c868902fde33ea5a2abc26421b2666ae54cc7218310adb65749fd640c00a4619 body_fp=65959935a1fef4dc14b15d6339d35c4680665545946071105a4705b04387e74d source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
`LspServerSpec` for `rust-analyzer` over stdio, with a 60 s init timeout and 3 s warmup before queries.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:C_SPEC fingerprint=c351b8287ea7087b15fb95000095aff6ebf6bd2f86d970f36bd36b714ac8ba48 body_fp=0cdfafd77bf80dc0794017a46cd02841a27d9349d7f25067498f8fa339675b9a source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
`LspServerSpec` constant binding clangd to the C language with a 30 s init timeout and 1.5 s warmup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:LUA_SPEC fingerprint=716ad57f5415b16c9bb8e3419ce7afa41c95ee55067e7e1d3a711394a9e39d60 body_fp=3abbbd1ca31be6d6b22dd316a8e57d5190d92d327f761b9ab4ea734acaeb02b8 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
`LspServerSpec` for Lua, binding `lua-language-server` over stdio with a 30 s init timeout and 1.5 s warmup.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:go_spec fingerprint=4814218a1652fd1e9e1124eb16b30c53af06d674659f819b183a85d17aae4eec body_fp=2928bfc587666a820f28bf83a54b9f151d5e478a27d8a70fe25923bb76463e15 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
Return `GO_SPEC` if `gopls` is found on PATH, otherwise `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:rust_spec fingerprint=df89aab21b9e311cb8b7d91f2a223de11b7bbb16cd636303478e4bda57bcf66d body_fp=272eebad8c80638b9ace482cbec36a28dd1771423216c0bfb6d61d8774ce296c source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
Return `RUST_SPEC` if `rust-analyzer` is on PATH, otherwise `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:c_spec fingerprint=afcb8e4942bc1452b52adb0457dc8c2d803c0278e555905464148f818398d556 body_fp=d6dc969b312ec95165cee62b2825fb18a1c2812641414b1bea5958d94a32b7ed source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
Return `C_SPEC` if clangd is found on PATH, otherwise return `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:lua_spec fingerprint=60e2741932327fb8f5e7b958dcc04480ececf370e91e68219e18604e678e878b body_fp=9f68ab4d8d194bfada77e5e2099a9108caf5738ec059748c88336f60a99c2c0d source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
Return `LUA_SPEC` if `lua-language-server` is found on PATH, otherwise return `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:__all__ fingerprint=f53857724770928045816ca885659b9eee3fbcb5ae9ad3416c6798b4c62a8bbc body_fp=8e54c74561709c785982da0a8ddb51cf7d70597846c6e0b3e030f4add3866dcc source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=config -->
Declares the public API of this module: all per-language `LspServerSpec` constants and their availability-checking accessor functions.
<!-- trie:end -->