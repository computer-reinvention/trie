---
trie_version: 0.1.0
source: trie/graph/store.py
file_fingerprint: 0a77633f9dcc887429cb9d41abcfc69a3ff0a8cd0c44f4c5d9ffda98747c390f
last_synced_at: '2026-05-16T12:51:05Z'
defines:
- kind: class
  qualified_name: trie/graph/store:FileRecord
  lines: 66-69
- kind: class
  qualified_name: trie/graph/store:FileStats
  lines: 73-76
- kind: class
  qualified_name: trie/graph/store:SymbolHit
  lines: 80-87
- kind: class
  qualified_name: trie/graph/store:SymbolDetail
  lines: 91-108
- kind: class
  qualified_name: trie/graph/store:LocatePredicate
  lines: 112-129
- kind: class
  qualified_name: trie/graph/store:Store
  lines: 132-675
- kind: method
  qualified_name: trie/graph/store:Store.__init__
  lines: 141-144
- kind: method
  qualified_name: trie/graph/store:Store._open
  lines: 146-167
- kind: method
  qualified_name: trie/graph/store:Store.close
  lines: 169-170
- kind: method
  qualified_name: trie/graph/store:Store.__enter__
  lines: 172-173
- kind: method
  qualified_name: trie/graph/store:Store.__exit__
  lines: 175-176
- kind: method
  qualified_name: trie/graph/store:Store.transaction
  lines: 179-185
- kind: method
  qualified_name: trie/graph/store:Store.get_file
  lines: 189-194
- kind: method
  qualified_name: trie/graph/store:Store.upsert_file
  lines: 196-207
- kind: method
  qualified_name: trie/graph/store:Store.delete_file
  lines: 209-211
- kind: method
  qualified_name: trie/graph/store:Store.list_files
  lines: 213-219
- kind: method
  qualified_name: trie/graph/store:Store.replace_file_symbols
  lines: 223-250
- kind: method
  qualified_name: trie/graph/store:Store.count_symbols
  lines: 252-263
- kind: method
  qualified_name: trie/graph/store:Store.replace_all_edges
  lines: 267-298
- kind: method
  qualified_name: trie/graph/store:Store.references_in
  lines: 300-312
- kind: method
  qualified_name: trie/graph/store:Store.references_in_with_files
  lines: 314-326
- kind: method
  qualified_name: trie/graph/store:Store.qnames_in_file
  lines: 328-334
- kind: method
  qualified_name: trie/graph/store:Store.symbols_in_file_with_lines
  lines: 336-355
- kind: method
  qualified_name: trie/graph/store:Store.search_symbols
  lines: 357-384
- kind: method
  qualified_name: trie/graph/store:Store.references_out
  lines: 386-398
- kind: method
  qualified_name: trie/graph/store:Store.count_edges
  lines: 400-401
- kind: method
  qualified_name: trie/graph/store:Store.inbound_count_per_symbol
  lines: 403-412
- kind: method
  qualified_name: trie/graph/store:Store.file_ref_counts
  lines: 414-444
- kind: method
  qualified_name: trie/graph/store:Store.file_stats
  lines: 446-468
- kind: method
  qualified_name: trie/graph/store:Store.upsert_section_record
  lines: 472-507
- kind: method
  qualified_name: trie/graph/store:Store.one_liner_for
  lines: 509-522
- kind: method
  qualified_name: trie/graph/store:Store.one_liners_for
  lines: 524-537
- kind: method
  qualified_name: trie/graph/store:Store.get_symbol_detail
  lines: 541-574
- kind: method
  qualified_name: trie/graph/store:Store.locate_symbols
  lines: 576-665
- kind: method
  qualified_name: trie/graph/store:Store.all_symbol_names
  lines: 667-670
- kind: method
  qualified_name: trie/graph/store:Store.all_qualified_names
  lines: 672-675
incoming_refs: 41
outgoing_refs: 2
---
<!-- trie:section symbol=trie/graph/store:FileRecord fingerprint=9e5bd64fbbf95f8eb3616b9da3d84b73687a569550e6ace513eef354bd16b1e1 body_fp=66d0f20070cb4ff0fbcc153cfb392d3aa24addf48f3b73c0f1c45f48d6b74475 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `FileRecord(path: str, fingerprint: str, last_scanned_at: int)`

