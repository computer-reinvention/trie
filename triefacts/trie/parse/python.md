---
trie_version: 0.1.2
source: trie/parse/python.py
file_fingerprint: c2775380973fba4b65ee337b5d0c97b9e5ff75611d5d95cb7e52010e063344c4
last_synced_at: '2026-05-19T10:41:32Z'
defines:
- kind: module
  qualified_name: trie/parse/python:__module__
  lines: 1-522
- kind: constant
  qualified_name: trie/parse/python:PY_LANGUAGE
  lines: 10-10
- kind: class
  qualified_name: trie/parse/python:Symbol
  lines: 14-26
- kind: function
  qualified_name: trie/parse/python:_make_parser
  lines: 29-32
- kind: function
  qualified_name: trie/parse/python:_node_text
  lines: 35-36
- kind: function
  qualified_name: trie/parse/python:_module_key
  lines: 39-42
- kind: function
  qualified_name: trie/parse/python:_signature_text
  lines: 45-50
- kind: function
  qualified_name: trie/parse/python:_extract_docstring
  lines: 53-63
- kind: function
  qualified_name: trie/parse/python:_normalize_body_tokens
  lines: 66-84
- kind: function
  qualified_name: trie/parse/python:_hash
  lines: 87-88
- kind: function
  qualified_name: trie/parse/python:_build_symbol
  lines: 91-123
- kind: function
  qualified_name: trie/parse/python:_undecorate
  lines: 126-132
- kind: function
  qualified_name: trie/parse/python:_walk_class
  lines: 135-171
- kind: function
  qualified_name: trie/parse/python:extract_module_docstring
  lines: 174-192
- kind: function
  qualified_name: trie/parse/python:strip_string_literal
  lines: 195-213
- kind: function
  qualified_name: trie/parse/python:_build_constant_symbol
  lines: 216-260
- kind: function
  qualified_name: trie/parse/python:_is_dunder
  lines: 263-270
- kind: function
  qualified_name: trie/parse/python:_module_level_constant
  lines: 273-296
- kind: function
  qualified_name: trie/parse/python:_build_module_body_symbol
  lines: 299-382
- kind: function
  qualified_name: trie/parse/python:extract_symbols
  lines: 385-521
incoming_refs: 57
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

<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=5a04917b0c9ad3d9b644201367ea96dfc21cd1ed82598e08eae81c0660e1fa13 body_fp=f3e8aa462bd67c3173fbee9450a98bd8c4a90fb09ceef15516e43b7a96f0253d source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `extract_symbols(file_path: Path, source_root: Path | None = None, *, source_text: str | None = None) -> list[Symbol]`

Parse a Python file and return all top-level symbols as `Symbol` objects.

- Returns four kinds: `function`, `class`+`method`, `constant` (module-level `NAME = value`, including dunders), and a synthetic `module` symbol (`__module__`) for residual top-level code not captured by the others.
- `source_root`: sets qualified-name prefix and stored `file_path`; defaults to `file_path.parent`.
- `source_text`: overrides disk read; lets callers parse a prior version while keeping current-file qualified names.
- Deduplicates by `qualified_name`; last definition wins (handles `@overload` and `@property`/setter pairs).
- The `__module__` symbol is omitted when no non-import, non-docstring residual lines remain.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_make_parser fingerprint=f081dfd6916c63e7cd485b9082a93717d76eda229f07a7d0259ca3c3aff9fcbc body_fp=a52c1ef2381629555a85de265f653bc194c110e852d66983c1c24ee7ad3e379b source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_make_parser() -> Parser`

Create and return a `Parser` configured with the Python tree-sitter language.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=f6db3e4fea545760e97d909ad4e2c88eed57b4c891928f530c05ea80f15be377 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_node_text(node: Node, source: bytes) -> str`

Decode and return the source slice covered by `node`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_module_key fingerprint=547f506083bc19722953e055c01a3da5c50856bd4d4b3dff9592f71eefc0121b body_fp=63616b8f8be460e262f974968efcc7f4ca090be080dc1f3e7b494717ae6de52d source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_module_key(file_path: Path, source_root: Path) -> str`

Return the dot-path module key used in qualified names, e.g. `src/foo`.

- **return**: file path relative to `source_root`, extension stripped
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_signature_text fingerprint=70e588b1dfb009e89ea973b67e2c9a765a3e9957e8fe35814acf708586e52bd7 body_fp=529a48012dcc7dd8167971bde51636739d4fcc18a5c8e6da322eafdd686cd89c source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_signature_text(node: Node, source: bytes) -> str`

Extract the header text of a `function_definition` or `class_definition`, excluding the body and trailing colon.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_extract_docstring fingerprint=776fa902c9dd74faa5590357a1f7ee2b3c2b6d355a41f01172c8db91ff0b127f body_fp=08d4c0e64bbef1973f792c66ce6446d11a4eb69fbb84bbdc462b8c538df638c2 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_extract_docstring(body_node: Node | None, source: bytes) -> str | None`

Return the raw docstring string node text from the first statement of a function or class body, or `None`.

- `body_node`: the `body` field node of a `function_definition` or `class_definition`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_normalize_body_tokens fingerprint=ce7a5b27392e47868d004b637327812ae0ce542353d09513ad71e087b9dc6cae body_fp=acca6eba04df32a181256ec7b42be97ce416e5ebcb5b33ec0176b9f7fa1c9a0c source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_normalize_body_tokens(node: Node | None, source: bytes) -> str`

