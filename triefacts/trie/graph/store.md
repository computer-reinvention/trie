---
trie_version: 0.1.5
source: trie/graph/store.py
file_fingerprint: e9928d85d19f8b7002da3561fa1402fedf5fb7722efd9f0a425d3dd16af25f91
last_synced_at: '2026-05-28T01:38:54Z'
defines:
- kind: module
  qualified_name: trie/graph/store:__module__
  lines: 1-911
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_VERSION
  lines: 13-13
- kind: constant
  qualified_name: trie/graph/store:SCHEMA_SQL
  lines: 17-73
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 77-80
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 84-87
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 91-98
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 102-121
- kind: class
  qualified_name: trie/graph/store:GrepPredicate
  lines: 125-144
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 147-910
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 156-159
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 161-182
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 184-185
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 187-188
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 190-191
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 194-200
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 204-209
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 211-222
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 224-226
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 228-234
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 238-265
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 267-278
- kind: method
  qualified_name: trie/graph/store:Store.count_section_records
  lines: 280-282
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 286-317
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 319-331
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 333-345
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 347-353
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 355-374
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 376-403
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 405-417
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 419-420
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 422-431
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 433-463
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 465-487
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 491-526
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 528-541
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 543-556
- kind: method
  qualified_name: trie/graph/store:Store.add_patch
  lines: 560-586
- kind: method
  qualified_name: trie/graph/store:Store.get_patches_for_qname
  lines: 588-597
- kind: method
  qualified_name: trie/graph/store:Store._get_patches_by_symbol_id
  lines: 599-613
- kind: method
  qualified_name: trie/graph/store:Store.get_all_patches_grouped
  lines: 615-636
- kind: method
  qualified_name: trie/graph/store:Store.delete_patches
  lines: 638-672
- kind: method
  qualified_name: trie/graph/store:Store.get_patched_qnames
  lines: 674-682
- kind: method
  qualified_name: trie/graph/store:Store.patch_count_for_symbol
  lines: 684-690
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 694-730
- kind: method
  qualified_name: trie/graph/store:Store.grep_symbols
  lines: 732-824
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 826-829
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 831-834
- kind: method
  qualified_name: trie/graph/store:Store.find_paths
  lines: 836-910
incoming_refs: 71
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=df19a7d92687c892c51d630679ee2dabd6fccb2ff46be566c0076aac8e7c9ed8 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `store`

SQLite-backed store for trie's symbol graph, file fingerprints, and triefact section metadata.

- `SCHEMA_VERSION`: bump to wipe and rebuild the regenerable `.trie/` cache
- `SCHEMA_SQL`: defines `files`, `symbols`, `edges`, and `triefact_sections` tables
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_VERSION fingerprint=53a1f6485212aab77917eb5d6c4bd1c49c78794b5e6b1a814925e6eeb2361140 body_fp=66f58615363476c6a59c8d9c9ffb0dcf24eb4611aff22d2dc2049338aa8b8cad source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `SCHEMA_VERSION = 3`

Integer sentinel compared against `schema_version` table on open; mismatch drops and rebuilds the DB.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SCHEMA_SQL fingerprint=7c0bc4f3e7ac8b93f808885b9703a21c211e05eacc35ab3e06838200fb916367 body_fp=fa4b9906115015a579ab71b1666344be0c975db82b8b9de1a9bf2bca8a5764d0 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `SCHEMA_SQL`

SQLite DDL string that creates all six core tables and their indexes on first connect.

- `schema_version`: holds `SCHEMA_VERSION`; mismatch triggers DB wipe and rebuild.
- `files`: per-file fingerprint and scan timestamp; primary key is path.
- `symbols`: one row per parsed symbol; cascades deletes to `edges` and `triefact_sections`.
- `edges`: directed symbol-reference pairs; both FKs cascade on symbol delete.
- `triefact_sections`: cached generated-section metadata keyed by `(triefact_path, symbol_id)`.
- `patches`: agent-authored notes per symbol, indexed by `symbol_id` and `session_id`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=e71b6c2fadb3adafc914d3af550c9545f7ffebbfa485fe78febaf64e5f8a842b source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `FileRecord(path: str, fingerprint: str, last_scanned_at: int)`

Immutable record representing a scanned file row from the `files` table.