Frozen dataclass representing a row from the `files` table.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:FileStats fingerprint=c724d544428a38f276d944f8e7e7b5ad7459d6b1a250e18b87c7d3031e7a4b40 body_fp=02d0787e8a2a78a87a9af72ee772781705289502a12848e4394599db77e11e46 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `FileStats`

Immutable per-file symbol count record returned by `Store.file_stats`.

- `total_symbols`: count of all symbols regardless of visibility
- `public_symbols`: count of `is_public = 1` symbols only
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:SymbolHit fingerprint=c97f130190c9d3e96d5d1b0be1314de0ae372cc1d5256f00b330cad27aac1b3e body_fp=9d60094abe38a42c1cacc9b0f987f8c61742937ba2217bc1ab806d1ee8ff6622 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `SymbolHit`

Frozen dataclass representing a lightweight symbol search result.

- `is_public`: derived from the `is_public` integer column, stored as `bool`
- `signature`: `None` when the symbol has no signature recorded
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:SymbolDetail fingerprint=79b8fb53099949838219ec9a398c584ec95ec2bad4f37021becc742118d59a63 body_fp=7c98fa7f3740b17671ab6d4d9f8d09652b84c253f80b622fc8dffe7295ca7c0a source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `SymbolDetail`

Frozen dataclass holding full per-symbol data with graph edge counts and cached one-liner for a single DB roundtrip.

- `inbound_count`: number of edges where this symbol is the target.
- `outbound_count`: number of edges where this symbol is the source.
- `one_liner`: empty string when no triefact section exists yet.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:LocatePredicate fingerprint=6c7f06d296f6fd21237853f2fbf326f7769fb6c93f91e321ad999c43eee096ac body_fp=ac8293fcc64be7cbaa13129c4083cbcb3a46ac3e6d03e8e998473cf81e862a01 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `LocatePredicate(name_contains=None, kind=None, scope_prefix=None, scope_exclude=(), public_only=False, inbound_count_min=None, inbound_count_max=None, outbound_count_min=None, outbound_count_max=None)`

Frozen dataclass encoding all server-side filter criteria for `Store.locate_symbols`.

- `kind`: accepts `"function"`, `"class"`, `"method"`, `"any"`, or `None`
- `scope_prefix` / `scope_exclude`: matched against `file_path`; exclude is a tuple of prefixes
- `inbound_count_min/max` / `outbound_count_min/max`: edge-count bounds; either bound may be `None`
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store fingerprint=1f1cf5e0501417b1dbc4dbdc0c0a438a461f43a1d0b81c24293eb5e5269ed20f body_fp=bf65225536c6d20ff0c87335ace1798a7d668859f5af19308b7fdddfff9939f2 source_ref=6da877cab7a13b55f8c9b77428537bc9a241cac7 -->
## `Store(db_path: Path)`

SQLite-backed store for trie's symbol graph, file fingerprints, edges, and cached triefact sections.

- `db_path`: path to the SQLite file; parent directories are created automatically.
- Stale schema (version mismatch) causes the DB file to be deleted and rebuilt on open.
- Use as a context manager to ensure `close()` is called.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.close fingerprint=a913f96235959366c1550f3902f93fb0cb6321b2a3dd492c780b5af0ba6b8e7b body_fp=3c968b282b4cec11f7e100fef24fd94bd6236359ef4715ea4108e5c6db9becb1 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `close(self) -> None`

Close the underlying SQLite connection.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.transaction fingerprint=92d85419eab7f0eb88451072a4fe4fd3da121109143afd8912055c863389d51b body_fp=b3dce50e8d9e8f59538e95d3a1de8daf50b76a32ba6a3e2e8a55b952f562630b source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `transaction(self) -> Iterator[sqlite3.Connection]`

Yield the connection within a commit/rollback transaction boundary.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.get_file fingerprint=eb7697a3a025059d896bd28c96b0f208e7ee3dc597aa5702581ea24d86dcb5de body_fp=440d8a5e08b380cc81a666c3d6d63376fbafebb6dfd15292ad3fd0ada0280d3e source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `get_file(self, path: str) -> FileRecord | None`

