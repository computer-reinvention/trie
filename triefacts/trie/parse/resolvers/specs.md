---
trie_version: 0.3.0
source: trie/parse/resolvers/specs.py
file_fingerprint: e0627c73baec64484adfd106641a70ed48f52c91d15db79bf3a80192807d19ce
last_synced_at: '2026-07-29T01:48:52Z'
description: "Per-language LSP server specs \u2014 the one place a new language is registered."
defines:
- kind: module
  qualified_name: trie/parse/resolvers/specs:__module__
  lines: 1-347
- kind: constant
  qualified_name: trie/parse/resolvers/specs:_ENABLED
  lines: 23-23
- kind: constant
  qualified_name: trie/parse/resolvers/specs:_DISABLED_LANGUAGES
  lines: 24-24
- kind: constant
  qualified_name: trie/parse/resolvers/specs:_SERVER_OVERRIDES
  lines: 25-25
- kind: function
  qualified_name: trie/parse/resolvers/specs:configure_resolver
  lines: 28-44
  signature: 'def configure_resolver( *, enabled: bool = True, disabled_languages: list[str] | None = None, servers: dict[str, list[str]] | None = None, ) -> None'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_apply_config
  lines: 47-54
  signature: 'def _apply_config(language: str, spec: LspServerSpec) -> LspServerSpec | None'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_python_call_sites
  lines: 57-62
  signature: 'def _python_call_sites(source: bytes) -> list[CallSite]'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_typescript_call_sites
  lines: 65-76
  signature: 'def _typescript_call_sites(source: bytes) -> list[CallSite]'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_walk_attribute_calls
  lines: 79-95
  signature: def _walk_attribute_calls(root) -> list[CallSite]
- kind: function
  qualified_name: trie/parse/resolvers/specs:_walk_member_calls
  lines: 98-114
  signature: def _walk_member_calls(root) -> list[CallSite]
- kind: function
  qualified_name: trie/parse/resolvers/specs:_go_call_sites
  lines: 117-137
  signature: 'def _go_call_sites(source: bytes) -> list[CallSite]'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_rust_call_sites
  lines: 140-160
  signature: 'def _rust_call_sites(source: bytes) -> list[CallSite]'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_c_call_sites
  lines: 163-188
  signature: 'def _c_call_sites(source: bytes) -> list[CallSite]'
- kind: function
  qualified_name: trie/parse/resolvers/specs:_lua_call_sites
  lines: 191-215
  signature: 'def _lua_call_sites(source: bytes) -> list[CallSite]'
- kind: constant
  qualified_name: trie/parse/resolvers/specs:PYRIGHT_SPEC
  lines: 218-223
- kind: constant
  qualified_name: trie/parse/resolvers/specs:BASEDPYRIGHT_SPEC
  lines: 225-230
- kind: constant
  qualified_name: trie/parse/resolvers/specs:TYPESCRIPT_SPEC
  lines: 232-237
- kind: function
  qualified_name: trie/parse/resolvers/specs:python_spec
  lines: 240-258
  signature: def python_spec() -> LspServerSpec | None
- kind: function
  qualified_name: trie/parse/resolvers/specs:typescript_spec
  lines: 261-264
  signature: def typescript_spec() -> LspServerSpec | None
- kind: constant
  qualified_name: trie/parse/resolvers/specs:GO_SPEC
  lines: 270-277
- kind: constant
  qualified_name: trie/parse/resolvers/specs:RUST_SPEC
  lines: 279-286
- kind: constant
  qualified_name: trie/parse/resolvers/specs:C_SPEC
  lines: 288-295
- kind: constant
  qualified_name: trie/parse/resolvers/specs:LUA_SPEC
  lines: 297-304
- kind: function
  qualified_name: trie/parse/resolvers/specs:go_spec
  lines: 307-310
  signature: def go_spec() -> LspServerSpec | None
- kind: function
  qualified_name: trie/parse/resolvers/specs:rust_spec
  lines: 313-316
  signature: def rust_spec() -> LspServerSpec | None
