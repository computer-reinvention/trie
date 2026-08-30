from __future__ import annotations

import asyncio
import functools
import random
import sys
import threading
import time
from collections.abc import Callable, Iterator
from contextlib import contextmanager, suppress
from types import SimpleNamespace
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field

from trie import telemetry
from trie.config import Sync

if TYPE_CHECKING:
    from anthropic import APIStatusError, AsyncAnthropic
    from pydantic_ai.models.anthropic import AnthropicModel
    from pydantic_ai.usage import RunUsage as Usage


@functools.cache
def _sdk() -> SimpleNamespace:
    """Import the LLM SDK stack (anthropic + pydantic_ai) on first use.

    These imports cost ~1.2s of wall clock — more than every read-only trie
    command combined. Importing them eagerly at module top made `trie grep`
    pay for an LLM client it never constructs (this module is reached from
    cli.py via the sync/diff import chains). Everything network-flavoured is
    accessed through this cached loader instead; the first actual LLM call
    pays the cost, pure-read commands never do.
    """
    from anthropic import (
        Anthropic,
        APIConnectionError,
        APIStatusError,
        APITimeoutError,
        AsyncAnthropic,
        InternalServerError,
        RateLimitError,
        Timeout,
    )
    from pydantic_ai import Agent, CachePoint
    from pydantic_ai.exceptions import ModelAPIError
    from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings
    from pydantic_ai.providers.anthropic import AnthropicProvider

    try:
        # pydantic_ai >= 0.1 renamed Usage to RunUsage; the old name was kept
        # as a deprecated alias and then removed. Prefer the new name, fall
        # back for older installs.
        from pydantic_ai.usage import RunUsage as Usage
    except ImportError:  # pragma: no cover — depends on installed pydantic_ai
        from pydantic_ai.usage import Usage  # type: ignore[no-redef,attr-defined]

    return SimpleNamespace(
        Timeout=Timeout,
        Anthropic=Anthropic,
        AsyncAnthropic=AsyncAnthropic,
        APIStatusError=APIStatusError,
        Agent=Agent,
        CachePoint=CachePoint,
        ModelAPIError=ModelAPIError,
        AnthropicModel=AnthropicModel,
        AnthropicModelSettings=AnthropicModelSettings,
        AnthropicProvider=AnthropicProvider,
        Usage=Usage,
        retryable_anthropic=(
            RateLimitError,
            InternalServerError,
            APITimeoutError,
            APIConnectionError,
        ),
        RateLimitError=RateLimitError,
        InternalServerError=InternalServerError,
        APITimeoutError=APITimeoutError,
    )


# Per-thread event loop AND per-thread async HTTP client.
#
# Two intertwined constraints force this design:
#
#   1. fd leak. ``Agent.run_sync`` (and a fresh client per call) creates a new
#      event loop / socketpair every call; under the parallel sync fan-out these
#      accumulate faster than GC reclaims them and we hit ``OSError: [Errno 24]
#      Too many open files``. So loops and clients must be *reused*, not per-call.
#
#   2. event-loop affinity. An ``httpx.AsyncClient`` (and thus the AsyncAnthropic
#      wrapping it) is bound to the event loop it is first used on — its pool
#      holds loop-bound locks/transports. Sync drives requests from many worker
#      threads, EACH with its own loop, so a single shared client used across
#      threads raises an immediate "Connection error" the moment a second loop
#      touches it. (This is the regression that replaced the old hang.)
#
# The reconciliation: one loop AND one model/client *per thread*, paired in a
# holder. A thread allocates them once and reuses them for every symbol it
# generates — bounded by thread count (no fd leak) and never shared across loops
# (no cross-loop corruption). The holder's ``__del__`` closes both when the
# owning thread dies; CPython runs that finaliser when the thread's thread-local
# storage is released at thread exit, so the short-lived nested ThreadPools that
# churn workers don't leak.
class _LoopHolder:
    __slots__ = ("aclient", "loop", "model")

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        model: AnthropicModel,
        aclient: AsyncAnthropic,
    ) -> None:
        self.loop = loop
        self.model = model
        # Public so the plaintext code-gen path (TrieClient.run_text) can drive
        # this thread's loop-bound AsyncAnthropic directly with messages.create,
        # reusing the same per-thread loop/client as the structured run() path.
        self.aclient = aclient

    def __del__(self) -> None:
        # Close the async client on its own loop (closing its connection pool)
        # before closing the loop itself. Best-effort throughout: thread teardown
        # must never raise.
        loop = self.loop
        with suppress(Exception):
            if loop is not None and not loop.is_closed():
                if self.aclient is not None:
                    with suppress(Exception):
                        loop.run_until_complete(self.aclient.close())
                loop.close()


