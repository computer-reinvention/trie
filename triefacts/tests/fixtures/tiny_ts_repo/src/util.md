---
trie_version: 0.1.9
source: tests/fixtures/tiny_ts_repo/src/util.ts
file_fingerprint: 3bbd02836fe9ac53a166c3605b37843efeff73581e466a67b4bf28b428144ea5
last_synced_at: '2026-06-17T16:40:51Z'
defines:
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:double
  lines: 2-4
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:secretHelper
  lines: 7-9
- kind: constant
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:PI
  lines: 11-11
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:compute
  lines: 13-13
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:double fingerprint=7eb61e3acb5cfc0dcf3fb8c675fe0c83dc1fac88d0b96390557adc5775f8d37f body_fp=10b3bb3991b9b53a3c4d4478f6409b4f3f8c39f37644e2d2ce0cffa50c6b2a10 source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
Return `n` multiplied by 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:secretHelper fingerprint=f6635d952012435d08170cf8998895d5d9b321f3c8d602e13743b35d5adddd3f body_fp=94c2112547d2db4ef9d20c5c657add73fcc491d9b1c276375420a14ec0ad11dc source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
Return `n - 1`; unexported helper used internally within `util.ts`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:PI fingerprint=2575d21d1bd5b58502b3cafb588cf430be242adb17ad524098933aa15490003d body_fp=aa230c82930e47b472e3fb15140a40ecfdbf2f8c537cf444aeffe71737e43cad source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=model -->
Exported constant holding an approximate value of π (3.14).
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:compute fingerprint=24f1699060b681871d710be00fbc4b600c91cf607a7ef335d7ec2cccd3b8ee35 body_fp=8e987f6e70e44c8820bc3f909d0c3f3519b54dd808d3bd6afb61dfed12b391b0 source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
Return the sum of `double(x)` and `secretHelper(x)` for a given number `x`.
<!-- trie:end -->