- `last_scanned_at`: Unix timestamp of the most recent scan.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=fa8faddb4a150158d41c557e962ca1d41912a9b7eeb85f7ed8ea68cd964ae21f source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `FileStats(path: str, total_symbols: int, public_symbols: int)`

Immutable per-file symbol count record returned by `Store.file_stats`.

- `public_symbols`: always equals `total_symbols`; preserved for API stability.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=d4c7d50d7e0ae3ae0433d42c253e9f05306cf1495118b76af64d640e8b6b3319 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `SymbolHit`

Immutable summary record returned by `Store.search_symbols`.

- `kind`: one of `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=e191e9b707c0ed386c0abdeed7cc8e4db62c4df947fcfb4e3bce992e0a811af7 body_fp=32686bf70764ecb05d5665071b9f438f80b91adb7788fecc34a31d84313cc5b8 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `SymbolDetail`

Frozen dataclass carrying full symbol metadata, edge counts, cached one-liner, and pending patch info for a single DB roundtrip.

- `one_liner`: empty string when no triefact section has been generated yet.
- `pending_patches`: list of patch dicts; defaults to empty list.
- `pending_patch_count`: number of pending patches; defaults to `0`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:GrepPredicate fingerprint=bb94fc53eb9ffe605f051d331b0b74099549200f353c204750e987092d9ac0e6 body_fp=f17b231b67864c154d77ecb6f0e90438bbd11b6ef083a1677e89aa4012e4efcd source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `GrepPredicate`

Server-side filter passed to `Store.grep_symbols`; all fields optional, omitted means no filter on that dimension.

- `kind`: one of `"function"`, `"class"`, `"method"`, `"constant"`, `"module"`, `"any"`, or `None`
- `scope_prefix`: matched as a prefix against `file_path`
- `scope_exclude`: each entry matched as a prefix against `file_path`; matching files excluded
- `inbound_count_min` / `inbound_count_max`: inclusive bounds on inbound edge count
- `outbound_count_min` / `outbound_count_max`: inclusive bounds on outbound edge count
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store fingerprint=54d8c229c6f2c126bc9491c3ec69919d02b081bbd3c11c2080a7f0021ad9776c body_fp=a313830ec51d254f13712d2182fde07242b7681aba00bcc90eadd4b3039d3b7f source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `class Store`

SQLite-backed persistence for trie's symbol graph, file fingerprints, and triefact section metadata.

- `db_path`: path to the SQLite file; parent directories are created on init.
- On open, stale schema versions cause the DB file to be deleted and rebuilt from scratch.
- Use as a context manager; `close()` is called on exit.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__init__ fingerprint=cbc4e30ba48edc9d8f65e1c5cbfcf9b29a9e2a9889581d7100fd1678981276b9 body_fp=ea90579aed35396efc8cf5031bddc512c7607e37fa2669ae0c861b812d99a580 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.__init__(self, db_path: Path) -> None`

Initialize the `Store`, creating parent directories and opening the SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._open fingerprint=1840acd2bf92663690f9ecd8c1a418eb53e4525df3070283393ae5fb73deed99 body_fp=068068d579edcf366278d09f5f7322f7da3784d22d9ffcae1c9e4128d6d59d4a source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store._open(self) -> None`

Open the SQLite connection, drop and recreate the database if the schema version is stale, then apply `SCHEMA_SQL`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=e1f769608951af7a4dad2163ae0ef5f716b724ab720222f4dc365bd6912895ad source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.close() -> None`

Close the `Store`'s SQLite connection.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=ad6b960971a2e22529189c34122dcc09f473f0fe3e6a8e6c899b428d804bc4a8 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.__enter__(self) -> Store`

Return the `Store` instance to support context-manager usage.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.__exit__ fingerprint=67b1b6b146522ac7c8bdfff45bab8a41537d8e61231b937b0475a712971729e7 body_fp=ad75b8ca65bfd6543cd22fd738d7c67488fb6a80d79f2fda066ab2dd68b3c280 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.__exit__(self, *_args: object) -> None`

Close the `Store` connection when exiting a context manager block.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=b19d855b1fd936c49408025922131e2969e73ba02010545f7d4b5968cb912ba8 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.transaction(self) -> Iterator[sqlite3.Connection]`

