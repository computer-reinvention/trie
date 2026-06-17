---
trie_version: 0.1.9
source: app/electron/opencode-config.ts
file_fingerprint: a5342e9471f32686d8e7d9d1f170219fbc63776ec55c4d15b6bd56f17803766a
last_synced_at: '2026-06-17T16:35:12Z'
defines:
- kind: interface
  qualified_name: app/electron/opencode-config:TrieMcpEntry
  lines: 13-16
- kind: function
  qualified_name: app/electron/opencode-config:configPathFor
  lines: 18-20
- kind: function
  qualified_name: app/electron/opencode-config:parseTolerant
  lines: 24-39
- kind: function
  qualified_name: app/electron/opencode-config:readOpencodeConfig
  lines: 41-49
- kind: function
  qualified_name: app/electron/opencode-config:isPlainObject
  lines: 51-53
- kind: function
  qualified_name: app/electron/opencode-config:deepMerge
  lines: 58-75
- kind: function
  qualified_name: app/electron/opencode-config:withTrieMcp
  lines: 77-88
- kind: function
  qualified_name: app/electron/opencode-config:writeOpencodeConfig
  lines: 92-105
- kind: function
  qualified_name: app/electron/opencode-config:ensureTrieMcp
  lines: 109-111
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=app/electron/opencode-config:TrieMcpEntry fingerprint=e8b4fea13faae7aba85b2574842c46d648652de7c32318318a474a74c8d29853 body_fp=16bbaccfa60f2695697bc380220056223d97fae36adbcabdc7008a16191332d6 source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=model -->
Holds the two inputs needed to construct the trie MCP command vector written into `opencode.json`.

- `trieMcpBin`: filesystem path to the trie MCP executable
- `projectDir`: absolute path to the project root passed as the second CLI argument
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:configPathFor fingerprint=a9b3f9522425d9ff41010a1794118b9df4eac60eb6b370021fcc3477b404beee body_fp=225e230554484f508763297601c4d84fc2bd269189f89aa839ba3aa1f21514ac source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=util -->
Return the absolute path to `.opencode/opencode.json` within `projectDir`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:parseTolerant fingerprint=f9f7854e436eac21fb8604b7468042e025c601316803624d50ae2970051f569c body_fp=c77e630f51a0f7f3c1e0a53d3204bb2b81ebd8e576ccba4f060d20536fd9b7fd source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=parsing -->
Parse a JSON or JSONC string, stripping `//`/`/* */` comments and trailing commas before retrying; returns `{}` on any failure.

- `text` — raw file contents, may contain JSONC syntax
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:readOpencodeConfig fingerprint=7e90471c946b3645f86f5562d2d613037bc30756121173f7fd779d0f381d7cdc body_fp=7d5a258eae02cd50791b9404446112714294494adb86f95cf92b94de44381004 source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=io -->
Read and tolerantly parse `.opencode/opencode.json` for the given project directory, returning `{}` on missing file or any error.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:isPlainObject fingerprint=94d59d70abfa8d6fe8ae1c06b65656e0bd166f38c552aa816a09a3e62227bc03 body_fp=aeb8fe6b9ebd44f2304a1afa81544aaba40b754591d3fc59759f7b59adaa53fc source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=util -->
Return `true` if `v` is a non-null, non-array object, narrowing its type to `Record<string, unknown>`.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:deepMerge fingerprint=5cfcf3ccaac7da590e712bb45d2b3aca08ec5b2181579bed5140d22ac68ae61b body_fp=3c388c83966c22497657f22b2d2ec209824f59b006aa9c4dd1707c29617dde23 source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=util -->
Recursively merge `delta` into `base`, returning a new object without mutating either input.

- `delta` value of `null` deletes the corresponding key from the result.
- Plain-object values merge recursively; arrays and scalars replace wholesale.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:withTrieMcp fingerprint=172c0a4911181f0be2488a5cd48ccad15c0b0ee2e4e3d43f5f64686a9551c646 body_fp=2539772dae7f5dd3b8768ff5722c006f4c775ed8345bc97730de4d8219c2d773 source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=domain -->
Return a copy of `config` with the trie MCP entry unconditionally asserted under `config.mcp.trie`.

- `trie.trieMcpBin` — path to the trie MCP binary, used as the first command element.
- `trie.projectDir` — passed as the second command element; existing `mcp` keys are preserved.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:writeOpencodeConfig fingerprint=0444a8608791a34daa1dee38774590a1b961bd7d42bc74e40b8161eda96ee23a body_fp=65c9e0cb57eebb0c0d3f2b2ee8ecef6564379ee6fc216f18719469806f195303 source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=io -->
Merge `delta` into the project's `.opencode/opencode.json`, re-assert the trie MCP entry, and write the result back to disk.

- `delta` — partial config keys to merge; `null` values delete existing keys.
- `trie` — supplies the trie MCP binary path and project directory to always re-assert.
- Creates `.opencode/` directory if absent.
<!-- trie:end -->
<!-- trie:section symbol=app/electron/opencode-config:ensureTrieMcp fingerprint=5634f7c5915d81a12461f2574b55faa1f512f582c3ac805015606919e104335d body_fp=829248716e2c0d5fd7aa564251d7022ef8ccbe245f9a8161cafb7e8ac54f0a8d source_ref=cd9c95ccce2ed2a7f7f6850e692f37ccd1b0d4e5 role=io -->
Ensure the trie MCP entry exists in `projectDir`'s `opencode.json` by calling `writeOpencodeConfig` with an empty delta.
<!-- trie:end -->