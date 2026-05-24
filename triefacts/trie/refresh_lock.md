---
trie_version: 0.1.2
source: trie/refresh_lock.py
file_fingerprint: 61056ade51e9c5714da16cd2dd35c2b8ff75a5c2f11dfbe5a5a9d160fa32419b
last_synced_at: '2026-05-23T23:53:21Z'
description: Mutual exclusion + coalescing queue for `trie refresh`.
defines:
- kind: module
  qualified_name: trie/refresh_lock:__module__
  lines: 1-176
- kind: constant
  qualified_name: trie/refresh_lock:LOCK_FILENAME
  lines: 51-51
- kind: constant
  qualified_name: trie/refresh_lock:QUEUED_FILENAME
  lines: 52-52
- kind: function
  qualified_name: trie/refresh_lock:lock_path
  lines: 55-57
- kind: function
  qualified_name: trie/refresh_lock:queued_path
  lines: 60-62
- kind: class
  qualified_name: trie/refresh_lock:LockHolder
  lines: 66-117
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.mark_queued
  lines: 79-94
- kind: method
  qualified_name: trie/refresh_lock:LockHolder.consume_queued
  lines: 96-117
- kind: function
  qualified_name: trie/refresh_lock:try_acquire
  lines: 121-175
incoming_refs: 20
outgoing_refs: 0
---
<!-- trie:section symbol=trie/refresh_lock:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=27f03d3cac54145eb834ac9c046a7198eff58dc15f7544a5f7713d7af30518fb source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
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
<!-- trie:section symbol=trie/refresh_lock:lock_path fingerprint=fa3088fd68739b854180275954958c8a963a73e37727f2320f06ad463de967ae body_fp=21bd1a47dcd485c6201aca71ee602336435efb715fdc7b3cfe09c5a2bf5b9e98 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `lock_path(project_root: Path) -> Path`

Return the path to the refresh lock file for a given project root.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:queued_path fingerprint=95879d8bf8bf8e968c77a60ea271e4ae651e7c92546d422b5101977181858495 body_fp=5f7a6994cfc3f016b69bbd5baa492128f50be99bb3bc84c0cc86c21585cb22f4 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `queued_path(project_root: Path) -> Path`

Return the canonical path of the `refresh.queued` sentinel file inside a project's `.trie/` directory.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder fingerprint=e439d723dd88420de64af59d7f5afb1254d78ef77abaefa15688d43e6a1bcc91 body_fp=74d7700e005b57ac9ba19350617b741d2f00a63f0460e541ddbad93df8195a8d source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LockHolder(project_root: Path, acquired: bool, _fd: IO[bytes] | None = None)`

Handle returned by `try_acquire` representing either a won or contested refresh lock.

- `acquired`: `True` if this process holds the exclusive lock; `False` if contested.
- `mark_queued()`: touches the queued sentinel; no-op if `acquired` is `True`.
- `consume_queued()`: atomically removes sentinel and returns `True` if a queued pass is needed; no-op returning `False` when not acquired.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.mark_queued fingerprint=3617b6220645cf133dc03e1790150b06f1ba85993dfb1a164ab33719285eef3a body_fp=1cb4321fb0f527aee6083e11e4b5e97760d51ff613466a88f0ebdda17e56a60f source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LockHolder.mark_queued() -> None`

Touch the `refresh.queued` sentinel file to signal that another refresh pass is wanted.

- Only writes the sentinel when `acquired` is `False`; no-op on the lock holder itself.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:LockHolder.consume_queued fingerprint=631fb126c50921f21ab18ff51f25092d1fe0a61275f82801982e65ae117f7f65 body_fp=d944acbb7cc9c095f677bb10741185140e7daf41439a61f1d3d0e7c6c61c994a source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `LockHolder.consume_queued() -> bool`

Atomically check and clear the `refresh.queued` sentinel, returning `True` if a queued pass is needed.

- Returns `False` if `LockHolder` did not acquire the lock or sentinel is absent.
- Safe only while holding the exclusive flock; non-atomic otherwise.
<!-- trie:end -->
<!-- trie:section symbol=trie/refresh_lock:try_acquire fingerprint=f8de1fece64c1bcb8892f7b44b2af75e6f447096db53f0ede3a47034ab8b659d body_fp=34eb26402bc4b26bfa97701b6a1b56021bb5fa26e39bb865ef806cdb63c1b7e2 source_ref=6b6fb8bf76ce617c5f239ce25cd25d4c0c1b377d -->
## `try_acquire(project_root: Path) -> Iterator[LockHolder]`

Context-manager that attempts a non-blocking `LOCK_EX` flock on the refresh lock file, yielding a `LockHolder` regardless of outcome.

- `acquired=True`: caller holds the lock; fd is closed on context exit.
- `acquired=False`: another process holds the lock; raises only for unexpected `OSError` (not `EAGAIN`/`EWOULDBLOCK`).
<!-- trie:end -->