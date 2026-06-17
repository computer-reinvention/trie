---
trie_version: 0.1.9
source: app/src/settings/opencodeSchema.ts
file_fingerprint: 9c6839edf3cd65ea94fa070abf1b33552a64f3970078e1704d2e170fe845af6c
last_synced_at: '2026-06-17T16:40:09Z'
defines:
- kind: type
  qualified_name: app/src/settings/opencodeSchema:OcFieldType
  lines: 15-26
- kind: interface
  qualified_name: app/src/settings/opencodeSchema:OcFieldDef
  lines: 28-47
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:PERMISSION_TOOLS
  lines: 49-60
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:PERMISSION_CHOICES
  lines: 62-66
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:OC_FIELDS
  lines: 68-368
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:OC_CATEGORIES
  lines: 370-370
- kind: function
  qualified_name: app/src/settings/opencodeSchema:ocFieldByPointer
  lines: 372-374
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:MANAGED_TOP_KEYS
  lines: 377-379
- kind: constant
  qualified_name: app/src/settings/opencodeSchema:PROVIDER_ENV_DEFAULTS
  lines: 383-393
- kind: function
  qualified_name: app/src/settings/opencodeSchema:defaultEnvVar
  lines: 395-397
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/opencodeSchema:OcFieldType fingerprint=a1e6cbcac613c7dde3ca6189bb7163d6662f7c123e72c1d30ac295ad94e1f13a body_fp=ab9512d98cd5ed6815d1f7921dc1125b7ba819a795eb597d8bf361df0c4fe963 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=model -->
Union of string literals enumerating every supported field-editor widget type for `OcFieldDef`.

- `stringList` — edits a `string[]` (e.g. instructions, ignore globs)
- `enumMap` — edits `{ key: oneOf(enum) }` (e.g. permission matrix)
- `toggleMap` — edits `{ key: boolean }` (e.g. tool on/off switches)
- `providerList` — provider entries with Keychain-backed `apiKey`
- `mcpList` — MCP server entries (local or remote)
- `agentTable` — per-agent override sub-editor
- `json` — arbitrary blob edited as raw JSONC
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:OcFieldDef fingerprint=11ebe0b78372d2adcfdf1ad22dd767b93d215067117850f5646ac8b00533931b body_fp=50cfdc6d3d32cd1329b1b68cba74451458265c913cdb21ddb678473d7c8fc429 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=model -->
Describes a single editable field in the opencode Settings UI, mapping a JSON pointer to its display metadata and editor constraints.

- `pointer`: dot-separated path into `opencode.json` (e.g. `"attachment.image.max_width"`)
- `restart`: when `true`, changing this field requires restarting the opencode server
- `enum`: allowed values for `"enum"` type fields
- `mapKeys` / `mapChoices`: row keys and allowed values for `"enumMap"` fields
- `toggleKeys`: tool names to render for `"toggleMap"` fields
- `min` / `max` / `step`: numeric bounds and increment for `"number"` fields
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:PERMISSION_TOOLS fingerprint=fcfdbb83864743cd41e8b957af54b66214f6c066f4e83876b14c332da61add54 body_fp=9a1dbf2fa6e7cca2ca0b260e8f78f98392c3c3fb01bf18829e421d704488010d source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Module-private list of tool names used as row keys in the `permission` `enumMap` field definition.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:PERMISSION_CHOICES fingerprint=162fdc2e6049a528d848f0437f9a395a29be0006c541ebb7bf9c58411eabb0dd body_fp=a36cf51b0ece10f089f8aff5787724a0e4f52132668bc2cf43f1dea8591f97b6 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Module-private label/value pairs for the three permission states used as `mapChoices` in the `permission` field definition.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:OC_FIELDS fingerprint=eaf1c60ae4c8537c83b37c65ae8444d5cdcc7e69f76ad0860f76194e66dea039 body_fp=3ab2ebd3fd2febcc1d086d86e7ac8568706b4be6040423f2d709f26a5de1ca78 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Master registry of all `OcFieldDef` entries the Settings UI exposes, grouped into categories: Model, Permissions, Context, Providers, Integrations, Agents, Behavior, and Advanced.

- Each entry's `pointer` is a dot-separated JSON path into `opencode.json`; keys absent here are never modified.
- Entries with `restart: true` require the opencode server to be restarted for the change to take effect.
- `permission` uses `enumMap` with `PERMISSION_TOOLS` rows and allow/ask/deny choices.
- `provider` entries store API keys in the system Keychain, never in `opencode.json`.
- `mcp` excludes the auto-managed trie server entry.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:OC_CATEGORIES fingerprint=7b0763132e5a6e08f4413f1a683c8c2c1bdd01875988283ad7ae524818dbce2d body_fp=f6415ba8fc27128164dff6956b3661c2d8983d51879aa91eaf982834dc93b2d8 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Deduplicated ordered list of category strings derived from `OC_FIELDS`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:ocFieldByPointer fingerprint=6545bbcbe02fc1044270df6c92f0f0a8201eaf5d1c0c54c5dee538599d4ba566 body_fp=15690e0257de21690cde2cc96d18b12d055786f55a3bd3c2ad447fdc403ac66c source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=util -->
Look up a field definition in `OC_FIELDS` by its dot-separated JSON pointer string.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:MANAGED_TOP_KEYS fingerprint=ea21937447a93d4b3b4ecb64bfde240c2a00ed9efeb72622535ea2f5f74335ef body_fp=112bb1d45093a4c916def0d0c1b1402366b659d9a1a0ccf7c69ec13407a68c44 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Deduplicated array of top-level `opencode.json` keys derived from `OC_FIELDS`, used by the merge writer to identify managed keys.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:PROVIDER_ENV_DEFAULTS fingerprint=04049a25e8dc39258aa688ef405a399bb72925beae4ec889f85464c7003635ce body_fp=57d31db41da8c50f491547b2a9e562f26725310cff39325d88d5278d8eebdb45 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=config -->
Maps well-known provider names to their canonical Keychain-injected API key environment variable names.

- `google` and `gemini` both map to `GOOGLE_GENERATIVE_AI_API_KEY`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/opencodeSchema:defaultEnvVar fingerprint=9da6589118ec49c68f6545f7c24466185550144ead49438b4273fcd2c4474657 body_fp=3d74f142a59fcdaa1b93020567586f5052f90648154460283bc3a2d3b4e216d3 source_ref=a9d1540f7438c746bee626f11d3d594e53973ee8 role=util -->
Return the Keychain env var name for `provider`, falling back to `<UPPER_SNAKE>_API_KEY` if not in `PROVIDER_ENV_DEFAULTS`.
<!-- trie:end -->