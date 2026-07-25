from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class TrieMeta:
    version: str = "0.1.9"


@dataclass
class Scope:
    include: list[str] = field(
        default_factory=lambda: [
            "**/*.py",
            "**/*.ts",
            "**/*.tsx",
        ]
    )
    exclude: list[str] = field(
        default_factory=lambda: [
            "**/.*/**",
            "**/__pycache__/**",
            "**/node_modules/**",
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
    edits: str = "anthropic/claude-sonnet-4-6"


@dataclass
class Cascade:
    default_depth: int = 1
    hub_symbol_threshold: int = 20
    max_judgments: int = 50  # hard cap on pre_filter_cascade calls per apply run
    # Surface second-order cascade (a caller edit that itself changed a signature)
    # as ApplyReport.unresolved rather than chasing it in-pipeline. Single sweep.
    surface_unresolved: bool = True


@dataclass
class LspBackend:
    """A language server / checker invoked for diagnostics during patch apply.

    `command` is the binary name (resolved via shutil.which).
    `check_args` are CLI flags passed before the file path.
    `output_format` is one of "pyright" or "ruff" — determines how
    stdout is parsed into our normalised diagnostic format:
      {line, column, code, message}[]
    `exit_ok_codes` — list of exit codes that mean "no diagnostics."
    Pyright exits 0 even with diagnostics when it's just warnings;
    we always read stdout regardless of exit code.
    """

    command: str
    check_args: list[str] = field(default_factory=list)
    output_format: str = "pyright"
    exit_ok_codes: list[int] = field(default_factory=lambda: [0])


@dataclass
class Edits:
    """Settings for the patch-apply pipeline and LSP diagnostics."""

    lsp_max_retries: int = 3
    lsp_backends: list[LspBackend] = field(
        default_factory=lambda: [
            LspBackend(command="pyright", check_args=["--outputjson"], output_format="pyright"),
        ]
    )
    # Per-symbol edit generation backend:
    #   "llm"      (default) — in-process LLM code generation
    #   "opencode" — one targeted opencode instance per symbol (Phase 2)
    #   "agent"    — patch apply returns an agent-executable worklist (workorder)
    #                instead of generating code; generation becomes opt-in at the
    #                call site. A repo opts into this flow by setting backend = "agent".
    # See trie/edits/backends.
    backend: str = "llm"
    # How a multi-item apply commits on partial failure:
    #   "all_or_nothing" (default) — any item failing aborts the whole commit
    #   "per_item"   — commit items that passed; failed items go to unresolved
    #   "per_group"  — commit coherent groups that fully pass
    commit_mode: str = "all_or_nothing"
    # Max regeneration attempts for a symbol whose generated source won't compile,
    # before surfacing it in ApplyReport.unresolved with the failed source verbatim.
    compile_retry_cap: int = 2
    # How many times pydantic-ai may re-ask the model when its STRUCTURED output
    # fails to parse/validate (separate from network retries). The library
    # defaults to 1, which makes a single malformed structured response abort the
    # whole apply ("Exceeded maximum output retries"). Large symbols (e.g. a long
    # React component regenerated as one source string) trip this; give the model
    # a few chances to return well-formed output before failing the symbol.
    output_retries: int = 3
    # Max output tokens for a code-generation call (per-symbol body, whole-file
    # regeneration, or LSP fixup). The model supports far more (Sonnet 4.x: 64K);
    # a low cap silently TRUNCATES the structured tool-call JSON mid-string on any
    # non-trivial symbol, which surfaces as "Exceeded maximum output retries" and
    # aborts the apply. Set generously so regenerating a large file/component fits
    # in one response. You pay only for tokens actually produced, so a high ceiling
    # costs nothing on small symbols.
    max_output_tokens: int = 16384


@dataclass
class LanguageConfig:
    """Per-language overrides, keyed by backend name (e.g. "typescript").

    `lsp_backends`, when non-empty, replaces the language backend's built-in
    default checkers for the edit pipeline. Other per-language knobs can be
    added here without touching the global config shape.
    """

    lsp_backends: list[LspBackend] = field(default_factory=list)


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
    max_retries: int = 8
    retry_base_delay_seconds: float = 1.0
    retry_cap_seconds: float = 60.0

    # Per-request timeout (seconds) for a single LLM call. Without an explicit
    # timeout a stalled connection (no response, half-open socket) makes the
    # async request — and the worker thread driving it — block forever, so the
    # file never finishes and the sync appears to hang. With a bound the request
    # raises APITimeoutError, which the retry loop catches and retries, then
    # ultimately surfaces as a per-file error instead of an indefinite spin.
    request_timeout_seconds: float = 120.0

    # Wave-based cross-file parallelism. `file_workers` is how many files the
    # scheduler generates concurrently; within each file, `concurrency` symbols
    # run in parallel. The product can exceed the provider's rate ceiling, so
    # `max_inflight_requests` is a process-wide semaphore capping the TOTAL
    # number of concurrent LLM calls regardless of how files/symbols fan out.
    # It is the real throttle: set it to your tier's safe concurrency and let
    # the 429 backoff absorb the rest. 0 disables the global cap.
    file_workers: int = 8
    max_inflight_requests: int = 8


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
    """Server-side knobs for the MCP agent surface (`grep` / `read` / `trace`).

    Every field here is implementation detail the agent never sees. They exist so we can
    flip behaviour based on observed agent usage without changing the public contract.
    """

    # grep
    grep_max_limit: int = 50
    grep_one_liner_max_chars: int = 200
    grep_default_rank_by: str = "public_first"
    # When `grep` returns no symbol-name matches, fall back to ripgrep
    # against in-scope source bodies and attribute hits to the symbols whose
    # line ranges enclose them. Two knobs:
    #   - max_files: walk at most this many in-scope files; a runtime guard that
    #     stops the rg walker when the substring is very common. The fallback
    #     still returns whatever was accumulated — never a "too noisy" refusal.
    #   - match_limit: cap on returned candidate symbols after hub-ranking by
    #     inbound count. Defaults to 30 so the agent sees enough to triangulate
    #     even on broad queries; raw shell grep would have shown N lines and we
    #     owe at least that floor of utility. The `match_count` / `unique_symbols`
    #     fields tell the agent how many candidates exist beyond the cap.
    grep_fallback_max_files: int = 200
    grep_fallback_match_limit: int = 30

    # fuzzy matching (rapidfuzz-based, applied across grep / grep_symbol /
    # grep_entry_points / grep_str fallback)
    #   - fuzzy_cutoff: minimum rapidfuzz WRatio score (0-100) for a hit to
    #     be included in any fuzzy result list. 45 is looser than the old
    #     difflib default of 60 and better handles short-name typos.
    #   - fuzzy_prose_pre_filter: minimum score a symbol must reach on name
    #     or one_liner alone before we read its triefact prose from disk.
    #     Guards against O(N) disk reads on large repos.
    #   - fuzzy_prose_window: characters of prose body fed to the scorer.
    #     Extends the old hardcoded 500-char limit.
    #   - fuzzy_prose_weight: multiplier applied to the prose-derived score
    #     before taking max with name/one_liner score, so a prose-only match
    #     ranks slightly below a name match of the same raw ratio.
    fuzzy_cutoff: float = 45.0
    fuzzy_prose_pre_filter: float = 30.0
    fuzzy_prose_window: int = 2000
    fuzzy_prose_weight: float = 0.6

    # read
    read_neighbour_one_liner_max_chars: int = 120
    read_max_neighbours_per_direction: int = 0  # 0 = unlimited
    read_prose_max_chars: int = 0  # 0 = unlimited

    # trace
    trace_max_depth: int = 5
    trace_hub_threshold: int = 50  # skip expanding symbols with >50 inbound refs during
    # trace/trace_flow so navigation never fans out through utility hubs. Higher than the
    # cascade guard (20) because read-side traversal tolerates more breadth than write-side
    # regen; set very high to effectively disable hub skipping.
    trace_max_nodes: int = 200
    trace_prose_at_depth: int = 0  # 0 = no prose on trace
    trace_prose_budget: int = 10


@dataclass
class Diff:
    """Config surface for the committed trie-diff digest system.

    Every digest write produces one immutable file under `diffs_dir`, named
    `<utc-timestamp>-<uuid>.md`, and repoints the `write_path` symlink at it.
    One file per commit means a PR's digest always appears as a brand-new
    file — pure additions, never a diff-of-a-diff. An amend/retry of the same
    commit rewrites that commit's existing file instead of creating another.
    """

    narrative: bool = True
    """Synthesise an LLM narrative at the top of each digest entry; falls back
    to deterministic evidence when the client/key is unavailable."""

    write_path: str = "TRIE_DIFF.md"
    """Symlink at the project root pointing at the latest digest file under
    `diffs_dir`. The pre-commit hook block hardcodes the default names, so
    changing these requires editing the hook."""

    diffs_dir: str = "triefacts/triediffs"
    """Directory (relative to project root) holding one digest file per
    commit. It lives inside the triefact tree, so digest evidence collection
    explicitly excludes it — previous digests never feed back into new
    ones."""

    max_entries: int = 20
    """Retention cap: keep at most this many digest files in `diffs_dir`;
    the oldest are pruned (they remain in git history)."""


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
    edits: Edits = field(default_factory=Edits)
    diff: Diff = field(default_factory=Diff)
    languages: dict[str, LanguageConfig] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> Config:
        raw_edits = dict(data.get("edits", {}))
        backends_raw = raw_edits.pop("lsp_backends", None)
        if backends_raw is not None:
            raw_edits["lsp_backends"] = [LspBackend(**b) for b in backends_raw]
        languages: dict[str, LanguageConfig] = {}
        for name, raw in (data.get("languages", {}) or {}).items():
            raw = dict(raw)
            lb = raw.pop("lsp_backends", None)
            languages[name] = LanguageConfig(
                lsp_backends=[LspBackend(**b) for b in lb] if lb else [],
            )
        return cls(
            trie=TrieMeta(**data.get("trie", {})),
            scope=Scope(**data.get("scope", {})),
            triefacts=Triefacts(**data.get("triefacts", {})),
            models=Models(**data.get("models", {})),
            cascade=Cascade(**data.get("cascade", {})),
            sync=Sync(**data.get("sync", {})),
            mcp=Mcp(**data.get("mcp", {})),
            debug=Debug(**data.get("debug", {})),
            edits=Edits(**raw_edits),
            diff=Diff(**data.get("diff", {})),
            languages=languages,
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
version = "0.1.9"

[scope]
# Glob patterns relative to the project root (the directory containing this file).
# Defaults cover every language trie has a parser backend for (Python +
# TypeScript/TSX). Trim this list to just the extensions your project uses to
# keep discovery fast and sync cost down.
# Tests are included by default — they encode behavioral spec worth documenting.
# Add `"**/tests/**"` to `exclude` if you'd rather skip them to keep cost down.
include = ["**/*.py", "**/*.ts", "**/*.tsx"]
# `**/.*/**` prunes every hidden directory (.git, .trie, .venv, .opencode,
# .vscode, …) — none of those are project source.
exclude = [
    "**/.*/**",
    "**/__pycache__/**",
    "**/node_modules/**",
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
edits = "anthropic/claude-sonnet-4-6"

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
# Wave-based cross-file parallelism. `file_workers` files generate concurrently;
# `max_inflight_requests` is a process-wide cap on TOTAL concurrent LLM calls
# (the real throttle — set to your tier's safe concurrency; 0 disables the cap).
file_workers = 8
max_inflight_requests = 8
# Retry-on-rate-limit settings for the underlying model client. `retry-after`
# headers from 429s are honoured exactly. For 429s without a header and for
# 529 (overloaded) responses, the client uses exponential backoff with jitter
# (base * 2**attempt + jitter, capped at retry_cap_seconds) for up to
# max_retries attempts before propagating the error.
max_retries = 8
retry_base_delay_seconds = 1.0
retry_cap_seconds = 60.0

[mcp]
# Server-side knobs for the agent surface (`grep` / `read` / `trace`). These are
# implementation detail — the agent never sees them. Tune to flip behaviour without
# changing the public tool contract.

# grep
grep_max_limit = 50
grep_one_liner_max_chars = 200
grep_default_rank_by = "public_first"          # or "inbound_count" / "alphabetical"

# read
read_neighbour_one_liner_max_chars = 120
read_max_neighbours_per_direction = 0          # 0 = unlimited
read_prose_max_chars = 0                       # 0 = unlimited

# trace
trace_max_depth = 5
trace_hub_threshold = 50                       # skip hubs >50 inbound in trace/trace_flow
trace_max_nodes = 200
trace_prose_at_depth = 0                       # 0 = no prose on trace
trace_prose_budget = 10

[edits]
# Patch-apply pipeline settings.
lsp_max_retries = 3

# Ordered list of LSP backends for source diagnostics during apply.
# The first backend on PATH wins; its diagnostics are fed to the fixup loop.
# Each entry: {command, check_args?, output_format?, exit_ok_codes?}.
# Supported output_formats: "pyright" (--outputjson), "ruff" (--output-format json).
# Add more backends (or replace pyright with ruff) by editing this list.
[[edits.lsp_backends]]
command = "pyright"
check_args = ["--outputjson"]
output_format = "pyright"

# [diff]
# narrative = true          # LLM narrative at the top of each digest entry (falls back to raw evidence without an API key)
# write_path = "TRIE_DIFF.md"  # root symlink pointing at the latest digest file
# diffs_dir = "triefacts/triediffs"  # one immutable digest file per commit lives here
# max_entries = 20          # keep at most this many digest files; oldest pruned

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
