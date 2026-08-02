---
trie_version: 0.3.0
source: trie/sync/generator.py
file_fingerprint: fa4100a84b3f0ba130c31957c5c3e8330d91769560bb7e2007bc33b76b1d249c
last_synced_at: '2026-08-01T01:53:06Z'
defines:
- kind: module
  qualified_name: trie/sync/generator:__module__
  lines: 1-269
- kind: constant
  qualified_name: trie/sync/generator:SYSTEM_PROMPT
  lines: 12-31
- kind: constant
  qualified_name: trie/sync/generator:DIFF_AWARE_RUBRIC
  lines: 37-56
- kind: class
  qualified_name: trie/sync/generator:FileGenerationContext
  lines: 60-62
  signature: class FileGenerationContext
- kind: constant
  qualified_name: trie/sync/generator:RegenMode
  lines: 65-65
- kind: class
  qualified_name: trie/sync/generator:GeneratedSection
  lines: 69-78
  signature: class GeneratedSection
- kind: function
  qualified_name: trie/sync/generator:build_cached_context
  lines: 81-86
  signature: 'def build_cached_context(ctx: FileGenerationContext) -> str'
- kind: function
  qualified_name: trie/sync/generator:_symbol_context_clause
  lines: 89-105
  signature: 'def _symbol_context_clause(symbol: Symbol) -> str'
- kind: function
  qualified_name: trie/sync/generator:_symbol_source
  lines: 108-113
  signature: 'def _symbol_source(symbol: Symbol) -> str'
- kind: function
  qualified_name: trie/sync/generator:_build_request
  lines: 116-123
  signature: 'def _build_request(symbol: Symbol) -> str'
- kind: function
  qualified_name: trie/sync/generator:_build_diff_aware_request
  lines: 126-141
  signature: 'def _build_diff_aware_request( symbol: Symbol, *, previous_source: str, previous_prose: str, current_source: str, ) -> str'
- kind: function
  qualified_name: trie/sync/generator:generate_section
  lines: 144-184
  signature: 'def generate_section( *, symbol: Symbol, file_ctx: FileGenerationContext, client: TrieClient, max_tokens: int = 1024, previous_source: str | None = None, previous_prose: str | None = None, ) -> GeneratedSection'
- kind: constant
  qualified_name: trie/sync/generator:ROLE_SYSTEM_PROMPT
  lines: 187-196
- kind: class
  qualified_name: trie/sync/generator:InferredRole
  lines: 200-209
  signature: class InferredRole
- kind: function
  qualified_name: trie/sync/generator:_taxonomy_clause
  lines: 212-215
  signature: 'def _taxonomy_clause(allowed_roles: list[tuple[str, str]]) -> str'
- kind: function
  qualified_name: trie/sync/generator:infer_role
  lines: 218-268
  signature: 'def infer_role( *, symbol: Symbol, file_ctx: FileGenerationContext, client: TrieClient, allowed_roles: list[tuple[str, str]], existing_prose: str | None = None, max_tokens: int = 128, ) -> InferredRole'
incoming_refs: 38
outgoing_refs: 4
---
<!-- trie:section symbol=trie/sync/generator:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=a111ad797f24416f434a6cb14b252a0a858200141f74eccc33747b7ae782f52d source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
Generates documentation for Python source symbols using LLM-powered analysis with caching and diff-aware regeneration capabilities.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:SYSTEM_PROMPT fingerprint=95516de738a5633ca13e52935ce9bac749d63d4c1f41461f4ed457302ccf56e2 body_fp=96692dba33a5100a07c02b0ce487aecc7ce14c1dbda1b61b967a6608b9dfd6ee source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
System prompt template instructing LLMs to generate terse, accurate documentation for Python symbols.

