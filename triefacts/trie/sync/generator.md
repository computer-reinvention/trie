---
trie_version: 0.1.5
source: trie/sync/generator.py
file_fingerprint: 8c718b35b1e8951bfad8c044a242877f43114e1e591e9b27bb61128ce58ff136
last_synced_at: '2026-05-28T14:27:14Z'
defines:
- kind: module
  qualified_name: trie/sync/generator:__module__
  lines: 1-171
- kind: constant
  qualified_name: trie/sync/generator:SYSTEM_PROMPT
  lines: 12-28
- kind: constant
  qualified_name: trie/sync/generator:DIFF_AWARE_RUBRIC
  lines: 34-53
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 57-59
- kind: constant
  qualified_name: trie/sync/generator:RegenMode
  lines: 62-62
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 66-73
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 76-81
- kind: function
  qualified_name: trie/sync/generator:_symbol_context_clause
  lines: 84-94
- kind: function
  qualified_name: trie/sync/generator:_symbol_source
  lines: 97-102
- kind: function
  qualified_name: trie/sync/generator:_build_request
  lines: 105-112
- kind: function
  qualified_name: trie/sync/generator:_build_diff_aware_request
  lines: 115-130
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 133-170
incoming_refs: 28
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=ec0a011bd8f536c4ab42af9bba41f34e592478d86ec94f6de15e8313b3b29ab9 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `trie/sync/generator.py`

Build and dispatch LLM generation requests for per-symbol Markdown documentation, with optional diff-aware regeneration.

- `SYSTEM_PROMPT`: instructions defining output format and rules for the model.
- `DIFF_AWARE_RUBRIC`: rubric prepended to diff-aware requests to anchor prose preservation.
- `FileGenerationContext`: source-root-relative file path and full source text for a prompt.
- `GeneratedSection`: output record carrying prose, token counts, and regen mode.
- `RegenMode`: either `"cold"` (fresh write) or `"diff_aware"` (preserve-unless-behavioural).
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:SYSTEM_PROMPT fingerprint=95516de738a5633ca13e52935ce9bac749d63d4c1f41461f4ed457302ccf56e2 body_fp=d5b32bec7ccafe6a308b928eb214b1aa3f124615aad4a0c7bd4647ba8452fcc1 source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `SYSTEM_PROMPT: str`

System prompt passed to the LLM defining prose style, format rules, and documentation guidelines for symbol summarisation.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:DIFF_AWARE_RUBRIC fingerprint=7c866bd51ce563f306b0d97f7dc4de26b2b4a58b79c09173c397935974ee876b body_fp=da851514c0741aa5a6fffe15156ee9c078948983deb7cb4966cfb77d500e3951 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `DIFF_AWARE_RUBRIC`

Prompt rubric prepended to diff-aware requests, instructing the model to preserve prose on cosmetic changes and update only on behavioural ones.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=c0f724cc0888f540553d321d746ea9ebeb22b020e117e123fa4b116381dd0f85 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `FileGenerationContext(file_path: str, source_text: str)`

Immutable container pairing a file's source-root-relative path with its full source text for prompt construction.

- `file_path`: source-root-relative path, used verbatim in the prompt header.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:RegenMode fingerprint=452f3b350a7c4165e170ddda83e4dd9e2a215de97abd1bad52673e3b27fe8a25 body_fp=4b412d4641e299d3e73ef8234206a979d8817ba1031f6f745aed0e0b9f35ffba source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `RegenMode = Literal["cold", "diff_aware"]`

Type alias distinguishing cold generation from diff-aware prose preservation mode.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=f1027611aa488c7d14aa4b428365e6cce3f9aa74c5c38a708d26b45f09c449b8 body_fp=cc375979e0ca578f8c771f2019c7f072a18807f864d2d494e8de577ad6711daa source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `@dataclass(frozen=True) class GeneratedSection`

Immutable result of a single symbol documentation generation call.

- `body`: the generated Markdown prose for the symbol.
- `mode`: `"cold"` for fresh generation; `"diff_aware"` for incremental update.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=08f6305ef63a87ca789cb18cdfcade953188d106e73688478124efff07fc5788 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `build_cached_context(ctx: FileGenerationContext) -> str`

Build the prompt preamble embedding the file path and full source text for prompt-cache reuse across symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_context_clause fingerprint=c09e100e6fb7e7cc96cdc11924de704c27a8ccd8dfe93971657b33f5d5703293 body_fp=5aa7f7d2548fefb90b3264b6856bf53dec331787280b82624863f84311a6bde7 source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `_symbol_context_clause(symbol: Symbol) -> str`

Build a human-readable context string describing a symbol's kind and class relationship for use in prompts.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_source fingerprint=68bf268b9a98ae2d58e9e30fa409031d97d648fe216e5835e1c5fe53e4b7b3a5 body_fp=755baffec017b39b7b44df3f5839667582d3625e035e144ea7ec3ff591d47e73 source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `_symbol_source(symbol: Symbol) -> str`

Render a `Symbol` as a source string, prepending decorator lines before the signature and body.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_request fingerprint=3fdb7f4957e6e175fe0f6f5969b47e187de7e809a518a6f3b81a8b8935857b70 body_fp=8b70b839a4502e0405dceb9dc325518894028b82677b34504150e3676cbc61f9 source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `_build_request(symbol: Symbol) -> str`

Build a cold-generation user prompt string for a single symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_diff_aware_request fingerprint=17ae7e782e9ad3e153d3b6375ce815b751c4a8347a297583f0c14dc12fbaac28 body_fp=c222d2d76a1491d57c4309dc4d1e09bb4eba85820296e8b7d3dfbef3abd1b947 source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `_build_diff_aware_request(symbol, *, previous_source, previous_prose, current_source) -> str`

Build a diff-aware LLM user prompt embedding the rubric, symbol metadata, and before/after source and prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=7029e9e7c2c66f887ff0ca6a4c46cace980c04a482ebf8a8c2ca11fd5a7a308a body_fp=c06e77c78ec257a46a84bdee23577c03f2f317f011ca3d1e43a19cf6b599d27e source_ref=f0773534fd360386bb5fff199726100f7f61a175 -->
## `generate_section(*, symbol, file_ctx, client, max_tokens=1024, previous_source=None, previous_prose=None) -> GeneratedSection`

Generate a documentation section for a single symbol by calling the LLM client.

- `previous_source` / `previous_prose`: when both provided, switches to diff-aware mode to preserve unchanged prose.
- `mode`: set to `"diff_aware"` or `"cold"` depending on whether previous context was supplied.
<!-- trie:end -->