---
trie_version: 0.3.0
source: trie/parse/go.py
file_fingerprint: d0f7dc6a234a525c3c095eefe9a8662ceb2ea587551aad14d2652f19daae7b66
last_synced_at: '2026-08-02T21:19:38Z'
description: "Go language backend \u2014 tree-sitter symbols + references, paired with gopls."
defines:
- kind: module
  qualified_name: trie/parse/go:__module__
  lines: 1-366
- kind: constant
  qualified_name: trie/parse/go:GO_LANGUAGE
  lines: 31-31
- kind: function
  qualified_name: trie/parse/go:_make_parser
  lines: 34-37
  signature: def _make_parser() -> Parser
- kind: function
  qualified_name: trie/parse/go:_node_text
  lines: 40-41
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/go:_hash
  lines: 44-45
  signature: 'def _hash(s: str) -> str'
- kind: function
  qualified_name: trie/parse/go:_module_key
  lines: 48-50
  signature: 'def _module_key(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/go:_signature_text
  lines: 53-57
  signature: 'def _signature_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/go:_is_public_go
  lines: 60-62
  signature: 'def _is_public_go(name: str) -> bool'
- kind: function
  qualified_name: trie/parse/go:_receiver_type
  lines: 65-74
  signature: 'def _receiver_type(method_node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/go:_rightmost_type_identifier
  lines: 77-84
  signature: 'def _rightmost_type_identifier(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/go:_make_symbol
  lines: 87-116
  signature: 'def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/go:extract_symbols
  lines: 119-209
  signature: 'def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/go:_find_node_for_symbol
  lines: 212-233
  signature: 'def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None'
- kind: function
  qualified_name: trie/parse/go:_collect_call_names
  lines: 236-256
  signature: 'def _collect_call_names(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/go:extract_file_data
  lines: 259-292
  signature: 'def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData'
- kind: constant
  qualified_name: trie/parse/go:GO_SYSTEM_PROMPT
  lines: 295-304
- kind: class
  qualified_name: trie/parse/go:GoBackend
  lines: 307-362
  signature: class GoBackend
- kind: method
  qualified_name: trie/parse/go:GoBackend.__init__
  lines: 313-315
  signature: def __init__(self) -> None
