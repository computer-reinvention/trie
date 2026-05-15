from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.check import StaleReason, check_project
from trie.cli import app
from trie.config import Config
from trie.models import GenerationRequest, GenerationResponse
from trie.sync.single_file import sync_single_file


@dataclass
class FakeClient:
    model_id: str = "fake/test"
    calls: int = 0

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        return GenerationResponse(
            text="## generated\n\nbody.",
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "alpha.py").write_text("def alpha():\n    return 1\n")
    (tmp_path / "src" / "beta.py").write_text("def beta():\n    return 2\n")
    return tmp_path


def _sync_all(project: Path) -> None:
    config, _ = Config.find_and_load(project)
    for src in (project / "src").glob("*.py"):
        sync_single_file(src, project_root=project, config=config, client=FakeClient())


def test_clean_after_fresh_sync(project: Path):
    _sync_all(project)
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    assert result.is_clean


def test_missing_triefact_detected(project: Path):
    # No triefacts generated at all
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    reasons = {it.reason for it in result.items}
    assert StaleReason.MISSING_TRIEFACT in reasons
    assert not result.is_clean


def test_stale_section_detected(project: Path):
    _sync_all(project)
    # Modify alpha's body
    (project / "src" / "alpha.py").write_text("def alpha():\n    return 999\n")
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    stale = [it for it in result.items if it.reason == StaleReason.STALE_SECTION]
    assert any(it.qualified_name == "src/alpha:alpha" for it in stale)


def test_missing_section_detected(project: Path):
    _sync_all(project)
    # Add a new symbol to beta
    (project / "src" / "beta.py").write_text(
        "def beta():\n    return 2\n\n\ndef beta2():\n    return 3\n"
    )
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    missing = [it for it in result.items if it.reason == StaleReason.MISSING_SECTION]
    assert any(it.qualified_name == "src/beta:beta2" for it in missing)


def test_orphan_section_detected(project: Path):
    _sync_all(project)
    # Remove alpha's symbol
    (project / "src" / "alpha.py").write_text(
        "# alpha was deleted; triefact still has its section\n"
    )
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    orphan = [it for it in result.items if it.reason == StaleReason.ORPHAN_SECTION]
    assert any(it.qualified_name == "src/alpha:alpha" for it in orphan)


def test_private_only_file_requires_a_triefact(project: Path):
    """Under symbol-level sync, the leading-underscore convention is descriptive,
    not a filter. A file of only `_`-prefixed symbols is still documented, and
    `check` flags `MISSING_TRIEFACT` for it until sync runs."""
    (project / "src" / "private_only.py").write_text(
        "def _hidden():\n    pass\n\n\ndef _also_hidden():\n    pass\n"
    )
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    private_items = [it for it in result.items if it.source_path == "src/private_only.py"]
    assert len(private_items) == 1
    assert private_items[0].reason == StaleReason.MISSING_TRIEFACT


def test_file_with_no_parser_surfaced_symbols_needs_no_triefact(project: Path):
    """A file with zero parser-surfaced defs (imports + module-level only) is
    excluded from the check — there is literally nothing to document."""
    (project / "src" / "empty_module.py").write_text(
        "import os\nfrom pathlib import Path\n\nCONSTANT = 1\n"
    )
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    items = [it for it in result.items if it.source_path == "src/empty_module.py"]
    assert items == []


def test_clean_when_all_in_sync_with_human_prose(project: Path):
    _sync_all(project)
    # Add hand-written prose between/after sections — must not trip the check
    triefact = project / "triefacts" / "src" / "alpha.md"
    text = triefact.read_text()
    triefact.write_text(text + "\n\n## Author notes\n\nHand-written.\n")
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    assert result.is_clean


def test_cli_verify_exits_zero_when_clean(project: Path, monkeypatch: pytest.MonkeyPatch):
    _sync_all(project)
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 0
    assert "coherent" in result.output


def test_cli_verify_exits_nonzero_when_stale(project: Path, monkeypatch: pytest.MonkeyPatch):
    _sync_all(project)
    (project / "src" / "alpha.py").write_text("def alpha():\n    return 999\n")
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 1
    assert "stale" in result.output
    assert "src/alpha:alpha" in result.output


def test_cli_verify_quiet_mode(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Global --quiet/-q suppresses per-symbol detail; summary still emits via reporter.error."""
    _sync_all(project)
    (project / "src" / "alpha.py").write_text("def alpha():\n    return 999\n")
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["-q", "verify"])
    assert result.exit_code == 1
    # Per-symbol details suppressed in quiet mode
    assert "src/alpha:alpha" not in result.output
    # Summary still present
    assert "issue" in result.output


def test_cli_verify_detects_tampered_body(project: Path, monkeypatch: pytest.MonkeyPatch):
    """Body inside section sentinels is hashed too: tampering trips TAMPERED_BODY."""
    import re

    _sync_all(project)
    triefact = project / "triefacts" / "src" / "alpha.md"
    text = triefact.read_text()
    tampered = re.sub(r"## generated\n\nbody\.", "TAMPERED CONTENT", text)
    triefact.write_text(tampered)
    monkeypatch.chdir(project)
    runner = CliRunner()
    result = runner.invoke(app, ["verify"])
    assert result.exit_code == 1
    assert "tampered" in result.output.lower()
    assert "src/alpha:alpha" in result.output


def test_check_project_detects_tampered_body(project: Path):
    """Unit-level: hand-edits inside a section sentinel are caught via body fingerprint."""
    import re

    _sync_all(project)
    triefact = project / "triefacts" / "src" / "beta.md"
    text = triefact.read_text()
    tampered = re.sub(r"## generated\n\nbody\.", "DIFFERENT TEXT", text)
    triefact.write_text(tampered)
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    assert any(
        it.reason == StaleReason.TAMPERED_BODY and it.qualified_name == "src/beta:beta"
        for it in result.items
    )


def test_check_project_detects_legacy_section(project: Path):
    """Sections without a body_fp= attribute (trie ≤ 0.1 output) flag LEGACY_SECTION."""
    import re

    _sync_all(project)
    triefact = project / "triefacts" / "src" / "alpha.md"
    text = triefact.read_text()
    # Strip the body_fp= field to simulate a legacy sentinel. We tolerate either
    # ordering of optional fields (body_fp= and source_ref= can appear in any order
    # in current trie output), so the regex removes a body_fp= run anywhere between
    # `fingerprint=...` and `-->`.
    legacy = re.sub(r"\s+body_fp=\S+", "", text, count=1)
    triefact.write_text(legacy)
    config, _ = Config.find_and_load(project)
    result = check_project(project_root=project, config=config)
    assert any(
        it.reason == StaleReason.LEGACY_SECTION and it.qualified_name == "src/alpha:alpha"
        for it in result.items
    )
