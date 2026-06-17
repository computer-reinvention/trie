---
trie_version: 0.1.9
source: app/src/graph/conductor.ts
file_fingerprint: ea633a35d092025786663505679f421333b98fa94c348f1845ad0a5c78af73ad
last_synced_at: '2026-06-17T16:39:39Z'
defines:
- kind: type
  qualified_name: app/src/graph/conductor:MotionIntensity
  lines: 22-22
- kind: type
  qualified_name: app/src/graph/conductor:CameraMode
  lines: 23-23
- kind: interface
  qualified_name: app/src/graph/conductor:MotionPrefs
  lines: 25-29
- kind: function
  qualified_name: app/src/graph/conductor:osPrefersReducedMotion
  lines: 31-37
- kind: function
  qualified_name: app/src/graph/conductor:motionPrefs
  lines: 39-47
- kind: interface
  qualified_name: app/src/graph/conductor:Ripple
  lines: 53-60
- kind: interface
  qualified_name: app/src/graph/conductor:Comet
  lines: 61-68
- kind: interface
  qualified_name: app/src/graph/conductor:Breadcrumb
  lines: 69-74
- kind: type
  qualified_name: app/src/graph/conductor:CueKind
  lines: 77-77
- kind: interface
  qualified_name: app/src/graph/conductor:Cue
  lines: 78-84
- kind: constant
  qualified_name: app/src/graph/conductor:RIPPLE_TTL
  lines: 86-86
- kind: constant
  qualified_name: app/src/graph/conductor:COMET_TTL
  lines: 87-87
- kind: constant
  qualified_name: app/src/graph/conductor:CUE_LOG_MAX
  lines: 88-88
- kind: constant
  qualified_name: app/src/graph/conductor:MAX_RIPPLES
  lines: 90-90
- kind: constant
  qualified_name: app/src/graph/conductor:MAX_COMETS
  lines: 91-91
- kind: constant
  qualified_name: app/src/graph/conductor:_seq
  lines: 93-93
- kind: function
  qualified_name: app/src/graph/conductor:nextId
  lines: 94-94
- kind: interface
  qualified_name: app/src/graph/conductor:ConductorStore
  lines: 96-117
- kind: constant
  qualified_name: app/src/graph/conductor:useConductor
  lines: 119-189
- kind: function
  qualified_name: app/src/graph/conductor:conductGlance
  lines: 198-212
- kind: constant
  qualified_name: app/src/graph/conductor:RING_STAGGER_MS
  lines: 214-214
- kind: constant
  qualified_name: app/src/graph/conductor:MAX_RING_MS
  lines: 215-215
- kind: function
  qualified_name: app/src/graph/conductor:playCascade
  lines: 220-270
- kind: function
  qualified_name: app/src/graph/conductor:ghostCascade
  lines: 272-282
- kind: function
  qualified_name: app/src/graph/conductor:replayTurn
  lines: 286-308
incoming_refs: 11
outgoing_refs: 10
---
<!-- trie:section symbol=app/src/graph/conductor:MotionIntensity fingerprint=b536cdac1a7cb43e2e51e396b92247cd0b1ad4f7be603ea2ea6c74bebd48eb5f body_fp=68d6843b09ba94d30b00e6a377253204bec35586eaf23ff5e04c9f0f29370fca source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Union type representing the three animation intensity levels for the conductor's motion system.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:CameraMode fingerprint=ad972a034f99246e1531cbf9b64c8fa92bd1501392601f116f73263db23612f2 body_fp=ac1f0274873d2d117d5cccc5f401c31052201cb12d4e66b531b3a3a6c84e1e6f source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Union type controlling camera animation behaviour: `"cinematic"` enables full tracking, `"edge-only"` restricts to edge transitions, `"off"` disables camera movement.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:MotionPrefs fingerprint=93f9a8d35f5484a8226a8f2fcb3b4b27fed3bd78f924312edd32a57f0a5c2f40 body_fp=7810dd7c2f1e98984ce6c43b067d4d7fb555d716197818b4d9c1c356d17fa8e5 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Holds resolved motion preference values consumed by the Conductor and FX layer.

