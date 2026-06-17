---
trie_version: 0.1.9
source: app/src/components/Sidebar/FileTree.tsx
file_fingerprint: f5c6e13e5ecafcab858b2fda45907e6c3a866f11d1045c6492a88a0b22e9e8f1
last_synced_at: '2026-06-17T16:38:22Z'
defines:
- kind: interface
  qualified_name: app/src/components/Sidebar/FileTree:DirEntry
  lines: 3-7
- kind: interface
  qualified_name: app/src/components/Sidebar/FileTree:FileTreeProps
  lines: 9-14
- kind: function
  qualified_name: app/src/components/Sidebar/FileTree:FileTree
  lines: 16-91
incoming_refs: 1
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/components/Sidebar/FileTree:DirEntry fingerprint=2ce73f8707935ad14657866f7e34967ad014c0871e26de6dbb39986cc0eedd87 body_fp=ca73e2031f76be8276605bdc2d3ea3db75029f2ea424443ad6ea7181ab647338 source_ref=63ada520c37e5af71421141d2da0e6b218ca371c role=model -->
Represents a single filesystem entry returned by `trie.readDir`.

- `isDirectory` — distinguishes directories (expandable) from files (clickable)
- `path` — absolute or relative path used as the stable React key and passed to callbacks
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Sidebar/FileTree:FileTreeProps fingerprint=59169b2bace799737cf25d3bcb71e6a56e394db768d3bc36a4fe5e2de8f5facd body_fp=98c4beb734680d9c41fcb2b951d08afe389cad2264352e70850b41181fdb7cb5 source_ref=63ada520c37e5af71421141d2da0e6b218ca371c role=model -->
Props for the `FileTree` component controlling directory rendering and file interaction callbacks.

- `onFileRightClick`: receives the file path and the originating mouse event.
- `depth`: current nesting level; defaults to `0` for the root call.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Sidebar/FileTree:FileTree fingerprint=33ee817f120352d28542aa62225517d5f395a512a18adca177bb7b3fc8b92055 body_fp=9c5a39c2cd7bb2d65a162e246ac903cc53ba9f35caf9f4863e5a740a87268bbd source_ref=63ada520c37e5af71421141d2da0e6b218ca371c role=api -->
Renders a recursive, collapsible directory tree by reading `dir` via `window.trie.readDir`, sorting directories first and filtering hidden/noise entries.

- `dir` — filesystem path to list; re-fetched whenever this prop changes.
- `onFileClick` — called with the file path on left-click.
- `onFileRightClick` — called with path and mouse event on context menu; default browser menu is suppressed.
- `depth` — controls left-indent level (12 px per level); defaults to `0`.
- Filters out entries starting with `.` and named `node_modules`, `__pycache__`, `dist`, or `build`.
<!-- trie:end -->