_thread_local = threading.local()


def _thread_holder(make_model: Callable[[], tuple[AnthropicModel, AsyncAnthropic]]) -> _LoopHolder:
    """Return this thread's loop+model holder, creating it on first use.

    ``make_model`` builds a fresh AnthropicModel + its AsyncAnthropic client bound
    to this thread's loop; it is only called when this thread has no live holder
    yet, so each thread gets exactly one client bound to its own loop. Reused for
    every subsequent call on the thread (no fd leak), never shared across loops
    (no cross-loop "Connection error").
    """
    holder = getattr(_thread_local, "loop_holder", None)
    if holder is None or holder.loop.is_closed():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        model, aclient = make_model()
        holder = _LoopHolder(loop, model, aclient)
        _thread_local.loop_holder = holder
    return holder


# ---------------------------------------------------------------------------
# Global in-flight request governor.
#
# Wave-based sync over-subscribes worker threads (file_workers x per-file
# concurrency) deliberately, so the actual throttle is this process-wide
# semaphore that caps the number of LLM calls hitting the provider at once.
# It is acquired per network attempt (not across retry sleeps), so a backed-off
# request frees its slot for someone else while it waits out a 429.
#
# Lazily (re)sized: `configure_inflight_limit(n)` is idempotent and only rebuilds
# the semaphore when the bound changes. A bound of 0 means "no cap".
# ---------------------------------------------------------------------------
_inflight_lock = threading.Lock()
_inflight_sem: threading.BoundedSemaphore | None = None
_inflight_bound: int = 0


def configure_inflight_limit(bound: int) -> None:
    """Set the global cap on concurrent LLM requests. 0 disables the cap.

    Idempotent: re-calling with the same bound is a no-op. Safe to call from the
    sync entrypoint before fanning out workers.
    """
    global _inflight_sem, _inflight_bound
    with _inflight_lock:
        if bound == _inflight_bound:
            return
        _inflight_bound = bound
        _inflight_sem = threading.BoundedSemaphore(bound) if bound > 0 else None


@contextmanager
def _inflight_slot() -> Iterator[None]:
    """Hold one global request slot for the duration of a single network attempt."""
    sem = _inflight_sem
    if sem is None:
        yield
        return
    sem.acquire()
    try:
        yield
    finally:
        sem.release()


# ---------------------------------------------------------------------------
# Structured output models — every LLM call returns one of these.
# No delimiter-parsing, no "Output:\n```python\n..." instructions.
# ---------------------------------------------------------------------------


