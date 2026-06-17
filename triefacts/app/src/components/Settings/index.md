---
trie_version: 0.1.9
source: app/src/components/Settings/index.tsx
file_fingerprint: b80c26fae9fdce6471ed4eeecfd39d56beb8270a2f8ccf4d49d79e241bb00690
last_synced_at: '2026-06-17T16:38:50Z'
defines:
- kind: interface
  qualified_name: app/src/components/Settings/index:SettingsProps
  lines: 22-24
- kind: constant
  qualified_name: app/src/components/Settings/index:APP_CATEGORIES
  lines: 26-26
- kind: function
  qualified_name: app/src/components/Settings/index:Settings
  lines: 31-243
- kind: function
  qualified_name: app/src/components/Settings/index:SectionLabel
  lines: 245-251
- kind: function
  qualified_name: app/src/components/Settings/index:CategoryButton
  lines: 253-275
- kind: function
  qualified_name: app/src/components/Settings/index:AppSettingRow
  lines: 278-308
- kind: function
  qualified_name: app/src/components/Settings/index:AppControl
  lines: 310-348
- kind: function
  qualified_name: app/src/components/Settings/index:TrieMissingNotice
  lines: 351-393
- kind: function
  qualified_name: app/src/components/Settings/index:TrieSettingRow
  lines: 396-437
- kind: function
  qualified_name: app/src/components/Settings/index:TrieControl
  lines: 439-482
- kind: function
  qualified_name: app/src/components/Settings/index:OcSettingRow
  lines: 485-520
- kind: function
  qualified_name: app/src/components/Settings/index:OcControl
  lines: 522-581
- kind: function
  qualified_name: app/src/components/Settings/index:coerceEnum
  lines: 584-589
- kind: function
  qualified_name: app/src/components/Settings/index:Spinner
  lines: 592-594
- kind: function
  qualified_name: app/src/components/Settings/index:Toggle
  lines: 596-611
- kind: function
  qualified_name: app/src/components/Settings/index:Select
  lines: 613-635
incoming_refs: 1
outgoing_refs: 31
---
<!-- trie:section symbol=app/src/components/Settings/index:SettingsProps fingerprint=deb97fca5c73a358308160dc9227d93caef742bb2b56b61c93bd1469ff841062 body_fp=5b86a144b716b4e02b8cd87b14e42094af074ddd74f18cb3ef12491ba66f7459 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=model -->
Props for the `Settings` component.

- `onClose`: callback invoked when the panel should be dismissed.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:APP_CATEGORIES fingerprint=36deff6148d45142eeb9aa8c98501a35b782d64277d76c9ad0adb54f19fa1337 body_fp=668ef969d63c53fb42c6e30532013b79c5674d96e7e029b1bb1b498df2fccfa6 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=model -->
Deduplicated list of category strings derived from the `SETTINGS` schema, used to populate the App section of the category nav.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:Settings fingerprint=ad8b544d81a6a5fccf718c935bbe8ea67114ec967ef2fa0939b7430aedaeaa3b body_fp=d502ce228dd9b278eb3341d086d8425da032690621ce099ff753ca694f0f01a2 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=api -->
Render a full-screen VS Code-style settings panel with category nav, search filtering, and three sections: app preferences (`prefs.json`), `trie.toml` fields, and opencode config (`opencode.json`); changes persist immediately.

- `onClose` — callback invoked when the close button is clicked or trie init completes.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:SectionLabel fingerprint=d14bbd1162e10e2accd842b5428bef96274d2df0a85939dcaf270497a4e2435d body_fp=f31f674891c6cbc53b1eb554145a5a35708c261743201582461752c83fd69d5a source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Render a styled uppercase section label in the Settings sidebar navigation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:CategoryButton fingerprint=6029ebfd3fb4bd2f69fbc89da29acdb155def706b5672a801dc0ef1e911ddc86 body_fp=007dd26561877b796ddc5831eafdb5c274998fdd9fe8bb27682f41f525c47ce1 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Render a sidebar navigation button with an accent left-border when active.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:AppSettingRow fingerprint=70473bd91ce0199f6e62edc99e6f90a679cea94fe6362f8983a923d871a32fc6 body_fp=2505e4ebd03a6093999009a8c4f1233e6e5d6f812b36f8b133b8431e09aea2de source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=api -->
Render a single app preference row (prefs.json) with its title, description, ID, an inline reset button when the value differs from the default, and an `AppControl` input.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:AppControl fingerprint=5837305fcbd64957c98ca6394748f1cb6f71281f885ed4da27770404838b5e19 body_fp=d43832dded432cfe9497928bde786668678bf1589b49faa040c5b330f0ea542c source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=ui -->
Render the appropriate input control for an app `SettingDef` based on its type: `Toggle`, `Select`, number input, or text input.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:TrieMissingNotice fingerprint=a75277fb730adee22a4e0cb63782ba6ec1b419123f989bbc787a5112d90e050d body_fp=f87c6b3a5e0e277a1764cdab26397fab0cc4b47b5dfbbab5ea56a1680974fc1d source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=api -->
Renders a notice when `trie.toml` is absent, offering a button that runs `trie init`, switches to the trie tab, and closes the Settings overlay.

