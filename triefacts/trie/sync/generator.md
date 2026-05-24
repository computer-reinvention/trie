---
trie_version: 0.1.2
source: trie/sync/generator.py
file_fingerprint: 489b23566c702a31779ddc39c9eb0e5cd556f54f118d3e253202927e369a5f97
last_synced_at: '2026-05-23T23:51:59Z'
defines:
- kind: module
  qualified_name: trie/sync/generator:__module__
  lines: 1-232
- kind: constant
  qualified_name: trie/sync/generator:SYSTEM_PROMPT
  lines: 9-30
- kind: constant
  qualified_name: trie/sync/generator:DIFF_AWARE_RUBRIC
  lines: 36-57
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 61-63
- kind: constant
  qualified_name: trie/sync/generator:RegenMode
  lines: 66-66
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 70-77
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 80-85
- kind: function
  qualified_name: trie/sync/generator:_symbol_context_clause
  lines: 88-116
- kind: function
  qualified_name: trie/sync/generator:_build_request
  lines: 119-127
- kind: function
  qualified_name: trie/sync/generator:_build_diff_aware_request
  lines: 130-160
- kind: function
  qualified_name: trie/sync/generator:_symbol_source
  lines: 163-175
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 178-231
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
<!-- trie:section symbol=trie/sync/generator:SYSTEM_PROMPT fingerprint=ad20b6f444c5ba37460802394b74294c961478ebd752b3e8c4cc32556ce7601c body_fp=5e13856ddc19dfd51664a8060516c3b268d930c002ab3c9fc92469abe30300e3 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `SYSTEM_PROMPT`

System prompt injected into every generation request, defining output format and hard rules for the LLM documentation writer.
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
<!-- trie:section symbol=trie/sync/generator:_symbol_context_clause fingerprint=66ffa00d18d0960758db5ad3f66c58d8a68fb444b601bc3317159e0906743eda body_fp=5099e4af1fdd8b172bf5ad4ad3ac58e2118267499083eaa78bd0b8ac84b294ce source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `_symbol_context_clause(symbol: Symbol) -> str`

Produce a human-readable string describing a `Symbol`'s kind and class membership for use in LLM prompts.

- Returns decorator-qualified label (e.g. `"a @property of class \`Foo\`"`) for significant decorators.
- Falls back to `"a method of class \`X\`"`, `"a class (decorated with ...)"`, or `"a {kind}"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_request fingerprint=b0e10db84ea47a101c1619368b1e7524d95dd0b8ea67b57ed7919bae32792039 body_fp=9d150d4275bffe2ccbebf01fa2dc6e875baa3c6f44b62c83b057e20aab2d04ca source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `_build_request(symbol: Symbol) -> str`

Build the cold-write user message for generating documentation for a single symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_diff_aware_request fingerprint=cf9165ed76197dbeecd98a545a6132e7cbad618c1e7727593abeb59788f1be08 body_fp=28cbdd00cc35df139b18b4397636e6442e54cbe342935147c83b646e1b2c55ee source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `_build_diff_aware_request(symbol: Symbol, *, previous_source: str, previous_prose: str, current_source: str) -> str`

Build the user-message string for diff-aware documentation regeneration, combining `DIFF_AWARE_RUBRIC` with three labelled source/prose blocks.

- `previous_source`: full decorated source (decorators + signature + body) from the prior version.
- `current_source`: same format for the current version; not synthesised from `symbol`.
- `previous_prose`: existing Markdown prose to preserve verbatim on cosmetic changes.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_source fingerprint=c4f0bf9d6a8940532c18d8bbf3cfa1580d0607b6c87bdcfe5afe636542806f9e body_fp=986ed820ac74fbd5f24cfe16c66c3d4e2cd4d8a12af77f0692354090505a9b76 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `_symbol_source(symbol: Symbol) -> str`

Reconstruct the full decorated source block for a `Symbol` by joining decorators, signature, and body into a single string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=15aece61f894d2f21e7f19deda458eb6d940a6813eb85e35d6540e5f39ff908f body_fp=bbfd6e62c856d7a824325066d14d2d8f879ae953c5a2c12b367269802469e4c1 source_ref=e1429e000717536ad70e96ef323336c0f72c9593 -->
## `generate_section(*, symbol, file_ctx, client, max_tokens=1024, previous_source=None, previous_prose=None) -> GeneratedSection`

Generate the Markdown documentation body for a single `Symbol` via a `ModelClient`.

- `previous_source` + `previous_prose`: both required to activate diff-aware mode; either `None` forces cold generation.
- `file_ctx`: provides the full source file as a cached prompt context shared across symbols.
- `mode`: set to `"diff_aware"` or `"cold"` in the returned `GeneratedSection`.
<!-- trie:end -->