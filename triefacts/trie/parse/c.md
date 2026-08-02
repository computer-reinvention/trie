---
trie_version: 0.3.0
source: trie/parse/c.py
file_fingerprint: 7cd0fc7a39a4881889459a47d626c693046112d93bbe7527e5563c2dfb89b076
last_synced_at: '2026-08-02T21:19:35Z'
description: "C language backend \u2014 tree-sitter symbols + references, paired with clangd."
defines:
- kind: module
  qualified_name: trie/parse/c:__module__
  lines: 1-311
- kind: constant
  qualified_name: trie/parse/c:C_LANGUAGE
  lines: 26-26
- kind: function
  qualified_name: trie/parse/c:_make_parser
  lines: 29-32
  signature: def _make_parser() -> Parser
- kind: function
  qualified_name: trie/parse/c:_node_text
  lines: 35-36
  signature: 'def _node_text(node: Node, source: bytes) -> str'
- kind: function
  qualified_name: trie/parse/c:_hash
  lines: 39-40
  signature: 'def _hash(s: str) -> str'
- kind: function
  qualified_name: trie/parse/c:_module_key
  lines: 43-45
  signature: 'def _module_key(file_path: Path, source_root: Path) -> str'
- kind: function
  qualified_name: trie/parse/c:_declarator_name
  lines: 48-61
  signature: 'def _declarator_name(node: Node, source: bytes) -> str | None'
- kind: function
  qualified_name: trie/parse/c:_is_static
  lines: 64-68
  signature: 'def _is_static(node: Node, source: bytes) -> bool'
- kind: function
  qualified_name: trie/parse/c:_make_symbol
  lines: 71-101
  signature: 'def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, is_public: bool = True, ) -> Symbol'
- kind: function
  qualified_name: trie/parse/c:extract_symbols
  lines: 104-166
  signature: 'def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]'
- kind: function
  qualified_name: trie/parse/c:_find_node_for_symbol
  lines: 169-191
  signature: 'def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None'
- kind: function
  qualified_name: trie/parse/c:_collect_call_names
  lines: 194-208
  signature: 'def _collect_call_names(node: Node, source: bytes) -> set[str]'
- kind: function
  qualified_name: trie/parse/c:extract_file_data
  lines: 211-238
  signature: 'def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData'
- kind: constant
  qualified_name: trie/parse/c:C_SYSTEM_PROMPT
  lines: 241-250
- kind: class
  qualified_name: trie/parse/c:CBackend
  lines: 253-307
  signature: class CBackend
- kind: method
  qualified_name: trie/parse/c:CBackend.__init__
  lines: 259-261
  signature: def __init__(self) -> None
