"""Tests for the narrow git helpers used by diff-aware regen.

These tests construct real git repos in tmp_path because the module's whole point
is to interact with `git` as a subprocess. We don't try to mock subprocess — the
failure modes we care about (no repo, no blob, bad hash) all come from real git
behaviour, and exercising it directly is the only honest test.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

try:
    import pytest
except ImportError:  # pragma: no cover
    pytest = None  # type: ignore[assignment]

from trie.git_helpers import compute_blob_hash, is_git_repo, retrieve_blob


def _git(args: list[str], cwd: Path) -> None:
    """Run git with default identity config so commits succeed in CI sandboxes."""
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _init_repo(path: Path) -> None:
    _git(["init", "-q", "-b", "main"], path)
    _git(["config", "user.email", "trie-test@example.com"], path)
    _git(["config", "user.name", "trie test"], path)


if pytest is not None:

    @pytest.fixture
    def repo(tmp_path: Path) -> Path:
        _init_repo(tmp_path)
        return tmp_path

    def test_is_git_repo_true_inside_repo(repo: Path):
        assert is_git_repo(repo) is True

    def test_is_git_repo_false_outside_repo(tmp_path: Path):
        # tmp_path itself isn't a repo when no _init_repo ran.
        assert is_git_repo(tmp_path) is False

    def test_compute_blob_hash_matches_git_hash_object(repo: Path):
        """The hash we record must equal what git would compute on `git add`."""
        f = repo / "foo.py"
        f.write_text("print('hello')\n")
        got = compute_blob_hash(f)
        assert got is not None
        # Independently compute via git for comparison.
        result = subprocess.run(
            ["git", "hash-object", "--", str(f)], cwd=repo, capture_output=True, check=True
        )
        expected = result.stdout.decode().strip()
        assert got == expected

    def test_compute_blob_hash_is_content_addressed(repo: Path):
        """Identical content in different paths produces the same blob hash."""
        a = repo / "a.py"
        b = repo / "b.py"
        a.write_text("same content\n")
        b.write_text("same content\n")
        assert compute_blob_hash(a) == compute_blob_hash(b)

    def test_compute_blob_hash_changes_when_content_changes(repo: Path):
        f = repo / "foo.py"
        f.write_text("version one\n")
        h1 = compute_blob_hash(f)
        f.write_text("version two\n")
        h2 = compute_blob_hash(f)
        assert h1 != h2

    def test_compute_blob_hash_missing_file_returns_none(repo: Path):
        assert compute_blob_hash(repo / "does-not-exist.py") is None

    def test_retrieve_blob_round_trips_committed_content(repo: Path):
        """A committed blob is retrievable by hash."""
        f = repo / "foo.py"
        content = "def foo():\n    return 42\n"
        f.write_text(content)
        blob_hash = compute_blob_hash(f)
        assert blob_hash is not None
        _git(["add", "foo.py"], repo)
        _git(["commit", "-q", "-m", "add foo"], repo)
        got = retrieve_blob(repo, blob_hash)
        assert got == content

    def test_retrieve_blob_unreachable_blob_returns_none(repo: Path):
        """A blob whose content was never written into .git/objects is unreachable."""
        f = repo / "foo.py"
        f.write_text("ephemeral\n")
        blob_hash = compute_blob_hash(f)
        assert blob_hash is not None
        # We computed the hash without `-w`, then deleted the file. The blob doesn't
        # exist in the object database, so cat-file fails and we return None.
        f.unlink()
        assert retrieve_blob(repo, blob_hash) is None

    def test_retrieve_blob_malformed_hash_returns_none(repo: Path):
        assert retrieve_blob(repo, "not-a-hash") is None
        assert retrieve_blob(repo, "") is None
        assert retrieve_blob(repo, "deadbeef") is None  # too short to be SHA-1

    def test_retrieve_blob_outside_repo_returns_none(tmp_path: Path):
        """A valid-shaped hash but no repo to consult → None."""
        fake_hash = "a" * 40
        assert retrieve_blob(tmp_path, fake_hash) is None

    def test_compute_blob_hash_outside_repo_returns_none(tmp_path: Path):
        """Outside a git repo, compute_blob_hash returns None deliberately.

        `git hash-object` does technically work without a repo, but stamping a hash
        that can never be retrieved is dead weight in the sentinel. We require an
        enclosing repo so the contract is "a non-None hash is theoretically resolvable."
        """
        f = tmp_path / "foo.py"
        f.write_text("content\n")
        assert compute_blob_hash(f) is None

    def test_diff_paths_includes_untracked_files(tmp_path: Path):
        """diff_paths returns add-diffs for untracked files alongside tracked modifications."""
        from trie.git_helpers import diff_paths

        repo = tmp_path / "repo"
        repo.mkdir()

        # Initialise a git repo with a committed triefacts file
        subprocess.run(["git", "init", str(repo)], check=True, capture_output=True)
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=repo,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Test User"],
            cwd=repo,
            check=True,
            capture_output=True,
        )

        triefacts_dir = repo / "triefacts"
        triefacts_dir.mkdir()

        mod_file = triefacts_dir / "mod.md"
        mod_file.write_text("old prose")
        subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "initial commit"],
            cwd=repo,
            check=True,
            capture_output=True,
        )

        # Tracked modification
        mod_file.write_text("new prose")

        # Untracked new file
        new_file = triefacts_dir / "new_feature.md"
        new_file.write_text("brand new prose")

        result = diff_paths(repo, ["triefacts"], base="HEAD")

        assert result is not None, "diff_paths should return a non-None result"
        assert "old prose" in result, "result should contain the removed 'old prose'"
        assert "new prose" in result, "result should contain the added 'new prose'"
        assert "brand new prose" in result, "result should contain untracked file content"
        assert "new_feature.md" in result, "result should mention the untracked filename"

        # Also verify that a repo with no pending changes returns an empty string
        # Commit the current changes first to produce a clean state
        clean_repo = tmp_path / "clean_repo"
        clean_repo.mkdir()
        subprocess.run(["git", "init", str(clean_repo)], check=True, capture_output=True)
        subprocess.run(
            ["git", "config", "user.email", "test@example.com"],
            cwd=clean_repo,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "config", "user.name", "Test User"],
            cwd=clean_repo,
            check=True,
            capture_output=True,
        )
        clean_triefacts = clean_repo / "triefacts"
        clean_triefacts.mkdir()
        (clean_triefacts / "stable.md").write_text("stable prose")
        subprocess.run(["git", "add", "."], cwd=clean_repo, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "stable commit"],
            cwd=clean_repo,
            check=True,
            capture_output=True,
        )

        clean_result = diff_paths(clean_repo, ["triefacts"], base="HEAD")
        assert clean_result == "", "diff_paths should return '' when there are no changes"
