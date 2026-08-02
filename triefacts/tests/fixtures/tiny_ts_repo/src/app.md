---
trie_version: 0.3.0
source: tests/fixtures/tiny_ts_repo/src/app.ts
file_fingerprint: fc8d4bd1b1a9eb0fd0d3a0ba465f72523348f08e0e56d25c5f9878a311a0e88b
last_synced_at: '2026-06-17T16:40:45Z'
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App
  lines: 9-20
  signature: class App extends Base implements Runnable
- kind: property
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App.status
  lines: 10-10
  signature: 'status: Status = Status.Active'
- kind: method
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App.run
  lines: 12-19
  signature: 'run(): void'
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App fingerprint=edc337736b3ea4c1d2026de2ffecc9bcccfbeb18d539caa1f1adb67c91510a9e body_fp=a18c654036aacdf2297a7032ff9c8f358835015b225aa4d7b0bc40d6f538aa4a source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=orchestration -->
## `class App extends Base implements Runnable`

Application entry class extending `Base` and implementing `Runnable`; its `run` method wires together utilities, store, core greeting, and external dependencies.

- `status`: initialised to `Status.Active` on construction.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App.status fingerprint=38f52b43cfa7903e397adb637010d689d749175d6b2c6e4f558fbdcf0c3afde7 body_fp=81e517560564549cc6c5ffafd1564bb2c05a41f2d8119e522cce21a0ee84c6de source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=model -->
## `status: Status = Status.Active`

`App.status` is an attribute holding the current `Status` of the application, defaulting to `Status.Active`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App.run fingerprint=3a75e618ab4331aa074d2dc0cc75196247723537dfbd2b96955c11797570553f body_fp=3ccf389466656f9f941571da9f325c447a6003cf8a79bcdd7df5fbb6d8dacc51 source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=orchestration -->
## `run(): void`

Execute `App`'s main logic by calling all wired utilities, store, core, and external dependencies in sequence.
<!-- trie:end -->