---
trie_version: 0.1.0
source: trie/parse/python.py
file_fingerprint: 31edbc721a78a215b976726fcab6efc9e315d463ccc73087f587cf164d5efd41
last_synced_at: '2026-05-14T19:38:59Z'
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
  lines: 216-264
incoming_refs: 44
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/python:Symbol fingerprint=d9bc6c2e7a7f2bbdca9af4f1c7982a826342217f984a3fec7cdd6b475bf8a35e body_fp=879c309a54165bf864d2ad851bebac172b40931735019bbda12c854e3ce53695 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `Symbol`

Frozen dataclass representing a single extracted Python symbol (function, class, or method).

- `qualified_name`: `"module/path:Dotted.Name"` format
- `body_normalized_hash`: SHA-256 of comment-stripped body tokens; used for change detection
- `signature_hash`: SHA-256 of the definition header, excluding the body
- `start_line` / `end_line`: 1-indexed, inclusive
- `is_public`: `False` if name starts with `_` or parent class is private
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=7a8c38450916eee77ffa934a2cec36fa46794ec5ed14791aa3ff78432b8ac732 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `extract_module_docstring(file_path: Path) -> str | None`

Return the module-level docstring literal (including quote marks) from a Python file, or `None`.

- `file_path`: resolved and read from disk; no `source_root` or override supported.
- Returns raw `string` node text; caller must strip delimiters via `strip_string_literal`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=66a67d1bf8e187b64ef156dfd53b6b1c963722101c7c4013ceec1d7d746a0dc5 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `strip_string_literal(raw: str) -> str`

Strip Python string-literal delimiters and leading prefix characters from a tree-sitter `string` node's text.

- `raw`: raw text including quote marks and optional `r/b/f/u` prefix
- Returns interior content with surrounding whitespace stripped
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=07b8cdbaa929d2a2494bcde5993404d850b1c67524fde1ad70f7d4d953c75c09 body_fp=984c378ca3038cc35fd209d5610e3c5b893044a76fb1e78dd10ec883e4ba5354 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `extract_symbols(file_path: Path, source_root: Path | None = None, *, source_text: str | None = None) -> list[Symbol]`

Parse a Python file and return all top-level functions, classes, and their methods as `Symbol` objects.

- `source_root`: sets qualified-name prefix and stored `file_path`; defaults to `file_path.parent`.
- `source_text`: overrides disk read; lets callers parse a prior version while keeping current-file qualified names.
- Deduplicates by `qualified_name`; last definition wins (handles `@overload` and `@property`/setter pairs).
<!-- trie:end -->