Yield the `Store` connection inside a transaction, committing on success or rolling back and re-raising on exception.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=894e48a3d96c7e60c1f66bf923ed7f897f5400273e722c0bd19724ee2f171a6f source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.get_file(self, path: str) -> FileRecord | None`

Look up a `Store` file record by exact path, returning `None` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=3c5da72d96097a01efb91a457866463ecaf2d15fa996272e130951d78b449300 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.upsert_file(*, path: str, fingerprint: str, now: int | None = None) -> None`

Insert or update a file record in the `Store`, committing immediately.

- `now`: Unix timestamp override; defaults to `int(time.time())`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=123de327c8e9aca2bbbc017166bdacfc95d94c450d20b930502f37a012006f89 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.delete_file(self, path: str) -> None`

Delete the `Store` file record for `path` and commit.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=f7c850dc3be51253d27b7ae5837b24ca4ecc23d98a80c087293d2eba89bcb437 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.list_files(self) -> list[FileRecord]`

Return all `FileRecord` rows from the `Store`, ordered by path.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=d8e44858ebcda72ec803e6d2d297bdbbd2658509fa3f8bcbbd924b106093881c body_fp=c738098792fd79c19ec4d895233ad54c941b4231bb38b41e4db52c73c277417b source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None`

Atomically delete and re-insert all `Store` symbol rows for a given file within a single transaction.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=5bdcb91085775b5207b64a51a91c2c83e596812e0686d991a61d8a8726a69737 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int`

Count symbols in the `Store`, optionally filtered by file and/or public visibility.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_section_records fingerprint=610f302acb473963e5a29105d08a8808237b8ffa314427ab6ac1f9a61e853fbe body_fp=1b696049be3e84725312e02eb988da952141a8b00aadf44bf099198632700629 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.count_section_records(self) -> int`

Return the total row count of the `triefact_sections` table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=f723b23ba6b913c951a282870d919431f131b8e31d304ccf18880dc9d37bfe93 body_fp=80660e7ebb923ac8dec041dc51b573d7a5208a4c496d0098bf314c5f893b6aac source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int`

Atomically wipe and rebuild the `edges` table from a per-file reference map, returning the number of edges inserted.

- `references_by_file`: keyed by file path; values are resolved `Reference` objects.
- Self-edges and references to unknown qualified names are silently dropped.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=bbfde003b1262c59cbe1d7e76a6bdddd076eb16bfd79a0872d513d023f73c769 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.references_in(self, qualified_name: str) -> list[str]`

Return all `qualified_name` strings of symbols that have an outbound edge targeting `qualified_name`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=e026973bef338cdbe99b84392bf19cc71c05bb611e98fc53ffa10900ad244ad7 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]`

Return `(src_qname, src_file_path)` pairs for every symbol that references `qualified_name`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=f0ca6cacd84a525727f675939e7854189d58b48363471391f82392e3071f22e3 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.qnames_in_file(self, file_path: str) -> list[str]`

Return all qualified names of symbols defined in `file_path`, ordered by start line.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.symbols_in_file_with_lines fingerprint=6c50f1692f561e61d68233e23f1452068b7dc5151923fcf1a75c9e9f32d8fc97 body_fp=bd29d791132a2af9e209260c6ff131ac20830415a2adcb5b24f1204df43dde21 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.symbols_in_file_with_lines(self, file_path: str) -> list[tuple[str, int, int]]`

Return `(qname, start_line, end_line)` for every symbol in `file_path`, ordered by start line.

- Returns `[]` when the file is unknown or has no recorded symbols.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=ded6ac8d363a81a923f20a15399a110f948ef04cb68409140b7617475cde8147 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]`

Case-insensitively search `Store` symbols by local name, returning up to `limit` `SymbolHit` results ordered public-first.

- `name_pattern`: substring matched against `name` (local part), not `qualified_name`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=8f9c049d224d32b9701b2ea10f2963101e050868e5445fd589489097b63891a7 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.references_out(self, qualified_name: str) -> list[str]`

Return all qualified names that `qualified_name` references (outbound edges).
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=58c891ad677790e75b31d8f73f31133c08bd5ce46da4c87d4d6b7ce739688cfb source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.count_edges(self) -> int`

Return the total number of rows in the `Store` edges table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=fa634196f55fd2ff22b86db6cb4831087b7b2532a7246ed2601780b1946db685 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.inbound_count_per_symbol(self) -> dict[str, int]`

