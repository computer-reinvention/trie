---
trie_version: 0.1.0
source: trie/sync/generator.py
file_fingerprint: 13f546d50e66cd8ef4ba3f573f2a567fa1fbb9466d7617db43d4e4bf4d304699
last_synced_at: '2026-05-14T18:32:56Z'
defines:
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 30-32
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 36-42
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 45-50
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 62-89
incoming_refs: 11
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=06718571b560b121ee570f9e7a3d89b3fb8feaa32abb21c5c48997ba6443b57c -->
## `FileGenerationContext(file_path: str, source_text: str)`

Frozen dataclass carrying the file path and source text needed to build a cached prompt context.

- `file_path`: source-root-relative path, used verbatim in the prompt.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=0ab9bfe3763274e340bdfc6f2419b51ca1b2697dc9a0e16ff239db3fa4a096be body_fp=f0e7905a0ec6104b71f0df61078000b1ebc0b6c502659bfd5b191c28f7963338 -->
## `GeneratedSection(qualified_name, body, input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens)`

Frozen dataclass holding the generated Markdown body for one symbol alongside token usage counters.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=3731bd19d300307a8b944762cd894039d66dfca1bd176cfe7d7b5f16d52f6bd5 -->
## `build_cached_context(ctx: FileGenerationContext) -> str`

Build the prompt string containing the file path and full source text for cache-eligible context.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=b0745b3e90674fb0bbcb0916b950724105c9fbc21de2603b133d9dd9f65e43aa body_fp=e32a37961a8229fe6c118f12b33e9f1dfda9ff29b19c196136558b48fcf2a898 -->
## `generate_section(*, symbol: Symbol, file_ctx: FileGenerationContext, client: ModelClient, max_tokens: int = 1024) -> GeneratedSection`

Generate the Markdown documentation body for a single Python symbol via a model call.

- `file_ctx`: provides file path and source text for the cached prompt context.
- `cached_context`: shared across all symbols in the file to amortise prompt-cache costs.
<!-- trie:end -->