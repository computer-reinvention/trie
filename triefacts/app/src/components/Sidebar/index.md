---
trie_version: 0.1.9
source: app/src/components/Sidebar/index.tsx
file_fingerprint: 6981db307bd9b5f14189f778b2090a0991aa80c7a78d4ad5885a3500092809f1
last_synced_at: '2026-06-17T16:38:13Z'
defines:
- kind: function
  qualified_name: app/src/components/Sidebar/index:Sidebar
  lines: 9-139
incoming_refs: 1
outgoing_refs: 8
---
<!-- trie:section symbol=app/src/components/Sidebar/index:Sidebar fingerprint=cec3a8c7f598a69da23ee0563afb07c133487815cd34298fe3d0fca69b9f4017 body_fp=fa2b77796de0773f3bf8c94e824b43ff6c34a0205e1a08cc8e69108530d1a873 source_ref=582f967e8c8a1465bb53105b652bd3ef16fc4e0f role=api -->
Render the collapsible file-tree sidebar with a mode toggle (source/triefact), per-file left/right-click handlers, and a bottom graph-legend drawer.

- Returns `null` when no `projectDir` is set.
- `treeMode` controls whether left-clicking a file opens it as `"source"` or `"triefact"`.
- `collapsed` renders a narrow 9px rail instead of the full 240px panel.
- Right-click context menu exposes open-as-source, open-as-triefact, and reveal-in-topology actions.
<!-- trie:end -->