class SectionBody(BaseModel):
    """Triefact documentation body for a single symbol, plus its architectural role."""

    body: str
    role: str = Field(
        default="",
        description=(
            "A single lowercase role tag classifying this symbol's architectural "
            "function in the codebase. Prefer one of the standard roles: "
            "'entrypoint' (CLI/main/server bootstrap), 'api' (request handlers, "
            "public interface surface), 'domain' (core business logic and rules), "
            "'persistence' (database/storage/serialization), 'io' (filesystem, "
            "network, subprocess, external services), 'parsing' (lexing/AST/"
            "deserialization of inputs), 'model' (data structures, schemas, "
            "dataclasses, types), 'config' (settings, environment, configuration), "
            "'orchestration' (pipelines, schedulers, coordinators that wire other "
            "components together), 'util' (small reusable helpers), 'test' (test "
            "code and fixtures). If none of these fit, coin a concise "
            "project-specific role (one or two lowercase words, hyphenated). "
            "Choose the single most specific role for what this symbol primarily does."
        ),
    )
    boundary: str = Field(
        default="internal",
        description=(
            "Where this symbol sits relative to the system's boundary with the "
            "outside world. One of exactly: 'entry' — execution enters the system "
            "here from outside (CLI commands, HTTP/route handlers, framework "
            "callbacks, public tool/RPC methods invoked by an agent or client, "
            "main/run entry functions); 'exit' — the symbol's primary job is to "
            "reach OUT of the system (spawn a subprocess, open a socket or network "
            "request, read/write the filesystem, call an external API or LLM "
            "client); 'internal' — neither; it is called by and calls other "
            "in-project code. Judge by the symbol's actual purpose in the source, "
            "not just its name. When a symbol both is invoked from outside and "
            "reaches outside, prefer 'entry'. Most symbols are 'internal'."
        ),
    )


class ProposedRole(BaseModel):
    """One role in a derived, project-specific role taxonomy."""

    name: str = Field(
        description=(
            "A short lowercase role name (one or two words, hyphenated if two), e.g. "
            "'request-handler', 'persistence', 'parser'. Names must be distinct and "
            "non-overlapping within the taxonomy."
        )
    )
    description: str = Field(
        description=(
            "One sentence defining what kind of symbol belongs to this role, concrete "
            "enough that a classifier can decide membership unambiguously."
        )
    )


class RoleTaxonomy(BaseModel):
    """A coherent, project-specific set of architectural roles derived by trie.

    Pass 1 of role tagging: rather than letting each symbol pick an arbitrary role
    in isolation (which yields an incoherent long tail of near-synonyms), trie
    surveys the whole codebase once and has the model propose a small fixed
    vocabulary fitted to THIS project. Pass 2 then classifies every symbol against
    exactly these names.
    """

    roles: list[ProposedRole] = Field(
        description=(
            "The complete role vocabulary for this codebase. Prefer 6-14 roles: enough "
            "to capture the real architectural divisions, few enough to stay legible. "
            "Cover every major kind of work the codebase does; avoid redundant or "
            "overlapping roles."
        )
    )


class RoleTag(BaseModel):
    """Classification of a single symbol against a fixed role vocabulary.

    Pass 2 of role tagging, and the unit of `trie sync --roles-only`. The allowed
    role names are injected into the prompt at call time (from the derived
    `RoleTaxonomy`), so this model intentionally carries no hardcoded vocabulary —
    `role` must be one of the names the prompt lists. `boundary` reuses the static
    entry/exit/internal classification shared with `SectionBody`.
    """

    role: str = Field(
        default="",
        description=(
            "The single best-fitting role for this symbol. Must be exactly one of the "
            "role names listed in the prompt's taxonomy — do not invent new names."
        ),
    )
    boundary: str = Field(
        default="internal", description=SectionBody.model_fields["boundary"].description
    )


class MergeNotesOutput(BaseModel):
    """Deduplicated patch notes."""

    notes: list[str]
    reasons: list[str]


class SymbolEdit(BaseModel):
    """Updated source code and prose for one symbol."""

    source: str
    prose: str


class SymbolProse(BaseModel):
    """Prose for one symbol within a multi-symbol file edit."""

    qname: str
    prose: str


class FileEdit(BaseModel):
    """Updated file content with per-symbol prose."""

    content: str
    prose: list[SymbolProse]


class CallerDecision(BaseModel):
    """Decision for one callee→caller relationship."""

    caller_qname: str
    action: str = "skip"
    note: str = ""
    reason: str = ""


