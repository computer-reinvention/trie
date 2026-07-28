---
trie_version: 0.1.9
source: trie/parse/resolvers/specs.py
file_fingerprint: ccd22413d5967589af651d139785cc89789a8f6f331af9ed4598ca01bd4a26b7
last_synced_at: '2026-07-28T23:35:51Z'
description: "Per-language LSP server specs \u2014 the one place a new language is\
  \ registered."
defines:
- kind: module
  qualified_name: trie/parse/resolvers/specs:__module__
  lines: 1-123
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
- kind: constant
  qualified_name: trie/parse/resolvers/specs:PYRIGHT_SPEC
  lines: 78-83
- kind: constant
  qualified_name: trie/parse/resolvers/specs:BASEDPYRIGHT_SPEC
  lines: 85-90
- kind: constant
  qualified_name: trie/parse/resolvers/specs:TYPESCRIPT_SPEC
  lines: 92-97
- kind: function
  qualified_name: trie/parse/resolvers/specs:python_spec
  lines: 100-108
- kind: function
  qualified_name: trie/parse/resolvers/specs:typescript_spec
  lines: 111-113
- kind: constant
  qualified_name: trie/parse/resolvers/specs:__all__
  lines: 116-122
incoming_refs: 5
outgoing_refs: 2
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
<!-- trie:section symbol=trie/parse/resolvers/specs:__all__ fingerprint=f894f7e21538dbc63d8f851639d2104f7cbeb7400f5593e9bec963f8ce5f2945 body_fp=3040d9be0dc273610cc2e6524e16b65fd3ee67d33ba7215c84a6d18965e1776c source_ref=490e2b18f9c0beeb78883965246615da4373c0d6 role=config -->
Declares the public API of the module, exporting the three `LspServerSpec` constants and the two availability-checking selector functions.
<!-- trie:end -->