Return a mapping of every symbol's qualified name to its inbound edge count.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=c91d16db66c8427e33861dc7b12859ce10573b7accd08ebfe18b42eaff7c8c62 body_fp=4a1597f8d924ae36429b2877c245d46d62aa766ef1d5a12233c3d50a359c30ef source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.file_ref_counts(self, file_path: str) -> tuple[int, int]`

Return cross-file `(inbound, outbound)` edge counts for a `Store` file path, excluding intra-file edges.

- **inbound**: edges from symbols in *other* files targeting symbols in `file_path`
- **outbound**: edges from symbols in `file_path` targeting symbols in *other* files
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=818ee47e02de6186ac43c3deb53c5ddc50df1980e52047b405fca30d50d264d6 body_fp=58b8371ba9fdb059f6807f953f8867193a7a574c264d801039492490229ac87c source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.file_stats(self) -> list[FileStats]`

Return per-file symbol counts for all tracked files, used by the bootstrap ranker.

- `public_symbols`: legacy field; always equals `total_symbols` — all scanned symbols are counted.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=c0ed5ba8a45dd21c6a60068fbc428a85bfe91bc62951744e0c93ca03042bdd96 body_fp=32a9910cde83940afc4039c26d245c3fe8895e29a47ee514701e0fda0955aad1 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.upsert_section_record(*, triefact_path, symbol_qname, section_fingerprint, one_liner, now=None) -> None`

Insert or update a `triefact_sections` row linking a generated section to its symbol; silently no-ops if the symbol no longer exists.

- `now`: Unix timestamp override; defaults to `int(time.time())`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=4069322568cd9e9c0b2f6077838330e6471ef0ca1a8ac6fe5f35484c16767c5a source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.one_liner_for(self, qualified_name: str) -> str`

Return the cached one-liner string for a symbol, or `''` if no triefact section exists.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=1376b17f9bf2bb106e42c8a78ae5cd1e072f6a10afac2d5248ed4b6e67dfef1d source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.one_liners_for(self, qnames: list[str]) -> dict[str, str]`

Batch-fetch cached one-liners from `Store` for multiple qualified names in one query.

- Returns only entries that exist; missing qnames are absent from the result dict.
- Empty string substituted for `NULL` one-liner values.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.add_patch fingerprint=7138f7d0247ef1f8126177ab0ec274e3b5204fe0c5425cd7ceb49ae37ec3a547 body_fp=e2729a75f8860a4b8979e952d549edce793c2e340a50cce47b30b14062e53cae source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.add_patch(self, qname: str, note: str, reason: str, session_id: str) -> int`

Insert a patch row for a symbol into the `Store`, returning the new patch id.

- `qname`: qualified name of the target symbol; raises `KeyError` if not found.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patches_for_qname fingerprint=99cf3d176ccf53de862a8deb7087fe8c39df8552d648c1cafb1bd48c038fa021 body_fp=55361e7062732103a6aca74e50f00f1dbfdbc9799f8c87f319f673cfe277d704 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.get_patches_for_qname(self, qname: str) -> list[dict]`

Return all pending patches for a symbol as a list of dicts, or `[]` if the symbol doesn't exist.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store._get_patches_by_symbol_id fingerprint=7237e3712892b20f9f97dda9893b1001944188b4c8a9517a3049eece76651481 body_fp=c6fcd02a1815982aef0857aa790cb4f783aa72ebcd949feb14b137f7d0638b76 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store._get_patches_by_symbol_id(self, symbol_id: int) -> list[dict]`

Fetch all patch rows for a given `symbol_id`, returning them as a list of dicts.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_all_patches_grouped fingerprint=82c6d9f5fc59b0b4c235714ed11733ead3f39828ab8e1c58b6b44a04469f5419 body_fp=c4ef7344794b6873987a5a7eb28d21cbb2180c5a0208481dc00793bacdd46a25 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.get_all_patches_grouped(self) -> dict[int, list[dict]]`

Return all `patches` rows from the `Store`, grouped by `symbol_id`.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.delete_patches fingerprint=c1457117713979a51e97ee435994b5d9819075c1f5bce24aaa7f31c328e1f99d body_fp=72f7e6e4d412c7002fb9a21d1d725a811a11e50d12407878a14d80fa3de036e1 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.delete_patches(self, *, qname: str | None = None, session_id: str | None = None, all: bool = False) -> int`

