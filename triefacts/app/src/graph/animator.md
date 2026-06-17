---
trie_version: 0.1.9
source: app/src/graph/animator.ts
file_fingerprint: f560a7597042680d1afa9af1532b2cf9b2044fa60470f53c5ca55183fa889d08
last_synced_at: '2026-06-17T16:39:06Z'
defines:
- kind: interface
  qualified_name: app/src/graph/animator:AnimChannel
  lines: 8-12
- kind: function
  qualified_name: app/src/graph/animator:channel
  lines: 14-16
- kind: function
  qualified_name: app/src/graph/animator:springStep
  lines: 20-29
- kind: interface
  qualified_name: app/src/graph/animator:NodeAnim
  lines: 31-38
- kind: class
  qualified_name: app/src/graph/animator:GraphAnimator
  lines: 40-97
- kind: property
  qualified_name: app/src/graph/animator:GraphAnimator.nodes
  lines: 41-41
- kind: property
  qualified_name: app/src/graph/animator:GraphAnimator.lastT
  lines: 42-42
- kind: method
  qualified_name: app/src/graph/animator:GraphAnimator.ensure
  lines: 44-56
- kind: method
  qualified_name: app/src/graph/animator:GraphAnimator.get
  lines: 58-60
- kind: method
  qualified_name: app/src/graph/animator:GraphAnimator.prune
  lines: 63-67
- kind: method
  qualified_name: app/src/graph/animator:GraphAnimator.setTargets
  lines: 69-74
- kind: method
  qualified_name: app/src/graph/animator:GraphAnimator.tick
  lines: 78-96
- kind: function
  qualified_name: app/src/graph/animator:easeOutBack
  lines: 100-104
incoming_refs: 1
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/graph/animator:AnimChannel fingerprint=74ff0ef22960b59fd3f2a59a0600d86f776d1f1b47b7a4658399fa123b3c9fe5 body_fp=ece5854b58c16c561aa8fcabd5a0193d05be39d042638637514bf088a1b7ea26 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=model -->
Holds the per-channel spring state for a single animated scalar value.

- `current`: interpolated value read by the painter each frame.
- `target`: desired value set by state; spring eases `current` toward it.
- `velocity`: spring velocity; carries overshoot momentum between frames.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:channel fingerprint=0d45ae3479e9b5bde6417dcd48c3abe99d7de9dfedd4738d33ab3abe5d24ddb2 body_fp=2fa8625b312d589aa0992f5eafc0879b00fb1893dc62e5d6d21fd45a40334649 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=util -->
Create an `AnimChannel` with `current`, `target`, and `velocity` all initialised to `v`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:springStep fingerprint=c7df5af8dee3c69fe0757785c1274ce47d7be9d807a70d14e27fbb85e4dcdcc3 body_fp=c89b9927c3ad28f52b6a20544c8b237712bd8d36589bb934abeadf6cc89641e9 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=util -->
Advance a single `AnimChannel` by one spring-physics step, snapping to target when displacement and velocity both fall below 0.001.

- `c` — mutated in place; `current` and `velocity` are updated
- `dt` — elapsed time in seconds for this frame
- `stiffness` — spring force multiplier; higher values accelerate convergence
- `damping` — per-frame exponential decay base applied as `damping^(dt*60)`
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:NodeAnim fingerprint=bf3b458bd56cc990b3b293849fd0b8e1c43b69274630a8031ce3c51b8887980b body_fp=3b9fbfbefbffc2f8ab804c8e113b44999e8d7ec603ad7cb2ee3ce3334cbd1b88 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=model -->
Holds the three `AnimChannel` fields that track per-node animation state for `GraphAnimator`.

- `reveal`: 0–1 scalar driving first-load scale/fade-in reveal.
- `pulse`: 0–1 scalar for agent read/write activity breathing effect.
- `emphasis`: 0–1 scalar for hover/selection size growth.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator fingerprint=a54f910b6e1c947b7f76b6b5296dec83451e9e243b2facfe914f1dfb6a365c66 body_fp=f52d9f19d5b6aaefba9df25d0033cb240e916bd619e514acff43d0bc758974ab source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=domain -->
Manages per-node spring animation state, advancing all `NodeAnim` channels each frame and tracking motion.

