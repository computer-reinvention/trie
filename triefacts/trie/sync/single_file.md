---
trie_version: 0.1.0
source: trie/sync/single_file.py
file_fingerprint: a96a71dbae311d4d30916bb4e099cbcb794cf4b8c12c114fd60d901427768f8a
last_synced_at: '2026-05-16T10:52:02Z'
defines:
- kind: class
  qualified_name: trie/sync/single_file:FileSyncResult
  lines: 25-36
- kind: class
  qualified_name: trie/sync/single_file:_SymbolJob
  lines: 40-50
- kind: function
  qualified_name: trie/sync/single_file:_file_fingerprint
  lines: 53-54
- kind: function
  qualified_name: trie/sync/single_file:_triefact_path_for
  lines: 57-61
- kind: function
  qualified_name: trie/sync/single_file:_file_description
  lines: 64-79
- kind: function
  qualified_name: trie/sync/single_file:_build_defines
  lines: 82-95
- kind: function
  qualified_name: trie/sync/single_file:_resolve_previous_symbols
  lines: 98-143
- kind: function
  qualified_name: trie/sync/single_file:sync_single_file
  lines: 146-398
incoming_refs: 41
outgoing_refs: 15
---
<!-- trie:section symbol=trie/sync/single_file:FileSyncResult fingerprint=f658b6cb6f956faf262f29751e15b6efaad12e661c2976d58946940db38a0ed7 body_fp=a14f526007aca92c0796d86e378c557ef5d8443dcb245ccd6b6df85d0970222e source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `@dataclass(frozen=True) class FileSyncResult`

Immutable result record returned by `sync_single_file` summarising token usage and mutation counts.

- `symbols_skipped`: count of symbols whose sections were passed through unchanged; always 0 when `symbols_to_regen` is `None`.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:sync_single_file fingerprint=cb552dd45724d07a7a457aeb0b5bfcf304002f1acb45a55d76bd98b9f488d62f body_fp=203ac363337b2fbbcc12d7035ecbd08eece56d9a939ce747ac824cacf77d13f8 source_ref=a30269d37f5e1cf5ab115c021914f0ca703881fd -->
## `sync_single_file(source_path, *, project_root, config, client, dest_triefact_path=None, store=None, symbols_to_regen=None) -> FileSyncResult`

Generate or refresh the triefact file for a single Python source file, upserting sections for all parser-surfaced symbols and removing stale ones.

- `symbols_to_regen`: `None` regenerates every symbol; a set of qnames limits LLM calls to only those symbols, passing others through byte-identically.
- `dest_triefact_path`: write output here instead of the canonical path; canonical file is still read for existing prose.
- `store`: when provided, enriches front matter with ref counts and records one-liner metadata; omit to skip graph queries.
- Raises `ValueError` if `source_path` is not under `config.triefacts.source_root`.
- Per-symbol LLM calls run in parallel via a `ThreadPoolExecutor` bounded by `config.sync.concurrency`; triefact and store mutations remain on the calling thread.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_file_fingerprint fingerprint=46c7c51a18ded3953f42cbf0478b0794532566079fd73b079dc9950d2c108e07 body_fp=3a3a26dce28d844c40dcedf8ffb17e41b1542e859c3800b44309f7e9e7760efe source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `_file_fingerprint(text: str) -> str`

Return the SHA-256 hex digest of the given UTF-8 encoded text.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_triefact_path_for fingerprint=1c2e2cf4fa444cf778b7950d1adb2c52f77952ba318f32650aa629fbcb6ee9a5 body_fp=3fe961a056cd9f4b2fb40203afcdedae833dd9933bc828a0fc4d2182c5c35f76 source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `_triefact_path_for(source_path: Path, project_root: Path, config: Config) -> Path`

Compute the canonical `.md` triefact output path for a given source file.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_file_description fingerprint=97cc879f813f006954b5d0e6ede8050e2fe029e19ecc73d275a9986d8eaed371 body_fp=86b0cdf9461941f9fa7f2413af86cc19f3122447ee5e84eb37580e1a2658619b source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `_file_description(source_path: Path) -> str | None`

Return the first non-empty line of a Python file's module docstring, or `None` if absent.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_build_defines fingerprint=ff4c3234574641e864f5fd19df73f86a54f735ea2a1cb641153e502aca6f4f1a body_fp=f7dfdb6e9d1dff6c73c6175b88eb0b0bc66633d1af032b6f73dadf4943411afe source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `_build_defines(symbols: list[Symbol]) -> list[dict[str, object]]`

Build a sorted list of `{kind, qualified_name, lines}` dicts for all documented symbols.

- `lines`: formatted as `"start-end"` string, not separate integers.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_resolve_previous_symbols fingerprint=7248cfa7303b0870f3a978ae9e249057d98b22401fd3291ebff715fa17660edf body_fp=e237e39e84175b49d59721b8651980fd55e40f83eb51c1a791fc724b713dcc5c source_ref=d6da1d131c5c5e11b320faa2c7147616cfbd1f01 -->
## `_resolve_previous_symbols(*, source_path, src_root, project_root, existing_section_refs) -> dict[str, Symbol]`

Retrieve and parse previous-version `Symbol` objects for each qname that has a recorded `source_ref` blob hash.

- `existing_section_refs`: mapping of qname → git blob hash from existing triefact sections.
- Returns empty dict if `existing_section_refs` is empty or all blobs are unresolvable.
- Deduplicates git calls by grouping qnames sharing the same blob hash.
- Silently skips qnames whose blob is unreachable, parse fails, or qname no longer exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/sync/single_file:_SymbolJob fingerprint=0f7b75b7a065300e3f0be7a0e01b8244c10ca3f48b6706b7dbfea7ecaacef021 body_fp=411cee5f28da64fe84f1a50ff955f2cc491ae480049fbb36924b161010ffa562 source_ref=a30269d37f5e1cf5ab115c021914f0ca703881fd -->
## `_SymbolJob`

Holds one symbol's inputs for the thread-pool generate phase.

- `previous_source`: prior signature+body from git blob; `None` triggers cold-write mode.
- `previous_prose`: existing section body; `None` triggers cold-write mode.
<!-- trie:end -->