---
trie_version: 0.1.9
source: app/src/components/Editor/SourceView.tsx
file_fingerprint: c41639d572d036c5336acc556bc5467bd6d9b685858be6d432a4d04e52b05d6f
last_synced_at: '2026-06-17T16:37:32Z'
defines:
- kind: function
  qualified_name: app/src/components/Editor/SourceView:languageFor
  lines: 14-21
- kind: interface
  qualified_name: app/src/components/Editor/SourceView:SourceViewProps
  lines: 23-28
- kind: function
  qualified_name: app/src/components/Editor/SourceView:SourceView
  lines: 30-123
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/components/Editor/SourceView:languageFor fingerprint=3ebf66345da1c8e28a0239810af873edd76cbdd16a77c1265253b989a7c286df body_fp=8822d23b78c5815fde12ca909f69b3dd84ef57d301ededa9b471e5d6e8b7e5ee source_ref=a23f0072d946cb09ddd2926bf1a1ac49f5b623dc role=util -->
Return a CodeMirror language extension matching the file extension of `relPath`, falling back to an empty array for unrecognised types.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/SourceView:SourceViewProps fingerprint=a08a2de05e44ed55ccc2fdf552a9a8bad9f35078592636d533f3b44d102cbaa0 body_fp=bd054a1c3d6056ad0a1d202016b201f8d2289e87fad0481f50b611c9b6e368c8 source_ref=a23f0072d946cb09ddd2926bf1a1ac49f5b623dc role=model -->
Props for the `SourceView` component controlling which file to display and optional deep-link scrolling.

- `focusLine`: 1-based line number to scroll to on load.
- `onFocusConsumed`: called once after `focusLine` has been applied, so the parent can clear it.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/SourceView:SourceView fingerprint=c70cee1104598c4fd5bc583eb75aeed15504bf44cddd75898c3be3a5c8c862ac body_fp=e23e1f1f52b892e9389d2f0b3b576b572a127637e43ae78f39fdd27841213bb2 source_ref=a23f0072d946cb09ddd2926bf1a1ac49f5b623dc role=api -->
Render a read-only CodeMirror 6 source viewer that fetches, syntax-highlights, and optionally deep-links to a specific line.

- `relPath` — repo-relative file path; drives both fetch and language detection
- `focusLine` — 1-based line number to scroll into view after content loads
- `onFocusConsumed` — called once after `focusLine` has been scrolled to, so the parent can clear it
<!-- trie:end -->