class BatchFilterOutput(BaseModel):
    """Batch filter decisions for all callee→caller pairs.

    ``decisions`` defaults to an empty list so a model reply of ``{}`` (which
    happens when it judges that no caller needs updating) validates instead of
    raising a pydantic ``ValidationError`` → ``UnexpectedModelBehavior`` that
    aborts the whole apply. An empty decision set is the correct, safe meaning:
    "no callers need to change."
    """

    decisions: list[CallerDecision] = Field(default_factory=list)


class FixupOutput(BaseModel):
    """Corrected file content after diagnostics."""

    content: str


# ---------------------------------------------------------------------------
# Result wrapper — structured output + token usage
# ---------------------------------------------------------------------------


class ModelResult:
    """Holds a structured Pydantic output plus token usage counters.

    Replace the old ``GenerationResponse`` — callers get typed data and
    usage in one object instead of raw text that needs fragile parsing.
    """

    def __init__(self, output: BaseModel, usage: Usage) -> None:
        self._output = output
        self._usage = usage

    @property
    def output(self) -> Any:
        return self._output

    @property
    def input_tokens(self) -> int:
        return self._usage.input_tokens

    @property
    def output_tokens(self) -> int:
        return self._usage.output_tokens

    @property
    def cache_creation_input_tokens(self) -> int:
        d = self._usage.details or {}
        return d.get("cache_creation_input_tokens", 0) or 0

    @property
    def cache_read_input_tokens(self) -> int:
        d = self._usage.details or {}
        return d.get("cache_read_input_tokens", 0) or 0


# ---------------------------------------------------------------------------
# Internal helpers: retry with backoff (kept from old AnthropicClient for
# use in the count_tokens path, which still hits the raw Anthropic SDK).
# ---------------------------------------------------------------------------


def _retry_after_seconds(exc: APIStatusError) -> float | None:
    response = getattr(exc, "response", None)
    if response is None:
        return None
    raw = response.headers.get("retry-after")
    if raw is None:
        return None
    try:
        return max(0.0, float(raw))
    except (TypeError, ValueError):
        return None


def _is_retryable(exc: BaseException) -> bool:
    # Direct anthropic exceptions: APIConnectionError covers transient network
    # failures (DNS lookup failure, connection refused, reset) and is the parent
    # of APITimeoutError; RateLimitError/InternalServerError cover 429/529.
    #
    # pydantic-ai wraps the underlying anthropic exception in its own
    # ModelAPIError, so a transient connection drop arrives as a ModelAPIError
    # ("Connection error.") that does NOT isinstance-match the anthropic types —
    # which is why these were surfaced immediately as a per-file failure instead
    # of being retried. We therefore (a) walk the __cause__/__context__ chain for
    # a retryable anthropic exception, and (b) treat a bare ModelAPIError whose
    # message names a connection/timeout as retryable.
    seen: set[int] = set()
    cur: BaseException | None = exc
    while cur is not None and id(cur) not in seen:
        seen.add(id(cur))
        if isinstance(cur, _sdk().retryable_anthropic):
            return True
        if isinstance(cur, _sdk().ModelAPIError):
            msg = str(cur).lower()
            if "connection error" in msg or "timed out" in msg or "timeout" in msg:
                return True
        cur = cur.__cause__ or cur.__context__
    return False


def _backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float:
    window = min(cap, base * (2**attempt))
    return rng.uniform(0.0, window)


