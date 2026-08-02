---
trie_version: 0.3.0
source: tests/fixtures/tiny_ts_repo/src/types/external.d.ts
file_fingerprint: fac4b7bec92c7f8a7ff6283100aa6468caa0b6da504bdf30e89da39dd54a98a2
last_synced_at: '2026-06-17T16:40:53Z'
defines:
- kind: module
  qualified_name: lang-map:__module__
  lines: 1-7
- kind: interface
  qualified_name: lang-map:MapReturn
  lines: 3-5
  signature: interface MapReturn
- kind: function
  qualified_name: lang-map:map
  lines: 6-6
  signature: 'function map(): MapReturn'
- kind: constant
  qualified_name: tests/fixtures/tiny_ts_repo/src/types/external:BUILD_ID
  lines: 9-9
incoming_refs: 2
outgoing_refs: 0
---
<!-- trie:section symbol=lang-map:__module__ fingerprint=6cbea2cff8765848545c0cad9bd60373740418ed5b90745b5268dc73f7c895bc body_fp=c13ab0bac5692f70e10bcfd1fe10f3e71d0ab71693061be392823dfe0533a1bd source_ref=3782dd198a5340569daae22c6becc4cc9f007937 role=model -->
Ambient module declaration for `lang-map`, exposing `MapReturn` and the `map()` factory function.

- `MapReturn.extensions`: maps language names to arrays of file extensions.
<!-- trie:end -->
<!-- trie:section symbol=lang-map:MapReturn fingerprint=72b4132a35c39b84a1650e3367ec84817f6bf74dab878f5c1005a11618068c96 body_fp=b959b6934031bf4f6c4041a27860770c42cdc7cc9728892a8cb032d9598afaec source_ref=3782dd198a5340569daae22c6becc4cc9f007937 role=model -->
## `interface MapReturn`

Interface describing the return value of `map()` in the `lang-map` module.

- `extensions`: maps a language name to its associated file extensions.
<!-- trie:end -->
<!-- trie:section symbol=lang-map:map fingerprint=2254bc47188ae061945f86d52646c18eabd1ca72577e7b93ffed81dbe3de3637 body_fp=abf10dbfd3ab352407b0610b803d3ca2afae29e9bc529ab6e2761dd6a94ae701 source_ref=3782dd198a5340569daae22c6becc4cc9f007937 role=domain -->
## `function map(): MapReturn`

Return a `MapReturn` object containing language-to-extensions mappings.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/types/external:BUILD_ID fingerprint=2b56261fcc84f936b33df2707000a8aad7f7220ef62e0d3ad2fe583717966950 body_fp=ce966e2e8440cbd52381bf88f58e5ef874d46ab73abe5520fcb20074a8d9b783 source_ref=3782dd198a5340569daae22c6becc4cc9f007937 role=config -->
Ambient constant declaring the global `BUILD_ID` string injected at build time.
<!-- trie:end -->