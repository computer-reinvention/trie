---
trie_version: 0.1.9
source: app/src/hooks/useTrieCommandEffects.ts
file_fingerprint: 45be08945fb5d6f9b36b4b84f99bc54fe1489d8ab568ce6fe85382e07eec4623
last_synced_at: '2026-06-17T16:39:23Z'
defines:
- kind: function
  qualified_name: app/src/hooks/useTrieCommandEffects:useTrieCommandEffects
  lines: 16-58
incoming_refs: 1
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/hooks/useTrieCommandEffects:useTrieCommandEffects fingerprint=3cd9ecc8ab35c831251c7e933007fb79652077ea26adbf850f599b0f2c96b93e body_fp=0a748495358397c39358495f04ddf0a0347f09c29bebbd8e860ba2329aa3a683 source_ref=118873d44543a5aaa766a0789dac7dd3c1f89bcf role=orchestration -->
React hook that wires centralised side-effects for state-changing trie CLI commands (`init`, `sync`, `refresh`), updating config, graph, and project summary on success.

- `repopulate` — callback invoked to re-pull the graph model after a graph-mutating command completes
<!-- trie:end -->