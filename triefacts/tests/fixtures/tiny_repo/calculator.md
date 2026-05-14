---
trie_version: 0.1.0
source: tests/fixtures/tiny_repo/calculator.py
file_fingerprint: d3b37289441711a16a1b150a6a1594f610ed72432d622215fdc582e2552d3f2c
last_synced_at: '2026-05-14T17:31:10Z'
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
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator fingerprint=74de98ffbf8ea1b6ea814eb2c7b4f292313d6260b4a177205449c9250c8b377b body_fp=e7f9f924b8e66c52852a06e214dc4cf6313da9881167eb5e567b25fc40a727b5 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `Calculator(value: float = 0.0)`

Stateful dataclass that accumulates a running numeric value across chained operations.

- **`value`**: current running total, initialised to `0.0`.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.add fingerprint=5d3a9c6d0ea1f1d91e57d2b99e95b60ff1990d437d4e2f4f5c1beaa78236b95c body_fp=6b7777cf1c532a1928175c5994cf67dc1b16e2bfca5a686f689188e33df56e44 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `add(self, x: float) -> "Calculator"`

Add `x` to the running value and return `self` for method chaining.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.multiply fingerprint=b83d9814f78b7a1e5900b7205181b38541a9a66a85e48fd43ae8ae2e1351dbbe body_fp=b642402036b91ee2403676712c52c29726785e91f7260607d739987f99b8c715 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `multiply(self, x: float) -> "Calculator"`

Multiply the running value by `x` and return `self` for chaining.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.reset fingerprint=4d978f6c3094c34c2b88383d732679183bfa60c79a3c63a3b6b0989ae68d1b44 body_fp=d75f38f461a346cff7af13e78090d84ba3103b0f29fb863cd29e16a295035198 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `reset(self) -> None`

Reset the running value to zero.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:add fingerprint=8cc28d14181d5579591af949e61d6a555af2f9fb54e46c7195393f9b46fce67b body_fp=b369752ce459a98f0a9ae697124c7da25e5578b6f22ecf55d9fdf76fe8dcf59f source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf -->
## `add(a: float, b: float) -> float`

Return the sum of two numbers.
<!-- trie:end -->