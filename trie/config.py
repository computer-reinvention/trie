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
class Sync:
    """Per-file sync execution knobs.

    `concurrency` controls how many per-symbol LLM calls run in parallel inside a
    single file's sync. The bottleneck is network I/O so threads are sufficient;
    no asyncio involvement on the call path. Default of 4 is conservative — it
    keeps headroom under Anthropic tier-1 RPM/ITPM ceilings while still giving
    a meaningful speedup over serial. Bump for larger tiers; set to 1 to disable
    parallelism (useful for deterministic eval runs or debugging).

    The retry knobs apply to the underlying model client. `retry_after` headers
    from 429 responses are honoured exactly; for 429s without a header and for
    529s (overloaded), the client backs off `retry_base_delay_seconds * 2**attempt`
    plus jitter, capped at `retry_cap_seconds`, up to `max_retries` attempts before
    propagating the error.
    """

    concurrency: int = 4
    max_retries: int = 5
    retry_base_delay_seconds: float = 1.0
    retry_cap_seconds: float = 60.0


@dataclass
class Debug:
    """Telemetry knobs. Off by default; flipped on for validation runs and dev work.

    The env var `TRIE_DEBUG` overrides `enabled`:
      - `TRIE_DEBUG=1`/`true`/`on`      → force-enabled
      - `TRIE_DEBUG=0`/`false`/`off`    → force-disabled
      - `TRIE_DEBUG=/path/to/log.jsonl` → force-enabled and override `log_path`

    Unset env var means "fall back to the config value." This lets a CI eval
    harness flip telemetry on for a single command (`TRIE_DEBUG=run-7.jsonl trie sync`)
    without editing trie.toml, while still letting a project commit
    `enabled = true` in trie.toml for persistent local dev.
    """

    enabled: bool = False
    log_path: str = "debug.jsonl"  # relative to project root, or absolute
    log_to_stderr: bool = False  # mirror events to stderr; useful in dev, noisy in eval
    capture_args: bool = True  # include MCP tool args in mcp_call events
    capture_responses: bool = False  # include full response bodies (large; off by default)
    redact_keys: list[str] = field(default_factory=list)


@dataclass
class Mcp:
    """Server-side knobs for the MCP agent surface (`locate` / `explain` / `walk`).

    Every field here is implementation detail the agent never sees. They exist so we can
    flip behaviour based on observed agent usage without changing the public contract.
    """

    # locate
    locate_max_limit: int = 50
    locate_one_liner_max_chars: int = 200
    locate_default_rank_by: str = "public_first"
    # When `locate` returns no symbol-name matches, fall back to grepping in-scope
    # source bodies for the `name_contains` string and attributing hits to the
    # symbols whose line ranges enclose them. Two knobs:
    #   - max_files: walk at most this many in-scope files; a runtime guard that
    #     stops the grep walker when the substring is very common. The fallback
    #     still returns whatever was accumulated — never a "too noisy" refusal.
    #   - match_limit: cap on returned candidate symbols after hub-ranking by
    #     inbound count. Defaults to 20 so the agent always sees enough to
    #     triangulate even on broad queries; raw grep would have shown N lines
    #     and we owe at least that floor of utility.
    locate_fallback_max_files: int = 200
    locate_fallback_match_limit: int = 20

    # explain
    explain_neighbour_one_liner_max_chars: int = 120
    explain_max_neighbours_per_direction: int = 0  # 0 = unlimited
    explain_prose_max_chars: int = 0  # 0 = unlimited

    # walk
    walk_max_depth: int = 5
    walk_hub_threshold: int = 20  # mirrors Cascade.hub_symbol_threshold
    walk_max_nodes: int = 200
    walk_prose_at_depth: int = 0  # 0 = no prose on walk
    walk_prose_budget: int = 10


@dataclass
class Config:
    trie: TrieMeta = field(default_factory=TrieMeta)
    scope: Scope = field(default_factory=Scope)
    triefacts: Triefacts = field(default_factory=Triefacts)
    models: Models = field(default_factory=Models)
    cascade: Cascade = field(default_factory=Cascade)
    sync: Sync = field(default_factory=Sync)
    mcp: Mcp = field(default_factory=Mcp)
    debug: Debug = field(default_factory=Debug)

    @classmethod
    def from_dict(cls, data: dict) -> Config:
        return cls(
            trie=TrieMeta(**data.get("trie", {})),
            scope=Scope(**data.get("scope", {})),
            triefacts=Triefacts(**data.get("triefacts", {})),
            models=Models(**data.get("models", {})),
            cascade=Cascade(**data.get("cascade", {})),
            sync=Sync(**data.get("sync", {})),
            mcp=Mcp(**data.get("mcp", {})),
            debug=Debug(**data.get("debug", {})),
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

[sync]
# Parallel per-symbol LLM calls inside a single file's sync. The bottleneck is
# network I/O so threads are sufficient. 4 is conservative under Anthropic tier-1
# RPM/ITPM ceilings; raise for larger tiers, set to 1 to force serial execution.
concurrency = 4
# Retry-on-rate-limit settings for the underlying model client. `retry-after`
# headers from 429s are honoured exactly. For 429s without a header and for
# 529 (overloaded) responses, the client uses exponential backoff with jitter
# (base * 2**attempt + jitter, capped at retry_cap_seconds) for up to
# max_retries attempts before propagating the error.
max_retries = 5
retry_base_delay_seconds = 1.0
retry_cap_seconds = 60.0

[mcp]
# Server-side knobs for the agent surface (`locate` / `explain` / `walk`). These are
# implementation detail — the agent never sees them. Tune to flip behaviour without
# changing the public tool contract.

# locate
locate_max_limit = 50
locate_one_liner_max_chars = 200
locate_default_rank_by = "public_first"        # or "inbound_count" / "alphabetical"

# explain
explain_neighbour_one_liner_max_chars = 120
explain_max_neighbours_per_direction = 0       # 0 = unlimited
explain_prose_max_chars = 0                    # 0 = unlimited

# walk
walk_max_depth = 5
walk_hub_threshold = 20                        # mirrors cascade.hub_symbol_threshold
walk_max_nodes = 200
walk_prose_at_depth = 0                        # 0 = no prose on walk
walk_prose_budget = 10

[debug]
# Append-only JSONL telemetry for trie's own operations. Off by default; flip on
# for validation runs and dev work. Overridable per-invocation via TRIE_DEBUG=1
# or TRIE_DEBUG=/path/to/log.jsonl. See trie/telemetry.py for the event schema.
enabled = false
log_path = "debug.jsonl"                       # relative to project root, or absolute
log_to_stderr = false                          # mirror events to stderr (dev only)
capture_args = true                            # include MCP tool args in events
capture_responses = false                      # include full response bodies (large)
redact_keys = []                               # field paths to elide, e.g. ["args.predicate"]
"""
