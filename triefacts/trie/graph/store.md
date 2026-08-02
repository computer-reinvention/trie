---
trie_version: 0.3.0
source: trie/graph/store.py
file_fingerprint: ca79cb847185dbec258df42caea5059da06f1d421d40ed55af36095f5762983a
last_synced_at: '2026-08-01T01:52:14Z'
defines:
- kind: module
  qualified_name: trie/graph/store:__module__
  lines: 1-1260
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_VERSION
  lines: 18-18
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_SQL
  lines: 22-116
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 120-123
  signature: class FileRecord
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 127-130
  signature: class FileStats
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 134-141
  signature: class SymbolHit
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 145-170
  signature: class SymbolDetail
- kind: class
  qualified_name: trie/graph/store:GrepPredicate
  lines: 174-196
  signature: class GrepPredicate
- kind: function
  qualified_name: trie/graph/store:_synchronized
  lines: 199-216
  signature: 'def _synchronized(method: Callable) -> Callable'
- kind: function
  qualified_name: trie/graph/store:_synchronize_store
  lines: 219-236
  signature: 'def _synchronize_store(cls: type) -> type'
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 240-1259
  signature: class Store
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 249-262
  signature: 'def __init__(self, db_path: Path) -> None'
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 264-290
  signature: "def _open(self) -> None: # check_same_thread=False because the lock \u2014 not thread affinity \u2014 # provides the mutual exclusion sqlite requires."
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 292-293
  signature: def close(self) -> None
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 295-296
  signature: def __enter__(self) -> Store
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 298-299
  signature: 'def __exit__(self, *_args: object) -> None'
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 302-308
  signature: def transaction(self) -> Iterator[sqlite3.Connection]
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 312-317
  signature: 'def get_file(self, path: str) -> FileRecord | None'
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 319-330
  signature: 'def upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None'
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 332-334
  signature: 'def delete_file(self, path: str) -> None'
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 336-342
  signature: def list_files(self) -> list[FileRecord]
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 346-375
  signature: 'def replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None'
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 377-388
  signature: 'def count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.count_section_records
  lines: 390-392
  signature: def count_section_records(self) -> int
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols_missing_role
  lines: 394-411
  signature: def count_symbols_missing_role(self) -> int
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 415-446
  signature: 'def replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 448-460
  signature: 'def references_in(self, qualified_name: str) -> list[str]'
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 462-474
  signature: 'def references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]'
- kind: method
  qualified_name: trie/graph/store:Store.symbol_hashes_for_file
  lines: 476-487
  signature: 'def symbol_hashes_for_file(self, file_path: str) -> dict[str, str]'
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 489-495
  signature: 'def qnames_in_file(self, file_path: str) -> list[str]'
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 497-516
  signature: 'def symbols_in_file_with_lines(self, file_path: str) -> list[tuple[str, int, int]]'
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 518-545
  signature: 'def search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]'
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 547-559
  signature: 'def references_out(self, qualified_name: str) -> list[str]'
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 561-562
  signature: def count_edges(self) -> int
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 564-573
  signature: def inbound_count_per_symbol(self) -> dict[str, int]
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 575-606
  signature: 'def file_ref_counts(self, file_path: str) -> tuple[int, int]'
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 608-630
  signature: def file_stats(self) -> list[FileStats]
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 634-694
  signature: 'def upsert_section_record( self, *, triefact_path: str, symbol_qname: str, section_fingerprint: str, one_liner: str, role: str = "", boundary: str = "", now: int | None = None, ) -> None'
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 696-709
  signature: 'def one_liner_for(self, qualified_name: str) -> str'
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 711-724
  signature: 'def one_liners_for(self, qnames: list[str]) -> dict[str, str]'
- kind: method
  qualified_name: trie/graph/store:Store.add_patch
  lines: 726-762
  signature: 'def add_patch( self, qname: str, note: str, reason: str, session_id: str, *, kind: str = "modify", rename_to: str | None = None, require_symbol: bool = True, ) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.add_delete_patch
  lines: 764-766
  signature: 'def add_delete_patch(self, qname: str, reason: str, session_id: str) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.add_rename_patch
  lines: 768-770
  signature: 'def add_rename_patch(self, qname: str, new_name: str, reason: str, session_id: str) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.add_create_patch
  lines: 772-798
  signature: 'def add_create_patch( self, *, target_file: str, target_qname: str, note: str, reason: str, session_id: str, anchor_qname: str | None = None, parent_class: str | None = None, ) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.get_create_patches_grouped
  lines: 800-827
  signature: 'def get_create_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]'
- kind: method
  qualified_name: trie/graph/store:Store.delete_create_patches
  lines: 829-853
  signature: 'def delete_create_patches( self, *, target_qname: str | None = None, session_id: str | None = None, all: bool = False, ) -> int'
