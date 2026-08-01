"""Retry-on-rate-limit behaviour of `AnthropicClient`.

The contract under test:
  - 429 with a `retry-after` header → wait exactly that many seconds.
  - 429 without a header → exponential backoff with jitter (bounded by cap).
  - 5xx including 529 overloaded → exponential backoff with jitter.
  - Timeouts → exponential backoff with jitter.
  - Non-retryable 4xx (auth, bad request) → propagate immediately, no sleep.
  - After `max_retries` attempts the original exception propagates.

The retry loop is wrapped around both `messages.create` and `messages.count_tokens`
so the same protections apply to plan-time token counting and sync-time generation.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from types import SimpleNamespace
from unittest.mock import MagicMock

import httpx
import pytest
from anthropic import (
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    InternalServerError,
    RateLimitError,
)

from trie.config import Sync
from trie.models import (
    TrieClient,
    _backoff_delay,
    _is_retryable,
    _retry_after_seconds,
    _run_with_retry,
)


def _fake_response(status: int, *, retry_after: str | None = None) -> httpx.Response:
    """Build an httpx.Response that the SDK's exception classes can wrap."""
    request = httpx.Request("POST", "https://api.anthropic.com/v1/messages")
    headers = {}
    if retry_after is not None:
        headers["retry-after"] = retry_after
    return httpx.Response(status, request=request, headers=headers)


def _rate_limit(retry_after: str | None = None) -> RateLimitError:
    return RateLimitError(
        message="rate limited",
        response=_fake_response(429, retry_after=retry_after),
        body=None,
    )


def _overloaded() -> InternalServerError:
    return InternalServerError(
        message="overloaded",
        response=_fake_response(529),
        body=None,
    )


def _auth_error() -> AuthenticationError:
    return AuthenticationError(
        message="bad key",
        response=_fake_response(401),
        body=None,
    )


@dataclass
class _Recorder:
    """Sleep + RNG stand-ins that record their calls without actually waiting."""

    sleeps: list[float] = field(default_factory=list)

    def sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)


def _frozen_rng(seed: int = 0) -> random.Random:
    return random.Random(seed)


# --- classification helpers ------------------------------------------------


def test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout():
    assert _is_retryable(_rate_limit())
    assert _is_retryable(_overloaded())
    assert _is_retryable(APITimeoutError(httpx.Request("POST", "https://x")))


def test_is_retryable_picks_up_connection_errors():
    # Transient network failures (DNS lookup failure, connection refused) surface
    # as APIConnectionError and must be retried, not crash the whole sync.
    exc = APIConnectionError(request=httpx.Request("POST", "https://x"))
    assert _is_retryable(exc)


def test_is_retryable_rejects_auth_and_other_4xx():
    assert not _is_retryable(_auth_error())
    assert not _is_retryable(ValueError("not an API error"))


def test_is_retryable_unwraps_pydantic_ai_model_api_error():
    """pydantic-ai wraps the underlying anthropic exception in ModelAPIError.

    A transient connection drop therefore arrives as ModelAPIError, which does
    NOT isinstance-match the anthropic types. Both the message-based match and the
    __cause__-chain walk must recognise it as retryable, otherwise the whole sync
    surfaces 'Connection error.' immediately instead of retrying (the regression
    that caused every large file to fail under parallel sync)."""
    from pydantic_ai.exceptions import ModelAPIError

    # (a) bare wrapper with a connection-error message
    assert _is_retryable(ModelAPIError("claude", "Connection error."))
    # (b) wrapper whose __cause__ is a retryable anthropic exception
    cause = APIConnectionError(request=httpx.Request("POST", "https://x"))
    wrapped = ModelAPIError("claude", "upstream failed")
    wrapped.__cause__ = cause
    assert _is_retryable(wrapped)
    # (c) a wrapper for a genuinely non-transient error stays non-retryable
    assert not _is_retryable(ModelAPIError("claude", "invalid request: bad schema"))


