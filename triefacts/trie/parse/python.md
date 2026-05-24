---
trie_version: 0.1.2
source: trie/parse/python.py
file_fingerprint: 6cc182c49cdbbec0046c0972db86bdad4bbbcfaa64c0c1ee1e6da2c2fa823edd
last_synced_at: '2026-05-23T23:45:57Z'
defines:
- kind: module
  qualified_name: trie/parse/python:__module__
  lines: 1-563
- kind: constant
  qualified_name: trie/parse/python:PY_LANGUAGE
  lines: 10-10
- kind: class
  qualified_name: trie/parse/python:Symbol
  lines: 14-28
- kind: function
  qualified_name: trie/parse/python:_make_parser
  lines: 31-34
- kind: function
  qualified_name: trie/parse/python:_node_text
  lines: 37-38
- kind: function
  qualified_name: trie/parse/python:_module_key
  lines: 41-44
- kind: function
  qualified_name: trie/parse/python:_signature_text
  lines: 47-52
- kind: function
  qualified_name: trie/parse/python:_extract_docstring
  lines: 55-65
- kind: function
  qualified_name: trie/parse/python:_normalize_body_tokens
  lines: 68-86
- kind: function
  qualified_name: trie/parse/python:_hash
  lines: 89-90
- kind: function
  qualified_name: trie/parse/python:_build_symbol
  lines: 93-128
- kind: function
  qualified_name: trie/parse/python:_extract_decorators
  lines: 131-144
- kind: function
  qualified_name: trie/parse/python:_undecorate
  lines: 147-153
- kind: function
  qualified_name: trie/parse/python:_walk_class
  lines: 156-202
- kind: function
  qualified_name: trie/parse/python:extract_module_docstring
  lines: 205-223
- kind: function
  qualified_name: trie/parse/python:strip_string_literal
  lines: 226-244
- kind: function
  qualified_name: trie/parse/python:_build_constant_symbol
  lines: 247-291
- kind: function
  qualified_name: trie/parse/python:_is_dunder
  lines: 294-301
- kind: function
  qualified_name: trie/parse/python:_module_level_constant
  lines: 304-327
- kind: function
  qualified_name: trie/parse/python:_build_module_body_symbol
  lines: 330-413
- kind: function
  qualified_name: trie/parse/python:extract_symbols
  lines: 416-562
incoming_refs: 71
outgoing_refs: 0
---
<!-- trie:section symbol=trie/parse/python:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=78b972ab1135c82f1b23baec8a8ab88c0fa2ea0d010f9be0a3e3a48e29fcb4f5 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `trie/parse/python`

Parse Python source files into structured `Symbol` records using tree-sitter.

- `PY_LANGUAGE`: initialized tree-sitter Python `Language` instance used by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:PY_LANGUAGE fingerprint=0a5ea4e9caea43b2aff7986c2453aaf98a5439baa3303d103a6a59fb780f0c9c body_fp=01bc5706a16338d00d526be59788d0488ff2e3e7d9b69a078449dc942efbcd36 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `PY_LANGUAGE = Language(tree_sitter_python.language())`

Module-level tree-sitter `Language` instance for Python, used to configure the parser.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:Symbol fingerprint=67410b76908def7ec7521baef1e77f8fa17f7b64e4da871a7c1b3eac081c35e0 body_fp=9e77737fd585f022eb848cc4d5c72be729468fac61234a39717161e19f46b387 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `Symbol(qualified_name, kind, name, file_path, signature, docstring, body_text, body_normalized_hash, signature_hash, start_line, end_line, is_public, parent_class=None, decorators=())`

Immutable record representing a single extracted Python symbol from a source file.

- `qualified_name`: `"module_key:dotted.name"` format.
- `kind`: one of `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`.
- `file_path`: source-root-relative path, e.g. `"src/foo.py"`.
- `body_normalized_hash`: SHA-256 of comment-stripped, whitespace-normalised body tokens.
- `signature_hash`: SHA-256 of the signature text; used for change detection.
- `start_line` / `end_line`: 1-indexed, inclusive.
- `parent_class`: unqualified class name; set only for `kind="method"`.
- `decorators`: verbatim decorator lines, e.g. `("@classmethod",)`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_make_parser fingerprint=f081dfd6916c63e7cd485b9082a93717d76eda229f07a7d0259ca3c3aff9fcbc body_fp=26d6c8d49fad584e01a582ede18278fc4f4afc6c8ff51867a0176014e93e56ea source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_make_parser() -> Parser`

Construct and return a `Parser` configured with the Python tree-sitter language.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=2c55785e7fc7ead7e0f0fdfaf1aeb5592dee33e8a533a3225244cb9109245d70 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_node_text(node: Node, source: bytes) -> str`

