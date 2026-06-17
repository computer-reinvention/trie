---
trie_version: 0.1.9
source: app/src/lib/sessionTitle.ts
file_fingerprint: a060e37d06b43f7c3c17535bcee85282e7891e16a2ca3fc4dab8cf3e1da91e60
last_synced_at: '2026-06-17T16:39:43Z'
defines:
- kind: constant
  qualified_name: app/src/lib/sessionTitle:DEFAULT_TITLE_PATTERNS
  lines: 12-12
- kind: function
  qualified_name: app/src/lib/sessionTitle:isDefaultTitle
  lines: 14-18
- kind: function
  qualified_name: app/src/lib/sessionTitle:displayTitle
  lines: 21-24
- kind: function
  qualified_name: app/src/lib/sessionTitle:updatedAt
  lines: 28-31
- kind: type
  qualified_name: app/src/lib/sessionTitle:SessionLike
  lines: 36-36
- kind: function
  qualified_name: app/src/lib/sessionTitle:infoOf
  lines: 38-45
- kind: function
  qualified_name: app/src/lib/sessionTitle:byRecency
  lines: 47-49
- kind: function
  qualified_name: app/src/lib/sessionTitle:relativeTime
  lines: 52-64
incoming_refs: 5
outgoing_refs: 4
---
<!-- trie:section symbol=app/src/lib/sessionTitle:DEFAULT_TITLE_PATTERNS fingerprint=f6f2bca4e6746a5b1f35d1c20e5f0002e54223f9697cc46c5000f845847a05d9 body_fp=84dd00f9f954d7483619ae3418cbb19f09cd337feb4b09aa4b4c5cdb4dd8d0b0 source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=config -->
Regex list matching placeholder titles opencode assigns before a real title is generated.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:isDefaultTitle fingerprint=42577ff45aa6225db32152d980ca5d956f447ef6740fe9d91718edcf7ef9aed3 body_fp=b638e392bc25a42a6a416b0e9d52f7d0c6fb4630d9aafe75b9f698144057367e source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Return `true` if `title` is empty, blank, or matches a known placeholder pattern (e.g. "new session", "untitled").
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:displayTitle fingerprint=1bb89689bbe10ddabcf38a75328ba2a45f90e48ba7e76dd88ac22aa9ffc41d44 body_fp=48892b8ff37b4c7c512fae52964e722547d07619d7666553d0bd5ee93b7793eb source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Return the human-facing title for a session, falling back to `"New chat"` if the title is absent or a default placeholder.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:updatedAt fingerprint=98f0527662585c1a75b77bb367d653b9c8892c94e3d0f91936cef09860261ed9 body_fp=6cd2a2ee2e7cefaa83826c0731a71d079ddcef688e1eebc051bae39841ed3cfd source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Return the best-available last-activity timestamp in milliseconds for a session, falling back to `0`.

- `info` — prefers `time.updated`, then `time.created`; returns `0` if either field or `info` itself is absent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:SessionLike fingerprint=d03b790057bfaf9d0008df7a643d06db80b715710bb603245b9674a611316cd0 body_fp=72ad8994b228b3bd1b120925b2c347946efe567796ae26bf6cb7c215e3e8ed67 source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=model -->
Union type accepted by `byRecency` and `infoOf`: a bare `OpencodeSession`, a wrapper object carrying an optional `.info` field, or a nullish value.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:infoOf fingerprint=63de3919a2b61867ac6950ca92d247a6f31427cf879246591673262480138f5c body_fp=74793688472dcf22a93f2ae5de6610af826d89721f14a1d6e42ecc59524fbe5c source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Extracts an `OpencodeSession` from a `SessionLike` value, handling both wrapped `{ info }` objects and bare `OpencodeSession` instances.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:byRecency fingerprint=1dbb3d242c8f80bdba0a2410a557e93d216e42b21d9737d9a2976419310fb110 body_fp=b9671e3dd3a5d4ff02e672ac643c16dde52ae46b525d3d0719b48d455b37de73 source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Sort comparator returning most-recently-active `SessionLike` first, accepting both bare `OpencodeSession` and `{ info?: OpencodeSession }` wrapper shapes.
<!-- trie:end -->
<!-- trie:section symbol=app/src/lib/sessionTitle:relativeTime fingerprint=18162670b1a0bde16b61a3fc2d34053a07ddbcc0173276bf1492707ea06d5d8b body_fp=d550e858f76beb80a475bff5b3684287811eba6e4a09eb996cbd3a85d05ae8f8 source_ref=10287571e9cc93067699961ca9279724a9e247a0 role=util -->
Convert a millisecond timestamp to a compact human-readable relative-time label.

- `ts`: epoch-ms timestamp; returns `""` for falsy values.
- Returns one of `"just now"`, `"Nm"`, `"Nh"`, `"Nd"`, or `"Nw"` depending on elapsed time.
<!-- trie:end -->