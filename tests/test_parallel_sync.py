"""Parallel per-symbol sync: the threaded generate phase must produce output
byte-identical to a serial run for the same inputs.

The plan/generate/apply split inside `sync_single_file` only parallelises the
generate phase. `TriefactFile.upsert_section` and `Store.upsert_section_record`
still run on the calling thread in source order. This module pins that contract
so a future refactor that accidentally interleaves writes — or relies on
completion order — fails the suite loudly.
"""

from __future__ import annotations

import shutil
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path

import pytest

from trie.config import Config
from trie.models import ModelResult, SectionBody
from trie.sync.single_file import sync_single_file

FIXTURE_DIR = Path(__file__).parent / "fixtures" / "tiny_repo"


@dataclass
class _DeterministicClient:
    """Stand-in for the LLM. Returns prose keyed on the symbol qname so output is
    a pure function of input — completion order can't shift any byte in the
    resulting triefact. Records observed peak concurrency so the parallel test
    can prove the pool was actually fanned out and not silently serialised."""

    model_id: str = "fake/test"
    in_flight: int = 0
    peak_in_flight: int = 0
    _lock: threading.Lock = field(default_factory=threading.Lock)
    delay_seconds: float = 0.0

    def run(
        self,
        output_type: type,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        with self._lock:
            self.in_flight += 1
            if self.in_flight > self.peak_in_flight:
                self.peak_in_flight = self.in_flight
        try:
            if self.delay_seconds:
                # Hold the slot so >1 worker overlap before any of them returns.
                time.sleep(self.delay_seconds)
            # Key the body on a stable substring of the per-symbol request so two
            # calls for the same qname produce identical text. The qname appears
            # verbatim in `_build_request` output, after "symbol `".
            if "symbol `" in user_prompt:
                qname_marker = user_prompt.split("symbol `")[1].split("`")[0]
            else:
                qname_marker = "?"
            body = f"## `signature`\n\nGenerated body for `{qname_marker}`."
            usage = type(
                "Usage",
                (),
                {
                    "input_tokens": 10,
                    "output_tokens": 20,
                    "details": {
                        "cache_creation_input_tokens": 100,
                        "cache_read_input_tokens": 0,
                    },
                },
            )()
            return ModelResult(output=SectionBody(body=body), usage=usage)
        finally:
            with self._lock:
                self.in_flight -= 1

    def count_tokens(self, system_prompt: str, user_prompt: str) -> int:
        return 100


def _make_project(tmp_path: Path, *, concurrency: int) -> Path:
    root = tmp_path / "demo"
    shutil.copytree(FIXTURE_DIR, root)
    (root / "trie.toml").write_text(
        '[trie]\nversion = "0.1.2"\n'
        '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
        'cascade = "anthropic/claude-sonnet-4-6"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
        f"[sync]\nconcurrency = {concurrency}\n"
    )
    return root


@pytest.fixture
def serial_project(tmp_path: Path) -> Path:
    return _make_project(tmp_path / "serial", concurrency=1)


@pytest.fixture
def parallel_project(tmp_path: Path) -> Path:
    return _make_project(tmp_path / "parallel", concurrency=8)


def test_parallel_output_byte_identical_to_serial(
    serial_project: Path, parallel_project: Path
) -> None:
    """Same inputs + deterministic client must yield the same triefact bytes
    whether we run concurrency=1 or concurrency=8."""
    serial_config, _ = Config.find_and_load(serial_project)
    parallel_config, _ = Config.find_and_load(parallel_project)

    sync_single_file(
        serial_project / "calculator.py",
        project_root=serial_project,
        config=serial_config,
        client=_DeterministicClient(),
    )
    sync_single_file(
        parallel_project / "calculator.py",
        project_root=parallel_project,
        config=parallel_config,
        client=_DeterministicClient(),
    )

    serial_bytes = (serial_project / "triefacts" / "calculator.md").read_bytes()
    parallel_bytes = (parallel_project / "triefacts" / "calculator.md").read_bytes()
    assert serial_bytes == parallel_bytes


def test_parallel_actually_fans_out(parallel_project: Path) -> None:
    """Prove the pool is being used: with concurrency=8 and a small per-call
    delay, more than one worker should be in-flight at the same time. If
    `peak_in_flight` is 1, the parallel path silently collapsed to serial."""
    config, _ = Config.find_and_load(parallel_project)
    client = _DeterministicClient(delay_seconds=0.05)

    result = sync_single_file(
        parallel_project / "calculator.py",
        project_root=parallel_project,
        config=config,
        client=client,
    )

    assert result.symbols_generated >= 2, "fixture should have >=2 symbols"
    assert client.peak_in_flight > 1, (
        f"expected concurrent generate() calls; peak was {client.peak_in_flight}"
    )


def test_serial_never_fans_out(serial_project: Path) -> None:
    """concurrency=1 must serialise even under the same workload — the eval
    determinism case depends on it."""
    config, _ = Config.find_and_load(serial_project)
    client = _DeterministicClient(delay_seconds=0.01)

    sync_single_file(
        serial_project / "calculator.py",
        project_root=serial_project,
        config=config,
        client=client,
    )

    assert client.peak_in_flight == 1


def test_totals_match_between_serial_and_parallel(
    serial_project: Path, parallel_project: Path
) -> None:
    """Token accounting and symbol counts are independent of completion order;
    the apply phase sums them deterministically."""
    serial_config, _ = Config.find_and_load(serial_project)
    parallel_config, _ = Config.find_and_load(parallel_project)

    serial_result = sync_single_file(
        serial_project / "calculator.py",
        project_root=serial_project,
        config=serial_config,
        client=_DeterministicClient(),
    )
    parallel_result = sync_single_file(
        parallel_project / "calculator.py",
        project_root=parallel_project,
        config=parallel_config,
        client=_DeterministicClient(),
    )

    assert serial_result.symbols_generated == parallel_result.symbols_generated
    assert serial_result.sections_removed == parallel_result.sections_removed
    assert serial_result.input_tokens == parallel_result.input_tokens
    assert serial_result.output_tokens == parallel_result.output_tokens
