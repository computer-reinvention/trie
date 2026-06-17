---
trie_version: 0.1.9
source: tests/fixtures/tiny_ts_repo/src/app.ts
file_fingerprint: fc8d4bd1b1a9eb0fd0d3a0ba465f72523348f08e0e56d25c5f9878a311a0e88b
last_synced_at: '2026-06-17T16:40:45Z'
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App
  lines: 9-20
- kind: property
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App.status
  lines: 10-10
- kind: method
  qualified_name: tests/fixtures/tiny_ts_repo/src/app:App.run
  lines: 12-19
incoming_refs: 0
outgoing_refs: 12
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App fingerprint=edc337736b3ea4c1d2026de2ffecc9bcccfbeb18d539caa1f1adb67c91510a9e body_fp=936901c706ab1ae79cbed06356faf96a506d53227f80a5878c0bcb6ffc7f8e8b source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=orchestration -->
Application entry class extending `Base` and implementing `Runnable`; its `run` method wires together utilities, store, core greeting, and external dependencies.

- `status`: initialised to `Status.Active` on construction.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App.status fingerprint=38f52b43cfa7903e397adb637010d689d749175d6b2c6e4f558fbdcf0c3afde7 body_fp=852e4453dd9543633ce4724b89ac76cf4d315527758f3f8ee2a73bab62d43efb source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=model -->
`App.status` is an attribute holding the current `Status` of the application, defaulting to `Status.Active`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/app:App.run fingerprint=3a75e618ab4331aa074d2dc0cc75196247723537dfbd2b96955c11797570553f body_fp=f01d12f35bae1ee88e65e5942786af958c055290d7254888e04e2a31e2c009db source_ref=c5e3e0c2dee826ac11d2412c101a788e80ba6a2a role=orchestration -->
Execute `App`'s main logic by calling all wired utilities, store, core, and external dependencies in sequence.
<!-- trie:end -->