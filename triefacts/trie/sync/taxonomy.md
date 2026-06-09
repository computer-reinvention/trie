---
trie_version: 0.1.5
source: trie/sync/taxonomy.py
file_fingerprint: d3527d467b1f6425152def101ac74e20134e50463b409924616b4766de39edd3
last_synced_at: '2026-06-09T09:39:12Z'
description: 'Role taxonomy: the project-specific role vocabulary that constrains
  role tagging.'
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
- kind: class
  qualified_name: trie/sync/taxonomy:Taxonomy
  lines: 37-60
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.names
  lines: 40-41
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.is_empty
  lines: 43-44
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.to_json
  lines: 46-47
- kind: method
  qualified_name: trie/sync/taxonomy:Taxonomy.from_json
  lines: 50-60
- kind: function
  qualified_name: trie/sync/taxonomy:taxonomy_path
  lines: 63-65
- kind: function
  qualified_name: trie/sync/taxonomy:load_taxonomy
  lines: 68-84
- kind: function
  qualified_name: trie/sync/taxonomy:save_taxonomy
  lines: 87-92
- kind: constant
  qualified_name: trie/sync/taxonomy:TAXONOMY_SYSTEM_PROMPT
  lines: 95-109
- kind: class
  qualified_name: trie/sync/taxonomy:TaxonomyResult
  lines: 113-118
- kind: function
  qualified_name: trie/sync/taxonomy:derive_taxonomy
  lines: 121-172
incoming_refs: 14
outgoing_refs: 2
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
<!-- trie:section symbol=trie/sync/taxonomy:Role fingerprint=37005627b79b0a919a77c83e93e0ff9ad5dfabc4d7d102cce3c7fa53d7216b6d body_fp=86f3bf0b52a4b1c6d2843afdfce7ec342882f4c2fc215532873ed0b0b7de7388 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
Represents a single architectural role with its name and description in the taxonomy.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy fingerprint=1d28e14bbd11830ab96acd0bc2efcb75c59a769fb59099a45cf635a74cd99c42 body_fp=f78e2e6b51532f22ca9ddaa6b93884fd846c13c19b212b9123e3ee823614440d source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
Holds a collection of architectural role definitions for the project.

- `roles`: Tuple of Role instances defining the project's role vocabulary
- `names()`: Returns list of role names extracted from the roles tuple
- `is_empty()`: Returns True if no roles are defined
- `to_json()`: Serializes taxonomy to JSON-compatible dictionary format
- `from_json()`: Class method that creates Taxonomy from JSON dictionary, normalizing role names to lowercase
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.names fingerprint=ba51d13709b7ad85dc5a95405322177721e76e22e36bfc8dff6e0bcbb367e49d body_fp=c2ae3e90224f1caff9c7c795937b0e9e45a4b55c083445b9c3369b0033e75f1d source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
Taxonomy.names returns a list of role names extracted from the taxonomy's roles.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.is_empty fingerprint=decc9836a222efc1d40ce77a47294c64f3c8e6c486a653212f67e15a0b382389 body_fp=d1d0d70f393f3ff5685bd4b5c6e8b294f28ba4e0b0a9d9d29e86de00b81b9f52 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
Returns whether the Taxonomy contains no roles.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.to_json fingerprint=f4a93b2933ee48fd50894f0719b7937299355f5b6c3fd0e56d603c6e39b8ae3f body_fp=ee0664d572c340365ef0c7c438371e6dd4b9fffdd16a67c991084a987dcf5d55 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=util -->
Serializes the Taxonomy instance to a JSON-compatible dictionary representation.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:Taxonomy.from_json fingerprint=a89877f1e6706796d73e6ae2381c90c6fa75c32971295e106e6d387b2daaef32 body_fp=4d5a7820fe17f6e0c659f0a76250be955398a505ba686c0eae5d40869b2489af source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
Creates a Taxonomy instance from a JSON dictionary containing role definitions.

- Filters out entries missing a name after normalization
- Role names are automatically lowercased and stripped of whitespace
- Invalid or malformed role entries are silently skipped
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:taxonomy_path fingerprint=7d122b5676739e2d379f0a46fa19d14b347969feefd017d099986c8f6e594dca body_fp=9cca1fdc90cf5fb2a5ff9b2338776e0de415ec75e6301e9ff4d7c89255fd0e2c source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=config -->
Returns the canonical filesystem path for the role taxonomy JSON file within the triefacts directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:load_taxonomy fingerprint=1a0a1fc86fd66a3a15f0d0adb14f814236d18eb4515426ef67826f3b94d488dc body_fp=c986cd73c6cb0416f796ff012f75873bd2593841f8a85de399626ce95a4256d8 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=persistence -->
Loads the role taxonomy from the persisted JSON file, returning None if the file is missing or malformed.

- Returns `None` for any read error, invalid JSON, or empty taxonomy to trigger re-derivation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:save_taxonomy fingerprint=6a5d0c1214c0931f450c591b40caa5549710b6f2c549cfb91ff78a9e2fdb6f6e body_fp=5f57950fa5ce822b04a1aad9418da671ada58aaea1d3495dbdd4a3965dc50233 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=persistence -->
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
<!-- trie:section symbol=trie/sync/taxonomy:TaxonomyResult fingerprint=3a1dc478e71b5f787dc44a9138de4a8feaad0f8becd9618cdf4b94ce88eb0f65 body_fp=d99d6ce9cb9d86725e145a217a328dc73ed14396d364b4b712e40ec334263d4e source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=model -->
Encapsulates the result of deriving a role taxonomy from codebase survey, including token usage metrics.

- `cache_creation_input_tokens`: tokens used for creating model cache during derivation
- `cache_read_input_tokens`: tokens used for reading from model cache during derivation
<!-- trie:end -->
<!-- trie:section symbol=trie/sync/taxonomy:derive_taxonomy fingerprint=5019174525678711d1fe2ebb91896361a90a2acbae82937d873ad209df0defeb body_fp=ff239367165e64f15e7629e074aafb957063c9c6f803edde15a9f5f100d874a3 source_ref=2fcd5b9b1578ce16edcfc18d978e61f85989305c role=orchestration -->
Surveys the codebase symbols and prompts a model to propose a fitted role vocabulary taxonomy.

- `max_survey_symbols`: cap on survey size to bound prompt length
- `max_tokens`: maximum tokens for model response
- Samples symbols with even stride when survey exceeds the cap
- Returns taxonomy with token usage metrics but does not persist results
<!-- trie:end -->