- `ensure(id, born)` — creates a `NodeAnim` for `id`; `born=true` starts `reveal` at 0 and animates to 1
- `get(id)` — returns the existing `NodeAnim` for `id`, or `undefined` if not yet registered
- `prune(presentIds)` — removes entries for node ids absent from `presentIds`, bounding memory growth
- `setTargets(id, t)` — updates the `target` of any supplied `pulse`, `emphasis`, or `reveal` channels
- `tick(now)` — steps all springs forward by the elapsed delta; returns `true` if any channel is still in motion
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.nodes fingerprint=dc3f10c7d2321872fce14b976d9efc4918fb2a2ed565fe7ecde78c196c0f415f body_fp=5482625f9354c031c79df196d7f9a678cac20c82632dadedcb3271a6c6440892 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=model -->
`GraphAnimator.nodes` is a private attribute mapping node IDs to their `NodeAnim` spring-channel state.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.lastT fingerprint=86ed72a61889427dbf45b28bd1876bda0707bdc85121f7bba813be033745fcd8 body_fp=90e46745ab897bc6f78f011c1316c209b7173fbeb8824f45c23e8c4bc06f0ff6 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=model -->
`GraphAnimator.lastT` is the timestamp (in milliseconds) of the most recent `tick` call, used to compute frame delta time.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.ensure fingerprint=27e6f8ec5b6f1ff955f6426b9f75df720865ff8a82c7b93db86ef65c55b8457c body_fp=2a4f6752c0324040a26fc1eff48dd9ea2a718fc5a7897a4a0d2a7ff3eef7ee3f source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=domain -->
Retrieves or creates a `NodeAnim` entry for a node in `GraphAnimator`, optionally initialising it as newly born.

- `born`: if `true`, sets `reveal.current` to `0` and `reveal.target` to `1`, triggering the appear animation.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.get fingerprint=0b5e23265d0e8f9c4eef3c8b548daffe586effb77a57bc7bb3fb8316c43dd4f6 body_fp=92b7a05ea43d5265f9cc1c00798fb99afd56f90832fd554435e1d71f7c2d6b3c source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=domain -->
Returns the `NodeAnim` state for the given node `id`, or `undefined` if no animation entry exists.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.prune fingerprint=70f9ac7999a29bba23530ee34df654576baa285965be4c0e9460b9fb820c543c body_fp=27c1a48c704c33fef5226e008fe6cc32dcfc0291ec4f10d5ca818e33eddcb0cd source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=util -->
Remove `GraphAnimator` entries whose IDs are absent from `presentIds`, preventing unbounded map growth after re-layouts.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.setTargets fingerprint=0b544b64b546fe66cb7b99afd73465ec5789e0a7341eea538723398a052b147a body_fp=a4358988ff7aad0fb0af6c29ca81bce3dc8dac27638b90f0cf9b8b12527962e0 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=domain -->
Update animation targets on a named node's `pulse`, `emphasis`, and/or `reveal` channels without affecting current values or velocity.

- `id` — node identifier; node is created via `ensure` if not yet tracked.
- `t` — only defined keys are applied; omitted channels are left unchanged.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:GraphAnimator.tick fingerprint=1f317f76f442dc07a3e57dd5e20576fcf7097f1f34f676a5733dc018d712f880 body_fp=ce2f5c386d4622cad8e400832f012df84264b1b111f220bc03e26c9ea4843f11 source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=domain -->
Advances all `GraphAnimator` spring channels by one frame and returns whether any node is still in motion.

- `now`: current timestamp in milliseconds; delta is clamped to 50 ms to avoid spiral-of-death on tab wake.
- Returns `true` if any channel has not yet settled, signalling the canvas to schedule another redraw.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/animator:easeOutBack fingerprint=0d2856ffac93de56d5a3d2bec204392b970b873fd37596059b15200a0e3bb731 body_fp=b33e964f9fe8571fa1769f614d808f18498971894a631ca014ae8f43c7f1c53d source_ref=3a6c7d827cc43605aadd3059aa74a0168758e623 role=util -->
Apply an easeOutBack cubic curve to `t`, producing a slight overshoot before settling at 1.

- `t`: normalized progress value, expected in `[0, 1]`
- Returns a value slightly exceeding 1 near the end before settling.
<!-- trie:end -->