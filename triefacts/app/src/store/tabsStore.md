---
trie_version: 0.1.9
source: app/src/store/tabsStore.ts
file_fingerprint: a6bb67e259676338ac9b4c61bf670711fc93353d09baabce9d45da5c1a5456a7
last_synced_at: '2026-06-17T16:40:51Z'
defines:
- kind: type
  qualified_name: app/src/store/tabsStore:TabView
  lines: 9-9
- kind: constant
  qualified_name: app/src/store/tabsStore:GRAPH_TAB_ID
  lines: 14-14
- kind: constant
  qualified_name: app/src/store/tabsStore:TOPOLOGY_TAB_ID
  lines: 15-15
- kind: constant
  qualified_name: app/src/store/tabsStore:PATCHES_TAB_ID
  lines: 16-16
- kind: constant
  qualified_name: app/src/store/tabsStore:TRIE_TAB_ID
  lines: 17-17
- kind: interface
  qualified_name: app/src/store/tabsStore:GraphTab
  lines: 19-22
- kind: interface
  qualified_name: app/src/store/tabsStore:TopologyTab
  lines: 24-27
- kind: interface
  qualified_name: app/src/store/tabsStore:PatchesTab
  lines: 29-32
- kind: interface
  qualified_name: app/src/store/tabsStore:TrieTab
  lines: 34-37
- kind: interface
  qualified_name: app/src/store/tabsStore:FileTab
  lines: 39-51
- kind: type
  qualified_name: app/src/store/tabsStore:Tab
  lines: 53-53
- kind: interface
  qualified_name: app/src/store/tabsStore:TabsStore
  lines: 55-76
- kind: function
  qualified_name: app/src/store/tabsStore:basename
  lines: 78-81
- kind: constant
  qualified_name: app/src/store/tabsStore:useTabsStore
  lines: 83-173
incoming_refs: 27
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/store/tabsStore:TabView fingerprint=787ed9d97894c48c01d5d89ee0dbd69a2ccbd0fac704c1e946b05247b712602d body_fp=6757f3ac053f839f960fcd7d0fa1dd56360a89ecdadc789b9c35a54b43b1453d source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Discriminates the two display faces a `FileTab` can show: raw source or generated Triefact prose.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:GRAPH_TAB_ID fingerprint=f0c5745c9c8e9862daa28c3ef3301536e45603fa84ea893b6e4fa83b6fb0b855 body_fp=c3710bcefb66240fef373759243d27d59bf3c8e12d6b17608df6b28300b00146 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=config -->
Tab ID constant for the Attention (AGM) graph tab; fixed string `"graph"` used as its stable identifier.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:TOPOLOGY_TAB_ID fingerprint=b89600f096012c4bc616b502384d10763ea0f74ebbe16e4806db240fa6bfe8b1 body_fp=d0a67c94fbe452f747798300486b9a62cc102dbdeb602a42acb14919ae84e8f6 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Tab ID constant for the permanent topology (legacy structural graph) tab.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:PATCHES_TAB_ID fingerprint=550407ad5d1c9056fde38a0958e8046ea542fd65de9a47d64a23521b5a6b871f body_fp=21776aedc3bfee61e7d588f0d9206c142c933fb300a0ad67030564c46365e8b4 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Stable string ID for the permanent patches tab, used as `PatchesTab.id`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:TRIE_TAB_ID fingerprint=26f8dc354bc2eeb505cc31522a631aaf59cd2e7e5bba468b77706a4e0f7a38cf body_fp=f21e72e7d2084395df11dddd924856359ac309ce1aa7c60648f586e98e947fe1 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Constant string ID `"trie"` identifying the permanent trie CLI lifecycle commands and output tab.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:GraphTab fingerprint=291a62b0221180145c2ca2c9296d03ca00c1fdef344be7f650324ff93a85fffb body_fp=ac1f832bc1ba6fdae07cd6130906f8621d61bf0befcacab7c8a6bcf17536ee62 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Tab descriptor for the permanent Attention (AGM) graph tab, with fixed `id` and `kind`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:TopologyTab fingerprint=1585c26d5039556fdff612e06d6ab7929381f8ba709c0d9a1fbabed1abed8532 body_fp=75e8bab485d64afbd3d9544ca7fd73e4681e5bb84f9f09d7a85309cb149af136 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Represents the permanent Topology tab with fixed `id` and discriminant `kind`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:PatchesTab fingerprint=ce5a2db2007490501f77414974f3e0b5c00e7f4078ee525a1421f5b9feae4ea8 body_fp=de0a193a89f5297869bf513fef6aa8ddf8c65e03c8ae31eab81eddc83d0e1583 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Represents the permanent patches tab with fixed `id` and `kind` discriminant fields.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:TrieTab fingerprint=8fb464c7526ec03db8f9c473df9417b3c64639a654215b593917caa406e60f0b body_fp=e4140d0dd0b88f29fb2aeb1d794b0586198848c5aac231e9d26dc50de4e65187 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Permanent tab shape for the trie CLI lifecycle commands and output panel.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:FileTab fingerprint=8ef0ab26c2a444154c6f7d7695ef2d5844f13d7374f04ba015a795742489d699 body_fp=2c5fce284e84f785f0643eb214dfcf3eb8114f3f6116c1211cc41c3689a7b7a6 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Represents an open file tab identified by its project-relative path.