- Emphasizes token economy and navigation benefits over source code
- Provides specific formatting guidelines for documentation sections
- Includes architectural role classification requirements for graph visualization
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:DIFF_AWARE_RUBRIC fingerprint=7c866bd51ce563f306b0d97f7dc4de26b2b4a58b79c09173c397935974ee876b body_fp=c72e1db635168008bccd66c118c4b2e25151fb16e923831343dfd56514c5feef source_ref=24a303d77a226761266352fc352f56726b09a861 role=llm-client -->
Provides LLM instructions for distinguishing cosmetic source changes from behavioral changes during prose regeneration.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:FileGenerationContext fingerprint=a1af16c6fabdf74c0ad9d8b4b7e134aaa5a35b72940340443be4ac8e2690cc4f body_fp=c2716d83e2a45497f95e9a2a8279f08a14bc5f48872f1bdf3b6996c0d27526dd source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `class FileGenerationContext`

Holds file metadata for documentation generation including the path and complete source text.

- `file_path`: Path identifier for the Python file being documented
- `source_text`: Complete source code content of the file
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:RegenMode fingerprint=452f3b350a7c4165e170ddda83e4dd9e2a215de97abd1bad52673e3b27fe8a25 body_fp=b18fe49d0110e4d165bb18a68ca7c8102c215ea6f1b51e91ca196abcf78a9f7b source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
Type alias for generation modes: "cold" for fresh generation, "diff_aware" for incremental updates.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:GeneratedSection fingerprint=f3aae776ff84ca6588c36720f5de56f41b475e3c957d6d99a5157e908517c9c1 body_fp=942cddfc945436242a441c7ac5b616f2f1c736525d2cbb5879270a900809f0ba source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `class GeneratedSection`

Represents the result of generating documentation for a single symbol, including the prose body and token usage metrics.

- `cache_creation_input_tokens`: tokens used when creating a new cache entry
- `cache_read_input_tokens`: tokens used when reading from an existing cache
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:build_cached_context fingerprint=34a370dbfcfc18986700426fc5c4d20f78bf632efbbbb8fa306a9f6e2ac0df1f body_fp=8ae4152ad67184f0f696ed3e48d627a9dfb088e47e955a46053171e5aabe7ff5 source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `def build_cached_context(ctx: FileGenerationContext) -> str`

Builds a cached context string that includes the file path and complete source code for LLM prompting.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_context_clause fingerprint=938c1b91eb07818906515b99b7ac59a305eb263b56a7facf16c9b43d6eff7c66 body_fp=b586bc5040aae0b06595c4137cedfcd571c1d213cac52cc2ea481503a240038d source_ref=21b7e93e31c07db925e2c129b972ded57bd0626f role=util -->
## `def _symbol_context_clause(symbol: Symbol) -> str`

Returns a descriptive string categorizing a Symbol for documentation prompts.

- Returns method type with class name for methods, including decorator labels for @property/@classmethod/@staticmethod/@abstractmethod
- Returns decorated class description when class has decorators
- Returns enum member description with owning enum name for `enum_member` kind
- Returns field/property description with owning class name for `property` kind
- Falls back to basic symbol kind for other cases
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_symbol_source fingerprint=68bf268b9a98ae2d58e9e30fa409031d97d648fe216e5835e1c5fe53e4b7b3a5 body_fp=96086fc3446923d7922a2dc4f7e8c6c342b83c7cda39e8dc1ee56447adaf7664 source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `def _symbol_source(symbol: Symbol) -> str`

Assembles Symbol decorators, signature, and body text into a complete source code string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_request fingerprint=3fdb7f4957e6e175fe0f6f5969b47e187de7e809a518a6f3b81a8b8935857b70 body_fp=72449fbf9dc4e98dd5b56a4b446c0d96343d41db1b8493997827035e38a5afcd source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `def _build_request(symbol: Symbol) -> str`

Builds a user prompt requesting documentation for a symbol by combining its context, location, and source code into a formatted string.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_build_diff_aware_request fingerprint=17ae7e782e9ad3e153d3b6375ce815b751c4a8347a297583f0c14dc12fbaac28 body_fp=65518e03a5c2a69953a3e1bb70b28578d8af106ae66d9d2ce270bff0becd6a73 source_ref=24a303d77a226761266352fc352f56726b09a861 role=documentation-sync -->
## `def _build_diff_aware_request( symbol: Symbol, *, previous_source: str, previous_prose: str, current_source: str, ) -> str`

