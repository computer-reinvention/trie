---
trie_version: 0.1.9
source: app/src/settings/schema.ts
file_fingerprint: e3260d8b055aa227fa63151760712207f40f5f7692a6086908cea84f9394be16
last_synced_at: '2026-06-17T16:39:52Z'
defines:
- kind: type
  qualified_name: app/src/settings/schema:SettingType
  lines: 5-5
- kind: interface
  qualified_name: app/src/settings/schema:SettingDef
  lines: 7-18
- kind: constant
  qualified_name: app/src/settings/schema:SETTINGS
  lines: 20-199
- kind: constant
  qualified_name: app/src/settings/schema:CATEGORIES
  lines: 201-201
- kind: constant
  qualified_name: app/src/settings/schema:DEFAULTS
  lines: 203-205
- kind: function
  qualified_name: app/src/settings/schema:settingDef
  lines: 207-209
incoming_refs: 6
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/schema:SettingType fingerprint=0d7f78c00753b8e655d7c0e352faa118bb5b11053463bb575e9f9e22913827a6 body_fp=9f71943d74f289186b2c1de35f4bd376a109f3436e5189d6512639da4a647e33 source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=model -->
Union type enumerating the four primitive setting value kinds a `SettingDef` may declare.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/schema:SettingDef fingerprint=dd51c73a15957b19f151154bd32c1fc6ec6193bd4126bf247615e87c28e7808a body_fp=4c6d52b494710e0d4dd6be956c51074206eb646c796f6f617ea310ac0cbea092 source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=model -->
Describes a single user-configurable setting including its identity, UI metadata, type, and constraints.

- `enum`: required when `type` is `"enum"`; each entry pairs a stored value with a display label.
- `min` / `max` / `step`: only meaningful when `type` is `"number"`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/schema:SETTINGS fingerprint=5df297ed09bf817ac2e820cf2aa0038c6dcc29817bd609aad5d0275acb70ce18 body_fp=2375caec49a5ec9a2f068ca055be1373c109ebf49981c4b038c34238a7e4a065 source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=config -->
Master registry of all `SettingDef` entries, covering Appearance, Graph, Agent, and Editor categories.

- `appearance.theme` — enum: `dark` | `midnight` | `slate`; default `dark`
- `appearance.accent` — enum: `indigo` | `violet` | `emerald` | `amber` | `rose`; default `indigo`
- `appearance.uiDensity` — enum: `comfortable` | `compact`; default `comfortable`
- `appearance.fontSize` — number, pixels, range 10–18, step 1; default `13`
- `graph.defaultAxis` — enum: `role` | `subsystem`; default `role`
- `graph.showTests` — boolean; default `false`
- `graph.hideMinor` — boolean; default `true`
- `graph.memberGrouping` — enum: `subsystem` | `class` | `owningClass`; default `subsystem`
- `graph.budget` — number, range 50–1000, step 25; default `250`
- `motion.intensity` — enum: `cinematic` | `restrained` | `off`; default `cinematic`
- `motion.camera` — enum: `edge-only` | `cinematic` | `off`; default `edge-only`
- `motion.reducedMotion` — enum: `auto` | `force-on` | `force-off`; default `auto`
- `agent.sendOnEnter` — boolean; default `true`
- `agent.autoSwitchToGraph` — boolean; default `true`
- `editor.confirmBeforeApply` — boolean; default `true`
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/schema:CATEGORIES fingerprint=588d559dbd077b2b97a8f9870ab638e9dae8dd56553b7ed89d5e820a94e7d696 body_fp=0b6750c1d35c4e7e0e35e2f4b61d5514e3976abba956bda56501edf6c2e1c314 source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=config -->
Derives a deduplicated, ordered list of category strings from `SETTINGS`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/schema:DEFAULTS fingerprint=67fd5c0e37071a9017332868ca3508284f643cc0d6e45f4ce5fdfc5f5bf8f944 body_fp=7998b8ad786ae879e279b74261accb2b80a1675a18d0e80f2623142f0741b73d source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=config -->
Map of every setting id to its default value, derived from `SETTINGS`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/schema:settingDef fingerprint=999d8f53b3ab7892e35ba63cc99a087a21e54a681a8ba4ebe49e9071298801c9 body_fp=7d4d4fbf199da39eeddf238c10259f3951b83175391e1141b9cfbe7d877711d4 source_ref=a06d97edbee5d52e292d4e4ad44273b881e06e72 role=util -->
Look up a `SettingDef` from `SETTINGS` by its dotted `id`, returning `undefined` if not found.
<!-- trie:end -->