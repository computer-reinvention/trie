---
trie_version: 0.1.9
source: app/src/components/Editor/PatchesPanel.tsx
file_fingerprint: ac2e44c673db6fff86a008cc94be191d4d996aa2a4fc7b7da85e1a674d9ec6d9
last_synced_at: '2026-06-17T16:37:39Z'
defines:
- kind: constant
  qualified_name: app/src/components/Editor/PatchesPanel:KIND_STYLE
  lines: 15-20
- kind: constant
  qualified_name: app/src/components/Editor/PatchesPanel:ORIGIN_STYLE
  lines: 22-26
- kind: function
  qualified_name: app/src/components/Editor/PatchesPanel:PatchesPanel
  lines: 28-125
- kind: function
  qualified_name: app/src/components/Editor/PatchesPanel:reveal
  lines: 127-131
- kind: function
  qualified_name: app/src/components/Editor/PatchesPanel:PatchRow
  lines: 133-210
- kind: function
  qualified_name: app/src/components/Editor/PatchesPanel:ApplyReportView
  lines: 212-296
incoming_refs: 1
outgoing_refs: 12
---
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:KIND_STYLE fingerprint=b87e6d3da1af59bcd1b2972e49df5c5b50566f39cc994480317d0815d06751ba body_fp=4fb19ea641d9702af93cca8a67ceaa12a4f117fea3d19ff85644347aa8c0d5ed source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=model -->
Maps each `PatchKind` value to its display label and Tailwind badge classes used by `PatchRow`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:ORIGIN_STYLE fingerprint=111e469f9ed98ae30cd43ca355433f8fa17d02c46c3460e577638f61c8c216ab body_fp=991fda796f45d790815769001d04ff05d6aba6dbed4d013b918a895a06db4a4b source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=model -->
Maps patch origin strings to Tailwind badge class strings for use in `PatchRow`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:PatchesPanel fingerprint=c4de2499910379808709e67ccb88654f7d9c112b6a2eeaa1ac2f01568a2c9a8b body_fp=1017cece2658e8ce0d2e67e89ef909cf5ad3f463da8c5765c306050e53d64144 source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=api -->
Render the patch review panel listing all staged edits with header counts, live apply progress, errors, and an `ApplyReportView` on completion.

- Staggers `playCascade` calls across up to 12 symbols at 120 ms intervals on apply.
- Shows `ApplyReportView` instead of the patch list once an `ApplyReport` is returned.
- "Discard all" and "Apply all" buttons are disabled while `applyInProgress` is true.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:reveal fingerprint=f6e7c3622d969a70328018ba54ebb821cc50b450c55b5c30b8cdabb548204a8c body_fp=b3bd09f5756fabb8e1e5516fe0b043cb8139d9feb696bf2d98a9ac98425488cf source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=util -->
Reveal a symbol in the graph by `qname`, switching to the topology tab if found.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:PatchRow fingerprint=07131917d9da664210fb14a0a60df922d33079027a5b2c26fc270c05e2d2355b body_fp=565ace0e637cf0439ccdecf06e9768d69d051d984b72f537c132dbe05bd0205b source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=api -->
Render a single `PatchEntry` as a list row showing kind badge, symbol name, origin, blast radius, and collapsible notes; pulses with activity color while the symbol is live in the graph runtime.

- `patch.blast_radius` — displays direct callers, cascade count, and hub stops when present
- `liveState` — non-empty when `agentState` is not idle or `activity > 0.05`; drives pulse animation
- `onDrop` — called when the discard (×) button is clicked for this symbol
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/PatchesPanel:ApplyReportView fingerprint=eb17ea91dea22d8b8d59e834ea99a0e02d10f83e9b0521a9052b7634b09810c1 body_fp=353803b069640fdbef215ebd0d7723b48c63222672453667c8482f6f533af9f8 source_ref=670b0937bbd8f6db558256ca1476c435387b49f4 role=api -->
Render the post-apply result view showing applied files, cascade-applied symbols, and unresolved conflicts with graph-reveal links.

- `report.ok` — controls green vs. amber status indicator in the header
- `unresolved` — items rendered with inline error code, message, and source pointer; each symbol is clickable to reveal in graph
- `onClose` — called by the "← back to patches" button to dismiss the report
<!-- trie:end -->