- kind: method
  qualified_name: trie/graph/store:Store._patch_row_to_dict
  lines: 856-867
  signature: def _patch_row_to_dict(r) -> dict
- kind: method
  qualified_name: trie/graph/store:Store.get_patches_for_qname
  lines: 871-879
  signature: 'def get_patches_for_qname(self, qname: str, *, applied: bool | None = None) -> list[dict]'
- kind: method
  qualified_name: trie/graph/store:Store.get_all_patches_grouped
  lines: 881-892
  signature: 'def get_all_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]'
- kind: method
  qualified_name: trie/graph/store:Store.mark_patches_applied
  lines: 894-909
  signature: 'def mark_patches_applied(self, session_note: str) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.delete_applied_patches
  lines: 911-916
  signature: def delete_applied_patches(self) -> int
- kind: method
  qualified_name: trie/graph/store:Store.delete_patches
  lines: 918-943
  signature: 'def delete_patches( self, *, qname: str | None = None, session_id: str | None = None, all: bool = False, ) -> int'
- kind: method
  qualified_name: trie/graph/store:Store.get_patched_qnames
  lines: 945-953
  signature: 'def get_patched_qnames(self, *, applied: bool | None = None) -> list[str]'
- kind: method
  qualified_name: trie/graph/store:Store.patch_summary
  lines: 955-981
  signature: def patch_summary(self) -> dict[str, object]
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 985-1035
  signature: 'def get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None'
- kind: method
  qualified_name: trie/graph/store:Store.grep_symbols
  lines: 1037-1152
  signature: 'def grep_symbols( self, predicate: GrepPredicate, *, rank_by: str = "public_first", limit: int = 10, ) -> list[SymbolDetail]'
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 1154-1157
  signature: def all_symbol_names(self) -> list[str]
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 1159-1162
  signature: def all_qualified_names(self) -> list[str]
- kind: method
  qualified_name: trie/graph/store:Store.survey_symbols
  lines: 1164-1183
  signature: 'def survey_symbols(self, *, public_only: bool = False) -> list[tuple[str, str, str, str]]'
- kind: method
  qualified_name: trie/graph/store:Store.find_paths
  lines: 1185-1259
  signature: 'def find_paths( self, from_qname: str, to_qname: str, *, max_depth: int = 6, hub_threshold: int = 20, max_paths: int = 3, ) -> list[list[str]]'
incoming_refs: 95
outgoing_refs: 0
---
<!-- trie:section symbol=trie/graph/store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6f905ee5b88763bc3efda571c4cc279538d18efe8ee96eddcd1224a9d34490e2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
SQLite-backed persistence layer for trie's symbol graph, file fingerprints, and documentation metadata.

- Stores parsed symbols with cross-references as a queryable graph
- Caches file fingerprints to enable incremental scanning
- Tracks triefact section metadata including LLM-inferred roles and boundaries
- Supports patch management for pending documentation updates
- Provides search, path-finding, and batch operations for agent tools
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_VERSION fingerprint=8684c9277e19a742142d499c38b1e1fee8a8ff5a930544a68015f399f4e17dc8 body_fp=6a09e5a6737a4a1a5d051ca7dcd499b0b89812f914c6a1cbb2d50b95edffa080 source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=config -->
Version number for the SQLite database schema, triggering recreation when incremented.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_SQL fingerprint=e447a4f3d69ac65cd9aabaf7580306df5387ceae40e22589ce501c8f558dfdc0 body_fp=231cf935eff06abed63919b4d7ccbe1db39d46f804995b7359cad07f2a701c6d source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=config -->
Defines SQLite schema for trie's symbol graph database with tables for files, symbols, edges, triefact sections, and patches.

- `files`: tracks file paths, fingerprints, and scan timestamps
- `symbols`: stores parsed symbol metadata including qualified names, signatures, and line ranges
- `edges`: represents call/reference relationships between symbols with edge kind classification
- `triefact_sections`: caches generated documentation sections with LLM-inferred roles and boundaries; `hist_mass` / `hist_mass_ts` columns removed in this version
- `patches`: keyed by `qname TEXT` (not a symbol FK) to survive graph refreshes; includes `applied` and `session_note` seal columns and an index on `applied`
- `create_patches`: stores pending symbol creations targeting non-existent symbols; includes `applied` and `session_note` seal columns
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=7865a1c93374824243d46ef90906744de81c6611d2a098955bf8dde494514630 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
## `class FileRecord`

Immutable record storing file path, content fingerprint, and last scan timestamp.

