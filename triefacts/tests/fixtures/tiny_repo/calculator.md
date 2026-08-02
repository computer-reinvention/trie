---
trie_version: 0.3.0
source: tests/fixtures/tiny_repo/calculator.py
file_fingerprint: d3b37289441711a16a1b150a6a1594f610ed72432d622215fdc582e2552d3f2c
last_synced_at: '2026-06-06T13:13:21Z'
description: A pocket calculator with a tiny API surface.
defines:
- kind: class
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator
  lines: 7-24
  signature: class Calculator
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.add
  lines: 12-15
  signature: 'def add(self, x: float) -> "Calculator"'
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.multiply
  lines: 17-20
  signature: 'def multiply(self, x: float) -> "Calculator"'
- kind: method
  qualified_name: tests/fixtures/tiny_repo/calculator:Calculator.reset
  lines: 22-24
  signature: def reset(self) -> None
- kind: function
  qualified_name: tests/fixtures/tiny_repo/calculator:add
  lines: 27-29
  signature: 'def add(a: float, b: float) -> float'
- kind: function
  qualified_name: tests/fixtures/tiny_repo/calculator:_internal_helper
  lines: 32-34
  signature: 'def _internal_helper(x: float) -> float'
incoming_refs: 0
outgoing_refs: 0
---
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator fingerprint=74de98ffbf8ea1b6ea814eb2c7b4f292313d6260b4a177205449c9250c8b377b body_fp=556729bdd4134f260b82a10b9c0d4741347e86ba25ac68c9e1a528a661f45565 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `class Calculator`

Stateful calculator that accumulates a running value with chainable arithmetic operations.

- `add(x)`: Adds x to the running value, returns self for method chaining
- `multiply(x)`: Multiplies running value by x, returns self for chaining
- `reset()`: Resets running value to zero
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.add fingerprint=5d3a9c6d0ea1f1d91e57d2b99e95b60ff1990d437d4e2f4f5c1beaa78236b95c body_fp=a625a0aec14398711f065af2eacef3f4de3dcab6303cc5a51af248bd426cd2d6 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `def add(self, x: float) -> "Calculator"`

Adds `x` to Calculator's running value and returns self for method chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.multiply fingerprint=b83d9814f78b7a1e5900b7205181b38541a9a66a85e48fd43ae8ae2e1351dbbe body_fp=2eea06d92862418dbeb4374f6e6271b5c88718daa6391845d0bfd19b578e49e5 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `def multiply(self, x: float) -> "Calculator"`

Multiplies Calculator's running value by `x` and returns self for method chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.reset fingerprint=4d978f6c3094c34c2b88383d732679183bfa60c79a3c63a3b6b0989ae68d1b44 body_fp=6598dd1b7b41ba7e16328ec68b4a4acc1ddc0c7ca9ec63fc32593cd2470ccd47 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `def reset(self) -> None`

Resets Calculator's running value to zero.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:add fingerprint=8cc28d14181d5579591af949e61d6a555af2f9fb54e46c7195393f9b46fce67b body_fp=c88cc5789adb73bee3c1f068f2880427b65af7de3d128ca6489bd2ef0337ef2f source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `def add(a: float, b: float) -> float`

Returns the sum of two numbers.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:_internal_helper fingerprint=51a7bd3ae943c2de14466feb851c5ef0db6e9070c468aee27c2642293ab586f8 body_fp=3bcd075432aad3dff8339497804ffde28b46701337341e898562d667235aa606 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
## `def _internal_helper(x: float) -> float`

Doubles the input value by multiplying by 2.
<!-- trie:end -->






