---
trie_version: 0.1.0
source: trie/parse/python.py
file_fingerprint: 9030494455ceb54707d181a941297997d2ef7d02e4d9d6ed62ed1681a2cd9c96
last_synced_at: '2026-05-14T17:27:07Z'
defines:
- kind: class
  qualified_name: trie/parse/python:Symbol
  lines: 14-26
- kind: function
  qualified_name: trie/parse/python:extract_module_docstring
  lines: 174-192
- kind: function
  qualified_name: trie/parse/python:strip_string_literal
  lines: 195-213
- kind: function
  qualified_name: trie/parse/python:extract_symbols
  lines: 216-253
incoming_refs: 38
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/python:Symbol fingerprint=d9bc6c2e7a7f2bbdca9af4f1c7982a826342217f984a3fec7cdd6b475bf8a35e body_fp=5f8b8bb5f31b2a6cbbba2754e7fb6267b961927dfa480a2a38d869c0610ce579 -->
## `Symbol`

Immutable dataclass representing a parsed Python symbol (function, class, or method) with identity, source location, and content hashes.

- `qualified_name`: `"module_key:dotted.name"` format
- `body_normalized_hash`: SHA-256 of comment-stripped body tokens; used for change detection
- `signature_hash`: SHA-256 of the definition header text
- `start_line` / `end_line`: 1-indexed, inclusive
- `is_public`: `False` if name starts with `_` or enclosing class is private
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=047ffff55c673abc852162f5737e9c5f09324a46801a9e33bf0e63826672d3f3 -->
## `extract_module_docstring(file_path: Path) -> str | None`

Parse a Python file and return the module-level docstring literal text, or `None`.

- Returns raw string including quote marks; callers must strip delimiters.
- Only the first statement is considered, per PEP 257.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=99067afec1280fd06516bbf5f87a4db4d6381d02374f8bea519a807098efb0b7 -->
## `strip_string_literal(raw: str) -> str`

Strip Python string-literal delimiters and leading `f`/`r`/`b`/`u` prefix from a tree-sitter `string` node's text.

- `raw`: raw node text including quotes and optional prefix characters
- Returns inner content with surrounding whitespace stripped
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=74c692ca103dc04ce6e5539f1c7a2068961cb9451642861cf10476095691e005 body_fp=b0ad967bf299a9fb5399f6a1faee1f50030ad119af297bf23ade86f9921da9f8 -->
## `extract_symbols(file_path: Path, source_root: Path | None = None) -> list[Symbol]`

Parse a Python file and return all top-level functions, classes, and class methods as `Symbol` objects.

- `source_root`: determines `qualified_name` prefix and stored `file_path`; defaults to `file_path.parent`.
- Duplicate `qualified_name` entries (e.g. `@overload`, `@property`/setter) are resolved last-wins.
<!-- trie:end -->