- kind: function
  qualified_name: trie/parse/resolvers/specs:c_spec
  lines: 319-322
  signature: def c_spec() -> LspServerSpec | None
- kind: function
  qualified_name: trie/parse/resolvers/specs:lua_spec
  lines: 325-328
  signature: def lua_spec() -> LspServerSpec | None
- kind: constant
  qualified_name: trie/parse/resolvers/specs:__all__
  lines: 331-346
incoming_refs: 22
outgoing_refs: 18
---
<!-- trie:section symbol=trie/parse/resolvers/specs:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=9af97eb90c31e8b7bcbcaf6033061f919c64c365ddef2549f32f007b4f796153 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
Register per-language `LspServerSpec` instances binding LSP server commands, language IDs, and tree-sitter call-site extractors for Python and TypeScript.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_ENABLED fingerprint=bc75b0349a5f890732098d9145b659cad8c080df5bd60a5da54f7a2d8a677b46 body_fp=5b06cc1da31d40e1bf01be6db2323c25a2558a9613840932f5e3385a72ca3b70 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
Process-global flag; when `False`, every `*_spec()` selector returns `None`, disabling LSP resolution entirely.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_DISABLED_LANGUAGES fingerprint=1b8cb254c23c66f920a4d07077ebe9757476cb23007af21a38f568740df5146c body_fp=867662aa6922596640a09656205eb6867f49480391b282c03ed840da6bef01cb source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
Process-global set of language names excluded from LSP resolution; populated by `configure_resolver`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_SERVER_OVERRIDES fingerprint=28d90a3086e1ed52700f340e765e0eab0c42413098ca79e38f15947c3f8dcea7 body_fp=0ba71091c9961acbb1d09a28f9572a4c1c80b286b5c8f822e8376d26c1bd2291 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
Process-global map from language name to replacement LSP server command, injected by `configure_resolver` before parsing.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:configure_resolver fingerprint=8109d45425d72179dfc7a502409179ce9725adab3be21d9672bf922666b103c0 body_fp=f3d5c159b14acad364b9fa9d3a87d0e6d87b038ea428db5c2fb1f4f28d8a9346 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def configure_resolver( *, enabled: bool = True, disabled_languages: list[str] | None = None, servers: dict[str, list[str]] | None = None, ) -> None`

Set process-global resolver configuration used by all `*_spec()` selectors.

- `enabled=False` forces every spec selector to return `None` (tree-sitter only).
- `disabled_languages`: language names whose spec selectors return `None`.
- `servers`: maps a language name to a replacement server command list.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_apply_config fingerprint=fb6156e18e459d651f3e717d5b0c4a7d029b5d675d2ecc8c8a9e3c1d7ccd950e body_fp=2a62421153db8748ec07abbb41214c31987d3dfe83f6c1dc18c2cb7ac1a9f49a source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def _apply_config(language: str, spec: LspServerSpec) -> LspServerSpec | None`

Return `None` if the language is globally or individually disabled, otherwise return the spec with its command replaced by any configured server override.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_python_call_sites fingerprint=ed0551b2e658fd519428649b97642b6dcf0e161ec33abf9df7db6b9f7f3ce5ca body_fp=78f039769931f51fab5e37419bd699d7d4ef6a4ed5d1925e6dc077f184674080 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
## `def _python_call_sites(source: bytes) -> list[CallSite]`

Parse `source` and return 0-based `(line, col)` positions for every `<expr>.<attr>(...)` attribute call in Python source.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_typescript_call_sites fingerprint=2b489fe744dae9005bd87ea7bd0aee99dcd50b873fe6495519e2d690c66f00ad body_fp=f7a9989912b9681df4f99f9fec7c5c801d39575c5b3ffe77259983372d076091 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
## `def _typescript_call_sites(source: bytes) -> list[CallSite]`

Parse `source` bytes as TypeScript and return 0-based `(line, col)` positions for each `<expr>.<member>(...)` call site.