- `fingerprint`: content hash for detecting file changes
- `last_scanned_at`: Unix timestamp of most recent scan
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=0daa3455558e3921b2b48fb15a0a894bf5ca972938bbeece240876742d5489ca source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
## `class FileStats`

Immutable record containing per-file symbol counts returned by Store.file_stats.

- `public_symbols`: legacy field name; equals `total_symbols` under current implementation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=68239d90b1db921fd472a0c304c6bff1e1322c7f65996f4284f7031508685fd3 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
## `class SymbolHit`

Immutable data record for symbol search results returned by `Store.search_symbols`.

- `name`: Local symbol name (not qualified)
- `qualified_name`: Full dotted path including module/class hierarchy
- `signature`: Function/method signature string; `None` for non-callable symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=434842c012b192c81334be8234403afc16f625ca71260f2296d77e12059eb78a body_fp=0eaf925046c2aebd4f2b8adbab0173082c7546d23bcf1501fd07c204f81f4e97 source_ref=6b17f7c7cdeef9470455fb704935cf18a7bdd3d0 role=model -->
## `class SymbolDetail`

Full per-symbol record with graph counts and cached one-liner for MCP tools.

- `one_liner`: empty string when no triefact section exists
- `role`: LLM-inferred architectural role tag, empty when unknown
- `boundary`: LLM-inferred boundary class (entry/exit/internal), empty when unknown
- `decorators`: newline-joined decorator lines, empty when none
- `fingerprint`: `body_normalized_hash` from the last scan; empty when unavailable; differs from sentinel fingerprint when prose predates current source
- `pending_patches`: list of patch dictionaries for this symbol
- `pending_patch_count`: number of pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:GrepPredicate fingerprint=bb94fc53eb9ffe605f051d331b0b74099549200f353c204750e987092d9ac0e6 body_fp=46cb39b661d5db1551b3e3a1730fa3c18eb15666045b7f84dccdf0400bf12154 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=model -->
## `class GrepPredicate`

Server-side filter object for symbol search queries in Store.grep_symbols.

- `name_contains`: substring match against symbol name
- `scope_prefix`: file path prefix filter
- `scope_exclude`: tuple of file path prefixes to exclude
- `inbound_count_min/max`: edge count range filters for incoming references
- `outbound_count_min/max`: edge count range filters for outgoing references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:_synchronized fingerprint=c94c45b26af5cc2b0f699d277c3b8f0b0b6cb111ffccb411c1975b0481c9333f body_fp=de19a6e15abfa60e1f01b984d68de869a6490ff03681cb85b42ff1b371e8fc9b source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=util -->
## `def _synchronized(method: Callable) -> Callable`

Wraps a Store method to execute its entire body under `self._lock` for SQLite thread safety.

- Prevents concurrent access to the shared connection which causes misleading SQLite errors
- Returns a wrapper function that acquires the re-entrant lock before calling the original method
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:_synchronize_store fingerprint=d1b9aace629d6d0844b4d70d2944ac013cb73c7b14e7e0eba36652fd84d9533f body_fp=a597f60cd18da15afbed54276fff43032ad43b96d909017f3a497cb4d1d6a80c source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=util -->
## `def _synchronize_store(cls: type) -> type`

Decorates a class to apply `_synchronized` to all public methods for thread-safe database access.

- Skips dunder methods and the `transaction` contextmanager to avoid lock conflicts
- Only wraps callable instance methods, not static or class methods
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store fingerprint=33e359213306b5a83ff713ac1cbe1397b7443e18d4e893132c4809adf5e1ef12 body_fp=c5cfd53eab9a76273941906a640a99190e27ad92c6e89d986c1ba77016b82dda source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
## `class Store`

SQLite-backed persistence for trie's symbol graph and file fingerprints.

Store provides thread-safe access to a SQLite database containing files, symbols, reference edges, triefact sections, and patches. All schema is auto-created and version-bumped when stale. The connection uses a re-entrant lock to guard concurrent access from worker threads during wave-based sync.

- `db_path`: Database file path, created with parent directories if needed
- `_lock`: Threading RLock protecting all connection operations
- `_conn`: SQLite connection with foreign keys enabled
- File operations: track fingerprints and scan timestamps for incremental updates
- Symbol operations: store parsed symbols with metadata like qualified names, signatures, line ranges
- Edge operations: maintain reference graph between symbols, filtering external/self-references, storing edge kind
- Section operations: cache generated triefact one-liners and LLM-inferred role/boundary tags; `upsert_section_record` no longer accepts or stores `hist_mass`/`hist_mass_ts` parameters
- Patch operations: store pending documentation corrections keyed by qname (survives graph refreshes); `add_patch` accepts `require_symbol=False` to allow removal notes for gone symbols; `get_patches_for_qname`, `get_all_patches_grouped`, `get_patched_qnames`, and `get_create_patches_grouped` all accept an `applied` filter; `mark_patches_applied` and `delete_applied_patches` manage the apply/consume lifecycle
- `grep_symbols`: ranking demotes test-path symbols within every bucket before `LIMIT` is applied, preventing test symbols from crowding production symbols out of results
- Query methods: search symbols by name patterns, get details with edge counts, find call paths
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__init__ fingerprint=96b28781440a25c3d116c96dc0909cc81a80b4ab488857c0f7339c90620fdcb4 body_fp=6d436cb7d8e0050bc9a0aaa4b0bc7964b9036eb7cb3e72df5ec0f67c2244b97e source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=orchestration -->
## `def __init__(self, db_path: Path) -> None`