- kind: method
  qualified_name: trie/parse/go:GoBackend.extract_file_data
  lines: 317-338
  signature: def extract_file_data(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/go:GoBackend.extract_symbols
  lines: 340-341
  signature: def extract_symbols(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/go:GoBackend.source_suffix
  lines: 343-344
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/go:GoBackend.system_prompt
  lines: 346-347
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/go:GoBackend.resolver
  lines: 349-362
  signature: def resolver(self)
- kind: constant
  qualified_name: trie/parse/go:__all__
  lines: 365-365
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=trie/parse/go:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=500e3e3db544d7136405b64a481dbfa9afa72818cbbfb3eb99daf75eb1cff5b0 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
Go language backend module providing tree-sitter-based symbol extraction and reference resolution, paired with gopls for method dispatch.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GO_LANGUAGE fingerprint=c457bd466d6b15171bdeac093d9cc60637d728221a25ed6488577e8ea1a8a390 body_fp=4101e4cb875e61643197507ac4f5b7b38fb6c5e437f7af2561b6604655d3f059 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
Module-level `tree_sitter.Language` instance initialised from the `tree_sitter_go` grammar, shared by all parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_make_parser fingerprint=4b7ecc412cec85f6a71881fe94705aba761469dd6cd0ccc05169ae3bbf0812f6 body_fp=d610e9246a6c6c85c9d182448dd057290e6e4e174b738337aba5668778e84b74 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _make_parser() -> Parser`

Create and return a `Parser` instance configured with `GO_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=1ba40df0de11d2cf3a4bf193503a292b59d17efab71ca874f459f8fc6ae8e792 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the byte slice of `source` spanned by `node` into a UTF-8 string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=6669477292c01bece7ef1f4345e604d994c8aba94e5f3aa365f05018167230e1 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=6a04ede280853fcbeb33be751e29610714bb89bf17bd260b659dc311016584f5 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _module_key(file_path: Path, source_root: Path) -> str`

Compute the module key for a file by returning its path relative to `source_root`, with the file extension stripped.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_signature_text fingerprint=caeebf96a4fca6581c08bcac31d81ca582afda6da9480f204a783b2505fcc244 body_fp=9763f1aac1c7581d4907b63c6cdb58a0466e2763e8456fd65a7f6c80e1acb3bb source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def _signature_text(node: Node, source: bytes) -> str`

Extract the declaration header of a tree-sitter node as a string, stopping before the body block.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_is_public_go fingerprint=2b77a07b537f87a530a80b5b35e6b9893926e31046c8c1dbefc65b7bf6834d69 body_fp=a613bc24d92b49cdd55c84a8ee70850f42eb8e944325570f72de7e0c5a91bcb1 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _is_public_go(name: str) -> bool`

Return `True` if `name` is a Go-exported identifier (non-empty and starts with an uppercase letter).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_receiver_type fingerprint=73bca43e3ecdb61fc22159bd22dd675636e295deef5a6ba5b7339b910d48101e body_fp=7e57df55246af5e0a06639667a84fea3f203168b58c76fea8e8935bac323bfe4 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def _receiver_type(method_node: Node, source: bytes) -> str | None`

Extract the receiver type name from a `method_declaration` node, handling both pointer and value receivers.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_rightmost_type_identifier fingerprint=c8583d2162ecc1ff89b64518a4bf277b705562ed1997c2948ac144af49e48a0c body_fp=229327ff04acb12fa6d15816ef050aa8ccfa76a3bfd7bebe479daac698b1f8c5 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def _rightmost_type_identifier(node: Node, source: bytes) -> str | None`

Recursively searches a tree-sitter node's named children in reverse to return the rightmost `type_identifier` text, or `None` if absent.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_make_symbol fingerprint=cafbdc588af8bdfbab920659d15982b57335a4f033437ff3f885e19fd8834a7d body_fp=c9078939365213a0576fbd7af11753ff9f2ec645d132f2856e364772028ffa56 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, parent: str | None = None, ) -> Symbol`

Construct a `Symbol` from a tree-sitter `Node`, computing its qualified name, signature, body text, hashes, and visibility.

- `parent`: receiver type name for methods; `None` for top-level declarations.
- `is_public`: `True` only when both `name` and `parent` (if present) are Go-exported (uppercase-initial).
- `docstring`: always `None` (not extracted in v1).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:extract_symbols fingerprint=3ff72c6d3fda81903690a43c5a0850294968df5a04bc40217fdbe6d74824ec6f body_fp=350b6bf459e71e92ef7bf3d7ceea97cd7bdfcc228a87f6dcd6a281e75fa268dd source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse a Go source file with tree-sitter and return `Symbol` objects for all top-level functions, methods, types, interfaces, constants, and variables.

- `source_text`: if provided, parsed directly instead of reading `file_path` from disk.
- `source_root`: defaults to `file_path.parent`; used to compute relative paths and `module_key`.
- Struct type declarations emit kind `"class"`; interface declarations emit `"interface"`; other type specs emit `"type"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_find_node_for_symbol fingerprint=0224069ed8592575a6194c18c1854a946e31f220c4654521c0eb37e1dd2ff14b body_fp=7ed5fc6787e9867645248482181747d8ac6d950d3cbd2fa825fb8b95c271cd1a source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None`

Walk `root` depth-first and return the first declaration node whose start line matches `sym.start_line`, or `None` if not found.

- Matches node types: `function_declaration`, `method_declaration`, `type_spec`, `const_spec`, `var_spec`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:_collect_call_names fingerprint=97519eb37edbaedbec2943ebc7225eeda41913fd228e59bb5b9055bff53a9f96 body_fp=56d281d4c9e6a2db04bb6e8736e6407007b171e20df80f6545bf47e5e04ab782 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def _collect_call_names(node: Node, source: bytes) -> set[str]`

Walk a tree-sitter `Node` recursively and collect all called identifier names, extracting the bare name for direct calls and the field name for selector calls.

- Skips comments and string literals to avoid false positives.
- Returns only the callee name, not the receiver; `x.M()` yields `"M"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:extract_file_data fingerprint=171d78ac5a79640148c191eb968fe9df360d6dd3d297ee75a88326fd639035af body_fp=747ff31b997218302e383af162d3d214a289b234b87ea2a17c6f372ae996c955 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=parsing -->
## `def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a Go file and return all extracted symbols plus deduplicated `"calls"` reference edges to top-level symbols within the same file.

- `source_root`: defaults to the file's parent directory if omitted.
- References are tree-sitter-only; method-dispatch edges require the `GoBackend` + gopls path.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GO_SYSTEM_PROMPT fingerprint=49ab3ffb3bfa6358f80f6d58370c2bdb7808b3d4ae2ab8487f3a1d9c08f355a8 body_fp=7e821d7ba143342811ebbb6a3b1282489e8a684d65edf4b8103dbca8cf4bf968 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
System prompt string injected into LLM documentation requests for Go symbols, guiding per-kind (func/method/type) description style.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend fingerprint=82c2bf8ac4bba16089fd8eb49f3a2cd87b4f014e2e18aff79a6c35ee0fae0895 body_fp=7e3d3c9ffc1854afbc89b25d8529ba0910e7052b62673550d0a2e332e0535c38 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
## `class GoBackend`

`LanguageBackend` implementation for Go that combines tree-sitter structural extraction with a lazily-initialised gopls `LspResolver` for method-dispatch edges.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is passed; merges gopls references into tree-sitter results when a resolver is available.
- `resolver()`: builds the `LspResolver` once on first call; skips it if `TRIE_DISABLE_RESOLVER=1`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=2188168c427c6070ac7bce34dc7d783adb76e2e6d583c203726d7eb5bc94a00d source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
## `def __init__(self) -> None`

Initialises `GoBackend` with `_resolver` set to `None` and `_resolver_built` flag set to `False`, deferring gopls resolver construction to first use.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=adcdb43803f0f0394958bfaa95d393db2290324a45e178b545e2f897066b2924 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=orchestration -->
## `def extract_file_data(self, file_path, source_root=None, *, source_text=None)`

Extract symbols and references for a Go file via `GoBackend`, merging tree-sitter edges with gopls-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if supplied.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=750ade4577ec69f13af368d3fc2c0901b9ab3d373f3f5714aa457cede5b7dedf source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=api -->
## `def extract_symbols(self, file_path, source_root=None, *, source_text=None)`

Delegates `GoBackend` symbol extraction to the module-level `extract_symbols` function.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.source_suffix fingerprint=dfe93906f787f83d8e88cf2dea2d3cf0489911aa06d7e7a33de8e3a97407b3c4 body_fp=c639d884025667b011f456435f5ddfe1486b234452a5d4d94a7104a6fa442b9f source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=util -->
## `def source_suffix(self) -> str`

Returns the file extension `".go"` for `GoBackend`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.system_prompt fingerprint=1d09be814896835261426d67e0ebd501e7d4034111a09a2f2f7e6662ba58f979 body_fp=cd5c3772f043485b894ac7e493127d4eacf07f3b49ce79caf0c3d63f278baadd source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=api -->
## `def system_prompt(self) -> str`

Returns the `GO_SYSTEM_PROMPT` constant string used to guide LLM documentation of Go symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:GoBackend.resolver fingerprint=b32248646eae7c251de744d08c0cf5961e5ac5931e8fb6f59498b6f75de029bf body_fp=08a47e939a842a582a24fe4b509492f0e7fb8e2a5f3ad8a05daed81623173426 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=domain -->
## `def resolver(self)`

Lazily initialises and returns `GoBackend`'s `LspResolver`, or `None` if `TRIE_DISABLE_RESOLVER=1` or `go_spec()` returns `None`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/go:__all__ fingerprint=13506e3717e93887edd000b3513b65d67ce9aae0d0eb8e3863dca495f28e22c1 body_fp=5f65e08b19929c3cb3c5cbdb0147ab400e3cef11c9c872dbc297d930a5635523 source_ref=31fdce4c3c1c3404aed37f51a74792db9e712a33 role=config -->
Declares the public API of `trie/parse/go`, exporting `GO_SYSTEM_PROMPT`, `GoBackend`, `extract_file_data`, and `extract_symbols`.
<!-- trie:end -->