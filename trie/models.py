from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import Any

from anthropic import (
    Anthropic,
    APIStatusError,
    APITimeoutError,
    InternalServerError,
    RateLimitError,
)
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.usage import Usage

from trie import telemetry
from trie.config import Sync

# ---------------------------------------------------------------------------
# Structured output models — every LLM call returns one of these.
# No delimiter-parsing, no "Output:\n```python\n..." instructions.
# ---------------------------------------------------------------------------


class SectionBody(BaseModel):
    """Triefact documentation body for a single symbol."""

    body: str


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
    """Batch filter decisions for all callee→caller pairs."""

    decisions: list[CallerDecision]


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
    return isinstance(exc, (RateLimitError, InternalServerError, APITimeoutError))


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
    while True:
        try:
            return fn()
        except BaseException as exc:
            if not _is_retryable(exc) or attempt >= cfg.max_retries:
                raise
            if isinstance(exc, RateLimitError):
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
                reason = "overloaded" if isinstance(exc, InternalServerError) else "timeout"
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
            sleep(delay)
            attempt += 1


T = Any  # TypeVar placeholder for the inner retry helper


# ---------------------------------------------------------------------------
# Client — Pydantic AI agent factory with a count_tokens side-channel
# ---------------------------------------------------------------------------

# Map from trie's "provider/model" config format to pydantic_ai's "provider:model" format.
_MODEL_ID_ALIASES: dict[str, str] = {
    "anthropic/claude-sonnet-4-6": "anthropic:claude-sonnet-4-20250514",
    "anthropic/claude-haiku-4-5-20251001": "anthropic:claude-haiku-4-5-20251001",
    "anthropic/claude-opus-4-7": "anthropic:claude-opus-4-7",
}


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
    ``system_prompt``, calls ``agent.run_sync(user_prompt)``, and returns a
    ``ModelResult`` with the structured output and token usage.

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
        self._pai_model = _pydantic_ai_model_id(full_model_id)
        self._anthropic_model = _anthropic_model_name(full_model_id)
        self._sync_cfg = sync_cfg or Sync()
        self._raw_client = Anthropic(max_retries=0)

    def run(
        self,
        output_type: type[BaseModel],
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
    ) -> ModelResult:
        """Run an agent with structured output.

        The ``system_prompt`` is set on the agent (eligible for Anthropic
        prompt caching). The ``user_prompt`` is sent as the user message.
        Returns the validated Pydantic model plus token usage counters.
        """
        with telemetry.timed("model_call", model=self.full_model_id, kind="generate") as tele:
            agent = Agent(
                self._pai_model,
                output_type=output_type,
                system_prompt=system_prompt,
            )
            result = agent.run_sync(user_prompt, model_settings={"max_tokens": max_tokens})
            usage = result.usage()
            tele["input_tokens"] = usage.input_tokens
            tele["output_tokens"] = usage.output_tokens
            tele["cache_creation_input_tokens"] = (usage.details or {}).get(
                "cache_creation_input_tokens", 0
            ) or 0
            tele["cache_read_input_tokens"] = (usage.details or {}).get(
                "cache_read_input_tokens", 0
            ) or 0
            return ModelResult(output=result.output, usage=usage)

    def count_tokens(self, system_prompt: str, user_prompt: str) -> int:
        """Return the number of input tokens via the Anthropic count_tokens API."""
        payload: dict[str, Any] = {
            "model": self._anthropic_model,
            "messages": [{"role": "user", "content": user_prompt}],
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