Decode the source bytes spanned by `node` into a UTF-8 string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_key fingerprint=547f506083bc19722953e055c01a3da5c50856bd4d4b3dff9592f71eefc0121b body_fp=f517edb263618b23c2dbe1d57bbe4dd8828722015d9012bb9f05f4277079f089 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_module_key(file_path: Path, source_root: Path) -> str`

Return the source-root-relative path without extension, used as the module prefix in qualified names.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_signature_text fingerprint=70e588b1dfb009e89ea973b67e2c9a765a3e9957e8fe35814acf708586e52bd7 body_fp=7cbd03de602e56687262b1a44f5ca87fa67beac192795bcb4e598fd8d91d98aa source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_signature_text(node: Node, source: bytes) -> str`

Extract the header text of a `function_definition` or `class_definition` node, excluding the body and trailing colon.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_docstring fingerprint=776fa902c9dd74faa5590357a1f7ee2b3c2b6d355a41f01172c8db91ff0b127f body_fp=09b584403bd1eb353eaa6b8557b4d5ce8345cb0b5c8d179558270634ea2b6f66 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_extract_docstring(body_node: Node | None, source: bytes) -> str | None`

Extract the raw docstring literal from the first statement of a function or class body node.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_normalize_body_tokens fingerprint=ce7a5b27392e47868d004b637327812ae0ce542353d09513ad71e087b9dc6cae body_fp=720d545f831dfdcc40d5dd3529341ffb50dda5d63d7ae996b231ce6244990a54 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_normalize_body_tokens(node: Node | None, source: bytes) -> str`

Concatenate all leaf tokens from `node` into a single space-joined string, skipping comment nodes.

- `node`: if `None`, returns empty string immediately.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=adcd1b89732edf100e15dee0d3e5a78222056de9c0e455645fb7fe05612da5e2 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8 encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_symbol fingerprint=7d482d42fbd226f146d9fcf96ed152b3fc0ba990f0e8493c18fbbfca67db0119 body_fp=5d51dc1984b98703fdf1c0d88f2212142a297f8970fd41b932bdaaabc412f2bf source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_build_symbol(node, source, *, module_key, rel_file, parent, kind, parent_is_private=False, decorators=()) -> Symbol`

Construct a `Symbol` from a tree-sitter `function_definition` or `class_definition` node.

- `parent`: dotted prefix for `qualified_name`; also stored as `parent_class`.
- `parent_is_private`: forces `is_public=False` regardless of the symbol's own name.
- `kind`: passed through verbatim (e.g. `"function"`, `"method"`, `"class"`).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_extract_decorators fingerprint=01ebd6355fccde3b490881e44d30de807fef73abe19e94670494a122c1dd4d18 body_fp=f12a372fae1b1b461da4e33ac2351bf59669ed6c3a199f1717bc9c864507ab8f source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_extract_decorators(node: Node, source: bytes) -> tuple[str, ...]`

Extract verbatim decorator strings from a `decorated_definition` node.

- Returns `()` if `node` is not a `decorated_definition` or has no decorator children.
- Each entry is leading-whitespace-stripped decorator text, e.g. `"@classmethod"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_undecorate fingerprint=b1cd6642b3e8e0609907b3d1832a68f8329945f8efb185e0fde9651547ddec76 body_fp=bc00efb2e21f08b456e92394ff012eb47dd40bd0e9c6c63f8262ddaf70b5740b source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_undecorate(node: Node) -> Node`

