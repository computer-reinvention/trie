"""Mutual exclusion + coalescing queue for trie's write-side commands.

The freshness hook fires on every agent turn boundary. When an agent ships
many rapid turns — or two MCP harnesses race the same project — multiple
`trie sync --graph-only` processes can land overlapping. Each one would run a full
scan + (potentially) an LLM-spending sync against the same `.trie/graph.db`
SQLite file and the same triefact tree, racing on writes.

We resolve this with two on-disk artefacts inside the per-checkout `.trie/`
directory:

  - `refresh.lock`: a file held with `fcntl.flock(LOCK_EX | LOCK_NB)`. The
    OS releases it automatically on process exit, including crashes, so a
    dead trie process never strands the lock for the next caller.

  - `refresh.queued`: a sentinel file whose mere existence means "a refresh
    came in while I held the lock; do one more pass before releasing." The
    contents don't matter; we only check `exists()`. We deliberately keep
    this as a boolean rather than a counter — coalescing N rapid turns to
    "one more pass after the current one" is exactly what we want.

The contract:

    with try_acquire(project_root) as holder:
        if holder.acquired:
            run_refresh()
            while holder.consume_queued():
                run_refresh()
        else:
            holder.mark_queued()

After this block: the project saw at least one refresh that began *after*
every call site that observed the contention, which is the freshness
invariant we owe agents at turn boundaries.

POSIX only. Windows would need `msvcrt.locking()` or `portalocker`; deferred
until someone asks.
"""

from __future__ import annotations

import errno
import fcntl
import os
from collections.abc import Iterator
from contextlib import contextmanager, suppress
from dataclasses import dataclass
from pathlib import Path
from typing import IO

LOCK_FILENAME = "refresh.lock"
QUEUED_FILENAME = "refresh.queued"

LOCK_NAMES: set[str] = set()


def _register_lock_name(name: str) -> None:
    """Register a lock name so we can validate it."""
    LOCK_NAMES.add(name)


_register_lock_name("refresh")


def lock_path(project_root: Path, name: str = "refresh") -> Path:
    """Conventional location of a lock file under `.trie/`.

    `name` determines the filename: `refresh` → `refresh.lock`, `apply` → `apply.lock`.
    """
    return project_root / ".trie" / f"{name}.lock"


def queued_path(project_root: Path, name: str = "refresh") -> Path:
    """Conventional location of the queued sentinel under `.trie/`.

    `name` determines the filename: `refresh` → `refresh.queued`, `apply` → `apply.queued`.
    """
    return project_root / ".trie" / f"{name}.queued"


@dataclass
class LockHolder:
    """Handle to an acquired (or contested) refresh lock.

    Callers introspect `acquired` to branch between "I hold the lock; do the
    work" and "another process holds it; record that I wanted a refresh and
    leave." The remaining methods are no-ops on the contested side, so call
    sites can stay flat.
    """

    project_root: Path
    acquired: bool
    name: str = "refresh"
    _fd: IO[bytes] | None = None

    def mark_queued(self) -> None:
        """Signal to the lock holder that another operation is wanted.

        Idempotent: writing the sentinel twice is the same as once.
        """
        if not self.acquired:
            path = queued_path(self.project_root, self.name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()

    def consume_queued(self) -> bool:
        """Check-and-clear the queued sentinel.

        Used by the holder at the tail of its operation: if another process
        signalled while we were busy, run one more pass and consume the flag.
        """
        if not self.acquired:
            return False
        path = queued_path(self.project_root, self.name)
        if not path.exists():
            return False
        try:
            path.unlink()
        except FileNotFoundError:
            return False
        return True


@contextmanager
def try_acquire(project_root: Path, name: str = "refresh") -> Iterator[LockHolder]:
    """Try to acquire the exclusive lock without blocking.

    `name` determines the lock file: `apply` → `apply.lock`, `refresh` → `refresh.lock`.
    Each named lock is independent — acquiring `apply.lock` does not conflict with
    `refresh.lock`.

    Yields a `LockHolder` whose `acquired` flag tells the caller whether it
    won the race. On exit:

      - if we acquired, the lock fd is closed (releasing the OS-level lock);
      - if we didn't, nothing is closed (we never opened anything we'd need
        to clean up beyond the brief stat for the queued sentinel write).

    The lock file itself is left on disk between runs. That's intentional:
    `flock` is per-fd, not per-inode, and creating the file is what gives
    us an inode to lock against. Re-creating it every run would race on
    inode swaps under load.
    """
    _register_lock_name(name)
    path = lock_path(project_root, name=name)
    path.parent.mkdir(parents=True, exist_ok=True)

    # `os.open` rather than `open()` so we control the exact flags. The file
    # is just an anchor for `flock`; we never read or write its contents.
    fd = os.open(str(path), os.O_RDWR | os.O_CREAT, 0o644)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            # EAGAIN / EWOULDBLOCK: another process holds the lock. Anything
            # else (EBADF, ENOLCK on filesystems without locking) is exceptional
            # and we surface it rather than masking. EACCES on some NFS setups
            # also lands here; same treatment.
            if exc.errno in (errno.EAGAIN, errno.EWOULDBLOCK):
                os.close(fd)
                yield LockHolder(project_root=project_root, acquired=False, name=name, _fd=None)
                return
            os.close(fd)
            raise
        # Wrap fd in an IO-ish handle for the dataclass type; we don't actually
        # read or write through it. Using `os.fdopen` would buffer; we want raw.
        holder = LockHolder(project_root=project_root, acquired=True, name=name, _fd=None)
        try:
            yield holder
        finally:
            # Releasing the lock: closing the fd is sufficient (POSIX releases
            # all flocks held by a process when its last reference to the file
            # is closed). Explicit unlock is belt-and-braces against the case
            # where the fd somehow lives on through finalisation in a fork.
            with suppress(OSError):
                fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
    except BaseException:
        # Make sure we don't leak the fd if the flock call itself raised
        # something we didn't catch. The targeted handlers above already
        # close on the EAGAIN path.
        with suppress(OSError):
            os.close(fd)
        raise