Store initializer creates a re-entrant lock, database directory, and opens the SQLite connection.

- Creates parent directories if they don't exist
- Initializes threading lock to guard concurrent access to connection
- Calls `_open()` to establish connection and apply schema
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._open fingerprint=2db77cc3475ec4448fea96703d16cab52d1530182b8118e946b15feccd865d62 body_fp=3055c151c7673b1535c48282daa952bd30a103f89b867e3b1dd7a45ac1280319 source_ref=745f21ee2948bc12ab64d268d7880452f6a96d0b role=persistence -->
## `def _open(self) -> None: # check_same_thread=False because the lock — not thread affinity — # provides the mutual exclusion sqlite requires.`

Store._open opens SQLite connection and initializes/migrates the database schema.

- Detects schema version mismatches and deletes stale database files
- Enables foreign key constraints via PRAGMA
- Creates tables from SCHEMA_SQL if not present
- Inserts current SCHEMA_VERSION on fresh database creation
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=c80df2c7b68b14c1f3475f42e421ae512d6ed735ad2d77b7ec323616a9ec1483 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def close(self) -> None`

Closes the Store's SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=d69a8d31556fe45e10936217b9a28167bd83d8dbbd0681d30a1f80ffe36a5bbc source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
## `def __enter__(self) -> Store`

Returns the Store instance for context manager entry.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__exit__ fingerprint=67b1b6b146522ac7c8bdfff45bab8a41537d8e61231b937b0475a712971729e7 body_fp=4077f62642fc91f4372d72f155cdd3f37975f2454eb26ba55a49ae546544683f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
## `def __exit__(self, *_args: object) -> None`

Store context manager exit method that closes the SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=1b877df6f4c41a49b79c239024909e4d4e85f92c2528de4dfe5262069638c224 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
## `def transaction(self) -> Iterator[sqlite3.Connection]`

Wraps Store database operations in a context manager that commits on success and rolls back on exceptions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=77b99c27c406b9a820c1b4c0c3422f166803bb0310b9adfe3e8efb5239631969 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def get_file(self, path: str) -> FileRecord | None`

Store.get_file retrieves a FileRecord for the given path from the files table.

- Returns None if no record exists for the path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=1bf85f253c1f35ab3ddf6c03ab97a23f251cbe1ceb1d96ace4c3b6d2250f3d15 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None`

Store.upsert_file inserts or updates a file record with path, fingerprint, and scan timestamp.

- `now`: optional timestamp override; defaults to current time if None
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=36c0e5a9298629e2ae926d73af66e8cba95a9eff8e3c8d4ffa9a2cfd88cd5ed1 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def delete_file(self, path: str) -> None`

Store.delete_file removes a file record from the database and commits the transaction.

- Cascades to delete all associated symbols due to foreign key constraints
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=0fc07250a8f92e02c0dac45e778ac23dbbc9bd1bcfc0b70f9b7363a60c8692a1 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def list_files(self) -> list[FileRecord]`

Returns all FileRecord instances from the database, ordered by path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=40b1980316c50d05be01ab45d27176c3428961e7489644041c1872db015f19c1 body_fp=e61d97158996c83e68412a4edace9a14d09dd2344613bf8b53e363ffb8e2663a source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None`

Store.replace_file_symbols atomically deletes all existing symbols for a file and inserts new ones from the provided list.

- Uses a transaction to ensure atomicity between deletion and insertion
- Converts Symbol objects to database row tuples with proper type casting
- Joins decorator lists with newlines for storage
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=db07d86487a8a73401a6671972b04a6a0d5ed9bab26efa47a8146b5059977ba3 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int`

Count symbols in the database with optional file and visibility filtering.

- `file_path`: when provided, count only symbols in that file
- `public_only`: when True, count only symbols marked as public
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_section_records fingerprint=610f302acb473963e5a29105d08a8808237b8ffa314427ab6ac1f9a61e853fbe body_fp=4fd4f55887d6b7a12e1a638a99f9603f49f131da87348fa8a42bcd45824845cb source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def count_section_records(self) -> int`

