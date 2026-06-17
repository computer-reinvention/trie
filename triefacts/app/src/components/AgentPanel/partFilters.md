---
trie_version: 0.1.9
source: app/src/components/AgentPanel/partFilters.ts
file_fingerprint: 93efdeafd78f88354fb8babeed66b90185c1ba669ea0f10f3b9cdc1349440003
last_synced_at: '2026-06-17T16:37:09Z'
defines:
- kind: function
  qualified_name: app/src/components/AgentPanel/partFilters:isHiddenText
  lines: 11-16
- kind: function
  qualified_name: app/src/components/AgentPanel/partFilters:isRenderablePart
  lines: 20-24
incoming_refs: 2
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/components/AgentPanel/partFilters:isHiddenText fingerprint=c920262831305fa4cb56bc5a1222bcc2af7debb4fd38d58b7180e6c184a8a7b8 body_fp=d0868a23289b5a20acde791e12573a63c1eaa56e33e9e9fa1c497f9d608ab39e source_ref=680c692588ccca0ddd91c8759e4a2cf3ce7d78dc role=domain -->
Return `true` if an `OpencodePart` is a server-injected text part that must not render in the transcript.

- `ignored` or `synthetic` flags on the part trigger suppression.
- Parts whose text starts with `<system-reminder>` are also suppressed regardless of flags.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/AgentPanel/partFilters:isRenderablePart fingerprint=275a70e1f168db6d6972ff1a2e30a441f28a2a55a036845d4e6861b46b2645b4 body_fp=6921a3fe1938645bf3841d25d9a83e8ab07727b475116933ccc5d9bacaf7b5be source_ref=680c692588ccca0ddd91c8759e4a2cf3ce7d78dc role=util -->
Return `true` if an `OpencodePart` should be rendered in the transcript: tool parts always pass; text parts must be non-hidden and non-empty.

- `p`: returns `false` for any part type other than `"tool"` or `"text"`
<!-- trie:end -->