- `reduceMotion`: `true` when intensity is `"off"`, forced, or OS prefers reduced motion.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:osPrefersReducedMotion fingerprint=14d03e5dd87d9ab1abeab3f44fa6d0729fa12eb71d12f73fea15e7f44081fe2a body_fp=8bad774cb2c1f1e1c0e038a43b936bc935cb0873c42c0240cca104a22e97be13 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=util -->
Return `true` if the OS `prefers-reduced-motion: reduce` media query matches, guarding against non-browser environments.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:motionPrefs fingerprint=11f24eb545eb8135ad131356cb7fd912d377009c50cfc4fb92ea8a4cf3c31b7e body_fp=0cd9fdc1c435c10edd1de9138482e3e98dc00e5909ad141028489c2b7c49a321 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Read motion settings from `useSettingsStore` and return a resolved `MotionPrefs` object.

- `reduceMotion`: `true` when intensity is `"off"`, `rm` is `"force-on"`, or `rm` is `"auto"` and the OS prefers reduced motion.
- `intensity`: defaults to `"cinematic"` if unset.
- `camera`: defaults to `"edge-only"` if unset.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:Ripple fingerprint=4c850332f2484d70b67272df8c73d5b504a04a434de32ffe4cd77a2ae1986e38 body_fp=66d69c7078e52cf26de18b1cfd0873b37bcfdbe4033e2e0cb037ab6ae8f7866c source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Transient FX particle representing a single ripple pulse on a graph node.

- `born`: epoch ms timestamp of creation; used with `ttl` to compute decay.
- `ttl`: lifetime in ms before the ripple is culled by `tick`.
- `qname`: qualified name of the node this ripple is anchored to.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:Comet fingerprint=9076fac129b9242e08089fe97c835ff8aea9a5918d8afabea8e656b78310c3a3 body_fp=11e9bf0026c93a41a4d59dd552071f5b576cfd98d752c030ee43020ea95225cd source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Represents a transient animated comet FX travelling between two graph nodes.

- `born`: timestamp (ms) at creation, used with `ttl` to compute expiry.
- `ttl`: lifetime in milliseconds before the comet is culled by `tick`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:Breadcrumb fingerprint=97af3809d6a35b2517317e8e585f9ed0dfbcc4b3900a695205b2a3410eee9a65 body_fp=9222fb218e6c778c5560d82d09478be2b8c06e3ecfa544da2d68351d644df0e0 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Shape representing a visited-node trail marker held in `ConductorStore.breadcrumbs`.

- `seq` — monotonically increasing counter used to order breadcrumbs within a turn
- `born` — `Date.now()` timestamp of creation, used for age-based rendering
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:CueKind fingerprint=6aa76707f4ebd823359d927a15c087a4385ab411941e16c9ce21f39cc57142f1 body_fp=650c75642f253210a9ff75c3e486c6cb52e5cce4c5a47b5774fce6f3337248db source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Union of string literals identifying the category of a recorded `Cue` in the conductor's replayable timeline.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:Cue fingerprint=bca218dc445e7c4932e3f980568bca0fdf17bcaaa1f277027c9faddbf29cef91 body_fp=8585f7730043e44aadb3c9f65f5e1aea1818bdedc2191d5920ae238b0e943b9c source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Represents a single recorded choreography event in the Conductor's replayable cue log.