def _run_with_retry(
    fn: Callable[[], T],
    *,
    cfg: Sync,
    kind: str,
    model_id: str,
    sleep: Callable[[float], None] = time.sleep,
    rng: random.Random | None = None,
) -> T:
    rng = rng or random.Random()
    attempt = 0
    started = time.monotonic()
    budget = getattr(cfg, "retry_total_seconds", 0.0) or 0.0
    while True:
        try:
            return fn()
        except BaseException as exc:
            if not _is_retryable(exc) or attempt >= cfg.max_retries:
                raise
            if budget > 0 and time.monotonic() - started >= budget:
                print(
                    f"trie: giving up on {kind} call after {time.monotonic() - started:.0f}s "
                    f"of retries ({attempt + 1} attempt(s)): {type(exc).__name__}",
                    file=sys.stderr,
                )
                raise
            if isinstance(exc, _sdk().RateLimitError):
                hinted = _retry_after_seconds(exc)
                delay = (
                    hinted
                    if hinted is not None
                    else _backoff_delay(
                        attempt=attempt,
                        base=cfg.retry_base_delay_seconds,
                        cap=cfg.retry_cap_seconds,
                        rng=rng,
                    )
                )
                reason = "rate_limit"
            else:
                delay = _backoff_delay(
                    attempt=attempt,
                    base=cfg.retry_base_delay_seconds,
                    cap=cfg.retry_cap_seconds,
                    rng=rng,
                )
                if isinstance(exc, _sdk().InternalServerError):
                    reason = "overloaded"
                elif isinstance(exc, _sdk().APITimeoutError):
                    reason = "timeout"
                else:
                    reason = "connection"
            delay = min(delay, cfg.retry_cap_seconds)
            telemetry.emit(
                "model_call_retry",
                model=model_id,
                kind=kind,
                attempt=attempt,
                delay_seconds=round(delay, 3),
                reason=reason,
                exception=type(exc).__name__,
            )
            # Retries were previously invisible outside debug.jsonl — a wedged
            # network looked like a silent hang. One concise line per retry.
            print(
                f"trie: model call retry #{attempt + 1} ({reason}, {type(exc).__name__}) — "
                f"waiting {delay:.1f}s",
                file=sys.stderr,
            )
            sleep(delay)
            attempt += 1


T = Any  # TypeVar placeholder for the inner retry helper


# ---------------------------------------------------------------------------
# Client — Pydantic AI agent factory with a count_tokens side-channel
# ---------------------------------------------------------------------------

# Map from trie's "provider/model" config format to pydantic_ai's "provider:model" format.
# Only needed for model ids whose pydantic_ai form differs from a plain `/`→`:`
# swap. `claude-sonnet-4-6` is a real Anthropic model id and must pass through
# untouched — the previous alias rewrote it to the now-deprecated dated snapshot
# `claude-sonnet-4-20250514`, which 404s.
_MODEL_ID_ALIASES: dict[str, str] = {}


def _pydantic_ai_model_id(full_model_id: str) -> str:
    """Convert trie's ``provider/model`` model ID to pydantic_ai's ``provider:model``."""
    return _MODEL_ID_ALIASES.get(full_model_id) or full_model_id.replace("/", ":", 1)


def _anthropic_model_name(full_model_id: str) -> str:
    """Extract the bare Anthropic model name from a full trie model ID."""
    if "/" in full_model_id:
        return full_model_id.split("/", 1)[1]
    return full_model_id


