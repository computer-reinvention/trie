---
trie_version: 0.1.9
source: app/src/settings/trieCommands.ts
file_fingerprint: 61f5e6fed682918da528dffeba80ddb9ecf76217515734b53472244ed9f5ced4
last_synced_at: '2026-06-17T16:39:54Z'
defines:
- kind: type
  qualified_name: app/src/settings/trieCommands:FlagType
  lines: 5-5
- kind: interface
  qualified_name: app/src/settings/trieCommands:CommandFlag
  lines: 7-20
- kind: interface
  qualified_name: app/src/settings/trieCommands:CommandDef
  lines: 22-36
- kind: constant
  qualified_name: app/src/settings/trieCommands:TRIE_COMMANDS
  lines: 38-202
- kind: function
  qualified_name: app/src/settings/trieCommands:buildArgs
  lines: 206-220
incoming_refs: 8
outgoing_refs: 0
---
<!-- trie:section symbol=app/src/settings/trieCommands:FlagType fingerprint=1a4c45df9473ee4271d8b8e23dbff05463edea6fd452ba088e058af962cae742 body_fp=82772d7019ed9c9b3f1f9d6b68eb2ea0a8ca074d82375846f9917c67fe416a27 source_ref=3970220964531885bebbb020f438eeda05e934f2 role=model -->
Union type enumerating the four value kinds a `CommandFlag` can represent.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands:CommandFlag fingerprint=bde8e901e47a8a63fc5692fffc8ab8c36c60ba6a1f353966f734967e712c3096 body_fp=5a320f9afcf80e398641a66620a2388c41e630ccc1ee117a66cd7a2da20f2f6e source_ref=3970220964531885bebbb020f438eeda05e934f2 role=model -->
Describes a single user-tunable CLI flag within a `CommandDef`, including its form binding and input constraints.

- `flag`: the raw CLI flag string passed to trie-cli (e.g. `--all`, `--limit`)
- `key`: doubles as React key and form state key
- `enum`: only present when `type` is `"enum"`; supplies allowed values with display labels
- `min` / `step`: numeric input constraints; only relevant when `type` is `"number"`
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands:CommandDef fingerprint=ca51a5bfd988c23b4d934a4f676e0b70fd98bcec3704d8644efefe30559b3368 body_fp=db6f0c5c9ab959e2fcfad2aa91b29e8c8f9d578f9902cbbe006bc997e55d6617 source_ref=3970220964531885bebbb020f438eeda05e934f2 role=model -->
Describes a single trie CLI command with its metadata, cost/streaming flags, and user-tunable flag definitions.

- `costly`: shows a cost warning in the UI when `true`
- `json`: emits `--json` and parses JSONL events for a structured progress view
- `fixedArgs`: always prepended to argv, regardless of user flag selections
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands:TRIE_COMMANDS fingerprint=85d914a7b821dce4becd79095b9dbb135d07ce4697904c4570b8fb7d5d59b6fe body_fp=1d692735cb37f1d0c96fdaed0cc0ab3361c483e22d7c0d6226cebeb9d8a78e89 source_ref=3970220964531885bebbb020f438eeda05e934f2 role=config -->
Declarative registry of all trie lifecycle `CommandDef` entries consumed by the command panel and command store.

- Commands: `init`, `refresh`, `sync`, `plan`, `verify`, `status`, `audit` — in display order.
- `sync` is the only entry marked `costly: true` (LLM cost warning shown).
- `refresh` and `status` set `json: true` (structured JSONL event stream expected).
- `init` hardcodes `fixedArgs: ["--no-install-hooks"]` — hook installation is always suppressed.
<!-- trie:end -->
<!-- trie:section symbol=app/src/settings/trieCommands:buildArgs fingerprint=6f4b42ec4588c760005b21de3045b331a63396835ba0edaab15f8fb6a5eca5ad body_fp=845af0093fd7aa62a105cbaa15484242098b76ad4eb614c9ed03f6e859b28e17 source_ref=3970220964531885bebbb020f438eeda05e934f2 role=util -->
Build the argv list (flags after the subcommand) from a `CommandDef` and a form-values map.

- `def` — command definition supplying `fixedArgs` and `flags`; `fixedArgs` are prepended unconditionally.
- `values` — keyed by `CommandFlag.key`; booleans are included only when `true`; non-boolean values are skipped if `undefined`, empty string, or `NaN`.
- Returns a flat `string[]` ready to append after the subcommand token.
<!-- trie:end -->