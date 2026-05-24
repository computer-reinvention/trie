---
trie_version: 0.1.2
source: tests/fixtures/tiny_repo/calculator.py
file_fingerprint: d3b37289441711a16a1b150a6a1594f610ed72432d622215fdc582e2552d3f2c
last_synced_at: '2026-05-23T23:54:42Z'
description: A pocket calculator with a tiny API surface.
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator
  lines: 7-24
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.add
  lines: 12-15
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.multiply
  lines: 17-20
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.reset
  lines: 22-24
- kind: function
  qualified_name: tests/fixtures/tiny_repo/calculator:add
  lines: 27-29
- kind: function
  qualified_name: tests/fixtures/tiny_repo/calculator:_internal_helper
  lines: 32-34
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator fingerprint=74de98ffbf8ea1b6ea814eb2c7b4f292313d6260b4a177205449c9250c8b377b body_fp=655ca3440550493e4c49ce9c25b0c0f92ea2412f47364934296e2652f91452fb source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `Calculator`

Stateful calculator that accumulates a running value across chained operations.

- `value`: current running total, defaults to `0.0`.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.add fingerprint=5d3a9c6d0ea1f1d91e57d2b99e95b60ff1990d437d4e2f4f5c1beaa78236b95c body_fp=a513f2d074f12f8cc91331913dc67afc6a78c0cebda9b7a985234882e7bdddb9 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `Calculator.add(self, x: float) -> "Calculator"`

Add `x` to `Calculator.value` and return `self` for method chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.multiply fingerprint=b83d9814f78b7a1e5900b7205181b38541a9a66a85e48fd43ae8ae2e1351dbbe body_fp=81f6b6b5e403dcfe1bc69336e71d3f3b954746f38d3bd9e4d76cdc453fcc9383 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `Calculator.multiply(self, x: float) -> "Calculator"`

Multiply the `Calculator`'s running value by `x`, returning `self` for chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.reset fingerprint=4d978f6c3094c34c2b88383d732679183bfa60c79a3c63a3b6b0989ae68d1b44 body_fp=5a212ef3232b5809122906e8279b09f8ff87cd354b998b5e0c2892a89e18f048 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `Calculator.reset(self) -> None`

Reset the `Calculator` running value to zero.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:add fingerprint=8cc28d14181d5579591af949e61d6a555af2f9fb54e46c7195393f9b46fce67b body_fp=263e4d8611b3a374920d3fd352694d4319cb3460c689ad46d712d4d8ac42e7cb source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `add(a: float, b: float) -> float`

Return the sum of two floats.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:_internal_helper fingerprint=51a7bd3ae943c2de14466feb851c5ef0db6e9070c468aee27c2642293ab586f8 body_fp=7207faf6432125d90ba6c6fc321cbc15b8c78eed159f83f16b557474493fbdcc source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `_internal_helper(x: float) -> float`

Double and return `x`.
<!-- trie:end -->