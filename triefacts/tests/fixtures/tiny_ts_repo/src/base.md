---
trie_version: 0.3.0
source: tests/fixtures/tiny_ts_repo/src/base.ts
file_fingerprint: 0b1dd499cb8f9482b96dc5f471d3be1e4f95e57504287abce0c8df814db52f86
last_synced_at: '2026-06-17T16:40:54Z'
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base
  lines: 2-7
  signature: class Base
- kind: property
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base.id
  lines: 3-3
  signature: 'id: number = 0'
- kind: method
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Base.describe
  lines: 4-6
  signature: 'describe(): string'
- kind: interface
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Runnable
  lines: 10-12
  signature: interface Runnable
- kind: type
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Identifier
  lines: 14-14
  signature: type Identifier = string | number
- kind: enum
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status
  lines: 16-20
  signature: enum Status
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Active
  lines: 17-17
  signature: Active = 1
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Inactive
  lines: 18-18
  signature: Inactive
- kind: enum_member
  qualified_name: tests/fixtures/tiny_ts_repo/src/base:Status.Pending
  lines: 19-19
  signature: Pending
incoming_refs: 4
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base fingerprint=084014a1217d2fc12038de54eea2d746c7677b38db86de5fda021c63ad7158e9 body_fp=512255e84e26e87aa50185964d56e979f2bd5fb43721f01317123b7793c7ef61 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `class Base`

Base class providing a default `id` field and a `describe` method returning `"base"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base.id fingerprint=7839b83aa5cf380c062bd22a8b7bf4b40461258fc50aeb6490fc6bb04628ec46 body_fp=ecf95d499f0c6442b1e6ce0d4a1669de40e288e1b737454c87b99240503d5dce source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `id: number = 0`

`Base.id` is a numeric attribute defaulting to `0`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Base.describe fingerprint=45fdb45334ea43ba10b4993cbfe222a71c2a81176535063a1374d0aeee56f662 body_fp=2c2db9ad159cabf96899e353b29ee636eeb6e4cdb896ed7c636119c5af67910f source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=domain -->
## `describe(): string`

`Base.describe` returns the fixed string `"base"`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Runnable fingerprint=b6bf9000a7b2c13d32ffc581032dfc55a586f511d6fddf5f9ad662ad6ccecd67 body_fp=a9b5fc334b663ca0e8be16d2f20cc142431cb26ac406c5695bb8c77763371bb8 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `interface Runnable`

Define the contract for objects that expose a `run` method returning `void`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Identifier fingerprint=f64aa218ca2706c04283a9824333b106222e3ee417cb458cac6f8674f862035c body_fp=bf92006e97d2bfec61f54a9b04b232503c200884dd1b35d21b2334627b2a9f7c source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `type Identifier = string | number`

Type alias representing a value that is either a `string` or a `number`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status fingerprint=e88f41271510a518b85b30e2ef998c215cd06df07b8ac657a886b6c262ba47a5 body_fp=7f3fe687711fcb864518eb5c3d0684e8cc2ea8ebdfa68101e3211b6044ba6d44 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `enum Status`

Numeric enum representing entity lifecycle states, with `Active = 1`, `Inactive = 2`, and `Pending = 3`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Active fingerprint=54428c40f07d669ce1c67082c6b9d0adbfedf8453082660e4dd6cbcafdc38bdc body_fp=326f1b632c3dd5e51c2df8d3bc79080485cd6694b27a5343cfd36d116650571f source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `Active = 1`

Numeric member of the `Status` enum with an explicit value of `1`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Inactive fingerprint=ac7c949f1211b7814bdd28a698e6c04e05e1a83f9f86e7ad43d2086d00e98afd body_fp=aaa8ac99323d9df88d88a791fa21ed83fbed2701c272c1d791920a55e88720b7 source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `Inactive`

`Status.Inactive` is the second member of the `Status` enum, with an auto-incremented value of `2`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_ts_repo/src/base:Status.Pending fingerprint=331551b0de4157c9abc7b72b61b96a2a928fd6db3cdf029c1fc44b08ad633aa6 body_fp=ffd671d46175dca47014764c57573ff30601fc4915f76b746f24d4056043a75b source_ref=b71d66fef6fe4367a4180c6b1c625fb4e82b2919 role=model -->
## `Pending`

Enum member of `Status` representing a pending state; auto-incremented value `3` (follows `Inactive = 2`).
<!-- trie:end -->