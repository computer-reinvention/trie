from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from trie.config import Config
from trie.cost import get_pricing
from trie.diff_cmd import diff_project
from trie.models import GenerationRequest, GenerationResponse
from trie.sync.single_file import sync_single_file


@dataclass
class StableClient:
    """First sync produces 'v1 body'; subsequent calls produce 'v2 body' so diffs show change."""

    model_id: str = "anthropic/claude-sonnet-4-6"
    body: str = "## v1\n\nv1 body."
    calls: int = 0

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        self.calls += 1
        return GenerationResponse(
            text=self.body,
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )


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
    return tmp_path


def test_diff_returns_empty_when_clean(project: Path):
    config, _ = Config.find_and_load(project)
    client_v1 = StableClient(body="## v1\n\nv1 body.")
    sync_single_file(
        project / "src" / "alpha.py",
        project_root=project,
        config=config,
        client=client_v1,
    )
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    result = diff_project(project_root=project, config=config, client=client_v1, pricing=pricing)
    assert result.diffs == []


def test_diff_shows_regenerated_content(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")

    # Generate v1
    sync_single_file(
        project / "src" / "alpha.py",
        project_root=project,
        config=config,
        client=StableClient(body="## v1\n\nv1 body."),
    )

    # Modify source so check sees a stale section
    (project / "src" / "alpha.py").write_text("def alpha():\n    return 999\n")

    # Diff with a v2 client
    client_v2 = StableClient(body="## v2\n\nv2 body.")
    result = diff_project(project_root=project, config=config, client=client_v2, pricing=pricing)
    assert len(result.diffs) == 1
    fd = result.diffs[0]
    assert fd.source_path == "src/alpha.py"
    assert "v1 body." in fd.unified_diff or "v1" in fd.unified_diff
    assert "v2 body." in fd.unified_diff
    # Preview file actually written
    assert fd.preview_triefact_path.exists()
    # Live file unchanged
    canonical_text = fd.canonical_triefact_path.read_text()
    assert "v1 body." in canonical_text
    assert "v2 body." not in canonical_text


def test_diff_writes_to_preview_dir(project: Path):
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")

    # Stale: missing triefact
    result = diff_project(
        project_root=project,
        config=config,
        client=StableClient(),
        pricing=pricing,
    )
    assert len(result.diffs) == 1
    preview_path = result.diffs[0].preview_triefact_path
    assert ".trie/preview" in str(preview_path).replace("\\", "/")
    assert preview_path.exists()
    # Live tree unchanged
    canonical = result.diffs[0].canonical_triefact_path
    assert not canonical.exists()


def test_diff_respects_limit(project: Path):
    (project / "src" / "beta.py").write_text("def beta():\n    pass\n")
    (project / "src" / "gamma.py").write_text("def gamma():\n    pass\n")
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    result = diff_project(
        project_root=project,
        config=config,
        client=StableClient(),
        pricing=pricing,
        limit=2,
    )
    assert len(result.diffs) == 2
    assert result.files_skipped_no_budget >= 1


def test_diff_respects_budget(project: Path):
    (project / "src" / "beta.py").write_text("def beta():\n    pass\n")
    (project / "src" / "gamma.py").write_text("def gamma():\n    pass\n")
    config, _ = Config.find_and_load(project)
    pricing = get_pricing("anthropic/claude-sonnet-4-6")
    # Tiny budget — first file may complete and overshoot, but subsequent files must skip.
    result = diff_project(
        project_root=project,
        config=config,
        client=StableClient(),
        pricing=pricing,
        budget_usd=0.00001,
    )
    assert len(result.diffs) >= 1
    assert len(result.diffs) < 3