- `name`: precomputed basename; avoids re-splitting the path on every render
- `view`: which face is currently shown — `"source"` or `"triefact"`
- `pendingFocusQname`: one-shot target; triefact view scrolls to this qualified name on open
- `pendingFocusLine`: one-shot target; source view scrolls to this line on open
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:Tab fingerprint=e8aac037c601840ad2d761c72178d8fd9e9feade33283b9ae802a15b9460fc4e body_fp=4ad635d0437e2a1f7b87948ce96130fe8740c436b0d174947d8c9eefffc62a82 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Union of all tab discriminants: `GraphTab`, `TopologyTab`, `PatchesTab`, `TrieTab`, and `FileTab`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:TabsStore fingerprint=8369a5d178be4309b0a977499d96e5ce761d7db16094ec2a311cbc19f4215d16 body_fp=b09f6017b807f7056571b9f1d6c62aa32eb094651142e37973c3a8f10268b032 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=model -->
Zustand store shape managing the tab strip, active tab, and all tab mutation actions.

- `tabs`: ordered list of all open tabs; first four are permanent system tabs
- `activeId`: `id` of the currently focused tab
- `openFile`: opens or focuses a file tab; respects `forceView` to override an existing tab's view
- `close`: no-ops on the four permanent tab IDs; falls back active tab to left neighbour
- `clearPendingFocus` / `clearPendingLine`: one-shot consumers clear deep-link targets after use
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:basename fingerprint=0ddd56b31745b3d1f8f3ca75bf8a2741bdd53b783b4964def22841c52559aa4b body_fp=c0d78a4f531e5718e5402c64bd1981415b4d07df0392f17c2b1a77ae17b70bd0 source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=util -->
Extract the final path segment from a `/`-separated `relPath`, falling back to the full string if no separator is found.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/tabsStore:useTabsStore fingerprint=652d5d92461e96ca7bc847b66ca1cd5c5231a63b2cca9f49748731c349a9478f body_fp=11b670d7c2796dfb2633b1d76cb34a2183a8419295af0416022414e5371ba94b source_ref=1d63648c191e753b3d507de30a50201c5f25f671 role=persistence -->
Zustand store managing the editor tab strip, including the four permanent tabs and any number of closeable file tabs.

- `openFile`: focuses an existing tab or appends a new file tab; `forceView` must be `true` to override an already-open tab's view.
- `close`: silently ignores attempts to close the four permanent tabs; activates the left neighbour on closure of the active tab.
- `clearPendingFocus` / `clearPendingLine`: one-shot consumers must call these after reading deep-link targets to avoid re-scrolling.
<!-- trie:end -->