---
trie_version: 0.1.9
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
- kind: function
  qualified_name: scripts/bench_resolver:_extract
  lines: 38-53
- kind: function
  qualified_name: scripts/bench_resolver:_reset_backend_caches
  lines: 56-60
- kind: function
  qualified_name: scripts/bench_resolver:main
  lines: 63-121
incoming_refs: 0
outgoing_refs: 5
---
<!-- trie:section symbol=scripts/bench_resolver:__module__ fingerprint=63d31af14754f244afb453096d4dcd82e0f61c7f0b3329fad0b084d20c7c93c8 body_fp=acc6f33069ca6235372ce784ad5b2a1bbbe59baeb756143f45e6ca19cdcb3550 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=entrypoint -->
Benchmark script comparing tree-sitter-only vs tree-sitter+LSP reference extraction over a directory, reporting edge counts, method-dispatch edges recovered, and timing.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_project_qnames fingerprint=48e167609823ebce706d34ccc1cc42e1581cd8c050e02e026dcdb60513936a0f body_fp=ad2b67b5ac418d6f1df8c918fa3f5936189bfbd4141c30c9342459202328c46f source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=util -->
Collect all qualified symbol names from `files` by extracting symbols via the registry, silently skipping files that raise exceptions.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_extract fingerprint=b2d807ff8bff5e2675026b46dc05b99035f491646e3a791bbfbd0c84170112f7 body_fp=e330d9004cb74d42aa0f90c7e9957dfb5e0cc11dae4eec47ee65533ca1fee33c source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=domain -->
Extract project-internal reference edges from `files`, returning `(edges, method_edges)` as sets of `(src_qname, target_qname)` pairs.

- `method_edges`: subset of `edges` where `kind == "calls"` and the target local name contains a `.` (i.e. method dispatch).
- `qnames`: used to filter both source and target to project-internal symbols only.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:_reset_backend_caches fingerprint=5c895d52e37ff83b9b26448a4205b2a2a8dcc0bc9681ca13955bee95a633ae59 body_fp=6bdcb4bd0463972a59275b07a886bbdb662ce101b928c769d2ef339d9257661e source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=util -->
Reset the `_resolver_built` and `_resolver` attributes on every registered backend that has them.
<!-- trie:end -->
<!-- trie:section symbol=scripts/bench_resolver:main fingerprint=35fd64f10df91822337dc72386857ff0743479cb6d3c6744ade88d0f637f71ca body_fp=4fd8d61a3a97c2a86f2fb1f9c5efd37338976a0ec908a2cdda5524f28cdf5ee3 source_ref=44f408aff4a5809c71f4881520eb897378e18bd8 role=entrypoint -->
Parse CLI arguments, run reference extraction twice (tree-sitter only, then tree-sitter + LSP resolver), and print a comparison table of edge counts, method-dispatch edges, timing, and recovery statistics.

- `TRIE_DISABLE_RESOLVER`: environment variable toggled to isolate each pass; unset before the resolver pass.
- Closes any spawned LSP servers after the second pass via each backend's `resolver().close()`.
- Prints up to 15 sample net-new method edges recovered by the resolver.
<!-- trie:end -->