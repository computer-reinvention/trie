from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TrieMeta:
    version: str = "0.1.0"


@dataclass
class Scope:
    include: list[str] = field(default_factory=lambda: ["**/*.py"])
    exclude: list[str] = field(
        default_factory=lambda: [
            "**/__pycache__/**",
            "**/.venv/**",
            "**/build/**",
            "**/dist/**",
        ]
    )


@dataclass
class Triefacts:
    root: str = "triefacts"
    source_root: str = "."


@dataclass
class Models:
    bootstrap: str = "anthropic/claude-sonnet-4-6"
    cascade: str = "anthropic/claude-sonnet-4-6"


@dataclass
class Cascade:
    default_depth: int = 1
    hub_symbol_threshold: int = 20


@dataclass
class Config:
    trie: TrieMeta = field(default_factory=TrieMeta)
    scope: Scope = field(default_factory=Scope)
    triefacts: Triefacts = field(default_factory=Triefacts)
    models: Models = field(default_factory=Models)
    cascade: Cascade = field(default_factory=Cascade)

    @classmethod
    def from_dict(cls, data: dict) -> Config:
        return cls(
            trie=TrieMeta(**data.get("trie", {})),
            scope=Scope(**data.get("scope", {})),
            triefacts=Triefacts(**data.get("triefacts", {})),
            models=Models(**data.get("models", {})),
            cascade=Cascade(**data.get("cascade", {})),
        )

    @classmethod
    def load(cls, path: Path) -> Config:
        with path.open("rb") as f:
            data = tomllib.load(f)
        return cls.from_dict(data)

    @classmethod
    def find_and_load(cls, start: Path) -> tuple[Config, Path]:
        """Walk up from `start` looking for trie.toml.

        Returns (config, config_dir) where config_dir is the directory containing trie.toml —
        used as the project root for resolving relative paths in scope/triefacts.
        """
        current = start.resolve()
        for d in (current, *current.parents):
            candidate = d / "trie.toml"
            if candidate.exists():
                return cls.load(candidate), d
        raise ConfigNotFoundError(
            f"No trie.toml found in {start} or any parent directory. Run `trie init` to create one."
        )


class ConfigNotFoundError(FileNotFoundError):
    pass


DEFAULT_CONFIG_TOML = """\
# trie configuration — see https://github.com/pankajgarkoti/trie

[trie]
version = "0.1.0"

[scope]
# Glob patterns relative to the project root (the directory containing this file).
# Tests are included by default — they encode behavioral spec worth documenting.
# Add `"**/tests/**"` to `exclude` if you'd rather skip them to keep cost down.
include = ["**/*.py"]
exclude = [
    "**/__pycache__/**",
    "**/.venv/**",
    "**/build/**",
    "**/dist/**",
]

[triefacts]
# Where the generated Markdown triefact tree lives. Mirrors the source tree under this root.
# Named `triefacts` (not `docs`) to avoid colliding with existing project docs dirs.
root = "triefacts"
# Source tree root, relative to this file. "." means the project root.
source_root = "."

[models]
# Default models for triefact generation. Use "anthropic/<model>" or "openai/<model>" form.
# Switch to a cheaper provider by changing these to e.g. "openai/deepseek-chat" with
# DEEPSEEK_API_BASE / OPENAI_API_KEY env vars set, or use --model on the CLI.
bootstrap = "anthropic/claude-sonnet-4-6"
cascade = "anthropic/claude-sonnet-4-6"

[cascade]
# Default reference-graph traversal depth on incremental sync.
default_depth = 1
# Symbols with more inbound references than this are treated as depth-0 only,
# preventing utility hubs (utils.py, common types) from invalidating the world.
hub_symbol_threshold = 20
"""
