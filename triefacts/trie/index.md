---
trie_version: 0.1.9
source: trie/index.py
file_fingerprint: 8e33a42b0a971d737a6ab7d3a34edb7a132b7bb1e04a36c907000d8f0fefa5f5
last_synced_at: '2026-07-25T01:52:18Z'
description: 'Generate the wiki front door: an index README for the triefact tree.'
defines:
- kind: module
  qualified_name: trie/index:__module__
  lines: 1-145
- kind: constant
  qualified_name: trie/index:INDEX_MARKER
  lines: 31-31
- kind: constant
  qualified_name: trie/index:_ENTRY_POINT_LIMIT
  lines: 33-33
- kind: function
  qualified_name: trie/index:_file_descriptions
  lines: 36-62
- kind: function
  qualified_name: trie/index:build_index
  lines: 65-132
- kind: function
  qualified_name: trie/index:write_index
  lines: 135-144
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=trie/index:__module__ fingerprint=9e1250a0aa1097f31e1890d650053028fe3a4312895ea493c0d41814d805a5bb body_fp=0586b611689ae2f1d560b7cee0ed189611012f02af271934de1a25f34d65ff21 source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=orchestration -->
Generate the wiki front door: a deterministic, LLM-free index `README.md` for the triefact tree, derived from the graph store and triefact front matter.
<!-- trie:end -->
<!-- trie:section symbol=trie/index:INDEX_MARKER fingerprint=747a38f63e83ad9bb0a2b102cda1f1ba310040ccb3f758296c1abea8d6dc0c5e body_fp=8a329f319d67582a139d5b159a897451ba74fab11f8a741c6e28db6bff042da9 source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=config -->
HTML comment string embedded in the generated `README.md` to mark it as trie-owned and warn against manual edits.
<!-- trie:end -->
<!-- trie:section symbol=trie/index:_ENTRY_POINT_LIMIT fingerprint=8ab101f599265d1097615a06228838c4fe3b3fa9e2216a7cf35eb6e2a6b415cb body_fp=67558018ce81b8aea0c93ec2f991fe34dc89f08d4cd6bd7d72ec2709d640b36e source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=config -->
Maximum number of entry-point symbols included in the index's "Entry points" section.
<!-- trie:end -->
<!-- trie:section symbol=trie/index:_file_descriptions fingerprint=d22da5781ceafcf787d93ddde3b9683572760df34647c442e3260c645f3174c9 body_fp=cbe310716811b7b553ffad1c1abccd98a8cfb08cf6233b1174ea1edd024900e1 source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=io -->
Scan all `.md` files under `triefacts_root` and return a mapping of triefact-relative paths to their YAML front-matter `description` field (empty string if absent or unparseable).

- `skip_dirs`: top-level directory names whose contents are excluded from the scan.
- `README.md` at the root is always skipped.
- Whitespace in extracted descriptions is normalised to single spaces.
<!-- trie:end -->
<!-- trie:section symbol=trie/index:build_index fingerprint=d07f7c4c5cc9043becd5fba4a690d84548d0e86b6d947632d6f5961e20a0f7cf body_fp=b4ad9f409b18593419cd817e4e871af5c759609fa9909f95ce26f3bb8d0fefc5 source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=domain -->
Render the full triefact-tree index as a Markdown string from `store` and on-disk triefact files.

- `store`: queried for top-`_ENTRY_POINT_LIMIT` public symbols ranked by inbound reference count.
- `project_root`: combined with `config.triefacts.root` to locate triefact files and exclude the diffs archive directory from the TOC.
- Returns a newline-joined Markdown document with a "Codebase wiki" heading, optional entry-points section, and a files section grouped by directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/index:write_index fingerprint=1d03c57e391e83aa8b67f025e146c37b4ae0df635e3862c97844f7ea80c25f31 body_fp=4819b6d35d3109e38bf37ed7ae843998e87bbc08934368ca16c81c5d76172912 source_ref=2cbb9fc54f20a44684a2b45d6c7b8509ee1375dd role=io -->
Write the generated index markdown to `<triefacts.root>/README.md`, returning the written path.

- Returns `None` if the triefact root directory does not yet exist.
<!-- trie:end -->