---
trie_version: 0.1.5
source: trie/sync/generator.py
file_fingerprint: 964981199b832fdb4da22374a1046eace1692f31593ac3856d98bc89fb0ff2d2
last_synced_at: '2026-06-03T21:15:52Z'
defines:
- kind: module
  qualified_name: trie/sync/generator:__module__
  lines: 1-178
- kind: constant
  qualified_name: trie/sync/generator:SYSTEM_PROMPT
  lines: 12-30
- kind: constant
  qualified_name: trie/sync/generator:DIFF_AWARE_RUBRIC
  lines: 36-55
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 59-61
- kind: constant
  qualified_name: trie/sync/generator:RegenMode
  lines: 64-64
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 68-77
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 80-85
- kind: function
  qualified_name: trie/sync/generator:_symbol_context_clause
  lines: 88-98
- kind: function
  qualified_name: trie/sync/generator:_symbol_source
  lines: 101-106
- kind: function
  qualified_name: trie/sync/generator:_build_request
  lines: 109-116
- kind: function
  qualified_name: trie/sync/generator:_build_diff_aware_request
  lines: 119-134
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 137-177
incoming_refs: 30
outgoing_refs: 1
---
<!-- trie:section symbol=trie/sync/generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a111ad797f24416f434a6cb14b252a0a858200141f74eccc33747b7ae782f52d source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Generates documentation for Python source symbols using LLM-powered analysis with caching and diff-aware regeneration capabilities.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:SYSTEM_PROMPT fingerprint=95516de738a5633ca13e52935ce9bac749d63d4c1f41461f4ed457302ccf56e2 body_fp=96692dba33a5100a07c02b0ce487aecc7ce14c1dbda1b61b967a6608b9dfd6ee source_ref=24a303d77a226761266352fc352f56726b09a861 -->
System prompt template instructing LLMs to generate terse, accurate documentation for Python symbols.

- Emphasizes token economy and navigation benefits over source code
- Provides specific formatting guidelines for documentation sections
- Includes architectural role classification requirements for graph visualization
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:DIFF_AWARE_RUBRIC fingerprint=7c866bd51ce563f306b0d97f7dc4de26b2b4a58b79c09173c397935974ee876b body_fp=c72e1db635168008bccd66c118c4b2e25151fb16e923831343dfd56514c5feef source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Provides LLM instructions for distinguishing cosmetic source changes from behavioral changes during prose regeneration.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=9f5623b4d7b5b7dce882366b565f7525d3e38eb1f5f98f530d69a229eec4d3c4 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Holds file metadata for documentation generation including the path and complete source text.

- `file_path`: Path identifier for the Python file being documented
- `source_text`: Complete source code content of the file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:RegenMode fingerprint=452f3b350a7c4165e170ddda83e4dd9e2a215de97abd1bad52673e3b27fe8a25 body_fp=b18fe49d0110e4d165bb18a68ca7c8102c215ea6f1b51e91ca196abcf78a9f7b source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Type alias for generation modes: "cold" for fresh generation, "diff_aware" for incremental updates.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=f3aae776ff84ca6588c36720f5de56f41b475e3c957d6d99a5157e908517c9c1 body_fp=0b0fef4cf510ed9faf7c4d53dc10b12eb17b7622964161848cdf56409acae725 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Represents the result of generating documentation for a single symbol, including the prose body and token usage metrics.

- `cache_creation_input_tokens`: tokens used when creating a new cache entry
- `cache_read_input_tokens`: tokens used when reading from an existing cache
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=df5e710483d89bfcbd36a5292b923844141f5aae8d297d2548d1229e8561762c source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Builds a cached context string that includes the file path and complete source code for LLM prompting.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_context_clause fingerprint=c09e100e6fb7e7cc96cdc11924de704c27a8ccd8dfe93971657b33f5d5703293 body_fp=e77866ebfe06d98483def51687fc630575ad27b3764646e5227b40b64a1a9035 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Returns a descriptive string categorizing a Symbol for documentation prompts.

- Returns method type with class name for methods, including decorator labels for @property/@classmethod/@staticmethod/@abstractmethod
- Returns decorated class description when class has decorators
- Falls back to basic symbol kind for other cases
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_source fingerprint=68bf268b9a98ae2d58e9e30fa409031d97d648fe216e5835e1c5fe53e4b7b3a5 body_fp=b38916be0f63a761b71d6d16f930e79567da2423ef5a05723e0bb6343a30be21 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Assembles Symbol decorators, signature, and body text into a complete source code string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_request fingerprint=3fdb7f4957e6e175fe0f6f5969b47e187de7e809a518a6f3b81a8b8935857b70 body_fp=939813eff15302c17c84a234d92e033c56382ce8e4d6378e6fd1ffd64436f9d8 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Builds a user prompt requesting documentation for a symbol by combining its context, location, and source code into a formatted string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_diff_aware_request fingerprint=17ae7e782e9ad3e153d3b6375ce815b751c4a8347a297583f0c14dc12fbaac28 body_fp=70c0dfdb664a6e0408fbcd4b8bb9c73fdc3499b1670f5b32b4bfe8ed8742c3b6 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Builds a user prompt for diff-aware documentation generation that compares previous and current source code with existing prose.

- **previous_source**: Source code from the symbol's previous version
- **previous_prose**: Existing documentation to potentially preserve
- **current_source**: Current version of the symbol's source code
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=ce4cab4168c3b93f3e1cedb7680f1a179adffb56e9c298754ee1afad94da334d body_fp=4b0558ca4e045c434a17185848d00f28d714026ca40421b3d88fc727e23e0bc5 source_ref=24a303d77a226761266352fc352f56726b09a861 -->
Generates documentation for a Python symbol using an LLM client, optionally using diff-aware regeneration.

- `previous_source` and `previous_prose`: when both provided, enables diff-aware mode that preserves existing prose unless behavior changed
- `max_tokens`: maximum tokens for the LLM response
- Returns `GeneratedSection` with generated documentation body, token usage metrics, and architectural metadata
<!-- trie:end -->