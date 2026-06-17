---
trie_version: 0.1.9
source: app/src/agm/symbolMenu.ts
file_fingerprint: 103520c4dcf9637413fd93019a6a1da205515f03d2984d68663e909c94186da4
last_synced_at: '2026-06-17T16:36:07Z'
defines:
- kind: interface
  qualified_name: app/src/agm/symbolMenu:SymbolMenuContext
  lines: 16-29
- kind: constant
  qualified_name: app/src/agm/symbolMenu:SEP
  lines: 31-31
- kind: function
  qualified_name: app/src/agm/symbolMenu:askAgentAbout
  lines: 34-36
- kind: function
  qualified_name: app/src/agm/symbolMenu:copy
  lines: 38-40
- kind: function
  qualified_name: app/src/agm/symbolMenu:buildSymbolMenu
  lines: 42-108
incoming_refs: 2
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/agm/symbolMenu:SymbolMenuContext fingerprint=89a7d79ca2ffcad1c80656355d2136e985a3da30fe56b6add6193e12ffa83333 body_fp=bfef910b83a04f190fe507108e6f11a5d80da0106ba793f7fcb006bdb04fc5dc source_ref=e14228cbae5752caeb63647e41ef6af8a0344459 role=model -->
Input context passed to `buildSymbolMenu`, carrying symbol identity and optional host-provided action callbacks.

- `qname`: fully-qualified symbol name; the only required field.
- `filePath`: when present, enables "Open triefact" and "Open source" menu items.
- `signature`: one-liner string copied via "Copy one-liner"; omitted if unavailable.
- `onShow*` / `on*` callbacks: each optional; menu items for that action are omitted when absent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/symbolMenu:SEP fingerprint=b0b0591213b2c4d2c90242d75c409e2c2e7c4fc53c7c9c641642a96d408d3301 body_fp=9fa89b2d0ad4b84fa00d57491f8df7e2ece59174eea69cff0e1686d3029929fb source_ref=e14228cbae5752caeb63647e41ef6af8a0344459 role=util -->
Reusable separator sentinel inserted between groups in the symbol context menu.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/symbolMenu:askAgentAbout fingerprint=1f2b52f6131f0d92b64c9e02db91dfac39e8f106f523851d5fbac0588e41a031 body_fp=37fdc5f21e44d556d39a384678cc0b217ef53f8dfa2f3acb6e09a5c6b68c8f3e source_ref=e14228cbae5752caeb63647e41ef6af8a0344459 role=io -->
Dispatch the `trie:node-selected` window event to add a composer context pill for the given qualified name.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/symbolMenu:copy fingerprint=a288366e3ab026d98ea34744d59c54a85d35e1701aca015eab61f4f83b6d9352 body_fp=f417809d34dd9c8fc5306b5f357ddc69dfa17658a42f9f87ab5cd7806ff14bb3 source_ref=e14228cbae5752caeb63647e41ef6af8a0344459 role=util -->
Write `text` to the system clipboard via `navigator.clipboard`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/symbolMenu:buildSymbolMenu fingerprint=5753b83960a1a0cd35a3453421b6e993072783ad1809988db36dc06a8951c7bb body_fp=5b3c19517c35ac80a712e1a7375ceae9302400cc90768d15d408184a42322e2e source_ref=e14228cbae5752caeb63647e41ef6af8a0344459 role=domain -->
Build a grouped `ContextMenuItem[]` for a symbol's right-click menu, wiring navigation, graph exploration, AGM verbs, agent handoff, editing, and clipboard actions.

- `ctx.filePath` — controls whether "Open triefact" / "Open source" items are included
- `ctx.onTracecallers/onTraceCallees/onShowBlastRadius/onStagePatch/onRename/onDelete/onShowStats/onReadProse` — each item only appears if the host callback is provided
- `ctx.signature` — if present, adds a "Copy one-liner" clipboard item
- "Start investigation here" creates a timestamped AGM investigation, ingests the node, and calls `agm.recompute()`
- Returns separator items (label `"-"`) between logical groups
<!-- trie:end -->