---
trie_version: 0.1.9
source: app/src/store/patchesStore.ts
file_fingerprint: b9ca74bf1e84ef3463d3ef03d70fdf2a3bfc8551a99a5dc7bab8f2fa12b2f0ac
last_synced_at: '2026-06-17T16:40:28Z'
defines:
- kind: interface
  qualified_name: app/src/store/patchesStore:PatchesStore
  lines: 8-19
- kind: constant
  qualified_name: app/src/store/patchesStore:usePatchesStore
  lines: 21-41
incoming_refs: 6
outgoing_refs: 2
---
<!-- trie:section symbol=app/src/store/patchesStore:PatchesStore fingerprint=b0db8001133ba47932c5430d09cdfe4303088fe463521c0c93bcf9da33038c0b body_fp=b4ad8214c85853fcd732a76c0a61f5b49b6d94d802ebf3a3bd810cc76fc46d22 source_ref=84d9b72580840e371f904e536d0283fca2e44d50 role=model -->
Zustand store shape holding pending patch state, apply progress, and derived symbol membership.

- `patchedQnames`: derived `Set` of qualified names from current `patches`, used to mark staged symbols in the graph.
- `setPatches`: replaces `patches` and recomputes `patchedQnames`; optionally updates `sessionNote` and `applyInProgress`.
- `setApplyProgress`: sets `applyProgress` and derives `applyInProgress` from nullability.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/patchesStore:usePatchesStore fingerprint=3691f35def806c044aaf6dd1a9b8fffe3373743770c169144138be159227fe03 body_fp=0aefd6465e820142434e490a84635d4a0b2cc3f80a0d00394a71da21096684c6 source_ref=84d9b72580840e371f904e536d0283fca2e44d50 role=persistence -->
Zustand store holding pending patch state, apply progress, and derived `patchedQnames` for graph annotation.

- `setPatches`: updates `patches` and recomputes `patchedQnames`; optionally sets `sessionNote` and `applyInProgress`
- `setApplyProgress`: sets `applyProgress` and infers `applyInProgress` from nullability
- `patchedQnames`: derived `Set<string>` of qnames with staged edits, rebuilt on each `setPatches` call
<!-- trie:end -->