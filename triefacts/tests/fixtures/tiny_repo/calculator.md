---
trie_version: 0.1.5
source: tests/fixtures/tiny_repo/calculator.py
file_fingerprint: d3b37289441711a16a1b150a6a1594f610ed72432d622215fdc582e2552d3f2c
last_synced_at: '2026-06-06T13:13:21Z'
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
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator fingerprint=74de98ffbf8ea1b6ea814eb2c7b4f292313d6260b4a177205449c9250c8b377b body_fp=cdabec5af26ee3bf3431822dada12680880246d3cd0cf79af1dda49d008a1ee3 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Stateful calculator that accumulates a running value with chainable arithmetic operations.

- `add(x)`: Adds x to the running value, returns self for method chaining
- `multiply(x)`: Multiplies running value by x, returns self for chaining
- `reset()`: Resets running value to zero
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.add fingerprint=5d3a9c6d0ea1f1d91e57d2b99e95b60ff1990d437d4e2f4f5c1beaa78236b95c body_fp=e30d6f6bed92da76fd4eefe4a28b4369ccf4697016d706e18616486798857e4f source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Adds `x` to Calculator's running value and returns self for method chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.multiply fingerprint=b83d9814f78b7a1e5900b7205181b38541a9a66a85e48fd43ae8ae2e1351dbbe body_fp=9f2d1ba054ebe3684d4423de13e06674d9bdec3ccf47267c9cf0b977f8cea99b source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Multiplies Calculator's running value by `x` and returns self for method chaining.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:Calculator.reset fingerprint=4d978f6c3094c34c2b88383d732679183bfa60c79a3c63a3b6b0989ae68d1b44 body_fp=9dc0602ca111b5f323d24e9f1f814efed913d4889f852c9c8d4229a74244b8b0 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Resets Calculator's running value to zero.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:add fingerprint=8cc28d14181d5579591af949e61d6a555af2f9fb54e46c7195393f9b46fce67b body_fp=d3b49222894df8cf2f54370b226d68222977e8c13b4c6694fe7dedb7da59e77d source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Returns the sum of two numbers.
<!-- trie:end -->
<!-- trie:section symbol=tests/fixtures/tiny_repo/calculator:_internal_helper fingerprint=51a7bd3ae943c2de14466feb851c5ef0db6e9070c468aee27c2642293ab586f8 body_fp=d57a82de81d1d2a1ba6dd3ccc0b718913f05c492b8bedef076be0d1ac6405e37 source_ref=881d199032d2ff0cbdb0952e5b809f523c3a0eaf role=test-infrastructure -->
Doubles the input value by multiplying by 2.
<!-- trie:end -->






