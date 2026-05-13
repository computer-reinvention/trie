---
trie_version: 0.1.0
source: trie/parse/python.py
file_fingerprint: 9030494455ceb54707d181a941297997d2ef7d02e4d9d6ed62ed1681a2cd9c96
last_synced_at: '2026-05-12T18:29:59Z'
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
<!-- trie:section symbol=trie/parse/python:Symbol fingerprint=d9bc6c2e7a7f2bbdca9af4f1c7982a826342217f984a3fec7cdd6b475bf8a35e body_fp=fe0d3c53e575be2b7662c8cea86f640184b73d18d0384496c8a660c2f8b0f9be -->
## `Symbol`

Frozen dataclass representing a single extracted Python symbol with identity, source location, and content hashes.

- `qualified_name`: `"module_key:dotted.name"` format
- `kind`: one of `"function"`, `"class"`, or `"method"`
- `file_path`: source-root-relative path string
- `body_normalized_hash`: SHA-256 of comment-stripped token stream; used for change detection
- `signature_hash`: SHA-256 of the `def`/`class` header line
- `start_line` / `end_line`: 1-indexed, inclusive
- `is_public`: `False` if name starts with `_` or enclosing class is private
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=1f9a4f969b09026fbc88b8dfdfbe4a8ff3dfd1581576d60ff9d0c123ccefc62b -->
## `extract_module_docstring(file_path: Path) -> str | None`

Parse a Python file and return its module-level docstring literal, or `None`.

- Returns raw text including surrounding quote marks; callers must strip delimiters.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=106831a44be3bf07323d2a8c3f3d6a97a343e7c2ecfce9e153291df34b5342c4 -->
## `strip_string_literal(raw: str) -> str`

Strip Python string-literal delimiters and leading `f`/`r`/`b`/`u` prefixes, returning trimmed content.

- `raw`: raw text of a tree-sitter `string` node, including quotes and any prefix.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=74c692ca103dc04ce6e5539f1c7a2068961cb9451642861cf10476095691e005 body_fp=ac2ff638cabe586e0b5b7ec176cab0a7fa781fc0f98693804547dcdc7bdb2f37 -->
## `extract_symbols(file_path: Path, source_root: Path | None = None) -> list[Symbol]`

Parse a Python file and return deduplicated top-level functions, classes, and methods.

- `source_root`: sets the qualified-name prefix; defaults to the file's parent directory.
- Duplicates (e.g. `@overload`, `@property`/setter) resolved last-wins by source order.
<!-- trie:end -->