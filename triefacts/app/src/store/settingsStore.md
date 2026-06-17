---
trie_version: 0.1.9
source: app/src/store/settingsStore.ts
file_fingerprint: e39cc467364cc1100c89b89b23a8063adecb1eeddcc5d95ffd29ec323f6cb647
last_synced_at: '2026-06-17T16:40:39Z'
defines:
- kind: type
  qualified_name: app/src/store/settingsStore:Value
  lines: 4-4
- kind: function
  qualified_name: app/src/store/settingsStore:trie
  lines: 7-7
- kind: interface
  qualified_name: app/src/store/settingsStore:SettingsStore
  lines: 9-16
- kind: constant
  qualified_name: app/src/store/settingsStore:useSettingsStore
  lines: 18-51
- kind: function
  qualified_name: app/src/store/settingsStore:applyTheme
  lines: 57-70
- kind: function
  qualified_name: app/src/store/settingsStore:useSetting
  lines: 73-75
incoming_refs: 7
outgoing_refs: 2
---
<!-- trie:section symbol=app/src/store/settingsStore:Value fingerprint=bceb21dd39ebd1043844de9dea22f405ca3ac1f1763974bd0e1a9fd4c09fdeb3 body_fp=8fc02a46e6f3fa599a76765919e97eca079397fc34554cb97c06bae353ed888e source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=model -->
Union type alias representing all supported settings value primitives.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/settingsStore:trie fingerprint=d81964481f895264e77431f65c590a5ffe9eef7a7a98fcfddb6a40ac89d33cf5 body_fp=3dbc6595ed332b0ab64812eb393307e757733e4de3aaee4e0d1330561dd3c7cb source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=util -->
Return the `trie` object from the global `window`, providing access to the native backend API.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/settingsStore:SettingsStore fingerprint=a2f2132928b20733d0ecfae8f5490d8e9779a913d23c9924e91cd17c96d0a025 body_fp=0b74c121de05efd986ca75d63d7c9f30e75bcd1aa9c842bce28d7b3d4616c641 source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=model -->
Zustand store shape managing user settings values and their lifecycle.

- `values`: current settings map, initialised from `DEFAULTS`
- `loaded`: becomes `true` after `load()` resolves
- `load`: fetches persisted settings via the backend, merges with `DEFAULTS`, applies theme
- `get`: returns a typed setting value, falling back to `DEFAULTS`
- `set`: updates a single setting in state, persists it, and re-applies the theme
- `reset`: resets backend storage and in-memory values to `DEFAULTS`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/settingsStore:useSettingsStore fingerprint=019c931cf807a9f524272c258e1ef2aece4c788f1d510d80d3757cceb947a177 body_fp=3975ddf7ba99983a6fd67ae2a51a457fe2e22bf0898dc83dc7e38fc6308c5a60 source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=persistence -->
Zustand store managing user settings: loading from, writing to, and resetting the native `trie` backend, with `applyTheme` called on every mutation.

- `values` — flat map of setting IDs to their current values, seeded from `DEFAULTS`
- `loaded` — becomes `true` after `load()` resolves, regardless of success or failure
- `load` — fetches all persisted settings via `trie().settingsGetAll()`; falls back to `DEFAULTS` on error
- `get` — returns the current value for `id`, falling back to `DEFAULTS[id]`
- `set` — writes a value locally then persists it via `trie().settingsSet()`; persistence errors are silently swallowed
- `reset` — calls `trie().settingsReset()` best-effort, then restores `values` to `DEFAULTS`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/settingsStore:applyTheme fingerprint=d13529d0c645ff68550a1ce52b37f08d80b5652dacb82bfecda5e3370a25b8b1 body_fp=82b840458d2196c56e7f290952b176e12676750cf848c0201197f6b70eed563d source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=io -->
Apply appearance settings from `v` to `document.documentElement` via `data-*` attributes and the `--ui-font-size` CSS variable.

- `v["motion.reducedMotion"]`: `"force-on"` / `"force-off"` set `data-reduced-motion`; `"auto"` removes the attribute, deferring to the OS `prefers-reduced-motion` media query.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/settingsStore:useSetting fingerprint=5ec94e9e2671da5295a91c4079f8204d5441faeedca49c6f4f057761f459122d body_fp=98949599b07a7c73228190c844e03c39fbb7ffa21fe07178cf9f65c2f97aa108 source_ref=9eb6e1b2808f1545e8a712b5867e2c49065edf8a role=util -->
Selects a single setting value from `useSettingsStore` by `id`, falling back to `DEFAULTS[id]`.
<!-- trie:end -->