Return the `FileRecord` for the given path, or `None` if not tracked.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.upsert_file fingerprint=6d8542fa2fb58dc7c77adab00e96758e35a7b4106aca18f02c39064c1ff2eeb6 body_fp=b0553e214a1fdb31e8e337cf2a7165dbaf820a88a38d71580b9cb0818b45bebc source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `upsert_file(self, *, path: str, fingerprint: str, now: int | None = None) -> None`

Insert or update a file record, setting `last_scanned_at` to `now` or the current epoch second.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.delete_file fingerprint=3cc0d8d1dfff6afab640378b3cec46ac06299bab51b118ae1e695914bcdb5e9d body_fp=0d9d648b074bb572d04e9df7af2d91cce08ea866422c59832fb3a37a722899b9 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `delete_file(path: str) -> None`

Delete the file record for `path` and commit immediately.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.list_files fingerprint=0ad09ddc7d8033f74e03712636d0159e4ad107c8be9c4d803563162dc7be55c5 body_fp=4294221590b393f9f894949bef5f966f14d007c80d4c03abe04c7b0e0b870f2e source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `list_files(self) -> list[FileRecord]`

Return all file records ordered by path.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_file_symbols fingerprint=d8e44858ebcda72ec803e6d2d297bdbbd2658509fa3f8bcbbd924b106093881c body_fp=60f9ae5e3e894516571d9a53ec0e82f8a6024b0a90daa632fe72666aa9d959a9 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `replace_file_symbols(self, file_path: str, symbols: list[Symbol]) -> None`

Atomically delete and re-insert all symbols for a given file within a single transaction.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_symbols fingerprint=2580fe16b3b00ec0a0343c0d528630dd899ab90e6d1a008d340e1aa6c5d92002 body_fp=1820db297a73f40e9620a01f3a3f31913c3d58f05434b0d7dd1d3873d6560606 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `count_symbols(self, *, file_path: str | None = None, public_only: bool = False) -> int`

Count symbols in the store, optionally filtered by file and/or visibility.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.replace_all_edges fingerprint=f723b23ba6b913c951a282870d919431f131b8e31d304ccf18880dc9d37bfe93 body_fp=1c78186320813d3d405646883f2329b4d0f85294a357fa99aef5c0030914c55a source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `replace_all_edges(self, references_by_file: dict[str, list[Reference]]) -> int`

Wipe the edges table, resolve references against current symbols, and insert new edges atomically.

- **`references_by_file`**: keyed by file path; values are resolved reference lists.
- Unresolvable or self-referential edges are silently dropped.
- Returns count of edges actually inserted.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in fingerprint=a64405c25c8effa2d37a933ece61b1b112c7cc2bc999fd7d05000ede0188ddc7 body_fp=2fcf4bc8111ccfa8bdf0798403e9832658e4986dc3611310b7cd9b2fad094486 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `references_in(self, qualified_name: str) -> list[str]`

Return all `qualified_name` strings of symbols that reference the given symbol via inbound edges.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_in_with_files fingerprint=773412d3d4e3f39ea3f1a7f9a058c6cf53d88e3ec7a563822446a9c4e2f271fe body_fp=3ed7a5ca9fd05056bf0ec77ff98d33edc0cbb5083598b0ea58b0445e91d31063 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `references_in_with_files(self, qualified_name: str) -> list[tuple[str, str]]`

Return `(src_qname, src_file_path)` pairs for every symbol that references `qualified_name`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.qnames_in_file fingerprint=0345839c8b81209c9f8e501ba0bbd84b97b79bcdffd157276f2c5f9433f1bf53 body_fp=03fcdaa2a35dc8cb4f625092defafc94e96e570ce5ef8179dbcb7e004a8fb5db source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `qnames_in_file(self, file_path: str) -> list[str]`

Return qualified names of all symbols defined in `file_path`, ordered by source line.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.search_symbols fingerprint=843fc4a051517ce70282ea2a98897dd8f7258793682bd113ad354a6fc4c517f6 body_fp=412151ce56e60b7a4b0d171718757f9848919045356f629e86b9d0cd708b685d source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `search_symbols(self, name_pattern: str, *, limit: int = 50) -> list[SymbolHit]`