- `t`: milliseconds elapsed since the current turn started
- `kind`: classifies the event for FX replay dispatch
- `from` / `to`: qualified node names; both optional depending on cue kind
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:RIPPLE_TTL fingerprint=6b20341d0992ca8926a7820bcd527d24aee091990ca069e9a93141b163e774f1 body_fp=f484be370b1acd44189350163269e4035f2c45fbc9ed5ea8c012104404324a3f source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Lifetime in milliseconds of a ripple FX particle before it is culled by `tick`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:COMET_TTL fingerprint=0ed482d3f44ed693488c89daf963fc2f83299e288f85988a5eea162c0180b398 body_fp=6872d7bd2f9b108a773b905ed62e1b969aa82cbb3fd8aced1295ffd1c5a775ed source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Lifetime in milliseconds for a `Comet` FX particle before it is culled by `tick`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:CUE_LOG_MAX fingerprint=f4542b899c34aa4da21d46947b38a27daefa2bda86b853b447a1d6c2f85ca4be body_fp=a5bc15cc7459c53fabfd9cf624d0ece4f7aadf3adef0224aa0c409948f7a42d2 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Maximum number of `Cue` entries retained in the ring-buffer cue log before oldest entries are dropped.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:MAX_RIPPLES fingerprint=beb4d06c012d2f119bcad241ce0ea5ae14c00ba40f11d0e31f6429aa00c4922c body_fp=5aeed2df7072a8037c3d7cafef1c81290391dc2530a06cdb1fa97c9576caeeb9 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Maximum number of concurrent ripple effects retained in the conductor store, enforcing concurrency governance.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:MAX_COMETS fingerprint=03bce646d62c0b33cac3cee95bf0011d9b714c284cea03d41632e426de8712b9 body_fp=adab4fd34df9d0fc36c36ff9b6fcd26d75ab3cb6e29f3d41b175831f5fc34d3f source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Hard concurrency cap controlling the maximum number of simultaneous comet-tail FX retained in `ConductorStore`.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:_seq fingerprint=1fdaabe35b7d8f542921265a9eb7204a1a5be24cf3978fd09d67b9561083be9a body_fp=296a6ed803bc140b5dfb965ab719a8c7dfb19b305685089b612c81faf519b20b source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=util -->
Module-level counter incremented by `nextId` to produce unique FX object IDs.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:nextId fingerprint=fb88090473760f9c42f2b6775e5ec552cd299d6003e72cca971ebf5140b8bbd3 body_fp=181a9bce293e1b556c5886d05e07c74eda7c6f4b21ab95e5d384c35487f2a512 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=util -->
Increments the module-level `_seq` counter and returns the new value as a unique FX object ID.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:ConductorStore fingerprint=3ce2a6731af3ff18dd8131144524f5cd0f3530fa26ddddb45cb0c402ee3d23ca body_fp=67b80ae1fa8f5631d7f03f8d4e6d58cddda24274cdba5502136f96db8ad73149 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=model -->
Zustand store shape for the Conductor's transient FX state and its mutation methods.

- `cueLog`: ring buffer of recorded `Cue` entries, capped at 600, anchored by `turnStart`
- `turnStart`: epoch ms marking the start of the current turn; used to compute relative cue timestamps
- `crumbSeq`: monotonically increasing counter used to order breadcrumbs
- `lastGlance`: qualified name of the most recently glanced symbol; `null` after `clearTurn`
- `hud`: ambient overlay for toolcalls with no graph node (bash/fetch etc.); `null` when inactive
- `tick`: advances FX decay; returns `true` while ripples or comets remain alive (drives rAF loop)
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:useConductor fingerprint=726e8b812f9af4e7959cf5a6d02100bad925411a3b25b94302f093d8878c053e body_fp=bf86ff4771f2bae01775ac5dd3069f34380890d65e47d0cfffb684eb142bb230 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=orchestration -->
Zustand store that owns all transient FX state (ripples, comets, breadcrumbs), the cue ring buffer, and turn lifecycle for the Conductor.

