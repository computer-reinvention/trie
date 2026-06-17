---
trie_version: 0.1.9
source: app/src/graph/agentChoreography.ts
file_fingerprint: 11dd448b9d65390636193c3d3c422b81b8f361fbac73dcd68c0962cf9d30dbce
last_synced_at: '2026-06-17T16:38:45Z'
defines:
- kind: type
  qualified_name: app/src/graph/agentChoreography:Intent
  lines: 18-18
- kind: interface
  qualified_name: app/src/graph/agentChoreography:ChoreographyResult
  lines: 20-31
- kind: constant
  qualified_name: app/src/graph/agentChoreography:EMPTY
  lines: 33-40
- kind: function
  qualified_name: app/src/graph/agentChoreography:bareTool
  lines: 43-45
- kind: function
  qualified_name: app/src/graph/agentChoreography:asString
  lines: 47-49
- kind: function
  qualified_name: app/src/graph/agentChoreography:qnamesFromOutput
  lines: 52-104
- kind: function
  qualified_name: app/src/graph/agentChoreography:choreographFor
  lines: 107-169
incoming_refs: 1
outgoing_refs: 1
---
<!-- trie:section symbol=app/src/graph/agentChoreography:Intent fingerprint=52873b90871254827cbe0b2db119dc50d470cf9ac641931e775277e2b28ee43d body_fp=b5957d01180c8e670a00757e72a8ef089c1562dbed9c4121b67553b43783f7f5 source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=model -->
Union type representing the three agent tool intents: reading symbols, scanning/grepping, or writing.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:ChoreographyResult fingerprint=66483d149aa2de3a38e66ada47c7b725e0eaf5793b59152053d333a36f932783 body_fp=f2643418c7202d050abdfdc79928502d4ddccceb89c382658fb565ba3dbf8abf source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=model -->
Describes the full choreography output for a single agent tool part: which symbols glow, which file paths glow, where the camera follows, and which edges animate.

- `reads` / `scans` / `writes`: qnames to glow blue, violet, or amber respectively
- `files`: file paths that trigger a whole-file glow on write
- `follow`: single qname the camera tracks; `null` for scan-intent tools
- `flows`: ordered edge pairs to animate as comets along the graph
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:EMPTY fingerprint=e76473a5bb1a62f27260b5bbd1465ed9bc1eeba08f09649657d257f6ffd68148 body_fp=2d4eed080caf79ae84f0cf2e059706e8365ae0fc4ea7feac79cbd31be641feb2 source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=model -->
Zero-state `ChoreographyResult` used as a spread base in every `choreographFor` branch to avoid repeating empty field defaults.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:bareTool fingerprint=2c654faaff2aabbc1649e2593d811b1c6f5f58bb5e0ddbf19e0f4e00da337dcd body_fp=0eda454e93b80a0cde481ab8fd275e260c030fbbcfb27e3dd4b3ebb056656484 source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=util -->
Strip the `trie_` MCP server prefix from a tool name, returning the bare verb.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:asString fingerprint=031e8bf1828d555e89bc3e53f72d830489f49747eb2fdd7aae32ce0f3bef7128 body_fp=25efef4903b9c15f02af4dbb0bc558799ac756dc4ed4b0887570c11e5f4669cb source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=util -->
Return `v` as a non-empty string, or `null` if it is not a string or is empty.
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:qnamesFromOutput fingerprint=908b6105e434dd6ab9a0929d67819b050d51bc2e9763f8f67d1ce83090a80dc8 body_fp=27bbb1f3b4af2f4d92fc056f02022ee82856bfd128eda7ad7409fc164d274017 source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=parsing -->
Parse a tool's JSON result string and extract all qnames and directed edges into `hits` and `flows`.

- `output` — raw JSON result text from a trie tool; returns empty collections if absent or unparseable.
- `hits` — qnames collected from `hits`, `match`, `similar`, `callers`, `callees`, and `fallback.matches` fields.
- `flows` — directed pairs from `edges[].{from,to}` (trace) and `paths[]` chains (trace_flow/explain_flow).
<!-- trie:end -->
<!-- trie:section symbol=app/src/graph/agentChoreography:choreographFor fingerprint=b5ed0dd6799b263426269ae231aae610a1b1f44c64405db5bb96f2b34744550c body_fp=fec0b547c616efcd2edb90e887e1764d14b30e77ce384f0e04509a496c2b1344 source_ref=b0f6281741accb88b6d618b78d0bac52bf52473f role=domain -->
Map a single `ToolPart` to a `ChoreographyResult` describing which symbols to glow, which file paths were edited, and which symbol the camera should follow.

- `part` — the live tool part; reads `part.tool`, `part.state.input`, `part.state.status`, and `part.state.output`
- Returns `EMPTY` (all arrays empty, `follow: null`) for unrecognised tools
- `follow` is set only for read/write intents; scan intent never sets it
- `flows` populated from parsed tool output only when `status === "completed"`
- File-write tools set both `files` and `writes` to the path; `follow` is always `null` for them
<!-- trie:end -->