Case-insensitive substring search on symbol local names; returns up to `limit` hits ordered by visibility then qualified name.

- `name_pattern`: matched as `%pattern%` against the `name` column, not the qualified name.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.references_out fingerprint=a6810cd7afde7caf6868995ebd2d05049eb7e7d1f292600fc55fed2112ad0138 body_fp=496acb9b03ca20394931eabf115b28ed4ad9cf6e664e7d22331137ce62138ea4 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `references_out(self, qualified_name: str) -> list[str]`

Return all qualified names of symbols that `qualified_name` references outbound.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.count_edges fingerprint=dd4f0506260e96b70c2e6c1cf90803909315a59857fe188eb5f56d47f7d9d49d body_fp=ec351bfea121c9091ce085750c5a9723db5a00731a8ce7e5df37e3cbd88e5210 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `count_edges(self) -> int`

Return the total number of edges in the `edges` table.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.inbound_count_per_symbol fingerprint=d02ef2425e589304c3c468f57c53c886dd73de83d538963d490f437f8fdb19c2 body_fp=4d2d2c3214df55e9e5123d359b376259fd47a5da5f5c1cbb1e9b91baf3f823c6 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `inbound_count_per_symbol(self) -> dict[str, int]`

Return a mapping of every symbol's `qualified_name` to its inbound edge count.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_ref_counts fingerprint=c91d16db66c8427e33861dc7b12859ce10573b7accd08ebfe18b42eaff7c8c62 body_fp=696ea34bfccf7a94140721fb92e6cd82d5eeed7453f6c25eb290d63334b36929 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `file_ref_counts(self, file_path: str) -> tuple[int, int]`

Return `(inbound, outbound)` cross-file edge counts for a given file, excluding intra-file edges.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.file_stats fingerprint=818ee47e02de6186ac43c3deb53c5ddc50df1980e52047b405fca30d50d264d6 body_fp=fe9ced4621dd1697950410e17189eb3cdb6319a7d0b5f1a3f8b8df8c2b4c11c7 source_ref=aef35014ee7ba97f7bb5ee8252255be994acfdac -->
## `file_stats(self) -> list[FileStats]`

Return per-file symbol counts joined from `files` and `symbols`, with `public_symbols` set equal to `total_symbols` for all files.

- `public_symbols`: always equals `total_symbols`; the distinct public count is no longer computed.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.upsert_section_record fingerprint=c0ed5ba8a45dd21c6a60068fbc428a85bfe91bc62951744e0c93ca03042bdd96 body_fp=7d0845a8ce7f98909060be44c5eca6cbee509a0d905ec2ff5fec6e41b31ec76c source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `upsert_section_record(self, *, triefact_path: str, symbol_qname: str, section_fingerprint: str, one_liner: str, now: int | None = None) -> None`

Insert or update a `triefact_sections` row, linking a generated section to its symbol.

- `symbol_qname`: silently skipped if not found in `symbols` (deleted/renamed symbol).
- `now`: Unix timestamp; defaults to `int(time.time())`.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.one_liner_for fingerprint=1f204b6ac59d246ef09d1541e51816e9a3261e8bcd10c625cb2b426a5c5dbaaa body_fp=2ca37524618426a38984ee105e1b5a187135a40a5ce1fe97460ef7be1c075c2e source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `one_liner_for(self, qualified_name: str) -> str`

Return the cached one-liner for a symbol, or `''` if no triefact section exists.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.one_liners_for fingerprint=41fe88c62a162851d437d2e65cd15c753d88bdc5f4d13d59609b2ab4f92550b4 body_fp=8e58990e7081bd658af84a31146df2a49f8fb2b9663d5f2786de3d399519fd22 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `one_liners_for(self, qnames: list[str]) -> dict[str, str]`

Batch-fetch cached one-liners for multiple qualified names.

- Returns only entries found in the DB; missing qnames are absent from the result.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.get_symbol_detail fingerprint=035c308d0bc43eb38d36a7245a821ffa036ba178cbd25c058ef045f1d485d90d body_fp=3da726177373e4410ad842775e59c85e71ca036a3f6cb72e3ce68be5145985fc source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `get_symbol_detail(self, qualified_name: str) -> SymbolDetail | None`

