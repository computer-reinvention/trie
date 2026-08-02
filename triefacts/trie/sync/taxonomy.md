---
trie_version: 0.3.0
source: trie/sync/taxonomy.py
file_fingerprint: d3527d467b1f6425152def101ac74e20134e50463b409924616b4766de39edd3
last_synced_at: '2026-08-01T01:53:04Z'
description: 'Role taxonomy: the project-specific role vocabulary that constrains role tagging.'
defines:
- kind: module
  qualified_name: trie/sync/taxonomy:__module__
  lines: 1-173
- kind: constant
  qualified_name: trie/sync/taxonomy:TAXONOMY_FILENAME
  lines: 27-27
- kind: class
  qualified_name: trie/sync/taxonomy:Role
  lines: 31-33
  signature: class Role
- kind: class
  qualified_name: trie/sync/taxonomy:Taxonomy
  lines: 37-60
  signature: class Taxonomy
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.names
  lines: 40-41
  signature: def names(self) -> list[str]
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.is_empty
  lines: 43-44
  signature: def is_empty(self) -> bool
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.to_json
  lines: 46-47
  signature: def to_json(self) -> dict[str, object]
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.from_json
  lines: 50-60
  signature: 'def from_json(cls, raw: dict[str, object]) -> Taxonomy'
- kind: function
  qualified_name: trie/sync/taxonomy:taxonomy_path
  lines: 63-65
  signature: 'def taxonomy_path(project_root: Path, config: Config) -> Path'
- kind: function
  qualified_name: trie/sync/taxonomy:load_taxonomy
  lines: 68-84
  signature: 'def load_taxonomy(project_root: Path, config: Config) -> Taxonomy | None'
- kind: function
  qualified_name: trie/sync/taxonomy:save_taxonomy
  lines: 87-92
  signature: 'def save_taxonomy(project_root: Path, config: Config, taxonomy: Taxonomy) -> Path'
- kind: constant
  qualified_name: trie/sync/taxonomy:TAXONOMY_SYSTEM_PROMPT
  lines: 95-109
- kind: class
  qualified_name: trie/sync/taxonomy:TaxonomyResult
  lines: 113-118
  signature: class TaxonomyResult
- kind: function
  qualified_name: trie/sync/taxonomy:derive_taxonomy
  lines: 121-172
  signature: 'def derive_taxonomy( *, store: Store, client: TrieClient, max_survey_symbols: int = 1200, max_tokens: int = 1500, ) -> TaxonomyResult'
incoming_refs: 16
outgoing_refs: 3
---
<!-- trie:section symbol=trie/sync/taxonomy:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=d0206e1d809212ec6e9a7c7343df949e8a755ac7a8fe78dd81e7b248c263a456 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=orchestration -->
Manages role taxonomy derivation and persistence for architectural classification of code symbols.

- **Role taxonomy**: Fixed vocabulary fitted to a specific codebase that constrains how symbols are architecturally classified
- **Persistence**: Stored at `<triefacts.root>/role_taxonomy.json` in the committed artifact tree, not regenerable cache
- **Two-pass system**: First derives coherent vocabulary from codebase survey, then classifies every symbol against that fixed set
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:TAXONOMY_FILENAME fingerprint=4f1a753dd3d049a62ec8dc8d04e9af37c6aa26bc61620d7ba099a85bb5e7ae44 body_fp=5bb22f591510851ff34e7b454d13ad1157b8e50a8f5e89450252f7766af0f8c8 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=config -->
Filename for the persisted role taxonomy file.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Role fingerprint=37005627b79b0a919a77c83e93e0ff9ad5dfabc4d7d102cce3c7fa53d7216b6d body_fp=0734b1f5f97a7934ec3052b034a4527dbf09ed3cea680065ed1c6cd77e9e7f2f source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
## `class Role`

Represents a single architectural role with its name and description in the taxonomy.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy fingerprint=1d28e14bbd11830ab96acd0bc2efcb75c59a769fb59099a45cf635a74cd99c42 body_fp=499355a721dda6f2361d80c23856bf83fb6ecfcc0e16976d310398665d198626 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
## `class Taxonomy`

Holds a collection of architectural role definitions for the project.

- `roles`: Tuple of Role instances defining the project's role vocabulary
- `names()`: Returns list of role names extracted from the roles tuple
- `is_empty()`: Returns True if no roles are defined
- `to_json()`: Serializes taxonomy to JSON-compatible dictionary format
- `from_json()`: Class method that creates Taxonomy from JSON dictionary, normalizing role names to lowercase
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.names fingerprint=ba51d13709b7ad85dc5a95405322177721e76e22e36bfc8dff6e0bcbb367e49d body_fp=55f53459380aa31e2e3b9367b8e7efb80faafbbd8a589f81b1f094afcc792792 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
## `def names(self) -> list[str]`

