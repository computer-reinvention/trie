---
trie_version: 0.1.0
source: trie/sync/cascade.py
file_fingerprint: 07d061b6c7fc8b0f6640fca2ab6ecab449f35402a0546dd573387179c361908a
last_synced_at: '2026-05-14T17:31:16Z'
defines:
- kind: class
  qualified_name: trie/sync/cascade:CascadeResult
  lines: 10-20
- kind: function
  qualified_name: trie/sync/cascade:compute_cascade
  lines: 23-79
incoming_refs: 9
outgoing_refs: 0
---
<!-- trie:section symbol=trie/sync/cascade:CascadeResult fingerprint=8ce9686496fd5022cd1a321752b0a1a34e058f9b70eccaa7ff85c65e47e1cef1 body_fp=b85fda3cd03a0c16fc8b403179cc57baebdfc2ea9d463eb33d98d2c490ac7d6b -->
## `CascadeResult`

Immutable dataclass holding the full regeneration set after a cascade walk.

- `affected_files`: sorted list of all files needing regeneration, including seeds.
- `changed_files`: the original seed files that triggered the cascade.
- `cascaded_from_change`: files pulled in by edge-walking, excluding direct changes.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/cascade:compute_cascade fingerprint=bacbdfaab014a561eca80987b0a686a4e5b8cbe689726c44df044ba0aa77e6ca body_fp=f01a7d07d098827f103f83d08dac2c66f112e0c27dcb981ae5de9e1cd32141fd -->
## `compute_cascade(*, changed_files: Iterable[str], store: Store, depth: int = 1, hub_threshold: int = 20) -> CascadeResult`

Compute the cascade closure for a set of changed files by walking inbound dependency edges up to `depth` hops.

- `depth`: number of hops to expand from seed symbols.
- `hub_threshold`: symbols with more inbound references than this are not expanded.
- Returns sorted `affected_files` always including `changed_files`; `cascaded_from_change` holds the non-seed additions.
<!-- trie:end -->