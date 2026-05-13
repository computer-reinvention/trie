---
trie_version: 0.1.0
source: tests/fixtures/tiny_repo/calculator.py
file_fingerprint: d3b37289441711a16a1b150a6a1594f610ed72432d622215fdc582e2552d3f2c
last_synced_at: '2026-05-12T18:34:54Z'
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
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator fingerprint=74de98ffbf8ea1b6ea814eb2c7b4f292313d6260b4a177205449c9250c8b377b body_fp=546c4d0764a04372b5acb79870886a171114941f49e3f485f434a9f41de5eec6 -->
## `Calculator(value: float = 0.0)`

Stateful dataclass that accumulates a running numeric value across chained operations.

- **`value`**: running total, initialised to `0.0`.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.add fingerprint=5d3a9c6d0ea1f1d91e57d2b99e95b60ff1990d437d4e2f4f5c1beaa78236b95c body_fp=6b7777cf1c532a1928175c5994cf67dc1b16e2bfca5a686f689188e33df56e44 -->
## `add(self, x: float) -> "Calculator"`

Add `x` to the running value and return `self` for method chaining.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.multiply fingerprint=b83d9814f78b7a1e5900b7205181b38541a9a66a85e48fd43ae8ae2e1351dbbe body_fp=b642402036b91ee2403676712c52c29726785e91f7260607d739987f99b8c715 -->
## `multiply(self, x: float) -> "Calculator"`

Multiply the running value by `x` and return `self` for chaining.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.reset fingerprint=4d978f6c3094c34c2b88383d732679183bfa60c79a3c63a3b6b0989ae68d1b44 body_fp=9eb957d6d17c8c03275329a0cca46813cb3921da7d39696a2f4e4a5d38e59f5f -->
## `reset() -> None`

Reset the running value to zero.
<!-- trie:end -->

<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:add fingerprint=8cc28d14181d5579591af949e61d6a555af2f9fb54e46c7195393f9b46fce67b body_fp=b369752ce459a98f0a9ae697124c7da25e5578b6f22ecf55d9fdf76fe8dcf59f -->
## `add(a: float, b: float) -> float`

Return the sum of two numbers.
<!-- trie:end -->