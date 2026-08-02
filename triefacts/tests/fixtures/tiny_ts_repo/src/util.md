---
trie_version: 0.3.0
source: tests/fixtures/tiny_ts_repo/src/util.ts
file_fingerprint: 3bbd02836fe9ac53a166c3605b37843efeff73581e466a67b4bf28b428144ea5
last_synced_at: '2026-06-17T16:40:51Z'
defines:
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:double
  lines: 2-4
  signature: 'function double(n: number): number'
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:secretHelper
  lines: 7-9
  signature: 'function secretHelper(n: number): number'
- kind: constant
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:PI
  lines: 11-11
- kind: function
  qualified_name: tests/fixtures/tiny_ts_repo/src/util:compute
  lines: 13-13
  signature: '(x: number): number =>'
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:double fingerprint=7eb61e3acb5cfc0dcf3fb8c675fe0c83dc1fac88d0b96390557adc5775f8d37f body_fp=fb2139007f410cc54d6e6f29133ec4138909eebd70b63bad797db00c354d25de source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
## `function double(n: number): number`

Return `n` multiplied by 2.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:secretHelper fingerprint=f6635d952012435d08170cf8998895d5d9b321f3c8d602e13743b35d5adddd3f body_fp=87c9385e62232700dcc79b51e8a8d5d1862f7eb95912b8fad02a1b72d379a1fa source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
## `function secretHelper(n: number): number`

Return `n - 1`; unexported helper used internally within `util.ts`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:PI fingerprint=2575d21d1bd5b58502b3cafb588cf430be242adb17ad524098933aa15490003d body_fp=aa230c82930e47b472e3fb15140a40ecfdbf2f8c537cf444aeffe71737e43cad source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=model -->
Exported constant holding an approximate value of π (3.14).
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/util:compute fingerprint=24f1699060b681871d710be00fbc4b600c91cf607a7ef335d7ec2cccd3b8ee35 body_fp=c114645cfac98dc8e956759d2451d04d147714d94ed45e8174b7fb2e6d4899c6 source_ref=5e55d71d47d458f9d673b5f41438ee99c1c12681 role=util -->
## `(x: number): number =>`

Return the sum of `double(x)` and `secretHelper(x)` for a given number `x`.
<!-- trie:end -->