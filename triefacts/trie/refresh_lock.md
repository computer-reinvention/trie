---
trie_version: 0.1.5
source: trie/refresh_lock.py
file_fingerprint: 461fdc42c9807dca5469c0c263a1dd0c6c9aef648163a419a850b80082a4e985
last_synced_at: '2026-05-28T01:39:17Z'
description: Mutual exclusion + coalescing queue for `trie refresh`.
defines:
- kind: module
  qualified_name: trie/refresh_lock:__module__
  lines: 1-185
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_FILENAME
  lines: 51-51
- kind: constant
  qualified_name: trie/refresh_lock:QUEUED_FILENAME
  lines: 52-52
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_NAMES
  lines: 54-54
- kind: function
  qualified_name: trie/refresh_lock:_register_lock_name
  lines: 57-59
- kind: function
  qualified_name: trie/refresh_lock:lock_path
  lines: 65-70
- kind: function
  qualified_name: trie/refresh_lock:queued_path
  lines: 73-78
- kind: class
  qualified_name: trie/refresh_lock:LockHolder
  lines: 82-121
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.mark_queued
  lines: 96-104
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.consume_queued
  lines: 106-121
- kind: function
  qualified_name: trie/refresh_lock:try_acquire
  lines: 125-184
incoming_refs: 22
outgoing_refs: 0
---
<!-- trie:section symbol=trie/refresh_lock:__module__ fingerprint=105fd9e2cb19d65e5a58241b307951982df73a98eefe163e2ed77c7e28088af6 body_fp=27f03d3cac54145eb834ac9c046a7198eff58dc15f7544a5f7713d7af30518fb source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `refresh_lock`

Provide mutual-exclusion and coalescing-queue primitives for concurrent `trie refresh` processes sharing a `.trie/` directory.

- `LOCK_FILENAME`: on-disk exclusive lock anchor; held via `fcntl.flock`.
- `QUEUED_FILENAME`: boolean sentinel; presence means a refresh was requested while the lock was held.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LOCK_FILENAME fingerprint=296a1160b03c3354b363b929e63bc996a136b8fc4b15c4e01a9d2363b44aa28f body_fp=d9e2ec936108321298c500b865cf7565abc69664ccb74ff92dad90af5c78757d source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LOCK_FILENAME = "refresh.lock"`

Filename of the exclusive flock anchor file inside `.trie/`.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:QUEUED_FILENAME fingerprint=ac36b1424db45b3f82f1af66a5c5f5305cb7bade6e39d059b3d4185e5b40a632 body_fp=97ece44d48c4ea4e82e73b616b46694395a3e48c75f7a47cdf9a8be3fbab10b5 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `QUEUED_FILENAME = "refresh.queued"`

Filename of the boolean sentinel file indicating a queued refresh is pending.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LOCK_NAMES fingerprint=c53f2ac7ddea965a4eba06568fa0a67759e9caed568f9374710e4d6f892b482b body_fp=53aec5b0b6ef1a43a296c92d7249cbf7f59dfb162fe955e1629c4895515d7738 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `LOCK_NAMES: set[str]`

Registry of all lock names passed to `_register_lock_name` for validation.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:_register_lock_name fingerprint=17f91ff119b7aa625e8976c7fa00bfe70b5e5018e1e985de026dc83d32c30fa8 body_fp=8920605b29a7297d4a28eda6b1934b5f5653121fb59da9ad1a593d6138c6f9cc source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `_register_lock_name(name: str) -> None`

Add `name` to the `LOCK_NAMES` set for later validation.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:lock_path fingerprint=c610e86a3f8542a0e1e182730727359ea33d3ac720a46ed3f5f681146368091f body_fp=21e9cbc0c9639d0bd0cac627d9355d9ac22cbf2a16eda45f59aa14036f432264 source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `lock_path(project_root: Path, name: str = "refresh") -> Path`

Return the path to a named lock file under `.trie/` for a given project root.

- `name`: base name determining the filename; `"refresh"` → `refresh.lock`, `"apply"` → `apply.lock`.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:queued_path fingerprint=68114fd059c6f0347ee6f892e273a22863abb4039065b72f3256a6e2f6ca2137 body_fp=11940afe71b0ef967b3ce6444f1123258e264983653feae92788cbcd9304aafb source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `queued_path(project_root: Path, name: str = "refresh") -> Path`

Return the canonical path of a `<name>.queued` sentinel file inside a project's `.trie/` directory.

- `name`: base name of the sentinel; `"refresh"` → `refresh.queued`, `"apply"` → `apply.queued`.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder fingerprint=b55694a146f40bf55285a276cd4df716502c440e040bb4cf4fde471f11a8b1bf body_fp=4f88ba1dcbe2dbe82e88e5d1741adfaea2927bd1af128ae053c64679e7c59eea source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `LockHolder(project_root: Path, acquired: bool, name: str = "refresh", _fd: IO[bytes] | None = None)`

Handle returned by `try_acquire` representing either a won or contested refresh lock.

- `acquired`: `True` if this process holds the exclusive lock; `False` if contested.
- `name`: selects which lock/queued sentinel files are used (e.g. `"refresh"`, `"apply"`).
- `mark_queued()`: touches the queued sentinel; no-op if `acquired` is `True`.
- `consume_queued()`: atomically removes sentinel and returns `True` if a queued pass is needed; no-op returning `False` when not acquired.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.mark_queued fingerprint=9aed2862bedff649eb249383557d2cddd31ef4a4a00c4933e32ba9521edb4857 body_fp=1cb4321fb0f527aee6083e11e4b5e97760d51ff613466a88f0ebdda17e56a60f source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `LockHolder.mark_queued() -> None`

Touch the `refresh.queued` sentinel file to signal that another refresh pass is wanted.

- Only writes the sentinel when `acquired` is `False`; no-op on the lock holder itself.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.consume_queued fingerprint=fb0387219d5a28f6c9e532241df5b67970a48d1252b5698e377364d9dcbebdd5 body_fp=d944acbb7cc9c095f677bb10741185140e7daf41439a61f1d3d0e7c6c61c994a source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `LockHolder.consume_queued() -> bool`

Atomically check and clear the `refresh.queued` sentinel, returning `True` if a queued pass is needed.

- Returns `False` if `LockHolder` did not acquire the lock or sentinel is absent.
- Safe only while holding the exclusive flock; non-atomic otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:try_acquire fingerprint=505f7d32ed2a79bce34da78a62c7a116f27146d64b62ffa5b247928d7f5b7179 body_fp=ff8c73590bfdfb9a3b771cc7ad72163f20f47328f51aec0866898c27fa424a3f source_ref=4f938fe8d35c1e2a4c3c1c2542008b437cfabcde -->
## `try_acquire(project_root: Path, name: str = "refresh") -> Iterator[LockHolder]`

Context-manager that attempts a non-blocking `LOCK_EX` flock on a named lock file, yielding a `LockHolder` regardless of outcome.

- `name`: selects the lock file (`refresh` → `refresh.lock`, `apply` → `apply.lock`); each name is independent.
- `acquired=True`: caller holds the lock; fd is closed on context exit.
- `acquired=False`: another process holds the lock; raises only for unexpected `OSError` (not `EAGAIN`/`EWOULDBLOCK`).
<!-- trie:end -->