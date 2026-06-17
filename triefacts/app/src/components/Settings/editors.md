---
trie_version: 0.1.9
source: app/src/components/Settings/editors.tsx
file_fingerprint: c795ad8e355d33ebcb8144f6cd9e569a9e82a7c3cc83e0c31e494d39d310f3f3
last_synced_at: '2026-06-17T16:38:36Z'
defines:
- kind: type
  qualified_name: app/src/components/Settings/editors:Json
  lines: 10-10
- kind: constant
  qualified_name: app/src/components/Settings/editors:inputCls
  lines: 12-13
- kind: function
  qualified_name: app/src/components/Settings/editors:StringListEditor
  lines: 16-58
- kind: function
  qualified_name: app/src/components/Settings/editors:EnumMapEditor
  lines: 61-103
- kind: function
  qualified_name: app/src/components/Settings/editors:ToggleMapEditor
  lines: 106-152
- kind: interface
  qualified_name: app/src/components/Settings/editors:ProviderInfo
  lines: 155-159
- kind: function
  qualified_name: app/src/components/Settings/editors:ProviderListEditor
  lines: 161-220
- kind: function
  qualified_name: app/src/components/Settings/editors:ProviderRow
  lines: 222-312
- kind: function
  qualified_name: app/src/components/Settings/editors:McpListEditor
  lines: 315-401
- kind: function
  qualified_name: app/src/components/Settings/editors:AgentTableEditor
  lines: 404-508
- kind: function
  qualified_name: app/src/components/Settings/editors:Labeled
  lines: 510-517
- kind: function
  qualified_name: app/src/components/Settings/editors:JsonEditor
  lines: 520-568
incoming_refs: 9
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/components/Settings/editors:Json fingerprint=193f4839518d0f5eabe96a6dc95b04eefbb128b2db55a3d41445f6b7a64b27f7 body_fp=975f870afea89c29c3e32e64103bca930ff7f0b3c648841cfb2cab499b830db8 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=model -->
Local alias for `unknown` used as the opaque JSON value type throughout this module's editor components.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:inputCls fingerprint=b3978a28dc4a26a482d9618a1a361fcb43809c43c7f45134d212347de86e749f body_fp=7ea7dc1a2fc9325713fbd5168e30d405f0f0f58f5223ab3c5e238ced5728ae9b source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=util -->
Shared Tailwind class string applied to all `<input>` and `<textarea>` elements across the settings editors.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:StringListEditor fingerprint=fd0aab07f76dc9f8e7d6c01c8162ceec6cfee0398afabff8d0c6843eb95d1261 body_fp=aa5cbc6a570ad8a075c1a97eef4fa5c04d0fe8b6f185b866636346947b0f4c57 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render an editable list of strings with per-item text inputs, remove buttons, and an append button.

- `value` — treated as `string[]`; non-array input renders as empty list.
- `onChange` — called with `undefined` when the list becomes empty.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:EnumMapEditor fingerprint=54af9d272d2439b1f40380563af3e2f0124aea1e2dca9c85daa06f7b3808a3f8 body_fp=50bdcc3b8b95b9e4717e28fa18290e906b945603aae12306d272c5663a5c1c8f source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a segmented-button matrix for a `Record<string, string>` field where keys and allowed enum choices are defined by `def`.

- `def`: supplies `mapKeys` (row labels) and `mapChoices` (button options with `value`/`label`)
- `onChange`: called with `undefined` when the resulting map is empty
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:ToggleMapEditor fingerprint=f5a40c002049f09ea616edccc6664bb7afe289290c414447879b4515cc5006fc body_fp=44ba483a9667c4bf0503e0cbc55382f305e5b633884cdd52b505385861d4bc71 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a grid of toggle buttons for a `{ key: boolean }` map, cycling each key through `default → off → on → default` (tristate) on click.

