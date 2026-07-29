---
trie_version: 0.1.9
source: trie/parse/c.py
file_fingerprint: 7cd0fc7a39a4881889459a47d626c693046112d93bbe7527e5563c2dfb89b076
last_synced_at: '2026-07-29T00:06:22Z'
description: "C language backend \u2014 tree-sitter symbols + references, paired with\
  \ clangd."
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
- kind: function
  qualified_name: trie/parse/c:_node_text
  lines: 35-36
- kind: function
  qualified_name: trie/parse/c:_hash
  lines: 39-40
- kind: function
  qualified_name: trie/parse/c:_module_key
  lines: 43-45
- kind: function
  qualified_name: trie/parse/c:_declarator_name
  lines: 48-61
- kind: function
  qualified_name: trie/parse/c:_is_static
  lines: 64-68
- kind: function
  qualified_name: trie/parse/c:_make_symbol
  lines: 71-101
- kind: function
  qualified_name: trie/parse/c:extract_symbols
  lines: 104-166
- kind: function
  qualified_name: trie/parse/c:_find_node_for_symbol
  lines: 169-191
- kind: function
  qualified_name: trie/parse/c:_collect_call_names
  lines: 194-208
- kind: function
  qualified_name: trie/parse/c:extract_file_data
  lines: 211-238
- kind: constant
  qualified_name: trie/parse/c:C_SYSTEM_PROMPT
  lines: 241-250
- kind: class
  qualified_name: trie/parse/c:CBackend
  lines: 253-307
- kind: method
  qualified_name: trie/parse/c:CBackend.__init__
  lines: 259-261
- kind: method
  qualified_name: trie/parse/c:CBackend.extract_file_data
  lines: 263-283
- kind: method
  qualified_name: trie/parse/c:CBackend.extract_symbols
  lines: 285-286
- kind: method
  qualified_name: trie/parse/c:CBackend.source_suffix
  lines: 288-289
- kind: method
  qualified_name: trie/parse/c:CBackend.system_prompt
  lines: 291-292
- kind: method
  qualified_name: trie/parse/c:CBackend.resolver
  lines: 294-307
- kind: constant
  qualified_name: trie/parse/c:__all__
  lines: 310-310
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=trie/parse/c:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=3935bfa1436dd870c449a2bb50073189a3ec81e7b6fd1892b1634ded22f2b134 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
C language backend implementing tree-sitter-based symbol extraction and intra-file reference resolution, paired with clangd for cross-file references.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:C_LANGUAGE fingerprint=32ef11120cd687e0fd0a61aa2e4e23551b0308764ed782450d301e410ad9f674 body_fp=3b3575f06b2f58602551c66146e81e2e7c716f1395bca0779ff7b4c0ee95b190 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
Module-level `Language` instance initialised from the `tree_sitter_c` grammar, shared by all C parsers in this module.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_make_parser fingerprint=288e56b014eeadc77f04b64ce2ffcd8f39a1c09d80945692913650559938b042 body_fp=f91fab0e3f345c963d2c8fb2e99fad60d64c116a3c68b5dddc1c913e1f6ae58a source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
Construct and return a `Parser` instance configured with `C_LANGUAGE`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_node_text fingerprint=90272da3050ae7f74f98b5fb62c5860239cd69d3c98b9843ee7816f84677e986 body_fp=453deefc55cdbe82678ff13c422c4bcd5392a0a56e3312af1dc4aeee3f9b0f25 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
Decode the UTF-8 text of a tree-sitter `Node` from the raw `source` bytes.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_hash fingerprint=7057d302a510678c4e042810b0eb270cc10d5047cb0a03fac868582b067b5767 body_fp=4d6c535ddd567d3e1fea8feeb45a70dc232492d2f3105352d59a2cda51262480 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
Return the SHA-256 hex digest of a UTF-8-encoded string.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_module_key fingerprint=af6ee1ee42882ba9ba4e716ba32e14d2b07819ce55d6304c1c80c90e619356e9 body_fp=5f9088c6d4bc89f59f6d74c9fd78afba2aa9b8dacc536189bcef44e4f2763f86 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
Compute the module key for a file by stripping its extension from its path relative to `source_root`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_declarator_name fingerprint=de84d761205b65e3fa1dd894c0dec702843714c9ccacf3bc50f108b9b0c66869 body_fp=50ce28e316481e7dbbac6522fc5755d19189e6c942c5496132c27968cbfc5a18 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Recursively traverses nested pointer, array, and function declarator nodes to return the leaf identifier name, or `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_is_static fingerprint=3e7bf885277f29a383637b8b7c497a2184e628202e412f5a39ec7e33c72d9703 body_fp=a65829f2d1197da39b890f1f7c74baec7f679518a0a0b882a68f77a8f19df7ab source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Return `True` if the tree-sitter `node` has a `static` storage-class specifier among its named children.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_make_symbol fingerprint=20913a70c6667376e46c113e24a9dcb32c5a7df82a1ee70aeda376438e825ba5 body_fp=68bf4a8b0c93554d76989c7ea9c0a98ae4c8d3fcba8b2f05de400a278390bba9 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Construct a `Symbol` from a tree-sitter `Node`, extracting signature, body text, hashes, and line numbers.

- `module_key`: colon-prefixed namespace used to form `qualified_name`.
- `signature`: text before the body node if a body exists, else the full node text.
- `body_text`: inner body node text, or falls back to `signature` when no body is present.
- `docstring`: always `None` (C has no docstring convention).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:extract_symbols fingerprint=96375bc3e6986df40fed908d10bb21c67386c98fa70dc774958bf82b528ff8a2 body_fp=501ec1df7a5722ef342855ff6c13ca901c19796abd5f7312a9077f3833c920ce source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Parse a C file (or provided source text) with tree-sitter and return a deduplicated list of top-level `Symbol` objects.

- `source_text`: if given, parsed directly instead of reading `file_path` from disk.
- `source_root`: used to compute module keys and relative paths; defaults to `file_path.parent`.
- Skips duplicate names; `static` symbols are emitted with `is_public=False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_find_node_for_symbol fingerprint=8867133b8e3fddce8207a725c1bcb9df7f220501a13fa64cc3501b1a272488d0 body_fp=29cdee2bf675579c14e40f8c4c16eb53dc034006a2f4751d50967bec22e02eb9 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Walk the tree-sitter `root` node tree to find the first top-level node whose start line matches `sym.start_line` and whose type is a recognised C declaration kind.

