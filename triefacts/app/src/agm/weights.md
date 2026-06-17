---
trie_version: 0.1.9
source: app/src/agm/weights.ts
file_fingerprint: 813d2b243c60374cb324db2bf2d2e88b29ac6383a43e9061e96b8620e99b6ff6
last_synced_at: '2026-06-17T16:36:34Z'
defines:
- kind: module
  qualified_name: app/src/agm/weights:__module__
  lines: 1-81
- kind: constant
  qualified_name: app/src/agm/weights:HISTORICAL_SEED_FACTOR
  lines: 44-44
- kind: constant
  qualified_name: app/src/agm/weights:COLD_FLOOR
  lines: 49-49
- kind: interface
  qualified_name: app/src/agm/weights:LiveContribution
  lines: 53-58
- kind: function
  qualified_name: app/src/agm/weights:makeContribution
  lines: 60-62
- kind: function
  qualified_name: app/src/agm/weights:foldLiveMass
  lines: 66-73
- kind: function
  qualified_name: app/src/agm/weights:decayScalar
  lines: 76-80
incoming_refs: 20
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/agm/weights:__module__ fingerprint=d92503c5ffe5d3e2d983fc529bae8c82876b775004f1e8dde28e32df61df8e43 body_fp=e0eb794b2c1a698a614dd2cc28dc0b20502183232e4256a8e82baa9e68a2cf92 source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=config -->
Pure math module providing AGM tuning constants, decay helpers, and live-mass folding; re-exports canonical contract values from `@/api/types`.

- `HISTORICAL_SEED_FACTOR` — scalar (0.15) weighting historical mass into the live field at load time
- `COLD_FLOOR` — absolute live-mass floor (1e-3) below which a node is a canvas-removal candidate
- `LiveContribution` — typed record for a single decaying event contribution (ts, weight, lambda, type)
- `makeContribution` — constructs a `LiveContribution` from an event type and timestamp
- `foldLiveMass` — sums all contributions to a live-mass scalar at a given wall-clock instant
- `decayScalar` — decays a single scalar value continuously between two timestamps
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:HISTORICAL_SEED_FACTOR fingerprint=ae85bb625e0fbdbe9cf89401f52ab38210202b66977a5290ab99f2afb68d9a2b body_fp=204baafba540e71e76a63fa78a46ed78d95cf00c3c43d27e638495b89fa382f6 source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=config -->
Scalar factor (0.15) controlling how strongly historical mass seeds the live field on initial load.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:COLD_FLOOR fingerprint=5acc4fa2c9e11671847ab3c5b7355c7fcadf3360bf4a1be4190211293c5ca6a9 body_fp=8f288fdb1497aef566167d6d3b86db9ef598162bec50848e13572b5f9f767c15 source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=config -->
Absolute lower bound (`0.001`) below which a symbol's log-compressed live mass is considered cold and eligible for removal from the canvas.
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:LiveContribution fingerprint=fa9379a32f37848298501e112ae5318d1c18555162387448dc7b1f996288fff5 body_fp=da8873392b2e1ae85b9ec752d5ab7fd7013744a1590a9fe16b598ee72f901803 source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=model -->
Represents one decaying contribution to a symbol's live mass from a single attention event.

- `ts`: unix seconds when the event landed
- `lambda`: per-event-type decay rate, derived via `liveLambda(type)`
- `type`: optional; identifies the tool intent, drives render kind
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:makeContribution fingerprint=540bb4d7bfcb66e2ae117c244fdb8a7e4344a981dcedbbcc7fc3c721413e4f47 body_fp=a6f0503d09d2a2578abb5f6ab07d5ee3644c2a7972bc003614a9057e57bad88f source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=util -->
Construct a `LiveContribution` by looking up the event weight and decay lambda for `type`.

- `ts` — unix seconds at which the event landed
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:foldLiveMass fingerprint=4d040490d2c119305d5c6a1147ea5848b8640ed263e423db2af640362810f761 body_fp=13c4407c5e9a74b1343f2d9ecb7a629955abb7e1aa38f42c162165447f79b6ba source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=domain -->
Sum all decaying `LiveContribution` values into a single live-mass scalar at `now`.

- `contributions` — iterable of per-event decay terms; each evaluated as `weight × e^(−λ·dt)`
- `now` — current time in unix seconds; `dt` is clamped to `≥ 0`
- Returns combined live mass; frame-rate independent via continuous exponential decay
<!-- trie:end -->
<!-- trie:section symbol=app/src/agm/weights:decayScalar fingerprint=4af507fba8fdd862c0efd221fe97cea74d972379b86a2ec415fd985390cc41c9 body_fp=edd7015fd5a844ba941a283530b56a1543946429c426d6a1cf25c78195787fda source_ref=c3589b8c5b117f16c6711b79298afb9685a2e420 role=util -->
Decay a single scalar `value` from `ts` to `now` using continuous exponential decay at rate `lambda`.

- `lambda`: per-event-type decay rate, as returned by `liveLambda`
- `ts`: unix seconds the value was recorded
- Returns `0` immediately if `value ≤ 0`
<!-- trie:end -->