- `def.toggleKeys` — list of keys to display as toggle buttons
- Each click calls `onChange` with the updated map, or `undefined` if all keys are cleared to default
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:ProviderInfo fingerprint=19c6eb0f633b67d7e025d1cf5a227f1041925ebacb1a8700e4a15025dde91cb2 body_fp=14991cd0f54aa54f8502a2b0d83ef8d4f26f940afd558456baa1fedae762e181 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=model -->
Describes the keychain state for a single provider returned by `trie().secrets.listProviders()`.

- `hasKey` — true if an API key is currently stored in the keychain
- `envVar` — name of the environment variable the key is injected under
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:ProviderListEditor fingerprint=1e28e734f27b0c6bba95f94a23825e132c7e1c36a716d7bfb654f7417fb1019a body_fp=c6dacb3a18b95b6f7b333efa7247e79d32fa509e3e9937e4fc2e24dcb65ce625 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a list of AI provider rows merged from config and Keychain state, with an add-provider input.

- `value` — current providers map from the opencode config store
- `onChange` — writes updated providers map back to the store; passes `undefined` when empty
- Calls `window.trie.secrets.listProviders()` on mount to populate Keychain-backed key status alongside config entries
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:ProviderRow fingerprint=8c6644fccced7ade09b5cab426323c3aea8be63ca3953b35a7a81b19eaf94f12 body_fp=09546106fecfed518bc680bb1ef2193b02c3c9775a3036297f3f5019b49ccd52 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a single provider card with API key save/clear (via `window.trie.secrets`), env-var name, and base URL fields.

- `info` — optional keychain state; absence means no key is stored yet
- `onConfig` — called with updated provider config object after key save or base URL change
- `onAfterKeyChange` — called after any keychain mutation to trigger parent refresh
- `envVar` — defaults to `defaultEnvVar(name)` if `info.envVar` is absent; written into `options.apiKey` as `{env:VAR}` on save
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:McpListEditor fingerprint=519453fbfc0daeb16391c1e141b1691819590d0c7fe347e1f6213a78cec77a93 body_fp=5bdfd7d9782fd2e5e7aebd9a87938a801678f35d20ff2905db6642702a7853c1 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render an editable list of MCP server entries, supporting add, remove, and per-server field editing.

- `value`: current MCP servers map from the opencode config store.
- `onChange`: called with the updated map, or `undefined` when all servers are removed.
- The `"trie"` server entry is locked (no remove/edit controls) and labelled "managed".
- New servers are added as `{ type: "remote", url: "", enabled: true }`; local servers expose a command field instead of a URL field.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:AgentTableEditor fingerprint=77fb4272bced062f9ce1953fd33bd1d32a2f93945e039e39a8cef397ceeb47a9 body_fp=b45fc48b5dabfb191a02594edaa2c14d7ca17f782164477cb230a833f7ecc1bd source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a collapsible list editor for the `agents` config map, supporting add, remove, and per-agent field editing (model, mode, description, prompt).

- `value`: current agents map; non-object values treated as empty.
- `onChange`: called with `undefined` when all agents are removed.
- Empty-string or `undefined` patch values are stripped from the agent record before writing back.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:Labeled fingerprint=0a99274d4642ac13f035ad27a16c5b51528fd5bc16f2416d86fbb9e7c65472e0 body_fp=498980c6ab47d8b2a61127b35bbb6a91f81065eb033e2a3cc8108bfd57ac80e0 source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=util -->
Render a labeled wrapper div pairing a small text label with arbitrary child content.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/Settings/editors:JsonEditor fingerprint=d2448c7521c777c04c8173bdcae92d9a8ac8f20e3025dd0c0a330959492059e3 body_fp=d7cd09af4f15cb5a06b74e095dce51e3a2ed5347a9884233d942eefae8e0d66c source_ref=6f216b37eab60789e4bdec31b5a49d14da6d3556 role=api -->
Render a resizable textarea for editing an arbitrary JSON value, parsing on each keystroke and surfacing parse errors inline.

- `value`: current JSON value; re-syncs the textarea when changed externally.
- `onChange`: called with parsed value, or `undefined` when the textarea is empty.
<!-- trie:end -->