Return full `SymbolDetail` for one symbol including inbound/outbound edge counts and cached one-liner, or `None` if not found.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.locate_symbols fingerprint=83b17a895d0060e7833abe22296476ad93ea93e488e0fd8bccb18773bec91068 body_fp=82798bb9fad2b4bee6d56b9f7513893039e6d55a1f74e36800560e588fe6e22d source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `locate_symbols(self, predicate: LocatePredicate, *, rank_by: str = "public_first", limit: int = 10) -> list[SymbolDetail]`

Execute a predicate-driven symbol search and return ranked `SymbolDetail` results.

- `rank_by`: accepts `"public_first"`, `"inbound_count"`, or `"alphabetical"`; unknown values fall back to `"public_first"`.
- `limit`: maximum number of results returned.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.all_symbol_names fingerprint=fd7275a10e4d910bbe493d3316de5e7e152c08eabc201043b81db9d247002f65 body_fp=c5c948306f096e398e8896567ea1426bcb3c09b4cc982c3d453d3a9ce2b66b34 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `all_symbol_names(self) -> list[str]`

Return all distinct local symbol names for fuzzy-match suggestions on not-found queries.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.all_qualified_names fingerprint=81e36419552fcadd1ffbad7e8109246d3055e765019c0633cfcabdafa0ad9eff body_fp=e8f38ca923e4cde4350dc281bd890af4ede0e25d00714ba5806360b1349c4b87 source_ref=63d2e770fe7d46f83042110fb3bb5403fb9b9d04 -->
## `all_qualified_names(self) -> list[str]`

Return every qualified symbol name in the database.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.__init__ fingerprint=cbc4e30ba48edc9d8f65e1c5cbfcf9b29a9e2a9889581d7100fd1678981276b9 body_fp=ee4be1a173be0da98881aa3cab05cd4dde05853e5691d349f495586782dab2fd source_ref=aef35014ee7ba97f7bb5ee8252255be994acfdac -->
## `Store.__init__(self, db_path: Path) -> None`

Open or create the SQLite database at `db_path`, initialising the schema and dropping stale versions.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store._open fingerprint=1840acd2bf92663690f9ecd8c1a418eb53e4525df3070283393ae5fb73deed99 body_fp=226094a7201d3de1c2ebbad53e6be972c9ae2ee30528221cd7ba0c2162ebd585 source_ref=aef35014ee7ba97f7bb5ee8252255be994acfdac -->
## `_open(self) -> None`

Open the SQLite connection, detect a stale schema version, nuke and recreate the DB if stale, then apply `SCHEMA_SQL` and record the current version.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.__enter__ fingerprint=9f210cb9718c0e2ccf1afd3e1a8f2d55beb6c6390abbe06ed35fdd33a7172f7f body_fp=8f144d8f59958372f7043f35f597c38d5e459da2eda5e89bf2c40427413e5bc9 source_ref=aef35014ee7ba97f7bb5ee8252255be994acfdac -->
## `Store.__enter__(self) -> Store`

Return `self` to support use as a context manager.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.__exit__ fingerprint=67b1b6b146522ac7c8bdfff45bab8a41537d8e61231b937b0475a712971729e7 body_fp=757f4b526a63273903bb78c3e05916c1337a73aba75e3355c816501c3d0db310 source_ref=aef35014ee7ba97f7bb5ee8252255be994acfdac -->
## `__exit__(self, *_args: object) -> None`

Close the store connection when exiting the context manager.
<!-- trie:end -->

<!-- trie:section symbol=trie/graph/store:Store.symbols_in_file_with_lines fingerprint=6c50f1692f561e61d68233e23f1452068b7dc5151923fcf1a75c9e9f32d8fc97 body_fp=2a5400049acefd959d2d6ceb60c1543714f3239b956b5216b8e6514df4d99096 source_ref=6da877cab7a13b55f8c9b77428537bc9a241cac7 -->
## `symbols_in_file_with_lines(self, file_path: str) -> list[tuple[str, int, int]]`

Return `(qname, start_line, end_line)` for every symbol in `file_path`, ordered by `start_line`.

- Returns empty list when the path has no recorded symbols.
<!-- trie:end -->