Concatenate all leaf-token texts from a syntax node, skipping comments, for change-detection hashing.

- `node`: if `None`, returns empty string.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=adcd1b89732edf100e15dee0d3e5a78222056de9c0e455645fb7fe05612da5e2 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8 encoded string.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_build_symbol fingerprint=799765dd272492eadd4d11bb7859bcb5b442578915c6808c9f27bdf78ebe76e6 body_fp=56b45c4c2a90d10aef8e68e8d1ce00c3f3628677c21777c0b34299892a6ca206 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_build_symbol(node, source, *, module_key, rel_file, parent, kind, parent_is_private=False) -> Symbol`

Construct a `Symbol` dataclass from a tree-sitter `function_definition` or `class_definition` node.

- `parent`: dotted name prefix; `None` for top-level symbols.
- `parent_is_private`: marks the symbol non-public regardless of its own name.
- `is_public`: `False` if name starts with `_` or `parent_is_private` is set.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_undecorate fingerprint=b1cd6642b3e8e0609907b3d1832a68f8329945f8efb185e0fde9651547ddec76 body_fp=587bc2e86deae9e74d2aa7df1ac9d5a1a8c60b1621b90409dcf85bf77c8946e6 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_undecorate(node: Node) -> Node`

If `node` is a `decorated_definition`, return the inner `def`/`class` node; otherwise return `node` unchanged.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_walk_class fingerprint=6f4b602e88e525913d8f14e2424638caeb5799e66d1c8c44fe8f0235633448cf body_fp=a6278817449ea8b5948d7c9d7465d7073ce63aba3433317348cdea7a7c7b2de1 source_ref=9ef40d21b0e2845b12219ed57628ec87f9eb4293 -->
## `_walk_class(class_node: Node, source: bytes, *, module_key: str, rel_file: str) -> list[Symbol]`

Emit the class symbol plus one level of method symbols for a `class_definition` node.

- `parent_is_private`: methods of a `_Foo` class inherit the private flag.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:PY_LANGUAGE fingerprint=0a5ea4e9caea43b2aff7986c2453aaf98a5439baa3303d103a6a59fb780f0c9c body_fp=a2c2a0c1f645dbfc4fe4d20a8a43b9d895aabc14e7107a08d51e7aaa6e364c0a source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `PY_LANGUAGE = Language(tree_sitter_python.language())`

Module-level tree-sitter `Language` instance for Python, used to configure parsers.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_build_constant_symbol fingerprint=1144abec1cfbde2447fcc8744f55915888eacaecc5ff1cea5114b4e662d1b56e body_fp=98a00ff26ad3252765bf58075fae31f9c55768ff412e468089801c6a1ae2e782 source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `_build_constant_symbol(node: Node, assignment_node: Node, target_name: str, source: bytes, *, module_key: str, rel_file: str) -> Symbol`

Build a `kind='constant'` Symbol for a module-level `NAME = value` assignment.

- `node`: wrapping `expression_statement`; sets the line range.
- `assignment_node`: inner `assignment` node; used for body-token normalisation.
- `target_name`: the identifier string on the left-hand side.
- Dunders (`__all__`, `__version__`) are marked `is_public=True` despite leading underscores.
- `signature` is the first line of the statement only; `body_text` is the full statement.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_is_dunder fingerprint=81d0c40a6404dfb330a7b05e9d459cf47b4ea3d89ac0964b2792d40358fcc217 body_fp=0cc548c4ad19f42cd74f9baf8c89f29302604d7ba74356bfe83a9a91376630c2 source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `_is_dunder(name: str) -> bool`

Return `True` if `name` is a dunder identifier (e.g. `__all__`, `__version__`).

- Requires `len(name) > 4` to exclude bare `____`.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_module_level_constant fingerprint=1470a5b4b31cb494ecca61bdcf5be516af254dc79fde2fc404bbe5345a1d88f7 body_fp=5aa0f649af2a720e09db485d5551006289f95409ea5978fdf5021b69a95e9b37 source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `_module_level_constant(node: Node, source: bytes) -> tuple[Node, str] | None`

Return `(assignment_node, name)` if `node` is a single-identifier top-level assignment, else `None`.

- Skips tuple unpacking and attribute-target assignments.
- `assignment_node`: the inner `assignment` node holding the right-hand side.
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:_build_module_body_symbol fingerprint=1910e1890486d83c8a17a98dabde20916177931683219cf50e4edebe4d8cfeab body_fp=004ecdac5d08671b82f46a3723fe11050dac0bdd50ae4a885aa9b73426b7d016 source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `_build_module_body_symbol(tree_root, source, *, module_key, rel_file, consumed_ranges, noise_ranges=None) -> Symbol | None`

Build a synthetic `kind='module'` symbol carrying residual module-level code not captured by any other symbol.

- `consumed_ranges`: line ranges already claimed by functions, classes, or constants.
- `noise_ranges`: line ranges of imports and the module docstring; also excluded.
- Returns `None` when no meaningful residual lines remain (blank, comment, or fully consumed).
<!-- trie:end -->

<!-- trie:section symbol=trie/parse/python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=623e75c61115d795321c9210eb23550a083efcab098cd518849856a733445d0c source_ref=c94a919b6dda52ca18b2bd62f9a0174e8c411a94 -->
## `python`

Parse Python source files into structured `Symbol` records using tree-sitter.

- `PY_LANGUAGE`: initialised tree-sitter Python language instance used by all parsers in this module.
<!-- trie:end -->