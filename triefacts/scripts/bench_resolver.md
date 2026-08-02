---
trie_version: 0.3.0
source: scripts/bench_resolver.py
file_fingerprint: 44b0173c8dbb2fb38e705aecd618763c768b0b8504ea1ea9b1d43cd128dcfdf4
last_synced_at: '2026-07-29T01:48:38Z'
defines:
- kind: module
  qualified_name: scripts/bench_resolver:__module__
  lines: 1-126
- kind: function
  qualified_name: scripts/bench_resolver:_project_qnames
  lines: 27-35
  signature: 'def _project_qnames(files: list[Path], source_root: Path) -> set[str]'
- kind: function
  qualified_name: scripts/bench_resolver:_extract
  lines: 38-53
  signature: 'def _extract(files: list[Path], source_root: Path, qnames: set[str])'
- kind: function
  qualified_name: scripts/bench_resolver:_reset_backend_caches
  lines: 56-60
  signature: def _reset_backend_caches() -> None
- kind: function
  qualified_name: scripts/bench_resolver:main
  lines: 63-121
  signature: def main() -> None
incoming_refs: 0
outgoing_refs: 6
---
<!-- trie:section symbol=scripts/bench_resolver:__module__ fingerprint=63d31af14754f244afb453096d4dcd82e0f61c7f0b3329fad0b084d20c7c93c8 body_fp=acc6f33069ca6235372ce784ad5b2a1bbbe59baeb756143f45e6ca19cdcb3550 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=entrypoint -->
Benchmark script comparing tree-sitter-only vs tree-sitter+LSP reference extraction over a directory, reporting edge counts, method-dispatch edges recovered, and timing.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_project_qnames fingerprint=48e167609823ebce706d34ccc1cc42e1581cd8c050e02e026dcdb60513936a0f body_fp=a325ac36fae034bf673a12fe40d90fe4212a02284a25d94ca18848ee2b124be1 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=util -->
## `def _project_qnames(files: list[Path], source_root: Path) -> set[str]`

Collect all qualified symbol names from `files` by extracting symbols via the registry, silently skipping files that raise exceptions.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_extract fingerprint=b2d807ff8bff5e2675026b46dc05b99035f491646e3a791bbfbd0c84170112f7 body_fp=5fb95298ca09a6db5eceaa7c9a200460361210fdcfcd3edf0aa31e57b6f67df4 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=domain -->
## `def _extract(files: list[Path], source_root: Path, qnames: set[str])`

Extract project-internal reference edges from `files`, returning `(edges, method_edges)` as sets of `(src_qname, target_qname)` pairs.

- `method_edges`: subset of `edges` where `kind == "calls"` and the target local name contains a `.` (i.e. method dispatch).
- `qnames`: used to filter both source and target to project-internal symbols only.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_reset_backend_caches fingerprint=5c895d52e37ff83b9b26448a4205b2a2a8dcc0bc9681ca13955bee95a633ae59 body_fp=9b79c3bd972b76d8520130c838aeb09ce633da91cd5ff4a25517851d009bb9ec source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=util -->
## `def _reset_backend_caches() -> None`

Reset the `_resolver_built` and `_resolver` attributes on every registered backend that has them.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:main fingerprint=35fd64f10df91822337dc72386857ff0743479cb6d3c6744ade88d0f637f71ca body_fp=a84ce59e133663d02c5b48f7c9144029985b06f6f5c9302444efd4040781bbf2 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=entrypoint -->
## `def main() -> None`

Parse CLI arguments, run reference extraction twice (tree-sitter only, then tree-sitter + LSP resolver), and print a comparison table of edge counts, method-dispatch edges, timing, and recovery statistics.

- `TRIE_DISABLE_RESOLVER`: environment variable toggled to isolate each pass; unset before the resolver pass.
- Closes any spawned LSP servers after the second pass via each backend's `resolver().close()`.
- Prints up to 15 sample net-new method edges recovered by the resolver.
<!-- trie:end -->