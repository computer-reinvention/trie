---
trie_version: 0.1.9
source: app/src/components/Editor/FileTabContent.tsx
file_fingerprint: 697caec18084d169a82261c61d6fbafe4842374d2493b27748da553a5905057b
last_synced_at: '2026-06-17T16:37:21Z'
defines:
- kind: function
  qualified_name: app/src/components/Editor/FileTabContent:FileTabContent
  lines: 11-78
incoming_refs: 1
outgoing_refs: 6
---
<!-- trie:section symbol=app/src/components/Editor/FileTabContent:FileTabContent fingerprint=14a316fd7e40c1c56ddd7185ed17d0527b8e012afca644bf377ed910b6ad4e16 body_fp=1a0465b7dbed4bcc459c7a6e17759730fc5b417f65022cf6e1bdd9b564ea3044 source_ref=8607290e022c091b92b51a1cf84ac68031802430 role=api -->
Render a single file tab's body with a source/triefact toggle and deep-link scroll-to-line behaviour.

- `tab.pendingFocusLine` — one-shot store-driven line; consumed into local `pendingLine` then cleared
- `onOpenSource` — flips view to source and sets `pendingLine` to the requested line
- `onRevealInGraph` — reveals the symbol in the graph store and activates the topology tab
<!-- trie:end -->