Unwrap a `decorated_definition` node to its inner `function_definition` or `class_definition`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_walk_class fingerprint=e926a23785fb4cbfc49fd08c397167580a455fd3f59e9f6993b28170cd7b360c body_fp=368acd81685046e73776ce93a9edbce9d61963e4009e656a5ba27b4d7d878167 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_walk_class(class_node, source, *, module_key, rel_file, class_decorators=()) -> list[Symbol]`

Emit one `class` `Symbol` plus one `method` `Symbol` per direct method, one level deep.

- `class_is_private`: methods of a `_`-prefixed class inherit `is_public=False`.
- Nested classes are not recursed into; only `function_definition` children are captured.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_module_docstring fingerprint=a2c67b5e81f19fe45381a6ac03c6b5e9ebc676e4d257b241a9600f8ce15222aa body_fp=7ed151afecfc4460ab30fba40177ed4a23f622db7a171629c4fac236fec27e3d source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `extract_module_docstring(file_path: Path) -> str | None`

Parse a Python file and return its raw module-level docstring, including quote marks, or `None`.

- `file_path`: resolved and read from disk; not a source-text override path.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:strip_string_literal fingerprint=d97254e76c736cbb686dec07837358d8ca659d0925bee0c37861f53acb07029f body_fp=64a9fcc4c4e86773862a5ced5ecf496275c86ce1ba48a2380f52b2767657fb98 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `strip_string_literal(raw: str) -> str`

Strip quote delimiters and up to two leading prefix characters (`r`, `b`, `u`, `f`) from a Python string literal, returning the inner content with surrounding whitespace stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_constant_symbol fingerprint=1144abec1cfbde2447fcc8744f55915888eacaecc5ff1cea5114b4e662d1b56e body_fp=888a22837100c88bdf11fae83bc2021aeb37d4f086d5334a4c9eebd6bb02c45c source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_build_constant_symbol(node: Node, assignment_node: Node, target_name: str, source: bytes, *, module_key: str, rel_file: str) -> Symbol`

Build a `kind='constant'` `Symbol` for a module-level `NAME = value` assignment.

- `node`: the wrapping `expression_statement`; sets the line range.
- `assignment_node`: the inner `assignment` node; used for token-normalised body hash.
- `signature`: first line of the assignment only, truncated at the first newline.
- `is_public`: `True` for non-underscore names and dunders; `False` for other `_`-prefixed names.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_is_dunder fingerprint=81d0c40a6404dfb330a7b05e9d459cf47b4ea3d89ac0964b2792d40358fcc217 body_fp=13305c2f96276f642708c3f5ea52c6b4ec727b40903b95fe2a79a6af84b20c25 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_is_dunder(name: str) -> bool`

Return `True` if `name` is a dunder identifier (starts and ends with `__`, length > 4).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_module_level_constant fingerprint=1470a5b4b31cb494ecca61bdcf5be516af254dc79fde2fc404bbe5345a1d88f7 body_fp=2a4c218310626d430b0f9f1996bf1b49c64d3c3dbe9cfc6827b701091313fda0 source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_module_level_constant(node: Node, source: bytes) -> tuple[Node, str] | None`

Check whether `node` is a single-identifier assignment statement and return `(assignment_node, name)` or `None`.

- Skips tuple-unpacking and attribute-target assignments; only `identifier` left-hand sides match.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:_build_module_body_symbol fingerprint=1910e1890486d83c8a17a98dabde20916177931683219cf50e4edebe4d8cfeab body_fp=7cf6a19d64a88f3f645b45abbd9119c102d84cd780dc2b6583c9b7584ee5c35c source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `_build_module_body_symbol(tree_root, source, *, module_key, rel_file, consumed_ranges, noise_ranges=None) -> Symbol | None`

Build a synthetic `kind='module'` symbol from residual module-level lines not claimed by any extracted symbol.

- `consumed_ranges`: `(start_line, end_line)` pairs for already-extracted symbols; these lines are excluded.
- `noise_ranges`: lines for imports and the module docstring; also excluded.
- Returns `None` when no non-blank, non-comment residual lines remain.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/python:extract_symbols fingerprint=7649dc31526e2e9955a047b483cf348d394b8861d4c34dc940800b91ac0f0ad3 body_fp=a2871cc5c2af51d9df9ba64199b3745d6aa8e097bc28faecec82974c469dd33e source_ref=5e8d03050d1b221cab9968d16c6e9555575ee417 -->
## `extract_symbols(file_path: Path, source_root: Path | None = None, *, source_text: str | None = None) -> list[Symbol]`

Parse a Python file and return all top-level `Symbol` objects, sorted by source line.

- `source_root`: controls `qualified_name` prefix and stored `file_path`; defaults to file's parent.
- `source_text`: parses this string instead of reading disk; qualified names still use `file_path`.
- Emits `kind` values: `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`.
- Deduplicates by `qualified_name`, last definition wins (handles `@overload` and `@property`/setter pairs).
- Appends a synthetic `__module__` symbol for residual module-level code not claimed by other symbols.
<!-- trie:end -->