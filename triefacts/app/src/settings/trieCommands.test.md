---
trie_version: 0.1.9
source: app/src/settings/trieCommands.test.ts
file_fingerprint: 22c3a99d19a9c5766a8580bffc510ddbf93ce74d73e4c0f26d7fbe97218ff37b
last_synced_at: '2026-06-17T16:39:48Z'
defines:
- kind: module
  qualified_name: app/src/settings/trieCommands.test:__module__
  lines: 1-64
- kind: constant
  qualified_name: app/src/settings/trieCommands.test:sync
  lines: 4-4
- kind: constant
  qualified_name: app/src/settings/trieCommands.test:refresh
  lines: 5-5
- kind: constant
  qualified_name: app/src/settings/trieCommands.test:init
  lines: 6-6
incoming_refs: 0
outgoing_refs: 3
---
<!-- trie:section symbol=app/src/settings/trieCommands.test:__module__ fingerprint=9b9a84620fb85ce016491625708bc0b77a8de7d4424a60795e7131cd66ddd5a7 body_fp=e95fdb391c503e596664daed964561eb636c052286cbd97a2a3965fae89c7fcf source_ref=87518041d606ba5273595d7beaff89b9ce736ef9 role=test -->
Test suite for `buildArgs` and `TRIE_COMMANDS` covering flag emission, ordering, `fixedArgs` prepending, and uniqueness invariants.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands.test:sync fingerprint=bdb15b8c3f1a99bcf0b1009375319e433c6245e437a598ecd2826a597ec7e9da body_fp=211a07b72677c2e3ba27857eabcfcc381f7daa92b71ff9377beabf1e961596a6 source_ref=87518041d606ba5273595d7beaff89b9ce736ef9 role=test -->
Test fixture holding the `"sync"` command definition extracted from `TRIE_COMMANDS` for use across `buildArgs` test cases.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands.test:refresh fingerprint=4160372179c8e93dbe830f41c73787d3851d52207d0f79c074546212d0762d70 body_fp=d5f180d96f86e51a7c51d6f619d5fe4115b4180c583024c8b2e251e88b6b0daa source_ref=87518041d606ba5273595d7beaff89b9ce736ef9 role=test -->
Test fixture holding the `"refresh"` command definition extracted from `TRIE_COMMANDS` for use in `buildArgs` assertions.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands.test:init fingerprint=a003073b060645621d3df3651fc9243e7e23dea8cee1fa8a0d444316426d3eb7 body_fp=036078e4b8be085613bc5d6e1cc0893bbe43fb6c838d1b497cf8bd0b3961a14d source_ref=87518041d606ba5273595d7beaff89b9ce736ef9 role=test -->
Test fixture holding the `"init"` command definition extracted from `TRIE_COMMANDS` for use in `buildArgs` tests.
<!-- trie:end -->