- `initing` — disabled state derived from command store; true only while `init` is the active running command.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:TrieSettingRow fingerprint=cb2057f273759a1630c7f2b1575de036eb1fd36fe9ec14125b8b164fee4e207c body_fp=46651b38e62d54e84c2a9e4f1640416c3d57edd994ede58b041b06cca9dd27d3 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=api -->
Render a single `trie.toml` setting row, reading and writing its value via `useTrieConfigStore`; setting a value equal to the field's default removes the key entirely from the stored delta.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:TrieControl fingerprint=1e953c2fa0e42f20a08950f243fb1766dbcb7cd132f7af4f57c47c8bf2660546 body_fp=89cd68226f830604e2c7ec743f97429d5dd1f796d685d816960d4e817a358378 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=ui -->
Render the appropriate input control for a `trie.toml` field based on `def.type`, delegating to `Toggle`, `Select`, `StringListEditor`, or `JsonEditor` as needed.

- `value`: empty string shown when `undefined`; empty number/string input reverts to `def.default`
- Returns `null` for unrecognised types.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:OcSettingRow fingerprint=db882204f9692179eb9b098fe6f64c10d13c044fc178a5bf1434aaa543cad08c body_fp=48f22fdd7e6996082638e42e14aedef2409b53f4f4536f9bb8c7e20d7a0ace01 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=api -->
Render a single opencode config field row, reading and writing its value via `useOpencodeConfigStore`, with a "restart" badge when `def.restart` is set.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:OcControl fingerprint=0f91e1840a717ae68499153d0c81f0914296855a2e8fc091e0e25048e64f1242 body_fp=54c4aad4bbb0fd5e9ff630be25b6aed605f18ddcab5e1e30591797e8fe84d7b4 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=domain -->
Render the appropriate input control for an `OcFieldDef` field, dispatching on `def.type` to one of ten specialised editors or primitives.

- `enum` values pass through `coerceEnum` so empty string maps to `undefined`, `"true"`/`"false"` to booleans.
- Empty number input calls `onChange(undefined)` rather than `0`.
- Empty string input calls `onChange(undefined)` rather than `""`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:coerceEnum fingerprint=d183ac55a6948851d147836b5481f61cd0ca6d5c3caedc9fd9f4940e6fbb2b11 body_fp=f42dab7efadc5439bbb9c0aca873d0fd44048b0306429500fdf96226a2805349 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Convert a select-option string to its typed value for opencode enum fields.

- Returns `undefined` for `""`, `true`/`false` booleans for their string forms, otherwise the string unchanged.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:Spinner fingerprint=6cc809a327d911221e5863613202a98ef19a5b1b1a22ea95ec35a7d37712a3e9 body_fp=cd17e9f7931ee269a72aaa4aa5605d8cb1f1ea18243c917e9e6719e0c3064fb8 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Render a small spinning `Loader2` icon at size 13 with the `animate-spin` class.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:Toggle fingerprint=21c0ce37b7eeb1cd0899b81babc609ef2f49f307043acfc394db3e026fc8b140 body_fp=db43ae786b9d845c7927fa22ff6661094510711f7140092d82b313951152ae51 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Render an accessible toggle switch button that calls `onChange` with the inverted boolean on click.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/index:Select fingerprint=11abca73954d8ad73235ac6513313b8b34b98de883bf4a4cdc9d627c889c7291 body_fp=b19a682eb8c99bb9b2cc37c2552eed7b2ea7c515c67c2fd28cd231752f474dc0 source_ref=3e44368f386f10ceacf240188f4a46cac13744ec role=util -->
Render a styled `<select>` element populated from `options`, calling `onChange` with the selected string value.
<!-- trie:end -->