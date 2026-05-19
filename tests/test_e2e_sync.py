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
        '[trie]\nversion = "0.1.2"\n'
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

    # Every parser-surfaced symbol is documented under symbol-level sync — the
    # `is_public` flag is descriptive metadata, not a filter. Calculator, its three
    # methods, the module-level `add`, and the underscored `_internal_helper` all
    # get sections (6 total).
    assert result.symbols_generated == 6
    assert result.triefact_path == project / "triefacts" / "calculator.md"
    assert result.triefact_path.exists()

    rendered = result.triefact_path.read_text()
    # Front matter present
    assert "trie_version:" in rendered
    assert "source: calculator.py" in rendered
    assert "file_fingerprint:" in rendered
    # Every symbol got a section, including the underscored helper.
    triefact = TriefactFile.parse(rendered)
    qnames = triefact.section_qnames()
    assert "calculator:add" in qnames
    assert "calculator:Calculator" in qnames
    assert "calculator:Calculator.add" in qnames
    assert "calculator:Calculator.multiply" in qnames
    assert "calculator:Calculator.reset" in qnames
    assert "calculator:_internal_helper" in qnames


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
    # 6 documented symbols (every parser-surfaced symbol — `_internal_helper` is
    # no longer filtered out) → 6 calls. First creates cache, rest read.
    assert client.calls == 6
    assert result.cache_creation_input_tokens == 100
    assert result.cache_read_input_tokens == 500


def test_cli_sync_auto_bootstraps_first_run(project: Path, monkeypatch):
    """In a fresh project, bare `trie sync` auto-detects first-run bootstrap. Pass
    --limit to satisfy the non-interactive cap requirement."""
    monkeypatch.chdir(project)

    monkeypatch.setattr(
        "trie.cli.make_client",
        lambda model_id, **_kw: FakeClient(model_id=model_id),
    )

    runner = CliRunner()
    result = runner.invoke(app, ["sync", "--limit", "10"])
    assert result.exit_code == 0, result.output
    assert "synced" in result.output


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


# --- diff-aware regen (Level 1) ---


def _init_git(repo: Path) -> None:
    """Initialize a git repo in `repo` so compute_blob_hash / retrieve_blob work."""
    import subprocess

    subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.email", "trie-test@example.com"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "trie test"], cwd=repo, check=True)


def test_first_sync_in_git_repo_stamps_source_ref(project: Path):
    """First sync against a git-managed file stamps source_ref= in every section."""
    _init_git(project)
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )
    triefact_path = project / "triefacts" / "strings.md"
    rendered = triefact_path.read_text()
    # Every section should carry source_ref now.
    triefact = TriefactFile.parse(rendered)
    for qn in triefact.section_qnames():
        sec = triefact.get_section(qn)
        assert sec is not None
        assert sec.source_ref is not None, f"section {qn} missing source_ref"
        assert len(sec.source_ref) == 40  # SHA-1 blob hash


def test_sync_outside_git_repo_omits_source_ref(project: Path):
    """Without git, source_ref is None — sections render without the field."""
    # No git init for this project.
    config, _ = Config.find_and_load(project)
    sync_single_file(
        project / "strings.py",
        project_root=project,
        config=config,
        client=FakeClient(),
    )
    triefact_path = project / "triefacts" / "strings.md"
    rendered = triefact_path.read_text()
    assert "source_ref=" not in rendered


def test_resync_with_committed_history_takes_diff_aware_path(project: Path):
    """After commit, resync of a changed file passes previous source + previous prose
    to the generator. Verified by inspecting the FakeClient's request payload."""
    import subprocess

    _init_git(project)
    config, _ = Config.find_and_load(project)

    src = project / "strings.py"
    # First sync against the original file content.
    sync_single_file(src, project_root=project, config=config, client=FakeClient())
    # Commit both the source and the triefact so the blob is reachable.
    subprocess.run(["git", "add", "-A"], cwd=project, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "first sync"], cwd=project, check=True)

    # Modify the source.
    src.write_text(
        '"""String manipulation helpers."""\n\n\n'
        "def shout(s: str, exclaim: int = 3) -> str:\n"
        '    """Uppercase a string and append several exclamation marks."""\n'
        '    return s.upper() + ("!" * exclaim)\n\n\n'
        "def whisper(s: str) -> str:\n"
        '    """Lowercase a string."""\n'
        "    return s.lower()\n"
    )

    second_client = FakeClient()
    sync_single_file(src, project_root=project, config=config, client=second_client)

    # The shout section should have been regenerated in diff-aware mode.
    # Inspect the requests the client received for evidence.
    assert second_client.requests_seen is not None
    shout_reqs = [r for r in second_client.requests_seen if "strings:shout" in r.request]
    assert shout_reqs, "expected at least one request mentioning strings:shout"
    shout_req = shout_reqs[0]
    assert "<previous_source>" in shout_req.request
    assert "<previous_prose>" in shout_req.request
    assert "<current_source>" in shout_req.request
    # Previous body referenced the old signature; current body has the new one.
    assert "exclaim: int = 1" in shout_req.request or "return s.upper() +" in shout_req.request
    assert "exclaim: int = 3" in shout_req.request


def test_resync_after_uncommitted_change_falls_back_to_cold(project: Path):
    """If the previous version's blob isn't in git's object store (file was modified
    but never committed since the last sync), retrieval fails and we degrade to cold.

    Note this also exercises the first-stamp-then-modify path: the first sync stamps
    a source_ref against an uncommitted file, but git hash-object computes the hash
    without writing. Modifying the file before any commit makes the original blob
    unreachable.
    """
    _init_git(project)
    config, _ = Config.find_and_load(project)
    src = project / "strings.py"

    sync_single_file(src, project_root=project, config=config, client=FakeClient())
    # Modify without committing.
    src.write_text(
        '"""String manipulation helpers."""\n\n\n'
        "def shout(s: str) -> str:\n"
        '    """Different docstring."""\n'
        "    return s.upper()\n\n\n"
        "def whisper(s: str) -> str:\n"
        '    """Lowercase a string."""\n'
        "    return s.lower()\n"
    )

    second_client = FakeClient()
    sync_single_file(src, project_root=project, config=config, client=second_client)
    # No <previous_source> block — diff-aware path didn't activate.
    assert second_client.requests_seen is not None
    for req in second_client.requests_seen:
        assert "<previous_source>" not in req.request