Store.count_section_records returns the number of rows in the triefact_sections table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols_missing_role fingerprint=b561b4d71aee1cc5a1c9bd9db7eb9512fd5929bdd36a0d3d108e502a516c06cd body_fp=bfeef252d7a76e59a25abb25f51356e12eb08df1a84329ae9451e1f6c8e84f55 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def count_symbols_missing_role(self) -> int`

Store.count_symbols_missing_role counts symbols without non-empty role tags in triefact_sections.

- Returns symbols with no section record or empty role string
- Used to short-circuit role auto-backfill when all symbols are tagged
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=41beb7afd9fb09d3072e05b524261ba259d6f9ecaed8f6ea1dc7126e95a5608a body_fp=db56a78c26c5fe73a8ac2d45c554cbcfec21335b114ef674009a7bd6e5f0f352 source_ref=dd47f824faeb09b6106e6961b05962e87fe03c05 role=persistence -->
## `def replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int`

Store method that wipes the edges table, resolves references to symbol IDs, and inserts new edges.

- Drops references where source or destination qualified names aren't found in symbols table
- Deduplicates identical edges and skips self-references
- Stores reference kind alongside edge source and destination IDs
- Returns count of edges actually inserted
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=87da43d1bef249ef28eafa7d131b1f451cae3d5a4c41d18e73be18de30aaeaa2 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def references_in(self, qualified_name: str) -> list[str]`

Store.references_in returns qualified names of all symbols that reference the given qualified name.

- `qualified_name`: target symbol to find incoming references to
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=7e3d8fa7fc953b8d09b91a5b3a25adac74a27e76f73dee560e69cebbd1baed4f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]`

Store.references_in_with_files returns `(src_qname, src_file_path)` tuples for every symbol that references the given `qualified_name`.

- Extends `references_in` by including the file path of each referencing symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.symbol_hashes_for_file fingerprint=c7cfa2cf6e7561a2887cee891e877879584d005ce8e7a9e1b5fcdf1afcfa24c0 body_fp=7b09c30cd4413a580440c52f2c89682e7ec1dd246d9ac0ed46028dd5f8737c0a source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
## `def symbol_hashes_for_file(self, file_path: str) -> dict[str, str]`

Return `{qualified_name: body_normalized_hash}` for all symbols in `file_path` from `Store`'s `symbols` table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=0f0e47dff18a2430f086a8aaa2213e6bcbdd175e2708288619de45ae31d7ed64 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def qnames_in_file(self, file_path: str) -> list[str]`

Store.qnames_in_file returns qualified names of all symbols defined in the given file path, ordered by start line.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.symbols_in_file_with_lines fingerprint=6c50f1692f561e61d68233e23f1452068b7dc5151923fcf1a75c9e9f32d8fc97 body_fp=383a2d4b67079e9163247458c38927c612e33600d617c357a0ca31a2144ad00f source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def symbols_in_file_with_lines(self, file_path: str) -> list[tuple[str, int, int]]`

Store.symbols_in_file_with_lines returns qualified names and line ranges for symbols in a file, ordered by start line.

- Returns tuples of `(qname, start_line, end_line)` for line bracket calculations
- Used by locate's grep fallback to map source lines to enclosing symbols
- Returns empty list if file has no recorded symbols or doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=508cd68d6b496d97a3e7981d52e2724c9e88bbf03a27ec5e29443c5650dde60a source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=api -->
## `def search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]`

Finds symbols whose local name contains a pattern via case-insensitive substring match.

- Returns up to `limit` `SymbolHit` instances ordered by public symbols first
- Searches the `name` field (local part) not the fully qualified name
- Designed for agent "find_symbol" queries that typically use local names
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=ad903b72d924708c3357bbb5a84f2c33b24adc76ca73095fcc385b339d4c45a3 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def references_out(self, qualified_name: str) -> list[str]`

Returns qualified names of all symbols referenced by the given symbol.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=e05a6efe8f80e09ec52b101b358eb9fc35da9ffdd35f78f0ea1735e92fe30e74 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def count_edges(self) -> int`

Store.count_edges returns the total number of edges in the graph database.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=4df95b02d0a5fedff85863a91b5681a3d4e1bd6b764caf06d71f54059aecb856 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=domain -->
## `def inbound_count_per_symbol(self) -> dict[str, int]`

Store.inbound_count_per_symbol returns a dictionary mapping qualified names to their inbound edge counts.

- Used to detect hub symbols with many incoming references
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=bf982e54730e691d4f235e2ea25f000e8eb351ce5f091f72ab4a025d077abe4d body_fp=c510ef87b242df2610bf3ba317564452c59b9ac4abcbba951f4e2d24e6c33bef source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def file_ref_counts(self, file_path: str) -> tuple[int, int]`