- `source`: raw TypeScript or TSX file bytes; TSX parses acceptably via the `.ts` grammar.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_walk_attribute_calls fingerprint=60d8023f0ddc6f3927f15eeec95a64c4e4db1bc7238dca78c80865eb79b8702f body_fp=6a978b8e114525486d3448ec6d2e895af28ce87bc22a8ecaca75dc314290d754 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
## `def _walk_attribute_calls(root) -> list[CallSite]`

Recursively walk a Python tree-sitter AST from `root`, returning 0-based `(line, col)` positions for each attribute-call site's method name node.

- Skips `comment` and `string` nodes entirely, avoiding false positives.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_walk_member_calls fingerprint=57f338f9c603ed8a7d93ec38b409442f145684f23105ed478da8cfae626beab5 body_fp=5a72dca5649552f07d45bd965dd86387b5cb14eaa87840d3255099f4e555c107 source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=parsing -->
## `def _walk_member_calls(root) -> list[CallSite]`

Walk a tree-sitter node tree and return 0-based `(line, col)` positions of each `<expr>.<member>(...)` call expression's property identifier, skipping comments and strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_go_call_sites fingerprint=73d8f2d256e6b4e48cac53c4625a8566bdf2673047293c780071ace437bcfee9 body_fp=47fcbe39763ff24968bc52d08fa33411d55a6c013e6284c1c7cccfcb8e837c57 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
## `def _go_call_sites(source: bytes) -> list[CallSite]`

Walk a Go source file's tree-sitter AST and return the 0-based `(line, col)` position of each selector field in `x.Method(...)` call expressions, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_rust_call_sites fingerprint=3003e44cdd652a788965c1090d3dd310c26de169400d6e0131b66292c3ee66e7 body_fp=6b3fb0d5b91e2e75e682a6b6e4c7b8e5b308b206fa8fa5e5f0621051d0748a73 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
## `def _rust_call_sites(source: bytes) -> list[CallSite]`

Parse `source` bytes as Rust and return 0-based `(line, col)` positions for each `x.method(...)` field-expression call site, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_c_call_sites fingerprint=19ed181f854bcd63beb168f00b3df96bbc573b348ce2c6bc07ac994e3c03d9cb body_fp=d0a47a43bdb8b0ff9c8c5f543d8000cec07b16e1e7176cd02bfb40dab13f4d9c source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
## `def _c_call_sites(source: bytes) -> list[CallSite]`

Parse `source` and return 0-based `(line, col)` positions of each `p->field(...)` or `s.field(...)` member call expression in C, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:_lua_call_sites fingerprint=8226c453d01e0a6bbb1b96dc77bf98b79321d413d73c776f9ba2380e023d9abc body_fp=dd42b9bdb2d595902291a504cba7d354d03f410cdb853e462af30fbb6c456f01 source_ref=6c32e743b56c123c0ee5a83d6b4335e505711be4 role=parsing -->
## `def _lua_call_sites(source: bytes) -> list[CallSite]`

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
<!-- trie:section symbol=trie/parse/resolvers/specs:python_spec fingerprint=96fc1ad209d46807b9fa45aec16bfdfab5308bcb5d34e6adb82105dc239d695e body_fp=255cd73a3f31b9d0fa3f201bb889079e1542bbce5596601f9f45945242dee492 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def python_spec() -> LspServerSpec | None`

Return the first available Python `LspServerSpec`, honouring a `servers.python` command override and returning `None` if the resolver is disabled or no server is installed; otherwise prefers `BASEDPYRIGHT_SPEC` over `PYRIGHT_SPEC`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:typescript_spec fingerprint=9a65f998d4034b9c4bfc9d24048066b01dac70b0922ff279822079e0c672b83b body_fp=db7754c59846ba399bfacff940399ca5848d74501d3b008afe601d9ad1d3d79c source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def typescript_spec() -> LspServerSpec | None`

