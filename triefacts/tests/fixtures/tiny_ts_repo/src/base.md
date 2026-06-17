---
trie_version: 0.1.9
source: tests/fixtures/tiny_ts_repo/src/base.ts
file_fingerprint: 0b1dd499cb8f9482b96dc5f471d3be1e4f95e57504287abce0c8df814db52f86
last_synced_at: '2026-06-17T16:40:54Z'
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base
  lines: 2-7
- kind: property
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base.id
  lines: 3-3
- kind: method
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base.describe
  lines: 4-6
- kind: interface
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Runnable
  lines: 10-12
- kind: type
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Identifier
  lines: 14-14
- kind: enum
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status
  lines: 16-20
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Active
  lines: 17-17
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Inactive
  lines: 18-18
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Pending
  lines: 19-19
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base fingerprint=084014a1217d2fc12038de54eea2d746c7677b38db86de5fda021c63ad7158e9 body_fp=60fb9a08901df7b28e23d748806ff99d3685d48705c24c7552d4be764adfa9ff source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Base class providing a default `id` field and a `describe` method returning `"base"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base.id fingerprint=7839b83aa5cf380c062bd22a8b7bf4b40461258fc50aeb6490fc6bb04628ec46 body_fp=fe01b64d5b0ca404786a23589d3d2aa2987d0aaa119ad6f3f26798d6e7cdb0df source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
`Base.id` is a numeric attribute defaulting to `0`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base.describe fingerprint=45fdb45334ea43ba10b4993cbfe222a71c2a81176535063a1374d0aeee56f662 body_fp=8cf3b869db05d576b93911a984c55c102c3bcb49ac8dada467dbb6e0a4954ef1 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=domain -->
`Base.describe` returns the fixed string `"base"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Runnable fingerprint=b6bf9000a7b2c13d32ffc581032dfc55a586f511d6fddf5f9ad662ad6ccecd67 body_fp=871fe14686c0a25e22b3299b67be4f1ca56133a922f00eb804a7923b45c89cee source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Define the contract for objects that expose a `run` method returning `void`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Identifier fingerprint=f64aa218ca2706c04283a9824333b106222e3ee417cb458cac6f8674f862035c body_fp=c7d8f83a746be066ead8c32f8955cbf68188c6819b84ec183f14b2a9d8db4c50 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Type alias representing a value that is either a `string` or a `number`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status fingerprint=e88f41271510a518b85b30e2ef998c215cd06df07b8ac657a886b6c262ba47a5 body_fp=da6cc0553579bff71995e9d4640707e1e5060e0c2d303447736e10e0bbbb7673 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Numeric enum representing entity lifecycle states, with `Active = 1`, `Inactive = 2`, and `Pending = 3`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Active fingerprint=54428c40f07d669ce1c67082c6b9d0adbfedf8453082660e4dd6cbcafdc38bdc body_fp=7340c37eb2f924d5f5b4e0fd181961879bddfc05ceaac0414621d0d763ae2252 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Numeric member of the `Status` enum with an explicit value of `1`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Inactive fingerprint=ac7c949f1211b7814bdd28a698e6c04e05e1a83f9f86e7ad43d2086d00e98afd body_fp=246b8c453290278e942b332456521c0a7f0e3cb127723cd86899d20b7336f982 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
`Status.Inactive` is the second member of the `Status` enum, with an auto-incremented value of `2`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Pending fingerprint=331551b0de4157c9abc7b72b61b96a2a928fd6db3cdf029c1fc44b08ad633aa6 body_fp=610529340e8c41813d9ec901615bcbf3588d48414d98f9e569bcebfd6602f49d source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
Enum member of `Status` representing a pending state; auto-incremented value `3` (follows `Inactive = 2`).
<!-- trie:end -->