def test_per_thread_models_are_distinct_and_reused():
    """Each worker thread must get its own AnthropicModel/AsyncAnthropic (bound to
    its own event loop) so a shared client is never used across loops — but the
    same thread reuses its client across calls so fds don't leak."""
    import threading

    client = TrieClient("anthropic/claude-sonnet-4-6")
    models: dict[int, list[int]] = {}

    def worker() -> None:
        tid = threading.get_ident()
        # Two builds on the same thread go through the holder cache.
        from trie.models import _thread_holder

        h1 = _thread_holder(client._make_thread_model)
        h2 = _thread_holder(client._make_thread_model)
        models[tid] = [id(h1.model), id(h2.model)]

    threads = [threading.Thread(target=worker) for _ in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # Same thread => same cached model (reused).
    for ids in models.values():
        assert ids[0] == ids[1]
    # Different threads => different models (not shared across loops).
    first_per_thread = [ids[0] for ids in models.values()]
    assert len(set(first_per_thread)) == len(first_per_thread)


def test_retry_after_reads_header_when_present():
    assert _retry_after_seconds(_rate_limit(retry_after="3")) == 3.0
    assert _retry_after_seconds(_rate_limit(retry_after="0.5")) == 0.5


def test_retry_after_none_when_header_missing_or_unparseable():
    assert _retry_after_seconds(_rate_limit(retry_after=None)) is None
    assert _retry_after_seconds(_rate_limit(retry_after="not-a-number")) is None


def test_backoff_delay_within_cap():
    rng = _frozen_rng()
    cfg = Sync(retry_base_delay_seconds=1.0, retry_cap_seconds=10.0)
    # attempt=10 would naively exceed cap; the function must clamp the upper bound.
    for _ in range(50):
        d = _backoff_delay(
            attempt=10, base=cfg.retry_base_delay_seconds, cap=cfg.retry_cap_seconds, rng=rng
        )
        assert 0.0 <= d <= cfg.retry_cap_seconds


# --- the loop itself -------------------------------------------------------


def test_run_with_retry_honours_retry_after_exactly():
    cfg = Sync(max_retries=3, retry_base_delay_seconds=99.0, retry_cap_seconds=99.0)
    rec = _Recorder()
    attempts = {"n": 0}

    def call():
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise _rate_limit(retry_after="7")
        return "ok"

    out = _run_with_retry(
        call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
    )
    assert out == "ok"
    assert rec.sleeps == [7.0], (
        "retry-after must be passed through verbatim, not run through jitter"
    )
    assert attempts["n"] == 2


def test_run_with_retry_caps_retry_after():
    """An over-the-top retry-after (server bug, malicious header) still respects our cap.

    Without this clamp a misbehaving upstream could pin a worker for hours."""
    cfg = Sync(max_retries=3, retry_base_delay_seconds=1.0, retry_cap_seconds=2.0)
    rec = _Recorder()
    attempts = {"n": 0}

    def call():
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise _rate_limit(retry_after="9999")
        return "ok"

    _run_with_retry(
        call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
    )
    assert rec.sleeps == [2.0]


def test_run_with_retry_uses_backoff_when_no_retry_after():
    cfg = Sync(max_retries=3, retry_base_delay_seconds=1.0, retry_cap_seconds=4.0)
    rec = _Recorder()
    attempts = {"n": 0}

    def call():
        attempts["n"] += 1
        if attempts["n"] < 3:
            raise _rate_limit()  # no header
        return "ok"

    _run_with_retry(
        call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
    )
    assert len(rec.sleeps) == 2
    for s in rec.sleeps:
        assert 0.0 <= s <= cfg.retry_cap_seconds


def test_run_with_retry_backs_off_on_overloaded():
    cfg = Sync(max_retries=2, retry_base_delay_seconds=0.5, retry_cap_seconds=5.0)
    rec = _Recorder()
    attempts = {"n": 0}

    def call():
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise _overloaded()
        return "ok"

    _run_with_retry(
        call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
    )
    assert len(rec.sleeps) == 1
    assert 0.0 <= rec.sleeps[0] <= cfg.retry_cap_seconds


def test_run_with_retry_gives_up_after_max_retries():
    cfg = Sync(max_retries=2, retry_base_delay_seconds=0.1, retry_cap_seconds=1.0)
    rec = _Recorder()

    def call():
        raise _rate_limit(retry_after="0")

    with pytest.raises(RateLimitError):
        _run_with_retry(
            call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
        )
    # max_retries=2 means 2 retries on top of the initial attempt = 3 calls, 2 sleeps.
    assert len(rec.sleeps) == 2


def test_run_with_retry_propagates_non_retryable_immediately():
    cfg = Sync(max_retries=5, retry_base_delay_seconds=0.1, retry_cap_seconds=1.0)
    rec = _Recorder()

    def call():
        raise _auth_error()

    with pytest.raises(AuthenticationError):
        _run_with_retry(
            call, cfg=cfg, kind="generate", model_id="m", sleep=rec.sleep, rng=_frozen_rng()
        )
    assert rec.sleeps == [], "non-retryable errors must not trigger any backoff sleep"


# --- end-to-end through TrieClient -----------------------------------------


def test_count_tokens_retries_on_rate_limit():
    """Same retry envelope applies to count_tokens (plan-time path)."""
    mock_anth = MagicMock()
    success_resp = SimpleNamespace(input_tokens=123)
    mock_anth.messages.count_tokens.side_effect = [_rate_limit(retry_after="0"), success_resp]

    client = TrieClient(
        "anthropic/claude-sonnet-4-6",
        sync_cfg=Sync(max_retries=2, retry_base_delay_seconds=0.0, retry_cap_seconds=0.0),
    )
    client._raw_client = mock_anth
    assert client.count_tokens(system_prompt="sys", user_prompt="r") == 123
    assert mock_anth.messages.count_tokens.call_count == 2


def test_trie_client_disables_sdk_internal_retries(monkeypatch: pytest.MonkeyPatch):
    """When constructing the underlying Anthropic SDK client without an explicit
    `client=` argument, we must pass `max_retries=0` so the SDK doesn't add its own
    retry layer on top of ours. Otherwise wall-clock and telemetry both lie."""
    captured: dict = {}

    class FakeAnthropic:
        def __init__(self, *args, **kwargs):
            captured["kwargs"] = kwargs

    from trie.models import _sdk

    monkeypatch.setattr(_sdk(), "Anthropic", FakeAnthropic)
    TrieClient("anthropic/claude-sonnet-4-6")

    assert captured["kwargs"].get("max_retries") == 0


def test_retry_total_seconds_bounds_the_loop(monkeypatch):
    """A wedged connection must not retry past the wall-clock budget even when
    attempts remain — 8 x 120s-timeout attempts looked like a 20-minute hang."""
    from trie.config import Sync
    from trie.models import _run_with_retry

    cfg = Sync(max_retries=100, retry_base_delay_seconds=0.0, retry_total_seconds=10.0)

    clock = {"now": 0.0}
    monkeypatch.setattr("trie.models.time.monotonic", lambda: clock["now"])

    calls = {"n": 0}

    def always_connection_error():
        calls["n"] += 1
        clock["now"] += 6.0  # each attempt burns 6s of wall clock
        raise APITimeoutError(request=httpx.Request("POST", "https://x"))

    with pytest.raises(APITimeoutError):
        _run_with_retry(
            always_connection_error,
            cfg=cfg,
            kind="generate",
            model_id="m",
            sleep=lambda _s: None,
        )
    # 6s, 12s -> budget (10s) exceeded on the second failure: exactly 2 calls.
    assert calls["n"] == 2


def test_retry_total_seconds_zero_is_unbounded(monkeypatch):
    from trie.config import Sync
    from trie.models import _run_with_retry

    cfg = Sync(max_retries=3, retry_base_delay_seconds=0.0, retry_total_seconds=0.0)
    calls = {"n": 0}

    def fail_then_succeed():
        calls["n"] += 1
        if calls["n"] < 4:
            raise APITimeoutError(request=httpx.Request("POST", "https://x"))
        return "ok"

    assert (
        _run_with_retry(
            fail_then_succeed, cfg=cfg, kind="generate", model_id="m", sleep=lambda _s: None
        )
        == "ok"
    )
    assert calls["n"] == 4