Taxonomy.names returns a list of role names extracted from the taxonomy's roles.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.is_empty fingerprint=decc9836a222efc1d40ce77a47294c64f3c8e6c486a653212f67e15a0b382389 body_fp=be3bc9544a8e65ea93159c8c17b821c00370877105aaa515c97b30809bc4bef1 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
## `def is_empty(self) -> bool`

Returns whether the Taxonomy contains no roles.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.to_json fingerprint=f4a93b2933ee48fd50894f0719b7937299355f5b6c3fd0e56d603c6e39b8ae3f body_fp=7c5a111f79f64fbe216d1db5e3daad8e954f817fe276be0df9cf8f0cb715364e source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
## `def to_json(self) -> dict[str, object]`

Serializes the Taxonomy instance to a JSON-compatible dictionary representation.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.from_json fingerprint=a89877f1e6706796d73e6ae2381c90c6fa75c32971295e106e6d387b2daaef32 body_fp=d48bbbbeefd12b9db06fa7b0e93182665dd4c227570726ebdc29eaf75055b725 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
## `def from_json(cls, raw: dict[str, object]) -> Taxonomy`

Creates a Taxonomy instance from a JSON dictionary containing role definitions.

- Filters out entries missing a name after normalization
- Role names are automatically lowercased and stripped of whitespace
- Invalid or malformed role entries are silently skipped
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:taxonomy_path fingerprint=7d122b5676739e2d379f0a46fa19d14b347969feefd017d099986c8f6e594dca body_fp=b01ecfae7b7cd2ea155acd5adf8e267d6d881d03843fed9d23d73d2c87df01e8 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=config -->
## `def taxonomy_path(project_root: Path, config: Config) -> Path`

Returns the canonical filesystem path for the role taxonomy JSON file within the triefacts directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:load_taxonomy fingerprint=1a0a1fc86fd66a3a15f0d0adb14f814236d18eb4515426ef67826f3b94d488dc body_fp=d2a21874e68e7a95fdc51a1e58514b33ae4ce2d7ed132a8be96dd998cb183c8f source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=persistence -->
## `def load_taxonomy(project_root: Path, config: Config) -> Taxonomy | None`

Loads the role taxonomy from the persisted JSON file, returning None if the file is missing or malformed.

- Returns `None` for any read error, invalid JSON, or empty taxonomy to trigger re-derivation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:save_taxonomy fingerprint=6a5d0c1214c0931f450c591b40caa5549710b6f2c549cfb91ff78a9e2fdb6f6e body_fp=e69379c72b5c5b5f54242d6df2dd34baa4b4bc94c8acc1018b2253378efd7a4f source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=persistence -->
## `def save_taxonomy(project_root: Path, config: Config, taxonomy: Taxonomy) -> Path`

Writes the taxonomy to its canonical filesystem path, creating parent directories as needed.

- Returns the path where the taxonomy was saved
- Creates parent directories if they don't exist
- Saves taxonomy as pretty-printed JSON with newline terminator
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:TAXONOMY_SYSTEM_PROMPT fingerprint=cd873d4b8a5be440701aaec446ebd85916825d57b027f5a7d362cf955f2e4993 body_fp=9a655f355f882b8ac252a85c80e038c49b6a5c44d62e4f99ccb8a39354d6f0b3 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=config -->
System prompt instructing the LLM to design a codebase-specific role vocabulary from a symbol survey.

- Requests 6-14 distinct, non-overlapping roles based on architectural function
- Emphasizes fitting vocabulary to actual codebase concerns rather than generic categories
- Specifies role naming convention: short, lowercase, hyphenated if two words
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:TaxonomyResult fingerprint=3a1dc478e71b5f787dc44a9138de4a8feaad0f8becd9618cdf4b94ce88eb0f65 body_fp=edd4e6647f6b777456107af57df22508959593bc03b193a388683b18636603ce source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
## `class TaxonomyResult`

Encapsulates the result of deriving a role taxonomy from codebase survey, including token usage metrics.

- `cache_creation_input_tokens`: tokens used for creating model cache during derivation
- `cache_read_input_tokens`: tokens used for reading from model cache during derivation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:derive_taxonomy fingerprint=5019174525678711d1fe2ebb91896361a90a2acbae82937d873ad209df0defeb body_fp=0e1f0eeb5afaa18d942fbf1fc8abbd1e4ab8e48a7722586bb1ae3504b5d03a78 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=orchestration -->
## `def derive_taxonomy( *, store: Store, client: TrieClient, max_survey_symbols: int = 1200, max_tokens: int = 1500, ) -> TaxonomyResult`

Surveys the codebase symbols and prompts a model to propose a fitted role vocabulary taxonomy.

- `max_survey_symbols`: cap on survey size to bound prompt length
- `max_tokens`: maximum tokens for model response
- Samples symbols with even stride when survey exceeds the cap
- Returns taxonomy with token usage metrics but does not persist results
<!-- trie:end -->