- `emitRipple` — no-ops when `reduceMotion` is true; caps live ripples at `MAX_RIPPLES` (most-recent kept)
- `emitComet` — no-ops when `reduceMotion` is true or `from === to`; caps at `MAX_COMETS`
- `emitBreadcrumb` — replaces any existing entry for `qname`; ring-caps breadcrumbs at 40
- `record` — appends a cue with `t` as ms offset from `turnStart`; ring-caps at `CUE_LOG_MAX` (600)
- `tick(now)` — evicts expired ripples/comets; returns `true` while any FX remain (use to gate rAF)
- `clearTurn` — resets all FX and the cue log, reanchors `turnStart` to now
- `hud` — ambient display for toolcalls that have no graph node; `null` when idle
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:conductGlance fingerprint=366e36731563f26f147dc8c1dc342ea00095696e913517226c0a6e39c996ac26 body_fp=9bc62cd5fe9f6c6d351a9f6997895a03d5d32b618971e9bf60f0b5561d2d5406 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=orchestration -->
Record a glance at `qname`: emits a breadcrumb, a ripple, an optional comet from the previous glance, and logs the cue to the conductor ring buffer.

- `qname`: fully-qualified symbol name receiving attention
- `state`: drives FX colour and determines cue kind (`"scanning"` → `"scan"`, else `"glance"`)
- Comet is only emitted when a distinct prior `lastGlance` exists
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:RING_STAGGER_MS fingerprint=6f6bd325c853ff5cee4ceb5a37b1108cfbd8cb980e87b93ed4c50369e592bf06 body_fp=3bcd75e98083831bb03f27bcb23e043cd5ed9b350d7c6134f1fe405c6ccfa656 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Millisecond delay between successive BFS-hop rings in `playCascade`'s staggered ripple wavefront.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:MAX_RING_MS fingerprint=6f21af119eacbac56865b6337223dffeefaecb76e83b8c42901456669f87d8dc body_fp=babdd5cd3ef0aeb9028c04a553efe5e38270f1b4fd4ad5423658bd238bb5443f source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=config -->
Cap the total stagger delay for cascade ripple rings at 900 ms regardless of hop count.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:playCascade fingerprint=5b77e9f3165b6c00de322beff30bd887f1f40cf8ce3452945778c1bf3302053f body_fp=503dab61017bcdae3ca7b913c2fdd3da683294362992de6b5fa7f4833fdbc1da source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=orchestration -->
Fetches the blast radius of `qname` then drives a staggered ripple wavefront over dependent nodes, grouped by BFS hop, respecting motion preferences.

- `qname` — qualified name of the changed symbol; its node is set to `"writing"` first.
- Returns early (no-op) if `motion.intensity` is `"off"` or the API call fails.
- Under `reduceMotion`, applies cascade state and notes instantly with no FX timing.
- Stagger delay is capped at `MAX_RING_MS` (900 ms) regardless of hop count.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:ghostCascade fingerprint=c702d7c9158834f6e12f3c48abfe0d7145134b8b04ff154cb1ed6539bf857efe body_fp=0441b081fa92a56239570b1d6541b8f197ac002ced514c90383c1db1a54d0fa9 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=orchestration -->
Fetch the blast radius of `qname` and annotate up to 40 affected nodes with a cascade note, silently ignoring errors.

- `qname`: qualified node name; short name (after `:`) used in the note text.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/conductor:replayTurn fingerprint=8475ffa3b7708cb53b4cee7b332f4aa3e71fcf451b96b9f95e51d8e777d7af11 body_fp=fc78dc4660f943b223d76956c1229d2ee86bfcb4349508bbceac705c89c83f28 source_ref=475a070adb489a72071bd46573f4bb54e69d680f role=orchestration -->
Replay the conductor's recorded cue log as an FX-only animation at the given playback speed.

- `speed`: multiplier applied to elapsed time; `1` = realtime, higher values fast-forward.
- Clears live FX before replay so the canvas reads cleanly; resets `replaying` to `false` when the log is exhausted.
- Node body state is not re-driven — only breadcrumbs, ripples, and comets are re-emitted.
<!-- trie:end -->