- kind: method
  qualified_name: trie/parse/c:CBackend.extract_file_data
  lines: 263-283
  signature: def extract_file_data(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/c:CBackend.extract_symbols
  lines: 285-286
  signature: def extract_symbols(self, file_path, source_root=None, *, source_text=None)
- kind: method
  qualified_name: trie/parse/c:CBackend.source_suffix
  lines: 288-289
  signature: def source_suffix(self) -> str
- kind: method
  qualified_name: trie/parse/c:CBackend.system_prompt
  lines: 291-292
  signature: def system_prompt(self) -> str
- kind: method
  qualified_name: trie/parse/c:CBackend.resolver
  lines: 294-307
  signature: def resolver(self)
- kind: constant
  qualified_name: trie/parse/c:__all__
  lines: 310-310
incoming_refs: 0
outgoing_refs: 13
---
<!-- trie:section symbol=trie/parse/c:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3935bfa1436dd870c449a2bb50073189a3ec81e7b6fd1892b1634ded22f2b134 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
C language backend implementing tree-sitter-based symbol extraction and intra-file reference resolution, paired with clangd for cross-file references.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:C_LANGUAGE fingerprint=32ef11120cd687e0fd0a61aa2e4e23551b0308764ed782450d301e410ad9f674 body_fp=3b3575f06b2f58602551c66146e81e2e7c716f1395bca0779ff7b4c0ee95b190 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
Module-level `Language` instance initialised from the `tree_sitter_c` grammar, shared by all C parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_make_parser fingerprint=288e56b014eeadc77f04b64ce2ffcd8f39a1c09d80945692913650559938b042 body_fp=5cfc09b01e9829759712ef9039696d2654f36eadc1bd697a623afaed20834a33 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
## `def _make_parser() -> Parser`

Construct and return a `Parser` instance configured with `C_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=dfdee8bbbd77f46d1a576f3fbe5841f5b2f21a94a8ec2f50131a635d6b4b70a4 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
## `def _node_text(node: Node, source: bytes) -> str`

Decode the UTF-8 text of a tree-sitter `Node` from the raw `source` bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=6669477292c01bece7ef1f4345e604d994c8aba94e5f3aa365f05018167230e1 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
## `def _hash(s: str) -> str`

Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=a489a7b11c78c58a9153fd3ba306f80f19c3740a83758474230840edebd4fddf source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
## `def _module_key(file_path: Path, source_root: Path) -> str`

Compute the module key for a file by stripping its extension from its path relative to `source_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_declarator_name fingerprint=de84d761205b65e3fa1dd894c0dec702843714c9ccacf3bc50f108b9b0c66869 body_fp=c7f94bcdcb5f3b56f534e8a686b84e0ff423f7278188db80ca4034b9e3c4d9d5 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def _declarator_name(node: Node, source: bytes) -> str | None`

Recursively traverses nested pointer, array, and function declarator nodes to return the leaf identifier name, or `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_is_static fingerprint=3e7bf885277f29a383637b8b7c497a2184e628202e412f5a39ec7e33c72d9703 body_fp=173c7661846b031b1b1a6f31faa089704786b9f0e5b06d3e4b61c72304e564a1 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def _is_static(node: Node, source: bytes) -> bool`

Return `True` if the tree-sitter `node` has a `static` storage-class specifier among its named children.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_make_symbol fingerprint=20913a70c6667376e46c113e24a9dcb32c5a7df82a1ee70aeda376438e825ba5 body_fp=ad7531a4b65edc7db54828e79599d872103b4ec7afc60be3be68c4c5f5689ca8 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def _make_symbol( node: Node, source: bytes, *, module_key: str, rel_file: str, name: str, kind: str, is_public: bool = True, ) -> Symbol`

Construct a `Symbol` from a tree-sitter `Node`, extracting signature, body text, hashes, and line numbers.

- `module_key`: colon-prefixed namespace used to form `qualified_name`.
- `signature`: text before the body node if a body exists, else the full node text.
- `body_text`: inner body node text, or falls back to `signature` when no body is present.
- `docstring`: always `None` (C has no docstring convention).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:extract_symbols fingerprint=96375bc3e6986df40fed908d10bb21c67386c98fa70dc774958bf82b528ff8a2 body_fp=973fe7cdeb76452b52a30ca60aca23f88991d3f9531364d4dfe1ae4715b0f8be source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def extract_symbols( file_path: Path, source_root: Path | None = None, *, source_text: str | None = None, ) -> list[Symbol]`

Parse a C file (or provided source text) with tree-sitter and return a deduplicated list of top-level `Symbol` objects.

- `source_text`: if given, parsed directly instead of reading `file_path` from disk.
- `source_root`: used to compute module keys and relative paths; defaults to `file_path.parent`.
- Skips duplicate names; `static` symbols are emitted with `is_public=False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_find_node_for_symbol fingerprint=8867133b8e3fddce8207a725c1bcb9df7f220501a13fa64cc3501b1a272488d0 body_fp=fbaffb9648b360c1596b32de2612cd7057834fb4c6245f45f7b0c33a6f314190 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def _find_node_for_symbol(root: Node, sym: Symbol) -> Node | None`

Walk the tree-sitter `root` node tree to find the first top-level node whose start line matches `sym.start_line` and whose type is a recognised C declaration kind.

- Returns `None` if no matching node is found.
- Stops traversal immediately once a match is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_collect_call_names fingerprint=63942098d6e67671fdc1cadcef8e97335d99104aee119a73eb5a8f75df8ec65e body_fp=8780c45799341a5862704f3972c72187af768cf8f85942356f804187bec56905 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def _collect_call_names(node: Node, source: bytes) -> set[str]`

Recursively walk a tree-sitter `Node` and return the set of all direct function-call identifiers found, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:extract_file_data fingerprint=91a91c016ed50333ae09b5ac599f759217e794b3573ae0232e9ea70a46cf0b6d body_fp=9108b907d5d9bc4d2800f7ef20d5a380188dfd8eb22c3e6cfff632709c3c8b7a source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
## `def extract_file_data(file_path: Path, source_root: Path | None = None) -> FileData`

Parse a C file and return all its symbols plus intra-file `"calls"` references between them.

- `source_root`: defaults to the file's parent directory if omitted.
- References are only emitted for calls to symbols defined in the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:C_SYSTEM_PROMPT fingerprint=218b85dcbc3c31f4db53f192e2859e58b8131d055bd01909efa0ae9bcbc248ee body_fp=ee376e779bc6f8dbb8822eeaf7701d5b29c3ba0b166ae343721eee437ce6c24c source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
System prompt string passed to the LLM when generating documentation for C symbols in a code-navigation graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend fingerprint=50bcab3f7e61f7b627e80295b644062267af251dc16626958efff78fc329d57c body_fp=63ec4ba3ae91368d5c99641d3aa8954f9d954c78f20d6350939f92b6e822d9b8 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
## `class CBackend`

Implements the `LanguageBackend` interface for C source files, combining tree-sitter symbol extraction with optional clangd-backed reference resolution.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is supplied; merges clangd references when a resolver is available.
- `resolver()`: lazily builds an `LspResolver` from `c_spec()`; returns `None` if `TRIE_DISABLE_RESOLVER=1` or spec is unavailable.
- `extensions`: handles both `.c` and `.h` files.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=667fd30000a252d974b41174f0feaad22f99b86bf5706b18a7111c0b7ac4ada5 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=domain -->
## `def __init__(self) -> None`

Initialize `CBackend` with `_resolver` set to `None` and `_resolver_built` flag set to `False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=eeba2336fe8a852ed92c8c8b954217196fc0b11aa9a70dee9823c67d78079a45 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=orchestration -->
## `def extract_file_data(self, file_path, source_root=None, *, source_text=None)`

Extract symbols and references from a C file, merging in clangd-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if provided.
- Returns a `FileData` with clangd cross-reference edges merged, or the tree-sitter-only result if no resolver is configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=14fbdc28904cc82a98c318a07944e3e36c9e159a80d39d23446045fc60308924 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
## `def extract_symbols(self, file_path, source_root=None, *, source_text=None)`

Delegates `CBackend.extract_symbols` to the module-level `extract_symbols` function unchanged.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.source_suffix fingerprint=68febd0fdec6b8e80b89cba64f0353078ade4b7310d55ed05faed3c5bdcf163a body_fp=268ac7241b20a72177df17fb9eb2ec9d6e1dc3f73b595cfde53e53d85e954087 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
## `def source_suffix(self) -> str`

Return the primary source file extension for `CBackend` as the string `".c"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.system_prompt fingerprint=6294bfd2b4c70790cda6b3fb1c4fabbfc6b5f9ba62cf1d242f7f22679ac9ae01 body_fp=85ae6f73fb18268e2ab65dcabf3f06f3298a4acaecc94d8d7159d69e5ff9e52b source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
## `def system_prompt(self) -> str`

Return the `C_SYSTEM_PROMPT` constant string used to guide LLM documentation of C symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.resolver fingerprint=b7b4ee80cfba3385c3ef0fd70f4608f3024e0a3939f02a0b960b2364fdb8b35a body_fp=b51862c706da7414f1d8d20038e6ebdcac968207198f87b8319b0d8cef687326 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=domain -->
## `def resolver(self)`

Return the lazily-initialised `LspResolver` for `CBackend`, building it once from `c_spec()` or returning `None` if `TRIE_DISABLE_RESOLVER=1` or the spec is unavailable.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:__all__ fingerprint=17db9df420cd252d29c389db4e958fbfa1492db31791812367c8d86c0df23509 body_fp=6b623c6c85f499a66a299a39f6869da7081676bf1baa6bbfd22200c81e53878a source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
Declares the public API exported from `trie/parse/c.py` as `["C_SYSTEM_PROMPT", "CBackend", "extract_file_data", "extract_symbols"]`.
<!-- trie:end -->