---
trie_version: 0.1.9
source: app/src/components/TitleBar/index.tsx
file_fingerprint: b4cdb6f51bc93acf21c34db0ab9abe6227b3cfc2908af350a15d2b4bebbc4d60
last_synced_at: '2026-06-17T16:38:36Z'
defines:
- kind: constant
  qualified_name: app/src/components/TitleBar/index:TITLEBAR_H
  lines: 5-5
- kind: constant
  qualified_name: app/src/components/TitleBar/index:TRAFFIC_LIGHT_CLEARANCE
  lines: 7-7
- kind: interface
  qualified_name: app/src/components/TitleBar/index:TitleBarProps
  lines: 9-18
- kind: function
  qualified_name: app/src/components/TitleBar/index:TitleBar
  lines: 23-52
- kind: function
  qualified_name: app/src/components/TitleBar/index:TitleBarIconButton
  lines: 54-75
- kind: function
  qualified_name: app/src/components/TitleBar/index:GearIcon
  lines: 77-84
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/components/TitleBar/index:TITLEBAR_H fingerprint=2e080946ab54c5fc6ae23739d2434cc1693022eb95d5b06b733e244aff6045be body_fp=ce6bf82e6e51ca1b36e9b0e22677b50268485e58e11935a1d58ea2a17b02c3e9 source_ref=925475307174c4b24915b8907a304ac185a46875 role=config -->
Shared title-bar height constant (38 px) used by `TitleBar` and every screen to reserve the top strip.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TitleBar/index:TRAFFIC_LIGHT_CLEARANCE fingerprint=596b449fc4b3231f88b856f2f07dd6e3d72fc55d83252c4d2e82baa605704a31 body_fp=ee2fe4be376d8bb715b26de84b998c7fe80f75a989221d33eb41751ff30cd799 source_ref=925475307174c4b24915b8907a304ac185a46875 role=config -->
Left pixel clearance reserved so content never renders beneath the macOS traffic-light buttons.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TitleBar/index:TitleBarProps fingerprint=6eb020aa7f829b18ea3044239a1c813b8828ceff937c10fd132fb93d15d7c56b body_fp=00cf82011dbfba3c719ea3d6b84830d7fe4c383466d283486ebdb589085663b8 source_ref=925475307174c4b24915b8907a304ac185a46875 role=model -->
Props for the `TitleBar` component.

- `subtitle`: dimmed secondary text rendered beside the title.
- `actions`: right-aligned controls wrapped in a non-draggable region.
- `children`: replaces the `title`/`subtitle` content area entirely when provided.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TitleBar/index:TitleBar fingerprint=e95cced2840ccc33bb20c8a3d2c49e508312c59a9cdcadff4acd10c5e67fc801 body_fp=6583a15f7b05b42148e0e904d2e6b9eee146709dcb34de7e6cdef45b378f5218 source_ref=925475307174c4b24915b8907a304ac185a46875 role=api -->
Render the shared macOS title bar with drag region, traffic-light clearance, optional title/subtitle, and right-aligned actions.

- `subtitle`: rendered in dimmed tabular-nums style beside the title.
- `actions`: wrapped in `app-no-drag` to allow clicks within the drag region.
- `children`: when provided, replaces the `title`/`subtitle` content area entirely.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TitleBar/index:TitleBarIconButton fingerprint=a0e2707b4fd4b49fedc7fd69b0fa81ad6c9b933ceb6d0ee379bcaef81ecb07b9 body_fp=bb1ef0b2e6ac90593e134976a95106c42fbf6c56ec23f981022ecd1fffe3aca9 source_ref=925475307174c4b24915b8907a304ac185a46875 role=api -->
Render a small 28×28 icon button styled for the `TitleBar` actions area.

- `label`: falls back to `title` as the `aria-label` when omitted.
- `children`: the icon node rendered inside the button.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/TitleBar/index:GearIcon fingerprint=43a2f13607a5ed608d80b7cb6de451e267b1950c4a02d7d61fd93a8ebc30cab4 body_fp=f6479390959be67b60772920d9fd3dbc3100b14799d1095c29e0ce5cd84f2e1a source_ref=925475307174c4b24915b8907a304ac185a46875 role=util -->
Render a 15×15 SVG gear icon using a circle and a single stroke path.
<!-- trie:end -->