Builds a user prompt for diff-aware documentation generation that compares previous and current source code with existing prose.

- **previous_source**: Source code from the symbol's previous version
- **previous_prose**: Existing documentation to potentially preserve
- **current_source**: Current version of the symbol's source code
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:generate_section fingerprint=ce4cab4168c3b93f3e1cedb7680f1a179adffb56e9c298754ee1afad94da334d body_fp=8e46eb1059273ba0881cd077ebfc0650f72296032ee7fe634daf1e4240d210b1 source_ref=21b7e93e31c07db925e2c129b972ded57bd0626f role=orchestration -->
## `def generate_section( *, symbol: Symbol, file_ctx: FileGenerationContext, client: TrieClient, max_tokens: int = 1024, previous_source: str | None = None, previous_prose: str | None = None, ) -> GeneratedSection`

Generates documentation for a Python symbol using an LLM client, optionally using diff-aware regeneration.

- `previous_source` and `previous_prose`: when both provided, enables diff-aware mode that preserves existing prose unless behavior changed
- `max_tokens`: maximum tokens for the LLM response
- Returns `GeneratedSection` with generated documentation body, token usage metrics, and architectural metadata
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:ROLE_SYSTEM_PROMPT fingerprint=57be9022b96f58095cf1b206c4d53a3a6b9ddc4e66084375bc4a2ba558c2ad3b body_fp=7936ae7dbd9bd0a721e4ff06c830c6e4add7ef84f7c060e46cea50b81e7f0777 source_ref=f21aebb2ba00fc12bbd954ea8c5fbeba249f65e7 role=config -->
System prompt template instructing the LLM to classify symbols into architectural roles without generating prose.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:InferredRole fingerprint=cdf45a00b4b0b0b231ed1379b31b7c580311e013bd4cb99b36041e4c1a4f8ee3 body_fp=0e6e84c2e9aaced318a74ec4cc0fa4da7c276e7489c673b0c8a07bbd8aace933 source_ref=f21aebb2ba00fc12bbd954ea8c5fbeba249f65e7 role=model -->
## `class InferredRole`

Stores role/boundary classification results for a symbol along with token usage metrics from the inference call.

- `role`: architectural role tag from the project vocabulary
- `boundary`: position relative to system boundary (entry/exit/internal)
- token fields: usage breakdown for the classification API call
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:_taxonomy_clause fingerprint=ec421c2ae1cc452d48a503a46081e844f7cc56d317355a0f1d25619413e73f8e body_fp=5b466ddbef97b3e082221b78c41a734dee8073ea2f72fa13ffd4ee102ca284a9 source_ref=f21aebb2ba00fc12bbd954ea8c5fbeba249f65e7 role=util -->
## `def _taxonomy_clause(allowed_roles: list[tuple[str, str]]) -> str`

Renders a list of role names and descriptions into a formatted prompt string for LLM classification.

- Returns a string starting with "Choose exactly one role from this vocabulary:"
- Each role becomes a bulleted line, with description if provided
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/generator:infer_role fingerprint=667c778f7f1ac6e10347561c7372c3b091feb87da78916d6b85e1640a037ce08 body_fp=382affe89ac382b7ac258a58ae07191d665cb23213305f0f529ecbb2ec9d202b source_ref=21b7e93e31c07db925e2c129b972ded57bd0626f role=domain -->
## `def infer_role( *, symbol: Symbol, file_ctx: FileGenerationContext, client: TrieClient, allowed_roles: list[tuple[str, str]], existing_prose: str | None = None, max_tokens: int = 128, ) -> InferredRole`

Classifies a Python symbol's architectural role using an LLM against a fixed vocabulary without regenerating prose.

- `allowed_roles`: List of (name, description) tuples defining the role taxonomy
- `existing_prose`: Optional documentation text to aid classification
- Returns role clamped to vocabulary or empty string if invalid
<!-- trie:end -->