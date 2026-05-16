from __future__ import annotations

import random
import time
from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol, TypeVar

from anthropic import (
    Anthropic,
    APIStatusError,
    APITimeoutError,
    InternalServerError,
    RateLimitError,
)

from trie import telemetry
from trie.config import Sync

T = TypeVar("T")


@dataclass(frozen=True)
class GenerationRequest:
    """A single LLM call. `cached_context` is intended to be reused across calls within
    the same file via Anthropic prompt caching; `request` is the small per-symbol delta."""

    system_prompt: str
    cached_context: str
    request: str
    max_tokens: int = 1024


@dataclass(frozen=True)
class GenerationResponse:
    text: str
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


class ModelClient(Protocol):
    model_id: str  # bare model name passed to the provider API (e.g. "claude-sonnet-4-6")
    full_model_id: str  # "provider/model" string used for telemetry + pricing lookups

    def generate(self, req: GenerationRequest) -> GenerationResponse: ...

    def count_tokens(self, req: GenerationRequest) -> int: ...


def _retry_after_seconds(exc: APIStatusError) -> float | None:
    """Read the `retry-after` header from a 429 response, if present.

    The header carries seconds as an integer string. Returns None when the header
    is absent or unparseable — the caller falls back to exponential backoff.
    """
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
    """Classify which exceptions our retry loop should re-attempt.

    - `RateLimitError` (429): always retryable.
    - `InternalServerError` (5xx including 529 overloaded): retryable.
    - `APITimeoutError`: network timeout, retryable.
    - Everything else (4xx auth/permission/bad-request): not retryable; propagate.
    """
    return isinstance(exc, (RateLimitError, InternalServerError, APITimeoutError))


def _backoff_delay(
    *,
    attempt: int,
    base: float,
    cap: float,
    rng: random.Random,
) -> float:
    """Exponential backoff with full jitter.

    `attempt` is 0-indexed (first retry is attempt=0). Formula: uniform(0, min(cap,
    base * 2**attempt)). Full jitter avoids the thundering-herd pattern when many
    concurrent workers all back off at once.
    """
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
    """Invoke `fn`, retrying on rate-limit / overloaded / timeout responses.

    Honours `retry-after` headers on 429 exactly; falls back to exponential backoff
    with full jitter for 429s without a header and for 5xx/timeout responses. Each
    retry emits a `model_call_retry` telemetry event with the attempt number, the
    sleep duration, and the exception class so backoff behaviour is observable.

    Stops after `cfg.max_retries` attempts (so total tries = max_retries + 1) and
    re-raises the last exception.
    """
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


class AnthropicClient:
    def __init__(
        self,
        model_id: str,
        *,
        client: Anthropic | None = None,
        sync_cfg: Sync | None = None,
        full_model_id: str | None = None,
    ) -> None:
        # `max_retries=0` disables the SDK's own retry loop. We run our own on top so
        # each attempt is visible in telemetry; doubling up would silently inflate
        # wall-clock without surfacing the cause.
        #
        # `model_id` is the bare name sent to the Anthropic API (e.g.
        # `"claude-sonnet-4-6"`). `full_model_id` retains the `"anthropic/..."` prefix
        # used by the pricing table and stamped into telemetry. We accept it as an
        # optional kwarg so direct constructions (tests, ad-hoc scripts) without going
        # through `make_client` still produce coherent identifiers.
        self.model_id = model_id
        self.full_model_id = full_model_id or f"anthropic/{model_id}"
        self._client = client or Anthropic(max_retries=0)
        self._sync_cfg = sync_cfg or Sync()

    def _payload(self, req: GenerationRequest) -> dict:
        content: list[dict] = [
            {
                "type": "text",
                "text": req.cached_context,
                "cache_control": {"type": "ephemeral"},
            },
        ]
        # Anthropic rejects empty text content blocks. `build_plan` calls count_tokens
        # with `request=""` to get just the cached-prefix size, so skip the block when
        # it's empty rather than sending an invalid payload.
        if req.request:
            content.append({"type": "text", "text": req.request})
        return {
            "model": self.model_id,
            "system": [
                {
                    "type": "text",
                    "text": req.system_prompt,
                    "cache_control": {"type": "ephemeral"},
                },
            ],
            "messages": [{"role": "user", "content": content}],
        }

    def generate(self, req: GenerationRequest) -> GenerationResponse:
        with telemetry.timed("model_call", model=self.full_model_id, kind="generate") as tele:
            resp = _run_with_retry(
                lambda: self._client.messages.create(
                    max_tokens=req.max_tokens, **self._payload(req)
                ),
                cfg=self._sync_cfg,
                kind="generate",
                model_id=self.full_model_id,
            )
            text = "".join(block.text for block in resp.content if block.type == "text")
            usage = resp.usage
            tele["input_tokens"] = usage.input_tokens
            tele["output_tokens"] = usage.output_tokens
            tele["cache_creation_input_tokens"] = (
                getattr(usage, "cache_creation_input_tokens", 0) or 0
            )
            tele["cache_read_input_tokens"] = getattr(usage, "cache_read_input_tokens", 0) or 0
            return GenerationResponse(
                text=text,
                input_tokens=usage.input_tokens,
                output_tokens=usage.output_tokens,
                cache_creation_input_tokens=getattr(usage, "cache_creation_input_tokens", 0) or 0,
                cache_read_input_tokens=getattr(usage, "cache_read_input_tokens", 0) or 0,
            )

    def count_tokens(self, req: GenerationRequest) -> int:
        """Return the number of input tokens for `req` per the Anthropic count_tokens API.

        Free, but rate-limited separately from message creation. Counts the same payload
        the generator would actually send (system + cached context + per-symbol request),
        so the result reflects real prompt size rather than a char-count heuristic.
        """
        with telemetry.timed("model_call", model=self.full_model_id, kind="count_tokens") as tele:
            resp = _run_with_retry(
                lambda: self._client.messages.count_tokens(**self._payload(req)),
                cfg=self._sync_cfg,
                kind="count_tokens",
                model_id=self.full_model_id,
            )
            tele["input_tokens"] = resp.input_tokens
            return resp.input_tokens


def make_client(model_id: str, *, sync_cfg: Sync | None = None) -> ModelClient:
    """Construct a model client from a "provider/model" id string.

    v0.1 only supports the `anthropic/` provider; other providers (deepseek, qwen via
    OpenAI-compatible base URLs) are deferred.

    `sync_cfg` carries retry knobs (max_retries, backoff bounds). When omitted, the
    client falls back to the `Sync()` dataclass defaults — useful for one-off calls
    that aren't part of a configured project.
    """
    if "/" not in model_id:
        raise ValueError(f"model_id must be of the form 'provider/model', got {model_id!r}")
    provider, model_name = model_id.split("/", 1)
    if provider == "anthropic":
        return AnthropicClient(model_name, sync_cfg=sync_cfg, full_model_id=model_id)
    raise NotImplementedError(
        f"provider {provider!r} not implemented in v0.1. "
        "Use 'anthropic/<model>' or extend trie.models.make_client."
    )
