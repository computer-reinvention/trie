---
trie_version: 0.1.9
source: app/electron/trie-config.ts
file_fingerprint: 89dba0592276e9e6a7addcf96a4b4b72f0f504e12855ab2949ce2f4a80d6741e
last_synced_at: '2026-06-17T16:35:26Z'
defines:
- kind: function
  qualified_name: app/electron/trie-config:configPathFor
  lines: 17-19
- kind: function
  qualified_name: app/electron/trie-config:trieConfigExists
  lines: 21-23
- kind: function
  qualified_name: app/electron/trie-config:readTrieConfig
  lines: 25-33
- kind: function
  qualified_name: app/electron/trie-config:isPlainObject
  lines: 35-37
- kind: function
  qualified_name: app/electron/trie-config:deepMerge
  lines: 42-59
- kind: function
  qualified_name: app/electron/trie-config:writeTrieConfig
  lines: 64-77
- kind: function
  qualified_name: app/electron/trie-config:stripUndefined
  lines: 81-92
incoming_refs: 3
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/trie-config:configPathFor fingerprint=b83eb329d883eb21b243057ab3a911ea2d845b7180e18964c257afd637e5153a body_fp=6739ee1e480dd199341d514c85e1693674162c224928f2a623b636b285ec5605 source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=util -->
Return the absolute path to `trie.toml` inside `projectDir`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:trieConfigExists fingerprint=d7898a950bc70b484fb419c65e00789c1146e131f8ce71513fad211ede30ee1d body_fp=747f146bb7f7fd79dc93368609aeffb35c1cff26d828ca90d84a2e9a65a3a687 source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=io -->
Return whether `trie.toml` exists in the given project directory.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:readTrieConfig fingerprint=72d123ff0c056a3c3fbc4c47248e2cd69df078f17df9fe26703a0330ffd2c95f body_fp=06ea7fe6c7114c37b4218899fcc091c86851a9347786cae6fa52b11c127aadee source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=io -->
Parse and return the `trie.toml` file in `projectDir` as a plain object, returning `{}` if the file is absent or unparseable.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:isPlainObject fingerprint=94d59d70abfa8d6fe8ae1c06b65656e0bd166f38c552aa816a09a3e62227bc03 body_fp=5683668192c6ff03134173e0c38380f557164ce1a025e13686b981a433ccf4f1 source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=util -->
Type-guard that returns `true` when `v` is a non-null, non-array plain object.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:deepMerge fingerprint=5cfcf3ccaac7da590e712bb45d2b3aca08ec5b2181579bed5140d22ac68ae61b body_fp=935f97ef96beb3f78f5db5de9210fe5cef50f088802f992d2fec336a2583f4bd source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=util -->
Recursively merges `delta` into `base`, returning a new object without mutating either argument.

- `delta` null value: deletes the corresponding key from the result
- Plain objects: merged recursively; arrays and scalars replace the base value wholesale
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:writeTrieConfig fingerprint=17d97d3ef4a11ce4244eb76bc1f57adcb2e3aeb024d06ded881d9c87ff77dc3d body_fp=b88ff8ff94ea45387ba1b516aba58848368c4465919c6be94d283fe5ba1f6ddc source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=io -->
Merges `delta` into the existing `trie.toml` in `projectDir` and writes the result back to disk.

- `delta`: partial config changes; `null` values delete keys, objects merge recursively.
- Throws `Error` if `trie.toml` does not exist; will not create a new file.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/trie-config:stripUndefined fingerprint=1d3d8d8c2bfe5ec270efffea0069343fd57b35833c9a96cf7b54d86dd2436c68 body_fp=4b59f6dce7235d56ffe2dbef7571bd8462ad1070fd35185debc9cfbfbfb84fd0 source_ref=fd3800ff27518fb763b782f45724875c8ed49227 role=util -->
Recursively remove all keys with `undefined` values from a nested object or array so the TOML serializer never receives an `undefined` value.
<!-- trie:end -->