Store.file_ref_counts returns cross-file inbound and outbound reference counts for a file.

- Inbound: references to symbols in this file from symbols in other files
- Outbound: references from symbols in this file to symbols in other files
- Excludes intra-file edges between symbols within the same file
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=818ee47e02de6186ac43c3deb53c5ddc50df1980e52047b405fca30d50d264d6 body_fp=08f3838decdb4b6a637250e7fb3bade99750907915d26654e47b1b85a255cc54 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def file_stats(self) -> list[FileStats]`

Returns per-file symbol counts from the Store for bootstrap ranking.

- `public_symbols` field is legacy naming; equals total_symbols count under current parser
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=4e4648b17b75c619be60bae4c667fd4ae21f12f086877226dc45b454cf980256 body_fp=9649124c047858c20bcdf215ea2f4850fd0998a2bb5653e3cba21c2deeb872d1 source_ref=a24eaf0dc9b17f272094d1b0167721b0dc9ceb26 role=persistence -->
## `def upsert_section_record( self, *, triefact_path: str, symbol_qname: str, section_fingerprint: str, one_liner: str, role: str = "", boundary: str = "", now: int | None = None, ) -> None`

Records or refreshes Store triefact section metadata for a symbol with LLM-inferred tags.

- Silently skips if symbol no longer exists in database
- Empty role/boundary values preserve existing non-empty values during updates
- Commits transaction immediately after upsert
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=e12701589966eec2b166abad415cc975e7b836018277a6f17f555c7041f156a7 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def one_liner_for(self, qualified_name: str) -> str`

Store.one_liner_for returns the cached one-liner documentation for a symbol by qualified name, or empty string if none exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=14cb92ac26ef36bdca6e1589176fe60877279b347a5f1da7e0b4298bb24efcbf source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def one_liners_for(self, qnames: list[str]) -> dict[str, str]`

Store method that batch-retrieves cached one-liners for multiple symbol qualified names.

- Returns dictionary mapping qualified names to their cached one-liners
- Only includes entries found in triefact_sections table; missing symbols are omitted
- Empty one-liners are normalized to empty strings in the result
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_patch fingerprint=02eaf1e0cb8c1f60de79caef696b5fc235cf444669b9bf1b8156141aa1fe96f3 body_fp=d348297b4a4355f7353ad28bc259059b17fb58b728c29281c1f36c894ab42e5a source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def add_patch( self, qname: str, note: str, reason: str, session_id: str, *, kind: str = "modify", rename_to: str | None = None, require_symbol: bool = True, ) -> int`

Store.add_patch inserts a patch record keyed by qname and returns the new patch ID.

- `kind` defaults to "modify"; accepts "modify", "delete", or "rename"
- `rename_to` specifies the new local name when `kind` is "rename"
- `require_symbol` (default `True`) validates qname exists in the graph; pass `False` for removal notes on already-deleted symbols
- Raises `KeyError` if qname is absent and `require_symbol` is `True`
- Returns the database-generated patch ID on success
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_delete_patch fingerprint=a20fe579a52fe50e5cb946c96461ef74dcbca5bc0ba560a4877bab37796c5b98 body_fp=67aaaad9235d49c870c4c306176fbd34cef79bb1b9b5a1acce2e190dc243c519 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def add_delete_patch(self, qname: str, reason: str, session_id: str) -> int`

Stages a deletion patch for an existing symbol by qname, raising KeyError if the symbol doesn't exist.

- Delegates to `add_patch` with empty note and kind="delete"
- Returns the new patch ID on success
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_rename_patch fingerprint=5ec878db09687bb2af48f86ca34e8f19c5a90c248c1d6d9a47627f874624f506 body_fp=7e35f55c94ba6020c4201026f461b9d37d95a108d02991766f2103fb8e414086 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def add_rename_patch(self, qname: str, new_name: str, reason: str, session_id: str) -> int`

Stages a rename patch for an existing symbol to the specified local name.

- `new_name`: the new local name (not qualified name) for the symbol
- Returns the new patch ID
- Raises KeyError if the symbol doesn't exist
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_create_patch fingerprint=5f404888744632f95f296e341da34e919e8a80a325315c80327e8c38e5f521a4 body_fp=d1c19b910405391d6d79494af8c2c705c9d8cc8f4d4f4899c4dce6251db713fb source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def add_create_patch( self, *, target_file: str, target_qname: str, note: str, reason: str, session_id: str, anchor_qname: str | None = None, parent_class: str | None = None, ) -> int`

Store method inserts a create_patch record for a new symbol that doesn't exist yet.

- Returns the database row id of the inserted patch record
- `anchor_qname` specifies location context for symbol placement
- `parent_class` indicates class membership for new methods
- Does not validate target_qname absence (caller responsibility)
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_create_patches_grouped fingerprint=5321a1bf1fbffeeaf55a77192770692b8f0bd4d85a847e24330868f3b3f2a4d9 body_fp=89ce70ef2d7b8a3c8aeea4a6a19f2081d07f46f656ba310cc77def14650428e6 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def get_create_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]`

