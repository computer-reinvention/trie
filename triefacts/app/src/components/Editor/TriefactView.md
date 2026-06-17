---
trie_version: 0.1.9
source: app/src/components/Editor/TriefactView.tsx
file_fingerprint: baa43acb4f89783b501e7feae24dff9391e165ebb787864c5739f7c3746d4088
last_synced_at: '2026-06-17T16:37:42Z'
defines:
- kind: interface
  qualified_name: app/src/components/Editor/TriefactView:TriefactViewProps
  lines: 12-20
- kind: function
  qualified_name: app/src/components/Editor/TriefactView:anchorId
  lines: 22-25
- kind: function
  qualified_name: app/src/components/Editor/TriefactView:RoleBadge
  lines: 27-34
- kind: function
  qualified_name: app/src/components/Editor/TriefactView:SectionCard
  lines: 36-88
- kind: function
  qualified_name: app/src/components/Editor/TriefactView:TriefactView
  lines: 90-171
incoming_refs: 1
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/components/Editor/TriefactView:TriefactViewProps fingerprint=b211e33f1cf49f024378fa48a2d54bff6f1de6a6e90fb92dde14dba520f89bad body_fp=9fe5cb263ca4ab8fb97dfada9bdb880834e5a351a9f1818c682b316e10d5dea7 source_ref=79a289c637671a748f2eed373e7dec7f3458d556 role=model -->
Props for `TriefactView` controlling which file to display and inter-panel navigation callbacks.

- `relPath`: relative path of the file whose triefact is fetched and rendered.
- `focusQname`: if set, scrolls to and briefly highlights the matching symbol card.
- `onFocusConsumed`: called after the focus scroll is performed, to clear the caller's state.
- `onOpenSource`: called with a line number and qname to jump to source in the same tab.
- `onRevealInGraph`: called with a qname to open that symbol in the graph view.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriefactView:anchorId fingerprint=4f7c3fad3b58897128bbf20abd55eea00bc3572bd3c5e1464f0c1600291b98cc body_fp=ce15e320b0069ace94aa0683cd1c328331340e97ca7b7fed3e0ab2b2e6ab82b0 source_ref=79a289c637671a748f2eed373e7dec7f3458d556 role=util -->
Convert a qualified name into a DOM-safe element id by prefixing `tf-` and replacing non-alphanumeric characters with underscores.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriefactView:RoleBadge fingerprint=05819b17d85cf3fbb59d103aef6e1ccdc4788fd60eba0e526f0d91c4796edd27 body_fp=c8a56ee0637b27b1f9d8af5c9486da2879e8ea8195ac3d9adba17ac5a12098a5 source_ref=79a289c637671a748f2eed373e7dec7f3458d556 role=util -->
Render a styled uppercase badge for a symbol's role string, or nothing if `role` is empty.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriefactView:SectionCard fingerprint=1dbdad1244a39c523234af76eb4b7a3021b74ed0f1a1cdd526d730986bfee9e0 body_fp=c0bbee0eaffbe2f15472f6b99a56c82e23019bab6578db2355093af78c7d0c70 source_ref=79a289c637671a748f2eed373e7dec7f3458d556 role=api -->
Render a single `TriefactSection` as a card with a header row, role badge, line-jump button, and Markdown body.

- `onOpenSource`: called with `start_line` and `qname` when the line button or context menu item is clicked.
- `onRevealInGraph`: called with `qname` from the context menu; omitted from menu when not provided.
- Context menu items are conditionally included only when their respective callbacks are provided and `start_line > 0`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Editor/TriefactView:TriefactView fingerprint=268b2717c0baad8b4c57d13a58519208a3730ee3ffbc1b24a288111cab93ce24 body_fp=149bccea9347fd0518f0f23069011dab4f8dde40afbdb59e8847f9c273b1ac6e source_ref=79a289c637671a748f2eed373e7dec7f3458d556 role=api -->
Fetch and render the triefact for `relPath` as a scrollable list of `SectionCard` components, scrolling to and briefly highlighting `focusQname` once loaded.

- `relPath` — repo-relative file path used to fetch triefact data via `graphClient`.
- `focusQname` — if set, scrolls the matching card into view after load and adds a transient accent ring.
- `onFocusConsumed` — called once after the focus scroll has been applied.
- `onOpenSource` — forwarded to each card; flips the tab to the symbol's source line.
- `onRevealInGraph` — forwarded to each card; opens the symbol in the graph view.
<!-- trie:end -->