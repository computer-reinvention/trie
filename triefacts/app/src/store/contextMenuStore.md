---
trie_version: 0.1.9
source: app/src/store/contextMenuStore.ts
file_fingerprint: 321fecdd466333e932fc548a6fe492b5d50211b3cd16f91284fa27e6085842f6
last_synced_at: '2026-06-17T16:40:19Z'
defines:
- kind: interface
  qualified_name: app/src/store/contextMenuStore:ContextMenuItem
  lines: 8-15
- kind: interface
  qualified_name: app/src/store/contextMenuStore:ContextMenuState
  lines: 17-24
- kind: constant
  qualified_name: app/src/store/contextMenuStore:useContextMenuStore
  lines: 26-33
- kind: function
  qualified_name: app/src/store/contextMenuStore:openContextMenu
  lines: 36-42
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/store/contextMenuStore:ContextMenuItem fingerprint=d20c8117ed367ed36c489b5c5ad7dbdd0fa9424375a62450c4c8898ab956974c body_fp=f56e88c425f448252155ea7be0507c773de6b63c1be74ffe95901fb7fa32b693 source_ref=95b2108d1aedeadd4852d82095d3357653eea3eb role=model -->
Describes a single item rendered inside the app-wide context menu.

- `label`: set to `"-"` to render a visual separator instead of an action.
- `onSelect`: invoked when the user clicks the item.
- `danger`: applies destructive/danger styling when `true`.
- `disabled`: prevents selection when `true`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/contextMenuStore:ContextMenuState fingerprint=74f02ad87bc5525cf73431cd505bcb17adf7da21461c9a5872d61d6a70377de0 body_fp=a15ce8d718e750bb581242c6b82035e0f2453627bd19f4e39add0b62d7a15326 source_ref=95b2108d1aedeadd4852d82095d3357653eea3eb role=model -->
Internal Zustand store shape for the single app-wide context menu instance.

- `open`: whether the menu is currently visible
- `x`, `y`: screen coordinates at which the menu is anchored
- `items`: ordered list of menu entries to render
- `show`: sets `open` to `true` and updates position and items
- `hide`: sets `open` to `false` and clears items
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/contextMenuStore:useContextMenuStore fingerprint=4a7f96e43c7152ad114211ae214afb352062bdce88d5cf3e2d27823680df0abb body_fp=b37f7cb116454161464f643bdb3b34e2e38bef4d30ea702239d3f80a1b432626 source_ref=95b2108d1aedeadd4852d82095d3357653eea3eb role=persistence -->
Zustand store managing the single app-wide context menu's open state, position, and items.

- `show`: sets `open: true` and records screen coordinates and menu items
- `hide`: sets `open: false` and clears items
- `items`: a separator is rendered for any entry whose `label` is `"-"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/contextMenuStore:openContextMenu fingerprint=eb98e91c3c95639dc8def5411acf7222a009dedd50b0db159c4607ff5ae2d137 body_fp=930cc3976f587c1f39e3f5ff50f79817bfcb1b9b0f6c0b90e761e5d2fb04c4bc source_ref=95b2108d1aedeadd4852d82095d3357653eea3eb role=util -->
Suppress the native browser context menu and open the app context menu at the event's client coordinates.

- `e` — any event-like object exposing `preventDefault`, `clientX`, and `clientY`
- `items` — menu entries to display; a `label` of `"-"` renders a separator
<!-- trie:end -->