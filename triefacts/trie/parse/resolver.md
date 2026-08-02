---
trie_version: 0.3.0
source: trie/parse/resolver.py
file_fingerprint: 33c0f610abcf183b5c12249c66f5e87f4518389a31dabab97218547fcb9c13ac
last_synced_at: '2026-08-02T21:19:42Z'
description: "The reference-resolver contract \u2014 tree-sitter's type-aware supplement."
defines:
- kind: module
  qualified_name: trie/parse/resolver:__module__
  lines: 1-123
- kind: constant
  qualified_name: trie/parse/resolver:KIND_RANK
  lines: 45-52
- kind: class
  qualified_name: trie/parse/resolver:ReferenceResolver
  lines: 56-85
  signature: class ReferenceResolver(Protocol)
- kind: method
  qualified_name: trie/parse/resolver:ReferenceResolver.resolve_file
  lines: 67-85
  signature: 'def resolve_file( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]'
- kind: function
  qualified_name: trie/parse/resolver:merge_references
  lines: 88-119
  signature: 'def merge_references( base: list[Reference], extra: list[Reference], ) -> list[Reference]'
- kind: constant
  qualified_name: trie/parse/resolver:__all__
  lines: 122-122
incoming_refs: 20
outgoing_refs: 3
---
<!-- trie:section symbol=trie/parse/resolver:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=27df979755999366e0d72f7025aee0f6cea500b654574f33aae7c87203e05372 source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=parsing -->
Defines the `ReferenceResolver` protocol and `merge_references` utility for the type-aware, post-tree-sitter reference-resolution pass.

- `KIND_RANK`: precedence map for edge kinds; strongest kind wins during dedup.
- `ReferenceResolver`: `runtime_checkable` `Protocol` for pluggable, per-language type-aware resolvers.
- `merge_references`: merges resolver edges into tree-sitter edges, deduping by `(src, target)` pair.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolver:KIND_RANK fingerprint=a3c07786b38bc888b475b76f1e40283e77d3dce2278e3997ba1c47aaab1ef35f body_fp=05056dba272d1e525455c964035e33c0880c1b3c1e60c2c92de12d1e150746f5 source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=config -->
Map edge-kind strings to integer precedence scores; higher wins during deduplication in `merge_references` and tree-sitter extraction.

- `"inherits"`, `"implements"`, `"contains"` share rank 3 (strongest).
- `"imports"` ranks 0 (weakest).
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolver:ReferenceResolver fingerprint=0349d63f0fd9c6dc6ab2be15c04edca3c7da217b675bd532b7ecf685e227a4de body_fp=53a1674898ec3f3ba0ecdabb70316a4b6adb11e3c365c3bae741d0703a8ff67c source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=domain -->
## `class ReferenceResolver(Protocol)`

Pluggable `Protocol` for type-aware reference resolution that supplements tree-sitter's syntactic extraction with method-dispatch edges.

- `name`: human/config identifier (e.g. `"jedi"`); used in telemetry.
- `resolve_file`: returns extra `Reference`s for one file; must return `[]` on failure, never raise; may over-approximate.
- `symbols`: tree-sitter-extracted symbols for the file, used to attribute `src_qname` without re-parsing.
- `source_root`: target qnames must match the backend's `extract_symbols` format relative to this root.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolver:ReferenceResolver.resolve_file fingerprint=af9b198e827864850594ce84830e5777c0f4c6dfb731e5d38cd9cf44795d5ac8 body_fp=bb383d3c7e83c08c7d969496f94845eb67344ae9068996e70f37613b3b2afa98 source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=domain -->
## `def resolve_file( self, file_path: Path, source_root: Path, symbols: list[Symbol], ) -> list[Reference]`

Return extra call/reference edges for one file that tree-sitter's structural pass could not resolve.

- `file_path`: absolute path to the source file under analysis.
- `source_root`: project root used to compute qnames matching the backend's format.
- `symbols`: pre-extracted tree-sitter symbols for `src_qname` attribution.
- Returns candidate `Reference`s; may over-approximate; must return `[]` on per-file failure, never raise.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolver:merge_references fingerprint=593973d4e7fb98609914f283cced0f28a1ec7e3bdf4eddfcf71e97d339bd39d5 body_fp=3cc1f4cc9b4c612018b230a5cb8a7ffd2c7e3f11f6816ade897ac79162fd5414 source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=util -->
## `def merge_references( base: list[Reference], extra: list[Reference], ) -> list[Reference]`

Merge `extra` resolver edges into `base` tree-sitter edges, deduplicating by `(src_qname, target_qname)` and retaining the strongest `KIND_RANK` per pair.

- `base`: tree-sitter-extracted references; ordering is preserved in output.
- `extra`: resolver-supplied references appended only for genuinely new pairs.
- Self-edges (where `src_qname == target_qname`) are silently dropped.
- Returns a new list; existing `base` entries may be replaced in-place if `extra` supplies a higher-ranked kind for the same pair.
<!-- trie:end -->
<!-- trie:section symbol=trie/parse/resolver:__all__ fingerprint=941d396f66bed004713d5a9ff34b620e8fb8b46b58fc43ee62310db6ecc8b0ba body_fp=8eceee1186c55590edd5f87f73d7dc810bc753262cba6262a16a8dfbbfbfa4dd source_ref=98caa279efde13ecf71fe3652575cbc535879d9c role=config -->
Declares the public exports of `trie.parse.resolver`: `KIND_RANK`, `ReferenceResolver`, and `merge_references`.
<!-- trie:end -->