- Returns `None` if no matching node is found.
- Stops traversal immediately once a match is found.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:_collect_call_names fingerprint=63942098d6e67671fdc1cadcef8e97335d99104aee119a73eb5a8f75df8ec65e body_fp=c770d3cb78db4cda027830223bd233c64d2372cc4bdac13038edae38639cf6e4 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Recursively walk a tree-sitter `Node` and return the set of all direct function-call identifiers found, skipping comments and string literals.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:extract_file_data fingerprint=91a91c016ed50333ae09b5ac599f759217e794b3573ae0232e9ea70a46cf0b6d body_fp=e3cd7c64825d62d389ba47979baa6301901118681842a36f890b6229b4445d11 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=parsing -->
Parse a C file and return all its symbols plus intra-file `"calls"` references between them.

- `source_root`: defaults to the file's parent directory if omitted.
- References are only emitted for calls to symbols defined in the same file.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:C_SYSTEM_PROMPT fingerprint=218b85dcbc3c31f4db53f192e2859e58b8131d055bd01909efa0ae9bcbc248ee body_fp=ee376e779bc6f8dbb8822eeaf7701d5b29c3ba0b166ae343721eee437ce6c24c source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
System prompt string passed to the LLM when generating documentation for C symbols in a code-navigation graph.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend fingerprint=50bcab3f7e61f7b627e80295b644062267af251dc16626958efff78fc329d57c body_fp=3b18f7f22570f639f3dad4ca1d892b11de7310923bb8725e70ddc5cdd5417071 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
Implements the `LanguageBackend` interface for C source files, combining tree-sitter symbol extraction with optional clangd-backed reference resolution.

- `extract_file_data`: raises `NotImplementedError` if `source_text` is supplied; merges clangd references when a resolver is available.
- `resolver()`: lazily builds an `LspResolver` from `c_spec()`; returns `None` if `TRIE_DISABLE_RESOLVER=1` or spec is unavailable.
- `extensions`: handles both `.c` and `.h` files.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.__init__ fingerprint=b84739b0fbbdbeb6b33571852fef53390cb973b63bb786a1526af79058a93652 body_fp=502319a8c1fe9d275afe64ff7aab9e5dfb8cca4d517016617fdbacb6cc8a591d source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=domain -->
Initialize `CBackend` with `_resolver` set to `None` and `_resolver_built` flag set to `False`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.extract_file_data fingerprint=b20e0b87585336f45b65241da08a639004c8728e185ae83f13add911ee485f41 body_fp=3f3976d78ae7060e052bd7acda4f470bb9c2ede1eb4a514027808d6f7eba76de source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=orchestration -->
Extract symbols and references from a C file, merging in clangd-resolved references when a resolver is available.

- `source_text`: not supported; raises `NotImplementedError` if provided.
- Returns a `FileData` with clangd cross-reference edges merged, or the tree-sitter-only result if no resolver is configured.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.extract_symbols fingerprint=af266339106949531c076cf2e82cb2565f65b39795b7b77394086774fac189f3 body_fp=5214e2e62a614695981d8a5664cf6eb9de52833c88b3d842134d28bd556b992d source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
Delegates `CBackend.extract_symbols` to the module-level `extract_symbols` function unchanged.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.source_suffix fingerprint=68febd0fdec6b8e80b89cba64f0353078ade4b7310d55ed05faed3c5bdcf163a body_fp=95f97dde5981a29022f63a88da1f19fbf5c66acf33131d417f0cb067027282a6 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=util -->
Return the primary source file extension for `CBackend` as the string `".c"`.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.system_prompt fingerprint=6294bfd2b4c70790cda6b3fb1c4fabbfc6b5f9ba62cf1d242f7f22679ac9ae01 body_fp=32b7a959bc320227a9b1c7449ecfa0802dcf35a82cd41784be01d4c95f21c3ac source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=api -->
Return the `C_SYSTEM_PROMPT` constant string used to guide LLM documentation of C symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:CBackend.resolver fingerprint=b7b4ee80cfba3385c3ef0fd70f4608f3024e0a3939f02a0b960b2364fdb8b35a body_fp=6f2410ab5839631bb61148c8fd66e7f76d42159a930eb3d62394bcd417cd56a8 source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=domain -->
Return the lazily-initialised `LspResolver` for `CBackend`, building it once from `c_spec()` or returning `None` if `TRIE_DISABLE_RESOLVER=1` or the spec is unavailable.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/c:__all__ fingerprint=17db9df420cd252d29c389db4e958fbfa1492db31791812367c8d86c0df23509 body_fp=6b623c6c85f499a66a299a39f6869da7081676bf1baa6bbfd22200c81e53878a source_ref=eae0fdcc655266a1948b0d13ed369d4c7727f4f4 role=config -->
Declares the public API exported from `trie/parse/c.py` as `["C_SYSTEM_PROMPT", "CBackend", "extract_file_data", "extract_symbols"]`.
<!-- trie:end -->