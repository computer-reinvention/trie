---
trie_version: 0.1.9
source: app/src/components/GraphCanvas/AgentActivityCards.tsx
file_fingerprint: b9354cac31d0c0b5ddac5c2ced441e28e0fea5cb8074ec9c15ce50f31ce8df04
last_synced_at: '2026-06-17T16:38:00Z'
defines:
- kind: constant
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:NOTE_TTL
  lines: 15-15
- kind: constant
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:NOTE_FADE
  lines: 16-16
- kind: constant
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:STACK_MAX
  lines: 18-18
- kind: function
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:actionColor
  lines: 20-24
- kind: function
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:actionVerb
  lines: 25-29
- kind: interface
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:CardsProps
  lines: 31-38
- kind: function
  qualified_name: app/src/components/GraphCanvas/AgentActivityCards:AgentActivityCards
  lines: 40-213
incoming_refs: 1
outgoing_refs: 5
---
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:NOTE_TTL fingerprint=72dcf4bab7467de65d41c7aa8619abc342cffbbdacae729a782abf0ee7fccc3d body_fp=c29fbb9256e06fe5bc25af56a7a2bc10e9d27a262a5eb71b1b7003e1d5d631fd source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=config -->
Milliseconds a card remains visible before it finishes fading out (9 seconds).
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:NOTE_FADE fingerprint=6a3e9e5c8ba0e306286a6ccf56330da352a0ed02080dfe3687fa1e16b45454e6 body_fp=e3a248961e5d6042b5d05e846b11dcf35fc5b18f37b5aa4131a82302124d2ab9 source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=config -->
Duration in milliseconds of the fade-out window at the end of a card's lifetime.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:STACK_MAX fingerprint=f6e5b9706e7ae6ba151de6f5881cc70fcb5260cf0f3c7ff471b36e9c2b5a01b2 body_fp=a2647335037e8897fb294cca2a32d713418ba0fa0a7040cf2716432cf5c621fb source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=config -->
Maximum number of activity cards stacked on a single component bubble; newest cards win when the limit is exceeded.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:actionColor fingerprint=11b16601bba63de3167fc72ac30ae37cfaf4c09a3fdd54f0987b4dafa02f63f7 body_fp=7561b24777337c012e3b010c2337e6385523396fa23d48d4ceb0622b2bdeda1b source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=util -->
Map an `AgentState` value to its corresponding `ACTIVITY` color string for rendering agent action indicators.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:actionVerb fingerprint=953b8ae08d8f7df06b2e2fba90b23379e3bd008fc5754905bbfb33c03a4b6ceb body_fp=104935ebc6228d3308a7f5384a70c869b007b6cb45d9a165b5f3eda65e5b2b24 source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=util -->
Map an `AgentState` value to a human-readable present-participle verb for display in activity cards.
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:CardsProps fingerprint=f4096b1b980d608e1a3bd97a9723aa141433900d28722195dbb3622db4a714ae body_fp=4152d72d3473526753eaa41e1392089de48686e12a363a4ef1a0b9faac7c8169 source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=model -->
Props for `AgentActivityCards`, supplying the force-graph ref, component positions, and viewport dimensions.

- `fgRef`: mutable ref to the force-graph instance used for coordinate projection
- `componentPos`: maps group key to graph-space `{x, y}` of its component bubble
- `width` / `height`: viewport pixel dimensions used for off-screen chevron clamping
<!-- trie:end -->
<!-- trie:section symbol=app/src/components/GraphCanvas/AgentActivityCards:AgentActivityCards fingerprint=0f2d5e5de01d019d7b6473a988066bcc33c2d856786f05d4117c385ed62a8db8 body_fp=42dab747eb5bb1261b4c352a9bd5f743354a5ee72816c31034648c059d76c805 source_ref=ff54a682c5d4c797f3ebe4c80c38b4ff9dda9fb7 role=api -->
Render DOM overlay cards anchored to component bubbles showing agent read/write/scan activity, plus off-screen chevron indicators that pan the camera when clicked.

- `fgRef` — ref to the force-graph instance; returns `null` if not yet mounted.
- `componentPos` — map from group key to graph-space `{x, y}` of each component bubble.
- `width` / `height` — viewport dimensions used to detect off-screen nodes and clamp chevron positions.
- Cards stack up to `STACK_MAX` (3) per bubble, newest closest to the bubble, older entries dimmed by 25 % per step.
- Cards fade during the final `NOTE_FADE` (1200 ms) of their `NOTE_TTL` (9000 ms) lifetime.
- Off-screen groups produce a clickable chevron clamped to the viewport edge; clicking calls `fg.centerAt` to follow the activity.
<!-- trie:end -->