Return `TYPESCRIPT_SPEC` gated through `_apply_config`, or `None` if disabled or `typescript-language-server` is not on PATH.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:GO_SPEC fingerprint=953d42759d95c7701356eb8949b276c65d97f699d8a543f9a4f22e08966aea73 body_fp=3c10ba7560ce42913cf7555a752289ee5c99ca581dd5d8145bf6c81e7e86ae2d source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
`LspServerSpec` for Go, binding `gopls` (stdio) to the Go call-site walker with a 30 s init timeout and 30 s ready timeout.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:RUST_SPEC fingerprint=6d6a8a0079cb0a530f8ded3703398d44d03a95fccc1430b3c08d258875f5264b body_fp=4c0f459af56940e0359470ce84f594eeab5b11258325c69b342ccbb45bd944ed source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
`LspServerSpec` for `rust-analyzer` over stdio, with a 90 s init timeout and 90 s ready timeout before queries.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:C_SPEC fingerprint=6924819c197d806b75b02b8c6a568d0f9a7a6b8c367406ca6370f0be39d449f0 body_fp=edf231c920678349b7b4ee5464f16bed31eb1c7a8d3d59c4207c7a594163aa6c source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
`LspServerSpec` constant binding clangd to the C language with a 30 s init timeout and 20 s ready timeout.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:LUA_SPEC fingerprint=90657db296a3ec19a70063390d4debce0c1f5b914d0d2598983ea30346f16571 body_fp=320038ba57d584e94e428b31f75b31587a04550a386d412c170dc3a9ab3e430e source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
`LspServerSpec` for Lua, binding `lua-language-server` over stdio with a 30 s init timeout and 20 s ready timeout.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:go_spec fingerprint=d7496da704f5290d3c9913b9c6ced9eba3469dd03ec3997d7570b9144a594e27 body_fp=aa13b38d403bd21946629947cbaa65068f96b0c83354e716c9b4af7350163b92 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def go_spec() -> LspServerSpec | None`

Return `GO_SPEC` (with any configured overrides applied) if `gopls` is found on PATH and the resolver is enabled, otherwise `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:rust_spec fingerprint=81bf238cd95fb4fc46ee3f5e6c1ec95ac40f399edf3e53566e1571fa71119cb1 body_fp=f18d318fb6cfc1d4e6058879ea8595218180a0cbc386c36119cdb74e75fb57a7 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def rust_spec() -> LspServerSpec | None`

Return `RUST_SPEC` (after applying config overrides) if `rust-analyzer` is on PATH and the resolver is enabled, otherwise `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:c_spec fingerprint=33ca96a0908a99934f9d9f1c40c99fb02bbf6601d192b127c7c081c7cdfbd1b2 body_fp=e9ac39e08b97babad7883e14c7c7b4ee8e3cd2fb096a5ac453376978ff459be4 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def c_spec() -> LspServerSpec | None`

Return `C_SPEC` (possibly overridden) if clangd is found on PATH and the resolver is enabled for C, otherwise return `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:lua_spec fingerprint=20d1f792e6441a624c34894e0293cec74833dab432b39fdb84cefed5fe8e0b22 body_fp=9a2988079c17027e002ec5389608f6e9f4b8b39fefbc6960fbb9814a1a8355e2 source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
## `def lua_spec() -> LspServerSpec | None`

Return the Lua LSP spec if `lua-language-server` is on PATH and the resolver is enabled for Lua, otherwise return `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolvers/specs:__all__ fingerprint=da297f2208e5710d49e326c325cdef0098d2d1141b32a1a60c8f362e17981352 body_fp=e1778cec5594f6e2ddfea877d371e992a22f3997dcebad5e56fe0c4c65bed1ea source_ref=6c06c7b10b7c4e22c232fe504e6f8e8229afcdd6 role=config -->
Declares the public API of this module: all per-language `LspServerSpec` constants, their availability-checking accessor functions, and `configure_resolver`.
<!-- trie:end -->