Delete patches from the `Store` matching the given criteria; returns the number of deleted rows.

- `all`: deletes every patch row when `True`, ignoring other filters.
- `qname`: deletes patches for the symbol with that qualified name; returns 0 if symbol not found.
- `session_id`: deletes all patches belonging to that session.
- Returns 0 if none of the three criteria are set.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_patched_qnames fingerprint=0e2e2afe6da23a44267b7db00a8fdca0a377fddfffb84b1d624128b0a1eb5136 body_fp=1a637ea8b118249f5cbfb64ae9a6c68e47cbc11b024ff67d052635c9724477e4 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.get_patched_qnames(self) -> list[str]`

Return all distinct qualified names in `Store` that have at least one pending patch, sorted alphabetically.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.patch_count_for_symbol fingerprint=0b9529da6e2ea49324486ddca6f3b682563b67ac8c3504c0249c1bebbb9dc8bd body_fp=a83eda62f0f441a38543f46ba07518dadc0e77e595b928f7ea29fccd66cb95f1 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.patch_count_for_symbol(self, symbol_id: int) -> int`

Return the number of pending patches for a given `Store` symbol by its integer primary key.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=e8ada704c34f269ef2b2059c6ed4f3a3ef9100e4add2b09fb2f40f67c1fd03f4 body_fp=3fd9e84fa873ad09468a8aef6a75bde86a7122d1d5686f10cb44b214b14ab46d source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None`

Fetch a fully-populated `SymbolDetail` for one symbol by qualified name, including edge counts, cached one-liner, and pending patches, in one query plus a patch lookup.

- `qualified_name`: exact match against `symbols.qualified_name`; returns `None` if not found.
- `pending_patches` / `pending_patch_count`: populated via a second `get_patches_for_qname` call.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.grep_symbols fingerprint=994b988c155b6f510d95253fd9cba6c0e9c0255289cc193b8b91fe3f12a385b4 body_fp=1231dce44d114c226fc535326e199aa705635b96235a1cb6e6ced26966cf8d70 source_ref=e9980a62504c58b5fea56d67ef9c83f4fc24aeb7 -->
## `Store.grep_symbols(self, predicate: GrepPredicate, *, rank_by: str = "public_first", limit: int = 10) -> list[SymbolDetail]`

Query `Store` symbols using a `GrepPredicate` filter, returning up to `limit` `SymbolDetail` results.

- `rank_by`: `"public_first"` (default), `"inbound_count"`, or `"alphabetical"`; unknown values fall back to `"public_first"`.
- `predicate`: all fields are optional; omitted fields apply no filter.
- Each returned `SymbolDetail` includes `pending_patch_count` populated from the `patches` table.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=a56ee588e9fdbe5fd8db0427f4d381769fcfad357bab3ad4870339ae2467b0d0 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.all_symbol_names(self) -> list[str]`

Return all distinct local symbol names from the `Store` for fuzzy-match suggestions.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=4ad80f02e28f3e5ef689ce1d06079e187ce0a85f82e67fecd371741129943251 source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.all_qualified_names(self) -> list[str]`

Return all qualified symbol names from the `Store`, used to suggest near-misses on not-found lookups.
<!-- trie:end -->
<!-- trie:section symbol=trie/graph/store:Store.find_paths fingerprint=1e0bfe75b333b57d1f17f2fd413879fcc9f8615e5c9313a5804159d4e9eaa1b9 body_fp=2f0541623432520b03898991297d54f2db1c61310b75132810fec1a06acfa7cb source_ref=13638c0451f438414c1a7dfd4d65e87c53be5767 -->
## `Store.find_paths(self, from_qname: str, to_qname: str, *, max_depth: int = 6, hub_threshold: int = 20, max_paths: int = 3) -> list[list[str]]`

BFS over callee edges in the `Store` graph, returning up to `max_paths` shortest qname-sequences from `from_qname` to `to_qname`.

- `hub_threshold`: symbols with inbound count above this are skipped during expansion.
- `max_depth`: paths exceeding this hop count are abandoned.
- Returns `[]` when no path exists within bounds; `[[from_qname]]` when source equals destination.
<!-- trie:end -->