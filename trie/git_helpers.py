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
    ok_returncodes: tuple[int, ...] = (0,),
) -> bytes | None:
    """Run `git <args>` from `cwd`. Return stdout bytes on success, None on any failure.

    Captures stderr to suppress noise. Times out after 5s as a defensive guard against
    a hung git invocation blocking sync. Callers may widen the accepted return codes via
    `ok_returncodes` (e.g. `git diff --no-index` exits 1 when files differ but is still
    considered a successful invocation).
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
    if result.returncode not in ok_returncodes:
        return None
    return result.stdout


def is_git_repo(path: Path) -> bool:
    """True if `path` is inside a git working tree. Cheap probe; cached per call only."""
    out = _run_git(["rev-parse", "--is-inside-work-tree"], cwd=path)
    return out is not None and out.strip() == b"true"


def current_head(repo_root: Path) -> str | None:
    """Return the commit SHA at HEAD, or None if the lookup fails.

    Used by trie's freshness gate to compare the working tree's HEAD against the
    stamp written at the last refresh. None is returned for empty repositories
    (no commits), detached states with no resolvable SHA, or any other git
    failure. Callers that need to fail loud on missing git should test for
    `is_git_repo` first; this function intentionally returns None rather than
    raising, matching the rest of `git_helpers`.
    """
    out = _run_git(["rev-parse", "HEAD"], cwd=repo_root)
    if out is None:
        return None
    text = out.decode("utf-8", errors="replace").strip()
    return text or None


def commit_timestamp(repo_root: Path, ref: str = "HEAD") -> float | None:
    """Return the committer unix timestamp of *ref* as a float, or None on any failure."""
    result = _run_git(["show", "-s", "--format=%ct", ref], cwd=repo_root)
    if result is None:
        return None
    raw = result.decode("utf-8", errors="replace").strip()
    if not raw:
        return None
    try:
        return float(raw.splitlines()[0].strip())
    except (ValueError, IndexError):
        return None


def compute_blob_hash(file_path: Path, *, max_bytes: int | None = None) -> str | None:
    """Compute the git blob hash for the working-tree content of `file_path`.

    Does not write the blob into `.git/objects`. The returned hash is the same one
    git would record if this file were staged and committed. Returns None when:

      - the file is unreadable,
      - git is unavailable,
      - the file is outside a git working tree,
      - the file size exceeds `max_bytes` (when set).

    When `max_bytes` is provided, files larger than the cap return None without
    invoking git. The cap is a defensive guard for diff-aware regen: a multi-MB
    file produces a hash trie can stamp but cannot usefully feed back into the
    diff-aware prompt window on the next sync. Default `None` preserves the
    unlimited behaviour every existing caller relies on.

    The repo check is deliberate: `git hash-object` technically works without a repo,
    but a hash stamped outside a repo is unretrievable forever and stamping it
    confuses future tooling that assumes a present hash is resolvable. We'd rather
    omit the field than carry a dead reference.
    """
    resolved = file_path.resolve()
    if not resolved.is_file():
        return None
    if max_bytes is not None and resolved.stat().st_size > max_bytes:
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


def diff_paths(repo_root: Path, paths: list[str], base: str = "HEAD") -> str | None:
    """Unified working-tree diff against `base` restricted to `paths`.

    Uses ``--no-color`` so output is machine-consumable.  Returns ``None``
    (not ``''``) when git itself fails, so callers can distinguish 'no
    changes' from 'no git'.  An empty string means the paths are unchanged
    relative to ``base``.

    Untracked files under ``paths`` are also included as add-diffs against
    ``/dev/null``, so brand-new files (e.g. freshly created triefacts) appear
    in the returned diff even before they have been staged or committed.
    """
    out = _run_git(["diff", "--no-color", base, "--", *paths], cwd=repo_root)
    if out is None:
        return None
    tracked_diff = out.decode("utf-8", errors="replace")

    untracked_out = _run_git(
        ["ls-files", "--others", "--exclude-standard", "--", *paths],
        cwd=repo_root,
    )
    if untracked_out is None:
        return tracked_diff

    parts = [tracked_diff]
    for raw_path in untracked_out.decode("utf-8", errors="replace").splitlines():
        raw_path = raw_path.strip()
        if not raw_path:
            continue
        abs_path = str(repo_root / raw_path)
        no_index_out = _run_git(
            ["diff", "--no-color", "--no-index", "--", "/dev/null", abs_path],
            cwd=repo_root,
            ok_returncodes=(0, 1),
        )
        if no_index_out is None:
            continue
        parts.append(no_index_out.decode("utf-8", errors="replace"))

    return "".join(parts)
