"""Quiet, narrowly-scoped git operations for diff-aware regen.

trie itself isn't a git tool; this module exists because diff-aware section
regeneration needs a way to retrieve "the source as it was when this section
was last generated." The mechanism we use:

  1. At generation time, compute a content-addressed reference for the file
     and stamp it into the section sentinel (`source_ref=<blob-hash>`).
  2. On next regen, read the stamp and ask git for the blob.

Why blob hash and not commit hash:

  - Content-addressed: same content always produces the same hash. Two
    commits with the same file content share a blob, and history rewrites
    (rebases, cherry-picks) don't invalidate the reference.
  - Computable on a working-tree file without committing or staging.
  - Retrievable in O(1) via `git cat-file blob <hash>` whenever the blob
    is reachable from any ref or the index.

Every function in this module fails quietly: if there's no git repo, the
git binary isn't available, the blob isn't reachable, or the call errors
for any other reason, we return None and the caller degrades to today's
cold-write regen path. We never raise into the sync pipeline.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


def _run_git(
    args: list[str],
    *,
    cwd: Path,
    input_bytes: bytes | None = None,
) -> bytes | None:
    """Run `git <args>` from `cwd`. Return stdout bytes on success, None on any failure.

    Captures stderr to suppress noise. Times out after 5s as a defensive guard against
    a hung git invocation blocking sync.
    """
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            input=input_bytes,
            capture_output=True,
            check=False,
            timeout=5.0,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        return None
    if result.returncode != 0:
        return None
    return result.stdout


def is_git_repo(path: Path) -> bool:
    """True if `path` is inside a git working tree. Cheap probe; cached per call only."""
    out = _run_git(["rev-parse", "--is-inside-work-tree"], cwd=path)
    return out is not None and out.strip() == b"true"


def compute_blob_hash(file_path: Path) -> str | None:
    """Compute the git blob hash for the working-tree content of `file_path`.

    Does not write the blob into `.git/objects`. The returned hash is the same one
    git would record if this file were staged and committed. Returns None when:

      - the file is unreadable,
      - git is unavailable,
      - the file is outside a git working tree.

    The repo check is deliberate: `git hash-object` technically works without a repo,
    but a hash stamped outside a repo is unretrievable forever and stamping it
    confuses future tooling that assumes a present hash is resolvable. We'd rather
    omit the field than carry a dead reference.
    """
    resolved = file_path.resolve()
    if not resolved.is_file():
        return None
    if not is_git_repo(resolved.parent):
        return None
    # Run from the file's directory so any repo-config flags that affect hashing
    # (autocrlf, attributes) behave the same way as commit-time hashing.
    raw = _run_git(["hash-object", "--", str(resolved)], cwd=resolved.parent)
    if raw is None:
        return None
    text = raw.decode("utf-8", errors="replace").strip()
    # A blob hash is a 40-char (SHA-1) or 64-char (SHA-256) hex string. Anything else
    # is unexpected output we'd rather not stamp into a sentinel.
    if len(text) not in (40, 64):
        return None
    return text


def retrieve_blob(repo_root: Path, blob_hash: str) -> str | None:
    """Read the content of a git blob by hash. Returns None if unreachable.

    The blob is unreachable when:
      - The hash was generated on a file that was never committed and then the working
        tree changed (so git's pack of loose objects doesn't include it).
      - `repo_root` isn't inside a git repo.
      - The hash is malformed.

    On success, returns the decoded text. Binary blobs are decoded with `replace`;
    callers are responsible for sanity-checking the result if they need strict
    round-tripping (Python source is virtually always valid UTF-8).
    """
    if not blob_hash or len(blob_hash) not in (40, 64):
        return None
    out = _run_git(["cat-file", "blob", blob_hash], cwd=repo_root)
    if out is None:
        return None
    return out.decode("utf-8", errors="replace")