Return `Store` create patches grouped by target_file, optionally filtered by seal state.

- `applied`: `True`/`False` filters to sealed/unsealed rows; `None` returns all
- Each patch dict includes `applied` (bool) and `session_note` (str) fields in addition to core create-patch columns
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_create_patches fingerprint=f5ee8cd63465f9f99615fd905f904caac138ba603909cdeed45f6c2d6742e977 body_fp=f95f0d34d68bfe35361124b637eb56135ddeb538ec888defdb6015cb2ccfeb1d source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def delete_create_patches( self, *, target_qname: str | None = None, session_id: str | None = None, all: bool = False, ) -> int`

Delete create patches by target_qname, session_id, or all patches, returning count of deleted rows.

- `target_qname`: delete patches creating this qualified name
- `session_id`: delete patches from this agent session  
- `all`: delete all create patches (overrides other filters)
- Returns 0 if no matching criteria specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._patch_row_to_dict fingerprint=13cf875676503735a3d9b60de815590f1061b036dfda8810b1581f7e25612b78 body_fp=c63939f0dc9af29c718c2a4151cf6cce153b18d9b9ad200a7b091c0bffca0e07 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=util -->
## `def _patch_row_to_dict(r) -> dict`

Convert a raw `patches` DB row tuple into the canonical patch dict used by `Store` query methods.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patches_for_qname fingerprint=ed02f1cb7614c48b7c57bc9009149334a09d5cac1484e3c5a16245418bcdaedb body_fp=1a2ac7ca52295d8cff05a71eb467b2ed579a686e0149e280171ca0604a14fad8 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def get_patches_for_qname(self, qname: str, *, applied: bool | None = None) -> list[dict]`

Return patches for one qname as dicts, optionally filtered by seal state via `applied`.

- `applied`: `True` = sealed only, `False` = pending only, `None` = all rows
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_all_patches_grouped fingerprint=c9470f3993903df761f557c439a95f27c77bbb3f60fa126443b17e1b0fe64f7a body_fp=969cb9f08966eb555217664cf3b31cd1341f4f262e9a68055ba783700b8a9833 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def get_all_patches_grouped(self, *, applied: bool | None = None) -> dict[str, list[dict]]`

Return all patches grouped by `qname`; `applied` filters to sealed or unsealed rows only (None = all).

- Returns `dict[str, list[dict]]` keyed by qname (was symbol_id in previous version)
- Each patch dict includes `applied` and `session_note` fields in addition to previous fields
- `applied=True` returns only sealed rows; `applied=False` only pending rows
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.mark_patches_applied fingerprint=9ca7fdb0b6144ac0c487bf8d5b5be56b7f9150e1191720bcdfe852288a7c09c1 body_fp=87e6f5059078f43f4d482a487cf53db7ef7b5c9b9cc902c909961fe12542e1e9 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def mark_patches_applied(self, session_note: str) -> int`

Stamp every unapplied row in `patches` and `create_patches` with `session_note` and `applied = 1`, then return the total count of sealed rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_applied_patches fingerprint=c67f14662f9b48c82b4dd6043baec1d01536466c1ea2daf5f8d2427dd9419f27 body_fp=9e19d543491878405594ebdc353eb10bac4c90ba506eb9b5aaa7562b3d089b0a source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def delete_applied_patches(self) -> int`

Delete all applied `patches` and `create_patches` rows, returning the total count of deleted rows.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_patches fingerprint=a059c49514e3e3e6326509ce064d54534ef91fdcb02041ae9ccbe0ee4eaef2ef body_fp=3fc1f65e82329b889e2250f2d842e3f01c1a0e6f8fc68b9e1faa1c8b46b66084 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def delete_patches( self, *, qname: str | None = None, session_id: str | None = None, all: bool = False, ) -> int`

Store method that deletes patches matching specified criteria and returns count of deleted rows.

