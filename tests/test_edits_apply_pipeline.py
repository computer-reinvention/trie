from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from trie.config import Config
from trie.edits.apply import apply_patches
from trie.graph.store import Store
from trie.models import (
    BatchFilterOutput,
    MergeNotesOutput,
    ModelResult,
    SectionBody,
    SymbolEdit,
)
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.2"\n'
    '[scope]\ninclude = ["src/**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    'edits = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
)


def _git(args: list[str], cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def _init_repo(path: Path) -> None:
    _git(["init", "-q", "-b", "main"], path)
    _git(["config", "user.email", "trie-test@example.com"], path)
    _git(["config", "user.name", "trie test"], path)


def _extract_old_source(request: str) -> str:
    """Extract source from the old source block in an infer prompt."""
    old_source = ""
    in_block = False
    for line in request.split("\n"):
        if line.startswith("```python"):
            in_block = True
            continue
        if in_block:
            if line.startswith("```") and not line.startswith("``````"):
                break
            if line.strip():
                old_source += line + "\n"
    return old_source.rstrip("\n")


def _extract_old_prose(request: str) -> str:
    """Extract old prose from the infer prompt."""
    prose_marker = "Old prose (the symbol's documented purpose):"
    if prose_marker not in request:
        return ""
    after = request.split(prose_marker, 1)[1]
    before_notes = after.split("\nImplementation notes", 1)[0]
    return before_notes.strip()


def _is_merge_prompt(request: str) -> bool:
    return "The following patch notes exist" in request


def _make_usage(**overrides: int):
    return type(
        "Usage",
        (),
        {
            "input_tokens": overrides.get("input_tokens", 10),
            "output_tokens": overrides.get("output_tokens", 20),
            "details": {
                "cache_creation_input_tokens": overrides.get("cache_creation_input_tokens", 0),
                "cache_read_input_tokens": overrides.get("cache_read_input_tokens", 0),
            },
        },
    )()


class FakeTriefactClient:
    """LLM stand-in that returns a static triefact body for sync_single_file."""

    model_id: str = "fake/triefact"

    @staticmethod
    def run(
        output_type: type,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        return ModelResult(
            output=SectionBody(body="## Symbol\n\nAuto-generated prose.\n"),
            usage=_make_usage(),
        )

    @staticmethod
    def count_tokens(system_prompt: str, user_prompt: str) -> int:
        return 100


class FakeEditClient:
    """LLM stand-in for patch-apply calls.

    Responds differently for merge_notes vs infer_source_and_prose prompts.
    """

    model_id: str = "fake/edits"

    @staticmethod
    def run(
        output_type: type,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        if output_type is MergeNotesOutput:
            return ModelResult(
                output=MergeNotesOutput(notes=["* change return value  —  test"], reasons=["test"]),
                usage=_make_usage(),
            )
        if output_type is BatchFilterOutput:
            return ModelResult(
                output=BatchFilterOutput(decisions=[]),
                usage=_make_usage(),
            )
        old_source = _extract_old_source(user_prompt)
        new_source = old_source + "\n# patch-applied"
        return ModelResult(
            output=SymbolEdit(source=new_source, prose="## Updated\n\nModified by patch.\n"),
            usage=_make_usage(),
        )

    @staticmethod
    def count_tokens(system_prompt: str, user_prompt: str) -> int:
        return 100


class PassthroughClient:
    """LLM stand-in that echoes the old source/prose unchanged."""

    model_id: str = "fake/passthrough"

    @staticmethod
    def run(
        output_type: type,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        if output_type is MergeNotesOutput:
            return ModelResult(
                output=MergeNotesOutput(notes=["* change return value  —  test"], reasons=["test"]),
                usage=_make_usage(),
            )
        if output_type is BatchFilterOutput:
            return ModelResult(
                output=BatchFilterOutput(decisions=[]),
                usage=_make_usage(),
            )
        old_source = _extract_old_source(user_prompt)
        old_prose = _extract_old_prose(user_prompt)
        return ModelResult(
            output=SymbolEdit(source=old_source, prose=old_prose),
            usage=_make_usage(),
        )

    @staticmethod
    def count_tokens(system_prompt: str, user_prompt: str) -> int:
        return 100


class BrokenClient:
    """LLM stand-in that returns syntactically invalid source."""

    model_id: str = "fake/broken"

    @staticmethod
    def run(
        output_type: type,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        if output_type is MergeNotesOutput:
            return ModelResult(
                output=MergeNotesOutput(notes=["* change return value  —  test"], reasons=["test"]),
                usage=_make_usage(),
            )
        if output_type is BatchFilterOutput:
            return ModelResult(
                output=BatchFilterOutput(decisions=[]),
                usage=_make_usage(),
            )
        return ModelResult(
            output=SymbolEdit(source="def broken(:", prose="Broken."),
            usage=_make_usage(),
        )

    @staticmethod
    def count_tokens(system_prompt: str, user_prompt: str) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Three-module project with call chain alpha -> beta -> gamma, fully synced."""
    src = tmp_path / "src"
    src.mkdir()
    (src / "__init__.py").write_text("")
    (src / "alpha.py").write_text(
        "from src.beta import beta_fn\n\n\n"
        "def alpha_fn() -> int:\n"
        '    """Top-level entry."""\n'
        "    return beta_fn() + 1\n"
    )
    (src / "beta.py").write_text(
        "from src.gamma import gamma_fn\n\n\n"
        "def beta_fn() -> int:\n"
        '    """Middle layer."""\n'
        "    return gamma_fn() + 10\n"
    )
    (src / "gamma.py").write_text(
        'def gamma_fn() -> int:\n    """Deepest callee."""\n    return 100\n'
    )

    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / ".gitignore").write_text(".trie/\n__pycache__/\n")

    config, _ = Config.find_and_load(tmp_path)
    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        sync_client = FakeTriefactClient()
        sync_single_file(
            tmp_path / "src/alpha.py",
            project_root=tmp_path,
            config=config,
            client=sync_client,
            store=store,
        )
        sync_single_file(
            tmp_path / "src/beta.py",
            project_root=tmp_path,
            config=config,
            client=sync_client,
            store=store,
        )
        sync_single_file(
            tmp_path / "src/gamma.py",
            project_root=tmp_path,
            config=config,
            client=sync_client,
            store=store,
        )

    _init_repo(tmp_path)
    _git(["add", "."], tmp_path)
    _git(["commit", "-q", "-m", "initial"], tmp_path)
    return tmp_path


class TestApplyPatchesEmpty:
    def test_no_patches_returns_immediately(self, project: Path):
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            result = apply_patches(store, config, FakeEditClient(), project)
        assert result["ok"] is True
        assert result["total_files"] == 0
        assert result["total_symbols"] == 0

    def test_git_clean_after_empty_apply(self, project: Path):
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            apply_patches(store, config, FakeEditClient(), project)
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=project,
            capture_output=True,
            text=True,
            check=True,
        )
        assert status.stdout.strip() == ""


class TestApplyPatchesSuccess:
    def test_applies_single_symbol(self, project: Path):
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "change return value", "test", "sess1")
            patches_before = store.get_patches_for_qname("src/gamma:gamma_fn")
            assert len(patches_before) == 1

            result = apply_patches(store, config, FakeEditClient(), project)

        assert result["ok"] is True
        assert result["total_files"] >= 1
        assert result["total_symbols"] >= 1

    def test_patches_deleted_after_success(self, project: Path):
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "change return", "test", "sess1")
            store.add_patch("src/gamma:gamma_fn", "add docstring", "docs", "sess1")
            result = apply_patches(store, config, FakeEditClient(), project)

        assert result["ok"] is True
        with Store(project / ".trie" / "graph.db") as store:
            assert store.get_patches_for_qname("src/gamma:gamma_fn") == []

    def test_no_git_commit_created(self, project: Path):
        """apply_patches no longer creates git commits."""
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "change return", "test", "s1")
            apply_patches(store, config, FakeEditClient(), project)

        log = subprocess.run(
            ["git", "log", "--oneline", "-1"],
            cwd=project,
            capture_output=True,
            text=True,
            check=True,
        )
        assert "apply" not in log.stdout

    def test_applies_in_topo_order(self, project: Path):
        """Patch deepest callee (gamma); verify alpha/beta chain works."""
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "return 999", "bump value", "s1")
            result = apply_patches(store, config, FakeEditClient(), project)

        assert result["ok"] is True

    def test_cascaded_no_change_skips_write(self, project: Path):
        """Cascaded neighbour with identical source should not modify files."""
        config, _ = Config.find_and_load(project)
        client = PassthroughClient()

        gamma_before = (project / "src/gamma.py").read_text()

        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "cosmetic only", "nit", "s1")
            result = apply_patches(store, config, client, project)

        assert result["ok"] is True
        assert result["total_files"] >= 1
        gamma_after = (project / "src/gamma.py").read_text()
        assert gamma_after == gamma_before


class TestApplyPatchesFailure:
    def test_compile_error_returns_failure(self, project: Path):
        config, _ = Config.find_and_load(project)
        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "break syntax", "test", "s1")
            result = apply_patches(store, config, BrokenClient(), project)

        assert result["ok"] is False
        assert len([f for f in result.get("files", []) if not f["ok"]]) >= 1
        assert result["error"] is not None

    def test_rollback_restores_files(self, project: Path):
        """After a failure, files should be back to committed state."""
        config, _ = Config.find_and_load(project)

        gamma_before = (project / "src/gamma.py").read_text()

        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "break syntax", "test", "s1")
            apply_patches(store, config, BrokenClient(), project)

        gamma_after = (project / "src/gamma.py").read_text()
        assert gamma_after == gamma_before

    def test_patches_preserved_after_rollback(self, project: Path):
        """On failure, patches should remain in DB for retry."""
        config, _ = Config.find_and_load(project)

        with Store(project / ".trie" / "graph.db") as store:
            store.add_patch("src/gamma:gamma_fn", "break syntax", "test", "s1")
            apply_patches(store, config, BrokenClient(), project)
            remaining = store.get_patches_for_qname("src/gamma:gamma_fn")

        assert len(remaining) == 1
