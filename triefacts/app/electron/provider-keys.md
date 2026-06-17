---
trie_version: 0.1.9
source: app/electron/provider-keys.ts
file_fingerprint: 4a7e1e107b16b051c824ff80fae8697d71147f46c3010275a61b90e613a6891a
last_synced_at: '2026-06-17T16:35:22Z'
defines:
- kind: constant
  qualified_name: app/electron/provider-keys:KEYCHAIN_SERVICE
  lines: 7-7
- kind: constant
  qualified_name: app/electron/provider-keys:KEY_PREFIX
  lines: 8-8
- kind: constant
  qualified_name: app/electron/provider-keys:ENV_PREFIX
  lines: 9-9
- kind: constant
  qualified_name: app/electron/provider-keys:PROVIDER_ENV_DEFAULTS
  lines: 12-22
- kind: function
  qualified_name: app/electron/provider-keys:defaultEnvVar
  lines: 24-29
- kind: constant
  qualified_name: app/electron/provider-keys:keytarModule
  lines: 31-31
- kind: function
  qualified_name: app/electron/provider-keys:getKeytar
  lines: 32-35
- kind: interface
  qualified_name: app/electron/provider-keys:ProviderKeyInfo
  lines: 37-41
- kind: function
  qualified_name: app/electron/provider-keys:listProviderKeys
  lines: 44-62
- kind: function
  qualified_name: app/electron/provider-keys:hasProviderKey
  lines: 64-72
- kind: function
  qualified_name: app/electron/provider-keys:getEnvVar
  lines: 74-82
- kind: function
  qualified_name: app/electron/provider-keys:setProviderKey
  lines: 86-107
- kind: function
  qualified_name: app/electron/provider-keys:deleteProviderKey
  lines: 109-118
- kind: function
  qualified_name: app/electron/provider-keys:providerEnvForSpawn
  lines: 121-135
incoming_refs: 6
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/provider-keys:KEYCHAIN_SERVICE fingerprint=234a79066185fb0ec268541d29b6d65b31b0a6c48f91adbe12fa1979ec57ebf5 body_fp=69eb2889dc8603b25950fd2d74d5f507feecd36e6b9e25b76b1c5be42fb50440 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=config -->
Keychain service name used as the namespace for all stored provider credentials.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:KEY_PREFIX fingerprint=4d645245396c00ad439ade77145c3acd792bd8fa6438c38c6d01367ad0585146 body_fp=63f11d5f270bdd6728e799372e372e1771ca83e07916ac847dfa1b3cb9e2e8d9 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=config -->
Keychain account prefix used to namespace stored provider API keys, concatenated with the provider name as the account identifier.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:ENV_PREFIX fingerprint=655a3547d499f317a1c9471182eedf4600d1a8903a9023ab03ca2f6f431d94e8 body_fp=6b29b4ea01691d017936e99f7c5a6b2ca686e92344526795453063a53ebdc0f7 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=config -->
Keychain account prefix for storing the env-var name associated with a provider key.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:PROVIDER_ENV_DEFAULTS fingerprint=84f2b6f319ed6c4b8e8e866176cf2532c5b0ee6036444d5d0206ebbbb632690c body_fp=9d51712b2d0768d5ae9dc9596d3649b9a4fc9a1123aa847ee3603fb7b0f081dd source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=config -->
Maps known provider identifiers to their canonical API key environment variable names, mirroring `src/settings/opencodeSchema.ts`.

