---
trie_version: 0.2.1
source: trie/render.py
file_fingerprint: 34d956ca914d483316449635b4eded9b9c7a31ba6d5a1c56643423dacb33e115
last_synced_at: '2026-08-01T01:14:48Z'
description: "Plain-text rendering for tool envelopes \u2014 the default output format\
  \ on"
defines:
- kind: module
  qualified_name: trie/render:__module__
  lines: 1-182
- kind: constant
  qualified_name: trie/render:PROSE_KEYS
  lines: 24-26
- kind: function
  qualified_name: trie/render:_squeeze
  lines: 31-34
- kind: function
  qualified_name: trie/render:_prose_block
  lines: 37-38
- kind: function
  qualified_name: trie/render:_is_chain
  lines: 41-47
- kind: function
  qualified_name: trie/render:_symbol_record
  lines: 50-85
- kind: constant
  qualified_name: trie/render:_RECORD_KEYS
  lines: 88-107
- kind: function
  qualified_name: trie/render:_render_value
  lines: 110-153
- kind: function
  qualified_name: trie/render:render_envelope
  lines: 156-181
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=trie/render:__module__ fingerprint=8fbe82ad99c9ec0b83af5c8e333c40b4c71c6e5597cf110a3787caeafdb5f2ad body_fp=80b8f4a07d898d8fc69a7de5f44c95d89d4978c711c98e69d5a24d0fe30d0697 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Render tool-envelope dicts as dense, human-readable plain text for CLI and MCP surfaces.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:PROSE_KEYS fingerprint=6110bc299df2e3cb29d9865d247a80501e423c1ead0133815bd4b44e2dfb7ce5 body_fp=4aa1c6d040011658c1d9066c8d5c8ddaa94a7c07c4120ad66209cad5d4962424 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=config -->
Frozenset of envelope keys whose values are rendered as verbatim prose blocks rather than collapsed single-line entries.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_squeeze fingerprint=0932ec4c3ee8759cd62e7b299df7ce15342bd259c8db9370de4ea4c28bb9d92e body_fp=897103df7b28472288b0d06463ff17b125576e94f74395f1997eef117baa719c source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Collapse whitespace runs in `text` to a single space-separated line, truncating to `cap` characters with a trailing `…`.

- `cap`: maximum output length in characters; defaults to 160.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_prose_block fingerprint=b64c36d3a0606df5cf4058372234bb83329f04e0e4d5bdbe0e95b9878537bb18 body_fp=5a59d81c1431a5c0fcfb40515dfee3cef072a949ed1703c8628ab612c695af35 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Convert `text` into indented lines, preserving blank lines as empty strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_is_chain fingerprint=75a5239e406d3f40549370baa75bf0768399fc54ecfb22e01c5058a786a0080c body_fp=12c9b09b677dd69a3cf8b9501aa66edf31b5cd162383e44cdd11ddd271e7d574 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Return `True` if `value` is a call-chain: a list of ≥2 colon-containing, space-free strings.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_symbol_record fingerprint=89e8fe2fad2cc808887feda641654be332f5dcd1227af42588229f1ec2c1624f body_fp=e017c659b99724cb5f9d8f191b7f5185c6998d2b90c7558b32ebb16b51e8e811 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Format a symbol dict into text lines: one header line (qname, kind, pointer, metrics), then collapsed signature, one-liner, and prose block.

- `rec`: symbol envelope dict; reads `qname`, `kind`, `file_pointer`/`source_pointer`, `inbound_count`, `outbound_count`, `score`, `match_count`/`text_match_hits_in_body`, `pending_patch_count`, `signature`, `one_liner`, `prose_snippet`, `prose`.
- `indent`: string prepended to every line; prose block uses `indent + "    "`.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_RECORD_KEYS fingerprint=b140cc3305f7a1d9250d59bb78e5abad8a33f37b4fb1725d8489532dce054bcc body_fp=d5fd31ab2890da7ed1e6589f96ddbf96ca3cab8af41d1928b7c9d27a5147b1eb source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=config -->
Frozenset of envelope dict keys that identify a pure symbol record, used by `_render_value` to dispatch to `_symbol_record`.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:_render_value fingerprint=448c8213d69f3de908c3a8246526f0642e015d497d99659f639822a261127d59 body_fp=85165a10ac42f9db4314aee3ae392b79c67b523b7fec7ab8a70202cc9bddf5e3 source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Recursively render one envelope key-value pair into indented text lines, dispatching on value type.

- Prose-keyed or multiline strings render as indented blocks via `_prose_block`.
- Dicts matching `_RECORD_KEYS` are formatted via `_symbol_record`; others recurse per key.
- Lists of ≥2 qname strings render as arrow-joined chains; lists of dicts render as symbol records or recurse; empty lists render as `(none)`.
<!-- trie:end -->
<!-- trie:section symbol=trie/render:render_envelope fingerprint=9bcaabd0bca84b15fadcdfccda16da6b571e1e54528d6f6899c6e7615f39b2c7 body_fp=9cfd50fad7f968e18133fe8b758f842855e76e478700c722fe4c6bc3e58e633c source_ref=2685ce56e95e5d51f5a54b767e09bfdf72d5a684 role=util -->
Convert a tool-result envelope dict to a dense, human-readable plain-text string.

- Error envelopes emit `error <code>: <message>` plus optional suggestion line.
- Suppresses `callers`/`callees` keys when a `story` or `usage_story` field is present.
<!-- trie:end -->