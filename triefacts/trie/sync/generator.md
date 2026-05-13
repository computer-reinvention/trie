---
trie_version: 0.1.0
source: trie/sync/generator.py
file_fingerprint: 13f546d50e66cd8ef4ba3f573f2a567fa1fbb9466d7617db43d4e4bf4d304699
last_synced_at: '2026-05-12T18:34:20Z'
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
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=ea66cd187e8db40b8d92b3e2fabde700f5cc4e42e638b69016dfcddd96701839 -->
## `FileGenerationContext(file_path: str, source_text: str)`

Frozen dataclass carrying the source file path and text needed to build a cached generation prompt.

- `file_path`: source-root-relative path, used verbatim in the prompt.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=0ab9bfe3763274e340bdfc6f2419b51ca1b2697dc9a0e16ff239db3fa4a096be body_fp=f4629e7d9d0b6e54190668d8873aac71ae33fb867988a84c9c65c5070544d825 -->
## `GeneratedSection(qualified_name, body, input_tokens, output_tokens, cache_creation_input_tokens, cache_read_input_tokens)`

Frozen dataclass holding the generated Markdown body for one symbol alongside token usage metrics.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=9f96546eb42ca45a9f31b5a24d66e3c469be4f316a6d813813d7f3d728a5b686 -->
## `build_cached_context(ctx: FileGenerationContext) -> str`

Build the cache-eligible prompt string containing the file path and full source text.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=b0745b3e90674fb0bbcb0916b950724105c9fbc21de2603b133d9dd9f65e43aa body_fp=7222ba2e55c9b213c27ce53abcbb7d38d92842b605fa22d09e26c743374f8004 -->
## `generate_section(*, symbol: Symbol, file_ctx: FileGenerationContext, client: ModelClient, max_tokens: int = 1024) -> GeneratedSection`

Generate a Markdown documentation section for a single Python symbol via a model client.

- `cached_context`: system prompt + full source file; shared across symbols for prompt-cache reuse.
- `max_tokens`: caps output length; defaults to 1024.
<!-- trie:end -->