---
trie_version: 0.1.0
source: trie/sync/generator.py
file_fingerprint: 6c1e05b2416c4eea05493d1f21246bc67e93bc98dc90c4e5c7fc34862fa01aff
last_synced_at: '2026-05-16T11:23:58Z'
defines:
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 58-60
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 67-74
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 77-82
- kind: function
  qualified_name: trie/sync/generator:_build_request
  lines: 85-91
- kind: function
  qualified_name: trie/sync/generator:_build_diff_aware_request
  lines: 94-124
- kind: function
  qualified_name: trie/sync/generator:_symbol_source
  lines: 127-135
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 138-191
incoming_refs: 19
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=c74c6bc4bd488ecf35317893d0fc0f1c328bee6d2c15d8b3bf489c02d8545ffe source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `FileGenerationContext(file_path: str, source_text: str)`

Frozen dataclass bundling a file's source-root-relative path and full source text for prompt construction.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=f1027611aa488c7d14aa4b428365e6cce3f9aa74c5c38a708d26b45f09c449b8 body_fp=e02db865349cba91660e534663243f83840d1580dab19749cfb09d3ea924335c source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `GeneratedSection`

Frozen dataclass holding the generated Markdown body and token-usage metrics for one symbol.

- `mode`: `"cold"` for fresh generation, `"diff_aware"` for rubric-guided update.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=51edf0b58251f176e080f38f80b531e910bbd7b6ba51f850d8a1d2d31569e71f source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `build_cached_context(ctx: FileGenerationContext) -> str`

Build the cacheable prompt block containing the file path and full source text.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=15aece61f894d2f21e7f19deda458eb6d940a6813eb85e35d6540e5f39ff908f body_fp=78574f7b1948e9adef58c6da52ea6a3fcbbc9b49cffb69fea97ed3703511e110 source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `generate_section(*, symbol, file_ctx, client, max_tokens=1024, previous_source=None, previous_prose=None) -> GeneratedSection`

Generate the Markdown body for a single symbol via a model call, using cold or diff-aware mode.

- `previous_source` + `previous_prose`: both must be provided to activate diff-aware mode; either `None` forces cold mode.
- `file_ctx`: supplies the full source file as a cached prompt context, amortised across symbols in the same file.
- `max_tokens`: caps the model's output length.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:_build_request fingerprint=fb0ae4000b307cb75a6341181dccf02c42032dde4b83bce0e52e722163d90df2 body_fp=edfd7883095c5806e92524b77f7b6aaa6897a90d1b94e6a65365b2e7dc6d7ef0 source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `_build_request(symbol: Symbol) -> str`

Build the cold-write user message prompting the LLM to document a single symbol.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:_build_diff_aware_request fingerprint=b52e15d8c213ac4ab7f45ccb1dec48b9a6ab14d7b394c14310fba357d95e3a67 body_fp=affda1abcc6d87296263b1a2838837cd018b7c23d4ad3cef61c57d613224a566 source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `_build_diff_aware_request(symbol: Symbol, *, previous_source: str, previous_prose: str, current_source: str) -> str`

Build the user-message string for a diff-aware regeneration request.

- `previous_source`: full source (signature + body) of the symbol before the change.
- `current_source`: full source (signature + body) of the symbol after the change.
- Returns a prompt block containing the rubric, three labelled source/prose sections, and a closing format constraint.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:_symbol_source fingerprint=3c066b91d6eeae404201d2b89cad5a68a613d9fb6d8b0fbf606f513a850a9509 body_fp=9c1f2c996237b789661dd13dbfdc386fcfee3ad306c04feca66037e1d0b19c78 source_ref=2c58b1aa9ada95e7978956fc2d84138ee1f9a681 -->
## `_symbol_source(symbol: Symbol) -> str`

Reconstruct the full `<signature>:\n<body>` text for a symbol by joining its signature and body with a colon.
<!-- trie:end -->