class TrieClient:
    """Pydantic AI-powered LLM client.

    ``run()`` creates a one-shot ``Agent`` with ``output_type`` and
    ``system_prompt`` and drives it via ``agent.run`` on a per-thread event loop
    (never ``run_sync`` — see ``_thread_holder`` for the fd-leak reasoning),
    returning a ``ModelResult`` with the output and token usage. Pass
    ``output_type=str`` (or use ``run_text``) for plain-text/code generation.

    ``count_tokens()`` still uses the Anthropic SDK ``count_tokens`` endpoint
    (free, no generation) to estimate prompt sizes before a run.
    """

    def __init__(
        self,
        full_model_id: str,
        *,
        sync_cfg: Sync | None = None,
    ) -> None:
        self.full_model_id = full_model_id
        self._pai_model_id = _pydantic_ai_model_id(full_model_id)
        self._anthropic_model = _anthropic_model_name(full_model_id)
        self._sync_cfg = sync_cfg or Sync()
        timeout = self._sync_cfg.request_timeout_seconds
        # Bounded per-request timeout. Without it a stalled connection makes the
        # request block forever; the worker thread driving it never returns, the
        # file never finishes, and the whole sync hangs (observed: 3 of 18 cascade
        # files spinning with zero telemetry for minutes). A read/connect/write/pool
        # timeout turns that into an APITimeoutError that _run_with_retry retries
        # and ultimately surfaces as a per-file error instead of an infinite spin.
        #
        # Use *anthropic.Timeout* (the SDK's own re-export) — NOT a raw
        # httpx.Timeout. Anthropic >= 1.0 migrated its transport from httpx to
        # httpx2; constructing a timeout with the wrong library's Timeout class
        # causes a TypeError at socket level, surfaced as APIConnectionError.
        self._http_timeout = _sdk().Timeout(timeout, connect=min(30.0, timeout))
        self._anthropic_model_name = self._pai_model_id.split(":", 1)[-1]
        # The sync count_tokens client lives on the main thread and is only used
        # synchronously, so a single instance is fine here.
        self._raw_client = _sdk().Anthropic(max_retries=0, timeout=self._http_timeout)

    def _make_thread_model(self) -> tuple[AnthropicModel, AsyncAnthropic]:
        """Build a fresh AnthropicModel + AsyncAnthropic for the CURRENT thread.

        Each worker thread runs its own event loop, and an httpx.AsyncClient is
        bound to the loop it's first used on — so the client (and the model
        wrapping it) must be created per thread, not shared. _thread_holder calls
        this once per thread and caches the result, giving us one client per
        thread (no fd leak) that never crosses event loops (no "Connection
        error"). The timeout is plumbed in so stalled requests still abort.
        """
        async_client = _sdk().AsyncAnthropic(max_retries=0, timeout=self._http_timeout)
        model = _sdk().AnthropicModel(
            self._anthropic_model_name,
            provider=_sdk().AnthropicProvider(anthropic_client=async_client),
        )
        return model, async_client

    def run(
        self,
        output_type: type[BaseModel] | type[str],
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
        cache_prefix: str | None = None,
        output_retries: int = 3,
    ) -> ModelResult:
        """Run an agent with structured output.

        Passing ``output_type=str`` selects pydantic-ai's plain-text output mode:
        the model replies with free text (no JSON schema, no tool call) and
        ``result.output`` is the raw string. The code-generation path uses this
        via ``run_text`` so large code bodies are never forced through an escaped
        JSON string field — the source of the apply-time ``UnexpectedModelBehavior``.

        Prompt caching (critical for cost control on multi-symbol files):

        - ``system_prompt`` is cached via ``anthropic_cache_instructions`` —
          identical across every symbol, so it's written once and read
          thereafter.
        - ``cache_prefix``, when given, is sent as a leading user content block
          followed by a ``CachePoint()`` marker, then ``user_prompt``. Everything
          up to (and including) the prefix is cached; the per-call ``user_prompt``
          stays dynamic. The sync path passes the full file source here so all
          symbols in a file share one cached prefix.

        Without explicit breakpoints pydantic-ai does NOT cache, which bills the
        full prefix on every call — the regression this guards against.

        Returns the validated Pydantic model plus token usage counters.
        """
        with telemetry.timed("model_call", model=self.full_model_id, kind="generate") as tele:
            if cache_prefix:
                user_input: str | list[Any] = [cache_prefix, _sdk().CachePoint(), user_prompt]
            else:
                user_input = user_prompt

            # Drive the async API on a per-thread loop + per-thread model/client
            # (see ``_thread_holder``) rather than ``run_sync`` or a shared client.
            # run_sync leaks a fresh loop per call (fd exhaustion); a shared async
            # client used across worker-thread loops raises an immediate
            # "Connection error". The holder gives each thread its own loop and
            # its own AsyncAnthropic bound to that loop, reused across calls. The
            # Agent is rebuilt per attempt from the thread's model (cheap — it
            # reuses the cached client). Each attempt holds one global in-flight
            # slot and is retried on 429/529/timeout/connection with backoff.
            def _attempt() -> Any:
                holder = _thread_holder(self._make_thread_model)
                agent = _sdk().Agent(
                    holder.model,
                    output_type=output_type,
                    system_prompt=system_prompt,
                    # pydantic-ai defaults to 1 output retry: a single malformed
                    # structured response (common for large symbols like a 200-line
                    # React component regenerated as one SymbolEdit.source) aborts
                    # the whole apply with "Exceeded maximum output retries (1)".
                    # Our network retry wrapper does NOT cover output-validation
                    # failures, so give pydantic-ai room to re-ask the model.
                    retries=output_retries,
                )
                with _inflight_slot():
                    return holder.loop.run_until_complete(
                        agent.run(
                            user_input,
                            model_settings=_sdk().AnthropicModelSettings(
                                max_tokens=max_tokens,
                                anthropic_cache_instructions=True,
                            ),
                        )
                    )

            result = _run_with_retry(
                _attempt,
                cfg=self._sync_cfg,
                kind="generate",
                model_id=self.full_model_id,
            )
            usage = result.usage
            tele["input_tokens"] = usage.input_tokens
            tele["output_tokens"] = usage.output_tokens
            tele["cache_creation_input_tokens"] = (usage.details or {}).get(
                "cache_creation_input_tokens", 0
            ) or 0
            tele["cache_read_input_tokens"] = (usage.details or {}).get(
                "cache_read_input_tokens", 0
            ) or 0
            return ModelResult(output=result.output, usage=usage)

    def run_text(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
        cache_prefix: str | None = None,
    ) -> ModelResult:
        """Run the model in plain-text mode and return its raw TEXT output.

        Free-text output mode (``output_type=str``): the model replies with
        plain text and ``result.output`` is the raw string. Used by callers
        that want prose (e.g. the digest narrative) rather than structured
        output — no JSON schema that a long body could fail to satisfy.

        Delegates to ``run`` so prompt caching, the per-thread loop/client, the
        in-flight governor, and network retries are all shared with the
        structured path — only the output mode differs. ``result.output`` is the
        raw string.
        """
        return self.run(
            str,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            max_tokens=max_tokens,
            cache_prefix=cache_prefix,
        )

    def count_tokens(self, system_prompt: str, user_prompt: str) -> int:
        """Return the number of input tokens via the Anthropic count_tokens API."""
        # The Anthropic API rejects empty or whitespace-only user message
        # content ("user messages must have non-empty content" / "text content
        # blocks must contain non-whitespace text"), but the plan-time cost
        # preview intentionally passes an empty user_prompt to measure only the
        # cached prefix (system + cached context). Substitute a minimal
        # non-whitespace placeholder so the request is accepted; the one-token
        # delta is negligible for cost estimation.
        payload: dict[str, Any] = {
            "model": self._anthropic_model,
            "messages": [{"role": "user", "content": user_prompt if user_prompt.strip() else "."}],
        }
        if system_prompt:
            payload["system"] = [{"type": "text", "text": system_prompt}]
        with telemetry.timed("model_call", model=self.full_model_id, kind="count_tokens") as tele:
            resp = _run_with_retry(
                lambda: self._raw_client.messages.count_tokens(**payload),
                cfg=self._sync_cfg,
                kind="count_tokens",
                model_id=self.full_model_id,
            )
            tele["input_tokens"] = resp.input_tokens
            return resp.input_tokens


def make_client(model_id: str, *, sync_cfg: Sync | None = None) -> TrieClient:
    """Construct a ``TrieClient`` from a ``provider/model`` id string.

    Only ``anthropic/`` is supported in v0.1.
    """
    if "/" not in model_id:
        raise ValueError(f"model_id must be of the form 'provider/model', got {model_id!r}")
    provider, _ = model_id.split("/", 1)
    if provider == "anthropic":
        return TrieClient(model_id, sync_cfg=sync_cfg)
    raise NotImplementedError(
        f"provider {provider!r} not implemented in v0.1. "
        "Use 'anthropic/<model>' or extend trie.models.make_client."
    )
