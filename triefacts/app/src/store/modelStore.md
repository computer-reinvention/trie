---
trie_version: 0.1.9
source: app/src/store/modelStore.ts
file_fingerprint: 7ba493df3ec840078291095b474ef69e35d99f341d2c7f6c1ab25ba957823620
last_synced_at: '2026-06-17T16:40:30Z'
defines:
- kind: constant
  qualified_name: app/src/store/modelStore:SELECTED_KEY
  lines: 10-10
- kind: interface
  qualified_name: app/src/store/modelStore:FlatModel
  lines: 12-15
- kind: interface
  qualified_name: app/src/store/modelStore:ModelStore
  lines: 17-25
- kind: function
  qualified_name: app/src/store/modelStore:readStored
  lines: 27-39
- kind: function
  qualified_name: app/src/store/modelStore:flatten
  lines: 41-55
- kind: constant
  qualified_name: app/src/store/modelStore:useModelStore
  lines: 57-106
incoming_refs: 2
outgoing_refs: 6
---
<!-- trie:section symbol=app/src/store/modelStore:SELECTED_KEY fingerprint=71bb553abf8130b554fb13173d685f843779fed732b7421afffb70011ac5fdbe body_fp=96c12ff34f0ac64a098e48b072015ef8ab1e6c4029320d042f7af4e2b51944cc source_ref=00745846339dde647365720a1c7086d2c572bda5 role=config -->
localStorage key under which the selected `ModelRef` is persisted across reloads.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/modelStore:FlatModel fingerprint=1437fdf0c283989795d32eac8a7710d567f9891b4f9e236d06c80b86498b8aa6 body_fp=00a3f6582646ac35cfe94aff675ad388454b4b184d2ffbec2b6b95c2720fb25d source_ref=00745846339dde647365720a1c7086d2c572bda5 role=model -->
Extends `ModelRef` with display strings for a resolved model entry in the flat model list.

- `label`: human-readable model name, falls back to `modelID`
- `providerLabel`: human-readable provider name, falls back to provider `id`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/modelStore:ModelStore fingerprint=f4884feec33b88a82501a7e4a04d6102a644152a22d2c04341dcdb32b5f5fc3e body_fp=634c23d096884ae226fade6a241217c69a4954993b1658fccf3eb09b6732d754 source_ref=00745846339dde647365720a1c7086d2c572bda5 role=model -->
Zustand store shape holding available providers, derived flat model list, and the currently selected model.

- `flat`: denormalized list of all models across all providers with display labels
- `selected`: persisted to `localStorage`; `null` until `load()` resolves
- `loaded`: set to `true` after `load()` completes, even on error
- `load`: fetches providers, validates/seeds `selected`, and populates the store
- `labelFor`: returns human-readable model name or `"Default model"` for `null`
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/modelStore:readStored fingerprint=dd5a689856ccfd4fc7662f40eb6dc17ff0a7c515a11fae411498bd718ffc7967 body_fp=f115e255c4c68b86884ac32f5ff1c50c63f38bb909d21b654cde8adc791fa82b source_ref=00745846339dde647365720a1c7086d2c572bda5 role=persistence -->
Read and validate a persisted `ModelRef` from `localStorage`, returning `null` on absence, parse failure, or invalid shape.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/modelStore:flatten fingerprint=c42d0bcfa2bdb60dc9f0719fdc1d06bc72667b69b233f538c72c65ae92456476 body_fp=8843da69301d48c9db737db153e5f30ea8923b4e82448f7ad973ac33cd4af324 source_ref=00745846339dde647365720a1c7086d2c572bda5 role=util -->
Convert a list of `OpencodeProviderInfo` objects into a flat array of `FlatModel` records, one per model across all providers.
<!-- trie:end -->
<!-- trie:section symbol=app/src/store/modelStore:useModelStore fingerprint=c7e682f73dc7019f7f0ce598d1218cc51715c081ce05ceb5b55ce20e9e0c1411 body_fp=9885a4128ff3f872fcf3fdd3fbf383427a4a23ab75bb9af9ab684e1177fda9f8 source_ref=00745846339dde647365720a1c7086d2c572bda5 role=persistence -->
Zustand store managing available providers/models and the user's selected model, persisted to `localStorage`.

- `load`: fetches providers via `opencodeClient.listProviders()`, validates or seeds `selected` from defaults, sets `loaded: true`
- `select`: updates `selected` and writes it to `localStorage` under `trie.agent.selectedModel`
- `labelFor`: returns the human-readable model name, or `"Default model"` if `null`
- `flat`: denormalised list of all models across all providers with display labels
- `selected`: seeds from `localStorage` on initialisation; falls back to provider default then first available model
<!-- trie:end -->