- `qname`: Delete all patches directly by `qname` column (no longer validates symbol existence)
- `session_id`: Delete all patches created in a specific session
- `all`: Delete all patches in the database
- At least one parameter must be specified
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patched_qnames fingerprint=caa0e417b575e83267895367b57e795e5928e9344044d6607f471915c22b6ca1 body_fp=7a0acbe62c6aabf5f53a0a564a06570151fcedf60d7a231215783a3ad8833b01 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def get_patched_qnames(self, *, applied: bool | None = None) -> list[str]`

Return distinct qnames from `patches`; `applied` filters by seal state (None returns all rows, True/False restricts to sealed/unsealed).
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_summary fingerprint=ee1164a6a6761ae48bfe4436a38be3f34d6fb9ef25040ce8a8d7ae23f876f921 body_fp=d9cfd1cf655e66522453c56d3d82a86b71919cc2b247857256b717fea555ad28 source_ref=d3fae78bb74f28009aa7e2af9642e5cb5b1e1779 role=persistence -->
## `def patch_summary(self) -> dict[str, object]`

Store.patch_summary aggregates pending-patch state into counts and classifications by session origin.

- `total_patches`: total number of patch rows across all symbols
- `symbol_count`: number of distinct symbols with pending patches
- `create_count`: number of create_patches (new symbols to be created)
- `by_origin`: symbols bucketed by patch session type (agent/cascade/mixed)
- `qnames`: sorted list of qualified names having pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=4810eb0c5b83545ed08d9625075a3a9b7715fcbe1c52ef4d28c2d2c79dbc394b body_fp=5e546bfaeaee80f47e77feb1d2084b49d108f060c2f238ec96a66e581a348e4e source_ref=6b17f7c7cdeef9470455fb704935cf18a7bdd3d0 role=persistence -->
## `def get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None`

Store.get_symbol_detail retrieves complete symbol metadata and graph metrics for an agent query in one roundtrip.

- Returns None if qualified_name is not found
- Includes inbound/outbound edge counts, cached one-liner, role/boundary tags, decorators, fingerprint, and pending patches
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.grep_symbols fingerprint=ace8af747c7eb029b2268d33c835964089f14085c7b416ed8016d3108366a8bb body_fp=13c88b1d5224b5b13636cbf2feed2d6a0299547500aa047a11a6a18ab77c569f source_ref=c1b107d3bdcc6c0717d71bfa4abea1d9a4020944 role=persistence -->
## `def grep_symbols( self, predicate: GrepPredicate, *, rank_by: str = "public_first", limit: int = 10, ) -> list[SymbolDetail]`

Store.grep_symbols searches symbols using predicate filters, returning SymbolDetail objects sorted by rank_by.

- `rank_by`: "public_first", "inbound_count", or "alphabetical" (defaults to "public_first"); test-path symbols are demoted within every bucket except "alphabetical"
- Edge count filters use scalar subqueries repeated in WHERE clause due to SQLite resolution order
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=aa6fcb83b97f96606831442f313822f1c8204fa7f1012f360a04e70c554f5143 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
## `def all_symbol_names(self) -> list[str]`

Returns all distinct local symbol names from the symbols table for fuzzy-match suggestions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=5e99a9ebeaecdac99c8a9227035d404d13a813a5da24427a2357a3665b5b3b14 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=util -->
## `def all_qualified_names(self) -> list[str]`

Returns all qualified names from the symbols table as a list of strings.

- Used by suggest systems for near-miss matching when explain/walk operations fail to find symbols
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.survey_symbols fingerprint=f68870a5028109f1a34ab0b012829014f156b48313c712e0bc9d0b20d440bcc9 body_fp=7a199f546398cf124df59e46098b5128d7e34e0d456cdf564fc001b482300905 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=persistence -->
## `def survey_symbols(self, *, public_only: bool = False) -> list[tuple[str, str, str, str]]`

Store.survey_symbols returns tuples of (qualified_name, kind, one_liner, file_path) for all symbols, optionally filtered to public ones.

- `public_only`: when True, filters to symbols where is_public=1
- Returns empty string for one_liner when no triefact section exists
- Results ordered by file_path then start_line
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.find_paths fingerprint=1e0bfe75b333b57d1f17f2fd413879fcc9f8615e5c9313a5804159d4e9eaa1b9 body_fp=9d16db27f737835d6e8bfc2650b360594c5b7adcc7a98c1cf08e0e4958dec948 source_ref=c7ae3282b7daa8851d972e12a49a88b5b44a3638 role=domain -->
## `def find_paths( self, from_qname: str, to_qname: str, *, max_depth: int = 6, hub_threshold: int = 20, max_paths: int = 3, ) -> list[list[str]]`

Store.find_paths performs breadth-first search to find shortest call paths between two symbols.

- Returns list of qualified name sequences from `from_qname` to `to_qname` following callee edges
- Limits search by `max_depth` hops, `max_paths` results, skips cycles and high-fanin hubs
- Empty return when no path exists within constraints
- For reverse direction (caller chains), swap the arguments
<!-- trie:end -->