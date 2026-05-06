"""End-to-end test for `trie sync --file` against the tiny fixture repo.

The LLM client is replaced with a deterministic FakeClient that returns canned section
bodies, so this test runs offline and is the M1 acceptance gate.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import pytest
from typer.testing import CliRunner

from trie.cli import app
from trie.config import Config
from trie.models import GenerationRequest, GenerationResponse
from trie.sync.single_file import sync_single_file
from trie.sync.writer import TriefactFile

FIXTURE_DIR = Path(__file__).parent / "fixtures" / "tiny_repo"


@dataclass
class FakeClient:
    """Returns a templated response per request, recording call count for caching assertions."""

    model_id: str = "fake/test"
    calls: int = 0
    requests_seen: list[GenerationRequest] | None = None

    def __post_init__(self) -> None:
        self.requests_seen = []

    def generate(self, req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        assert self.requests_seen is not None
        self.requests_seen.append(req)
        # Pull the symbol qname out of the request text for a unique deterministic body.
        return GenerationResponse(
            text=f"## generated section\n\nrequest #{self.calls} body.",
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=100 if self.calls == 1 else 0,
            cache_read_input_tokens=0 if self.calls == 1 else 100,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    """Copy the tiny fixture into a fresh temp dir and run `trie init` semantics manually."""
    root = tmp_path / "demo"
    shutil.copytree(FIXTURE_DIR, root)
    # Drop a minimal trie.toml so Config.find_and_load works.
    (root / "trie.toml").write_text(
        '[trie]\nversion = "0.1.0"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )
    return root


def test_sync_single_file_writes_triefact(project: Path):
    config, _ = Config.find_and_load(project)
    client = FakeClient()

    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
    )

    # Public symbols only: Calculator, Calculator.add, Calculator.multiply, Calculator.reset, add (5).
    assert result.symbols_generated == 5
    assert result.triefact_path == project / "triefacts" / "calculator.md"
    assert result.triefact_path.exists()

    rendered = result.triefact_path.read_text()
    # Front matter present
    assert "trie_version:" in rendered
    assert "source: calculator.py" in rendered
    assert "file_fingerprint:" in rendered
    # All public symbols got sections
    triefact = TriefactFile.parse(rendered)
    qnames = triefact.section_qnames()
    assert "calculator:add" in qnames
    assert "calculator:Calculator" in qnames
    assert "calculator:Calculator.add" in qnames
    assert "calculator:Calculator.multiply" in qnames
    assert "calculator:Calculator.reset" in qnames
    # Private symbol skipped
    assert "calculator:_internal_helper" not in qnames


def test_human_prose_between_sections_survives_resync(project: Path):
    config, _ = Config.find_and_load(project)

    # First sync to create triefacts
    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )
    triefact_path = project / "triefacts" / "strings.md"

    # Human edits prose between sections
    original = triefact_path.read_text()
    edited = original.replace(
        "<!-- trie:end -->",
        "<!-- trie:end -->\n\n## Why this module exists\n\nHand-written rationale.\n",
        1,  # only the first occurrence
    )
    triefact_path.write_text(edited)

    # Second sync (with new fake client → different generated bodies)
    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )

    after = triefact_path.read_text()
    assert "Hand-written rationale." in after
    assert "## Why this module exists" in after
    # Sections still present
    triefact = TriefactFile.parse(after)
    assert "strings:shout" in triefact.section_qnames()
    assert "strings:whisper" in triefact.section_qnames()


def test_resync_updates_section_when_source_changes(project: Path):
    config, _ = Config.find_and_load(project)

    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )
    triefact_path = project / "triefacts" / "strings.md"
    triefact_v1 = TriefactFile.parse(triefact_path.read_text())
    shout_v1 = triefact_v1.get_section("strings:shout")
    assert shout_v1 is not None

    # Modify the source: add a parameter to shout
    src = project / "strings.py"
    src.write_text(
        '"""String manipulation helpers."""\n\n\n'
        "def shout(s: str, exclaim: int = 1) -> str:\n"
        '    """Uppercase a string and append exclamation marks."""\n'
        '    return s.upper() + ("!" * exclaim)\n\n\n'
        "def whisper(s: str) -> str:\n"
        '    """Lowercase a string."""\n'
        "    return s.lower()\n"
    )

    sync_single_file(src, project_root=project, config=config, client=FakeClient())
    triefact_v2 = TriefactFile.parse(triefact_path.read_text())
    shout_v2 = triefact_v2.get_section("strings:shout")
    assert shout_v2 is not None
    # The fingerprint should have changed because the body was modified
    assert shout_v2.fingerprint != shout_v1.fingerprint


def test_resync_removes_section_when_symbol_deleted(project: Path):
    config, _ = Config.find_and_load(project)

    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )
    triefact_path = project / "triefacts" / "strings.md"
    assert "strings:whisper" in TriefactFile.parse(triefact_path.read_text()).section_qnames()

    # Delete whisper from the source
    src = project / "strings.py"
    src.write_text(
        '"""String manipulation helpers."""\n\n\n'
        "def shout(s: str) -> str:\n"
        '    """Uppercase a string and append an exclamation mark."""\n'
        '    return s.upper() + "!"\n'
    )

    result = sync_single_file(src, project_root=project, config=config, client=FakeClient())
    assert result.sections_removed == 1
    after = TriefactFile.parse(triefact_path.read_text())
    assert "strings:whisper" not in after.section_qnames()
    assert "strings:shout" in after.section_qnames()


def test_first_call_creates_cache_subsequent_calls_read(project: Path):
    """Verify that the prompt-cache token accounting reflects the first-call/subsequent-call split."""
    config, _ = Config.find_and_load(project)
    client = FakeClient()
    result = sync_single_file(
        project / "calculator.py",
        project_root=project,
        config=config,
        client=client,
    )
    # 5 public symbols → 5 calls. First creates cache, rest read.
    assert client.calls == 5
    assert result.cache_creation_input_tokens == 100
    assert result.cache_read_input_tokens == 400


def test_cli_sync_runs_incremental_when_no_flags(project: Path, monkeypatch):
    """Bare `trie sync` runs incremental cascade. Without a config it errors; the test
    here just confirms the command isn't rejected outright."""
    monkeypatch.chdir(project)

    monkeypatch.setattr("trie.cli.make_client", lambda model_id: FakeClient(model_id=model_id))

    runner = CliRunner()
    result = runner.invoke(app, ["sync"])
    # Project has no triefacts yet → all files are stale → incremental should sync them.
    assert result.exit_code == 0
    assert "synced" in result.output or "coherent" in result.output


def test_cli_sync_errors_on_missing_file(project: Path):
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--file", str(project / "nope.py")])
    assert result.exit_code == 1
    assert "does not exist" in result.output


def test_cli_sync_errors_when_no_config(tmp_path: Path):
    src = tmp_path / "lonely.py"
    src.write_text("def x():\n    pass\n")
    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--file", str(src)])
    assert result.exit_code == 1
    assert "trie.toml" in result.output