- `gemini` and `google` both resolve to `GOOGLE_GENERATIVE_AI_API_KEY`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:defaultEnvVar fingerprint=1498444ab62866bb5f908ffd7f3e2bc9e79375f67ee753a407151350c74821b4 body_fp=188837b69379c95164b13da6d3a426e5feab77ab7074a3ca6ce29bfcc6baac7b source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=util -->
Return the default environment variable name for a provider, falling back to `<PROVIDER>_API_KEY` if not in `PROVIDER_ENV_DEFAULTS`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:keytarModule fingerprint=1268e94d62cb55b11b4dd4d12d2957d5928f0aa951ab9db9e569d63880e9db62 body_fp=312ae6db77e3646da97c3f005d4cf0549dbc34ec736a10ac14c948a711008459 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=config -->
Module-level cache holding the lazily-imported `keytar` instance, or `null` before first use.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:getKeytar fingerprint=53aadb48c3317e0b16effbf0706b01f15d1d0af5a532f83417a84407365a3cc2 body_fp=b9a13cd1dc8f7ca9a5e49d342bfb11a7c71b0aa1cc69a1eab621d8fcdd502545 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=util -->
Lazily imports and caches the `keytar` native module, returning the singleton on subsequent calls.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:ProviderKeyInfo fingerprint=bb6b8b59dbbc157c8fa5e2e10165727d8239cd6dfd06038ba8585c629a6f25a2 body_fp=837fc0ddc53a123cfc65aed589287646d31e8de3487a4c0f63074cb967aebc0f source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=model -->
Shape returned by `listProviderKeys` describing one stored provider key entry.

- `hasKey`: `true` when a non-empty secret exists in the keychain.
- `envVar`: resolved env var name (custom override or default).
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:listProviderKeys fingerprint=550e2ed07e76d9c8270497f43da163c7809bd49493db4bfbb67dbcb15cd4099a body_fp=09c60b82a62935f7c1acea9d92e99a6b0f09036b2a51d744420f7c4dcb81fa08 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=io -->
Return all providers with a stored keychain entry, each with their resolved env var name.

- Returns `[]` on any keychain error rather than throwing.
- `hasKey` reflects whether a non-empty password is stored for that provider.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:hasProviderKey fingerprint=c9688425743a6cfe181921e7c1ba1596803b789eaaf388baee76d6ee79f9bbb0 body_fp=a8c1f5a0c0fa2ea74d97902747a30a7763626c12aab3cf9f0dcb9cc02943426c source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=io -->
Check whether a non-empty API key is stored in the keychain for the given provider.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:getEnvVar fingerprint=817fa788bad6ed4ba230b6986ea58441f89c29bfe1e9eb2f4c2333cdf4ae6176 body_fp=816eb29a0d8cb3b429e2103aed36b47b6717a210a3a55c884fbb8bd38a724f05 source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=persistence -->
Resolve the env-var name for a provider, returning any keychain-stored custom value or falling back to `defaultEnvVar`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:setProviderKey fingerprint=5e370771d11d8dd0a15872d33184c4b006c7c0ac3a329322864552accb3e75fd body_fp=1b99a1ac474c421c61e2647e5cb55264e3b4f84ebed62fc0ad273e798529f14f source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=io -->
Store or delete a provider API key and its associated env-var name in the system keychain.

- `key`: empty string triggers deletion of the stored secret instead of a write.
- `envVar`: omitted or equal to the provider default causes the custom env-var record to be deleted.
- Returns `{ ok: false, error }` if any keychain operation throws.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:deleteProviderKey fingerprint=3b5bb1dbfff70313b568e4a44eaaab0b443fde3bae4c0864ac0c147fc4945e25 body_fp=8c7c4dc6928157280352f8306b4ea71c8cd76e126e3f7a6342513baa38666dea source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=io -->
Delete both the stored key and env-var name for the given provider from the keychain.

- `ok`: `false` if any keychain operation throws, `true` otherwise.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/provider-keys:providerEnvForSpawn fingerprint=bedf1a199589154dd720edae3fb9c983405ad552bd9de9ca36ce1953cd3d988c body_fp=766f9ca884bc1b61642a00af3e4f45e06d8f844cd98d1bbb74acd50299af2d2f source_ref=339b08dec0a89adbc8abe1731f48e5ac3a5c1d0f role=io -->
Build a `Record<string, string>` mapping each stored provider's resolved env-var name to its keychain secret, for injection into the opencode child process environment.

- Returns an empty object silently if the keychain is unavailable.
<!-- trie:end -->